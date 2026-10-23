# Contributing to Fontlore

Thanks for wanting to improve Fontlore. This repository has one quality rule above all others: nothing enters the data layer or the references without being verifiable. Read SKILL.md for context and scripts/validate.py for the exact machine checks.

## What to contribute

- Data corrections: a wrong designer, foundry, license, classification, or script coverage claim in data/fonts.json, pairings.json, or tools.json. Corrections need an evidence URL (foundry page, license text, or catalog page), not a vibe.
- New font entries: open-license families with verifiable metadata. Every required field must be filled or explicitly null; the license must be in the accepted set and confirmed at the source URL you provide.
- Reference improvements: factual fixes, sharper worked examples, missing failure modes in the 90 references. Improvements keep the existing structure; new sections go before Cross-references.
- New tool entries: real tools with an https URL, an honest one-line "what", and the correct section.
- Code fixes: decide.py, validate.py, build_data.py, and CI. Keep everything stdlib-only.

We do not accept: promotional entries, AI-generated font "reviews", fabricated metrics, links to pirated or cracked font files, and any change that weakens the null policy.

## House style for references

The validator enforces these; getting them right is the fastest way to a merged PR:

- Pure ASCII. No emoji, no smart quotes, no en or em dashes (use a hyphen).
- Exactly one H1 at the top.
- The first paragraph starts with the sentence "What this reference covers:".
- Between 140 and 320 lines.
- A "## Cross-references" section with 2 to 5 relative links that resolve inside the repository.
- The final line is exactly: "Compiled 2025 as part of the Fontlore project."
- Honest numbers only. If you cite a count (fonts, pairings, tools), it must match the current data files.

## Validation requirement

Run the full gate before opening a PR:

```bash
python3 scripts/validate.py
```

It must pass with zero errors. CI runs the same command on every push and PR to main; a red check means the PR is not reviewed.

## Commit style

- Imperative mood, one logical change per commit: "add jetbrains-mono hebrew coverage note", "fix pairings rationale for pair-041".
- Data changes mention the slugs touched; reference changes mention the file names.
- No "wip" commits in PRs; squash if you must, but make the final history readable.

## Pull request process

1. Fork, branch from main, make your change.
2. Run python3 scripts/validate.py and confirm it passes.
3. Fill the PR template: summary, and the checklist (validator passes, ASCII only, no invented data, license verified at the source, no emoji).
4. For data additions, include the evidence URLs in the PR description, not only in the data.
5. One maintainer review is required for references and tools; two are required for license or schema changes.
6. If your PR touches counts (a new font, a new tool), update every place the counts appear: README.md, SKILL.md, MASTER-SKILL.md, and the site data in the same PR.

## Licensing of contributions

By contributing you agree your contributions are licensed under the repository's MIT license. Font files are never committed to this repository; we link to sources under their own licenses.
