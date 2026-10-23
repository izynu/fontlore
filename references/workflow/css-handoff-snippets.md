# CSS Handoff Snippets

What this reference covers: The exact CSS that ships with a font decision: @font-face blocks, fallback metric overrides, custom properties, type scales, feature settings, preload markup, and per-language adjustments. A font choice without these snippets is a suggestion, not a handoff; this file is the template to fill in.

## @font-face blocks

Static weights, one block per file, honest descriptors:

- font-family: "App Sans"; src: url("/fonts/app-sans-latin-400.woff2") format("woff2"); font-weight: 400; font-style: normal; font-display: swap;
- Repeat per weight (400, 500, 600, 700) and per style (italic blocks carry font-style: italic), with unicode-range per subset file (latin, latin-ext, cyrillic, greek, vietnamese as the language matrix requires).
- Variable version: one block, font-weight: 100 900 (the actual range), font-style: normal, same font-display and unicode-range discipline.

Metric-adjusted fallback, sized against the primary (generate the numbers with tooling, see the fallback reference):

- @font-face { font-family: "App Sans Fallback"; src: local("Arial"); size-adjust: 105%; ascent-override: 105%; descent-override: 35%; line-gap-override: 0%; }
- The stack then reads: font-family: "App Sans", "App Sans Fallback", sans-serif;

## Custom properties: the token layer

- --font-sans: "App Sans", "App Sans Fallback", system-ui, sans-serif;
- --font-display: "App Display", "App Display Fallback", Georgia, serif;
- --font-mono: "App Mono", ui-monospace, "Cascadia Mono", monospace;
- Weights as tokens too: --font-weight-regular: 400; --font-weight-medium: 500; --font-weight-semibold: 600; --font-weight-bold: 700; components consume tokens, never raw numbers, so a family swap is a token edit.
- Per-script adjustments as scoped rules: :lang(ar) { line-height: 1.6; } :lang(th) { line-height: 1.7; } :lang(hi) { line-height: 1.6; } plus any size bumps; these live next to the family tokens, not scattered in components.

## Type scale

Rem-based, role-named, with leading attached:

- --text-xs: 0.75rem with --leading-xs: 1.4 (captions, metadata; check contrast and 12 px floor).
- --text-sm: 0.875rem with --leading-sm: 1.45 (dense UI, tables).
- --text-base: 1rem with --leading-base: 1.5 (body).
- --text-lg: 1.125rem with --leading-lg: 1.55 (intro text).
- --text-xl through display sizes with leading stepping down (1.3, 1.2, 1.1); fluid display sizes use clamp() with rem bounds: --text-display: clamp(2rem, 1.4rem + 2.5vw, 4rem).
- Scale values are a project decision; what is not negotiable is that leading travels with size as one token, so components cannot pair 1.6 leading with display sizes by accident.

## Feature settings

- Tables and data: .tabular { font-variant-numeric: tabular-nums; } applied at the table or metric component level.
- Editorial body (if the face earns it): .body-editorial { font-variant-numeric: oldstyle-nums proportional-nums; } one class, documented.
- Stylistic sets frozen in tokens: .brand-display { font-variation-settings: "SOFT" 60, "WONK" 1; } with the axis values recorded as the brand's chosen instance, or @font-feature-values for named sets.
- Disable ligatures in code contexts: code, kbd { font-variant-ligatures: none; }
- Nothing else: default ligatures and kerning stay on; feature sprawl is a maintenance tax.

## Preload markup

- link rel="preload" href="/fonts/app-sans-latin-400.woff2" as="font" type="font/woff2" crossorigin
- One or two faces maximum, exactly matching the @font-face URLs; the crossorigin attribute is mandatory even same-origin.
- Pair with font-display: swap and the metric-adjusted fallback so the swap is invisible.

## The handoff package

Ship the decision as a package, not a message:

1. fonts/ directory with files, license texts, and a manifest (family, version, source, date).
2. tokens.css with the custom properties above.
3. fonts.css with the @font-face blocks and fallback overrides.
4. README with the tuning notes (per-language leading, feature decisions, size floors) and links to the decision record.
5. The comparison and test artifacts referenced, so future maintainers can re-verify.

## Common mistakes

- Handing over family names without weights: the team then loads six weights "to be safe" and the budget dies.
- Tokens for families but not for weights and leading, so components hardcode values and the next swap is a rewrite.
- Preload URLs that drift from @font-face URLs after a rename; the preload silently becomes waste.
- Missing per-language leading in the handoff, discovered when the first Arabic or Thai content ships.
- Fallback overrides copied from a template without regenerating for the actual font pair; wrong overrides are worse than none.
- License files not shipped with the fonts; the first vendor or audit request stalls the release.

## Decision rules

- Every font decision ships with this package on the same day; a decision that waits for "CSS cleanup" ships without its tuning.
- Any new surface (email, docs site, app webview) inherits the tokens; new tokens require a governance request, not a local edit.
- Version bumps regenerate the whole package (files, overrides, manifest) atomically; partial updates are how mixed-version bugs start.
- If the handoff cannot include a metric-adjusted fallback for some surface (email clients, for example), document the swap risk in the README for that surface.

