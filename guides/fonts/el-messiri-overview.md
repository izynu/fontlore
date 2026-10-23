# El Messiri: typeface overview

What this reference covers: El Messiri as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | El Messiri |
| Slug | el-messiri |
| Designer | Mohamed Gaber |
| Foundry | not recorded in the data layer |
| License | OFL-1.1 |
| Category | display |
| Classification | humanist |
| Source | https://fonts.google.com/specimen/El+Messiri |

## Position in the taxonomy

The data layer files El Messiri under display with the humanist classification. Tags: arabic, display, humanist.

Data-layer note: Arabic display with contemporary humanist details

## Script and subset coverage

| Script or subset | Record |
| --- | --- |
| arabic | declared in the data layer |
| latin | declared in the data layer |

Coverage is recorded as declared by the upstream catalog. Before shipping a multilingual product, run the strings from the project through the family; see the cross-referenced testing guide at the end of this file.

## Technical profile

Variable build: no. Serve static weights.

Specific weight list not recorded in the data layer; confirm on the source page.

## Where it fits

- Headlines, posters, and hero sections
- Short, high-impact strings rather than paragraphs
- Brand moments that need a distinct voice

## Where it does not fit

- Body text and small sizes: most display designs collapse below 20 px
- Data-dense layouts that need tabular figures

## Alternatives in the same slot

Compared against the same classification and category in the data layer:

| Family | Classification | License | Variable |
| --- | --- | --- | --- |
| Alegreya Sans | humanist | OFL-1.1 | yes |
| Assistant | humanist | OFL-1.1 | yes |
| Atkinson Hyperlegible | humanist | OFL-1.1 | no |
| Cabin | humanist | OFL-1.1 | yes |

## License notes

Released under the SIL Open Font License 1.1. The family may be used, studied, modified, embedded, and bundled in commercial and personal work. Selling the font files on their own is the only prohibited use. If a Reserved Font Name applies, modified versions must be renamed.

Always verify against the source page: https://fonts.google.com/specimen/El+Messiri

## How to load it

- npm package: `@fontsource/el-messiri`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/el-messiri@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Requesting weights the family does not ship; browsers will synthesize bold or light and wreck the color.
- Serving every static weight when the page uses two; subset the list first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Alegreya Sans overview](./alegreya-sans-overview.md)
- [El Messiri implementation guide](./el-messiri-implementation.md)
- [El Messiri pairing playbook](./el-messiri-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
