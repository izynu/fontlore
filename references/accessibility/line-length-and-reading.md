# Line Length and Reading

What this reference covers: The measure (characters per line) and leading choices that make long-form reading comfortable, how they scale with font size, and the WCAG requirements that encode them. Line length is the most under-managed readability variable on the web: it costs nothing to fix and quietly degrades everything from docs to checkout flows when wrong.

## The measure targets

The widely accepted comfortable range for continuous reading is 45 to 75 characters per line, with around 66 as the classic optimum. WCAG 1.4.8 (Visual Presentation, AAA) sets a maximum of 80 characters. Below 45, the eye returns to the line start too often; above 75 to 80, return sweeps lose their place and reading pace drops.

- CSS provides the ch unit (width of the "0" glyph) for measure: max-width: 66ch on an article body is a good default, tuned per face because glyph widths differ.
- Set the measure on the text container, not the page: sidebars, cards, and metadata columns each get their own measure.
- Mobile: 30 to 45 characters is unavoidable and acceptable at larger relative sizes; do not force 66ch on a phone, do force it on desktop where designs often sprawl to 120.
- Headlines have their own measure logic (8 to 12 words per line); do not cap them at 66ch and force awkward breaks.
- The measure is also a mobile decision: at 30 to 45 characters, prefer the lower end of the leading band (1.5 to 1.6) so vertical rhythm does not collapse.

## Line height by size and role

Line height (leading) must scale inversely with size: small dense text needs relatively more leading, display sizes less.

- Body text: 1.5 is the floor for accessibility (1.4.12 assumes users may raise it to 1.5; 1.4.8 AAA asks for at least 1.5); 1.5 to 1.7 is the comfortable band for 16 to 18 px text.
- Large display: 1.1 to 1.25; tight leading is safe at display sizes and wrong for paragraphs.
- Small labels and captions: 1.3 to 1.4 with generous tracking only on short strings.
- Scripts with tall demands override these numbers: Thai, Devanagari, Arabic, Khmer, and Myanmar need 1.5 to 1.9 at body sizes to avoid clipped marks. Scope with :lang() rather than inflating globally.
- Paragraph spacing: 1.4.8 asks for paragraph spacing at least 1.5 times the line spacing; in practice, one blank line equivalent (0.75 to 1em) reads well and satisfies it.

## The interplay with font choice

- Wide faces reach 75 characters in a narrower container; a face with wide figures and spacing inflates ch-based measures differently. Measure in ch for the actual face, not a remembered pixel width.
- Typefaces with large x-heights tolerate slightly longer measures; small-x-height faces feel sparse at 75 characters and prefer 55 to 65.
- Old-style figures and generous inter-word spacing (serif book faces) change perceived density; judge the measure after the feature settings are applied (tnum vs pnum changes table widths, not body measure, but tracking changes do).
- Monospace faces: 66ch is far wider visually than in a proportional face; for code and mono content, 80 to 100 characters is conventional, and reading rules differ.
- Comfort check: a paragraph block at 1.5 leading should occupy roughly the vertical space its measure suggests; if it looks airless at 1.5, the face is dense and large-x-height, and 1.6 to 1.7 is the fix.

## Beyond the line: paragraph and block rhythm

- Left-aligned ragged right is the default for accessibility; justification without hyphenation creates rivers and uneven word spacing that harm tracking. If justification is required, enable hyphens: auto with correct lang attributes and test.
- Hyphenation: good with lang set, poor to nonexistent without it; browsers hyphenate per language dictionaries.
- Constrain width, not height: never clip paragraphs into fixed boxes; use "read more" patterns.
- Multi-column: CSS columns on the web are risky for reading order and focus; prefer single column at proper measure for accessibility-first products.
- Vertical whitespace between blocks (headings, figures, pull quotes) is part of reading comfort; typography hands these values to layout as tokens.
- Newsletters and email templates are reading surfaces too; a 600 px table with 90-character lines fails the same rules as a web article, and the fix is the same: a measure on the text, not on the wrapper.

## Common mistakes

- Desktop article pages at 100 to 140 characters because a max-width was set on a wrapper, not the text column.
- Line-height 1.2 everywhere because a display style leaked into body styles, or 1.8 everywhere because an accessibility pass over-corrected.
- ch used with a different font than the one rendering the text (measure tuned on the fallback).
- Justified text with hyphens: auto but no lang attribute, so the browser cannot hyphenate and the gaps balloon.
- Forgetting that content editors can paste long unbroken strings (URLs, codes); overflow-wrap: anywhere on body text prevents a single token from breaking the measure.
- Treating the measure as print dogma: the 66-character rule is for sustained reading; forms, tables, and UI text follow component logic instead.
- Setting the measure with max-width in px after tuning it in ch; the two drift apart the moment the type size changes.
- Widow and orphan wishful thinking: text-wrap: balance and text-wrap: pretty improve headings and paragraphs where supported; use them as progressive enhancement, never as the only plan.

## Decision rules

