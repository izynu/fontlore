# Testing and Comparing Shortlists

What this reference covers: Building specimen tests with the project's real copy, running side-by-side comparison matrices, using size ramps, and scoring candidates so a shortlist becomes a decision. Specimens show fonts at their best; tests show fonts at your worst-case, which is the only case that matters.

## Real copy or nothing

Generic specimen text (pangrams, marketing slogans) hides exactly the problems fonts have in production. Build the test corpus from the project:

- The longest product name, the longest headline, the shortest button label, the densest table, a real error message, a real address, a real date range, a currency amount, and one piece of long-form copy from the actual content.
- The full language set from the constraint sheet: real paragraphs in every launch language, pulled from the UDHR translations or the product's own content.
- Edge inputs: all-caps UI strings, user names with mixed scripts, emoji in context, numbers of every shape (prices, percentages, phone numbers, IDs).

One HTML file with a section per candidate and the same corpus in each is the entire tooling needed; build it once, reuse it forever.

## The side-by-side matrix

For each candidate family, render the same blocks in the same order:

1. Body paragraph at production size and measure (the values from the constraint sheet, not arbitrary ones).
2. The UI strip: nav, button row, form field, status label, error message at their production sizes.
3. Headline stack: display size, section heading, card title.
4. Data block: table with tabular figures, price, timestamp, ID in mono if the system uses one.
5. Language blocks: every launch language, same paragraph, at body size.
6. Feature checks: bold, italic (if used), tabular numerals, small caps (if used).

Read each column at each block and note failures against the block's job; a matrix entry is a judgment ("crumbles at 13 px labels"), not a vibe.

## Size ramps and stress settings

- Size ramp: each candidate at 12, 14, 16, 20, 32, 48, 72 px equivalents in one column; UI faces must survive 12 to 16, display faces 32 and up. Failure at a size you ship is disqualifying, whatever the rest looks like.
- Weight ladder: set the same paragraph in every shipped weight; gaps between weights (missing 500) or mushy bolds appear immediately.
- Tracking and case stress: the all-caps label style, the tracked kicker, the tight display leading; apply your actual production CSS values.
- Script stress: the language blocks at production line-height, including the tall-mark scripts; this is where line-height and coverage failures surface.
- Rendering stress: screenshots on Windows at small sizes and, for CJK or complex scripts, in a second browser; platform differences are real and recurring.

## Scoring without pretending it is math

A simple rubric keeps discussions honest; scores are structured opinions, not measurements:

- Legibility at production sizes (1-5): the body and UI blocks.
- Coverage and shaping (pass/fail per language): a hard gate, not a score.
- Hierarchy range (1-5): do the weights and styles build the system the design needs?
- Data typography (1-5 or pass/fail): tabular figures, alignment, mono quality if relevant.
- Fit to voice (1-5): the only taste entry; score it as a group, not by fiat.
- License and logistics (pass/fail plus notes): verified in research.

Hard gates first (coverage, license, tabular figures): anything failing is out regardless of score. Then compare scores; a tie is broken by fit to voice and by evidence of proven performance in similar contexts.

## Deciding and recording

- Rank survivors, keep the top three for the stakeholder presentation (see the presenting reference); record scores and the corpus used.
- Note per candidate what tuning it needs (size bumps, leading adjustments, per-language rules): these become the CSS handoff, and a candidate needing heavy tuning is a real cost.
- Archive the comparison page with the version of each font tested; decisions get re-audited against the artifacts, and the artifacts must show what was actually seen.

## Common mistakes

- Comparing fonts at sizes the project never uses; a 72 px showcase means nothing to a 13 px dashboard.
- One language tested, five shipped; the missing languages fail later, in production, in front of users.
- Scoring before hard gates, so a font with broken Vietnamese wins on charm.
- Testing in the design tool only; Figma rendering is not Windows ClearType, and the difference is the decision.
- Letting the loudest stakeholder's taste override a recorded hard-gate failure; the matrix exists to prevent exactly that.
- No tuning notes: the chosen font ships with default leading and the wrong numeral style, and nobody remembers why it looked better in the test.

## Decision rules

- Hard-gate failure: out, no appeals; record the gate and the reason.
- Two candidates tie: run one more round with new, harder copy (longer, denser, more languages), not with more opinions.
- A candidate needs tuning to win: acceptable if the tuning is written into the handoff; not acceptable if it depends on per-page fixes.
- The winner on scores loses on voice with the stakeholder: present the evidence, then let voice break the tie consciously and record that it did.
- Any change of corpus, size, or settings mid-comparison: re-run all candidates; a matrix is only valid under identical conditions.

## Quick reference: the standard corpus blocks

| Block | Contents | What it reveals |
| --- | --- | --- |
| Longest headline | The longest real title at display size | Tracking, wrapping, repeated-letter collisions |
| Body paragraph | Two paragraphs of the actual long-form copy at production size and measure | Rhythm, color, comfort over a real read |
| UI strip | Nav labels, buttons, form field, status badge, error message at production sizes | Small-size survival, letterform disambiguation |
| Data block | Table with prices, timestamps, IDs | Tabular figures, digit width consistency, alignment |
| Language blocks | One paragraph per launch language | Diacritics, shaping, vertical metrics |
| Edge inputs | All caps, mixed-script user names, emoji neighbors, every numeral shape | Case mapping, fallback behavior, punctuated strings |
| Measure sweep | The body paragraph at narrow, production, and wide measures | Rivers and one-word lines at the extremes |
| Export block | The PDF or report surface, if the constraint sheet names one | Rendering outside the browser before it becomes a launch surprise |

Build the corpus once per project from the constraint sheet and version it with the comparison artifacts; a corpus that drifts between rounds invalidates the scores recorded against it.

