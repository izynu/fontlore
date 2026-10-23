# Numerals and Notation

What this reference covers: Numeral styles (lining, old-style, proportional, tabular) and the OpenType features behind them, fractions and ordinals, math notation limits of text fonts, and currency glyph coverage. Numeric typography is where otherwise good font choices quietly fail, especially in tables, prices, and data-dense interfaces.

## The four numeral styles

Two axes, usually independent, describe how a font's figures behave:

- Lining (lnum): all figures share cap height. The default in most UI and sans faces; the safe choice for interfaces.
- Old-style (onum): figures have ascenders and descenders like lowercase letters (3 and 4 descend, 6 and 8 ascend). The default in many classic text serifs; lovely in running prose, disruptive in tables.
- Proportional (pnum): each figure takes its natural width; a 1 is narrower than an 8. Default in most fonts; fine in prose, wobbly in columns.
- Tabular (tnum): every figure occupies the same width; columns of numbers align. Essential in tables, dashboards, timers, and anywhere values change in place.

Combinations matter: editorial body text often reads best in proportional old-style; any column of data wants tabular lining. Set the feature per role, not per site. Enable via `font-variant-numeric: tabular-nums` (or `lining-nums`, `oldstyle-nums`, `proportional-nums`) rather than low-level `font-feature-settings`, so styles compose predictably.

## Zero variants and disambiguation

- The slashed zero is the zero feature (`font-variant-numeric: slashed-zero`) in fonts that ship it; dotted-zero variants exist in some monospace and technical faces as character variants.
- In UIs where O (letter) and 0 (digit) are both shown (order IDs, serials), prefer a font whose zero is visibly distinct by design, or a monospace face for such strings; forcing the feature everywhere is not needed.
- I/l/1 and rn/m confusions are letterform issues; test them with real ID-like strings at production size.

## Fractions, ordinals, and superiors

- Precomposed fractions like one-half, one-quarter exist in Latin-1 (U+00BD, U+00BC, U+00BE) and a handful of others; anything else needs OpenType.
- The frac feature converts digit-slash-digit sequences into built fractions where the font supports it; numr and dnom expose numerator and denominator forms for custom assembly.
- Never fake fractions with superscript and subscript on full-size digits; the result never matches a real built fraction.
- Ordn converts ordinal markers (the letters after 1st, 2nd, 3rd) to superior forms; sups raises figures for footnote markers. Check both exist before promising footnote styling.
- Recipes and specs with many non-standard fractions: pick a font with strong frac/numr/dnom support, or accept diagonal "1/3" text and standardize it.

## Math notation in text fonts

Text fonts are not math fonts, and that is fine until someone asks for equations:

- Plus, minus, equals, and comparison signs exist in nearly every font but are often proportionally spaced and optically mediocre; aligning equations in a text font is a losing battle.
- The true minus sign is U+2212, distinct from hyphen-minus; typographically careful content should use it, and a font used for technical docs should be checked for it (some fonts omit U+2212, which then falls back jarringly).
- For real mathematics, use a math-aware stack: STIX Two Text pairs with STIX Two Math; LaTeX-derived projects use Latin Modern; web pages can render math via MathJax or KaTeX with their bundled fonts rather than the site's text font.
- Multiplication in running text: the proper sign is the multiplication sign U+00D7 (often drawn as a centered x); using the letter x reads as a typo at display sizes.
- Degrees, prime marks, and micro signs: check U+00B0, U+2032/U+2033, U+00B5 in technical content fonts; omissions are common.

## Currency coverage

Currency symbols are where older or narrower fonts fail, because the Unicode block kept growing:

- Euro U+20AC: near-universal, but check it in display faces.
- Pound U+00A3, yen U+00A5, cent U+00A2: universal in practice.
- Rupee sign U+20B9 was added to Unicode in 2010; fonts released before then, and many clones of old fonts, lack it.
- Turkish lira U+20BA (2012), ruble U+20BD (2014): frequent omissions in fonts frozen before those dates.
- Shekel U+20AA, won U+20A9, Thai baht U+0E3F: check per market.
- Some currencies are written with letters (Brazilian real as "R$", Polish zloty as "z" with a Latin-extended z); those need no special glyph but do need the formatting convention.
- Symbol position and spacing are locale decisions (before in the US, after with a space in much of Europe); handle in i18n formatting, not in the font.

## Practical guidance by context

