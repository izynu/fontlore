# Master skill: from project brief to font decision

What this covers: the full decision pipeline this repository implements - extracting constraints from a brief, hard-filtering the 165-font data layer, scoring survivors against a weighted rubric, pairing the shortlist, verifying licenses at the source, and emitting a deliverable an agent can defend. scripts/decide.py is this document compiled into a CLI; when this document and the script disagree, fix one of them in the same commit.

## Inputs

Answer these 8 questions about any project before touching the data. If a question cannot be answered from the brief, ask; if nobody knows, record the assumption in the deliverable.

1. Medium: webapp, dashboard, marketing site, editorial product, ecommerce, brand system, or documentation? This selects the primary role categories in Stage 2.
2. Audience: who reads this, on what devices, at what sizes, in what lighting? Dense data tools and long-form reading pull toward different classifications.
3. Scripts: which scripts must render on day one, and which are on the 12-month roadmap? List exact languages, not script families.
4. Text volume: is this interface chrome (labels, tables) or sustained reading? Interface work favors sans-serif and monospace; reading favors serif or highly readable sans.
5. Sizes: smallest and largest sizes in the product? Tiny UI text and large display work constrain x-height and optical-size behavior.
6. License constraints: zero budget, open-source product, embedding needs, seat counts, redistribution? This is a hard filter, not a preference.
7. Performance budget: total font payload per page, file-count limits, whether variable builds are required to stay inside it.
8. Brand tone: neutral, friendly, editorial, technical, playful? This drives the tone-classification match in Stage 2.

## Stage 1: hard filters

Eliminate fonts that fail a hard constraint before any scoring. Three fields do the work:

- License scope: font.license must fit the project's budget and distribution model. With open-only rules (the default), the accepted set is OFL-1.1, Apache-2.0, UFL-1.0, ITF-FFL-1.0, MIT; Custom-OFL-based records need a manual read of the upstream license before use.
- Script coverage: font.scripts must include every required script. A font missing Devanagari is out of an English-plus-Hindi project, no matter how good it looks. Run the filter against the scarcest script first; it eliminates the most candidates.
- Category: font.category must match a role the project actually needs. A dashboard needs sans-serif and monospace roles; a handwriting face cannot fill them.

In decide.py these are the --script, --open-only, and category-fit checks. A font that fails any hard filter is out regardless of its score. Never resurrect a filtered font without a written license or coverage change.

## Stage 2: scoring

Score every survivor on the weighted rubric. The weights are named constants in scripts/decide.py and sum to 100:

| Criterion | Weight | Full marks | Partial | Zero |
| --- | --- | --- | --- | --- |
| Category fit | 30 | font.category is a primary role for the project type | secondary role (0.6 of the weight) | other roles (0.2) |
| Tone-classification match | 25 | font.classification reads as the requested tone | adjacent classification (0.5) | mismatch (0.1) |
| Variable build | 15 | font.variable is true | - | static |
| Script coverage | 15 | 6 or more entries in font.scripts | proportional below 6 | none beyond the required script |
| Open license | 15 | license in the open set | - | not in the open set |

Primary and secondary roles per project type (from CATEGORY_FIT in decide.py):

| Project | Primary categories | Secondary |
| --- | --- | --- |
| webapp | sans-serif | serif, monospace |
| dashboard | sans-serif, monospace | serif |
| marketing | sans-serif, display | serif |
| editorial | serif | sans-serif, display |
| ecommerce | sans-serif, display | serif |
| brand | display | sans-serif, serif, handwriting |
| docs | sans-serif, monospace | serif |

Tone-classification sets (from TONE_MATCH in decide.py): neutral reads grotesque, humanist, geometric; friendly reads geometric, humanist, rounded; editorial reads old-style, transitional, didone, mincho; technical reads mono, grotesque, techno, squared; playful reads rounded, casual, script, marker, brush.

Thresholds: 85 and above is a strong candidate; 60 to 84 is shortlistable with stated caveats; 40 to 59 only survives in a thin pool, and the thinness is part of the answer; below 40 is out. Ties are broken alphabetically by family for determinism, and the tie itself is a signal that the top candidates need a differentiator from the brief, not from the rubric.

Run it:

