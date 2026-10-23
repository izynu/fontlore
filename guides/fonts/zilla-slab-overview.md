# Zilla Slab: typeface overview

What this reference covers: Zilla Slab as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Zilla Slab |
| Slug | zilla-slab |
| Designer | not recorded in the data layer |
| Foundry | Typotheque |
| License | OFL-1.1 |
| Category | serif |
| Classification | slab |
| Source | https://fonts.google.com/specimen/Zilla+Slab |

## Position in the taxonomy

The data layer files Zilla Slab under serif with the slab classification. Tags: mozilla, slab, editorial.

Data-layer note: Mozilla's brand slab; contemporary and tech-editorial

## Script and subset coverage

| Script or subset | Record |
| --- | --- |
| latin | declared in the data layer |
| latin-ext | declared in the data layer |
| cyrillic | declared in the data layer |

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
| Aleo | slab | OFL-1.1 | yes |
| Arvo | slab | OFL-1.1 | no |
| Besley | slab | ITF-FFL-1.0 | yes |
| Bitter | slab | OFL-1.1 | yes |

## License notes

Released under the SIL Open Font License 1.1. The family may be used, studied, modified, embedded, and bundled in commercial and personal work. Selling the font files on their own is the only prohibited use. If a Reserved Font Name applies, modified versions must be renamed.

Always verify against the source page: https://fonts.google.com/specimen/Zilla+Slab

## How to load it

- npm package: `@fontsource/zilla-slab`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/zilla-slab@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Requesting weights the family does not ship; browsers will synthesize bold or light and wreck the color.
- Serving every static weight when the page uses two; subset the list first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Aleo overview](./aleo-overview.md)
- [Zilla Slab implementation guide](./zilla-slab-implementation.md)
- [Zilla Slab pairing playbook](./zilla-slab-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