- Dashboard and tables: tabular lining figures, right-aligned columns, monospace for IDs; see the dashboard application reference.
- Editorial body: proportional old-style if the font offers a tasteful set; lining otherwise. Consistency within a publication matters more than the choice itself.
- Prices: tabular figures for alignment in lists; consider a slightly larger size and heavier weight for the integer part; never let old-style figures wander through a price grid.
- Timers, counters, live scores: tabular figures are mandatory; proportional figures make the number visibly "breathe".
- Legal and regulatory small print: lining figures, generous size; check currency and section symbols coverage.

## Common mistakes

- Shipping proportional figures in a data table and calling the resulting wobble a design choice.
- Enabling old-style figures globally in a UI font that mixes prose and numbers, then fighting misalignment line by line.
- Using hyphen-minus where a minus sign is meant, or letter x for multiplication, in technical content.
- Assuming the rupee or lira sign exists in the brand font chosen years ago.
- Faking fractions with small caps or super/subscript, producing inconsistent stroke weights.
- Mixing figure styles across one page: prices in tabular lining, body in old-style, captions in something else, with no system.

## Decision rules

- One rule to start: tables and any changing number get tabular-nums; prose gets whatever the font's default reads as, checked once.
- If a font lacks tnum and the product is data-heavy: choose another font; this is a hard requirement, not a nice-to-have.
- Multi-currency products: run the currency codepoint checklist on every candidate font before shortlisting.
- Technical documentation: verify U+2212, U+00D7, primes, and degree signs; consider pairing with a dedicated technical or mono face for inline code and measurements.

## Comparison table

Figure settings by context, with the CSS that reaches them. The high-level font-variant properties compose predictably; prefer them over raw font-feature-settings:

| Context | Setting | CSS | Why |
| --- | --- | --- | --- |
| Data tables, dashboards | Tabular lining | font-variant-numeric: tabular-nums lining-nums | Columns align; changing values hold width |
| Editorial prose | Proportional old-style when offered | font-variant-numeric: oldstyle-nums proportional-nums | Figures sit in the text like letters |
| Price lists and grids | Tabular lining | font-variant-numeric: tabular-nums | Alignment across items and rows |
| Timers, counters, live scores | Tabular lining | font-variant-numeric: tabular-nums | No visible width breathing |
| Footnote and reference markers | Superior forms | font-variant-position: super | Real raised figures, not scaled caps |
| Order and serial IDs | Slashed zero or mono face | font-variant-numeric: slashed-zero (or a mono face) | O versus 0 disambiguation |
| Recipes and specifications | Built fractions where supported | font-variant-numeric: diagonal-fractions | Real built fraction instead of slash text |
| Ordinals in UI copy | Ordinal markers | font-variant-numeric: ordinal | Designed 1st/2nd/3rd forms |

Notes on the table:

