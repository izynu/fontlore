# Building a Font Shortlist with Sources

What this reference covers: How to turn scattered font research into a reproducible shortlist with evidence records, source logging, and confidence levels. It defines the record format this project recommends and shows how to keep a shortlist defensible when teammates, auditors, or future you ask "why this font?"

Most font decisions die in reproducibility: someone remembers "we looked at a nice grotesque last month" but not which one, from where, under what license. A source-backed shortlist fixes that with a small, disciplined record.

## What a source-backed shortlist is

- A shortlist is not a mood board. It is a set of candidates, each carrying evidence: where it came from, what version, what license, who checked it, when, and with what result.
- The evidence serves three audiences: the current decision (scoring), future maintainers (why is this here), and audits (prove the license).
- Reproducibility means a teammate can retrace your path: same sources, same filters, same specimens, same conclusion or a documented disagreement.
- The format below is deliberately lightweight: if keeping the record is hard, it will not be kept.

## Evidence records

Keep one record per candidate. Minimum fields:

- family: name and version (or version signal, if the family does not publish versions).
- source: where you found it (fonts.google.com, fontsource.org, foundry site, GitHub release) as an https URL when available.
- license: exact license name and where the license file lives (repo path, purchase email, PDF copy stored with files).
- checked_by and checked_on: the human and the date; stale checks are re-checks, not facts.
- coverage: scripts, subsets, weights, axes actually verified, not just claimed.
- notes: one paragraph of honest judgment: strengths, failures at specific sizes, tone fit.
- status: shortlisted, rejected, or adopted, with one line of why.

A shortlist with complete records survives handoffs; one without them restarts from zero every quarter.

## Source logging

- Log the query, not just the destination: "google fonts, filter Devanagari + sans, sorted by popular" is reproducible; "Google Fonts" is not.
- Record exclusion reasons for close calls ("rejected: no true italic", "rejected: RFN complicates planned fork"). Excluded candidates get re-proposed every few months unless the reason is written down.
- Keep the raw materials: specimen screenshots with dates, type tester exports, links to the exact release. Evidence ages; label it.
- Distinguish discovery sources from verification sources. Discovery is where you found it; verification is where you confirmed license and version. Both belong in the record.

## Confidence levels

Use three levels and define them once, project-wide:

- verified: license file read at the source, version confirmed against the file or repository, rendering tested at target sizes. Safe to adopt.
- likely: strong metadata agreement across two sources but no direct file or license inspection yet. Safe to keep on the shortlist, not to ship.
- unverified: seen in a list or a screenshot, nothing checked. Treat as a lead only.

Downgrade confidently when anything contradicts: a mismatch between sources is worse than a single missing check. Upgrades happen by doing the missing check, not by deciding the font "feels fine".

## Turning research into a shortlist

- Start from constraints (scripts, sizes, license scope, technical needs) so the shortlist answers a question rather than collecting favorites.
- Cap the list at five to eight candidates with full records; ten unvetted names is a collection, not a shortlist.
- Include one free and one commercial option per role when budget is unresolved, so the decision conversation is about trade-offs, not availability.
- Attach the scoring rubric you plan to use before scoring; a rubric invented after seeing the candidates quietly bends toward the favorite.

## Workflow

1. Write constraints and roles (heading face, body face, mono, script fallbacks) at the top of the working document.
2. Research per role using catalogs and foundries; log every source as you go, including dead ends.
3. Fill an evidence record for every candidate that survives a first look; assign a confidence level.
4. Re-verify records older than a quarter before scoring; versions and availability move.
5. Score, pick finalists, and freeze the shortlist with a date and an owner; future changes get dated entries.

## Common mistakes

- Screenshot-only research with no source URLs, making every claim unverifiable in a month.
- Recording discovery but never verification, then discovering at handoff that the "free" font was a trial.
- Letting the shortlist grow unbounded because nothing is ever formally rejected.
- Skipping dates, so stale license information gets recirculated as current.
- Keeping evidence in chat threads instead of the manifest, guaranteeing it is lost at the next reorg.

## Decision rules

- No evidence record, no shortlist slot; enthusiasm is not evidence.
- Confidence below verified blocks adoption, no exceptions for deadlines; the deadline is when errors are most expensive.
- When two candidates tie, prefer the one with better documentation culture (foundry or project), because future maintenance tracks it.
- Any change to a frozen shortlist is a new dated entry, never an edit in place.

## Worked example: a filled evidence record

A record earns its keep when a stranger could act on it. Here is the format filled in for a real adoption:

- family: Inter (variable), version 4.x pinned via @fontsource-variable/inter exact release
- source: https://github.com/rsms/inter for upstream; Fontsource package for deployment
- license: OFL-1.1, license file read in package directory; no Reserved Font Name issues for our use
- checked_by: A. Designer; checked_on: 2025-03-14
- coverage: Latin, Latin-ext, Cyrillic verified in glyph grid; Greek confirmed absent, Noto Sans Greek added as fallback
- notes: x-height suits 14 to 16 px UI; numerals default to proportional, tabular figures enabled via font-feature-settings for tables; display sizes above 32 px feel neutral to the point of blandness, headings pair with Fraunces
- status: adopted for product UI; rejected for marketing headlines (tone)

Each line answers a future question. "Why is Greek missing?" and "can we use Inter for the campaign?" are now answered by the record instead of a meeting.

## Confidence levels as a table

| Level | Definition | Allowed uses | Exit criteria |
| --- | --- | --- | --- |
| verified | License read at source, version confirmed against file or repository, rendering tested at target sizes | Adoption, production, client handoff | None; re-verify after a quarter or a version change |
| likely | Two sources agree, no direct file or license inspection | Shortlist slots, budgeting, design exploration | Perform the missing checks |
| unverified | Seen in a list, a screenshot, or a chat thread | Leads for research only | Full verification pass or formal rejection |

Downgrades happen on contradiction, not on elapsed time alone: a mismatch between sources is a worse signal than a single missing check. Upgrades happen by doing the check, never by deciding the font "feels fine".

## Source logging in practice

- Log the query path, not just the destination: the filter combination, the search terms, and the sort order that produced the candidate. "Found on Google Fonts" is not reproducible; "Language: Vietnamese + Serif, sorted by popular, third page" is.
- Screenshot specimens with the date visible or rename files with dates; undated evidence becomes folklore within a quarter.
- Record exclusions with reasons at rejection time. Unwritten rejections resurface every few months as someone's bright idea, and the team relitigates them from zero.
- Separate discovery from verification in the record: where you found it and where you confirmed it are different facts with different URLs.
- Keep the raw materials linked: the type tester export, the release page, the license file path in your repository. Evidence that cannot be re-opened is not evidence.

## Field notes

- Cap the shortlist at five to eight fully recorded candidates; a list of twenty names with no records is a mood board wearing a spreadsheet's clothes.
- Re-verify records older than a quarter before scoring; versions move, foundries fold, licenses get rewritten.
- The rubric gets written before scoring, not after; a rubric invented while looking at candidates bends toward the incumbent favorite every time.
- Include one commercial and one open candidate per role when budget is unresolved, so the decision conversation is about trade-offs rather than availability.
- Freeze the shortlist with a date and an owner; changes after the freeze are new dated entries, never silent edits, because the audit trail is the point.
- When two candidates tie on scores, prefer the better-documented project: maintenance culture predicts your future experience better than any single specimen does.

## Questions to ask before presenting a shortlist

- Can every candidate name its source, license, and version in one line, right now?
- Which records are verified versus likely, and does anyone believe a likely record is ship-ready?
- What did we reject this round, and is every rejection written down with a reason?
- Whose approval freezes this list, and what reopens it?
- If the top pick fails licensing review tomorrow, which candidate inherits its role without restarting research?

## Tool notes

- Keep the shortlist document itself in the repository next to the code it governs; a shortlist that lives only in a design tool is invisible to engineers and auditors.
- A pinned evidence-record template (markdown or YAML) removes the friction of inventing fields per candidate; consistency is what makes records comparable across rounds.
- Screenshots belong in a dated folder with names like candidate-family-2025-03-14.png; the filename is the metadata.
- For packaged families, the Fontsource single-font endpoint can auto-fill subsets, weights, and the variable flag; automate the mechanical fields and spend human time on the judgment fields.
- Diff the shortlist at each freeze: the added and removed lines tell the story of how requirements moved, which is exactly what stakeholders will ask about.
- A one-page summary table (family, role, license, confidence, status) on top of the records gives leadership the answer without dragging them through the details.

## Signals to trust in an existing shortlist

- Records with dates, sources, and named checkers; authorship and timestamps are what separate evidence from opinion.
- Written rejection reasons that still make sense on re-read a quarter later.
- Confidence levels that match the checks actually described in the record, no more and no fewer.
- A frozen list with a named owner, and dated entries for every change since the freeze.
- Exclusion reasons specific enough to be wrong (for example, "no true italic") rather than vague enough to be safe ("did not feel right").

## Cross-references

- [Evaluating catalog metadata](evaluating-catalog-metadata.md)
- [Scoring and shortlisting](../selection/scoring-and-shortlisting.md)
- [Fontsource REST API](fontsource-api.md)
- [Open-source due diligence](../licensing/open-source-due-diligence.md)

Compiled 2025 as part of the Fontlore project.
