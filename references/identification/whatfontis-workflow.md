# WhatFontIs Workflow

What this reference covers: How to use WhatFontIs, the identifier built around manual glyph correction: marking and confirming character boxes, using the free tier effectively, filtering commercial versus free results, and knowing when its approach beats fully automatic tools.

WhatFontIs trades a little manual labor for accuracy. Where other tools guess at segmentation, it lets you fix it, which rescues many samples that automatic identifiers mangle.

## What the tool is

- WhatFontIs is an independent font identification service with a large indexed database spanning commercial foundries and free font sources.
- Its differentiator is a correction step: after upload, you confirm or fix the boxes around detected characters and type in the letters, teaching the matcher exactly what it is looking at.
- The free tier covers the core workflow; a paid tier removes interruptions and adds convenience features like advanced filtering and larger result sets.
- Because it indexes free font aggregators as well as commercial catalogs, it frequently identifies OFL and free-use families that commercial-only tools miss.

## Preparing the image

- Crop a clean string of letters, straightened and high contrast, as with any identifier.
- Include enough letters to be diagnostic but not so many that correction becomes tedious; 6 to 10 characters is the sweet spot.
- If letters touch or overlap, try to pick a string where they separate; manual correction can survive minor issues but clean input still wins.
- Dark-on-light or light-on-dark both work; the tool can invert, but a normal-contrast crop avoids that step entirely.

## The manual correction step

- After upload, review the detected character boxes: fix box positions that are off, delete boxes on noise, and add missing letters.
- Type the actual character for each box; accurate transcription materially improves matching, especially for ambiguous shapes like l, I, and 1.
- Use this step to exclude decorative characters (swashes, ornaments) that would mislead shape matching.
- The correction step is also the fastest way to learn what identifiers struggle with: you see the segmentation problems with your own eyes.

## Free versus Pro

- The free tier requires solving a check and shows results with some limits; it is fully capable of identifying common fonts.
- Pro removes interruptions, expands result counts, and unlocks filters that speed up repeated identification work.
- Occasional users: free is enough; run the workflow and stop. Professional identify-anything services and agencies: Pro pays for itself in saved minutes.
- Whatever the tier, the core discipline is identical: correct the boxes honestly, verify candidates by hand, and log the outputs.

## Filtering commercial and free results

- Use the free/commercial filter when you already know your constraint: a zero-budget project should not fall in love with a commercial match.
- The free filter is especially valuable for finding open-source stand-ins for famous commercial faces; verify the free candidate's license before adopting, since aggregator-indexed licenses vary.
- When a commercial result matches best, note the foundry and check the foundry's own site; WhatFontIs listing data can lag the foundry's current version.
- Filtered results still require hand verification; filters narrow the field, they do not confirm identity.

## Running the identification

- Upload, then invest real attention in the correction step; it is the tool's whole advantage.
- Read the full result list and compare top candidates against your sample at matched size.
- Cross-run the crop through WhatTheFont and Matcherator; independent agreement is the strongest cheap signal.
- For survivors, verify at the foundry and search Fonts In Use for real-world confirmations.

## When WhatFontIs is the right tool

- Low-quality or partially obscured samples where automatic segmentation fails: the correction step rescues these.
- Suspected free or open-source fonts: its free-source indexing beats commercial-focused tools.
- Stylized but separated display lettering: manual transcription guides the matcher past the weirdness.
- Repeated professional identification work where Pro filters compound over time.

## Workflow

1. Crop 6 to 10 clean, straight letters at good contrast.
2. Upload and correct the character boxes carefully; transcribe accurately.
3. Read the full results; filter by free or commercial according to the project constraint.
4. Hand-compare top candidates at matched size; eliminate on diagnostic letters.
5. Cross-check with a second tool for agreement.
6. Record outputs, dates, and confidence in the evidence file.

## Common mistakes

- Skipping or rushing the correction step, then blaming the tool for bad results.
- Mistranscribing characters, especially l, I, 1 and O, 0, which steers the matcher badly.
- Trusting a result because it is first; the ranking is shape distance, not identity.
- Forgetting to verify the license of free results surfaced from aggregator sources.
- Using WhatFontIs on connected script where even manual correction cannot fix structural mismatch.

## Decision rules

- Automatic tools returned nothing plausible: WhatFontIs with careful correction is the next move, not an afterthought.
- The corrected transcription produces strong candidates: verify by hand, then check license before adoption.
- Results are only commercial but the budget is zero: use the free filter and evaluate open alternatives on merit, not desperation.
- If the sample is a logo or custom wordmark, leave this workflow; no identifier will match drawn lettering.

## Comparison table

When the manual correction step pays, by sample problem:

| Sample problem | Automatic tools do | WhatFontIs with correction does |
| --- | --- | --- |
| Letters touching at one join | Segment merges two glyphs; results skew | Split the boxes; the matcher reads true |
| Noise, grain, or scan texture | Boxes land on specks; garbage candidates | Delete noise boxes; transcription carries the match |
| One decorative glyph in the string | The swash dominates shape distance | Exclude the glyph; letterforms decide |
| Ambiguous stems (l, I, 1) | Misread and misranked | You type what each box is; ranking stabilizes |
| Light text on dark | Some tools miss it or invert wrongly | Handled at upload; correction mops up the rest |
| Partial letters at crop edges | Half-glyphs pollute matching | Delete or trim the boxes; clean input restored |