- Defaults vary by design intent: classic text faces like Georgia default to old-style figures, which is why Georgia in a UI stack makes tables wobble until tabular lining is requested explicitly.
- A font can be excellent and still lack onum, frac, or sups; check the feature list per family (Wakamai Fondue and the foundry's specimen page both list them) before promising these settings in the design system.
- Tabular figures are a hard requirement for data-heavy products: if a candidate family lacks tnum, keep shopping.

## Worked example

An invoicing dashboard: totals, negatives, three currencies, and identifier strings:

1. Requirements: invoice line items and totals in aligned columns, negative values, USD, EUR, and INR, order identifiers that users read aloud to support.
2. Base font: a UI sans with a real tnum feature (IBM Plex Sans in this case), with IBM Plex Mono for identifiers.
3. Tables: font-variant-numeric: tabular-nums lining-nums on numeric columns; a screenshot diff with the feature off versus on shows the wobble the feature removes.
4. Negatives: the true minus U+2212 is verified present in both the sans and the mono; hyphen-minus is banned in rendered amounts by the formatter.
5. Currency gate: the rupee sign U+20B9 is checked before the India launch and is missing in a legacy brand font used by one email template; the template's stack is fixed before launch, not after a support ticket.
6. Identifiers: monospace plus slashed-zero policy for order IDs; the letter O and digit 0 confusion disappears at a glance.
7. Ordinals: font-variant-numeric: ordinal for billing-period copy; the font's designed forms replace the fake superscripts.
8. Verification: totals align across a 200-row column, currencies render from the same face, and the formatter's output passes the U+2212 and U+00D7 checks.

Outcome: a numeric UI where alignment is structural rather than lucky, and currency coverage was a gate instead of an incident.

## Field notes

- font-variant-numeric composes: tabular-nums lining-nums is a single coherent request; raw font-feature-settings with multiple tags is harder to reason about and overrides the high-level properties when both are present.
- Old-style figures in prices are a specific failure: the wandering baseline reads as broken alignment in a grid even when each number is individually beautiful.
- numr and dnom exist for custom fraction assembly; they matter when the font's frac feature only covers the Latin-1 precomposed set and your content needs 7/8 or 13/64.
- The multiplication sign U+00D7 versus the letter x, and the true minus U+2212 versus hyphen-minus, are content-pipeline checks: typography cannot fix the wrong codepoint, and the wrong codepoint survives every good font.
- Degrees U+00B0, primes U+2032 and U+2033, and micro U+00B5 are the technical-doc omissions that surface as jarring fallback glyphs; check them in documentation faces.
- Currency symbol age is a coverage predictor: fonts drawn before 2010 often lack the rupee U+20B9, before 2012 the Turkish lira U+20BA, before 2014 the ruble U+20BD. Clones of old fonts inherit the gaps.
- Math is a different category: STIX Two Text pairs with STIX Two Math, LaTeX-derived projects use Latin Modern, and MathJax or KaTeX bring their own fonts; do not stretch a text face over real equations.
- Symbol position (before the number in the US, after with a space in much of Europe) is an i18n formatting decision; the font only needs the glyph.
- Live-updating numbers with proportional figures visibly breathe as widths change; the tabular request belongs on the component, not on the page, so prose elsewhere keeps its default setting.
- Roman numerals have dedicated Unicode codepoints in the U+2160 block, but they are compatibility characters; typeset roman numerals as Latin letters and let the font's letterforms do the work.
- font-variant-position: super and sub work only where the font ships the sups and subs features; when it does not, browsers ignore the request rather than synthesizing, so verify the feature exists before deleting CSS-based positioning.
- Percent U+0025, per-mille U+2030, plus U+002B, and parentheses deserve a glance in display weights: symbols borrowed from a different weight stand out in headlines where body sizes would hide them.
- Choose one fraction convention per product (diagonal or stacked), document it in the tokens, and stop ad hoc decisions per component.
- Ranges in careful typography use the en dash between values; the web mostly survives on hyphens, but print-quality and PDF output deserve a documented convention and a font check for the dash and its spacing.
- If the formatter emits space-separated digit grouping, check the font draws the separator acceptably tight; a full space inside a dense table reads as two separate numbers.

## Quick reference

- One rule to start: tables and any changing number get font-variant-numeric: tabular-nums; prose gets the font's default, checked once.
- CSS set: tabular-nums, lining-nums, oldstyle-nums, proportional-nums, slashed-zero, ordinal, diagonal-fractions, stacked-fractions; font-variant-position: super and sub.
- Feature tags behind them: lnum, onum, pnum, tnum, zero, ordn, frac, sups, subs, numr, dnom.
- Codepoints to verify in technical and financial faces: U+2212 minus, U+00D7 multiplication, U+00B0 degree, U+2032 and U+2033 primes, U+00B5 micro, U+20AC euro, U+00A3 pound, U+00A5 yen, U+20B9 rupee, U+20BA lira, U+20BD ruble, U+20AA shekel.
- Zero policy: slashed or dotted zero for ID-like strings; otherwise rely on letterform quality and mono faces for serials.
- Fractions: prefer real built fractions via frac; numr plus dnom for custom assembly; never fake with scaled digits.
- Math: STIX Two for text-plus-math pairing; MathJax or KaTeX fonts for web equations; the site's text face stays out of it.
- Verification: a column of totals rendered with the feature toggled, currency gates run per market, and the formatter checked for U+2212 and U+00D7 discipline.
- Roman numerals: typeset with Latin letters; the U+2160 compatibility block is a trap, not a feature.
- Positional figures: verify sups and subs exist in the font before relying on font-variant-position; the request is ignored when the feature is missing.
- Ranges: pick the en dash convention deliberately for print-quality output, and let the formatter emit it consistently.

## Cross-references

- [OpenType features](../technical/opentype-features.md)
- [Dashboards and data-dense UI](../applications/dashboards-and-data-dense-ui.md)
- [Ecommerce typography](../applications/ecommerce-typography.md)
- [CSS handoff snippets](../workflow/css-handoff-snippets.md)

Compiled 2025 as part of the Fontlore project.
