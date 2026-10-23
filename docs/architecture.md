# Architecture

> This document describes docextract as it is now. It grows as decisions are made.

## Purpose

docextract extracts structured data from documents and serves it over an HTTP API.

## Constraints

- **Document-agnostic:** the service must handle any document type, without a hard-coded format per document.
- **Multi-tenant:** one deployment serves multiple tenants, and each tenant's data stays separate.
- **Cross-platform:** development on Windows, CI on Linux.

## Current state

Bootstrap. The service starts and answers a liveness check; no extraction features exist yet.

## Components

All backend code lives in `backend/src/docextract/`.

| Component     | Module            | Responsibility                                                              |
| ------------- | ----------------- | --------------------------------------------------------------------------- |
| App factory   | `app.py`          | `create_app()` builds the FastAPI app and registers routers; `app` is the instance uvicorn serves |
| Health router | `api/health.py`   | `GET /health` liveness check returning `{"status": "ok"}`; touches no dependencies |

New endpoint groups get their own router module under `api/` and one `include_router` line in `create_app()`.

## Open questions

These are deliberately undecided until a requirement needs them:

- How extraction works for arbitrary document types
- How tenants are identified and isolated
- Where documents and results are stored
- How users and tenants authenticate

## Decisions

| #    | Decision                      | Status   |
| ---- | ----------------------------- | -------- |
| 0001 | Record architecture decisions | Accepted |
| 0002 | Backend stack                 | Accepted |
