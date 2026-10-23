# Design Tokens for Type

What this reference covers: Turning a type system into design tokens: family, size, weight, line-height, and tracking tokens; primitive versus semantic layers; responsive and multi-brand variations; syncing with CSS variables and Tailwind; and versioning tokens without breaking consumers. The goal is a type system that survives redesigns, theming, and handoffs because the decisions live in named tokens, not in scattered CSS.

## Primitive and semantic layers

- Primitive tokens are the raw facts: font families, a size scale, weight values, line-height values. They are named by position or scale step (size-300), never by role.
- Semantic tokens are the roles: heading, body, data, caption, code. Each resolves to primitives and is the only layer components consume.
- Components reference semantic tokens only. When the brand swaps its serif, no component CSS changes; one primitive behind the heading token changes.
- Keep the mapping one-directional: semantic references primitive, never the reverse. Circular or reverse references make themes impossible to reason about.
- This layering is the same idea as the constraint sheet in selection work: decisions recorded once, consumed everywhere.

## Family tokens

- One token per family in the system: family-sans, family-serif, family-mono. The value is the full CSS stack, including metrics-sensible fallbacks.
- Put generic keywords last in every stack (sans-serif, serif, monospace) so unknown environments still land in the right classification.
- Do not create family tokens per weight (font-sans-bold); weight is its own dimension and multiplying family tokens by weight creates a matrix you cannot maintain.
- For multi-script systems, token the script order too: a hindi-body token whose value is a stack ordering Devanagari coverage first, so locale differences are a token swap, not a CSS hunt.

## Size scale tokens (rem-based)

- Build the scale in rem so user font-size preferences scale the whole system; the browser default of 16px is the reference, not a value to hard-code.
- Use a small named set of steps rather than arbitrary values: 0.75, 0.875, 1, 1.125, 1.25, 1.5625, 2, 2.5, 3.25rem is a workable product scale (12 through 52px at default root size).
- Name steps by number (size-100 through size-800), not by use; "size-small" breaks the moment small changes meaning.
- Constrain consumers to the scale: if a component needs 1.4rem, the scale is missing a step, and the fix is a token, not an exception.
- Keep step ratios deliberate: a 1.2-1.25 ratio suits dense product UI; a 1.333 ratio suits editorial scale. The scale encodes the typographic voice as much as the family does.

## Weight tokens

- One token per weight actually used, named for the weight: weight-regular (400), weight-medium (500), weight-semibold (600), weight-bold (700).
- The token list is also a shipping contract: every weight token must correspond to a font file or variable axis range you actually load. A weight-800 token with no 800 file renders faux-bold or nothing.
- For variable fonts, weight tokens map to points inside the loaded axis range; record the axis range alongside the tokens so nobody tokenizes a weight the font cannot produce.
- Map weights to roles in the semantic layer (emphasis, heading, data) so accessibility review can check that hierarchy is not weight-only; the wcag-baseline reference explains why weight must never be the only signal.

## Line-height tokens

- Token line-heights as unitless numbers (1.15, 1.3, 1.4, 1.6), named by purpose: tight, heading, normal, reading, dense.
- Bind line-height to size steps at the semantic layer (body = size-300 plus reading), because the same numeric line-height reads differently at 12px and at 24px.
- Reserve a dense token for tables and data UI; dense text at 1.2-1.3 is fine for numerals and labels, and wrong for paragraphs.
- For multi-script products, allow locale overrides: Devanagari and other Brahmic scripts need taller leading than Latin; the devanagari-script reference explains the anatomy behind the number.

## Tracking tokens

- Token the few tracking values you actually use: tight (-0.01 to -0.02em) for large headings, normal (0), wide (0.05-0.08em) for small caps and labels.
- Express tracking in em, never px, so it scales with size; a fixed px letter-spacing at small sizes crushes the text.
- Pair tracking tokens with size tokens at the semantic layer: display sizes get tight tracking, caps-label gets wide. Tracking applied globally is a common way teams ruin a text face at body sizes.
- Note in the token description when a value exists to compensate for a specific family's spacing; that context disappears otherwise.

## Responsive tokens

- Two honest options: fixed steps with breakpoint-scoped semantic mappings, or fluid tokens using clamp() for headline sizes.
- Fluid pattern: --text-display: clamp(2.5rem, 5vw + 1rem, 4rem); keep fluid behavior to display sizes where drift is safe, and keep body sizes stable for reading comfort.
- Encode the same policy in the semantic layer: heading tokens may be fluid, body and data tokens are fixed steps.
- Document responsive intent in the token description ("display scales 40 to 64px between 375 and 1440") so implementers do not re-derive it.

## Naming conventions

- Pattern: namespace-dimension-step, with hyphens only: type-size-300, type-weight-semibold, type-line-height-reading.
- Reserve the semantic namespace for roles: type-heading, type-body, type-data, type-caption. Consumers see these; primitives exist for theming.
- Never encode appearance in semantic names: type-heading-blue is how tokens rot. Semantic names encode role; primitives encode value.
- Keep names stable across brands: the semantic layer is identical everywhere, and only primitive values differ. That is what makes multi-brand theming cheap.

## Multi-brand font stacks

