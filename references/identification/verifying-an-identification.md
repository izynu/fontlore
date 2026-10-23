# Verifying an Identification

What this reference covers: How to confirm a font identification before it becomes a purchase or an adoption: full-specimen comparison, metrics overlays, confirmation from designers and foundries, and checking Fonts In Use for real-world corroboration.

Identification tools produce candidates; verification produces answers. The step most teams skip is the one that prevents wrong purchases, and it costs minutes.

## Full-specimen comparison

- Pull the candidate's complete specimen: every letter A to Z and a to z, all numerals, and the full punctuation set, at a size close to your sample's size.
- Compare glyph by glyph against your sample, starting with the letters your sample actually contains.
- Check the punctuation and numerals even when the sample lacks them; you will use them, and mismatched punctuation is a delayed surprise.
- Check all the weights you plan to use, not just the one that matched; some families' bolds diverge noticeably between versions.
- Look at diacritics if any language beyond basic Latin is in scope; missing or clumsy accents disqualify a candidate quietly.

## Metrics overlay

- Set the same string in your sample and the candidate at matched size, then overlay or flip between them.
- Matching widths across a string indicate compatible metrics; diverging widths rule out identity even when shapes look similar.
- Compare baseline positions, x-height, and cap height explicitly; proportions are harder to fake than outlines.
- For suspected clones, the overlay usually reveals the truth quickly: clones differ in details or metrics almost by definition.
- Any design tool or even a browser with two rows and a flicker toggle works; the method matters more than the tooling.

## Designer and foundry confirmation

- The fastest authoritative answer is a short, polite email to the foundry or designer with your sample attached; many answer within days and appreciate the interest.
- Foundries confirm identifications they recognize and often point to the correct family when their catalog contains something close.
- Type design communities and identification threads (such as the identifythisfont community on Reddit) provide human pattern-matching at scale; provide your best crop and context.
- Record confirmations in the evidence file: who confirmed, when, and in what words. A written confirmation is the highest confidence tier available.

## Fonts In Use corroboration

- Fonts In Use (fontsinuse.com) documents real projects with credited typefaces; search the candidate's name to see it in authentic settings.
- If your sample came from a notable project, search the project; the typeface credit may already be documented.
- Real-use entries also show the family in varied weights and sizes, which helps verify the specific cut you identified.
- Absence from Fonts In Use means little for obscure fonts; presence with matching artifacts is strong corroboration.
- Pair with Typewolf and foundry news pages for era context: a candidate must plausibly have existed when your artifact was made.

## Confidence tiers before acting

- Confirmed: foundry or designer confirmation, or overlay-identical metrics and shapes. Safe to purchase or adopt.
- Probable: multiple tools agree, hand-check passes, no contradictions. Safe to proceed with a paper trail.
- Possible: single tool or partial agreement; keep hunting or mark clearly as provisional in any deliverable.
- Unknown: memory-based or heavily stylized samples; label honestly and avoid purchase decisions.
- The tier goes in the record; downstream readers should never have to guess how sure you were.

## Workflow

1. Build the candidate's full specimen sheet at matched size.
2. Run the glyph-by-glyph comparison; eliminate or advance.
3. Overlay metrics on the same string; eliminate or advance.
4. Search Fonts In Use and the foundry catalog for corroboration and era fit.
5. Request confirmation from the foundry or community for anything consequential.
6. Assign the confidence tier and write the record before any purchase.

## Common mistakes

- Verifying with a two-letter specimen image from a font blog instead of the full character set.
- Comparing at different sizes and concluding the shapes differ.
- Skipping numerals and punctuation checks, then discovering the mismatch in production.
- Buying based on "probable" confidence when a free confirmation email was available.
- Not recording the verification, so the next person repeats the entire hunt.

## Decision rules

- Metrics overlay identical and shapes match: call it confirmed and move to licensing.
- Shapes match but metrics differ: you are looking at a clone, revival, or different version; resolve at the foundry before adopting.
- Foundry is unresponsive and stakes are high: treat the tier as probable at best and document the attempted confirmation.
- If verification keeps failing for a "certain" identification, reconsider whether the sample is modified lettering.

## Comparison table

Verification methods ranked by evidence strength per minute spent:

| Method | Evidence produced | Strength | Cost |
| --- | --- | --- | --- |
| Metrics overlay on a long string | Width-by-width match or mismatch | Very high; hard to fake accidentally | Minutes |
| Full-specimen glyph comparison | Letter-by-letter agreement list | High | 10 to 20 minutes |
| Foundry confirmation by email | Named human testimony | Highest when it arrives | Days, often unanswered |
| Fonts In Use project match | The exact artifact documented | Very high when it exists | Minutes |
| Community identification thread | Independent human reads | Medium; useful for leads | Hours |
| Wakamai Fondue on the file | Name table, axes, and features of the actual file | High for free candidates | Minutes |
| Archived page or file check | What the artifact itself declared | Very high when it exists | Minutes |

No single method is sufficient for consequential decisions; two agreeing methods are the working minimum. The overlay plus a Fonts In Use match, or the overlay plus a foundry reply, moves a probable to confirmed honestly, and the pair matters because the two methods fail differently.

The bottom rows are the quiet workhorses. Community threads rarely confirm anything alone, but they shortlist fast; archived pages and files confirm what the artifact itself claimed, which is evidence no amount of shape comparison can replace when it exists.

