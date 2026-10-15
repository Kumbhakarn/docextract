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
| Language        | Python 3.12                             | Planned (Step 3)   |
| Packaging       | [uv](https://docs.astral.sh/uv/)        | Planned (Step 3)   |
| Web framework   | [FastAPI](https://fastapi.tiangolo.com) | Planned (Step 4)   |
| Data validation | [Pydantic](https://docs.pydantic.dev)   | Planned (Step 4)   |

## Getting started

### Prerequisites

- Python 3.12
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Setup

Setup instructions will be added once the backend is scaffolded.

## Roadmap

- [x] Repository hygiene (`.gitignore`, `.gitattributes`)
- [x] Documentation and architecture decision records
- [ ] Backend scaffold
- [ ] `/health` endpoint with tests
- [ ] Pre-commit hooks and secret scanning (gitleaks)
- [ ] Continuous integration

## Documentation

- [Architecture overview](docs/architecture.md)
- [Architecture decision records](docs/adr/)
