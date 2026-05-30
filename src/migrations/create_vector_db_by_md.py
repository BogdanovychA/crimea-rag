# -*- coding: utf-8 -*-

import logging
import shutil

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import MarkdownTextSplitter

from config import app

logger = logging.getLogger(__name__)


def main():
    if app.settings.database_dir.exists():
        logger.info(f"Видалення існуючої бази знань з {app.settings.database_dir}...")
        try:
            shutil.rmtree(app.settings.database_dir)
        except Exception as e:
            logger.error(f"Не вдалося видалити директорію бази знань: {e}")

    logger.info("Завантаження Markdown файлів...")
    documents = []
    for path in app.settings.content_dir.rglob("**/*.md"):
        if path.is_file():
            try:
                text = path.read_text(encoding="utf-8")
                relative_path = path.relative_to(app.settings.content_dir)
                documents.append(
                    Document(page_content=text, metadata={"source": str(relative_path)})
                )
            except Exception as e:
                logger.exception(f"Помилка читання файлу {path}: {e}")

    logger.info("Розбиття текстів на чанки...")
    text_splitter = MarkdownTextSplitter(chunk_size=500, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)

    logger.info("Зв'язок з Ollama та створення векторів...")
    embeddings = OllamaEmbeddings(
        model=app.settings.embed_model,
        base_url=f"{app.settings.embed_url}:{app.settings.embed_port}",
        mirostat=0,
        mirostat_eta=0.0,
        mirostat_tau=0.0,
        tfs_z=1.0,
    )

    logger.info("Ініціалізація бази Chroma...")
    vector_db = Chroma(
        embedding_function=embeddings, persist_directory=str(app.settings.database_dir)
    )

    logger.info(f"Всього чанків для обробки: {len(chunks)}")

    batch_size = app.settings.batch_size

    logger.info(f"Запис у базу порціями по {batch_size} батчів...")

    for i in range(0, len(chunks), batch_size):
        batch = chunks[i : i + batch_size]
        vector_db.add_documents(batch)
        logger.info(f"Оброблено чанків: {i + len(batch)} з {len(chunks)}")

    logger.info(
        f"Успішно! База знань збережена локально в: {app.settings.database_dir}"
    )


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )

    main()
