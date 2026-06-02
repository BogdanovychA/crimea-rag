# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

    from langchain_core.documents.base import Document
    from langchain_core.vectorstores.base import VectorStoreRetriever


from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


class ChromaManager:
    def __init__(
        self, model: str, base_url: str, persist_directory: Path, k: int
    ) -> None:

        self.model = model
        self.base_url = base_url
        self.persist_directory = str(persist_directory)
        self.k = k

        self.embedding_function = OllamaEmbeddings(
            model=self.model,
            base_url=self.base_url,
        )

        self.vector_db = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embedding_function,
        )

    def get_retriever(self, k: int | None = None) -> VectorStoreRetriever:
        k = k or self.k
        return self.vector_db.as_retriever(search_kwargs={"k": k})

    def similarity_search(self, query: str) -> list[Document]:
        return self.vector_db.similarity_search(query, k=self.k)

    def max_marginal_relevance_search(self, query: str) -> list[Document]:
        return self.vector_db.max_marginal_relevance_search(query, k=self.k)


if __name__ == "__main__":
    from config import app, embed

    port_suffix = f":{embed.settings.port}" if embed.settings.port else ""
    client = ChromaManager(
        model=embed.settings.model,
        base_url=f"{embed.settings.url}{port_suffix}",
        persist_directory=app.settings.database_dir,
        k=3,
    )

    q = "Крим чи Рим?"
    the_list = client.similarity_search(q)
    # the_list = client.max_marginal_relevance_search(q)

    for item in the_list:
        print("Content:")
        print(item.page_content)
        print("Source: ", item.metadata["source"])
        print()
        print("-" * 10)
        print()
