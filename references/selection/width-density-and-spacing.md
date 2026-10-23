# Width, Density, and Spacing

What this reference covers: How to choose between condensed, normal, and extended widths; how tracking and line spacing should change with size and medium; and how density decisions play out in interfaces and dense documents. Width is one of the most underused tools in typography.

Width choices change how much text fits, how it reads, and what it signals. Most teams inherit one width and never decide again. The rules below make width, tracking, and leading into explicit decisions.

## The width spectrum

- Condensed faces fit more characters per line and read as urgent, dense, or editorial. League Gothic is the classic free condensed; IBM Plex Sans Condensed brings the treatment to a system.
- Extended or expanded faces occupy more horizontal space and read as confident, graphic, and calm at large sizes; they fail quickly at small sizes and in narrow columns.
- Normal width is not a default to sleep through; it is a decision that most content most of the time should receive.
- Variable fonts with a wdth axis (Archivo, for example) make width a continuous dial; decide the stops you will actually use (two or three, named in the system).

## Choosing width by context

- Narrow columns, data-dense tables, and tall headline stacks: condensed earns its place; verify small-size legibility because compression punishes open apertures.
- Signage, hero sections, and poster-like moments: extended provides presence without extra weight.
- Long-form body text: normal width, almost always. Condensed body text fatigues; extended body text wastes measure.
- Bilingual or b Script layouts (Latin plus Arabic or Devanagari): remember width choices apply per script; a condensed Latin with a normal Arabic looks like two brands.

## Tracking by size

- Display sizes tolerate negative tracking; letters have room to spare. Tighten cautiously, a few thousandths of an em at a time.
- Text sizes need neutral to slightly positive tracking; negative tracking at 12px is a legibility self-own.
- All-caps settings want positive tracking at any size; caps lack the ascender rhythm that separates lowercase words.
- Small caps and overlines benefit from tracking that scales down with size, not up.

## Line spacing by size and medium

- Display headlines: line-height around 1.0 to 1.15. Tight leading binds multi-line headlines into a block.
- Body text on screens: 1.4 to 1.6 is the common range; taller x-heights and longer measures push toward the upper end.
- Print body text runs tighter than screen body text; do not carry print leading into CSS unchanged.
- Dense UI (tables, code, logs): 1.3 to 1.45 keeps rows scannable without collisions; check ascender and descender overlap explicitly.
- User-controlled spacing (accessibility settings, ebook readers) must survive your layout; fixed line-heights that assume one size break when users override.

## Density in interfaces

- Dashboards and tables want restraint: normal width, moderate x-height, tabular numerals, and consistent row rhythm. Personality comes from the display layer, not the cells.
- Density is a system property: if one screen is dense and the next is airy with no reason, the product feels unstable.
- Condensed widths in dense UIs trade horizontal space for vertical crowding; test the trade with real data, including the worst-case long strings.
- Numerals and monospace companions (see the monospace guide) solve alignment more honestly than cramming a proportional face does.

## Decision rules

- Default to normal width for anything users read in paragraphs; deploy condensed and extended deliberately and locally.
- Two named width stops beat a free wdth axis nobody governs.
- Tighten leading only as size grows; loosen it as size shrinks. The ratio is the design, not the absolute value.
- If a layout needs extreme tracking or width tweaks to "fit", the problem is usually the layout or the column measure, not the face.

## Common mistakes

- Shipping one width everywhere because the variable font made every width available.
- Condensed faces in body text; compression plus small size destroys apertures.
- Negative tracking inherited from a display style sheet into small UI labels.
- Fixed line-heights that break when users increase text size (a plain accessibility failure).
- Mixing condensed and normal widths at the same hierarchy level, which reads as inconsistency rather than intent.
- Forgetting that wide faces blow out narrow mobile columns even at headline sizes.

## Comparison table

Starting values by context. Tracking values are starting points; the face's native spacing is the authority, and these override it only with cause. The line-height column tightens as size grows and loosens as it shrinks.

| Context | Width | Tracking | Line-height | Measure |
| --- | --- | --- | --- | --- |
| Hero display, 48 to 96px | Normal or extended | 0 to -0.01em | 1.0 to 1.15 | 3 to 8 words per line |
| Section headline, 24 to 40px | Normal | 0 to -0.01em | 1.1 to 1.25 | Up to 10 words |
| UI labels, 11 to 13px | Normal | 0 | 1.2 to 1.35 | One line, truncate |
| All-caps eyebrows, 11 to 13px | Normal | +0.04 to +0.08em | 1.2 to 1.35 | 2 to 5 words |
| Body text, 14 to 16px | Normal | 0 | 1.4 to 1.6 | 45 to 75 characters |
| Long-form reading, 16 to 20px | Normal | 0 | 1.5 to 1.7 | 50 to 75 characters |
| Dense tables, 12 to 14px | Normal or condensed | 0 | 1.3 to 1.45 | Column-driven |
| Code and logs, 12 to 14px | Mono, fixed | 0 | 1.45 to 1.6 | Container-driven |
| Footnotes and legal, 11 to 12px | Normal | 0 | 1.4 to 1.5 | 45 to 65 characters |
| User-controlled reading | Normal | 0 | User setting; layout must survive | Reflow must survive |

The principle behind the columns: width changes track hierarchy or context, tracking goes negative only at display sizes and positive for caps, and line-height is a ratio decision, not an absolute number.

