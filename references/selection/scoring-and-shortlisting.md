# Scoring and Shortlisting

What this reference covers: A weighted scoring rubric for typeface candidates, a bias-resistant comparison protocol using real copy, and the mechanics of picking three to five finalists. It turns taste arguments into documented, repeatable decisions.

Scoring does not replace judgment; it disciplines it. A rubric forces the team to say what matters before seeing the answers, and a fixed testing protocol keeps the loudest voice in the room from deciding by volume.

## The weighted rubric

Define criteria and weights before looking at candidates. A serviceable default for product work:

- Legibility at real sizes: 25 points. Can users actually read this at 13px in the worst supported environment?
- Tone fit: 20 points. Does it express the brand words in the brief, tested with real copy?
- Technical fitness: 15 points. Variable axes or the weight range you need, true italics, formats, rendering quality.
- Coverage: 15 points. Scripts, diacritics, numerals modes, symbols the product actually ships.
- Licensing and governance: 15 points. License scope matches every usage context; versioning and vendor health are acceptable.
- System fit: 10 points. Plays well with the incumbent (or replaces it cleanly); numerals and metrics align.

Total 100. Adjust weights per project, but write them down first and keep them constant through the round.

## Scoring protocol

- Score all candidates on one criterion before moving to the next (score legibility for all five, then tone for all five). This suppresses halo effects from a favorite's early strength.
- Use the same copy, same sizes, same background, same environment for every candidate; differences other than the font are noise.
- Require evidence notes per score: "7 because it held at 13px in low-DPI test" not "7, feels good".
- Two scorers minimum for anything contentious; average and record disagreements rather than debating them away.
- Cap the scale granularity (whole or half points). Ten-point precision on tone is theater.

## Comparison testing with real copy

- Build one specimen page with rows per candidate: headline, body paragraph, UI label row, data row, and an edge-case row (long words, diacritics, mixed scripts, numerals).
- Use the product's actual vocabulary: feature names, error messages, prices, legal snippets, and the target languages.
- Test the failure modes explicitly: all-caps, tight columns, dark mode, small sizes, user-forced larger text.
- Time-box the review; fatigue makes later candidates look worse than they are. Rotate row order between sessions if the review spans days.
- Screenshot every state; the record feeds the evidence file and survives the meeting.

## Picking 3 to 5 finalists

- From a scored field of 8 to 12, keep three to five that lead on different axes; a mono-criteria shortlist collapses when requirements shift.
- Ensure finalist diversity of trade-offs: one maximal coverage option, one best-tone option, one safest technical option. Finals are decisions between trade-off profiles, not between clones.
- Each finalist gets an evidence record (source, license, version, confidence) before the final round; scoring a candidate you cannot license is wasted motion.
- Name the runner-up and the reason it lost; it is the first candidate when the winner hits a licensing or technical wall.

## Workflow

1. Freeze constraints and rubric weights with the brief; get stakeholder sign-off on the weights, not just the fonts.
2. Assemble candidates from the sourcing shortlist; verify metadata and license before scoring.
3. Build the comparison specimen page and run the scoring protocol with at least two scorers.
4. Tally, write the trade-off narrative (three paragraphs maximum), and pick finalists.
5. Run finalists through the real product (a staging page, a real email) before final adoption; the lab is never quite the field.
6. Record the decision, the scores, and the losing candidates' reasons in the font manifest.

## Common mistakes

- Inventing weights after seeing candidates, then defending the favorite with post-hoc criteria.
- Scoring tone from a specimen page instead of the brand's real sentences.
- Letting one stakeholder's laptop or monitor become the evaluation environment.
- Comparing candidates at matched point sizes instead of matched x-heights (see the x-height guide).
- Keeping ten "finalists" because nobody will do the killing; a shortlist that short is a mood board.
- Skipping the licensing check until after the winner is announced, then renegotiating the whole round.

## Decision rules

- If two candidates tie, the tiebreaker is governance: better documentation, healthier upstream, cleaner license.
- If the top scorer fails licensing, promote the runner-up; do not bend the product around a license mismatch.
- One strong dissent on legibility from a credible reader is a veto, not an opinion to outvote.
- Re-score only when constraints change; re-scoring to reach a preferred answer corrupts the whole method.

## Worked example

A scored round for a B2B analytics product choosing one UI sans, run exactly as the protocol prescribes. Weights fixed before any candidate was opened: legibility 25, tone fit 20, technical fitness 15, coverage 15, licensing and governance 15, system fit 10. Two scorers, whole points only.

| Candidate | Legibility (25) | Tone (20) | Technical (15) | Coverage (15) | Governance (15) | System fit (10) | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Inter | 23 | 15 | 15 | 14 | 15 | 9 | 91 |
| Source Sans 3 | 22 | 16 | 14 | 14 | 15 | 9 | 90 |
| Work Sans | 21 | 17 | 14 | 13 | 15 | 8 | 88 |
| IBM Plex Sans | 22 | 18 | 14 | 14 | 15 | 9 | 92 |
| Public Sans | 21 | 14 | 13 | 13 | 15 | 9 | 85 |

