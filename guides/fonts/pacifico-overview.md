# Pacifico: typeface overview

What this reference covers: Pacifico as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Pacifico |
| Slug | pacifico |
| Designer | Vernon Adams |
| Foundry | not recorded in the data layer |
| License | OFL-1.1 |
| Category | handwriting |
| Classification | brush |
| Source | https://fonts.google.com/specimen/Pacifico |

## Position in the taxonomy

The data layer files Pacifico under handwriting with the brush classification. Tags: brush, surf, food.

Data-layer note: brush script with surf-shop charm; food and leisure brands

## Script and subset coverage

| Script or subset | Record |
| --- | --- |
| latin | declared in the data layer |
| latin-ext | declared in the data layer |
| cyrillic | declared in the data layer |
| vietnamese | declared in the data layer |

Coverage is recorded as declared by the upstream catalog. Before shipping a multilingual product, run the strings from the project through the family; see the cross-referenced testing guide at the end of this file.

## Technical profile

Variable build: no. Serve static weights.

| Weight | Record |
| --- | --- |
| 400 | available |

## Where it fits

- Accents, annotations, and short personal touches
- Greeting surfaces and celebration states
- Never for body text or critical UI labels

## Where it does not fit

- Anything users must read quickly or at small sizes
- Accessibility-critical text of any kind

## Alternatives in the same slot

Compared against the same classification and category in the data layer:

| Family | Classification | License | Variable |
| --- | --- | --- | --- |
| Caveat | casual | OFL-1.1 | yes |
| Dancing Script | script | OFL-1.1 | yes |
| Great Vibes | script | OFL-1.1 | no |
| Indie Flower | casual | OFL-1.1 | no |

## License notes

Released under the SIL Open Font License 1.1. The family may be used, studied, modified, embedded, and bundled in commercial and personal work. Selling the font files on their own is the only prohibited use. If a Reserved Font Name applies, modified versions must be renamed.

Always verify against the source page: https://fonts.google.com/specimen/Pacifico

## How to load it

- npm package: `@fontsource/pacifico`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/pacifico@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Requesting weights the family does not ship; browsers will synthesize bold or light and wreck the color.
- Serving every static weight when the page uses two; subset the list first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Caveat overview](./caveat-overview.md)
- [Pacifico implementation guide](./pacifico-implementation.md)
- [Pacifico pairing playbook](./pacifico-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