## Worked example

A dashboard density pass. The dashboard renders 14 columns of usage data, and the incumbent layout wastes a fifth of the viewport on spacing inherited from a display stylesheet.

1. Audit first: the stylesheet sets letter-spacing -0.02em globally, a display decision leaking into 12px table cells.
2. Rule applied: negative tracking never below 24px; the global override is removed.
3. Width decision: normal width retained; the condensed experiment compressed apertures at 12px and failed the small-size gate.
4. Line-height set to 1.35 for table rows: tight enough for density, loose enough that ascenders and descenders never collide.
5. Row rhythm check with the worst-case strings: long IDs in the mono companion, tabular figures in the sans for amounts.
6. Measure discipline: table cells truncate with an ellipsis beyond 30 characters rather than wrapping; wrapping is reserved for the detail pane.
7. Numerals: tabular figures enabled in the sans for all numeric columns; jitter disappears without going all-mono.
8. Condensed width earns exactly one job: the date-range picker labels, at 13px caps with +0.04em tracking, on the principle that caps want positive tracking.
9. The marketing hero keeps its extended display cut at 72px and 1.05 line-height; density rules stop at the marketing boundary.
10. User override test: browser text-size increase to 125 percent; the table reflows without clipping because line-heights are unitless.
11. Dark mode re-check: 1.35 line-height holds; the light-on-dark spread does not cause row collisions at this spacing.
12. Tokens recorded: table-line-height 1.35, label-tracking +0.04em for caps only, display-tracking -0.01em at 48px and up.
13. The audit report names the original sin (global display tracking) so the next stylesheet does not repeat it.

The reusable pattern: audit inherited values, apply the size-based rules, verify with worst-case strings and user overrides, then encode the results as tokens.

## Field notes

- Width is the most underused dial in product typography; most teams inherit one width and never decide again.
- Extended reads confident at 72px and broken at 14px; width choices are size-bound decisions, not brand constants.
- Condensed buys characters per line and pays in apertures; at small sizes the payment is unaffordable.
- Negative tracking inherited from display stylesheets is the most common typographic bug in design systems.
- Caps without tracking is a defect, not a style; all-caps want positive tracking at every size.
- Unitless line-heights survive user overrides; fixed pixel line-heights are accessibility failures waiting for a resize.
- Two named width stops beat a free wdth axis nobody governs.
- If a layout needs extreme tracking or width tweaks to fit, the layout or the measure is the problem, not the face.
- Tables want rhythm, not personality; density comes from spacing discipline, not from squeezing glyphs.
- Justified text in narrow columns creates rivers; left-aligned rag is the honest setting below 60 characters.
- Condensed and normal at the same hierarchy level reads as inconsistency; width changes should track hierarchy or context, not whim.
- Print leading does not survive the trip to CSS unchanged; screens need looser leading than ink.
- Check ascender and descender collisions explicitly when tightening line spacing on long-extender faces.
- Bilingual layouts apply width per script; a condensed Latin beside a normal Arabic reads as two brands.
- Density is a system property: one dense screen next to an airy one with no reason makes the product feel unstable.
- Monospace companions solve alignment more honestly than cramming a proportional face does.
- The wdth axis tempts continuous fiddling; freeze the stops in tokens and delete the dial from daily use.
- Measure failures masquerade as font failures; check the 45 to 75 character window before blaming the typeface.
- Spacing tokens are load-bearing: one tracking token reused across every size is how display tracking leaks into 12px labels.
- Width and case interact: condensed caps read denser than condensed lowercase; test the combination, not the width alone.

## Quick reference

- Default to normal width for anything users read in paragraphs.
- Condensed for narrow columns and tall headline stacks; verify small-size legibility first.
- Extended for signage, heroes, and poster moments; never for body or narrow columns.
- Display tracking: 0 to -0.01em, tightened a few thousandths of an em at a time.
- Body tracking: 0; negative tracking at 12px is a legibility self-own.
- All-caps tracking: +0.04 to +0.08em depending on size; caps need separation, not tightening.
- Display line-height: 1.0 to 1.15.
- Body line-height: 1.4 to 1.6; tall x-heights and long measures push to the top.
- Dense UI line-height: 1.3 to 1.45; verify ascender and descender collisions.
- Measure: 45 to 75 characters; the low 60s for articles.
- Table cells: truncate rather than wrap; wrapping belongs to detail panes.
- Tabular figures for numeric columns before reaching for a mono.
- Unitless line-heights only; user text-size overrides must survive.
- Two named width stops in tokens; the rest of the wdth axis is off-limits without a review.
- Width changes track hierarchy or context, never whim.
- Re-test width decisions in dark mode; optical spread changes with polarity.
- Print leading does not transfer to CSS unchanged; re-derive for screens.
- When layout fights the type, fix the layout or the measure first.
- Eyebrows and overlines: caps with positive tracking; never inherit the headline's negative tracking.
- Legal and footnote text keeps body line-height ratios; do not compress spacing because the size is small.

## Cross-references

- [X-height and legibility](x-height-and-legibility.md)
- [Choosing monospace](choosing-monospace.md)
- [Choosing display typefaces](choosing-display-typefaces.md)
- [Choosing body typefaces](choosing-body-typefaces.md)

Compiled 2025 as part of the Fontlore project.
