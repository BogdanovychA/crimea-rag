# -*- coding: utf-8 -*-

import asyncio
import logging

import chainlit as cl

from abstract.embed_manager import EmbedManager
from abstract.llm_manager import LLMManager
from chainlit_app.utils.models import PandorasBox
from config import server
from core.langchain_manager import get_rag_chain

logging.basicConfig(
    level=server.settings.logging_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

system_prompt = """
Ти — помічник-знавець бази знань. Твоє завдання — відповідати на запитання,
спираючись виключно на наданий контекст. Якщо в контексті немає відповіді,
так і скажи, що не знаєш, не намагайся вигадувати відповідь.\n\n
Також надай посилання на джерело інформації.\n
Коли надаєш посилання на джерело:\n
* додай префікс: "https://crimea-is-ukraine.org/"\n
* видали суфікс: "index.md".\n
Джерело має виглядати як посилання на сайт.\n\n
Контекст для аналізу:\n
{context}\n\n
Запитання користувача:\n{question}
"""

embed_manager = EmbedManager()
llm_manager = LLMManager.get_manager()


@cl.on_chat_start
async def start():

    box = PandorasBox(
        rag_chain=get_rag_chain(
            system_prompt=system_prompt,
            retriever=embed_manager.get_retriever(5),
            llm=llm_manager,
        ),
    )

    cl.user_session.set("box", box)

    hello_text = """
    Привіт! Я штучний інтелект. Можеш поставити мені будь-яке запитання
    щодо контенту сайту "Крим - це Україна" (https://crimea-is-ukraine.org)
    """

    await cl.Message(content=hello_text).send()


@cl.step(type="tool")
async def rag_search(request: str):
    await asyncio.sleep(3)
    return request


@cl.on_message
async def main(message: cl.Message):

    content = message.content

    if not content or not isinstance(content, str):
        answer = "Я вмію працювати лише з текстом"
        await cl.Message(content=answer).send()
        return

    box = cl.user_session.get("box")

    try:
        stream = box.rag_chain.astream(content)

        msg = cl.Message(content="")
        await msg.send()

        async for chunk in stream:
            await asyncio.sleep(0.05)
            await msg.stream_token(chunk)

        await msg.update()

    except Exception as e:
        logger.exception("Unexpected error: %s", e)
        text = "Неочікувана помилка. Повідомте розробника."
        await cl.Message(content=text).send()
