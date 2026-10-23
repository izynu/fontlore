# Roboto Mono: typeface overview

What this reference covers: Roboto Mono as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Roboto Mono |
| Slug | roboto-mono |
| Designer | not recorded in the data layer |
| Foundry | Google |
| License | Apache-2.0 |
| Category | monospace |
| Classification | mono |
| Source | https://fonts.google.com/specimen/Roboto+Mono |

## Position in the taxonomy

The data layer files Roboto Mono under monospace with the mono classification. Tags: neutral, code, data.

Data-layer note: Roboto's monospace; a safe neutral for code and data

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
| Fira Mono | mono | OFL-1.1 | no |

## License notes

Released under the Apache License 2.0. Use, redistribution, and modification are permitted in commercial and open-source projects; keep the license notice with any redistributed font files.

Always verify against the source page: https://fonts.google.com/specimen/Roboto+Mono

## How to load it

- npm package: `@fontsource-variable/roboto-mono`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/roboto-mono@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Assuming every named instance in design tools exists as a web-safe CSS value; set axes explicitly.
- Loading the full variable file when only two weights are needed; check the size budget first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Azeret Mono overview](./azeret-mono-overview.md)
- [Roboto Mono implementation guide](./roboto-mono-implementation.md)
- [Roboto Mono pairing playbook](./roboto-mono-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
