# Fontlore: Typeface Intelligence

Fontlore is an open-source typeface-intelligence skill for AI agents: a curated data layer of 165 fonts, 66 pairings, and 71 tools, backed by 95 curated references across 9 categories and 632 generated guides (727 guides and references in total). It exists so an agent can go from a project brief to a defensible font decision without inventing facts, guessing licenses, or recommending faces it cannot verify. Every claim in the data layer carries a source URL, unverifiable values are null rather than guessed, and every recommendation can be re-derived from the data.

## When to use this skill

Load this skill when the task involves:

- Selecting fonts: choosing a family for a webapp, dashboard, marketing site, editorial product, ecommerce store, brand system, or documentation set.
- Pairing: choosing a heading and body combination, with 66 curated pairings and contrast rules as backup.
- Identifying: working out which font is in a screenshot, logo, or PDF, with a tool-driven verification workflow.
- Licensing checks: confirming what a license permits before a font ships, with license-family references and audit checklists.
- Implementing webfonts: loading strategies, subsetting, fallback metrics, and CSS handoff.
- Building type systems: scales, tokens, multi-script coverage, and governance for a product or organization.

## Quick start

The canonical agent workflow, end to end:

1. Read the brief. Extract what the project actually needs, not what the client says they want. Walk through references/workflow/brief-to-constraints.md and write the constraint sheet.
2. Extract constraints. Scripts and languages required, surfaces, license scope, performance budget, accessibility floor, brand constraints. Hard lines only; preferences lose to beauty, constraints do not.
3. Hard-filter data/fonts.json. Keep only records where license fits the budget, scripts include every required script, and category matches the role. A font that fails a hard constraint is out regardless of how it looks.
4. Score and shortlist 3-5. Use the rubric in MASTER-SKILL.md or run scripts/decide.py (see "Decision engine" below). Keep the reasons attached to each candidate.
5. Pair using data/pairings.json. If a curated pairing covers your shortlist, start there. If not, fall back to the contrast rules in references/selection/superfamily-and-family-systems.md and MASTER-SKILL.md Stage 3.
6. Verify the license at the source URL. Every font record has a source field pointing at the foundry or catalog page. Read the license there; do not trust third-party aggregators.
7. Test with real copy. The client's actual headlines, legal text, numerals, and every required script, at production sizes. references/scripts/testing-multilingual-coverage.md is the checklist.
8. Deliver with evidence. Top pick plus two alternates, reasons, license evidence, weights and styles needed, fallback stack, and a CSS snippet (Stage 5 of MASTER-SKILL.md).

references/workflow/brief-to-constraints.md and references/workflow/research-workflow.md are the canonical walkthroughs for steps 1 through 5. Read them before your first run.

## Repository map

| Path | What it contains | Count |
| --- | --- | --- |
| data/fonts.json | Font records: identity, classification, scripts, license, source URLs | 165 |
| data/pairings.json | Curated heading-plus-body pairings with context and rationale | 66 |
| data/tools.json | Tools: catalogs, APIs, inspectors, identification services | 71 |
| references/sourcing/ | Where to find fonts: catalogs, foundries, regional sources | 10 |
| references/selection/ | How to choose: classification, tone, scoring, x-height | 10 |
| references/identification/ | How to identify a font from an image or specimen | 10 |
| references/licensing/ | License families, OFL details, embedding rights, audits | 15 |
| references/scripts/ | Per-script typography: Latin, Arabic, Devanagari, CJK, and more | 10 |
| references/technical/ | Formats, loading, subsetting, variable fonts, OpenType features | 10 |
| references/accessibility/ | WCAG for type, contrast, zoom, dyslexia, RTL | 10 |
| references/applications/ | Per-context practice: dashboards, ecommerce, editorial, chat | 10 |
| references/workflow/ | End-to-end process: briefs, research, presentation, governance | 10 |
| guides/ | Generated guides, one per font, pairing, and tool: 495 per-font + 66 per-pairing + 71 per-tool | 632 |
| scripts/decide.py | The decision engine CLI (see below) | 1 |
| scripts/validate.py | The repository quality gate (see below) | 1 |
| scripts/build_data.py | Rebuilds the data layer from its source tables | 1 |

That is 95 curated references across 9 categories, 632 generated guides, 727 guides and references in total. Font categories in the data: sans-serif 87, serif 42, display 16, monospace 11, handwriting 9.

## Data files

All three data files share the same shape: a top-level count field matching the array length, plus the array itself. Fields that could not be verified are null, never invented.

### data/fonts.json (165 records)

