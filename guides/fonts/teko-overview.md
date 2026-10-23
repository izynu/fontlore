# Teko: typeface overview

What this reference covers: Teko as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Teko |
| Slug | teko |
| Designer | not recorded in the data layer |
| Foundry | Indian Type Foundry |
| License | OFL-1.1 |
| Category | display |
| Classification | condensed |
| Source | https://www.fontshare.com/fonts/teko |

## Position in the taxonomy

The data layer files Teko under display with the condensed classification. Tags: devanagari, condensed, scores.

Data-layer note: Devanagari + Latin condensed for scores and tickers

## Script and subset coverage

| Script or subset | Record |
| --- | --- |
| devanagari | declared in the data layer |
| latin | declared in the data layer |
| latin-ext | declared in the data layer |

Coverage is recorded as declared by the upstream catalog. Before shipping a multilingual product, run the strings from the project through the family; see the cross-referenced testing guide at the end of this file.

## Technical profile

Variable build: yes. Declared axes: wght.

| Axis | What it controls |
| --- | --- |
| wght | weight from thin to black |

Static instances can be generated from the variable file, but prefer serving the variable build where the platform supports it.

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
| Anton | condensed | OFL-1.1 | no |
| Barlow Condensed | condensed | OFL-1.1 | yes |
| Bebas Neue | condensed | OFL-1.1 | no |
| IBM Plex Sans Condensed | condensed | OFL-1.1 | no |

## License notes

Released under the SIL Open Font License 1.1. The family may be used, studied, modified, embedded, and bundled in commercial and personal work. Selling the font files on their own is the only prohibited use. If a Reserved Font Name applies, modified versions must be renamed.

Always verify against the source page: https://www.fontshare.com/fonts/teko

## How to load it

- npm package: `@fontsource-variable/teko`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/teko@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Assuming every named instance in design tools exists as a web-safe CSS value; set axes explicitly.
- Loading the full variable file when only two weights are needed; check the size budget first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Anton overview](./anton-overview.md)
- [Teko implementation guide](./teko-implementation.md)
- [Teko pairing playbook](./teko-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
