# Zodiak: typeface overview

What this reference covers: Zodiak as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Zodiak |
| Slug | zodiak |
| Designer | not recorded in the data layer |
| Foundry | Indian Type Foundry |
| License | ITF-FFL-1.0 |
| Category | serif |
| Classification | didone |
| Source | https://www.fontshare.com/fonts/zodiak |

## Position in the taxonomy

The data layer files Zodiak under serif with the didone classification. Tags: fontshare, didone, editorial.

Data-layer note: Fontshare's fat didone for editorial display

## Script and subset coverage

| Script or subset | Record |
| --- | --- |
| latin | declared in the data layer |
| latin-ext | declared in the data layer |

Coverage is recorded as declared by the upstream catalog. Before shipping a multilingual product, run the strings from the project through the family; see the cross-referenced testing guide at the end of this file.

## Technical profile

Variable build: no. Serve static weights.

Specific weight list not recorded in the data layer; confirm on the source page.

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

Released under the Indian Type Foundry Free Font License. Free for personal and commercial use, including web embedding; redistribution of the raw font files as a standalone product is restricted. Read the license text shipped with the family before bundling.

Always verify against the source page: https://www.fontshare.com/fonts/zodiak

## How to load it

- npm package: `@fontsource/zodiak`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/zodiak@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Requesting weights the family does not ship; browsers will synthesize bold or light and wreck the color.
- Serving every static weight when the page uses two; subset the list first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Abril Fatface overview](./abril-fatface-overview.md)
- [Zodiak implementation guide](./zodiak-implementation.md)
- [Zodiak pairing playbook](./zodiak-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
