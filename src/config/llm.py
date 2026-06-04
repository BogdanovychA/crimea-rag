# -*- coding: utf-8 -*-

from pydantic_settings import BaseSettings, SettingsConfigDict

from config import app


class Settings(BaseSettings):
    """Налаштування Lapathoniia"""

    api_key: str = ""
    model: str = ""
    base_url: str | None = None
    temperature: float | int | None = None
    max_tokens: int | None = None

    model_config = SettingsConfigDict(
        env_file=app.settings.env_file,
        env_prefix="LLM__",
        extra="ignore",
    )


settings = Settings()

if __name__ == "__main__":
    print(settings)
