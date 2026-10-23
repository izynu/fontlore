# Besley: typeface overview

What this reference covers: Besley as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Besley |
| Slug | besley |
| Designer | not recorded in the data layer |
| Foundry | Indian Type Foundry |
| License | ITF-FFL-1.0 |
| Category | serif |
| Classification | slab |
| Source | https://www.fontshare.com/fonts/besley |

## Position in the taxonomy

The data layer files Besley under serif with the slab classification. Tags: fontshare, slab, clarendon.

Data-layer note: Fontshare's Clarendon-flavored slab

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
| Bitter | slab | OFL-1.1 | yes |
| Roboto Slab | slab | Apache-2.0 | yes |

## License notes

Released under the Indian Type Foundry Free Font License. Free for personal and commercial use, including web embedding; redistribution of the raw font files as a standalone product is restricted. Read the license text shipped with the family before bundling.

Always verify against the source page: https://www.fontshare.com/fonts/besley

## How to load it

- npm package: `@fontsource-variable/besley`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/besley@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Assuming every named instance in design tools exists as a web-safe CSS value; set axes explicitly.
- Loading the full variable file when only two weights are needed; check the size budget first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Aleo overview](./aleo-overview.md)
- [Besley implementation guide](./besley-implementation.md)
- [Besley pairing playbook](./besley-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
