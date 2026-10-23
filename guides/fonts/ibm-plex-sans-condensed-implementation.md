# IBM Plex Sans Condensed: implementation guide

What this reference covers: shipping IBM Plex Sans Condensed on the web: install paths, CSS setup, variable axis usage, font-display strategy, fallbacks, and a pre-launch checklist.

## Install paths

- npm: `npm install @fontsource/ibm-plex-sans-condensed`
- Import per weight: `import '@fontsource/ibm-plex-sans-condensed/400.css';`

CDN stylesheet, no install:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/ibm-plex-sans-condensed@latest/index.css">
```

Self-hosting beats the CDN for production: it removes a third-party dependency, lets you control cache headers, and keeps font bytes on your own domain.

## CSS setup

```css
:root {
  --font-brand: 'IBM Plex Sans Condensed';
  --font-brand-fallback: system-ui, -apple-system, 'Segoe UI', sans-serif;
}

.brand-type { font-family: var(--font-brand), var(--font-brand-fallback); }
```

## Weight and axis strategy

IBM Plex Sans Condensed serves static weights. Recorded available weights: 400, 700.

```css
/* request exactly the weights the family ships */
.weight-400 { font-weight: 400; }
.weight-700 { font-weight: 700; }
```

If a design calls for a weight between two statics, choose the nearest available weight deliberately; browsers synthesize the rest and the fake weights are always worse than the honest nearest neighbor.

## font-display strategy

- Body text: `font-display: swap` keeps content readable during load at the cost of a brief fallback flash.
- Display headlines: `swap` is usually acceptable; `optional` suits cases where layout stability outranks brand type on first paint.
- Avoid `block` for anything above the fold; invisible text is the worst outcome for readers.

## Subset and performance notes

Declared subsets: latin, latin-ext, vietnamese. Load only the subsets the page actually renders; the Fontsource packages and the Google Fonts CSS API split coverage with unicode-range so browsers fetch what they need.

Budget guidance: audit the network tab after wiring the family up. If the font payload exceeds roughly 100 KB for a Latin-only page, question whether every requested weight earns its bytes.

## Fallback strategy

The recommended fallback stack above picks system faces that share the sans-serif category, so the swap flash changes letterforms but not layout category. For tighter control, measure the fallback with size-adjust and ascent-override rather than eyeballing it.

## Pre-launch checklist

- [ ] Weights requested match weights shipped; no synthetic bold in the UI.
- [ ] font-display chosen deliberately for body and display roles.
- [ ] Only needed subsets load; network tab audited.
- [ ] Fallback stack renders the page without layout shift during swap.
- [ ] License verified at the source page for the current project scope.
- [ ] Real copy tested at real sizes, including numerals and punctuation.

## Common mistakes

- Importing the whole package when one stylesheet would do; tree shaking does not apply to CSS.
- Hard-coding px everywhere and losing the variable optical sizing benefit.
- Forgetting `font-optical-sizing: auto` on optical-size families, which pins the wrong optical cut.
- Shipping the CDN stylesheet in production and eating the third-party request.

## Cross-references

- [IBM Plex Sans Condensed overview](./ibm-plex-sans-condensed-overview.md)
- [@font-face and CSS reference](../../references/technical/font-face-and-css.md)
- [font-display strategies](../../references/technical/font-display-strategies.md)
- [Fallback metrics and CLS](../../references/technical/fallback-metrics-and-cls.md)
Compiled 2025 as part of the Fontlore project.
