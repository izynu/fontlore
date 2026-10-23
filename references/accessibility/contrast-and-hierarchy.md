# Contrast and Hierarchy

What this reference covers: How contrast ratios work for text, the interplay between font weight, size, and contrast, and how to build hierarchy that survives without relying on color alone. Contrast is a token-level property, but weight and size choices decide how much contrast you need and whether the design reads.

## The ratios and their sizes

WCAG 1.4.3 (AA) requires a contrast ratio of at least 4.5 to 1 for normal text and 3 to 1 for large text. Large text means at least 24 px regular or 18.66 px bold. AAA (1.4.6) raises these to 7 to 1 and 4.5 to 1. The ratios apply to text against its background, including over images (with a scrim) and inside components.

- Non-text contrast (1.4.11, 3 to 1) applies to focus indicators, input borders, and icons that carry meaning; it is separate from text contrast and often missed.
- Contrast is measured between actual rendered colors: opacity, blending, dark-mode variants, and gradients all create pairs nobody measured until the audit.

## Weight and size interplay

The same color pair reads differently at different weights and sizes:

- Small and light text needs the full 4.5 to 1 and is the first thing to fail in practice; a 300-weight 14 px paragraph in mid-gray fails on most brand palettes.
- Thin strokes on light backgrounds effectively lower perceived contrast: the anti-aliased stroke blends with the background. A 2 px stroke at 300 weight carries less ink than a 2 px stroke at 500.
- Larger text earns a lower requirement because letterforms are bigger; that is what the 24 px / 18.66 px-bold boundary encodes. Do not stretch it: 18 px at 400 weight is not large text.
- On dark backgrounds, light weights get worse, not better: bright thin strokes bloom (halation). Dark mode usually wants weights one step heavier than light mode, and pure white on pure black is harsher than an off-white on near-black.
- Practical mapping: body text 400-500 weight; secondary text 400 at higher contrast than you think; labels and captions 500-600; display can be lighter only because of size.
- WCAG 1.4.3 exempts inactive components, but enabled controls styled to look disabled still carry real information; keep them above the floor.

## Hierarchy without color alone

WCAG 1.4.1 (Use of Color) forbids color as the only visual means of conveying information; the same discipline builds hierarchy that works for color-blind users, in grayscale printing, and under forced-colors modes:

- Scale: size steps of at least 1.2x between adjacent hierarchy levels (a 1.25 modular scale is common); tiny steps like 15 to 16 px do not read as hierarchy.
- Weight: real weights from the family (500, 600, 700), not synthesized bold; combine with size for the strongest signal.
- Case and spacing: tracked uppercase labels are a distinct tier; keep them short (see the line-length reference for why long uppercase text fails).
- Position and grouping: whitespace, alignment, and rules (hairlines) carry structure in every mode.
- Decoration: for links, underline (or a weight change plus underline on hover) rather than color alone; for status, pair color with an icon or text label.

The grayscale test: desaturate the design (or print it) and check the hierarchy and links still read. If everything collapses into one gray, the hierarchy was color.

## Dark mode specifics

- Do not invert the palette; re-derive it. Text at 90 to 95 percent lightness on a 8 to 12 percent lightness background passes contrast without halation.
- Re-check every token pair in dark mode; many light-mode pairs that pass fail when naively flipped because perception of contrast is not symmetric.
- Weights: bump thin text one step; avoid 300-weight body in dark themes.
- Elevation cues (shadow) weaken on dark backgrounds; typography and borders must carry hierarchy instead.
- Pure white #FFFFFF on pure black #000000 passes at 21 to 1 yet reads harsher than off-white on near-black; the criterion is a floor, not a target.

## Making it enforceable

- Define contrast at the token level: every text-on-background pair used by components is listed and tested; new pairs require a check before use.
- Automate the boring part: token linters and browser extensions (and build-time checkers) verify pairs; visually verify images-with-text and gradient surfaces manually.
- Include disabled, placeholder, hover, focus, and visited states in the audit; these are the states nobody checks and audits find failing.
- Document the "large text" exceptions explicitly (which sizes and weights qualify) so designers do not assume every heading gets the 3 to 1 pass.
- Store the pair list with its ratio results as a generated artifact; a token change without a fresh report is an unreviewed change.
- Contrast-check the focus ring against every surface it crosses (card on page, header on content), not only the component's own background.
- Round against yourself: compute to two decimals and treat a 4.49 as a fail; tools round differently, and the criterion does not.

## Common mistakes