One habit makes every row stronger: write the agreement list before the verdict. A verdict written first bends the list toward itself; a list written first can be checked by anyone.

## Worked example

A blog template revamp where the old site's headers look like Merriweather. Verification, in order:

1. Specimen: Merriweather's full character set is pulled from Google Fonts at the sample's rendered size; the sturdy serifs, large x-height, and double-story g all match the sample.
2. Overlay: the string "Quarterly reading notes" is set in both and overlaid; widths align across every word.
3. Fonts In Use: entries document Merriweather in editorial settings matching the sample's weight usage, and era fits, since the family dates to 2011 and the old site launched in 2013.
4. File check: the original site's CSS serves a Merriweather woff2; running the downloaded file through Wakamai Fondue shows the Merriweather name table with its expected axes and features.
5. Confirmation: no foundry email needed; the DOM read, the overlay, and the corroboration already cross three method families.

Confidence: confirmed, recorded with the evidence links. Total time: under fifteen minutes. The counterfactual matters: the team nearly licensed a commercial "Merriweather-style" serif recommended by a contractor, and the overlay method is exactly what would have exposed the substitution before money moved.

The same case verified lazily: a two-letter specimen image from a blog, a squint, and "close enough". That version takes one minute and produces a wrong purchase with a receipt, which is the most expensive minute in typography.

A second case, the clone check: a vendor's catalog page matches the sample's shapes convincingly, but the metrics overlay shows every word running about five percent wider than the sample. Shapes matching while widths differ is the signature of a clone, a revival, or a different version, not of identity. The verdict is therefore negative: the record names the class as probable and identity as unresolved pending foundry contact, and the purchase waits. Five percent is invisible in a screenshot and unmistakable in an overlay, which is the whole reason the overlay exists.

Verification's core discipline is the same at every scale: set the same string in both faces at the same size, look for where they differ, and let the difference, not the resemblance, write the conclusion.

## Signals to trust

- Overlay identity across a string of fifteen or more characters, including spaces; width accidents do not survive that length.
- Two methods from different families of evidence agreeing: pixels plus metadata, or shapes plus provenance.
- A written foundry reply naming the family; even a two-line confirmation outranks any tool output.
- Fonts In Use crediting the same family for the same artifact or campaign.
- Era coherence: release dates, redesigns, and the artifact's date fitting together without special pleading.
- A downloaded file whose name table, axes, and feature set match the claimed family exactly.
- Convergence over time: a second look a week later, with fresh eyes, reaches the same conclusion.
- The overlay stays aligned on ascenders and descenders, not just on x-height letters; vertical metrics agreeing is rarer and stronger than horizontal luck.
- Punctuation matches: the ampersand, the quotes, and the dashes are where clones and lookalikes get lazy.
- Numerals agree in both style and width, lining or old-style, across the full run.
- Diacritics match where any language beyond basic Latin is in scope; accent placement is expensive to fake and rarely bothered with.
- The foundry's own specimen renders the sample's string identically at the same size in the same browser.
- Two verifiers working separately produce the same agreement list without comparing notes.
- Tabular figures align in a column when both sample and candidate are set tabular; proportional figures line up word for word in running text.
- The candidate's own changelog or release notes describe the version the sample matches, closing the version-trap question.
- Independent re-derivation: run the identification again from the crop alone, without looking at the first conclusion, and land in the same place.

Trust in verification is always relative to stakes: a favicon swap survives on one signal, a brand rollout wants the foundry's name on an email.

## Signals to distrust

- Similarity percentages and scores from any tool; they rank shapes, they do not certify identity.
- Blog and social media specimen images of unknown size and version, which have been resaved, recolored, and sometimes retyped.
- Family names that differ by one word from the famous face they echo; lookalikes live exactly there.
- A candidate that requires the sample to be "a bit stretched" or "probably an older version" to fit; each rescue is a contradiction wearing a costume.
- Verification performed only against the two or three letters that already matched; full character sets or it did not happen.
- Community consensus formed from a thumbnail; a thread agreeing on a guess is still a guess with company.
- Your own momentum: after an hour of hunting, the desire to be finished is the loudest voice in the room; the overlay does not care how long you have been at it.
- Rounded comparisons: "close enough" is the sound of a verification that did not happen.
- Overlays done at different sizes, where everything mismatches for boring reasons and real differences hide under the scaling.
- Tool confidence badges and marketplace ratings; they measure popularity, not glyph identity.
- A confirmation reply that names the family but never mentions your sample; ask whether anyone actually looked at the image.
- Verification against the candidate you chose first; confirmation bias runs the whole hunt unless the diff is written down before the verdict.
- Full-specimen checks skipped because the first three letters agreed; the fourth letter is usually where the clone lives.
- Overlays that only show the matched string; ask to see the string the candidate gets wrong, which every honest verifier can produce.
- A verification chain where every link is the same person; two independent paths to the same answer beat one path walked twice.

## Cross-references

- [Identification workflow overview](identification-workflow-overview.md)
- [Manual letterform analysis](manual-letterform-analysis.md)
- [Documenting identification results](documenting-identification-results.md)
- [WhatTheFont workflow](whatthefont-workflow.md)

Compiled 2025 as part of the Fontlore project.
