# IBM Plex Mono: pairing playbook

What this reference covers: how IBM Plex Mono behaves in a pairing: its documented partners in the data layer, the contrast rules that apply to its classification, and a testing workflow.

## Pairing temperament

A monospace signals code and data; it pairs with a proportional voice that handles prose.
Specifically, mono shapes: fixed advance widths; anything proportional around them benefits from shared x-height.

## Documented pairings in the data layer

| This family as | Partner | Context | Kind | Guide |
| --- | --- | --- | --- | --- |
| heading | IBM Plex Sans | engineering-platform | family-system | [pair-025](../pairings/pair-025.md) |

## Candidate partners from the same slot

| Family | Classification | Category | License |
| --- | --- | --- | --- |
| Azeret Mono | mono | monospace | OFL-1.1 |
| Courier Prime | mono | monospace | OFL-1.1 |
| Fira Code | mono | monospace | OFL-1.1 |
| Fira Mono | mono | monospace | OFL-1.1 |

## Contrast rules that apply here

- Contrast by role first: if IBM Plex Mono leads, the partner supports.
- Contrast by temperature second: pair a warm voice with a cooler one, not two of each.
- Contrast by structure last: x-height and width must agree even when style differs.
- Same-family systems skip these rules by design; use them when cohesion outranks expression.

## Testing workflow

1. Set the pair in the project's real headline and body copy, not lorem ipsum.
2. Test the smallest size the body will render at, typically 13 to 16 px.
3. Test numerals and mixed-script strings if either appears in the product.
4. Check hierarchy: can a reader separate heading, body, caption, and label without color?
5. Record the outcome in the project's type decision log with links to both license pages.

## Common mistakes

- Pairing two display voices because both looked good alone.
- Ignoring license compatibility: both families must cover the project's use scope.
- Matching by similarity instead of contrast; two middleweights blur into hierarchy soup.
- Skipping the small-size test where contrast and apertures actually fail.

## Cross-references

- [IBM Plex Sans overview](./ibm-plex-sans-overview.md)
- [IBM Plex Mono overview](./ibm-plex-mono-overview.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Choosing body typefaces](../../references/selection/choosing-body-typefaces.md)
Compiled 2025 as part of the Fontlore project.
