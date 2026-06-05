from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from langchain_core.vectorstores.base import VectorStoreRetriever

from abc import ABC, abstractmethod

from config import app, embed
from core.chroma_manager import ChromaManager


class BaseEmbedManager(ABC):
    """Абстрактний базовий менеджер для векторних ембеддингів."""

    @abstractmethod
    def get_retriever(self) -> VectorStoreRetriever:
        """Повертає об'єкт ретривера."""
        pass

    @property
    @abstractmethod
    def max_query_length(self) -> int:
        """Повертає максимальну дозволену довжину запиту."""
        pass


class EmbedManager(BaseEmbedManager):
    """Менеджер для взаємодії з векторними ембеддингами та базою даних Chroma."""

    def __init__(self) -> None:
        """Ініціалізує менеджер ембеддингів та підключає клієнт Chroma."""
        port_suffix = f":{embed.settings.port}" if embed.settings.port else ""
        self.client = ChromaManager(
            model=embed.settings.model,
            base_url=f"{embed.settings.url}{port_suffix}",
            persist_directory=app.settings.database_dir,
            k=embed.settings.default_k,
        )

        self._max_query_length = embed.settings.max_query_length

    def get_retriever(self, *args, **kwargs) -> VectorStoreRetriever:
        """Повертає об'єкт ретривера з Chroma DB client."""
        return self.client.get_retriever(*args, **kwargs)

    @property
    def max_query_length(self) -> int:
        """Повертає ліміт довжини вхідного запиту."""
        return self._max_query_length
