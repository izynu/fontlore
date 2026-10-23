# Variable Fonts and Axes

What this reference covers: How variable fonts work, the registered axes and their CSS mappings, custom axes, the gap between high-level properties and font-variation-settings, and how axis support varies in practice. It also covers when a variable font is the wrong choice.

## What a variable font is

A variable font packs a design space into one file: instead of separate 400 and 700 files, one file interpolates between them. The design space is defined by named axes with ranges. Benefits: fewer requests, continuous weights, animation possibilities, smaller total size when many weights are used. Costs: larger single files when few instances are used, and a two-layer CSS model that is easy to misuse.

## The registered axes

Registered axes are lowercase and map to standard CSS properties:

- wght, weight: typically 100 to 1000; maps to font-weight. Ranges like 100-900 are common; Inter runs 100-900, and families can define any range.
- wdth, width: percentage of normal width, commonly 50-200 but often much narrower per family; maps to font-stretch.
- slnt, slant: degrees of slant, negative values slant clockwise per convention; maps to font-style: oblique with an angle.
- ital, italic: a binary 0 or 1 for a separate italic design within the same file; maps to font-style: italic. Many families still ship italic as a separate file instead; both patterns are legitimate.
- opsz, optical size: point size the design was tuned for; maps to font-optical-sizing: auto, which sets opsz from font-size automatically. Text and display designs differ substantially in a good opsz axis (Fraunces spans 9-144; display designs get tighter spacing and higher contrast).

Custom axes are uppercase four-character tags, family-specific: Fraunces has SOFT (softness) and WONK (wonky letterforms); Roboto Flex exposes GRAD (grade, which adjusts stroke weight without changing metrics, useful for dark modes), plus many more. There is no CSS property for custom axes; they are reached only through font-variation-settings.

## The two-layer CSS model

High-level properties (font-weight, font-stretch, font-style, font-optical-sizing) are the API: they compose, inherit normally, respond to user styles, and work with design tokens. font-variation-settings is a low-level escape hatch that sets axes directly:

- font-variation-settings: "wght" 550 works, but it overrides the high-level property chain and does not cascade the way properties do: a child setting one axis does not inherit the parent's other axis settings in an intuitive way. Mixing layers produces unpredictable results.
- Rule: use high-level properties for wght, wdth, slnt/ital, and opsz. Reserve font-variation-settings for custom axes (SOFT, WONK, GRAD), ideally centralized in a token or utility class, and never scattered per element.
- When both are set on the same element, font-variation-settings wins; that is the mechanism behind most "my font-weight is ignored" bugs.

## Support reality

- The variable font format itself is supported in all current browsers; loading, unicode-range, and the wght/wdth mappings are safe.
- opsz auto behavior is broadly supported; verify in your target browsers when opsz is central to the design.
- Named instances expose nicely in some tooling but are irrelevant to CSS; author against ranges, not instance names.
- Animating axes with CSS transitions works for registered axes in current browsers; test on real hardware, since variable interpolation on low-end devices can jank.
- Older corporate browsers may ignore ranges and render the default instance; provide static fallback faces if that audience matters, and check analytics before building on interpolation.

## When variable is wrong

- Two weights only: two static files are often smaller than one variable file, and simpler to reason about. Compare actual woff2 sizes before choosing.
- Icon fonts: variable axes add nothing; use SVG.
- A brand that legally or stylistically restricts itself to three fixed styles: bake them as statics; design systems often prefer fixed values anyway.
- Subsetting interplay: heavy subsetting of a variable font can strip variation tables or bloat them; measure the subset output.

## Practical recipes