| Field | Type | Meaning |
| --- | --- | --- |
| slug | string | Lowercase hyphenated identifier, e.g. "inter". The join key for pairings. |
| family | string | Display name, e.g. "Inter". |
| designer | string | Named designer(s), or null if unverified. |
| foundry | string or null | Publishing foundry or vendor, or null (many OFL releases are self-published). |
| license | string | One of: OFL-1.1, Apache-2.0, UFL-1.0, ITF-FFL-1.0, MIT, Custom-OFL-based. |
| category | string | One of: sans-serif, serif, display, monospace, handwriting. |
| classification | string | Finer grain: grotesque, humanist, geometric, transitional, mono, didone, old-style, slab, condensed, rounded, naskh, and others. |
| scripts | list | Scripts the font covers, e.g. ["latin", "devanagari"]. Conservative: only verified coverage. |
| subsets | list | Available unicode-range subsets for web loading. |
| variable | bool | True if a variable build exists. |
| axes | list | Registered and custom axes, e.g. ["wght", "wdth"]. Empty for static fonts. |
| weights | list or null | Static weight values where known; null when the family is variable or the set is unverified. |
| source | https URL | Where the font actually lives: foundry page or canonical catalog page. Verify licenses here. |
| specimen | https URL | Where to test the font with your own text. |
| note | string | One-line factual description of the face. |
| tags | list | Free-form search terms, e.g. ["ui", "neutral", "variable"]. |

### data/pairings.json (66 records)

| Field | Type | Meaning |
| --- | --- | --- |
| id | string | Stable identifier, e.g. "pair-001". |
| heading | string | Slug of the heading font. Must exist in fonts.json. |
| body | string | Slug of the body font. Must exist in fonts.json, never equals heading. |
| context | string | Intended use, e.g. "tech-saas", "editorial-magazine", "fintech-product". |
| rationale | string | Why the pairing works, in one sentence. |
| kind | string | Pairing pattern, e.g. "contrast-plus-neutral", "family-system", "superfamily". |

### data/tools.json (71 records)

| Field | Type | Meaning |
| --- | --- | --- |
| name | string | Tool name, unique across the file. |
| url | string | https URL to the tool. |
| section | string | One of: catalogs, apis, source-repos, identification, licensing, technical, tooling, pairing, discovery, foundries, scripts, accessibility, education, evidence, creation, commercial. |
| what | string | What the tool does, in one sentence. |
| access | string | Access model: free, freemium, paid, and similar. |

## Decision engine

scripts/decide.py is the deterministic core of this skill. It hard-filters fonts.json by script and license, scores the survivors against the rubric in MASTER-SKILL.md, and prints a ranked shortlist with reasons plus curated pairings that touch the shortlist. It is stdlib-only, needs no network, and gives identical output for identical input.

```bash
# Dashboard project, Latin only, neutral tone, top 5 (default)
python3 scripts/decide.py --project dashboard --script latin --tone neutral

# Fintech dashboard that must render Hindi, open licenses only
python3 scripts/decide.py --project dashboard --script devanagari --tone neutral --open-only --top 8

# Machine-readable output for an agent pipeline
python3 scripts/decide.py --project webapp --script latin --tone technical --json
```

Arguments: --project (webapp, dashboard, marketing, editorial, ecommerce, brand, docs), --script (latin, devanagari, arabic, hebrew, thai, japanese, korean, chinese-simplified), --tone (neutral, friendly, editorial, technical, playful), --open-only (default on; disable with --no-open-only), --top N (default 5), --json.

What it guarantees: no font outside the required script survives the filter; no font outside the open-license set survives when --open-only is on; every score is decomposable into the named reasons printed beside it; suggested pairings are limited to the 66 curated records, so no pairing is invented on the spot.

What it does not do: it cannot see your actual brief, verify a license change at the foundry, or test the font with your copy. Those steps stay with you (Quick start steps 1, 6, and 7).

## Validation

scripts/validate.py is the repository quality gate. Run it before every commit; CI runs it on every push and pull request to main.

```bash
python3 scripts/validate.py            # full check
python3 scripts/validate.py --data     # data layer only
python3 scripts/validate.py --docs     # markdown house style only
```

It enforces: JSON parseability and count-field consistency; required fields on every font record; licenses within the accepted set; https-only URLs; no static font declaring axes; pairings that reference existing font slugs with no self-pairings and no duplicate direction-agnostic pairs; unique tool names; pure-ASCII markdown with exactly one H1 per reference or guide; the "What this reference covers:" intro rule; the 140-320 line house range; 2-5 resolving cross-references per reference; the exact footer line; and Python compilation of every script in scripts/.

## Rules

These are non-negotiable. They override anything else in this skill:

- Null over invented values. If a fact cannot be verified from the data or the source URL, say "unverified" or write null. Never guess a designer, weight list, or license.
- License before aesthetics. A beautiful face that fails the license scope is the wrong answer. Check the license at the source URL before the font enters any shortlist.
- Popularity is a weak prior. Widely used fonts are widely used partly because they are default-shaped; that is a starting point for search, not a reason. Score on fit, not fame.
- Verify at the foundry source. Aggregators go stale and vendors fork. The source field is the truth; read the license text there, especially before embedding, redistribution, or logo use.
- State uncertainty. When coverage, licensing, or identification is not certain, say so in the deliverable and name what would settle it. A decision with labeled uncertainty is usable; a confident guess is not.
