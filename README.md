# docextract

A document-agnostic, multi-tenant document extraction service.

> **Status:** bootstrap. The repository is being set up; no extraction features exist yet.

## Goals

- **Document-agnostic:** extract structured data from any document type, without hard-coding a format per document.
- **Multi-tenant:** serve multiple tenants from one deployment, with each tenant's data kept separate.

## Tech stack

| Area            | Choice                                  |
| --------------- | --------------------------------------- |
| Language        | Python 3.12                             |
| Web framework   | [FastAPI](https://fastapi.tiangolo.com) |
| Data validation | [Pydantic](https://docs.pydantic.dev)   |
| Packaging       | [uv](https://docs.astral.sh/uv/)        |

## Getting started

### Prerequisites

- Python 3.12
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Setup

Setup instructions will be added once the backend is scaffolded.

## Roadmap

- [x] Repository hygiene (`.gitignore`, `.gitattributes`)
- [ ] Documentation and architecture decision records
- [ ] Backend scaffold
- [ ] `/health` endpoint with tests
- [ ] Pre-commit hooks and secret scanning (gitleaks)
- [ ] Continuous integration

## Documentation

- [Architecture overview](docs/architecture.md)
- [Architecture decision records](docs/adr/)
