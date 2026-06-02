from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from langchain_core.language_models import BaseChatModel

from abc import ABC, abstractmethod

from langchain_openai import ChatOpenAI

from config import lapathoniia


class BaseLLMManager(ABC):
    @classmethod
    @abstractmethod
    def get_manager(cls) -> BaseChatModel:
        pass


class LLMManager(BaseLLMManager):
    @classmethod
    def get_manager(cls) -> BaseChatModel:
        return ChatOpenAI(**lapathoniia.settings.model_dump())
