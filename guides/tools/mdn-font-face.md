# MDN @font-face: workflow guide

What this reference covers: MDN @font-face as a Fontlore workflow tool: what it is, where it sits in the implementation stage, how to use it well, and what evidence to record from it.

## What it is

The definitive @font-face reference including font-display and unicode-range.

- Section: technical
- Access: free
- URL: https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face

## Where it sits in the Fontlore workflow

This tool belongs to the **implementation** stage. Concretely: inspect axes, features, and coverage before committing to the family. It feeds records into the decision log, not opinions into the chat.

## How to use it well

- Go in with the project constraints written down: scripts, sizes, license scope, medium.
- Record what the tool returned, not what you hoped it would return.
- Prefer the tool's own primary data (files, license text, metadata) over summaries elsewhere.
- Combine with at least one independent source before treating a fact as verified.
- Pin versions: note the release, endpoint snapshot, or file hash alongside the retrieval date.

## Evidence to record

When this tool contributes to a decision, log: the measurements taken (axes, features, coverage) and the file version.

## Limitations and cautions

Tool output describes the file, not the design. A clean file can still be the wrong voice for the project.

## Alternatives and complements

| Tool | Section | Access |
| --- | --- | --- |
| MDN font loading guide | technical | free |
| OpenType specification | technical | free |
| Axis-Praxis | technical | free |
Siblings serve the same stage; pick one primary and keep one fallback in case the primary changes terms or disappears.

## Common mistakes

- Copying tool output into the decision log without the URL and date.
- Letting one tool be the single source of truth for license facts.
- Using the tool outside its stage: identification tools do not verify licenses, catalogs do not test rendering.

## Cross-references

- [Inspecting Font Files](../../references/technical/inspecting-font-files.md)
- [MDN font loading guide guide](./mdn-font-loading-guide.md)
- [Research workflow](../../references/workflow/research-workflow.md)
- [Evaluating catalog metadata](../../references/sourcing/evaluating-catalog-metadata.md)
Compiled 2025 as part of the Fontlore project.
