# Modular Scale: workflow guide

What this reference covers: Modular Scale as a Fontlore workflow tool: what it is, where it sits in the implementation stage, how to use it well, and what evidence to record from it.

## What it is

The classic ratio-based scale calculator.

- Section: tooling
- Access: free
- URL: https://www.modularscale.com/

## Where it sits in the Fontlore workflow

This tool belongs to the **implementation** stage. Concretely: measure and inspect rather than guess; record what the tool reported. It feeds records into the decision log, not opinions into the chat.

## How to use it well

- Go in with the project constraints written down: scripts, sizes, license scope, medium.
- Record what the tool returned, not what you hoped it would return.
- Prefer the tool's own primary data (files, license text, metadata) over summaries elsewhere.
- Combine with at least one independent source before treating a fact as verified.
- Pin versions: note the release, endpoint snapshot, or file hash alongside the retrieval date.

## Evidence to record

When this tool contributes to a decision, log: the raw output relevant to the decision, trimmed to what matters.

## Limitations and cautions

Numbers without context mislead. Record sizes alongside the measurements you take.

## Alternatives and complements

| Tool | Section | Access |
| --- | --- | --- |
| Typescale | tooling | free |
Siblings serve the same stage; pick one primary and keep one fallback in case the primary changes terms or disappears.

## Common mistakes

- Copying tool output into the decision log without the URL and date.
- Letting one tool be the single source of truth for license facts.
- Using the tool outside its stage: identification tools do not verify licenses, catalogs do not test rendering.

## Cross-references

- [Inspecting Font Files](../../references/technical/inspecting-font-files.md)
- [Typescale guide](./typescale.md)
- [Research workflow](../../references/workflow/research-workflow.md)
- [Evaluating catalog metadata](../../references/sourcing/evaluating-catalog-metadata.md)
Compiled 2025 as part of the Fontlore project.
