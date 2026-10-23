# Packaging and Retail

What this reference covers: Typography for physical packaging and retail environments: shelf-distance legibility, mandatory regulatory text and its size floors, print production constraints (substrates, knockouts, ink spread), and how a brand type system maps onto a box. Print is unforgiving; these rules are older than the web and still enforced by physics.

## Shelf impact and the three-foot test

- Packaging is read at distances: category block at 3 meters (brand recognition), product name at arm's length, claims and details in hand. Each distance needs a typographic layer; a box that only works in hand disappears on shelf.
- The silhouette test: blur the design or squint; if the product name and brand do not survive as shapes, the hierarchy is wrong. Weight and size carry this, not color.
- Flavor/variant systems: one layout, variable words. Set the variant word in a size and weight that survives both "Mint" and the longest variant in the line; check all of them, every time.
- Front-of-pack word count is a design constraint: three messages maximum, each with a defined typographic rank.

## Regulatory text and size floors

Mandatory information has legal minimums, and they are size floors, not suggestions:

- EU food information (Regulation (EU) No 1169/2011): mandatory particulars must use a font size where the x-height is at least 1.2 mm; when the largest surface is under 80 square centimeters, 0.9 mm applies. X-height, not point size: the brand face's x-height ratio determines whether your nominal size passes.
- Nutrition declarations and ingredient lists have their own layout conventions (tables, minimum spacing); typography must accommodate both.
- US and other jurisdictions have their own floors; the pattern is identical: mandatory text has a minimum physical size, measured in the real world, not in CSS pixels.
- Practical consequence: the legal floor often sets the smallest size in the whole system; everything else sits above it. Compute the floor early (x-height in millimeters at print scale) and design up from there.
- Nutrition tables: tabular figures and aligned columns are as mandatory in practice as in web UI; misaligned nutrition panels fail review and look unsafe.

## Print production basics

- Minimum sizes: positive (dark on light) text survives down to about 5 to 6 pt for legal copy; reversed (light on dark) text needs more, practically 7 to 8 pt and a sturdier weight, because ink gain fills counters on press.
- Ink spread on uncoated stock closes small apertures and counters: avoid hairline weights, thin serifs, and delicate scripts below about 10 pt on uncoated substrates; lighter weights get bumped one step.
- Knockouts out of dark panels: increase weight and size versus positive text; fine strokes disappear into the dark ink.
- Registration: tiny multicolor text (misregistered by a hair) turns to mush; keep small text in one ink (black or a spot) whenever possible.
- Barcodes and QR codes are not typography but they constrain it: keep type out of their quiet zones.
- Dielines: text respects fold and trim margins; nothing critical within 3 mm of a cut or fold. Backing panels and flaps change what "adjacent" means; proof on the actual dieline.

## Substrate and finish effects

- Uncoated paper stock: softer dots, more spread; favors sturdier serifs and sans, heavier weights, larger minimums.
- Coated stock: crisper; more room for contrast and detail.
- Corrugated and kraft: coarse surfaces demand bold, simple forms; delicate faces vanish. Direct printing on corrugated is closer to stamping than to offset; plan for it.
- Metallic, foil, and spot varnish accents: text in foil needs more size and simpler forms than text in ink; thin strokes in foil break.
- Embossing and debossing: shapes only; extremely fine detail fails. Choose faces with sturdy stems if the brand wants embossed type.

## Mapping the brand system onto packaging

- The brand's display face fronts the pack; the UI sans rarely belongs on shelf; packaging usually needs a third voice only for mandatory legal text, which can be the brand sans at its print floor.
- Files travel: vendors need fonts or outlines; outlined artwork for anything fixed, licensed font files only where text is typeset by the vendor, with the license checked for vendor use (see the licensing references).
- Proofing: color proofs on the actual substrate, not screen; typography is judged at print scale with the x-height ruler on the mandatory text.
- Versioning: packaging lives for years; pin the exact font versions used for approved artwork in the brand's asset register, or a re-order reprint will drift.

## Common mistakes

- Designing in CSS pixels and scaling to print without recomputing x-height floors for the mandatory text.
- Reversed thin-weight legal text that disappears on the uncoated inner panel.
- Variant name set at a size that fits six variants but not the seventh; check the full variant list, always.
- Hairline rules and delicate scripts on kraft or corrugated.
- Legal text in the display face because "the brand is one font"; mandatory copy has floors, and display faces have fragile counters.
- Sending live font files to vendors without checking license terms; outline the artwork instead.

## Decision rules

- Start from the floor: compute the mandatory text minimum in millimeters of x-height on your substrate, then build the hierarchy above it.
- Substrate dictates weight: uncoated and corrugated bump every small weight one step.
- Small text: one ink, positive if possible, sturdy weight, no hairlines.
- The variant system is tested against the longest variant string before the layout is approved.
- Any font leaving the studio: outlined artwork unless the vendor's typesetting requires otherwise, with license terms confirmed in writing.

## Comparison table: type roles on a pack

Packaging assigns each role its own distance, size, and constraints; the cast is small:

| Role | Reading distance | Typical print size | Face class | Hard constraints |
| --- | --- | --- | --- | --- |
| Brand lockup | 1 to 3 m | large, drawn or display | display or lettering | fixed, outlined, trademark-clean |
| Product name | about 1 m | 30 to 70 pt | display or sturdy text | survives the longest variant string |
| Claims and benefits | in hand | 12 to 18 pt | UI sans or text face | three messages maximum |
| Variant or flavor | in hand | 12 to 18 pt | UI sans | one slot; longest string sets the size |
| Prep and instructions | in hand | 7 to 9 pt | sturdy text | positive, one ink preferred |
| Legal and regulatory | close | 5 to 8 pt | sturdy text | x-height floors; avoid reversing |

