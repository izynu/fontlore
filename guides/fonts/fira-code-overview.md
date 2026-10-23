# Fira Code: typeface overview

What this reference covers: Fira Code as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Fira Code |
| Slug | fira-code |
| Designer | Nikita Prokopov |
| Foundry | not recorded in the data layer |
| License | OFL-1.1 |
| Category | monospace |
| Classification | mono |
| Source | https://fonts.google.com/specimen/Fira+Code |

## Position in the taxonomy

The data layer files Fira Code under monospace with the mono classification. Tags: code, ligatures, pioneer.

Data-layer note: the ligature pioneer; widely loved for symbol-rich code

## Script and subset coverage

| Script or subset | Record |
| --- | --- |
| latin | declared in the data layer |
| latin-ext | declared in the data layer |
| cyrillic | declared in the data layer |
| greek | declared in the data layer |

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
| Fira Mono | mono | OFL-1.1 | no |
| Fragment Mono | mono | OFL-1.1 | no |

## License notes

Released under the SIL Open Font License 1.1. The family may be used, studied, modified, embedded, and bundled in commercial and personal work. Selling the font files on their own is the only prohibited use. If a Reserved Font Name applies, modified versions must be renamed.

Always verify against the source page: https://fonts.google.com/specimen/Fira+Code

## How to load it

- npm package: `@fontsource-variable/fira-code`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/fira-code@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Assuming every named instance in design tools exists as a web-safe CSS value; set axes explicitly.
- Loading the full variable file when only two weights are needed; check the size budget first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Azeret Mono overview](./azeret-mono-overview.md)
- [Fira Code implementation guide](./fira-code-implementation.md)
- [Fira Code pairing playbook](./fira-code-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
