# WhatTheFont Workflow

What this reference covers: How to get reliable results from MyFonts' WhatTheFont: preparing the image, understanding what the tool sees, reading the candidate list honestly, and moving from a match to a purchase with the right license. It also covers what to do when the tool fails.

WhatTheFont is the most-used automated identifier and the first tool most people try. Used carelessly it produces confident wrong answers; used well it solves most common-case identifications in under a minute.

## What the tool is

- WhatTheFont is MyFonts' font identification service, backed by a trained model and the MyFonts catalog, which is the largest commercial font marketplace.
- It returns a ranked list of visually similar fonts from catalog inventory, each with a similarity score and a direct path to the family's MyFonts listing.
- Because results come from MyFonts inventory, a correct answer can be absent when the font is not sold there; absence of a match is information, not failure.
- The tool works on letterform shapes, not on metadata: it does not know what the site claimed, only what the pixels show.

## Preparing the image

- Crop to a short string of letters, ideally 4 to 12 characters. More letters can help, but decorative or distorted glyphs hurt.
- Prefer lowercase strings; lowercase shapes discriminate better than caps, which are more similar across families.
- Straighten the baseline. Even a few degrees of rotation degrades segmentation.
- Maximize contrast: dark letters on light background or the reverse, with minimal noise around the glyphs.
- Avoid connected scripts, letters that touch, and heavy texture overlays; segmentation will fail and the results will be garbage.
- If the source is a photo of a screen, re-shoot or find the digital original; moire and resampling are poison.

## Running the identification

- Upload the crop and let the tool segment the letters; check its reading. If it detected wrong characters or split letters, fix the crop rather than accepting nonsense output.
- Read the candidate list from the top but never stop at the first row. The correct font frequently sits in positions two through five.
- Compare candidates against your sample at matched size. Similarity scores are visual rankings, not probabilities.
- Use the tool's side-by-side comparison view to spot differences in the letters your sample actually contains.
- If no candidate looks right, recrop with different letters and try again; a second, different crop is often all it takes.

## Reading candidates honestly

- Check the letters in your sample, glyph by glyph, for each of the top five: the diagnostic letters (g, a, r, y, R, Q) matter more than overall texture.
- Watch for the weight trap: your sample may be a medium or bold cut of a family whose regular is being shown as the match.
- Watch for the version trap: families get redesigned, and an old sample may match an older release better than the current one.
- Watch for the lookalike trap: several families are near-clones of each other; provenance (where you saw it) usually disambiguates.
- When the top candidates differ only in tiny details, switch from tool judgment to manual letterform analysis and foundry catalogs.

## From match to purchase

- Once you have a confident match, open the family's MyFonts listing and verify the styles available and the current version.
- Choose the license scope for your actual use: desktop, web pageviews, app, or the bundled options; see the licensing guides before clicking buy.
- Buy from the foundry directly when the foundry also sells it, if you prefer supporting the source; MyFonts and foundry-direct licenses are usually equivalent in scope.
- Keep the receipt and the license document with your font records; the identification log plus the receipt is your audit trail.

## When WhatTheFont fails

- Custom lettering and logos: retail fonts will not match drawn wordmarks; move to the lettering route.
- Obscure or historical faces not in the catalog: use Matcherator and WhatFontIs, which index different inventories, then human routes.
- Heavily stylized display faces: tools struggle with extreme personality; manual analysis wins here.
- All results are plausible: the sample is too small or too generic; get more letters or more context.

## Workflow

1. Secure the best-resolution sample; archive the original.
2. Crop 4 to 12 straight, high-contrast letters, lowercase if possible.
3. Upload, verify the tool's segmentation, read the top five candidates.
4. Hand-compare each candidate against the sample; eliminate on diagnostic letters.
5. Confirm the survivor at the foundry or on Fonts In Use.
6. Purchase with the correct license scope and file the evidence record.

## Common mistakes

- Stopping at the first result and buying a wrong font; the first row is a starting point, not an answer.
- Feeding logos and custom lettering into the tool and treating "no match" as a mystery.
- Uploading busy, low-contrast crops and blaming the tool.
- Ignoring weight and version differences between the sample and the matched family.
- Buying a license scope that does not cover the project because the purchase happened at the peak of identification excitement.

## Decision rules

- Top five all fail the glyph check: recrop once, then switch tools; do not iterate forever.
- Match found and hand-check passes: verify license next; identification is only half the job.
- No plausible candidate twice in a row: the font is probably not in MyFonts inventory; rotate to Matcherator and WhatFontIs.
- The sample is a wordmark: stop tool work and analyze the lettering instead.

## Comparison table

WhatTheFont against its two main rivals, with the decision rule each row implies:

| Dimension | WhatTheFont | Matcherator | WhatFontIs |
| --- | --- | --- | --- |
| Inventory center | MyFonts commercial catalog | Fontspring plus free fonts | Commercial plus aggregator-indexed free |
| Segmentation | Automatic | Automatic | Automatic, then user-corrected |
| Speed to first list | Fastest | Fast | Slower; correction takes minutes |
| Free-font coverage | Weak | Strong | Strong |
| Purchase funnel | Direct to MyFonts listings | Soft; purchase optional | Soft on the free tier |
| Best role | First pass on common commercial faces | Second opinion and free candidates | Rescue pass on damaged samples |

