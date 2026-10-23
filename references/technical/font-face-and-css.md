# Font-face and CSS

What this reference covers: Writing @font-face rules correctly: family naming, src order, weight and style descriptors, unicode-range, variable font ranges, and how feature settings fit in at the usage site. Most webfont bugs trace back to one of these descriptors being wrong.

## Anatomy of a correct rule

A production @font-face for a static weight:

- font-family: "Inter" - your private name for the family inside CSS. It does not need to match the installed font's name, and naming it the same as a system font is a hack that backfires unpredictably.
- src: url("inter-latin-400-normal.woff2") format("woff2") - one modern source is usually enough; add a WOFF second only for genuinely legacy targets. The browser uses the first source it can handle, so order is meaningful.
- font-weight: 400 - the descriptor declares what this file actually is. It must be honest; claiming 400 for a 300 file breaks weight matching everywhere.
- font-style: normal; font-display: swap; and optionally unicode-range, size-adjust, and metric overrides.
- The same family name repeats across rules: 400, 400 italic, 700, 700 italic each get their own block with accurate descriptors. The browser then composes font-weight: bold requests correctly.

The most common structural error is giving each weight a different family name (InterBold, InterLight). That forces authors to hardcode families instead of weights, disables proper weight interpolation, and breaks user stylesheets and accessibility overrides.

## Variable font rules

A variable file declares its ranges:

- font-weight: 100 900 tells the browser this face spans the weight axis; requests like font-weight: 550 then resolve continuously.
- font-stretch: 75% 125% and font-style: oblique 0deg 10deg (or italic) do the same for wdth and slnt/ital where present.
- font-optical-sizing: auto at the usage site maps font-size to the opsz axis; do not disable it without reason.
- Named instances are not needed on the web; the continuous ranges are the point. If you must support very old browsers with a variable file, provide static fallback faces before deciding that is worth it.

## unicode-range in practice

- Declare the codepoints each file actually contains; the browser downloads a face only when content touches its range.
- For a Latin site with German and French content, latin plus latin-ext files suffice; Vietnamese requires the vietnamese range file, and a missing range silently falls back to system fonts mid-word.
- Ranges must be accurate: a range wider than the file invites missing glyphs; narrower wastes the file. When subsetting yourself, generate ranges from the actual subset with tooling rather than hand-writing them.
- One subtle behavior: characters not covered by any declared range fall to the next font in the stack even if the file would have contained them; this is how multilingual stacks are composed.

## Feature settings at the usage site

@font-face enables nothing by default beyond the font's own defaults. Turn features on where you use the text:

- Prefer high-level properties: font-variant-numeric: tabular-nums; font-variant-caps: small-caps; font-variant-ligatures: common-ligatures no-discretionary-ligatures.
- Use font-feature-settings only for things high-level properties cannot express, such as stylistic sets ("ss01" 1) or character variants, and prefer @font-feature-values with font-variant-alternates for named alternates.
- Do not mix high-level and low-level on the same element; font-feature-settings wins and makes the stylesheet unreadable.
- Disable ligatures or kerning only with cause; kerning stays on by default and should stay on.

## Preventing synthesis

When the requested weight or style has no face, browsers synthesize fake bold or fake oblique. In CJK, Devanagari, and display faces this looks immediately broken:

- Declare every weight you actually use, and no more; unused weights are bytes, undeclared weights are synthesis.
- font-synthesis: none on elements where a fake would be worse than nothing (icon fonts, monospace data); the shorthand font-synthesis-weight/style exist for finer control.
- Italic on a family without italics: either load real italics, or accept synthesis consciously and document it. In Arabic and Devanagari, slanted "italics" are typographically wrong; use weight or color instead.

## A robust default block set

For a typical UI family, the handoff includes: one variable face (weights 100-900, normal style), one variable italic face if the design uses italics, unicode-range per subset (latin, latin-ext, cyrillic, greek, vietnamese as needed), font-display: swap, and metric-adjusted fallback declared via size-adjust on a fallback @font-face. Static-weight projects follow the same shape with one block per weight.

## Common mistakes

