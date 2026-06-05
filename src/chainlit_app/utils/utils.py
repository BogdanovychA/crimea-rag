# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Union

    from chainlit.session import HTTPSession, WebsocketSession
    from fluent_manager import FluentManager
    from langchain_core.documents.base import Document

from langchain_core.messages import AIMessage, HumanMessage

from chainlit_app.utils.models import ChatHistoryKey, ChatHistoryValue


def get_lang(session: Union["HTTPSession", "WebsocketSession"]) -> str:
    """Визначає мову користувача на основі налаштувань сесії Chainlit."""
    user_locale = getattr(session, "language", "en-US")
    user_locale = user_locale.strip().replace("_", "-").lower()
    lang = user_locale.split("-")[0]
    return lang


def format_docs(docs: list[Document]) -> str:
    """Форматує знайдені документи у вигляді текстового блоку з джерелами."""
    return "\n\n".join(
        f"--- Source: {doc.metadata.get('source')} ---\nDocument: {doc.page_content}"
        for doc in docs
    )


def create_source_links_list(docs: list[Document], fluent: FluentManager) -> list[str]:

    seen_sources = set()
    source_links = []

    for doc in docs:
        source = doc.metadata.get("source", "")
        if not source:
            continue
        clean_name = source.replace("index.md", "").strip("/")

        if not clean_name:
            clean_name = fluent.get("home-page")

        url = f"https://crimea-is-ukraine.org/{source.replace('index.md', '')}"

        if clean_name not in seen_sources:
            seen_sources.add(clean_name)
            source_links.append(f"[{clean_name}]({url})")

    return source_links


def create_formatted_history(
    chat_history: list[dict[ChatHistoryKey, ChatHistoryValue | str]],
) -> list[HumanMessage | AIMessage]:
    formatted_history = []
    for element in chat_history:
        new_element = None
        if element[ChatHistoryKey.ROLE] == ChatHistoryValue.USER:
            new_element = HumanMessage(content=element[ChatHistoryKey.CONTENT])
        elif element[ChatHistoryKey.ROLE] == ChatHistoryValue.AI:
            new_element = AIMessage(content=element[ChatHistoryKey.CONTENT])
        if new_element is not None:
            formatted_history.append(new_element)
    return formatted_history
