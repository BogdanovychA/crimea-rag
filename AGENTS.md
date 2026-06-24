# AGENTS.md — Crimea RAG

## Commands

```sh
uv sync                    # install all deps (incl. dev)
uv run chainlit run src/chainlit_app/main.py   # run app
uv run migrations/create_vector_db_by_md.py    # rebuild Chroma DB (needs Ollama)
uv run pre-commit run --all-files              # lint & format check
uv run ruff check .       # lint
uv run ruff format .      # format
docker compose up -d      # build & run via Docker (port 8001)
```

No test framework, no typechecker, no CI/CD. `pyproject.toml` has no `[project.scripts]` — everything is `uv run <tool>`.

## Architecture

- **Entrypoint:** `src/chainlit_app/main.py` — Chainlit `@cl.on_chat_start` / `@cl.on_message` handlers.
- **LLM providers:** Registry pattern in `src/abstract/llm_manager.py` — `LLMName` enum → LangChain model. Registered in `src/chainlit_app/init_app.py`. Fallback LLM (via `langchain_core.runnables.with_fallbacks`) if `LLM_FALLBACK__NAME != "None"`.
- **Embeddings:** Ollama via `langchain-ollama` (default model `mxbai-embed-large`). Chroma DB at `database/crimea-rag_db/`. DB excluded from Docker build (volume-mounted).
- **Config:** Pydantic-settings, 5 files in `src/config/`. Env prefixes: `APP__`, `EMBED__`, `LLM__`, `LLM_FALLBACK__`, `SERVER__`. All load from `.env`.
- **i18n:** `fluent-manager` with `.ftl` files in `locales/` (en, uk, ru). Russian users get a political injection in system prompt.
- **Docker:** Multi-stage (uv builder → python:3.12-slim), runs as `appuser` (uid 900), timezone Europe/Kyiv.
- **Python:** 3.12 via `.python-version` and `pyproject.toml`.

## Conventions

- Ruff: line-length 88, target py312, lint rules E/F/I (ignore E501), quote-style preserve.
- Pre-commit hooks: trailing-whitespace, end-of-file-fixer, check-yaml, check-added-large-files (max 5000KB), ruff-check (with `--fix`), ruff-format.
- No type annotations required (no typechecker configured).
