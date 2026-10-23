# Switzer: typeface overview

What this reference covers: Switzer as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Switzer |
| Slug | switzer |
| Designer | not recorded in the data layer |
| Foundry | Indian Type Foundry |
| License | ITF-FFL-1.0 |
| Category | sans-serif |
| Classification | grotesque |
| Source | https://www.fontshare.com/fonts/switzer |

## Position in the taxonomy

The data layer files Switzer under sans-serif with the grotesque classification. Tags: fontshare, grotesque, helvetica-like.

Data-layer note: Helvetica-inspired grotesque from Fontshare

## Script and subset coverage

| Script or subset | Record |
| --- | --- |
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

Released under the Indian Type Foundry Free Font License. Free for personal and commercial use, including web embedding; redistribution of the raw font files as a standalone product is restricted. Read the license text shipped with the family before bundling.

Always verify against the source page: https://www.fontshare.com/fonts/switzer

## How to load it

- npm package: `@fontsource-variable/switzer`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/switzer@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Assuming every named instance in design tools exists as a web-safe CSS value; set axes explicitly.
- Loading the full variable file when only two weights are needed; check the size budget first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Archivo overview](./archivo-overview.md)
- [Switzer implementation guide](./switzer-implementation.md)
- [Switzer pairing playbook](./switzer-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
