# Dashboards and Data-Dense UI

What this reference covers: Typography for data-heavy interfaces: tabular numerals and column alignment, monospace for identifiers, density management, status text, and the unit-and-value patterns that keep numbers readable. Data UIs live or die on numeric typography; the font choice matters less than the features you enable.

## Numeric typography first

- Tabular figures (tnum) everywhere numbers sit in columns, update in place, or get compared: tables, KPI cards, charts, timers. Proportional figures make right-aligned columns wobble and changing values "breathe".
- Right-align numbers on the decimal point (or on the right edge for integers); center-aligned numbers are unreadable as a column.
- Consistent decimal places per column; a column mixing 1, 1.5, and 1.50 needs a formatting decision, not a font decision.
- Thousands separators and negative numbers: pick conventions and let the font's tabular figures handle alignment; the minus sign (U+2212 in careful contexts, hyphen-minus in practice) should render visibly at your sizes.
- Big KPI numbers: proportional figures are acceptable for single isolated values, but tabular everywhere avoids exceptions; consistency wins.
- Units: set units smaller and lighter next to the value (48 px value, 16 px unit), never baked into the number string in a way that breaks copy-paste.

## Monospace for identifiers and codes

- Order IDs, hashes, IPs, versions, log lines: monospace. It aligns, it disambiguates I/l/1 and 0/O, and it signals "this is a literal value users may copy".
- Choices with good UI manners: JetBrains Mono, IBM Plex Mono, Fira Code, Roboto Mono, Source Code Pro. Sizes 12 to 13 px; mono runs visually larger, so size down one step versus proportional UI text.
- Disable programming ligatures (or choose a mono without them) in data contexts; fi ligatures in an order number are a support ticket.
- Letter-spacing: none on mono; the face already handles rhythm.

## Density management

- Base density: 13 to 14 px body text, 11 to 12 px captions and metadata. Going below 12 px trades support tickets for pixels.
- Row heights derive from typography: line-height 1.4 plus fixed vertical padding; resist 28 px rows with 12 px text and 8 px of air, which read as cramped rather than dense.
- Hierarchy in dense UIs: weight contrast (500 labels versus 400 values) beats size contrast, which is expensive vertically.
- Density is a setting, not a decision: offer comfortable and compact modes by scaling a spacing token, keeping type sizes constant.
- Truncation rules: mid-string ellipsis for paths and IDs with a copy button and full-value tooltip; end-truncation for names. Truncation is a typography decision; document it.

## Status text and semantic labels

- Status pairs an icon or colored dot with text, never color alone (WCAG 1.4.1): "Failed", "Running", "Queued" as words, with the color as reinforcement.
- Uppercase tracking for status chips works if strings are short and controlled; long status strings in caps are unreadable. Cap tracked-caps labels at a few words.
- Timestamps: tabular figures, fixed format, monospace only if columns align across rows; "3 minutes ago" strings change width every render, so prefer absolute timestamps in tables.
- Semantic colors must pass contrast at the chip's size; amber-on-white is the classic failure.

## Charts and data visualization type

- Chart labels: 11 to 13 px, tabular where they number axes; axis labels right-aligned on the axis they measure.
- In-chart text uses the UI family, not the chart library's default; ship the font into the chart rendering context (canvas and SVG text need explicit font declarations).
- Legends and tooltips inherit the tabular setting; tooltip values changing width per frame is the same "breathing" problem as tables.
- Big number tiles: pick one scale (48/16, 40/14) and use it everywhere; ad-hoc per-card sizing reads as noise.

## Common mistakes

- Proportional figures in tables and live metrics; the entire interface shimmers as values update.
- Monospace with programming ligatures for identifiers.
- All-caps tracked status strings for messages longer than a few words.
- 11 px body text and 1.2 line-height "to fit more"; density comes from spacing tokens, not from illegibility.
- Chart text in the library's default font, clashing with the interface around it.
- Forgetting tnum in date columns; dates are numbers and wobble like them.
- Copy-paste breakage: styled minus signs, narrow spaces in numbers, or units inside value strings that users then paste into tickets.

