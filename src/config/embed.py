# -*- coding: utf-8 -*-

from pydantic_settings import BaseSettings, SettingsConfigDict

from config import app


class Settings(BaseSettings):
    model: str = ""
    url: str = ""
    port: int | None = None

    max_query_length: int = 550

    default_k: int = 5

    batch_size: int = 50

    model_config = SettingsConfigDict(
        env_file=app.settings.env_file,
        env_prefix="EMBED__",
        extra="ignore",
    )


settings = Settings()

if __name__ == "__main__":
    print(settings)
