# -*- coding: utf-8 -*-

from enum import StrEnum


class LLMName(StrEnum):
    """Назва LLM провайдера"""

    NONE = "None"
    LAPA = "Lapathoniia"
    OPENAI = "OpenAI"
    ANTHROPIC = "Anthropic"
    GOOGLE = "Google"
