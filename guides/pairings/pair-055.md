# Playfair Display + Lora: pairing guide

What this reference covers: the documented pairing of Playfair Display for headings and Lora for body text: why it works, where it fits, how to implement it, and what to test before shipping.

## The pair at a glance

| Role | Family | Classification | License | Variable |
| --- | --- | --- | --- | --- |
| Heading | Playfair Display | didone | OFL-1.1 | yes |
| Body | Lora | transitional | OFL-1.1 | yes |

Pairing kind: `serif-duet`. In practice, two serifs at different temperatures, tuned to agree.

## Why this pair works

Didone headlines with a contemporary transitional body; two serifs in tune.

The mechanism is complementary contrast: didone headlines bring a different structure than the transitional body, while both agree on overall color and proportion enough to sit on one page without arguing.

## Where to use it

This pairing targets all-serif editorial systems.

- Landing pages that need the headline voice to land in one glance.
- Content products where the body voice must survive thousands of words.
- Design systems that want a documented default before teams improvise.

## How to set it up

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/playfair-display@latest/index.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/lora@latest/index.css">
```

```css
:root {
  --font-heading: 'Playfair Display';
  --font-body: 'Lora';
}

h1, h2, h3 { font-family: var(--font-heading), serif; font-weight: 600; }
body { font-family: var(--font-body), sans-serif; font-size: 1rem; line-height: 1.6; }
```

Self-host both families in production and drop the CDN links; the snippet above is for quick evaluation only.

## Hierarchy suggestions

- Display: Playfair Display at 40 to 72 px, tightened tracking above 1.2 ratios.
- Section heads: Playfair Display at 24 to 32 px, or switch to Lora at 600 for dense UIs.
- Body: Lora at 15 to 17 px with 1.5 to 1.7 line height.
- Captions and metadata: the body family at 12 to 13 px, medium weight, muted color.
- Code and numerals in tables: add a monospace; this pair does not cover those roles.

## Alternatives with the same logic

No other pairing in the data layer shares this exact logic; browse the pairings tab of the library for adjacent kinds.

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

- [Playfair Display overview](../fonts/playfair-display-overview.md)
- [Lora overview](../fonts/lora-overview.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Testing and comparing shortlists](../../references/workflow/testing-and-comparing-shortlists.md)
Compiled 2025 as part of the Fontlore project.
