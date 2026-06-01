# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.lapathoniia_manager import LapathoniiaManager


from dataclasses import dataclass


@dataclass
class PandorasBox:
    """Контейнер для зберігання основних об'єктів та стану застосунку"""

    l9a: LapathoniiaManager
    system_prompt: str
