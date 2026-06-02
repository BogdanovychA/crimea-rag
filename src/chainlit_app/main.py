# -*- coding: utf-8 -*-

import logging

import chainlit as cl
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from abstract.embed_manager import EmbedManager
from abstract.llm_manager import LLMManager
from chainlit_app.utils.models import PandorasBox
from config import app, llm, server
from core.langchain_manager import format_docs

logging.basicConfig(
    level=server.settings.logging_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

system_prompt = """
Ти — помічник-знавець бази знань. Твоє завдання — відповідати на запитання, спираючись виключно на наданий контекст. Якщо в контексті немає відповіді, так і скажи, що не знаєш, не намагайся вигадувати відповідь.

Контекст для аналізу:
{context}

Запитання користувача:
{question}
"""

prompt = ChatPromptTemplate.from_template(system_prompt)

embed_manager = EmbedManager()
llm_manager = LLMManager.get_manager()


@cl.on_chat_start
async def start():

    user_chain = prompt | llm_manager | StrOutputParser()

    box = PandorasBox(
        retriever=embed_manager.get_retriever(),
        chain=user_chain,
    )

    cl.user_session.set("box", box)

    hello_text = f"""Привіт!
Я - штучний інтелект від інференс провайдера "{app.settings.llm_name}", модель: "{llm.settings.model}".
Можеш поставити мені будь-яке запитання щодо контенту сайту ["Крим - це Україна"](https://crimea-is-ukraine.org).
    """

    await cl.Message(content=hello_text).send()


@cl.on_message
async def main(message: cl.Message):

    content = message.content

    if not content or not isinstance(content, str):
        answer = "Я вмію працювати лише з текстом"
        await cl.Message(content=answer).send()
        return

    box = cl.user_session.get("box")

    try:
        # Пошук у базі знань через крок chainlit
        async with cl.Step(name="Пошук у базі знань") as step:
            docs = await cl.make_async(box.retriever.invoke)(content)
            step.output = f"Знайдено {len(docs)} релевантних фрагментів у базі знань."

        # Формування контексту
        formatted_context = format_docs(docs)

        stream = box.chain.astream({"context": formatted_context, "question": content})

        msg = cl.Message(content="")
        await msg.send()

        async for chunk in stream:
            await msg.stream_token(chunk)

        # Створення інтерактивних джерел для інтерфейсу Chainlit
        elements = []
        seen_sources = set()
        source_links = []

        for doc in docs:
            source = doc.metadata.get("source", "")
            if not source:
                continue
            clean_name = source.replace("index.md", "").strip("/")
            if not clean_name:
                clean_name = "Головна"

            url = f"https://crimea-is-ukraine.org/{source.replace('index.md', '')}"

            if clean_name not in seen_sources:
                seen_sources.add(clean_name)
                elements.append(
                    cl.Text(
                        name=f"📎 {clean_name}",
                        content=f"Джерело: {url}\n\nФрагмент тексту:\n{doc.page_content}",
                        display="side",
                    )
                )
                source_links.append(f"[{clean_name}]({url})")

        # Додаємо список посилань в кінець повідомлення
        if source_links:
            msg.content += "\n\n**Джерела:**\n" + "\n".join(
                f"* {link}" for link in source_links
            )

        msg.elements = elements

        await msg.update()

    except Exception as e:
        logger.exception("Unexpected error: %s", e)
        text = "Неочікувана помилка. Повідомте розробника."
        await cl.Message(content=text).send()