The operational summary: start with WhatTheFont for speed, bring in Matcherator when the answer must be budget-free or the first pass failed, and reserve WhatFontIs for samples whose segmentation is visibly broken. Tools are cheap; the expensive resource is your attention, so spend tool runs before spending analysis time.

What the table cannot show is inventory drift: catalogs reindex, foundries move, and free fonts migrate. Re-run a failed hunt every few months if the case still matters; a no-match from last year is not a no-match today.

## Worked example

A landing page headline screenshot, "Payments for platform teams", clean antialiased text. The fast case, run properly:

1. Crop: "Payments for" gives twelve characters at native resolution; the baseline is level and the background is flat.
2. WhatTheFont: the top five are all UI grotesques, led by Roboto; every candidate is plausible at silhouette distance.
3. Hand check: the sample's g is double-story, matching Roboto; the single-story-g candidates are out. The slightly condensed proportions and open apertures agree with Roboto's build as well.
4. Cross-read: Fonts Ninja on the live page reports the CSS declaring Roboto with woff2 files served; declarations and pixels agree.
5. License: Roboto is Apache 2.0 in the google/fonts repository; the "purchase" step dissolves into a download, and the record notes that a paid lookalike would have been the wrong buy.
6. Record: confidence confirmed; alternatives kept with one-line losses; the tool log attached.

The case took under five minutes because the sample was clean and the font is common. The discipline that made it fast was the hand check at step 3: without it, "Roboto or something like Roboto" ships as a guess, and guesses in records metastasize into facts.

The same case gone wrong is just as instructive: the top candidate accepted on sight, a MyFonts license purchased for a lookalike, and the clone discovered two sprints later when a developer compared letter widths. Every failure mode in this guide compresses into that one skipped step.

Where it could have gone wrong, and what held:

- A crop taken from a resized marketing thumbnail would have carried resampling softness into every ranking; the tools would have compared shapes against mush, confidently.
- Naming the family from the tool list before the hand check would have produced the lookalike purchase that a later overlay unravels at twice the price.
- Skipping the Ninja cross-read would have left "probably Roboto" in the record instead of a confirmed, free, Apache-licensed answer with a download path.

## Field notes

What repeated WhatTheFont use teaches:

- The top result is right often enough to feel trustworthy and wrong often enough to embarrass you; positions two through five deserve a real read every time.
- Lowercase crops beat caps-heavy crops; caps are too similar across families to rank reliably.
- The weight trap is the most common near-miss: the sample is a medium or bold while the tool ranks the regular, and everything looks subtly off. Check the weight row before eliminating a family.
- A second crop with different letters is the cheapest retry; keep two or three crop variants from the start and feed the tool the best one, not the biggest one.
- Moire, JPEG artifacts, and resampled screenshots each depress ranking quality in ways that look like "no good match" rather than "bad input".
- For a free font the catalog does not carry, the tool's near-misses still help: they describe the class, and Matcherator's free index usually holds the actual family.
- Log the run even when it fails; a dated "top five, all rejected for reasons X and Y" entry is what makes the eventual answer auditable.
- Similarity scores near 100 percent still mean nothing on their own; near-clones score as high as the original, and provenance decides between them.
- Decorative first letters lure the segmenter; crop past the display initial into the plain text whenever possible.
- When everything in the top five shares one trait the sample lacks (closed apertures, flat terminals), the trait itself is a clue: the family you want sits outside the catalog, and the shared trait tells you what to search for next.
- Antialiased text at very small sizes reads bolder than it is; find a larger rendering of the same face before judging weight.
- Compare lowercase against candidates' lowercase first and caps second; lowercase discriminates, caps confirm.
- Screenshot the candidate list with the sample visible in the same frame; the pairing reads instantly in review and settles arguments without a re-run.
- WhatTheFont also runs as a mobile app pointed at the physical world; the same crop discipline applies, and packaging photos need even more care with glare and angle.

## Quick reference

The WhatTheFont loop, compressed:

1. Secure the best-resolution sample and archive the original untouched.
2. Crop 4 to 12 straight, high-contrast letters, lowercase if possible.
3. Upload, verify the tool's segmentation, and read the top five candidates.
4. Hand-compare each candidate against the sample; eliminate on diagnostic letters.
5. Confirm the survivor at the foundry or on Fonts In Use.
6. Purchase with the correct license scope, or download if open, and file the evidence record.

Retry ladder when nothing fits: one recrop, then one different-crop run, then one other tool, then manual analysis. Anything past that ladder is grinding, and grinding produces confident wrong answers.

Scores, ranks, and similarity badges are sorting devices; the hand check on g, a, R, t, and the numerals is the verification. The tool earns its speed only when its answer survives being read closely.

## Cross-references

- [Identification workflow overview](identification-workflow-overview.md)
- [Matcherator workflow](matcherator-workflow.md)
- [Verifying an identification](verifying-an-identification.md)
- [Marketplace license models](../licensing/marketplace-license-models.md)

Compiled 2025 as part of the Fontlore project.
