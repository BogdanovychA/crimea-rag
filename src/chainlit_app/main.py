# -*- coding: utf-8 -*-

import logging

import chainlit as cl
from chainlit.context import context
from fluent_manager import FluentManager
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from abstract.embed_manager import EmbedManager
from abstract.llm_manager import LLMManager
from chainlit_app import init_app
from chainlit_app.utils import utils
from chainlit_app.utils.models import ChatHistoryKey, ChatHistoryValue, PandorasBox
from config import app, server
from core.langchain_manager import format_docs

logging.basicConfig(
    level=server.settings.logging_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

init_app.register_llm_managers()

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

    # Ін'єкція для російськомовних браузерів :)
    lang_list = ["ru", "uk"] if lang == "ru" else [lang]

    fluent = FluentManager(
        locales=lang_list,
        locales_path=str(app.settings.locales_dir),
        default_locale=app.settings.default_locale,
    )

    #  Ін'єкція для російськомовних браузерів :)
    if lang == "ru":
        hello_text_prefix = fluent.get("ru-browser")
        hello_text_suffix = fluent.get("glory-to-ukraine")
        system_prompt_prefix = fluent.get("putin-khuilo")
    else:
        hello_text_prefix = ""
        hello_text_suffix = ""
        system_prompt_prefix = ""

    global_system_prompt_text = system_prompt_prefix + fluent.get(
        "global-system-prompt"
    )
    global_user_prompt_text = fluent.get("global-user-prompt")

    global_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", global_system_prompt_text),
            MessagesPlaceholder(variable_name="formatted_history"),
            ("human", global_user_prompt_text),
        ]
    )

    user_chain = global_prompt | llm.manager | StrOutputParser()

    rephrase_system_prompt_text = fluent.get("rephrase-system-promp")
    rephrase_user_prompt_text = fluent.get("rephrase-user-prompt")
    rephrase_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", rephrase_system_prompt_text),
            MessagesPlaceholder(variable_name="formatted_history"),
            ("human", rephrase_user_prompt_text),
        ]
    )

    rephrase_chain = rephrase_prompt | llm.manager | StrOutputParser()

    box = PandorasBox(
        retriever=embed.get_retriever(),
        chain=user_chain,
        lang=lang,
        fluent=fluent,
        chat_history=[],
        rephrase_chain=rephrase_chain,
    )

    cl.user_session.set("box", box)

    hello_text = box.fluent.get("hello-text", llm_name=llm.name, llm_model=llm.model)
    await cl.Message(content=hello_text_prefix + hello_text + hello_text_suffix).send()


@cl.on_message
async def main(message: cl.Message):

    box = cl.user_session.get("box")
    content = message.content

    if not content or not isinstance(content, str):
        answer = box.fluent.get("only-text-supported")
        await cl.Message(content=answer).send()
        return

    # Обрізаємо запит, якщо завеликий.
    max_query_length = embed.max_query_length
    if len(content) > max_query_length:
        content = content[:max_query_length]
        warning = box.fluent.get("request-too-large", max_query_length=max_query_length)
        await cl.Message(content=warning).send()

    formatted_history = []
    for element in box.chat_history:
        new_element = None
        if element[ChatHistoryKey.ROLE] == ChatHistoryValue.USER:
            new_element = HumanMessage(content=element[ChatHistoryKey.CONTENT])
        elif element[ChatHistoryKey.ROLE] == ChatHistoryValue.AI:
            new_element = AIMessage(content=element[ChatHistoryKey.CONTENT])
        if new_element is not None:
            formatted_history.append(new_element)

    if formatted_history:
        async with cl.Step(name=box.fluent.get("contextualizing-query")) as step:
            search_query = await box.rephrase_chain.ainvoke(
                {"formatted_history": formatted_history, "question": content}
            )
            step.output = box.fluent.get("standalone-query", search_query=search_query)
    else:
        search_query = content

    # Обрізаємо уточнений запит, якщо завеликий.
    search_query = search_query[:max_query_length]

    try:
        # Пошук у базі знань через крок chainlit
        async with cl.Step(name=box.fluent.get("kb-search-step-name")) as step:
            docs = await cl.make_async(box.retriever.invoke)(search_query)
            step.output = box.fluent.get("kb-search-step-output", count=len(docs))

        # Формування контексту
        formatted_context = format_docs(docs)

        stream = box.chain.astream(
            {
                "context": formatted_context,
                "formatted_history": formatted_history,
                "question": search_query,
            }
        )

        msg = cl.Message(content="")
        await msg.send()

        async for chunk in stream:
            await msg.stream_token(chunk)

        # Фіксуємо історію чату
        box.chat_history.append(
            {
                ChatHistoryKey.ROLE: ChatHistoryValue.USER,
                ChatHistoryKey.CONTENT: search_query,
            }
        )

        if box.lang == "ru":  #  Ін'єкція для російськомовних браузерів :)
            await msg.stream_token(box.fluent.get("glory-to-ukraine"))

        # Фіксуємо історію чату
        box.chat_history.append(
            {
                ChatHistoryKey.ROLE: ChatHistoryValue.AI,
                ChatHistoryKey.CONTENT: msg.content,
            }
        )

        # Створення інтерактивних джерел для інтерфейсу Chainlit
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
                source_links.append(f"[{clean_name}]({url})")

        # Додаємо список посилань в кінець повідомлення
        if source_links:
            sources_title = box.fluent.get("sources-title")
            msg.content += f"\n\n**{sources_title}:**\n" + "\n".join(
                f"* {link}" for link in source_links
            )

        await msg.update()

    except Exception as e:
        logger.exception("Unexpected error: %s", e)
        text = box.fluent.get("unexpected-error")
        await cl.Message(content=text).send()
