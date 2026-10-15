# Architecture

> This document describes docextract as it is now. It grows as decisions are made; the reasoning lives in the [ADRs](adr/).

## Purpose

docextract extracts structured data from documents and serves it over an HTTP API.

## Constraints

- **Document-agnostic:** the service must handle any document type, without a hard-coded format per document.
- **Multi-tenant:** one deployment serves multiple tenants, and each tenant's data stays separate.
- **Cross-platform:** development on Windows, CI on Linux.

## Current state

Bootstrap. No components exist yet.

## Components

*To be added when the backend is scaffolded.*

## Open questions

These are deliberately undecided until a requirement needs them:

- How extraction works for arbitrary document types
- How tenants are identified and isolated
- Where documents and results are stored
- How users and tenants authenticate

## Decisions

| ADR                                             | Title                         | Status   |
| ----------------------------------------------- | ----------------------------- | -------- |
| [0001](adr/0001-record-architecture-decisions.md) | Record architecture decisions | Proposed |
| [0002](adr/0002-backend-stack.md)                 | Backend stack                 | Proposed |