- Dishonest descriptors: a 600 file labeled 700, or a single file declared for all weights, which silently disables real weight rendering.
- Per-weight family names, as above; it always ends in tears during a redesign.
- Forgetting font-style: italic on italic blocks, so italics never trigger and text synthesizes instead.
- unicode-range hand-written from memory instead of generated from the subset, producing phantom ranges.
- Putting @font-face inside a media query or after usage in a way that delays resolution; font-face blocks are global, keep them together and early.
- Testing @font-face in one browser with the font installed locally; install-cache hides descriptor errors. Test in a clean profile.

## Decision rules

- Static site with two weights: two static files, honest descriptors, no variable complexity.
- Design system using many weights and some interpolation: one variable file per style, ranges declared, optical sizing auto.
- Any multilingual content: unicode-range subsets are mandatory, generated by tooling.
- Data-heavy UI: declare tabular-nums at the table level and confirm the loaded face supports it; declaration without support is a no-op.
- If a needed style is missing from the family: decide consciously between synthesis, a different font, and dropping the style; do not leave it to chance.

## Comparison table

| Descriptor | Declares | Classic mistake |
| --- | --- | --- |
| font-family | the CSS-side name for this face | per-weight names (InterBold, InterLight) |
| src | file URLs and their formats | TTF listed first; local() pointing at an uncontrolled installed copy |
| font-weight | the weight (or range) this file renders | a static file declared as a range; a dishonest 400 on a 300 file |
| font-style | normal, italic, or an oblique angle range | missing italic on italic blocks, so italics synthesize |
| font-display | load and swap behavior | left at auto, which is block in practice |
| unicode-range | the codepoints this file covers | hand-written ranges that drift from the actual subset |
| size-adjust | fallback glyph scaling | applied to the primary face instead of the fallback |
| ascent-override, descent-override, line-gap-override | line-box metrics for the fallback | nonzero line-gap re-adding leading |
| font-stretch | the width range of a variable file | omitted, so wdth silently never engages |

## Code notes

Static weight with honest descriptors (latin range abbreviated for reading):

```
@font-face {
  font-family: "Inter";
  src: url("/fonts/inter-latin-400.woff2") format("woff2"),
       url("/fonts/inter-latin-400.woff") format("woff");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+2013-2014, U+2018-201D, U+20AC;
}
```

The 700 block repeats the same family name with font-weight: 700; bold text then resolves to it automatically.

Variable face declaring its ranges:

```
@font-face {
  font-family: "Inter";
  src: url("/fonts/inter-var-latin.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}
```

Named alternates keep feature numbers out of component code:

```
@font-feature-values "Inter" {
  @styleset { disambiguated: 1; }   /* binds to ss01 */
}
.mono-label { font-variant-alternates: styleset(disambiguated); }
```

Loading and checking from JavaScript when canvas or measurement depends on a face:

```
await document.fonts.load("700 16px Inter", "Sample text");
document.fonts.ready.then(measureEverything);
document.fonts.check("700 16px Inter"); // true once loaded
```

## Field notes

- Chrome's Computed pane shows a "Rendered fonts" row: which family actually painted and whether synthesis kicked in. It is the fastest answer to "is the webfont even loading".
- DevTools' Rendering panel has a "disable local fonts" switch that unmasks descriptor errors hidden by an installed copy of the family.
- src is first-supported-wins: put woff2 first or modern browsers will happily download the larger file listed earlier.
- One family with many blocks is what makes font-weight: bold, user stylesheets, and editor toolbars work; per-weight family names break all three.
- A broken src URL still burns the block period: text stays invisible, then swaps. Fix the URL, not the display value.

## Quick reference

- One family name, many blocks: each weight and style gets its own @font-face with honest descriptors.
- src order: woff2 first, woff second for a real legacy tier, TTF never as a webfont.
- font-display: set it explicitly; auto is block in practice.
- unicode-range: generate from the subset's cmap, never from memory.
- Variable faces: declare the range (font-weight: 100 900) and keep font-optical-sizing: auto at the usage site.
- Metric overrides: they live on the fallback face, never on the primary.
- Synthesis: declare every weight you actually use; font-synthesis: none where a fake would be worse than nothing.
- Test in a clean profile or with local fonts disabled; an installed copy hides every descriptor error.

## Cross-references

- [Webfont formats](webfont-formats.md)
- [Variable fonts and axes](variable-fonts-and-axes.md)
- [OpenType features](opentype-features.md)
- [Fallback metrics and CLS](fallback-metrics-and-cls.md)

Compiled 2025 as part of the Fontlore project.