```bash
python3 scripts/decide.py --project dashboard --script latin --tone neutral
python3 scripts/decide.py --project dashboard --script devanagari --tone neutral --open-only --top 8
python3 scripts/decide.py --project webapp --script latin --tone technical --json
```

Every printed score decomposes into the printed reasons. If you cannot read a score back into its reasons, treat it as a bug and fix the tool.

## Stage 3: pairing

Check data/pairings.json first. All 66 records are curated, reference existing slugs, and carry a rationale; a pairing that touches your shortlist beats an invented one. decide.py prints up to 3 of them under "Suggested pairings:".

If no curated pairing covers the shortlist, pair by classification contrast rules:

- Contrast pairing: a high-energy or high-contrast heading face over a calm body face (contrast-plus-neutral, character-plus-workhorse patterns). Keep the pair different in one dimension, not five.
- Family system: one superfamily for everything, or siblings from the same design program (family-system, superfamily kinds). Safest for dense products; least distinctive.
- Same-classification duets: two grotesques at different temperatures for news-like products (grotesque-duet). Works when the pair differs in width or weight range rather than skeleton.
- Avoid: two personalities fighting for the same job, a body face with a smaller or wildly different x-height than the heading, and any pair where both faces are display-grade.

references/selection/superfamily-and-family-systems.md is the deep reference for family systems; references/selection/classification-primer.md explains the classification vocabulary used here.

## Stage 4: verification

Three checks before a candidate becomes a recommendation:

- License check at the source URL. Open font.source and read the license on the foundry or catalog page. Aggregators go stale; the foundry is the truth. Confirm the license name matches the data, and check embedding and redistribution clauses against the project's surfaces. references/licensing/license-audit-checklist.md is the audit.
- Specimen test. Open font.specimen, paste real project copy (headlines, legal text, numerals, UI labels), and check the required weights and styles exist in the actual build.
- Multilingual test, if any roadmap language is in play. Render the required script at production sizes and check shaping (conjuncts, tone marks, ligatures) with real words. references/scripts/testing-multilingual-coverage.md is the checklist and includes tool-based verification with document.fonts.check() and fonttools.

A candidate that fails verification drops out and the next ranked candidate takes its place. Record what failed; the reason is reusable evidence.

## Stage 5: output contract

Deliver decisions in exactly this shape. It is what an agent owes its caller and what a reviewer can audit:

- Top pick: family name plus slug, with a one-paragraph reason tied to the brief's constraints.
- Two alternates: each with the reason it differs from the top pick and when to prefer it.
- Reasons: the scored dimensions (category fit, tone, variable, coverage, license) restated against this brief, not generic praise.
- License evidence: license name, source URL where it was verified, and the date of verification.
- Weights and styles: the exact weights and styles the product needs, confirmed to exist (font.weights when listed, otherwise verified at the specimen).
- Fallback stack: the CSS font-family chain including system fallbacks, chosen for metric similarity. references/technical/fallback-metrics-and-cls.md explains why this matters.
- CSS snippet: a minimal @font-face or link-based implementation with font-display and unicode-range notes where relevant.

Mark anything unverified as unverified. The contract is the place where uncertainty is stated, not hidden.

## Worked example

Brief: "a fintech dashboard, English and Hindi, open licenses only." Walk the pipeline:

1. Inputs: medium dashboard; audience is banking customers on mid-range Android; scripts latin and devanagari (Hindi at launch); interface text plus some reading; sizes 12 to 32 px; license constraint open-only; performance budget 120 KB per page; tone neutral with a trustworthy feel.
2. Stage 1: run the filter on the scarcest script first. Devanagari is scarcer than Latin, so:

```bash
python3 scripts/decide.py --project dashboard --script devanagari --tone neutral --top 6
```

Real output from the current data layer (165 fonts, 13 cover Devanagari):

