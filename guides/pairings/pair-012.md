# IBM Plex Serif + IBM Plex Sans: pairing guide

What this reference covers: the documented pairing of IBM Plex Serif for headings and IBM Plex Sans for body text: why it works, where it fits, how to implement it, and what to test before shipping.

## The pair at a glance

| Role | Family | Classification | License | Variable |
| --- | --- | --- | --- | --- |
| Heading | IBM Plex Serif | transitional | OFL-1.1 | no |
| Body | IBM Plex Sans | humanist | OFL-1.1 | no |

Pairing kind: `superfamily`. In practice, a designed serif and sans pair that share skeleton, metrics, and intent.

## Why this pair works

The Plex superfamily keeps documents and UI visually aligned.

The mechanism is complementary contrast: transitional headlines bring a different structure than the humanist body, while both agree on overall color and proportion enough to sit on one page without arguing.

## Where to use it

This pairing targets enterprise products where documents and UI must agree.

- Landing pages that need the headline voice to land in one glance.
- Content products where the body voice must survive thousands of words.
- Design systems that want a documented default before teams improvise.

## How to set it up

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/ibm-plex-serif@latest/index.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/ibm-plex-sans@latest/index.css">
```

```css
:root {
  --font-heading: 'IBM Plex Serif';
  --font-body: 'IBM Plex Sans';
}

h1, h2, h3 { font-family: var(--font-heading), serif; font-weight: 600; }
body { font-family: var(--font-body), sans-serif; font-size: 1rem; line-height: 1.6; }
```

Self-host both families in production and drop the CDN links; the snippet above is for quick evaluation only.

## Hierarchy suggestions

- Display: IBM Plex Serif at 40 to 72 px, tightened tracking above 1.2 ratios.
- Section heads: IBM Plex Serif at 24 to 32 px, or switch to IBM Plex Sans at 600 for dense UIs.
- Body: IBM Plex Sans at 15 to 17 px with 1.5 to 1.7 line height.
- Captions and metadata: the body family at 12 to 13 px, medium weight, muted color.
- Code and numerals in tables: add a monospace; this pair does not cover those roles.

## Alternatives with the same logic

| Pair | Context | Guide |
| --- | --- | --- |
| Alegreya + Alegreya Sans | humanist-editorial | [pair-013](./pair-013.md) |
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

- [IBM Plex Serif overview](../fonts/ibm-plex-serif-overview.md)
- [IBM Plex Sans overview](../fonts/ibm-plex-sans-overview.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Testing and comparing shortlists](../../references/workflow/testing-and-comparing-shortlists.md)
Compiled 2025 as part of the Fontlore project.
