# Prata: typeface overview

What this reference covers: Prata as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Prata |
| Slug | prata |
| Designer | not recorded in the data layer |
| Foundry | Cyreal |
| License | OFL-1.1 |
| Category | serif |
| Classification | didone |
| Source | https://fonts.google.com/specimen/Prata |

## Position in the taxonomy

The data layer files Prata under serif with the didone classification. Tags: didone, editorial, fashion.

Data-layer note: didone with old-style warmth; editorial fashion alternates

## Script and subset coverage

| Script or subset | Record |
| --- | --- |
| latin | declared in the data layer |
| latin-ext | declared in the data layer |
| cyrillic | declared in the data layer |
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
| DM Serif Display | didone | OFL-1.1 | no |
| DM Serif Text | didone | OFL-1.1 | no |

## License notes

Released under the SIL Open Font License 1.1. The family may be used, studied, modified, embedded, and bundled in commercial and personal work. Selling the font files on their own is the only prohibited use. If a Reserved Font Name applies, modified versions must be renamed.

Always verify against the source page: https://fonts.google.com/specimen/Prata

## How to load it

- npm package: `@fontsource/prata`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/prata@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Requesting weights the family does not ship; browsers will synthesize bold or light and wreck the color.
- Serving every static weight when the page uses two; subset the list first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Abril Fatface overview](./abril-fatface-overview.md)
- [Prata implementation guide](./prata-implementation.md)
- [Prata pairing playbook](./prata-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
