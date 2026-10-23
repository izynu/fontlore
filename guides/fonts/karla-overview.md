# Karla: typeface overview

What this reference covers: Karla as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Karla |
| Slug | karla |
| Designer | Jonathan Ball |
| Foundry | not recorded in the data layer |
| License | OFL-1.1 |
| Category | sans-serif |
| Classification | grotesque |
| Source | https://fonts.google.com/specimen/Karla |

## Position in the taxonomy

The data layer files Karla under sans-serif with the grotesque classification. Tags: friendly, grotesque, brand.

Data-layer note: grotesque with personality in the details; a favorite for friendly-but-serious brands

## Script and subset coverage

| Script or subset | Record |
| --- | --- |
| latin | declared in the data layer |
| latin-ext | declared in the data layer |
| cyrillic | declared in the data layer |
| cyrillic-ext | declared in the data layer |
| vietnamese | declared in the data layer |

Coverage is recorded as declared by the upstream catalog. Before shipping a multilingual product, run the strings from the project through the family; see the cross-referenced testing guide at the end of this file.

## Technical profile

Variable build: yes. Declared axes: wght.

| Axis | What it controls |
| --- | --- |
| wght | weight from thin to black |

Static instances can be generated from the variable file, but prefer serving the variable build where the platform supports it.

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
| Archivo | grotesque | OFL-1.1 | yes |
| Archivo Black | grotesque | OFL-1.1 | no |
| Asap | grotesque | OFL-1.1 | yes |
| Barlow | grotesque | OFL-1.1 | yes |

## License notes

Released under the SIL Open Font License 1.1. The family may be used, studied, modified, embedded, and bundled in commercial and personal work. Selling the font files on their own is the only prohibited use. If a Reserved Font Name applies, modified versions must be renamed.

Always verify against the source page: https://fonts.google.com/specimen/Karla

## How to load it

- npm package: `@fontsource-variable/karla`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/karla@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Assuming every named instance in design tools exists as a web-safe CSS value; set axes explicitly.
- Loading the full variable file when only two weights are needed; check the size budget first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Archivo overview](./archivo-overview.md)
- [Karla implementation guide](./karla-implementation.md)
- [Karla pairing playbook](./karla-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