- UI system: one variable file, font-weight driven by tokens (400 body, 500 labels, 600 buttons, 700 headings). No font-variation-settings anywhere.
- Display brand: a family with opsz and custom axes; headings get font-optical-sizing: auto plus a tokenized utility for the custom axes (for example .brand-display { font-variation-settings: "SOFT" 80, "WONK" 1; }).
- Dark mode compensation: some families (Roboto Flex's GRAD) let you add stroke weight on dark backgrounds to counteract halation; wire it to a color-scheme media query rather than per-element hacks.
- Fluid display type: pair opsz with clamp()-based font-size so the optical axis tracks viewport changes naturally.

## Common mistakes

- Using font-variation-settings for weight and then wondering why inherited font-weight styles from a parent or user stylesheet do nothing.
- Shipping the full variable file when two static weights were used; variable files can be several times larger than the two statics actually rendered.
- Declaring font-weight: 100 900 on a static face, which lies to the browser and breaks synthesis prevention.
- Ignoring opsz on a display face with a strong optical axis, then complaining it looks clunky at headline sizes.
- Animating wght on long body text; weight animation is for display moments and short labels, and it can hurt readability while running.
- Assuming custom axes exist on a font because they exist on another family's file; axis tags are per-family and must be checked per file.

## Decision rules

- Three or more weights, or continuous weight needs: variable.
- Exactly one or two weights: statics, unless the variable file is genuinely smaller.
- Display design with optical size and character: variable with opsz, custom axes tokenized.
- Strict legacy support: statics with a documented upgrade path.
- Any custom axis usage: centralize it, document it in the design system, and add a fallback for browsers that ignore the axis.

## Comparison table

| Tag | Name | Value space | CSS mapping |
| --- | --- | --- | --- |
| wght | weight | typically 100-900; the spec permits 1-1000 | font-weight |
| wdth | width | percent of normal; the range is per family | font-stretch |
| slnt | slant | angle in degrees; negative slants clockwise | font-style: oblique with an angle |
| ital | italic | 0 or 1 | font-style: italic |
| opsz | optical size | point size the design was tuned for | font-optical-sizing: auto |
| GRAD (custom) | grade | stroke weight with no metric change | font-variation-settings only |
| SOFT, WONK (custom) | Fraunces softness and wonk | family-specific | font-variation-settings only |

## Code notes

A variable face declares its space in @font-face:

```
@font-face {
  font-family: "Inter";
  src: url("/fonts/inter-var-latin.woff2") format("woff2");
  font-weight: 100 900;        /* the wght span of this file */
  font-style: normal;
  font-display: swap;
  unicode-range: U+0000-00FF, U+2000-206F, U+20AC;
}
```

Width joins when the file carries it:

```
@font-face {
  font-family: "Roboto Flex";
  src: url("/fonts/roboto-flex-var.woff2") format("woff2");
  font-weight: 100 1000;
  font-stretch: 25% 151%;
  font-display: swap;
}
```

Usage stays high-level; custom axes get one tokenized utility:

```
body { font-weight: 400; font-optical-sizing: auto; }
.hero-display {
  font-variation-settings: "SOFT" var(--display-soft), "WONK" var(--display-wonk);
}
```

Dark-mode grade compensation, wired to the scheme rather than to elements:

```
@media (prefers-color-scheme: dark) {
  :root { --grade-boost: 100; }   /* a value inside the family's GRAD range */
}
.brand-text { font-variation-settings: "GRAD" var(--grade-boost, 0); }
```

## Worked example

Migrating a static four-weight UI system to one variable file without touching component code:

1. Before: inter-400, inter-500, inter-600, inter-700 files, each with its own @font-face; components set font-weight numerically.
2. Ship the variable file with font-weight: 100 900 in the descriptor, keeping the same family name.
3. Delete the static blocks. No component changes: font-weight: 600 keeps resolving, now continuously.
4. Compare bytes: the variable latin file against the sum of the four statics actually rendered; if it is larger, question the migration (see "When variable is wrong").
5. Re-verify the adjusted fallback overrides and opsz behavior, then confirm in the network panel that one file loads and synthetic bold is gone.

## Field notes

- With no variation settings applied you get the default instance (usually Regular); a browser that ignores an axis renders exactly that, which is also your fallback appearance.
- font-variation-settings inherits as a whole: a parent's "wght" 550 silently beats a child's font-weight: 700. This inheritance quirk is behind most "my weight is ignored" bugs.
- Grade differs from weight: GRAD adjusts stroke thickness without moving advance widths, so text does not reflow, which is why it suits dark-mode compensation while wght does not.
- Animating wght re-lays-out text every frame when advances shift; animate axes only on display-size text where reflow is acceptable.
- Named instances (Thin, SemiBold Condensed) belong to design tools and specimens; CSS addresses ranges, never instance names.

## Quick reference

- Declare ranges in @font-face (font-weight: 100 900, font-stretch where the file has it); the browser interpolates inside them.
- High-level properties for wght, wdth, slnt, ital, and opsz; font-variation-settings only for custom axes, centralized in one place.
- font-variation-settings beats high-level properties on the same element and inherits as one block; keep it off body text hierarchies.
- font-optical-sizing: auto maps font-size to opsz; leave it on for faces with a real optical axis.
- Compare the variable file against the statics actually rendered before committing; variable is not automatically smaller.
- Named instances are for design tools; CSS addresses ranges, never instance names.

## Cross-references

- [OpenType features](opentype-features.md)
- [Inspecting font files](inspecting-font-files.md)
- [Design tokens for type](../workflow/design-tokens-for-type.md)
- [Dynamic type and preferences](../accessibility/dynamic-type-and-preferences.md)

Compiled 2025 as part of the Fontlore project.