Reading the table the disciplined way:

- Scores were entered criterion by criterion across all candidates; row totals were computed last, never eyeballed first.
- Inter took legibility on the low-DPI test; IBM Plex Sans took tone because the product's engineering brand wanted Plex's angular terminals.
- Work Sans lost system-fit points: its figure rhythm clashed with the incumbent's tabular numerals in mixed tables.
- The one-point spread between Inter and IBM Plex Sans is inside scorer variance; the recorded tone evidence, not the totals, decided it.
- Public Sans scored high on governance and low on tone for this brand; "neutral" was the wrong voice for a product selling analytical confidence.
- Licensing was verified before scoring, so no candidate died after the announcement; the round cost two afternoons, not two months.
- Outcome: IBM Plex Sans adopted; Inter recorded as runner-up with its reason (legibility margin, tone deficit against the brand words); scorecard and screenshots filed in the manifest.

The scores are illustrative, not endorsements of any ranking; the pattern to copy is evidence-based scoring, not the numbers themselves.

## Comparison table

The rubric as an evidence table. A criterion nobody can produce evidence for is a criterion to delete, not to guess.

| Criterion | Weight | The question | Evidence that earns points |
| --- | --- | --- | --- |
| Legibility at real sizes | 25 | Can users read this at 13px in the worst environment? | Low-DPI screenshots at target sizes, both color modes, notes per size |
| Tone fit | 20 | Does it express the brand words with real copy? | Side-by-side rows with the brand's sentences; forced-choice results |
| Technical fitness | 15 | Does it ship the weights, italics, and axes you need? | Feature list verified against the brief; variable instances sampled |
| Coverage | 15 | Does it cover the scripts and symbols you ship? | Rendered checks for every locale; diacritics, currency, math symbols |
| Licensing and governance | 15 | Does the license match every usage context? | License text read against use cases; upstream activity and versioning noted |
| System fit | 10 | Does it coexist with the incumbent? | Matched x-height check; numerals rhythm in mixed tables |

Weights are project-specific: freeze them before candidates are opened, keep them constant through the round, and get stakeholder sign-off on the weights, not just the fonts.

## Field notes

- Freeze the rubric before opening a single specimen; the first candidate you see quietly rewrites your weights.
- Score one criterion across all candidates before moving on; halo effects are stronger within a row than within a column.
- Whole points only: decimal precision on tone is a costume for certainty nobody has.
- Two scorers with different jobs (one design, one engineering) catch different failures; same-role scorers catch the same ones.
- Screenshots outlive meetings; capture every state or the evidence dies in the room.
- Rotate row order between sessions; later rows look worse to tired eyes, and order bias is real.
- A tie is not a problem to break with another criterion; it is a trade-off profile to present to the decision owner.
- Runner-ups are assets: record why each lost and the wall it would take to bring it back.
- The lab never matches the field; run finalists through a staging page or a real email before adoption.
- Re-scoring after seeing results corrupts the method; constraints changed means re-run, preferences changed means stop.
- Beware the candidate everyone calls "safe"; safety is a score on the governance line, not an excuse to skip the others.
- Fatigue is measurable in scores; three candidates per session keeps the later rows honest.
- Evidence notes beat adjectives: "held at 13px on the 2019 laptop" is a fact; "readable" is a mood.
- If a candidate wins on tone but loses on legibility, it is a display candidate, not a body candidate; re-slot it instead of re-scoring it.
- Disagreements between scorers are data; record them, average them, and let the tiebreak rules work.
- The scorecard is a decision record, not a verdict on the faces; keep it humble and it stays useful.

## Quick reference

- Define weights first, in writing, with stakeholder sign-off on the weights and not just the fonts.
- Default product weights: legibility 25, tone 20, technical 15, coverage 15, governance 15, system fit 10.
- Score criterion-by-criterion across all candidates; compute totals last.
- Require an evidence note per score; no evidence, no points.
- Two scorers minimum for contentious rounds; average and record disagreements.
- Whole or half points; cap the granularity.
- Same copy, same sizes, same background, same environment for every candidate.
- Match x-heights, not point sizes, when comparing across classes.
- Shortlist three to five from eight to twelve, with diverse trade-off profiles.
- Verify licensing before scoring; scoring a candidate you cannot license is wasted motion.
- Name the runner-up and the reason; it is the first fallback.
- One credible dissent on legibility is a veto, not an opinion to outvote.
- Re-score only when constraints change, never to reach a preferred answer.
- File the scorecard, screenshots, and rejection reasons in the manifest.
- Run finalists in the real product before adoption; the lab is not the field.
- Tiebreak on governance: documentation, upstream health, license clarity.

## Cross-references

- [Choosing body typefaces](choosing-body-typefaces.md)
- [Personality and tone](personality-and-tone.md)
- [Building a font shortlist with sources](../sourcing/building-a-font-shortlist-source.md)
- [License audit checklist](../licensing/license-audit-checklist.md)

Compiled 2025 as part of the Fontlore project.
