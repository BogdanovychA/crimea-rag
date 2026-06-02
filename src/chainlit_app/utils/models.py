# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fluent_manager import FluentManager
    from langchain_core.runnables.base import RunnableSerializable
    from langchain_core.vectorstores.base import VectorStoreRetriever


from dataclasses import dataclass


@dataclass
class PandorasBox:
    """Контейнер для зберігання основних об'єктів та стану застосунку"""

    retriever: VectorStoreRetriever
    chain: RunnableSerializable
    lang: str
    fluent: FluentManager
