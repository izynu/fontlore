# Logos and Custom Lettering

What this reference covers: Why logo lettering usually is not a font, how to recognize custom lettering and modifications on top of retail fonts, and what to do instead of chasing a nonexistent font file. This guide saves teams from the most common dead end in identification work.

Wordmarks are drawn, not typed. Even when a designer started from a retail typeface, the outlines in a logo are usually modified enough that no font will match exactly, and treating the logo as a font hunt wastes days.

## Why logos usually are not fonts

- A logo is artwork with a job: distinctiveness, legal distinctness, and reproduction at extreme sizes. Those goals pull lettering away from any typeface's neutral forms.
- Lettering for logos is typically spaced by eye, with custom joins, lengthened strokes, and altered terminals; kerning tables cannot express what logo designers do by hand.
- Famous examples are lettering, not type: the Coca-Cola script derives from Spencerian penmanship (the original was written by bookkeeper Frank M. Robinson), and the FedEx wordmark is custom-drawn lettering in the geometric sans tradition rather than any retail cut.
- Even supposedly simple wordmarks usually adjust a handful of details, which is enough to defeat exact matching.

## Spotting custom lettering

- Inconsistent stroke logic: curves that do not correspond to any system of construction, one-off joins, and asymmetries that no foundry would ship.
- Optical corrections beyond kerning: letters redrawn per position, crossbars that shift weight, counters that change shape across the wordmark.
- Unique ligatures and connections: letters linking in ways no OpenType feature would produce.
- Single-instance oddities: one letter in the wordmark has a detail no other letter shares; retail fonts are consistent.
- Spacing that ignores typeface conventions: gaps tuned for the specific word at the specific size, forever.

## Spotting modifications on top of a font

- A recognizable skeleton with surgical changes: the base font is identifiable, but a few letters are stretched, cut, or respaced.
- Mixed sources: caps from one family, lowercase from another, numerals redrawn; agencies splice regularly.
- Distortion tools at work: horizontally stretched faces are the most common modification, and they never match the original's proportions.
- When a modification is suspected, identify the base font first, then describe the deltas; that is usually all the client actually needs.

## What to do instead

- For brand work: hire a lettering artist or type designer to draw the wordmark; this is standard practice and produces the distinctiveness logos exist for.
- For internal documentation: record the wordmark as artwork with a note on its closest typeface relatives, so designers can build supporting typography around it.
- For lookalike needs: identify the closest retail font, license it properly, and accept that it is an homage, not a match.
- For fonts that were genuinely modified from a licensed base: check the license; most commercial licenses restrict modification, and an OFL base makes modification legal with the renaming rules applied.
- When the client insists on "the exact font of the logo", show them the overlay: render the best candidate over the logo and let the mismatch end the discussion with evidence.

## Working with the base font once identified

- Supporting typography around a custom wordmark usually wants a neutral family that does not compete; the wordmark is the personality, the system is the discipline.
- If the lettering derived from a specific typeface, using that same family for the wider system can tie the brand together, provided the license permits the uses.
- Document the relationship in the brand guidelines: which family the lettering grew from, which family carries body text, and which license applies to each.

## Workflow

1. Ask first: is this lettering or type? Run the spotting checklist before any tool work.
2. If lettering, identify the closest relatives (classification, era, construction logic) and stop tool-based matching.
3. If a modified font is suspected, identify the base with normal tools, then catalog the modifications.
4. Check the base font's license for what the modification plan implies.
5. Write the finding into the identification record with the honest label: custom lettering, or font plus modifications.

## Common mistakes

- Running logo screenshots through WhatTheFont repeatedly and treating "no good match" as a puzzle to solve harder.
- Recommending a retail font as "the logo font" and watching it fail to match anywhere it matters.
- Modifying a commercial font for logo use without checking the license, an audit incident waiting to happen.
- Assuming famous wordmarks use famous fonts; the famous ones are usually the most hand-drawn.
- Delivering "it is custom" with no path forward; the deliverable is the closest relatives and a recommendation, not a shrug.

## Decision rules

- Lettering detected: stop tool work, document relatives, recommend a letterer or the closest licensed family.
- Modified font detected: identify the base, list the deltas, verify modification rights in the license.
- Client needs a match for legal or reproduction reasons: commission redrawn vector artwork from the original, do not approximate with a font.
- Any recommendation built on a modified or custom source carries a lower confidence level in the record, explicitly labeled.

## Comparison table

Three kinds of logo lettering, and the tells for each:

| Kind | What it looks like | Hand-check tells | Right conclusion |
| --- | --- | --- | --- |
| Pure custom lettering | No coherent system across letters | Inconsistent joins, one-off details, spacing no font would produce | Artwork; document closest relatives only |
| Modified retail font | Recognizable skeleton with surgical changes | A known family's g or R visible under the distortions | Base font plus a written delta list |
| Untouched retail font | Behaves like normal type everywhere | Every glyph, the punctuation, and the spacing match a specimen | A real identification, then license work |

The third row is rarer than clients expect, and the first two are where tool cycles go to die. Run the hand-check tells before the first upload, not after the third "no close match"; the checklist costs minutes and the habit saves days.

Rows two and three grade into each other: a wordmark can be 95 percent a font with two letters adjusted. The record should say exactly that rather than forcing a binary; "Roboto Condensed with a redrawn R and S, spacing re-tuned" is a usable deliverable, "it's Roboto Condensed" is not.

The modifications worth naming in records have their own patterns:

