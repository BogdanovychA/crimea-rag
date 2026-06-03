# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Union

    from chainlit.session import HTTPSession, WebsocketSession


def get_lang(session: Union["HTTPSession", "WebsocketSession"]):
    user_locale = getattr(session, "language", "en-US")
    user_locale = user_locale.strip().replace("_", "-").lower()
    lang = user_locale.split("-")[0]
    return lang
