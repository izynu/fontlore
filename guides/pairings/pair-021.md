# Exo 2 + Titillium Web: pairing guide

What this reference covers: the documented pairing of Exo 2 for headings and Titillium Web for body text: why it works, where it fits, how to implement it, and what to test before shipping.

## The pair at a glance

| Role | Family | Classification | License | Variable |
| --- | --- | --- | --- | --- |
| Heading | Exo 2 | techno | OFL-1.1 | yes |
| Body | Titillium Web | humanist | OFL-1.1 | no |

Pairing kind: `techno-duet`. In practice, two technical voices balanced so the page reads engineered, not gimmicky.

## Why this pair works

Two techno voices in balance: angular display, technical body.

The mechanism is complementary contrast: techno headlines bring a different structure than the humanist body, while both agree on overall color and proportion enough to sit on one page without arguing.

## Where to use it

This pairing targets techno products and speculative brands.

- Landing pages that need the headline voice to land in one glance.
- Content products where the body voice must survive thousands of words.
- Design systems that want a documented default before teams improvise.

## How to set it up

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/exo-2@latest/index.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/titillium-web@latest/index.css">
```

```css
:root {
  --font-heading: 'Exo 2';
  --font-body: 'Titillium Web';
}

h1, h2, h3 { font-family: var(--font-heading), serif; font-weight: 600; }
body { font-family: var(--font-body), sans-serif; font-size: 1rem; line-height: 1.6; }
```

Self-host both families in production and drop the CDN links; the snippet above is for quick evaluation only.

## Hierarchy suggestions

- Display: Exo 2 at 40 to 72 px, tightened tracking above 1.2 ratios.
- Section heads: Exo 2 at 24 to 32 px, or switch to Titillium Web at 600 for dense UIs.
- Body: Titillium Web at 15 to 17 px with 1.5 to 1.7 line height.
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

- [Exo 2 overview](../fonts/exo-2-overview.md)
- [Titillium Web overview](../fonts/titillium-web-overview.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Testing and comparing shortlists](../../references/workflow/testing-and-comparing-shortlists.md)
Compiled 2025 as part of the Fontlore project.