| Modification | Tell in the sample |
| --- | --- |
| Horizontal stretching | Caps look condensed but every stroke is too thick for the width |
| Manual respacing | Gaps ignore the font's own fit system and change per position |
| Selective redrawing | One or two letters break the logic the rest of the word follows |
| Spliced families | Caps from one design language, lowercase or numerals from another |
| Added joins and swashes | Connections no OpenType feature would produce, usually one-off |
| Optical size faking | Thin strokes redrawn heavier for small sizes, which no retail optical grade would do this way |
| Borrowed punctuation | Quotes and apostrophes that match a different family entirely from the letters |

Neither table replaces looking: run every row against the actual artifact at actual size, because most modification tells vanish in thumbnails and reappear the moment you zoom.

## Worked example

A coffee roaster's wordmark: five condensed caps, uniform weight, obviously drawn with care. The full walk:

1. Spotting checklist first: the two E letters carry different crossbar lengths, the S is wider than any condensed specimen would make it, and the spacing tightens around the R in a way no kerning table expresses. Verdict: custom lettering.
2. Tool discipline: one WhatTheFont run is allowed for the record, and it returns no close match, exactly as predicted. No further uploads; the lettering question was settled by the checklist, not by the tool's silence.
3. Relative identification: the skeleton is condensed, geometric, and industrial; the closest retail relatives live in the DIN tradition, with Roboto Condensed as the obvious free stand-in for supporting type.
4. License note: the client assumed the mark was "a font they could buy more of"; the record states plainly that the lettering is artwork owned with the brand, and that no font license covers or replaces it.
5. Recommendation: license Roboto Condensed under Apache 2.0 for the supporting system, and commission a letterer for any future extensions of the mark.
6. Record: conclusion labeled custom lettering; identity confidence marked not applicable; the closest-relative listing marked probable with its reasoning attached; deltas and relatives documented.
7. Relative verification: specimens of the DIN-family faces and Roboto Condensed are compared against the mark, confirming the class and, just as usefully, the distance between the lettering and anything retail.
8. Handoff: the letterer receives the vector artwork and the record; the client receives the plan in writing, with the license class of the supporting font named.

What the record actually delivered, item by item:

- The verdict with its three tells, so nobody re-runs the hunt next quarter.
- Two named retail relatives with one line each on why they are relatives and not matches.
- A supporting-type recommendation with its license class, so the wider brand system has a legal, working font today.
- A commissioning path for the mark itself, with the note that a letterer will want the original vector artwork, not a screenshot.
- An explicit statement that no font identification exists for the mark, so nobody reopens the hunt expecting a different answer.
- The evidence attached: the wordmark at full size, and the two-letter zoom that shows the mismatched E crossbars.

The client's actual need was never "the font"; it was the ability to extend the brand without breaking it. Delivering relatives plus a plan answered that need; chasing an exact match would have answered nothing and cost a week.

## Signals to trust

- Identical repeats: the same letter appears twice in the wordmark with pixel-identical outlines, which points to a font or an unusually disciplined redraw.
- Punctuation that behaves: an apostrophe, ampersand, or period that matches a retail specimen exactly is a strong font signal, because lettering artists rarely draw punctuation with font-grade care.
- Consistent construction logic: every curve built on the same skeleton system, every stem the same weight, overshoots exactly where round letters meet flat rows.
- A secondary weight or an italic in the wild that shares the wordmark's logic; drawn lettering almost never comes with a family.
- License paperwork: brand guidelines that name a family and a foundry are testimony, even though they are occasionally wrong and worth checking.
- Consistency across years: the same letterforms reproduced in a campaign five years later without drift suggest a font file rather than a drawing that gets retraced.
- Live text: a wordmark that selects, copies, and reflows on the website is rendered from an actual font, whatever else it may be.
- Kerning pairs that repeat identically in different contexts behave like a metrics table, not an eye.
- Numerals rendered from the same source as the letters, verified by width consistency across a price list or a date line.
- A foundry or designer credit in the colophon, the website footer, or the guidelines package; attribution in writing beats speculation every time.

## Signals to distrust

- One letter that breaks the system: a unique join, a single flared stem, a counter shape no other letter shares.
- Spacing tuned per position with no recoverable logic; fonts space by rules, lettering spaces by eye, forever fixed at one size.
- Horizontally stretched caps, which read as condensed faces but never match one; the distortion itself is the tell.
- Mixed sources: caps from one design language and lowercase from another, or numerals that clearly arrived from elsewhere.
- Evidence at a single size only; lettering redrawn at a second size often reveals its hand-tuned nature, while a font stays consistent.
- "It looks like Helvetica" as a starting point: the famous faces are the ones most often modified, and the modifications are the whole game.
- Optical corrections beyond kerning: crossbars that shift weight mid-word, counters that change shape between instances, letters redrawn per position.
- A wordmark that only ever appears as flattened artwork at one locked size, with no live-text or secondary-weight evidence anywhere.
- Letterforms that change subtly between the website and the packaging; a font renders identically everywhere, a redraw drifts.
- Optical corrections beyond convention: every retail font ships with overshoots and weight balancing, but idiosyncratic fixes beyond those patterns signal hands, not code.

## Cross-references

- [Manual letterform analysis](manual-letterform-analysis.md)
- [Verifying an identification](verifying-an-identification.md)
- [Logos and trademark use](../licensing/logos-and-trademark-use.md)
- [Documenting identification results](documenting-identification-results.md)

Compiled 2025 as part of the Fontlore project.
