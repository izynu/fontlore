# Alegreya + Alegreya Sans: pairing guide

What this reference covers: the documented pairing of Alegreya for headings and Alegreya Sans for body text: why it works, where it fits, how to implement it, and what to test before shipping.

## The pair at a glance

| Role | Family | Classification | License | Variable |
| --- | --- | --- | --- | --- |
| Heading | Alegreya | old-style | OFL-1.1 | yes |
| Body | Alegreya Sans | humanist | OFL-1.1 | yes |

Pairing kind: `superfamily`. In practice, a designed serif and sans pair that share skeleton, metrics, and intent.

## Why this pair works

A calligraphic serif with its designed sans companion; bookish and warm.

The mechanism is complementary contrast: old-style headlines bring a different structure than the humanist body, while both agree on overall color and proportion enough to sit on one page without arguing.

## Where to use it

This pairing targets publishing, essays, and warm editorial products.

- Landing pages that need the headline voice to land in one glance.
- Content products where the body voice must survive thousands of words.
- Design systems that want a documented default before teams improvise.

## How to set it up

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/alegreya@latest/index.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/alegreya-sans@latest/index.css">
```

```css
:root {
  --font-heading: 'Alegreya';
  --font-body: 'Alegreya Sans';
}

h1, h2, h3 { font-family: var(--font-heading), serif; font-weight: 600; }
body { font-family: var(--font-body), sans-serif; font-size: 1rem; line-height: 1.6; }
```

Self-host both families in production and drop the CDN links; the snippet above is for quick evaluation only.

## Hierarchy suggestions

- Display: Alegreya at 40 to 72 px, tightened tracking above 1.2 ratios.
- Section heads: Alegreya at 24 to 32 px, or switch to Alegreya Sans at 600 for dense UIs.
- Body: Alegreya Sans at 15 to 17 px with 1.5 to 1.7 line height.
- Captions and metadata: the body family at 12 to 13 px, medium weight, muted color.
- Code and numerals in tables: add a monospace; this pair does not cover those roles.

## Alternatives with the same logic

| Pair | Context | Guide |
| --- | --- | --- |
| IBM Plex Serif + IBM Plex Sans | enterprise-systems | [pair-012](./pair-012.md) |
| Red Hat Display + Red Hat Text | enterprise-family | [pair-045](./pair-045.md) |

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

- [Alegreya overview](../fonts/alegreya-overview.md)
- [Alegreya Sans overview](../fonts/alegreya-sans-overview.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Testing and comparing shortlists](../../references/workflow/testing-and-comparing-shortlists.md)
Compiled 2025 as part of the Fontlore project.