- These are roles, not brands: one display voice, one workhorse, and legal text at its floor is the entire cast.
- Hierarchy between adjacent roles is kept by weight and position, because print sizes are less elastic than screen ones.
- Every role has a print floor that beats the screen floor; packs are designed bottom-up from the legal minimum.
- If the brand owns only a display face and a UI face, the UI face inherits legal text; check its x-height clears the rule.

## Worked example: a granola front of pack

Scenario: a food brand designs a 500 g kraft pouch for the EU market: five flavor variants (the longest is "Sea Salt and Caramel"), a mandatory nutrition panel, uncoated substrate, and an identity built on Archivo.

- Distance layering: the drawn brand lockup reads at three meters; the product name in Archivo at weight 800 reads at arm's length; flavor and claims in Manrope read in hand.
- Front-of-pack discipline: three messages maximum (brand, name, one claim), each with a defined rank; everything else moved to the side panel.
- Variant system: the flavor word's size is fixed by the longest variant, not the average; "Mint" keeps whitespace, "Sea Salt and Caramel" fills its line, and the layout never reflows.
- Legal floor first: mandatory particulars use a size whose x-height clears the 1.2 mm EU floor, measured with an x-height ruler on the print proof, not estimated from the CSS mockup.
- Nutrition panel: tabular figures, aligned columns, one ink; set in Manrope at 7.5 pt positive black because reversed text at that size fails on kraft.
- Substrate bumps: every weight on the uncoated kraft is one step heavier than the screen design; the hairline rule under the brand became a 0.5 pt rule that survives ink spread.
- Quiet zones: the barcode and QR block reserves its margins; no typography enters them, however tempting the corner.
- Vendor pack: outlined artwork for the fixed design; live font files only where the vendor typesets nutrition translations, with license terms confirmed in writing first.
- Proof loop: two proof rounds on the actual substrate; the second caught a reversed batch code dropping below legibility and bumped it one weight.
- Multilingual check: German and French legal strings ran longest; the variant and legal slots were sized on those, not on English.
- Aftermath: five variants share one dieline with a variable word slot, and the printer's press-check questions were about ink, not about type.

## Field notes

- The three-foot test uses a real mockup at arm's length and a squint; a screen at 100 percent lies about print.
- Regulators measure x-height, not point size; two faces at the same point size can pass and fail the same rule.
- Uncoated stocks close counters and apertures; what looked delicate in the studio looks broken on shelf.
- Reversed text is the first casualty; budget one extra point of size and one weight step for anything knocked out of a dark panel.
- Foil and embossing simplify letterforms by force; thin strokes in foil break, fine serifs in emboss fill in.
- Direct corrugated printing is closer to stamping than offset; faces that survive it are bold, simple, and slightly condensed.
- Small mandatory text stays in one ink; misregistered multicolor text at 6 pt is mush before it leaves the press.
- The variant list is a design input, not an afterthought; the seventh flavor arrives right after the sixth is approved.
- Nutrition tables with proportional figures fail review and look unsafe even when the numbers are right.
- Vendors do not need your fonts for fixed artwork; outlines are the license answer and the versioning answer at once.
- Pin font versions per approved artwork in the asset register; a re-order reprint two years later must match the shelf.
- The legal floor is the floor of the whole system; compute it first and design upward, never downward from the hero.
- Dielines change adjacency; a flap fold can put a caption three millimeters from a cut.
- Barcode quiet zones are specification, not etiquette; type inside them fails at the register.
- Proofs are judged at print scale under print light; a laptop screen in a bright studio is the opposite of both.
- Spot varnish over small text can fill counters; ask the printer before varnishing type.
- Translation grows German and French; the variant slot must hold the longest legal string in every market.
- If the brand face has fragile hairlines at text sizes, the brand sans at a heavier weight becomes the legal voice; mandatory text is not the place for personality.

## Quick reference: packaging floors and clearances

- EU mandatory particulars: x-height at least 1.2 mm; 0.9 mm when the largest surface is under 80 square centimeters.
- Positive small text: about 5 to 6 pt practical floor; reversed: 7 to 8 pt plus a weight step.
- Uncoated and corrugated: bump small weights one step; no hairlines below about 10 pt.
- One ink for small text; registration tolerance eats multicolor detail.
- 3 mm clearance from cuts and folds for anything critical.
- Barcode and QR quiet zones reserved before typography places anything.
- Variant systems tested against the longest variant string, every time.
- Nutrition panels: tabular figures, aligned columns, one ink.
- Brand block judged at three meters; name at arm's length; details in hand.
- Outlined artwork for fixed pack files; vendor font use licensed in writing.
- Font versions pinned per approved artwork in the asset register.
- Proofs on the actual substrate, twice, judged at print scale.
- X-height measured on the proof, never inferred from screen size.
- Every market's legal and variant strings checked before approval.
- Front of pack: three messages maximum, each with a defined rank.
- The legal floor sets the system's smallest size; design up from it.
- Kraft and corrugated proofing is non-negotiable; coated results do not transfer.
- Reversed legal text gets one extra point and one weight step, minimum.
- Ingredient and allergen lists follow the same x-height floor as other mandatory text.
- Flavor and claim strings proofed in every market language before dieline approval.
- Embossed type uses sturdy stems; hairlines fail in relief.
- Print vendors receive outlines plus a proofing spec, not font files.

## Cross-references

- [Branding and logotypes](branding-and-logotypes.md)
- [Contrast and hierarchy](../accessibility/contrast-and-hierarchy.md)
- [Numerals and notation](../scripts/numerals-and-notation.md)
- [Brief to constraints](../workflow/brief-to-constraints.md)

Compiled 2025 as part of the Fontlore project.
