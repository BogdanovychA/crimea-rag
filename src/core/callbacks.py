# -*- coding: utf-8 -*-

import logging

from langchain_core.callbacks import AsyncCallbackHandler

logger = logging.getLogger(__name__)


class RAGErrorLogger(AsyncCallbackHandler):
    async def on_llm_error(self, error: BaseException, **kwargs) -> None:
        logger.warning(
            "Primary LLM failed, switching to fallback. Error: %s. Context: %s",
            error,
            kwargs,
            exc_info=error,
        )