- Long-form content (docs, articles, email): 60 to 70ch, 1.5 to 1.6 leading, 17 to 18 px, left-aligned.
- Product UI text: measure is set by the component; enforce minimum line-height 1.4 for anything multi-line.
- Multilingual pages: per-language leading via :lang(), shared measure in ch re-checked per face per language.
- If a layout demands long lines: use a sidebar, larger type, or a wider gutter with the text column capped; never "just this once" 120-character paragraphs.
- Editorial redesigns: pick the measure first (it constrains everything), then the type size, then the family.

## Quick reference: values that ship

| Context | Size | Leading | Measure | Alignment |
| --- | --- | --- | --- | --- |
| Long-form article | 17 to 19 px | 1.6 | 60 to 70ch | Left |
| Documentation | 16 to 17 px | 1.6 | 65 to 75ch | Left |
| Marketing hero copy | 20 to 28 px | 1.4 | 40 to 55ch | Left or centered, short strings only |
| UI panels and forms | 14 px | 1.45 | component-bound | Left |
| Dense tables | 13 px | 1.4 | cell padding decides | Left; numbers right |
| Captions and metadata | 12 to 13 px | 1.4 | 40 to 60ch | Left |
| Code blocks | 13 to 14 px mono | 1.5 | 80 to 100 columns | Left |

Treat the table as starting points tied to the roles in your tokens, not as universal law; the per-face re-check (in ch, on the real font) is what makes them true.

## Worked example: the 140-character article

A publication's article page rendered 130 to 145 characters per line on desktop. Diagnosis and fix:

1. The layout wrapper had max-width: 1100px, and the article container inherited the full width; no measure was ever set on the text itself.
2. The fix is one rule on the prose container: max-width: 66ch, which on the body face at 18 px lands in the high 60s of characters per line.
3. Sidebars and figure captions get their own measures: 44ch for captions, since small sizes want shorter lines.
4. Pull quotes break out of the measure deliberately; breakouts are exempt, body text is not.
5. Verify in the CMS with the longest real article, including one with tables, because tables inside a 66ch column need their own overflow plan.

Result: return sweeps stop missing, reading pace recovers, and the page gains margin it can spend on pull quotes and whitespace. One rule, found by measuring characters, not pixels.

## Code notes: measure and leading in practice

```css
.prose {
  max-width: 66ch;          /* measure on the text container, not the page */
  font-size: 1.125rem;
  line-height: 1.6;         /* unitless so overrides and scaling survive */
  text-align: left;         /* ragged right by default */
  hyphens: auto;            /* only meaningful with correct lang attributes */
  overflow-wrap: break-word;
}
.caption { max-width: 44ch; font-size: 0.8125rem; line-height: 1.45; }

/* Per-language leading: scoped, not global inflation */
:lang(th) .prose, :lang(hi) .prose { line-height: 1.8; }
:lang(ar) .prose, :lang(ja) .prose { line-height: 1.75; }

/* Long unbreakable tokens (URLs, IDs) must not wreck the measure */
.prose .token { overflow-wrap: anywhere; }
```

Measure in ch is per-font: after a family swap, re-check the rendered character count once, because 66ch in a wide face is a different line than 66ch in a narrow one.

Leading floors vary by script; scope them with :lang() instead of inflating globally:

| Script | Body leading floor | Why |
| --- | --- | --- |
| Latin | 1.5 | The accessibility and comfort baseline |
| Cyrillic, Greek | 1.5 to 1.6 | Taller ascenders and descenders |
| Arabic, Hebrew | 1.6 to 1.7 | Diacritics and vertical stroke density |
| Devanagari and Indic scripts | 1.7 to 1.8 | Matras and conjuncts above and below the line |
| Thai, Lao, Khmer | 1.8 | Stacked marks above and below |
| Han scripts, Kana, Hangul | 1.7 to 1.9 | Dense glyph boxes; leading is the main air supply |

## Comparison table: measure guidance by face class

| Face class | Comfortable measure | Notes |
| --- | --- | --- |
| Proportional sans (Inter, Source Sans 3) | 60 to 75ch | Forgiving; tolerates the top of the range |
| Sturdy text serif (Source Serif 4, Literata, Lora) | 55 to 70ch | Classic book measure; watch long German compounds |
| High-contrast editorial serif in body duty | 45 to 60ch | Fatigues at long measures; keep display work short |
| Large x-height humanist sans | up to 75ch briefly | Still under the 80-character AAA ceiling |
| Monospace (JetBrains Mono, IBM Plex Mono) | 80 to 100 columns | Code convention; reading rules differ |
| CJK (Noto Sans SC/JP) | 35 to 45 characters | In CJK faces 1ch is close to one hanzi; count characters |

For CJK the character-count target, not the ch value, is the real control; treat ch as a convenient approximation only.

## Cross-references

- [Text spacing criterion](text-spacing-criterion.md)
- [Contrast and hierarchy](contrast-and-hierarchy.md)
- [Editorial and news](../applications/editorial-and-news.md)
- [CSS handoff snippets](../workflow/css-handoff-snippets.md)

Compiled 2025 as part of the Fontlore project.
