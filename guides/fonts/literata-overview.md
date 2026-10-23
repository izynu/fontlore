# Literata: typeface overview

What this reference covers: Literata as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Literata |
| Slug | literata |
| Designer | not recorded in the data layer |
| Foundry | TypeTogether |
| License | OFL-1.1 |
| Category | serif |
| Classification | transitional |
| Source | https://fonts.google.com/specimen/Literata |

## Position in the taxonomy

The data layer files Literata under serif with the transitional classification. Tags: ebook, reading, google.

Data-layer note: Google Play Books default; a reading-optimized serif with personality

## Script and subset coverage

| Script or subset | Record |
| --- | --- |
| latin | declared in the data layer |
| latin-ext | declared in the data layer |
| cyrillic | declared in the data layer |
| greek | declared in the data layer |
| vietnamese | declared in the data layer |

Coverage is recorded as declared by the upstream catalog. Before shipping a multilingual product, run the strings from the project through the family; see the cross-referenced testing guide at the end of this file.

## Technical profile

Variable build: yes. Declared axes: opsz, wght.

| Axis | What it controls |
| --- | --- |
| opsz | optical size; detail tuning from small text to display |
| wght | weight from thin to black |

Static instances can be generated from the variable file, but prefer serving the variable build where the platform supports it.

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
| Charis SIL | transitional | OFL-1.1 | no |
| Eczar | transitional | OFL-1.1 | yes |
| Frank Ruhl Libre | transitional | OFL-1.1 | yes |
| IBM Plex Serif | transitional | OFL-1.1 | no |

## License notes

Released under the SIL Open Font License 1.1. The family may be used, studied, modified, embedded, and bundled in commercial and personal work. Selling the font files on their own is the only prohibited use. If a Reserved Font Name applies, modified versions must be renamed.

Always verify against the source page: https://fonts.google.com/specimen/Literata

## How to load it

- npm package: `@fontsource-variable/literata`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/literata@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Assuming every named instance in design tools exists as a web-safe CSS value; set axes explicitly.
- Loading the full variable file when only two weights are needed; check the size budget first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Charis SIL overview](./charis-sil-overview.md)
- [Literata implementation guide](./literata-implementation.md)
- [Literata pairing playbook](./literata-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
