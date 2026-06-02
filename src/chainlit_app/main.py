# -*- coding: utf-8 -*-

import logging

import chainlit as cl
from chainlit.context import context
from fluent_manager import FluentManager
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from abstract.embed_manager import EmbedManager
from abstract.llm_manager import LLMManager
from chainlit_app.utils import utils
from chainlit_app.utils.models import PandorasBox
from config import app, server
from core.langchain_manager import format_docs
from models.llm import LLMName

logging.basicConfig(
    level=server.settings.logging_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

LLMManager.register(LLMName.LAPA, ChatOpenAI)


embed = EmbedManager()
llm = LLMManager()


@cl.on_chat_start
async def start():

    lang = utils.get_lang(context.session)

    fluent = FluentManager(
        locales=[lang],
        locales_path=str(app.settings.locales_dir),
        default_locale=app.settings.default_locale,
    )

    prompt = ChatPromptTemplate.from_template(fluent.get("system-prompt"))

    user_chain = prompt | llm.manager | StrOutputParser()

    box = PandorasBox(
        retriever=embed.get_retriever(),
        chain=user_chain,
        lang=lang,
        fluent=fluent,
    )

    cl.user_session.set("box", box)

    await cl.Message(
        content=box.fluent.get("hello-text", llm_name=llm.name, llm_model=llm.model)
    ).send()


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
                        display="page",
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
