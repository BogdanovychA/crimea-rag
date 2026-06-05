# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from langchain_core.language_models import BaseChatModel

from abc import ABC, abstractmethod

from config import llm
from models.llm import LLMName


class BaseLLMManager(ABC):
    """Абстрактний менеджер для мовних моделей (LLM)."""

    @classmethod
    @abstractmethod
    def register(cls, llm_name: LLMName, chat_model_class: Type[BaseChatModel]) -> None:
        """Реєструє клас клієнта для конкретного провайдера LLM."""
        pass

    @classmethod
    @abstractmethod
    def get_manager_class(cls, llm_name: LLMName) -> Type[BaseChatModel]:
        """Повертає зареєстрований клас клієнта LLM."""
        pass


class LLMManager(BaseLLMManager):
    """Менеджер для ініціалізації та управління підключенням до LLM."""

    _REGISTRY: dict[LLMName, Type[BaseChatModel]] = {}

    @classmethod
    def register(cls, llm_name: LLMName, chat_model_class: Type[BaseChatModel]) -> None:
        """Додає клас провайдера LLM до реєстру."""
        cls._REGISTRY[llm_name] = chat_model_class

    @classmethod
    def get_manager_class(cls, llm_name: LLMName) -> Type[BaseChatModel]:
        """Отримує клас провайдера LLM або викликає ValueError, якщо він не знайдений."""
        if llm_name not in cls._REGISTRY:
            raise ValueError(
                f"LLM provider '{llm_name}' is not registered. Please check LLM__NAME in your .env"
            )
        return cls._REGISTRY[llm_name]

    def __init__(self):
        """Ініціалізує менеджер LLM та створює об'єкт клієнта моделі."""
        self.name = llm.settings.name
        self.api_key = llm.settings.api_key
        self.model = llm.settings.model
        self.base_url = llm.settings.base_url
        self.temperature = llm.settings.temperature
        self.max_tokens = llm.settings.max_tokens

        manager_class = self.get_manager_class(self.name)

        kwargs = {
            "api_key": self.api_key,
            "model": self.model,
        }
        if self.base_url is not None:
            kwargs["base_url"] = self.base_url
        if self.temperature is not None:
            kwargs["temperature"] = self.temperature
        if self.max_tokens is not None:
            kwargs["max_tokens"] = self.max_tokens

        self.manager: BaseChatModel = manager_class(**kwargs)
