# Eczar + Hind: pairing guide

What this reference covers: the documented pairing of Eczar for headings and Hind for body text: why it works, where it fits, how to implement it, and what to test before shipping.

## The pair at a glance

| Role | Family | Classification | License | Variable |
| --- | --- | --- | --- | --- |
| Heading | Eczar | transitional | OFL-1.1 | yes |
| Body | Hind | humanist | OFL-1.1 | no |

Pairing kind: `devanagari-duet`. In practice, a Devanagari editorial display over a quiet UI humanist.

## Why this pair works

Sharp Devanagari editorial display over ITF's quiet UI humanist.

The mechanism is complementary contrast: transitional headlines bring a different structure than the humanist body, while both agree on overall color and proportion enough to sit on one page without arguing.

## Where to use it

This pairing targets Hindi-first editorial and advocacy.

- Landing pages that need the headline voice to land in one glance.
- Content products where the body voice must survive thousands of words.
- Design systems that want a documented default before teams improvise.

## How to set it up

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/eczar@latest/index.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/hind@latest/index.css">
```

```css
:root {
  --font-heading: 'Eczar';
  --font-body: 'Hind';
}

h1, h2, h3 { font-family: var(--font-heading), serif; font-weight: 600; }
body { font-family: var(--font-body), sans-serif; font-size: 1rem; line-height: 1.6; }
```

Self-host both families in production and drop the CDN links; the snippet above is for quick evaluation only.

## Hierarchy suggestions

- Display: Eczar at 40 to 72 px, tightened tracking above 1.2 ratios.
- Section heads: Eczar at 24 to 32 px, or switch to Hind at 600 for dense UIs.
- Body: Hind at 15 to 17 px with 1.5 to 1.7 line height.
- Captions and metadata: the body family at 12 to 13 px, medium weight, muted color.
- Code and numerals in tables: add a monospace; this pair does not cover those roles.

## Alternatives with the same logic

| Pair | Context | Guide |
| --- | --- | --- |
| Halant + Mukta | devanagari-corporate | [pair-034](./pair-034.md) |

## Testing checklist

- [ ] Real headline copy at final sizes; check the heading voice does not collapse.
- [ ] Real body copy for three paragraphs minimum; no rhythmic snags.
- [ ] Numerals in both faces match the product's needs (tabular vs proportional).
- [ ] Both licenses cover the project scope; record URLs in the decision log.
- [ ] Fallback stacks chosen per role so a slow load never swaps both faces at once.

## Common mistakes

- Letting the heading face appear in running text; contrast faces tire fast at small sizes.
- Matching weights instead of roles: 700 heading vs 400 body beats 600 vs 500 every time.
- Forgetting the caption style, which silently becomes the third voice on the page.

## Cross-references

- [Eczar overview](../fonts/eczar-overview.md)
- [Hind overview](../fonts/hind-overview.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Testing and comparing shortlists](../../references/workflow/testing-and-comparing-shortlists.md)
Compiled 2025 as part of the Fontlore project.
