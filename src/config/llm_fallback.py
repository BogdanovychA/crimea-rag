# -*- coding: utf-8 -*-

from pydantic_settings import BaseSettings, SettingsConfigDict

from config import app
from models.llm import LLMName


class Settings(BaseSettings):
    """Налаштування LLM провайдерів."""

    name: LLMName = LLMName.NONE
    api_key: str = ""
    model: str = ""
    base_url: str | None = None
    temperature: float | int | None = None
    max_tokens: int | None = None
    timeout: float | int = 10
    max_retries: int = 1

    model_config = SettingsConfigDict(
        env_file=app.settings.env_file,
        env_prefix="LLM_FALLBACK__",
        extra="ignore",
    )


settings = Settings()

if __name__ == "__main__":
    print(settings)