The pattern: whenever segmentation, not shape matching, is the bottleneck, correction turns a dead sample into a live one. Whenever the crop is already clean, correction buys little and a fully automatic tool is faster; knowing which situation you are in is most of the tool-selection skill.

The table also doubles as a triage order: try one automatic pass first, read its segmentation, and bring the sample here only when the boxes visibly failed. Automatic tools cost a minute; correction costs ten, and ten minutes spent on a healthy sample is ten minutes lost.

## Worked example

A scanned book cover from 2004, title in an old-style serif, scan quality mediocre with two letters touching. The rescue, step by step:

1. Automatic first pass: WhatTheFont merges the touching letters and returns high-contrast display serifs, none close; the sample's moderate contrast and old-style proportions point elsewhere anyway.
2. WhatFontIs upload: the box step finds six of eight letters; the joined "ct" pair gets split manually, one noise box on a scan shadow is deleted, and each surviving box is transcribed.
3. Result list: Garamond-class candidates lead; among them EB Garamond, the open revival based on the 1592 Egenolff-Berner specimen, and Adobe Garamond Pro, the commercial revival.
4. Honest limit: silhouette comparison cannot separate Garamond revivals reliably; the letterform evidence supports the class, not one revival within it.
5. Decision logic: with the class probable and the revivals tied, the zero-budget use case adopts EB Garamond under OFL 1.1, and the record says exactly that; the artifact itself would be needed to push higher.
6. Record: confidence probable; evidence attached; the tie and its resolution documented for the next person.

This is the honest shape of many real cases: the tool narrows the class, correction rescues the sample, and the final step is a licensing decision rather than a certainty. Recording the tie is what keeps the work reusable; hiding it is what forces the next person to redo the hunt.

Note what the record deliberately does not claim: it does not name one Garamond revival as the answer, because the sample cannot support that. A probable class with a documented, license-driven adoption is worth more than a confident wrong revival name, and the next person who touches the case inherits a decision they can defend.

## Field notes

Habits that separate productive WhatFontIs sessions from wasted ones:

- Transcribe honestly even when a box looks like a different letter than expected; the matcher benefits from what is there, not what should be there.
- Six to ten corrected letters is the effort sweet spot; beyond that, correction cost grows faster than result quality.
- Solve the l, I, 1 problem deliberately: if the sample contains all three, transcribe each and let the face's own distinctions work for you.
- The free/commercial filter is a decision made before falling in love with a candidate, never after.
- Listing data lags foundries; when a candidate's listing shows an old version, check the foundry's own catalog for the current one before ruling it out.
- Re-run after fixing boxes rather than reading tea leaves in a bad result set; one corrected resubmit is cheaper than an hour of speculation.
- Keep the corrected-boxes screenshot in the record; it shows the next person exactly what the tool was asked to match.
- The interruption on the free tier doubles as a pacing device: if a case is not worth one captcha, it is not worth a Pro subscription either.
- Inverted samples (light on dark) work, but transcribe after inverting mentally; transcription errors spike on inverted text.
- When the correction step reveals the segmentation was fine all along, the problem is shape matching, and the fix is a different tool, not better boxes.
- Scan shadows and book spine curvature bend baselines; straighten the crop before blaming the boxes, or you will fight the geometry letter by letter.
- Small caps and old-style figures in a sample confuse transcription; confirm whether those letters are what they look like before typing them.
- The correction step is also free training: every session teaches what segmenters fail at, which makes your crops better across every tool.
- When Pro features would help once, note which one and why; the case for a subscription is a pattern of those notes, not a single busy afternoon.

## Quick reference

The WhatFontIs loop, compressed:

1. Crop 6 to 10 clean, straight letters at good contrast; PDFs and native screenshots beat photos.
2. Upload, then invest real attention in the box step: fix positions, delete noise, transcribe each character.
3. Read the full result list; apply the free/commercial filter only when the project constraint is already known.
4. Hand-compare top candidates at matched size; eliminate on diagnostic letters (g, a, R, t, numerals).
5. Cross-check with one other tool for independent agreement.
6. Record outputs, dates, corrected-box screenshots, and the confidence tier.
7. When the class is probable but the exact face is tied, say so in the record and decide on license grounds; ties are decisions, not failures.
8. Route logos and wordmarks out of this workflow before the first upload; no amount of box fixing turns drawn lettering into a font.

Standing rules: correction quality caps result quality; filters narrow, they never confirm; and a logo or wordmark leaves this workflow entirely, because no amount of box fixing turns drawn lettering into a font.

## Cross-references

- [Identification workflow overview](identification-workflow-overview.md)
- [WhatTheFont workflow](whatthefont-workflow.md)
- [Identifont decision tree](identifont-decision-tree.md)
- [Free font risks](../licensing/free-font-risks.md)

Compiled 2025 as part of the Fontlore project.