The corpus is versioned text, not vibes: store it beside the comparison page. When a later dispute asks what the decision was based on, the corpus plus the archived matrix is the complete answer. Reusing last year's corpus is allowed and encouraged; the version history then shows what the project learned between selections.

## Worked example: two body faces for a documentation site

Shortlist of two after research: a sturdy text serif and a neutral grotesque, both OFL, both with the needed Cyrillic.

1. Corpus: the real getting-started guide (two paragraphs), the real API error strings, a table of rate limits, German and Polish paragraphs, and a code snippet in mono context.
2. Size ramp at production sizes only (14, 16, 20 px): the serif held its color better at 14 px; the grotesque won the 20 px intro text on openness.
3. The UI strip killed nothing but exposed tuning: the grotesque's all-caps labels needed 0.01em tracking to match the serif's; recorded as a handoff note either way.
4. Data block: the serif's default figures were proportional; switching the table to tabular-nums aligned it cleanly, but the grotesque's tabular figures ran wider, adding a character of width to the price column. Column budgets adjusted.
5. Language blocks: both passed Cyrillic; the serif's Polish diacritics sat tighter against ascenders at 1.45 leading, so 1.5 was locked for both.
6. Scores: legibility 4 versus 4; hierarchy range 4 versus 3 (the serif had a true italic, the grotesque an oblique); data 3 versus 4; voice 4 versus 3 as scored by the group.
7. Decision: the serif for article bodies, the grotesque retained for UI chrome, which the matrix had been quietly suggesting all along; both tuning notes entered the CSS handoff.
8. Archive: the comparison page, the corpus file, and both candidates' tested versions stored with the decision record; the tuning notes (the tracking value, the leading floor, the tabular-nums scope) copied verbatim into the CSS handoff.

Two candidates, one afternoon, and a record that explains the split-system decision to whoever inherits it.

The afternoon produced one more output worth the effort: the losing grotesque stayed in the record with its scores, so when a UI-only redesign began the following year, it started from a documented candidate instead of a blank page. Split-system decisions (one face for reading, one for chrome) need this record most, because the next maintainer inherits two families and one paragraph of rationale.

## Field notes: failures only tests catch

- Fake italics: the family ships a true italic for regular but synthesizes bold italic; the weight ladder with italics is the only way to see it.
- Mushy 500: some faces render their 500 nearly identical to 400 at UI sizes, which silently deletes medium emphasis from the design.
- Digit drift: default figures that look fine in prose misalign a price column; tabular figures exist but were never tested.
- Vietnamese clipping at tight leading: diacritics clear at 1.5 leading and touch at 1.3; only the language block at production leading shows it.
- Windows rendering at 13 px: a face that renders beautifully on macOS falls apart at small sizes on Windows; screenshots from one platform are half the evidence.
- Fallback flash: with font-display: swap and no metric-adjusted fallback, the comparison page itself hides the layout shift production gets on every load.
- All-caps accent clipping: uppercase Vietnamese or German in tracked labels clips accents against tight line-height; the tracked-kicker stress block exists for this.
- Numeral ambiguity: a zero that reads like a capital O at 13 px looks charming in specimens and generates support tickets in production; the data block catches it.
- Ascender height versus leading: a face with tall ascenders forces looser leading, which silently rewrites the vertical rhythm tokens; the language blocks at production leading surface it before launch.
- Subset drift: a candidate whose latin-ext file lags its latin file produces half-updated pages after every font update; pin all subset files to one release.
- Punctuation color: some faces set quotes, hyphens, and parentheses a size too large, which shows only in dense error strings; the edge-inputs block is where it appears.
- Faked small caps: scaled capitals survive specimens and die in the feature check; test the real smcp feature if the design uses small caps.
- Weight coverage gaps: a family missing 500 forces the design system to choose between two wrong emphasis levels; the weight ladder exposes it immediately.
- Return-sweep failures: at over-wide measures a face's rhythm can send the eye to the wrong line; the measure sweep has ended two display-serif candidates in practice.
- Fallback mismatch: view the corpus in the fallback stack first, and the webfont's contribution becomes visible; comparisons that never show the fallback understate the cost of slow loading.

Each of these has ended a real comparison, and none appears in foundry specimens, which is precisely why the specimen is not the test.

## Audit checklist: comparison validity

- [ ] Every candidate renders the same corpus, in the same order, at the same sizes.
- [ ] Font files pinned to specific versions; the versions recorded with the artifacts.
- [ ] Browser and OS versions recorded; at least one Windows capture if UI text ships below 16 px.
- [ ] Hard gates (coverage, license, tabular figures) applied before any scoring.
- [ ] Scores entered per rubric line with the scorer named; the group-scored voice entry noted as such.
- [ ] Tuning needs recorded per candidate as handoff-ready notes.
- [ ] The comparison page archived (file or screenshot set) with the corpus version.
- [ ] Any mid-comparison change (corpus, sizes, weights) triggers a full re-run; no partial updates.
- [ ] The corpus includes at least one block per shipped language and one block per production size class.
- [ ] Candidates tested at their production tuning (tracking, leading), not at browser defaults only.
- [ ] The archive can be reopened: file paths and versions recorded so a maintainer can rebuild the comparison page.
- [ ] Feature checks run where used (tabular figures, real small caps, true italic), not assumed from listings.
- [ ] Tabular figures verified in the actual data block, including the minus sign and currency glyphs.
- [ ] The losing candidates' scores kept; the record of why they lost is as load-bearing as the winner's.

## Cross-references

- [Research workflow](research-workflow.md)
- [Presenting to stakeholders](presenting-to-stakeholders.md)
- [Testing multilingual coverage](../scripts/testing-multilingual-coverage.md)
- [CSS handoff snippets](css-handoff-snippets.md)

Compiled 2025 as part of the Fontlore project.
