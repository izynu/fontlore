# DM Serif Display: typeface overview

What this reference covers: DM Serif Display as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | DM Serif Display |
| Slug | dm-serif-display |
| Designer | Colophon Foundry |
| Foundry | Colophon Foundry |
| License | OFL-1.1 |
| Category | serif |
| Classification | didone |
| Source | https://fonts.google.com/specimen/DM+Serif+Display |

## Position in the taxonomy

The data layer files DM Serif Display under serif with the didone classification. Tags: didone, marketing, display.

Data-layer note: didone display companion to DM Sans; confident marketing headlines

## Script and subset coverage

| Script or subset | Record |
| --- | --- |
| latin | declared in the data layer |
| latin-ext | declared in the data layer |
| vietnamese | declared in the data layer |

Coverage is recorded as declared by the upstream catalog. Before shipping a multilingual product, run the strings from the project through the family; see the cross-referenced testing guide at the end of this file.

## Technical profile

Variable build: no. Serve static weights.

| Weight | Record |
| --- | --- |
| 400 | available |

## Where it fits

- Longform reading: articles, documentation prose, books
- Editorial hierarchies where a serif voice signals depth
- Pairing with a sans for UI chrome around text-heavy screens

## Where it does not fit

- Tiny UI labels and dense table text where sans shapes stay clearer
- Interfaces that need a strictly neutral, invisible voice

## Alternatives in the same slot

Compared against the same classification and category in the data layer:

| Family | Classification | License | Variable |
| --- | --- | --- | --- |
| Abril Fatface | didone | OFL-1.1 | no |
| Bodoni Moda | didone | OFL-1.1 | yes |
| DM Serif Text | didone | OFL-1.1 | no |
| Playfair Display | didone | OFL-1.1 | yes |

## License notes

Released under the SIL Open Font License 1.1. The family may be used, studied, modified, embedded, and bundled in commercial and personal work. Selling the font files on their own is the only prohibited use. If a Reserved Font Name applies, modified versions must be renamed.

Always verify against the source page: https://fonts.google.com/specimen/DM+Serif+Display

## How to load it

- npm package: `@fontsource/dm-serif-display`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/dm-serif-display@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Requesting weights the family does not ship; browsers will synthesize bold or light and wreck the color.
- Serving every static weight when the page uses two; subset the list first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Abril Fatface overview](./abril-fatface-overview.md)
- [DM Serif Display implementation guide](./dm-serif-display-implementation.md)
- [DM Serif Display pairing playbook](./dm-serif-display-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
