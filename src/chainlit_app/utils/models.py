# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fluent_manager import FluentManager
    from langchain_core.runnables.base import RunnableSerializable
    from langchain_core.vectorstores.base import VectorStoreRetriever


from dataclasses import dataclass
from enum import StrEnum


class ChatHistoryKey(StrEnum):
    ROLE = "role"
    CONTENT = "content"


class ChatHistoryValue(StrEnum):
    AI = "ai"
    USER = "user"


@dataclass
class PandorasBox:
    """Контейнер для зберігання основних об'єктів та стану застосунку"""

    retriever: VectorStoreRetriever
    chain: RunnableSerializable
    lang: str
    fluent: FluentManager
    chat_history: list[dict[ChatHistoryKey, ChatHistoryValue | str]]
    rephrase_chain: RunnableSerializable
