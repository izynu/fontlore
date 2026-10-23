# Google Fonts Developer API: workflow guide

What this reference covers: Google Fonts Developer API as a Fontlore workflow tool: what it is, where it sits in the research stage, how to use it well, and what evidence to record from it.

## What it is

Structured metadata for every Google Fonts family: variants, subsets, scripts, and updates.

- Section: apis
- Access: free
- URL: https://developers.google.com/fonts/docs/developer_api

## Where it sits in the Fontlore workflow

This tool belongs to the **research** stage. Concretely: pull structured metadata (weights, subsets, variable status) and cache it with a retrieval date. It feeds records into the decision log, not opinions into the chat.

## How to use it well

- Go in with the project constraints written down: scripts, sizes, license scope, medium.
- Record what the tool returned, not what you hoped it would return.
- Prefer the tool's own primary data (files, license text, metadata) over summaries elsewhere.
- Combine with at least one independent source before treating a fact as verified.
- Pin versions: note the release, endpoint snapshot, or file hash alongside the retrieval date.

## Evidence to record

When this tool contributes to a decision, log: the metadata snapshot (weights, subsets, variable flag) plus the endpoint and date.

## Limitations and cautions

API metadata can lag behind releases. Record the retrieval date and verify critical fields at the source.

## Alternatives and complements

| Tool | Section | Access |
| --- | --- | --- |
| Fontsource API | apis | free |
| Fontsource list endpoint | apis | free |
Siblings serve the same stage; pick one primary and keep one fallback in case the primary changes terms or disappears.

## Common mistakes

- Copying tool output into the decision log without the URL and date.
- Letting one tool be the single source of truth for license facts.
- Using the tool outside its stage: identification tools do not verify licenses, catalogs do not test rendering.

## Cross-references

- [Fontsource Api](../../references/sourcing/fontsource-api.md)
- [Fontsource API guide](./fontsource-api.md)
- [Research workflow](../../references/workflow/research-workflow.md)
- [Evaluating catalog metadata](../../references/sourcing/evaluating-catalog-metadata.md)
Compiled 2025 as part of the Fontlore project.
