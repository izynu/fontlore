# Red Hat Display + Red Hat Text: pairing guide

What this reference covers: the documented pairing of Red Hat Display for headings and Red Hat Text for body text: why it works, where it fits, how to implement it, and what to test before shipping.

## The pair at a glance

| Role | Family | Classification | License | Variable |
| --- | --- | --- | --- | --- |
| Heading | Red Hat Display | humanist | OFL-1.1 | yes |
| Body | Red Hat Text | humanist | OFL-1.1 | yes |

Pairing kind: `superfamily`. In practice, a designed serif and sans pair that share skeleton, metrics, and intent.

## Why this pair works

One foundry's designed display/text split for enterprise systems.

The mechanism is complementary contrast: humanist headlines bring a different structure than the humanist body, while both agree on overall color and proportion enough to sit on one page without arguing.

## Where to use it

This pairing targets enterprise systems built on one family.

- Landing pages that need the headline voice to land in one glance.
- Content products where the body voice must survive thousands of words.
- Design systems that want a documented default before teams improvise.

## How to set it up

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/red-hat-display@latest/index.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/red-hat-text@latest/index.css">
```

```css
:root {
  --font-heading: 'Red Hat Display';
  --font-body: 'Red Hat Text';
}

h1, h2, h3 { font-family: var(--font-heading), serif; font-weight: 600; }
body { font-family: var(--font-body), sans-serif; font-size: 1rem; line-height: 1.6; }
```

Self-host both families in production and drop the CDN links; the snippet above is for quick evaluation only.

## Hierarchy suggestions

- Display: Red Hat Display at 40 to 72 px, tightened tracking above 1.2 ratios.
- Section heads: Red Hat Display at 24 to 32 px, or switch to Red Hat Text at 600 for dense UIs.
- Body: Red Hat Text at 15 to 17 px with 1.5 to 1.7 line height.
- Captions and metadata: the body family at 12 to 13 px, medium weight, muted color.
- Code and numerals in tables: add a monospace; this pair does not cover those roles.

## Alternatives with the same logic

| Pair | Context | Guide |
| --- | --- | --- |
| IBM Plex Serif + IBM Plex Sans | enterprise-systems | [pair-012](./pair-012.md) |
| Alegreya + Alegreya Sans | humanist-editorial | [pair-013](./pair-013.md) |

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

- [Red Hat Display overview](../fonts/red-hat-display-overview.md)
- [Red Hat Text overview](../fonts/red-hat-text-overview.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Testing and comparing shortlists](../../references/workflow/testing-and-comparing-shortlists.md)
Compiled 2025 as part of the Fontlore project.
