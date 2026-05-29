# -*- coding: utf-8 -*-

import os
from importlib.metadata import metadata
from pathlib import Path

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

meta = metadata("crimea-rag")


class Settings(BaseSettings):
    @staticmethod
    def get_asset_dir() -> Path:
        """Повертає шлях до директорії з ресурсами."""
        default_assets_dir = Path(__file__).resolve().parent.parent / "assets"
        return Path(os.environ.get("FLET_ASSETS_DIR", default_assets_dir)).resolve()

    name: str = meta["name"]
    version: str = meta["version"]
    license: str = meta["License-Expression"]

    base_url: str = ""

    assets_dir: Path = get_asset_dir()
    env_file: Path = assets_dir / ".env"

    base_dir: Path = Path(__file__).resolve().parent.parent.parent

    database_dir_name: str = "crimea-rag"

    @computed_field
    @property
    def database_dir(self) -> Path:
        return self.base_dir / "database" / self.database_dir_name

    parent_dir: Path = base_dir.parent

    www_project_name: str = "crimea-is-ukraine"
    www_content_dir_name: str = "content"

    @computed_field
    @property
    def content_dir(self) -> Path:
        return self.parent_dir / self.www_project_name / self.www_content_dir_name

    llm_model: str = "mxbai-embed-large"
    llm_url: str = "http://127.0.0.1"
    llm_port: int = 11434

    batch_size: int = 50

    model_config = SettingsConfigDict(
        env_file=env_file,
        env_prefix="APP__",
        extra="ignore",
    )


settings = Settings()

if __name__ == "__main__":
    print(settings)
