# Identification Workflow Overview

What this reference covers: The end-to-end process for identifying an unknown typeface from a sample: collecting a usable image, cropping glyphs for tools, running automated identifiers in the right order, cross-checking results by hand, and finishing with license verification before any purchase.

Most identification failures are process failures: a bad crop fed to three tools, the first plausible answer accepted, and the wrong font purchased. The workflow below is short enough to follow under deadline and strict enough to catch wrong answers.

## Stage 1: Collect the best possible sample

- Start from the highest-resolution source you can reach: the original website asset, print scan at 300dpi or better, or a vector PDF if the artifact allows it.
- Photograph print with even lighting, no glare, and the page flat; keystone distortion wrecks glyph matching.
- For screenshots, capture at native resolution and avoid browser zoom, which resamples pixels.
- Note the context while you are there: where the sample came from, what the text says, and any visible branding. Context often answers the question before tools do.
- If the sample is from a video or a photo of a screen, expect tools to struggle; plan for manual analysis from the start.

## Stage 2: Crop for the tools

- Isolate a short run of text: 4 to 12 characters with clear letterforms. Tools want letters, not paragraphs.
- Include lowercase-heavy samples when possible; lowercase carries more distinguishing shape than caps.
- Straighten the baseline and crop tightly without clipping glyph extremes; descenders and ascenders carry diagnostic information.
- Boost contrast if needed so letters are solid black on white; anti-aliased gray edges confuse segmentation.
- Keep an unprocessed copy of the original image with your notes; the crop is for tools, the original is evidence.

## Stage 3: Run automated identifiers in order

- WhatTheFont (MyFonts) is the fastest first pass with the largest commercial database behind it. Expect a ranked candidate list within seconds.
- Matcherator (Fontspring) is the strongest second opinion, with no purchase pressure and free-font suggestions mixed in.
- WhatFontIs adds manual glyph correction, which rescues many samples the automatic segmenters mangle.
- Run at least two tools before believing any result. Agreement between independent tools is the cheapest confidence signal available.
- Log each tool's top five candidates with dates; the logs become part of the evidence record.

## Stage 4: Cross-check candidates by hand

- Pull specimens for the top candidates and compare glyph by glyph, not by overall impression: g, a, r, y, R, G, numerals, and punctuation.
- Check the details that identification images usually crop: the tail of the Q, the leg of the R, the shape of the ampersand.
- Compare weights honestly: a bold sample matched against a regular cut will look wrong for reasons that have nothing to do with identity.
- Use a metrics overlay or a side-by-side specimen at matched size to compare proportions, not just shapes.
- When two candidates differ only in details, look for the sample's era and context; foundry redesigns and version changes explain many near-misses.

## Stage 5: Verify provenance and license

- Once a candidate survives cross-checking, confirm it exists at the foundry or publisher and note the current license.
- If the font is free and open (OFL and friends), record the license and repository; if commercial, record the purchase path and scope needs before anyone falls in love with it.
- Beware the free lookalike trap: several famous typefaces have free imitations with similar names. Identity and legitimacy are separate questions.
- Only now does buying or adopting make sense; identification without license verification ends in audits.

## Choosing the right route

- Clean digital sample, common face: automated tools alone usually suffice.
- Distorted, stylized, or rare lettering: manual letterform analysis first, tools second.
- No image at all, only memory or description: skip tools entirely and use question-based identification.
- Suspected custom lettering (logos, wordmarks): shift to the lettering-analysis route before wasting tool cycles.

## Workflow

1. Secure the best sample and archive the original.
2. Crop 4 to 12 clean glyphs, straightened and high contrast.
3. Run WhatTheFont, then Matcherator, then WhatFontIs if needed; log top five from each.
4. Hand-compare top candidates against specimens, glyph by glyph.
5. Search Fonts In Use and the foundry catalogs for confirmation.
6. Verify license and purchase path; write the evidence record with a confidence level.

## Common mistakes

- Feeding a whole poster to a tool and trusting its guess on the decorative words.
- Stopping at the first plausible candidate instead of the first verified one.
- Comparing candidates by silhouette rather than by the diagnostic letters.
- Identifying the font correctly and shipping it without checking that its license permits the actual use.
- Treating a tool's confidence score as truth; the scores are rankings, not probabilities.
- Forgetting that modified or distorted lettering (logos, custom titles) will never match any retail font exactly.

## Decision rules

- Two tools agree and hand-check passes: proceed to license verification with high confidence.
- Tools disagree and the sample is clean: your crop is probably the problem; recrop before doubting the tools.
- No tool produces a plausible candidate after two clean attempts: move to manual analysis and human routes.
- The sample is a logo: stop; route to the custom lettering guide instead.

## Comparison table

The main routes into an identification, and when each earns its keep:

| Route | Input needed | Strength | Failure mode |
| --- | --- | --- | --- |
| WhatTheFont | Clean image crop | Fastest first pass; largest commercial inventory | Confident-looking wrong answers on lookalikes |
| Matcherator | Clean image crop | No purchase pressure; indexes free fonts | Struggles with scripts, texture, hairlines |
| WhatFontIs | Image crop plus corrections | Human-corrected segmentation rescues bad samples | Correction quality caps result quality |
| Identifont | Memory or description | Works with no image at all | Wrong answers prune silently |
| Fonts Ninja | Live web page | Reads the served fonts directly | Declared is not always rendered |
| Manual analysis | Your eye and vocabulary | Works on stylized, distorted, and rare lettering | Slowest; skill-dependent |
| Fonts In Use | Search terms | Documented projects with credited faces | Absence proves nothing for obscure work |

Sequence matters more than tool choice: two independent routes agreeing is worth more than any single tool's ranking, and the manual read at the end converts agreement into evidence. Choose routes by what you actually have (pixels, memory, or a live page), not by habit, and switch routes the moment input quality becomes the bottleneck.

The table also explains the economics. Upload tools cost minutes; manual analysis costs an afternoon; foundry confirmation costs days. Spend the cheap currency first, and escalate only when the cheap answers conflict with each other or with the hand check.

## Worked example

A photograph of a coffee bag on a shelf, headline set in a geometric sans. The full pipeline, condensed:

1. Sample: the first photo is at an angle with glare across one letter; a second straight-on shot is secured before any tool work, because feeding tools a damaged sample wastes the entire run.
2. Crop: the string "pale roast" is cropped tight, straightened, and contrast-boosted; lowercase dominates, which is what the tools want.
3. WhatTheFont: the top five cluster around Futura and its descendants; the ranking is a lead, not a verdict.
4. Matcherator: agrees on the geometric class and, usefully, lists free geometric candidates alongside commercial ones.
5. Hand check: the sample's a is single-story and its g is single-story; the arches of m and n come to points; the x-height is small relative to the caps. Futura shows exactly this profile, while the free geometric candidates mostly show a double-story a or a much larger x-height.
6. Era and context: the roaster's brand story dates the design to a period when Futura was in wide use; nothing in the timeline contradicts it.
7. Verification: a specimen overlay of Futura Medium against the crop matches letter for letter at matched size, and Fonts In Use shows the family in comparable packaging contexts.
8. Record: confidence confirmed; license noted as commercial with the purchase path logged; alternatives kept with one-line reasons.

Where the case could have gone wrong, and what held it:

- The angled first photo would have degraded every ranking silently; securing a clean shot before uploading kept the tools useful.
- Silhouette distance alone would have let the free lookalikes through; the single-story a is what eliminated them.
- Stopping at position one of the list would have matched a Futura descendant rather than Futura itself; reading all five mattered.
- The overlay turned two tools agreeing into measurable evidence, and it took under five minutes.

## Field notes

Notes from running this pipeline on real cases:

- Context often answers before tools do: a publisher's colophon, an app's credits screen, a press kit, or a Fonts In Use entry can end the hunt in one search.
- Tools rank silhouettes and are blind to weight, width, and version traps, which is exactly what the hand check exists for.
- Log failures with the same care as successes; a dated "both tools, top five, all rejected on the g" entry makes the eventual answer auditable.
- Recropping beats re-running: three different crops through two tools outperform six retries of the same crop through one.
- When every result is plausible, the sample is too small or too generic; the fix is more letters or more context, not more tools.
- Special characters are gifts: a distinctive ampersand, a slashed zero, or an old-style numeral can decide a case the letters cannot.
- Keep the original artifact readable in the archive; a crop that lost its context is a clue that lost its case.
- Route, do not grind: the moment a route stalls twice, switch routes and record why, rather than iterating the same upload a seventh time.

## Quick reference

The whole workflow on one line each:

1. Best sample you can get; archive the original untouched.
2. Crop 4 to 12 straight, high-contrast letters, lowercase if possible.
3. Run two identifiers at minimum; log each tool's top five with dates.
4. Hand-check candidates glyph by glyph: g, a, r, y, R, Q, t, numerals.
5. Overlay or matched-size comparison for the finalists.
6. Fonts In Use and foundry catalog checks for corroboration and era fit.
7. License verified at the source before anyone buys or commits.
8. Record with a confidence tier, alternatives, and next actions.

Triage shortcuts:

- Logo or wordmark: stop; take the lettering route.
- Only a memory: take the question-tree route.
- Clean digital text: automated tools alone usually close the case.
- Stylized, distorted, or rare: manual analysis decides, tools confirm.
- Everything else: tools shortlist, humans decide, records remember.

The two rules that survive every workflow revision: never act on a single source, and never let identification outrun license verification.

## Cross-references

- [WhatTheFont workflow](whatthefont-workflow.md)
- [Manual letterform analysis](manual-letterform-analysis.md)
- [Verifying an identification](verifying-an-identification.md)
- [Logos and custom lettering](logos-and-custom-lettering.md)

Compiled 2025 as part of the Fontlore project.
