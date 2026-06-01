# -*- coding: utf-8 -*-

import asyncio
import logging

import chainlit as cl

from chainlit_app.utils.models import PandorasBox
from config import lapathoniia, server
from core.lapathoniia_manager import LapathoniiaManager

logging.basicConfig(
    level=server.settings.logging_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


@cl.on_chat_start
async def start():

    system_prompt = """
    Ти — помічник-знавець бази знань. Твоє завдання — відповідати на запитання,
    спираючись виключно на наданий контекст. Якщо в контексті немає відповіді,
    так і скажи, що не знаєш, не намагайся вигадувати відповідь.\n\n
    Контекст для аналізу:\n
    {context}\n\n
    Запитання користувача: {question}
    """

    box = PandorasBox(
        l9a=LapathoniiaManager(**lapathoniia.settings.model_dump()),
        system_prompt=system_prompt,
    )

    cl.user_session.set("box", box)

    hello_text = """
    Привіт! Я штучний інтелект. Можеш поставити мені будь-яке питання
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

    request = await rag_search(content)

    msg = cl.Message(content="")
    await msg.send()

    stream = box.l9a.query(box.system_prompt, request)

    async for chunk in stream:
        await asyncio.sleep(0.05)
        await msg.stream_token(chunk)

    await msg.update()
