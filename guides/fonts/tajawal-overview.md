# Tajawal: typeface overview

What this reference covers: Tajawal as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Tajawal |
| Slug | tajawal |
| Designer | not recorded in the data layer |
| Foundry | Boutros |
| License | OFL-1.1 |
| Category | sans-serif |
| Classification | geometric |
| Source | https://fonts.google.com/specimen/Tajawal |

## Position in the taxonomy

The data layer files Tajawal under sans-serif with the geometric classification. Tags: arabic, geometric, gulf.

Data-layer note: geometric Arabic + Latin with even color; modern Gulf brand voice

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
| Cairo | geometric | OFL-1.1 | yes |
| Clash Display | geometric | ITF-FFL-1.0 | yes |
| DM Sans | geometric | OFL-1.1 | yes |
| Epilogue | geometric | OFL-1.1 | yes |

## License notes

Released under the SIL Open Font License 1.1. The family may be used, studied, modified, embedded, and bundled in commercial and personal work. Selling the font files on their own is the only prohibited use. If a Reserved Font Name applies, modified versions must be renamed.

Always verify against the source page: https://fonts.google.com/specimen/Tajawal

## How to load it

- npm package: `@fontsource/tajawal`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/tajawal@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Requesting weights the family does not ship; browsers will synthesize bold or light and wreck the color.
- Serving every static weight when the page uses two; subset the list first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Cairo overview](./cairo-overview.md)
- [Tajawal implementation guide](./tajawal-implementation.md)
- [Tajawal pairing playbook](./tajawal-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