## Decision rules

- Any column of numbers: tnum, right-aligned, consistent decimals; this is non-negotiable and belongs in the component, not the page.
- Any identifier users copy: monospace, explicit copy affordance, ligatures off.
- Any live-updating value: tabular figures and a fixed-width container if the value range is known.
- Font shortlisting for a data product: tnum support and weight range outrank personality; check numerals first in Wakamai Fondue.
- Density complaints: adjust spacing tokens before type sizes; if type sizes must drop, re-verify contrast and Windows rendering.

## Comparison table: monospace faces for values and identifiers

All monospaced faces align by construction; they differ in weight range, defaults, and voice:

| Face | Weights | Ligature default | Voice | Watch-outs |
| --- | --- | --- | --- | --- |
| JetBrains Mono | 100-800 | programming ligatures on | tall x-height, reads large | switch ligatures off in data cells |
| IBM Plex Mono | 100-700 | none | engineered, kin to Plex Sans | true italics exist; decide if you want them |
| Fira Code | 300-700 | programming ligatures on | the ligature-first face | wrong default for order IDs and codes |
| Roboto Mono | 100-700 | none | neutral, narrow, ubiquitous | personality budget near zero |
| Source Code Pro | 200-900 | opt-in | Adobe workhorse, kin to Source Sans 3 | wider advance than peers; size down a step |

- Mono guarantees equal advances, so the tnum conversation is over inside a mono face; it begins for proportional faces like Inter, IBM Plex Sans, Source Sans 3, and Public Sans.
- Size mono one step below proportional UI text at the same row height; mono runs visually larger.
- 0 versus O and 1 versus l versus I: pick a face whose zero style you accept everywhere, then keep it forever; consistency is the disambiguation.
- Weights: 400 for values, 500 for emphasized values; mono bold at small sizes fills counters.
- Dashboard canvases (chart libraries, PDF exporters) do not inherit your font by cascade; declare it in every rendering context explicitly.
- All five families are open licensed, so embedding them in exported PDF reports is uncomplicated.

## Worked example: a fleet logistics control tower

Scenario: a logistics company builds a control tower with live shipment tables, KPI tiles, an exception queue, and an audit log, displayed on 24 to 32 inch ops-room monitors and 13 inch laptops, by users who copy identifiers into tickets all day.

- Foundation: IBM Plex Sans for UI text and labels; IBM Plex Mono for identifiers, audit lines, and KPI values.
- KPI tiles: value in Plex Mono at weight 500, 32 px, with the unit ("min", "km", "%") at 14 px weight 400 outside the value string.
  - Delta lines: "+4.2% vs last week" with the direction word spelled out; color is reinforcement, never the whole signal.
- Shipment tables: 13 px Plex Sans with font-variant-numeric: tabular-nums on every numeric column; right-aligned numbers with right-aligned headers.
  - Date columns get tnum too; dates wobble like any number without it.
- Exception queue: status chips with a word plus a dot ("Delayed", "Held"), 12 px at 600; amber verified at 4.5 to 1 on both white cards and the dark header.
- Audit log: 12 px Plex Mono, one ink, no mid-identifier line wrap; white-space: nowrap with mid-string ellipsis and a per-row copy button.
- Timezones: absolute timestamps in tables and logs; relative strings ("3 minutes ago") only in detail headers, where width changes are harmless.
- Density modes: comfortable (36 px rows) and compact (28 px rows) via one spacing token; type sizes identical in both modes.
- Copy-paste discipline: values carry real minus signs and no styled spaces, so pasted strings survive into tickets and spreadsheets.
- Charts: Plex Sans declared inside the chart rendering context; axis labels 11 px, tabular, right-aligned to the axis they measure.
- Loading: skeleton cells sized to tabular widths so rows do not reflow when data lands.
- Rejected: Fira Code as the data mono (its ligatures merged characters inside IDs during the pilot), and a condensed proportional face for tables (saved columns, lost 13 px legibility on Windows).
- Result: no "the number moved" complaints after launch, and audit-log copies round-trip into tickets unchanged.

