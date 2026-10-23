# Halant + Mukta: pairing guide

What this reference covers: the documented pairing of Halant for headings and Mukta for body text: why it works, where it fits, how to implement it, and what to test before shipping.

## The pair at a glance

| Role | Family | Classification | License | Variable |
| --- | --- | --- | --- | --- |
| Heading | Halant | old-style | OFL-1.1 | no |
| Body | Mukta | humanist | OFL-1.1 | no |

Pairing kind: `devanagari-duet`. In practice, a Devanagari editorial display over a quiet UI humanist.

## Why this pair works

Book-quiet Devanagari serif over Ek Type's publishing humanist.

The mechanism is complementary contrast: old-style headlines bring a different structure than the humanist body, while both agree on overall color and proportion enough to sit on one page without arguing.

## Where to use it

This pairing targets Indian corporate and publishing products.

- Landing pages that need the headline voice to land in one glance.
- Content products where the body voice must survive thousands of words.
- Design systems that want a documented default before teams improvise.

## How to set it up

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/halant@latest/index.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/mukta@latest/index.css">
```

```css
:root {
  --font-heading: 'Halant';
  --font-body: 'Mukta';
}

h1, h2, h3 { font-family: var(--font-heading), serif; font-weight: 600; }
body { font-family: var(--font-body), sans-serif; font-size: 1rem; line-height: 1.6; }
```

Self-host both families in production and drop the CDN links; the snippet above is for quick evaluation only.

## Hierarchy suggestions

- Display: Halant at 40 to 72 px, tightened tracking above 1.2 ratios.
- Section heads: Halant at 24 to 32 px, or switch to Mukta at 600 for dense UIs.
- Body: Mukta at 15 to 17 px with 1.5 to 1.7 line height.
- Captions and metadata: the body family at 12 to 13 px, medium weight, muted color.
- Code and numerals in tables: add a monospace; this pair does not cover those roles.

## Alternatives with the same logic

| Pair | Context | Guide |
| --- | --- | --- |
| Eczar + Hind | devanagari-editorial | [pair-033](./pair-033.md) |

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

- [Halant overview](../fonts/halant-overview.md)
- [Mukta overview](../fonts/mukta-overview.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Testing and comparing shortlists](../../references/workflow/testing-and-comparing-shortlists.md)
Compiled 2025 as part of the Fontlore project.
