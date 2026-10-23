# IBM Plex Sans Devanagari: typeface overview

What this reference covers: IBM Plex Sans Devanagari as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | IBM Plex Sans Devanagari |
| Slug | ibm-plex-sans-devanagari |
| Designer | not recorded in the data layer |
| Foundry | IBM |
| License | OFL-1.1 |
| Category | sans-serif |
| Classification | humanist |
| Source | https://fonts.google.com/specimen/IBM+Plex+Sans+Devanagari |

## Position in the taxonomy

The data layer files IBM Plex Sans Devanagari under sans-serif with the humanist classification. Tags: devanagari, enterprise, plex.

Data-layer note: Plex voice for Devanagari; matches Latin Plex metrics

## Script and subset coverage

| Script or subset | Record |
| --- | --- |
| devanagari | declared in the data layer |
| latin | declared in the data layer |
| latin-ext | declared in the data layer |

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
| Alegreya Sans | humanist | OFL-1.1 | yes |
| Assistant | humanist | OFL-1.1 | yes |
| Atkinson Hyperlegible | humanist | OFL-1.1 | no |
| Cabin | humanist | OFL-1.1 | yes |

## License notes

Released under the SIL Open Font License 1.1. The family may be used, studied, modified, embedded, and bundled in commercial and personal work. Selling the font files on their own is the only prohibited use. If a Reserved Font Name applies, modified versions must be renamed.

Always verify against the source page: https://fonts.google.com/specimen/IBM+Plex+Sans+Devanagari

## How to load it

- npm package: `@fontsource/ibm-plex-sans-devanagari`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/ibm-plex-sans-devanagari@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Requesting weights the family does not ship; browsers will synthesize bold or light and wreck the color.
- Serving every static weight when the page uses two; subset the list first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Alegreya Sans overview](./alegreya-sans-overview.md)
- [IBM Plex Sans Devanagari implementation guide](./ibm-plex-sans-devanagari-implementation.md)
- [IBM Plex Sans Devanagari pairing playbook](./ibm-plex-sans-devanagari-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
