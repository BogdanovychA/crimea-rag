# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Union

    from chainlit.session import HTTPSession, WebsocketSession
    from langchain_core.documents.base import Document


def get_lang(session: Union["HTTPSession", "WebsocketSession"]):
    """Визначає мову користувача на основі налаштувань сесії Chainlit."""
    user_locale = getattr(session, "language", "en-US")
    user_locale = user_locale.strip().replace("_", "-").lower()
    lang = user_locale.split("-")[0]
    return lang


def format_docs(docs: list[Document]):
    """Форматує знайдені документи у вигляді текстового блоку з джерелами."""
    return "\n\n".join(
        f"--- Source: {doc.metadata.get('source')} ---\nDocument: {doc.page_content}"
        for doc in docs
    )