- Placeholder text at 40 percent opacity: fails contrast and vanishes for low-vision users; placeholders are labels people need.
- Gray-on-gray dark modes and low-emphasis text that quietly sits at 3.8 to 1.
- Thin weights compensating for failing contrast ("it looks elegant"); perceived legibility drops even when a large-size ratio technically passes.
- Hierarchy built from three shades of one color and nothing else; it fails grayscale, forced-colors, and color-blind users simultaneously.
- Forgetting focus indicators in the re-theme: the new brand color passes for text and fails 3 to 1 as a focus ring on the background.
- Checking contrast in the design tool on flat swatches, then shipping text over photos with no scrim.
- Treating dark-mode text as "white on black, done"; the ramp examples above exist because that assumption produces halation and failing secondary text.

## Decision rules

- New color pair: compute the ratio for its actual size class; no exceptions for "it's just a label".
- Contrast fails: change the color, not the weight; thinning type to "reduce visual noise" makes it worse.
- Building hierarchy: use at least two of size, weight, case, and position on each tier difference; color may be the accent, never the only signal.
- Dark mode: re-run the full token audit; do not derive by inversion.
- Image-backed text: require a scrim or overlay that guarantees the ratio across the whole text box, verified at the extremes of the image set.

## Quick reference: contrast math and anchor values

The ratio is (L1 + 0.05) / (L2 + 0.05), where L is relative luminance and the lighter color goes first. Anchor values worth memorizing against pure white #FFFFFF:

| Foreground on white | Ratio | Verdict |
| --- | --- | --- |
| #000000 black | 21 to 1 | Passes everything |
| #595959 | about 7 to 1 | AAA body text |
| #767676 | about 4.5 to 1 | AA body text; fails AAA |
| #949494 | about 3 to 1 | Large text only (24 px, or 18.66 px bold) |
| #B3B3B3 | under 2.5 to 1 | Decorative use at best |

On near-black #121212, #E8E8E8 text lands around 15 to 1 and #A0A0A0 around 7 to 1, which is why dark-mode ramps are built lighter than a naive inversion suggests.

Relative luminance is nonlinear (it is computed out of sRGB gamma), so you cannot eyeball ratios from hex brightness; compute them, and compute them on the composited result whenever opacity, blending, or gradients are involved.

## Worked example: deriving a dark-mode text ramp

Surface #121212, target AA with AAA for body:

1. Body text: #E8E8E8 at weight 400, about 15 to 1; comfortably AAA.
2. Secondary text: #A0A0A0 at 400, about 7 to 1; AAA for body, generous for captions.
3. Placeholder and disabled: #8A8A8A, about 5.4 to 1; above the AA floor even though disabled components are technically exempt.
4. Accent as link text: the raw brand orange measures below 3 to 1 on the surface (compute your own pair); the link token is lightened until it clears 4.5 to 1, and the brand orange is reserved for fills with dark text on top.
5. Focus ring: a separate token at 3 to 1 minimum against every surface it can appear on.
6. Halation check: the lightest weight in the ramp is 400; 300 is banned in dark themes.

The lesson: dark mode re-derives every pair, and the accent usually needs a dedicated text variant.

## Code notes: enforcing contrast in CSS

```css
:root {
  --ink: #1a1a1a;      /* body on light: about 16 to 1 */
  --ink-2: #595959;    /* secondary on light: about 7 to 1, AAA */
  --ink-3: #767676;    /* tertiary on light: about 4.5 to 1, AA floor */
  --paper: #ffffff;
}
.theme-dark {
  --paper: #121212;
  --ink: #e8e8e8;      /* about 15 to 1 */
  --ink-2: #a0a0a0;    /* about 7 to 1 */
  --ink-3: #8a8a8a;    /* about 5.4 to 1; placeholder and disabled */
}

a { text-underline-offset: 0.15em; text-decoration-thickness: 1px; }
a:hover { text-decoration-thickness: 2px; }  /* hover reinforces; color alone never signals */
```

Name tokens by role, not by value: when the palette changes, the audit re-runs against the same pair list instead of a new set of ad-hoc colors.

## Comparison table: hierarchy signals and their failure modes

| Signal | Works | Fails when |
| --- | --- | --- |
| Size | Steps of 1.2x or more between adjacent tiers | 15 to 16 px "hierarchy" nobody perceives |
| Weight | Real 500, 600, 700 from the family | Synthetic bold; 300 versus 400 at small sizes |
| Case | Tracked uppercase labels as a distinct tier | Long strings in caps; case as the only signal |
| Color | Accent as reinforcement | Color as the sole carrier (a 1.4.1 failure) |
| Position | Indents, grouping, whitespace | Cramped layouts where position reads as accident |
| Decoration | Underlines for links, rules for asides | Decoration on everything, so nothing stands out |

Grayscale is the arbiter: desaturate the screen or print it, and every tier that disappears was never a tier.

## Cross-references

- [WCAG baseline for type](wcag-baseline-for-type.md)
- [Line length and reading](line-length-and-reading.md)
- [Editorial and news](../applications/editorial-and-news.md)
- [Packaging and retail](../applications/packaging-and-retail.md)

Compiled 2025 as part of the Fontlore project.
