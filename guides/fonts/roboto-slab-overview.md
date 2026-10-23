# Roboto Slab: typeface overview

What this reference covers: Roboto Slab as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Roboto Slab |
| Slug | roboto-slab |
| Designer | not recorded in the data layer |
| Foundry | Google |
| License | Apache-2.0 |
| Category | serif |
| Classification | slab |
| Source | https://fonts.google.com/specimen/Roboto+Slab |

## Position in the taxonomy

The data layer files Roboto Slab under serif with the slab classification. Tags: slab, documentation, product.

Data-layer note: slab companion to Roboto; documentation and product education default

## Script and subset coverage

| Script or subset | Record |
| --- | --- |
| latin | declared in the data layer |
| latin-ext | declared in the data layer |
| cyrillic | declared in the data layer |
| cyrillic-ext | declared in the data layer |
| greek | declared in the data layer |
| vietnamese | declared in the data layer |

Coverage is recorded as declared by the upstream catalog. Before shipping a multilingual product, run the strings from the project through the family; see the cross-referenced testing guide at the end of this file.

## Technical profile

Variable build: yes. Declared axes: wght.

| Axis | What it controls |
| --- | --- |
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
| Aleo | slab | OFL-1.1 | yes |
| Arvo | slab | OFL-1.1 | no |
| Besley | slab | ITF-FFL-1.0 | yes |
| Bitter | slab | OFL-1.1 | yes |

## License notes

Released under the Apache License 2.0. Use, redistribution, and modification are permitted in commercial and open-source projects; keep the license notice with any redistributed font files.

Always verify against the source page: https://fonts.google.com/specimen/Roboto+Slab

## How to load it

- npm package: `@fontsource-variable/roboto-slab`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/roboto-slab@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Assuming every named instance in design tools exists as a web-safe CSS value; set axes explicitly.
- Loading the full variable file when only two weights are needed; check the size budget first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Aleo overview](./aleo-overview.md)
- [Roboto Slab implementation guide](./roboto-slab-implementation.md)
- [Roboto Slab pairing playbook](./roboto-slab-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
