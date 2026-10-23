# Google Fonts licensing guide: workflow guide

What this reference covers: Google Fonts licensing guide as a Fontlore workflow tool: what it is, where it sits in the implementation stage, how to use it well, and what evidence to record from it.

## What it is

How licensing metadata works in the google/fonts repository.

- Section: licensing
- Access: free
- URL: https://googlefonts.github.io/gf-guide/license-file.html

## Where it sits in the Fontlore workflow

This tool belongs to the **implementation** stage. Concretely: verify license scope for the exact use: web, desktop, app, logo, client handoff. It feeds records into the decision log, not opinions into the chat.

## How to use it well

- Go in with the project constraints written down: scripts, sizes, license scope, medium.
- Record what the tool returned, not what you hoped it would return.
- Prefer the tool's own primary data (files, license text, metadata) over summaries elsewhere.
- Combine with at least one independent source before treating a fact as verified.
- Screenshot or archive the license terms at review time; terms change without notice.

## Evidence to record

When this tool contributes to a decision, log: license name, official license URL, scope decision, and review date.

## Limitations and cautions

License summaries are not legal advice. When money changes hands, read the actual license text or ask the foundry.

## Alternatives and complements

| Tool | Section | Access |
| --- | --- | --- |
| SIL Open Font License | licensing | free |
| OFL FAQ | licensing | free |
| Adobe Fonts licensing FAQ | licensing | paid |
Siblings serve the same stage; pick one primary and keep one fallback in case the primary changes terms or disappears.

## Common mistakes

- Copying tool output into the decision log without the URL and date.
- Letting one tool be the single source of truth for license facts.
- Using the tool outside its stage: identification tools do not verify licenses, catalogs do not test rendering.

## Cross-references

- [Open Font License](../../references/licensing/open-font-license.md)
- [SIL Open Font License guide](./sil-open-font-license.md)
- [Research workflow](../../references/workflow/research-workflow.md)
- [Evaluating catalog metadata](../../references/sourcing/evaluating-catalog-metadata.md)
Compiled 2025 as part of the Fontlore project.