## Field notes

- The shimmer complaint is always proportional figures; fixing tnum once in the table component fixes every page that inherits it.
- Windows at 13 px is the truth test for the proportional face; mono faces are forgiving there, proportional ones are not.
- Sticky name columns with ellipsis plus right-aligned numbers is the layout that survives review; center-aligned numerals never do.
- Chart libraries default to Helvetica or whatever the canvas falls back to; inject the UI family or the dashboard reads as two products.
- Dark themes re-rank mono legibility; re-check the mono at weight 400 on the dark surface, not just on white.
- Units live in separate elements, never inside the value string; the day finance changes the currency label, a find-and-replace should not touch values.
- Negative values keep the real minus and right alignment; parentheses break both alignment and copy-paste.
- Percentages, currencies, and counts each get one formatting function; per-page formatting drift is how columns stop aligning.
- Thousands separators are a locale decision made once; the font renders whatever you hand it.
- IDs that wrap are IDs that get mistyped; nowrap plus mid-string ellipsis plus copy is the whole fix.
- Live-updating KPIs change width every frame; tabular figures plus a fixed-width container when the range is known.
- Skeleton loaders sized to tabular widths stop the reflow flash when data arrives.
- CSV and PDF exports must carry the same values the screen shows; styled minus signs and narrow spaces in exports are self-inflicted wounds.
- Status color pairs with a word at every size; amber-on-white is the classic 3 to 1 failure.
- Screen readers cannot absorb fifty value changes a minute; throttle live regions regardless of typography.
- Keyboard focus on dense tables needs a visible ring at 13 px; re-verify after any font swap because widths shift.
- The audit log is read during incidents at 2 a.m.; it deserves the best mono in the product and the least decoration.
- Empty and zero states render differently per font; check that a lone hyphen placeholder does not vanish at 12 px in your mono.

## Quick reference: dashboard numbers

- Numeric columns: tabular-nums, right-aligned, consistent decimals, headers aligned to the numbers.
- Live values: tabular figures mandatory; fixed-width containers when the range is known.
- Identifiers users copy: mono, nowrap, mid-string ellipsis, copy button.
- Mono shortlist: JetBrains Mono, IBM Plex Mono, Roboto Mono, Source Code Pro; ligatures off for data.
- Proportional faces with solid tnum: Inter, Source Sans 3, IBM Plex Sans, Public Sans.
- Mono size: 12 to 13 px, one step below proportional body text.
- Body 13 to 14 px; captions and metadata 11 to 12 px; no sentences below 12 px.
- Row heights from line-height 1.4 plus padding; density via spacing tokens, not font shrinkage.
- Status: word plus dot, never color alone; tracked caps only for short controlled strings.
- KPI tiles: one scale everywhere (32/14 or 48/16); units smaller and lighter, outside the value string.
- Charts: UI family declared in the rendering context; legends and tooltips inherit tabular figures.
- Timestamps: absolute and tabular in tables; relative strings only where width changes are harmless.
- Contrast: 4.5 to 1 for all text including chips, verified in both themes.
- Weights: 400 values, 500 labels and emphasis, 600 section heads; mono bold rarely helps.
- Exports: real minus signs, no styled spaces, values identical to screen.
- Copy affordances live next to anything users might retype.
- Font-feature-settings live in components, not pages, so every future view inherits the fix.
- Right-align headers over right-aligned numbers; centered heads over centered numbers never align with the data.
- Percent columns share one decimal convention; mixing 12.4 and 12.40 in one column reads as two formats.
- Test layouts with the longest realistic identifier in the first column, not the average one.
- Tooltips inherit the tabular setting; a tooltip whose numbers shift per hover reads as broken.

## Cross-references

- [Web and SaaS interfaces](web-and-saas-interfaces.md)
- [Numerals and notation](../scripts/numerals-and-notation.md)
- [OpenType features](../technical/opentype-features.md)
- [Contrast and hierarchy](../accessibility/contrast-and-hierarchy.md)

Compiled 2025 as part of the Fontlore project.
