# IBM Plex Mono + IBM Plex Sans: pairing guide

What this reference covers: the documented pairing of IBM Plex Mono for headings and IBM Plex Sans for body text: why it works, where it fits, how to implement it, and what to test before shipping.

## The pair at a glance

| Role | Family | Classification | License | Variable |
| --- | --- | --- | --- | --- |
| Heading | IBM Plex Mono | mono | OFL-1.1 | no |
| Body | IBM Plex Sans | humanist | OFL-1.1 | no |

Pairing kind: `family-system`. In practice, both sides come from the same designed system, so weight and proportion agree by construction.

## Why this pair works

Engineering mono with the Plex sans for spec sheets and consoles.

The mechanism is complementary contrast: mono headlines bring a different structure than the humanist body, while both agree on overall color and proportion enough to sit on one page without arguing.

## Where to use it

This pairing targets engineering platforms, specs, and internal tools.

- Landing pages that need the headline voice to land in one glance.
- Content products where the body voice must survive thousands of words.
- Design systems that want a documented default before teams improvise.

## How to set it up

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/ibm-plex-mono@latest/index.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/ibm-plex-sans@latest/index.css">
```

```css
:root {
  --font-heading: 'IBM Plex Mono';
  --font-body: 'IBM Plex Sans';
}

h1, h2, h3 { font-family: var(--font-heading), serif; font-weight: 600; }
body { font-family: var(--font-body), sans-serif; font-size: 1rem; line-height: 1.6; }
```

Self-host both families in production and drop the CDN links; the snippet above is for quick evaluation only.

## Hierarchy suggestions

- Display: IBM Plex Mono at 40 to 72 px, tightened tracking above 1.2 ratios.
- Section heads: IBM Plex Mono at 24 to 32 px, or switch to IBM Plex Sans at 600 for dense UIs.
- Body: IBM Plex Sans at 15 to 17 px with 1.5 to 1.7 line height.
- Captions and metadata: the body family at 12 to 13 px, medium weight, muted color.
- Code and numerals in tables: add a monospace; this pair does not cover those roles.

## Alternatives with the same logic

| Pair | Context | Guide |
| --- | --- | --- |
| DM Serif Display + DM Sans | marketing-hero | [pair-004](./pair-004.md) |
| Space Mono + Space Grotesk | dev-tools | [pair-022](./pair-022.md) |
| Fira Code + Fira Sans | code-heavy-docs | [pair-024](./pair-024.md) |

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

- [IBM Plex Mono overview](../fonts/ibm-plex-mono-overview.md)
- [IBM Plex Sans overview](../fonts/ibm-plex-sans-overview.md)
- [Classification primer](../../references/selection/classification-primer.md)
- [Testing and comparing shortlists](../../references/workflow/testing-and-comparing-shortlists.md)
Compiled 2025 as part of the Fontlore project.
