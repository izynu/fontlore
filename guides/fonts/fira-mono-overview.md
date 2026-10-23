# Fira Mono: typeface overview

What this reference covers: Fira Mono as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Fira Mono |
| Slug | fira-mono |
| Designer | not recorded in the data layer |
| Foundry | Mozilla |
| License | OFL-1.1 |
| Category | monospace |
| Classification | mono |
| Source | https://fonts.google.com/specimen/Fira+Mono |

## Position in the taxonomy

The data layer files Fira Mono under monospace with the mono classification. Tags: code, mozilla, plain.

Data-layer note: Fira Sans's monospace sibling without ligatures

## Script and subset coverage

| Script or subset | Record |
| --- | --- |
| latin | declared in the data layer |
| latin-ext | declared in the data layer |
| cyrillic | declared in the data layer |
| greek | declared in the data layer |

Coverage is recorded as declared by the upstream catalog. Before shipping a multilingual product, run the strings from the project through the family; see the cross-referenced testing guide at the end of this file.

## Technical profile

Variable build: no. Serve static weights.

| Weight | Record |
| --- | --- |
| 400 | available |
| 700 | available |

## Where it fits

- Code blocks, terminals, and technical documentation
- Tabular data where fixed advance widths keep columns aligned
- Metadata, timestamps, and identifiers

## Where it does not fit

- Longform prose: fixed widths slow reading
- Marketing headlines unless the brief calls for a technical voice

## Alternatives in the same slot

Compared against the same classification and category in the data layer:

| Family | Classification | License | Variable |
| --- | --- | --- | --- |
| Azeret Mono | mono | OFL-1.1 | yes |
| Courier Prime | mono | OFL-1.1 | no |
| Fira Code | mono | OFL-1.1 | yes |
| Fragment Mono | mono | OFL-1.1 | no |

## License notes

Released under the SIL Open Font License 1.1. The family may be used, studied, modified, embedded, and bundled in commercial and personal work. Selling the font files on their own is the only prohibited use. If a Reserved Font Name applies, modified versions must be renamed.

Always verify against the source page: https://fonts.google.com/specimen/Fira+Mono

## How to load it

- npm package: `@fontsource/fira-mono`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/fira-mono@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Requesting weights the family does not ship; browsers will synthesize bold or light and wreck the color.
- Serving every static weight when the page uses two; subset the list first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Azeret Mono overview](./azeret-mono-overview.md)
- [Fira Mono implementation guide](./fira-mono-implementation.md)
- [Fira Mono pairing playbook](./fira-mono-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
