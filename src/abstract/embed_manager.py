from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from langchain_core.vectorstores.base import VectorStoreRetriever

from abc import ABC, abstractmethod

from config import app, embed
from core.chroma_manager import ChromaManager


class BaseEmbedManager(ABC):
    @abstractmethod
    def get_retriever(self) -> VectorStoreRetriever:
        pass


class EmbedManager(BaseEmbedManager):
    def __init__(self) -> None:

        port_suffix = f":{embed.settings.port}" if embed.settings.port else ""
        self.client = ChromaManager(
            model=embed.settings.model,
            base_url=f"{embed.settings.url}{port_suffix}",
            persist_directory=app.settings.database_dir,
            k=embed.settings.default_k,
        )

    def get_retriever(self, *args, **kwargs) -> VectorStoreRetriever:
        return self.client.get_retriever(*args, **kwargs)
