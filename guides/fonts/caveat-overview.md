# Caveat: typeface overview

What this reference covers: Caveat as recorded in the Fontlore data layer: identity, classification, script coverage, technical profile, license, and where the family fits or does not fit.

## Identity

| Field | Value |
| --- | --- |
| Family | Caveat |
| Slug | caveat |
| Designer | not recorded in the data layer |
| Foundry | Impallari Type |
| License | OFL-1.1 |
| Category | handwriting |
| Classification | casual |
| Source | https://fonts.google.com/specimen/Caveat |

## Position in the taxonomy

The data layer files Caveat under handwriting with the casual classification. Tags: handwriting, casual, notes.

Data-layer note: casual pen handwriting that stays legible; annotations and friendly notes

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
| Indie Flower | casual | OFL-1.1 | no |
| Kalam | casual | OFL-1.1 | no |
| Patrick Hand | casual | OFL-1.1 | no |
| Shadows Into Light | casual | OFL-1.1 | no |

## License notes

Released under the SIL Open Font License 1.1. The family may be used, studied, modified, embedded, and bundled in commercial and personal work. Selling the font files on their own is the only prohibited use. If a Reserved Font Name applies, modified versions must be renamed.

Always verify against the source page: https://fonts.google.com/specimen/Caveat

## How to load it

- npm package: `@fontsource-variable/caveat`
- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/caveat@latest/index.css`
- Implementation details, axis usage, and fallback strategy: see the implementation guide below.

## Common mistakes

- Assuming every named instance in design tools exists as a web-safe CSS value; set axes explicitly.
- Loading the full variable file when only two weights are needed; check the size budget first.
- Treating this overview as license advice; the license text at the source URL is the authority.
- Skipping a real-copy test because the catalog preview looked right.

## Cross-references

- [Indie Flower overview](./indie-flower-overview.md)
- [Caveat implementation guide](./caveat-implementation.md)
- [Caveat pairing playbook](./caveat-pairing-playbook.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Open Font License reference](../../references/licensing/open-font-license.md)
Compiled 2025 as part of the Fontlore project.
