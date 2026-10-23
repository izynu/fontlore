# Ecommerce Typography

What this reference covers: Typography for commerce: product cards, price display mechanics, trust and legal small print, long-form product descriptions, and the mobile-first hierarchy that converts. Commerce type has one job above all: make price and product name scannable at speed.

## Product cards

- Product name: 14 to 16 px, two lines maximum with a consistent truncation rule; names are scanning anchors and must hold a fixed height across the grid.
- Price: the loudest element after imagery. Tabular figures are mandatory; grids of prices misalign without them (see the numerals reference for the feature details).
- Hierarchy inside the card: image, then price, then name, then meta (rating, shipping). Some shops invert price and name; either is fine, mixing per section is not.
- Meta text: 12 to 13 px, single line where possible; ratings and review counts use tabular figures too.
- Badges (sale, new, low stock): short strings only; tracked uppercase at 10 to 11 px with verified contrast, or pill backgrounds at 12 px.

## Price display mechanics

- Structure: large integer, smaller decimals and currency symbol (or symbol first, locale-dependent). Never one uniform string; the eye grabs the integer part.
- Currency symbol placement and spacing are locale decisions: before without space in the US, after with a space in much of Europe. Handle in i18n formatting; the font just needs the symbol glyph (check U+20AC, U+00A3, U+00A5, U+20B9, U+20BA, U+20BD for your markets).
- Sale displays: original price struck through with a real line-through at the same size or one step down, current price emphasized by weight and size; avoid red-everything, which fails hierarchy and accessibility at once.
- Per-unit pricing ("$4.50 per 100 g"): the qualifier is secondary text, tabular figure aligned with the main price where they stack.
- Installments and "from" prices: prefix words are secondary style; the numeric part keeps tabular alignment across the grid.
- Never use old-style figures in price grids; they misalign by design. If the brand face defaults to onum, override with lining-nums for commerce surfaces.

## Trust signals and small print

- Reviews, guarantees, return policies: 12 to 14 px with full contrast (4.5 to 1); small print is where trust dies when it goes gray-on-white at 3:1.
- Legal text (terms, shipping restrictions): 12 px minimum, lining figures, generous line-height (1.5); this text gets read precisely when something goes wrong, and that is the worst moment to be illegible.
- Security cues (payment icons, certificates): icons at non-text contrast 3 to 1; text labels adjacent, not baked into images.

## Long descriptions and detail pages

- Detail-page body: 16 to 17 px, line-height 1.5 to 1.6, measure 60 to 75ch; product descriptions are long-form reading whether or not the template admits it.
- Structure sells: bullet lists for specs, tables for dimensions, headings for sections. A wall of centered text reads as SEO filler and converts worse than structured content.
- Specs tables: tabular figures, left-aligned labels, right-aligned or tabular-aligned values; units in a consistent column.
- Mobile-first: descriptions collapse under a "read more" fold on mobile; typography must survive both states (no fixed heights; see the text-spacing accessibility work).

## Mobile-first hierarchy

- One column, one action: primary CTA typography (14 to 16 px, 500 to 600 weight) consistent across the funnel; button text is a promise, keep its size stable.
- Touch targets sized by layout, but type in buttons stays at 14 px minimum; 44 px targets with 11 px labels waste the target.
- Sticky purchase bars: price and CTA repeat at 14 to 16 px; the tabular figure requirement follows the price everywhere it goes.
- Form typography (address, payment): 16 px inputs on iOS to prevent zoom-on-focus; labels above fields, not placeholders-only.

## Common mistakes

- Price in a display face with old-style or proportional figures; the grid wobbles and the brand looks cheap without anyone knowing why.
- Six levels of hierarchy on a product card; cards support three, maybe four.
- Gray 11 px meta text failing contrast; the accessibility audit and the conversion audit find the same bug.
- Centered, justified long descriptions on desktop.
- Currency symbols missing from the brand font for a launch market (rupee, lira, ruble are the repeat offenders).
- Truncation rules applied inconsistently, so cards in one grid hold one, two, or three lines and the grid ripples.

## Decision rules

- Any numeric column or price grid: tabular lining figures, right-aligned; put it in the component once.
- Price typography: integer dominates, decimals and symbol step down, locale formatting owns position.
- Product name display: fixed two-line block with ellipsis; never variable height inside a grid.
- Small print floor: 12 px and full contrast; if legal demands smaller, the layout is wrong, not the floor.
- New market launch: currency glyph check plus the script checklist before shipping templates.

## Comparison table: price display patterns

Price typography is a component decision made once and reused everywhere money appears:

| Pattern | Anatomy | Where it belongs |
| --- | --- | --- |
| Dominant integer | integer 22 to 32 px at 600; decimals and symbol 14 to 16 px at 500 | product grids and detail pages |
| Uniform tabular | single size 16 to 18 px at 500, lining tabular figures | cart lines, checkout summaries, invoices |
| Strike-and-emphasize | original struck at the same integer size but 400; current price one step up | sale rows and campaign pages |
| Per-unit qualifier | main price plus "per 100 g" at 12 to 13 px secondary | groceries and consumables |
| Range display | "from 19.00" with the prefix in secondary style, numerals tabular | listings with variant pricing |

- Every pattern uses lining tabular figures; proportional or old-style figures make a price grid wobble and read cheap.
- Currency symbol position and spacing are locale formatting decisions, not design decisions; hard-coded placement breaks the second market.
- Sale color is reinforcement: the strikethrough and the weight change carry the message, because small red text usually fails 4.5 to 1 on white.
- The strikethrough is a real text decoration on the same face; an SVG line breaks screen readers and survives font swaps badly.
- Line-height: tight (1.1 to 1.2) inside the price group, generous between price and meta; a price is one visual unit.
- Test the component against the longest realistic string (a seven-figure price with separators) and the shortest, before approving it.

