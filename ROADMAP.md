# Roadmap

## Current status: v1.0 shipped

- Data layer: 165 font records, 66 curated pairings, 71 tool entries, all validated by scripts/validate.py with null-over-invented and https-only policies.
- References: 95 curated references across 9 categories (sourcing 10, selection 10, identification 10, licensing 15, scripts 10, technical 10, accessibility 10, applications 10, workflow 10).
- Generated guides: 632 (495 per-font + 66 per-pairing + 71 per-tool), 727 guides and references in total.
- Decision engine: scripts/decide.py, the weighted rubric documented in MASTER-SKILL.md, with hard filters, scored reasons, and curated pairing suggestions.
- Quality gate: scripts/validate.py enforcing the data schema, the markdown house style, and script compilation; CI runs it on every push and PR to main.
- Site: the Fontlore site with tabbed browsing (Fonts / Pairings / Tools / nine reference categories) built from this data layer.

## Planned

These are directions we intend to work in, in no strict order. We have not committed to dates; promises of quarters and weeks age badly, so none appear here.

- More scripts coverage: the current data layer is strongest in Latin, Devanagari, Arabic, and Hebrew; deeper coverage for Thai, CJK families, Tamil, Myanmar, and Ethiopic is the largest known gap, and decide.py's script filter makes new entries immediately usable.
- Per-context generated guides expansion: growing the 632 generated guides to 1000+ as the data layer grows, with per-context variants (dashboards, ecommerce, editorial) rather than only per-record pages.
- Foundry partnerships for verified metadata: working with foundries and catalogs so license, weight, and axis data arrives signed at the source instead of reconciled by hand.
- Multi-language references: translating the 90 references, starting with the licensing and scripts categories, without weakening the ASCII validation contract for the English canon.
- Agent eval harness: a graded set of briefs (constraint extraction, shortlisting, pairing, license verification) that scores an agent's end-to-end use of this skill, so skill changes can be measured rather than guessed.
- Pairing data growth beyond the current 66 records, prioritized by the contexts decide.py users actually query.

## Guiding principles for what gets built

- Anything added must survive the validator; convenience never outruns the quality gate.
- Coverage gaps are addressed where agents actually fail: scripts with no candidates, contexts with no curated pairings, licenses without plain-language guidance.
- The rubric stays inspectable: if a scoring change cannot be explained in one paragraph, it does not ship.
- The site and the repository share one source of truth for counts and data; features that fork the truth are rejected.
- Accessibility and licensing references are treated as load-bearing; changes there need the same care as schema changes.

## Non-goals

- Hosting or redistributing font files; we link to sources under their own licenses.
- Recommending commercial fonts by default; open licenses stay the default filter.
- Rankings based on popularity metrics; the rubric scores fit, not fame.
- Chasing every catalog API for its own sake; a source earns data-layer status when its metadata can be verified at the origin.

## How to influence the roadmap

Open a Discussion with a concrete proposal and the evidence for it. Data additions that survive validation merge faster than roadmap debates; if you want more script coverage, contributing the entries is the most direct path. Proposals that change the rubric, the schema, or the house style need a written case and maintainer sign-off, because every downstream consumer inherits the change.
