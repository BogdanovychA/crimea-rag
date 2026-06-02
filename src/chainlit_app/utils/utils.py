# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Union

    from chainlit.session import HTTPSession, WebsocketSession


def get_lang(session: Union["HTTPSession", "WebsocketSession"]):
    user_locale = getattr(session, "language", "en-US")
    lang, *_ = user_locale.split("-")
    return lang