## Worked example: a grocery storefront

Scenario: a mid-size grocery chain rebuilds its storefront with twelve locales, price grids on every page, mobile-first traffic above 70 percent, and an open-license-only font budget.

- Foundation: Public Sans for UI, prices, and tables; tabular figures and civic plainness suit price-heavy layouts, and the license deploys freely across twelve locales.
- Brand voice: Fraunces for campaign headers and category titles at 28 to 44 px, weight 600, always above the grid, never inside it.
- Price component: integer 22 px at 600; decimals and symbol 14 px at 500; stacked per-unit qualifier at 12 px; font-variant-numeric: tabular-nums lining-nums on the group.
  - Sale rows: original at the same integer size, weight 400, real line-through, full-contrast gray; current at 600 with an 11 px tracked-caps badge checked for contrast.
- Product cards: image, name at 15 px in a fixed two-line block with ellipsis, price, then meta at 12 px; rating counts tabular.
- Trust layer: delivery estimates, return links, and review snippets at 13 px full contrast; legal small print at 12 px minimum with 1.5 leading.
- Detail pages: body 16 px, 1.6 leading, 65ch measure; specs in tables with tabular figures and a consistent unit column.
- Cart and checkout: the same price component at uniform tabular sizing; totals, subtotal, and per-line prices align as one table.
  - Sticky purchase bar: price and CTA repeat at 14 to 16 px; the tabular rule follows the price into overlays.
- Form typography: 16 px inputs on iOS to prevent zoom-on-focus; labels above fields, never placeholder-only.
- Launch checklist catch: the rupee sign was missing from the first font pick; the currency glyph check (rupee, lira, ruble on the roadmap) forced an early swap instead of a launch-week fire drill.
- German strings ("Inklusive MwSt.") doubled meta line lengths; the meta slot became a two-line reserve instead of a one-line ellipsis.
- Rejected: a display serif for prices (brand charm where scanning was the job) and old-style figures anywhere near money.
- Result: one price component everywhere, alignment complaints gone, and receipt emails recognizable even in system-font fallbacks.

## Field notes

- Users scan price before product name in grids you test yourself; treat price typography as conversion infrastructure, not styling.
- Tabular figures are invisible when present and obvious when absent; the grid tells on you.
- Gray small print is where trust dies; return policies and shipping terms get read precisely when something went wrong.
- Currency glyphs missing from a brand font surface late, usually in a market launch; check at template time.
- Per-unit pricing prevents shrinkflation guesswork in support tickets; typography keeps the qualifier secondary.
- "From" prices need tabular numerals across the grid or the ranges look jagged.
- Cart inherits the grid's price component; the moment checkout redraws prices differently, users smell an error.
- Old-style figures in a brand face charm in headlines and misalign in invoices; override with lining-nums on commerce surfaces.
- Review counts and ratings: tabular counts, and never color-only stars.
- Buttons: 14 to 16 px at 500 to 600, identical across the funnel; a shrinking CTA reads as hesitation.
- Badges ("Sale", "New") are typography too: short strings, verified contrast, one style per store.
- A/B tests that change price size also change wrap points; re-test truncation when testing size.
- Emails run on system stacks; design the receipt so the price hierarchy survives Calibri.
- Jurisdictions regulate price presentation (strike-through history, unit pricing); typography implements the rules, it does not invent them.
- Product names truncate by one rule per grid; mixed truncation makes the whole grid ripple.
- Centered justified description text reads as filler and converts worse than structured content.
- Stock and urgency messages ("Only 3 left") take the metadata style, not a display style; urgency is a word, not a font.
- The price is the only element that appears in grid, card, detail, cart, bar, and email; it earns the most careful component in the system.

## Quick reference: commerce floors

- Price grids: lining tabular figures, right-aligned, set once in the component.
- Price anatomy: integer dominates; decimals and symbol step down; locale owns placement.
- Product names: 14 to 16 px, fixed two-line block, one truncation rule per grid.
- Meta text: 12 to 13 px, single line where possible, tabular counts.
- Badges: 10 to 11 px tracked caps or 12 px pills, contrast verified.
- Small print: 12 px floor, 4.5 to 1 contrast, 1.5 leading.
- Detail body: 16 to 17 px, 1.5 to 1.6 leading, 60 to 75ch measure.
- Buttons: 14 px floor, stable size across the funnel.
- Inputs: 16 px on iOS to prevent zoom-on-focus.
- Currency glyphs verified per market (rupee, lira, ruble are repeat offenders).
- No old-style figures on any money surface; lining-nums override where the brand face defaults otherwise.
- Sale display: real line-through at equal or one-step-down size; color as reinforcement only.
- One price component everywhere money appears, including sticky bars and receipts.
- Trust text at full contrast; small print is read exactly when trust is at stake.
- Every new market triggers the glyph check and the script checklist before templates ship.
- Ratings and review counts use tabular figures like prices; counts misalign the same way.
- Per-unit qualifiers stack under the main price, aligned to its integer edge.
- Installment strings keep the numeric part tabular alongside the words.
- The purchase bar's price mirrors the grid's price component exactly; two treatments of one price read as two prices.
- Free-shipping thresholds and cart totals: tabular, full contrast.
- Test grids with the longest product name in the catalog, not the average.
- Structured descriptions (bullets, spec tables, headings) beat walls of centered prose on every measured funnel.

## Cross-references

- [Web and SaaS interfaces](web-and-saas-interfaces.md)
- [Numerals and notation](../scripts/numerals-and-notation.md)
- [Contrast and hierarchy](../accessibility/contrast-and-hierarchy.md)
- [Worked examples](../workflow/worked-examples.md)

Compiled 2025 as part of the Fontlore project.
