from __future__ import annotations

from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from langchain_core.language_models import BaseChatModel

from abc import ABC, abstractmethod

from config import app, llm
from models.llm import LLMName


class BaseLLMManager(ABC):
    @classmethod
    @abstractmethod
    def register(cls, llm_name: LLMName, chat_model_class: Type[BaseChatModel]) -> None:
        pass

    @classmethod
    @abstractmethod
    def get_manager_class(cls, llm_name: LLMName) -> Type[BaseChatModel]:
        pass


class LLMManager(BaseLLMManager):
    _REGISTRY: dict[LLMName, Type[BaseChatModel]] = {}

    @classmethod
    def register(cls, llm_name: LLMName, chat_model_class: Type[BaseChatModel]) -> None:

        cls._REGISTRY[llm_name] = chat_model_class

    @classmethod
    def get_manager_class(cls, llm_name: LLMName) -> Type[BaseChatModel]:

        return cls._REGISTRY[llm_name]

    def __init__(self):

        self.name = app.settings.llm_name

        self.api_key = llm.settings.api_key
        self.model = llm.settings.model
        self.base_url = llm.settings.base_url
        self.temperature = llm.settings.temperature
        self.max_tokens = llm.settings.max_tokens

        manager_class = self.get_manager_class(self.name)

        self.manager: BaseChatModel = manager_class(
            api_key=self.api_key,
            model=self.model,
            base_url=self.base_url,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
