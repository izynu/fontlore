# Permanent Marker: typeface overview

What this reference covers: Permanent Marker as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Permanent Marker |
| Slug | permanent-marker |
| Designer | not recorded in the data layer |
| Foundry | Font Diner |
| License | Apache-2.0 |
| Category | handwriting |
| Classification | marker |
| Source | https://fonts.google.com/specimen/Permanent+Marker |

## Position in the taxonomy

The data layer files Permanent Marker under handwriting with the marker classification. Tags: marker, attitude, announcements.

Data-layer note: marker-drawn display; announcements with attitude

## Script and subset coverage

| Script or subset | Record |
| --- | --- |
| latin | declared in the data layer |

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

Released under the Apache License 2.0. Use, redistribution, and modification are permitted in commercial and open-source projects; keep the license notice with any redistributed font files.

Always verify against the source page: https://fonts.google.com/specimen/Permanent+Marker

## How to load it

- npm package: `@fontsource/permanent-marker`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/permanent-marker@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Requesting weights the family does not ship; browsers will synthesize bold or light and wreck the color.
- Serving every static weight when the page uses two; subset the list first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Caveat overview](./caveat-overview.md)
- [Permanent Marker implementation guide](./permanent-marker-implementation.md)
- [Permanent Marker pairing playbook](./permanent-marker-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