```
rank family                    score class          license      reasons
------------------------------------------------------------------------
1    Poppins                   92    geometric      OFL-1.1      category fit: sans-serif is a primary role for dashboard; tone match: geometric reads neutral; variable build: wght; script coverage: 3 script ranges listed; open license: OFL-1.1
2    Noto Sans Devanagari      88    grotesque      OFL-1.1      category fit: sans-serif is a primary role for dashboard; tone match: grotesque reads neutral; variable build: wght; script coverage: 1 script ranges listed; open license: OFL-1.1
3    Hind                      78    humanist       OFL-1.1      category fit: sans-serif is a primary role for dashboard; tone match: humanist reads neutral; script coverage: 3 script ranges listed; open license: OFL-1.1
4    IBM Plex Sans Devanagari  78    humanist       OFL-1.1      category fit: sans-serif is a primary role for dashboard; tone match: humanist reads neutral; script coverage: 3 script ranges listed; open license: OFL-1.1
5    Mukta                     78    humanist       OFL-1.1      category fit: sans-serif is a primary role for dashboard; tone match: humanist reads neutral; script coverage: 3 script ranges listed; open license: OFL-1.1
6    Baloo 2                   70    rounded        OFL-1.1      category fit: sans-serif is a primary role for dashboard; tone mismatch: rounded fights neutral; variable build: wght; script coverage: 3 script ranges listed; open license: OFL-1.1
```

3. Stage 1, second pass: the project is English plus Hindi, so each candidate must also cover latin. Checking font.scripts: Poppins, Hind, IBM Plex Sans Devanagari, Mukta, and Baloo 2 all list latin; Noto Sans Devanagari lists devanagari only, so as a single-family body pick it fails the second hard filter - but the curated pairing "Noto Sans Devanagari + Noto Sans - indic-multilingual" is exactly the two-family answer to that gap, which is why pairing data exists.
4. Stage 2: scores stand as printed. Poppins leads at 92; the humanist trio (Hind, IBM Plex Sans Devanagari, Mukta) sits at 78; Baloo 2's rounded classification fights the neutral tone and it lands at 70.
5. Stage 3: suggested pairings from the run include "Poppins + Lato - startup-landing" and "Noto Sans Devanagari + Noto Sans - indic-multilingual". For a single-family body, Poppins covers both scripts; for the most conservative Hindi shaping, the Noto pairing wins. Hind exists precisely as a Devanagari-plus-Latin UI family, which keeps it in the alternates.
6. Stage 4: verify OFL-1.1 at each source URL (Google Fonts specimen pages in the current data), confirm weights at the specimen, and run the conjunct smoke test from references/scripts/devanagari-script-typography.md at 12, 14, and 16 px on a mid-range Android device.
7. Stage 5: deliver top pick Poppins (both scripts, variable wght, OFL-1.1), alternates IBM Plex Sans Devanagari (more mechanical, engineered pairing with IBM Plex Sans) and Mukta (broad Devanagari conjoined coverage, conservative forms), with license evidence, the exact weight list, a fallback stack, and the CSS snippet per the output contract.

## Edge cases

- The client brings a commercial font. It can still win - open-only is a project constraint, not an ideology. Treat the commercial license as a hard filter to check manually: seats, embedding, webfont hosting, and the renewal owner. Remove --open-only from the decide.py run (--no-open-only) and record the license evidence in the deliverable.
- Script coverage gaps. The required script has few or zero candidates (the Devanagari pool here is 13 of 165; some scripts are fewer). Report the thin pool honestly, fall back to the Noto families for coverage, and flag that a two-family system (script-specific face plus a Latin workhorse) is the standard answer, not a compromise.
- No pairing data for the shortlist. decide.py prints "none of the 66 curated pairings involve this shortlist". Do not invent a pairing record; apply the Stage 3 contrast rules manually and say in the deliverable that the pairing is derived, not curated.
- Variable axes conflicts. Two variable faces with overlapping axes (both with wdth, both with opsz) can fight in a shared type scale. Freeze the axes in the tokens, or prefer a single family-system for the axes-heavy surfaces. references/technical/variable-fonts-and-axes.md covers the mechanics.
- RFN forks. An OFL Reserved Font Name means forked builds cannot use the original name. If the project serves a modified build, the CSS family name and the license evidence must reflect the fork, and the original's name stays out of the stack.
- Trial fonts. Trial builds are for evaluation only: they often lack glyphs, carry embedding restrictions, and expire. Never let a trial font reach the output contract's weights-and-styles line; pair any trial with a purchase decision date and a full-build retest.
