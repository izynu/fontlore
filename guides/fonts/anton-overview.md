# Anton: typeface overview

What this reference covers: Anton as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Anton |
| Slug | anton |
| Designer | Vernon Adams |
| Foundry | not recorded in the data layer |
| License | OFL-1.1 |
| Category | display |
| Classification | condensed |
| Source | https://fonts.google.com/specimen/Anton |

## Position in the taxonomy

The data layer files Anton under display with the condensed classification. Tags: heavy, condensed, loud.

Data-layer note: heavy condensed sans; loud headlines with minimal effort

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
| Barlow Condensed | condensed | OFL-1.1 | yes |
| Bebas Neue | condensed | OFL-1.1 | no |
| IBM Plex Sans Condensed | condensed | OFL-1.1 | no |
| Oswald | condensed | OFL-1.1 | yes |

## License notes

Released under the SIL Open Font License 1.1. The family may be used, studied, modified, embedded, and bundled in commercial and personal work. Selling the font files on their own is the only prohibited use. If a Reserved Font Name applies, modified versions must be renamed.

Always verify against the source page: https://fonts.google.com/specimen/Anton

## How to load it

- npm package: `@fontsource/anton`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/anton@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Requesting weights the family does not ship; browsers will synthesize bold or light and wreck the color.
- Serving every static weight when the page uses two; subset the list first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Barlow Condensed overview](./barlow-condensed-overview.md)
- [Anton implementation guide](./anton-implementation.md)
- [Anton pairing playbook](./anton-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
