# Marcellus: typeface overview

What this reference covers: Marcellus as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Marcellus |
| Slug | marcellus |
| Designer | not recorded in the data layer |
| Foundry | not recorded in the data layer |
| License | OFL-1.1 |
| Category | serif |
| Classification | inscriptional |
| Source | https://fonts.google.com/specimen/Marcellus |

## Position in the taxonomy

The data layer files Marcellus under serif with the inscriptional classification. Tags: roman, inscriptional, luxury.

Data-layer note: flared Roman inscriptional caps; classical luxury accents

## Script and subset coverage

| Script or subset | Record |
| --- | --- |
| latin | declared in the data layer |
| latin-ext | declared in the data layer |

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
| Alegreya | old-style | OFL-1.1 | yes |
| Aleo | slab | OFL-1.1 | yes |
| Amiri | naskh | OFL-1.1 | no |
| Arvo | slab | OFL-1.1 | no |

## License notes

Released under the SIL Open Font License 1.1. The family may be used, studied, modified, embedded, and bundled in commercial and personal work. Selling the font files on their own is the only prohibited use. If a Reserved Font Name applies, modified versions must be renamed.

Always verify against the source page: https://fonts.google.com/specimen/Marcellus

## How to load it

- npm package: `@fontsource/marcellus`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/marcellus@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Requesting weights the family does not ship; browsers will synthesize bold or light and wreck the color.
- Serving every static weight when the page uses two; subset the list first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Alegreya overview](./alegreya-overview.md)
- [Marcellus implementation guide](./marcellus-implementation.md)
- [Marcellus pairing playbook](./marcellus-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
