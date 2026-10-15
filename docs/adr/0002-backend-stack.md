# ADR-0002: Backend stack

- **Status:** Proposed
- **Date:** 2026-10-15

## Context

docextract is an HTTP service that accepts documents and returns structured data.
Because it is document-agnostic, the shape of that data varies, so request and response validation matters.
Development happens on Windows and CI runs on Linux, so tooling must behave the same on both.

## Decision

| Area            | Choice      | Alternatives considered         |
| --------------- | ----------- | ------------------------------- |
| Language        | Python 3.12 | Python 3.11, 3.13               |
| Web framework   | FastAPI     | Flask, Django + DRF             |
| Data validation | Pydantic v2 | marshmallow, dataclasses        |
| Packaging       | uv          | pip + venv, Poetry              |

- **Python 3.12:** mature and widely supported by libraries, with good typing features. 3.13 is newer but some libraries lag behind it.
- **FastAPI:** async support, request validation and OpenAPI docs built in, and it uses Pydantic directly. Flask needs extensions for the same features. Django brings an ORM and admin we don't need yet.
- **Pydantic v2:** one model type for validation, serialization and the OpenAPI schema. Its Rust core is fast.
- **uv:** fast installs, a cross-platform lockfile (`uv.lock`), and it can manage the Python version itself. One tool replaces pip, venv and pip-tools.

## Consequences

- API contracts are defined as Pydantic models and documented automatically through OpenAPI.
- Async code paths require care: blocking work (for example, CPU-heavy parsing) must not run on the event loop.
- Contributors and CI need uv installed. `uv.lock` is committed so every environment resolves the same dependencies.
- uv is younger than pip and Poetry. If it stops being maintained, migrating away means replacing the lockfile and commands, but not the code.