## Code notes: the fonts.css skeleton

A complete minimal handoff file; fill in the project specifics and delete what does not apply:

```css
/* fonts.css - ships with tokens.css and the license texts */

/* Primary face: one block per subset per weight */
@font-face {
  font-family: "App Sans";
  src: url("/fonts/app-sans-latin-400.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
  /* Abbreviated; copy the exact range from the source of the subset files */
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}

/* Metric-adjusted fallback: regenerate the numbers for the actual pair */
@font-face {
  font-family: "App Sans Fallback";
  src: local("Arial");
  size-adjust: 105%;
  ascent-override: 105%;
  descent-override: 35%;
  line-gap-override: 0%;
}

/* Tokens: families, weights, and leading travel together */
:root {
  --font-sans: "App Sans", "App Sans Fallback", system-ui, sans-serif;
  --font-weight-regular: 400;
  --font-weight-semibold: 600;
  --leading-body: 1.5;
  --leading-tight: 1.2;
}

/* Roles consume tokens; text sizes in rem only */
body { font-family: var(--font-sans); font-size: 1rem; line-height: var(--leading-body); }
h1, h2, h3 { line-height: var(--leading-tight); }

/* No fixed heights on text containers; overrides and zoom must reflow */
.button { min-height: 2.75rem; padding: 0.5rem 1rem; }

/* Data alignment */
.tabular { font-variant-numeric: tabular-nums; }

/* Per-script leading lives here, not in components */
:lang(ar) { line-height: 1.7; }
:lang(th) { line-height: 1.8; }
```

A note on the unicode-range: copy it from the source of the subset files (the google/fonts repository and Fontsource publish the exact values). Hand-guessed ranges silently exclude glyphs and are miserable to debug.

## Quick reference: font-display values

| Value | Behavior | Use when |
| --- | --- | --- |
| swap | Fallback shows at once; swaps when the webfont loads (zero block period, unlimited swap period) | Default for text users must read; pair with a metric-adjusted fallback |
| block | Invisible text during a short block period, then swap | Faces where a flash of fallback is unacceptable and slow loads are rare |
| fallback | Very short block (about 100 ms), short swap window (about 3 s), then the fallback sticks | Ambient or non-critical faces |
| optional | Very short block; the browser uses it only if cached; no swap after the first visit | Faces the design can lose entirely on a slow connection |

The time constants are browser-defined and have shifted over browser releases; treat the durations as approximate and verify in current browsers. Whichever value ships, it belongs in the @font-face block and its reason belongs in the handoff README.

## Worked example: handoff for a three-family system

A product ships App Sans (UI and body), App Display (marketing hero), and App Mono (code). The handoff package, as built:

1. fonts/: the woff2 files (sans 400/600/700 in latin and latin-ext, the display variable file, mono 400/500), the OFL license text for each family, and MANIFEST.md listing family, version, source URL, and download date per file.
2. fonts.css: @font-face blocks with unicode-range per subset, a metric-adjusted fallback generated for App Sans against Arial, and font-display: swap everywhere except the display face (fallback, because the hero tolerates it).
3. tokens.css: family, weight, size, and leading tokens; per-script leading for the two shipped second languages; the tabular-nums utility.
4. README: the size floors (16 px inputs, 18 px reading surfaces), the preload pair (sans 400 latin only), the decisions that were rejected (no 300 weight: unused, saved kilobytes), and links to the comparison artifacts.
5. The acceptance checklist below, run by the receiving engineer before merge.

The package took half a day to assemble and one review round. The same handoff previously delivered as a message with three family names cost the team two weeks of wrong-weight loading and a re-audit.

## Audit checklist: handoff acceptance

The receiving engineer runs this before merging a font handoff:

- [ ] Every @font-face URL resolves and matches the preload URLs exactly.
- [ ] Weight and style descriptors match the actual files (open one and check the name table).
- [ ] unicode-range values copied from the file source, not hand-typed from memory.
- [ ] The fallback overrides were regenerated for the actual primary and fallback pair, not copied from a template.
- [ ] Tokens exist for families, weights, sizes, and leading; components import tokens only.
- [ ] No text container has a fixed height; min-height in rem at most.
- [ ] Per-language rules present for every shipped language.
- [ ] The license text for every family ships in the package; the manifest records version and source.
- [ ] The 1.4.12 spacing sweep and the 200 percent zoom pass run against the handoff state, screenshots filed.
- [ ] Preload limited to one or two files that are actually used above the fold.

## Cross-references

- [Font-face and CSS](../technical/font-face-and-css.md)
- [Design tokens for type](design-tokens-for-type.md)
- [Font loading pipeline](../technical/font-loading-pipeline.md)
- [Fallback metrics and CLS](../technical/fallback-metrics-and-cls.md)

Compiled 2025 as part of the Fontlore project.
