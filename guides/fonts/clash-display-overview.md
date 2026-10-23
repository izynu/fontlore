# Clash Display: typeface overview

What this reference covers: Clash Display as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Clash Display |
| Slug | clash-display |
| Designer | not recorded in the data layer |
| Foundry | Indian Type Foundry |
| License | ITF-FFL-1.0 |
| Category | display |
| Classification | geometric |
| Source | https://www.fontshare.com/fonts/clash-display |

## Position in the taxonomy

The data layer files Clash Display under display with the geometric classification. Tags: fontshare, display, statement.

Data-layer note: Fontshare's statement display face; sharp apertures and tension

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
| Cairo | geometric | OFL-1.1 | yes |
| DM Sans | geometric | OFL-1.1 | yes |
| Epilogue | geometric | OFL-1.1 | yes |
| Figtree | geometric | OFL-1.1 | yes |

## License notes

Released under the Indian Type Foundry Free Font License. Free for personal and commercial use, including web embedding; redistribution of the raw font files as a standalone product is restricted. Read the license text shipped with the family before bundling.

Always verify against the source page: https://www.fontshare.com/fonts/clash-display

## How to load it

- npm package: `@fontsource-variable/clash-display`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/clash-display@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Assuming every named instance in design tools exists as a web-safe CSS value; set axes explicitly.
- Loading the full variable file when only two weights are needed; check the size budget first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Cairo overview](./cairo-overview.md)
- [Clash Display implementation guide](./clash-display-implementation.md)
- [Clash Display pairing playbook](./clash-display-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
