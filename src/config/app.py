# -*- coding: utf-8 -*-


# from importlib.metadata import metadata
from pathlib import Path

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

# meta = metadata("crimea-rag")


class Settings(BaseSettings):
    # name: str = meta["name"]
    # version: str = meta["version"]
    # license: str = meta["License-Expression"]

    base_dir: Path = Path(__file__).resolve().parent.parent.parent

    public_dir: Path = base_dir / "public"
    locales_dir: Path = base_dir / "locales"

    default_locale: str = "en"

    env_file: Path = base_dir / ".env"

    database_dir_name: str = ""

    @computed_field
    @property
    def database_dir(self) -> Path:
        return self.base_dir / "database" / self.database_dir_name

    parent_dir: Path = base_dir.parent

    www_project_name: str = ""
    www_content_dir_name: str = ""

    @computed_field
    @property
    def content_dir(self) -> Path:
        return self.parent_dir / self.www_project_name / self.www_content_dir_name

    model_config = SettingsConfigDict(
        env_file=env_file,
        env_prefix="APP__",
        extra="ignore",
    )


settings = Settings()

if __name__ == "__main__":
    print(settings)
