# ADR-0001: Record architecture decisions

- **Status:** Accepted
- **Date:** 2026-10-15

## Context

Significant decisions will be made as docextract is built: storage, tenant isolation, how extraction works.
Without a record, the reasoning behind each choice is lost and decisions get re-argued.

## Decision

Record each significant architectural decision as a short Markdown file in `docs/adr/`.

- Files are named `NNNN-short-title.md`, numbered in order and never reused.
- Each ADR has: **Status**, **Date**, **Context**, **Decision**, **Consequences**.
- Status is one of: Proposed, Accepted, Superseded by ADR-NNNN.
- An accepted ADR is not rewritten. A changed decision gets a new ADR that supersedes the old one.
- ADRs are written only when a real requirement forces the decision.

## Consequences

- The reasoning behind each decision stays next to the code and goes through review like code.
- Writing an ADR adds a small cost to each significant decision.
- `docs/architecture.md` describes the current system and links to the ADRs that shaped it.
