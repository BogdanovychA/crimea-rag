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

# @cl.password_auth_callback
# def auth_callback(username: str, password: str):
#     # Fetch the user matching username from your database
#     # and compare the hashed password with the value stored in the database
#     if (username, password) == ("admin", "admin"):
#         return cl.User(
#             identifier="admin", metadata={"role": "admin", "provider": "credentials"}
#         )
#     else:
#         return None


@cl.on_chat_start
async def start():

    lang = utils.get_lang(context.session)

    #  Ін'єкція для російськомовних браузерів :)
    lang_list = ["ru", "uk"] if lang == "ru" else [lang]

    fluent = FluentManager(
        locales=lang_list,
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

    box = cl.user_session.get("box")
    content = message.content

    if not content or not isinstance(content, str):
        answer = box.fluent.get("only-text-supported")
        await cl.Message(content=answer).send()
        return

    max_query_length = embed.max_query_length
    if len(content) > max_query_length:
        content = content[:max_query_length]
        warning = box.fluent.get("request-too-large", max_query_length=max_query_length)
        await cl.Message(content=warning).send()

    try:
        # Пошук у базі знань через крок chainlit
        async with cl.Step(name=box.fluent.get("kb-search-step-name")) as step:
            docs = await cl.make_async(box.retriever.invoke)(content)
            step.output = box.fluent.get("kb-search-step-output", count=len(docs))

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
                clean_name = box.fluent.get("home-page")

            url = f"https://crimea-is-ukraine.org/{source.replace('index.md', '')}"

            if clean_name not in seen_sources:
                seen_sources.add(clean_name)
                elements.append(
                    cl.Text(
                        name=f"📎 {clean_name}",
                        content=box.fluent.get(
                            "source-element-content",
                            url=url,
                            content=doc.page_content,
                        ),
                        display="page",
                    )
                )
                source_links.append(f"[{clean_name}]({url})")

        # Додаємо список посилань в кінець повідомлення
        if source_links:
            sources_title = box.fluent.get("sources-title")
            msg.content += f"\n\n**{sources_title}:**\n" + "\n".join(
                f"* {link}" for link in source_links
            )

        msg.elements = elements

        await msg.update()

    except Exception as e:
        logger.exception("Unexpected error: %s", e)
        text = box.fluent.get("unexpected-error")
        await cl.Message(content=text).send()
