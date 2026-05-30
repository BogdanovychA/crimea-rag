# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from langchain_core.documents.base import Document


from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


class ChromaManager:
    def __init__(
        self, model: str, base_url: str, persist_directory: str, default_k: int
    ) -> None:

        self.model = model
        self.base_url = base_url
        self.persist_directory = persist_directory
        self.k = default_k

        self.embedding_function = OllamaEmbeddings(
            model=app.settings.embed_model,
            base_url=f"{app.settings.embed_url}:{app.settings.embed_port}",
        )

        self.vector_db = Chroma(
            persist_directory=str(app.settings.database_dir),
            embedding_function=self.embedding_function,
        )

    def similarity_search(self, query: str, k: int | None = None) -> list[Document]:
        k = self.k if k is None else k
        return self.vector_db.similarity_search(query, k=k)

    def max_marginal_relevance_search(
        self, query: str, k: int | None = None
    ) -> list[Document]:
        k = self.k if k is None else k
        return self.vector_db.max_marginal_relevance_search(query, k=k)


if __name__ == "__main__":
    from config import app

    client = ChromaManager(
        model=app.settings.embed_model,
        base_url=app.settings.embed_url,
        persist_directory=app.settings.database_dir,
        default_k=3,
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