- Primitive values are per-brand: brand A resolves type-family-serif to a licensed commercial face, brand B resolves the same token to an OFL serif. Everything downstream is untouched.
- Ship brand differences as value sets (a theme file per brand), not as forked token names; forks multiply maintenance linearly with brands.
- License scope is a token-level fact worth documenting: record in the brand theme which families are OFL and which are commercial, so the license register and the tokens agree.
- When brands share a product but not families, keep metrics compatible: fallback stacks and layout components assume similar x-heights and widths, or text reflows between brands.

## Syncing with CSS variables and Tailwind

Emit primitives as CSS custom properties and let semantic tokens reference them:

```css
:root {
  --type-family-sans: "Inter", ui-sans-serif, system-ui, sans-serif;
  --type-family-serif: "Source Serif 4", Georgia, serif;
  --type-size-300: 1rem;
  --type-line-height-reading: 1.6;
  --type-weight-semibold: 600;
}
body {
  font-family: var(--type-family-sans);
  font-size: var(--type-size-300);
  line-height: var(--type-line-height-reading);
}
```

In Tailwind v3, map tokens into the theme config so utilities and tokens cannot diverge:

```js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter", "ui-sans-serif", "system-ui", "sans-serif"],
        serif: ["Source Serif 4", "Georgia", "serif"],
      },
      fontSize: {
        body: ["1rem", { lineHeight: "1.6" }],
        "display-lg": ["3.25rem", { lineHeight: "1.1", letterSpacing: "-0.02em" }],
      },
      fontWeight: { regular: "400", semibold: "600" },
    },
  },
};
```

Tailwind v4 moves this into CSS with @theme variables (--font-sans, --text-body and its line-height modifier); the principle is identical: one source of truth, generated utilities, no hand-typed values in components.

## Example token JSON

A design-tokens format (DTCG-style) export that tools and style pipelines can consume:

```json
{
  "type": {
    "family": {
      "sans": { "$type": "fontFamily", "$value": "Inter, ui-sans-serif, system-ui, sans-serif" },
      "serif": { "$type": "fontFamily", "$value": "Source Serif 4, Georgia, serif" },
      "mono": { "$type": "fontFamily", "$value": "JetBrains Mono, ui-monospace, monospace" }
    },
    "size": {
      "200": { "$type": "dimension", "$value": "0.875rem" },
      "300": { "$type": "dimension", "$value": "1rem" },
      "400": { "$type": "dimension", "$value": "1.25rem" },
      "700": { "$type": "dimension", "$value": "2.5rem" },
      "800": { "$type": "dimension", "$value": "3.25rem" }
    },
    "lineHeight": {
      "tight": { "$type": "number", "$value": 1.15 },
      "normal": { "$type": "number", "$value": 1.4 },
      "reading": { "$type": "number", "$value": 1.6 },
      "dense": { "$type": "number", "$value": 1.3 }
    },
    "weight": {
      "regular": { "$type": "fontWeight", "$value": 400 },
      "medium": { "$type": "fontWeight", "$value": 500 },
      "semibold": { "$type": "fontWeight", "$value": 600 }
    },
    "tracking": {
      "tight": { "$type": "dimension", "$value": "-0.02em" },
      "normal": { "$type": "dimension", "$value": "0em" },
      "caps": { "$type": "dimension", "$value": "0.06em" }
    }
  },
  "semantic": {
    "heading": {
      "family": { "$type": "fontFamily", "$value": "{type.family.serif}" },
      "size": { "$type": "dimension", "$value": "{type.size.800}" },
      "lineHeight": { "$type": "number", "$value": "{type.lineHeight.tight}" },
      "tracking": { "$type": "dimension", "$value": "{type.tracking.tight}" }
    },
    "body": {
      "family": { "$type": "fontFamily", "$value": "{type.family.sans}" },
      "size": { "$type": "dimension", "$value": "{type.size.300}" },
      "lineHeight": { "$type": "number", "$value": "{type.lineHeight.reading}" }
    },
    "data": {
      "family": { "$type": "fontFamily", "$value": "{type.family.mono}" },
      "size": { "$type": "dimension", "$value": "{type.size.200}" },
      "lineHeight": { "$type": "number", "$value": "{type.lineHeight.dense}" }
    }
  }
}
```

## Versioning and deprecating tokens

- Version the token file like code; a token change is a user-visible typographic change and goes through the same review as a font update.
- Deprecate by addition: introduce the replacement, mark the old token deprecated with a pointer, migrate consumers, then remove in the next major. Silent renames strand every consumer.
- Keep a changelog entry per release: added, deprecated, removed, value changes. "Value changes" is the dangerous category; a quiet change to type-size-300 reflows the product.
- Record the font versions each token release was validated against, so token history and font history stay coupled.

## Common mistakes

- Semantic tokens named by appearance instead of role, which breaks at the first rebrand.
- Tokens for weights or sizes no font file can render; the token list and the shipped files must agree.
- Hard-coding px sizes alongside a token system, quietly exempting parts of the product from user preferences.
- Letting components consume primitive tokens directly, which makes the semantic layer decorative.
- Tracking tokens applied globally instead of bound to size steps, crushing body text.
- Multi-brand forks that duplicate token names instead of varying values.

## Cross-references

- [Font-face and CSS](../technical/font-face-and-css.md)
- [CSS handoff snippets](css-handoff-snippets.md)
- [Web and SaaS interfaces](../applications/web-and-saas-interfaces.md)
- [WCAG baseline for type](../accessibility/wcag-baseline-for-type.md)

Compiled 2025 as part of the Fontlore project.
