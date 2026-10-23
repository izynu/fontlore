# Varela Round: typeface overview

What this reference covers: Varela Round as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Varela Round |
| Slug | varela-round |
| Designer | Joe Prince |
| Foundry | not recorded in the data layer |
| License | OFL-1.1 |
| Category | sans-serif |
| Classification | rounded |
| Source | https://fonts.google.com/specimen/Varela+Round |

## Position in the taxonomy

The data layer files Varela Round under sans-serif with the rounded classification. Tags: rounded, hebrew, single-weight.

Data-layer note: single-weight rounded classic; also covers Hebrew

## Script and subset coverage

| Script or subset | Record |
| --- | --- |
| latin | declared in the data layer |
| latin-ext | declared in the data layer |
| hebrew | declared in the data layer |

Coverage is recorded as declared by the upstream catalog. Before shipping a multilingual product, run the strings from the project through the family; see the cross-referenced testing guide at the end of this file.

## Technical profile

Variable build: no. Serve static weights.

Specific weight list not recorded in the data layer; confirm on the source page.

## Where it fits

- Interface text, navigation, and form controls
- Dashboards and dense data layouts when paired with tabular figures
- Marketing headlines at larger sizes for geometric and grotesque voices

## Where it does not fit

- Long literary body text where an old-style serif reads more comfortably
- Display contexts that need strong contrast or personality

## Alternatives in the same slot

Compared against the same classification and category in the data layer:

| Family | Classification | License | Variable |
| --- | --- | --- | --- |
| Baloo 2 | rounded | OFL-1.1 | yes |
| Comfortaa | rounded | OFL-1.1 | yes |
| Modak | rounded | OFL-1.1 | no |
| Nunito | rounded | OFL-1.1 | yes |

## License notes

Released under the SIL Open Font License 1.1. The family may be used, studied, modified, embedded, and bundled in commercial and personal work. Selling the font files on their own is the only prohibited use. If a Reserved Font Name applies, modified versions must be renamed.

Always verify against the source page: https://fonts.google.com/specimen/Varela+Round

## How to load it

- npm package: `@fontsource/varela-round`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/varela-round@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Requesting weights the family does not ship; browsers will synthesize bold or light and wreck the color.
- Serving every static weight when the page uses two; subset the list first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Baloo 2 overview](./baloo-2-overview.md)
- [Varela Round implementation guide](./varela-round-implementation.md)
- [Varela Round pairing playbook](./varela-round-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
