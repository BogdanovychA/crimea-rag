# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from langchain_core.language_models import BaseChatModel

from abc import ABC, abstractmethod

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

    def __init__(
        self,
        name: LLMName,
        api_key: str,
        model: str,
        base_url: str | None = None,
        temperature: float | int | None = None,
        max_tokens: int | None = None,
        timeout: float | int | None = None,
        max_retries: int | None = None,
    ) -> None:
        """Ініціалізує менеджер LLM та створює об'єкт клієнта моделі."""
        self.name = name
        self.model = model

        manager_class = self.get_manager_class(self.name)

        kwargs: dict[str, str | float | int] = {
            "api_key": api_key,
            "model": self.model,
        }
        if base_url is not None and base_url.strip() != "":
            kwargs["base_url"] = base_url
        if temperature is not None:
            kwargs["temperature"] = temperature
        if max_tokens is not None:
            kwargs["max_tokens"] = max_tokens
        if max_retries is not None:
            kwargs["max_retries"] = max_retries
        if timeout is not None:
            kwargs["timeout"] = timeout

        self.manager: BaseChatModel = manager_class(**kwargs)
