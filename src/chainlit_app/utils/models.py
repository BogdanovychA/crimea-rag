# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from langchain_core.runnables.base import RunnableSequence


from dataclasses import dataclass


@dataclass
class PandorasBox:
    """Контейнер для зберігання основних об'єктів та стану застосунку"""

    rag_chain: RunnableSequence
