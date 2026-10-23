# docextract

A document-agnostic, multi-tenant document extraction service.

> **Status:** bootstrap. The repository is being set up; no extraction features exist yet.

## Goals

- **Document-agnostic:** extract structured data from any document type, without hard-coding a format per document.
- **Multi-tenant:** serve multiple tenants from one deployment, with each tenant's data kept separate.
- **Grounded results (planned):** every extracted value points back to where it came from in the source document.

## Tech stack

| Area            | Choice                                  | State              |
| --------------- | --------------------------------------- | ------------------ |
| Language        | Python 3.12                             | In use             |
| Packaging       | [uv](https://docs.astral.sh/uv/)        | In use             |
| Web framework   | [FastAPI](https://fastapi.tiangolo.com) | In use             |
| Data validation | [Pydantic](https://docs.pydantic.dev)   | In use             |

## Getting started

### Prerequisites

- Python 3.12
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Setup

The backend lives in `backend/`. From the repo root:

```
cd backend
uv sync
```

`uv sync` creates `backend/.venv` and installs the exact versions pinned in `uv.lock`, including the dev tools.

### Checks

Run these from `backend/`:

```
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run mypy
```

### Run locally

From `backend/`:

```
uv run uvicorn docextract.app:app --reload
```

Then open `http://127.0.0.1:8000/health` (should return `{"status":"ok"}`) or the interactive API docs at `http://127.0.0.1:8000/docs`.

## Roadmap

- [x] Repository hygiene (`.gitignore`, `.gitattributes`)
- [x] Documentation and architecture decision records
- [x] Backend scaffold
- [x] `/health` endpoint with tests
- [ ] Pre-commit hooks and secret scanning (gitleaks)
- [ ] Continuous integration

## Documentation

- [Architecture overview](docs/architecture.md)
