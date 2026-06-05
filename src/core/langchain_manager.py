from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from langchain_core.documents.base import Document
    from langchain_core.language_models import BaseChatModel
    from langchain_core.runnables.base import RunnableSequence
    from langchain_core.vectorstores.base import VectorStoreRetriever

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough


def format_docs(docs: list[Document]):
    """Форматує знайдені документи у вигляді текстового блоку з джерелами."""
    return "\n\n".join(
        f"--- Source: {doc.metadata.get('source')} ---\nDocument: {doc.page_content}"
        for doc in docs
    )


def get_rag_chain(
    system_prompt: str, retriever: VectorStoreRetriever, llm: BaseChatModel
) -> RunnableSequence:
    """Створює базовий RAG-ланцюжок LangChain."""
    prompt = ChatPromptTemplate.from_template(system_prompt)

    return (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
