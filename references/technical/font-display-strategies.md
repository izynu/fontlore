# Font Display Strategies

What this reference covers: What each font-display value does with real timing, the FOUT versus FOIT tradeoff in practical terms, how preload changes outcomes, and how to match a strategy to page type. This is a small API with outsized UX consequences; most sites should use swap, some should use optional, almost none should use block.

## The values and their timing

font-display is set per @font-face and controls what happens in the gap between page render and font arrival:

- auto: browser default behavior, effectively block in practice. Choose it only by conscious omission, not by habit.
- block: the text is invisible (rendered with an invisible fallback) for a block period, up to about 3 seconds in current browsers, then swaps. Highest risk: blank text on slow networks.
- swap: essentially no block period; text renders in the fallback font immediately and swaps when the webfont arrives. Layout shifts once, text is never invisible.
- fallback: a short block period (around 100 ms), then fallback text, then swap if the font arrives within about 3 seconds. A compromise that avoids both blank text and permanent unstyled flashes for marginal fonts.
- optional: a very short block period (around 100 ms); if the font is not ready, the fallback is used for this page view, and the browser may download the font in the background for subsequent views. Designed for near-zero layout impact.

FOUT (flash of unstyled text) is what swap produces; FOIT (flash of invisible text) is what block produces. The 2016-era debate ended with a consensus: invisible text is worse than a font swap for content, which is why swap became the default recommendation.

## Matching strategy to context

- Content and marketing pages: swap. Reading is the product; invisible text is a failure. Pair with metric-matched fallbacks to make the swap small.
- Web apps and dashboards: swap or fallback. The first paint is usually the chrome; a single small shift on text-heavy panes is acceptable if fallbacks are metric-matched.
- Fonts that are pure brand polish (a display face for a logo-like wordmark in the page): optional. If it does not arrive instantly, the fallback is fine, and returning visitors get the real thing from cache.
- Fonts above the fold on a conversion funnel: swap plus preload, and measure; the goal is arrival before first paint so no swap is visible at all.
- Icon fonts and pictogram faces: avoid them entirely; inline SVG removes the problem. If unavoidable, block or swap with a fixed-size container so layout cannot shift.

## Preload changes the math

A preloaded font starts downloading immediately with the CSS rather than after layout discovers it needs it:

- With preload and correct subset paths, swap and fallback usually complete the swap before first paint, making the choice mostly moot; the strategy then matters only on cache misses and slow devices.
- optional plus preload behaves like "use it if it's instant", which on repeat views is exactly what you want for brand faces; many teams standardize on optional plus preload for display fonts and swap for body fonts.
- Preload only the exact files first paint needs (usually one or two faces, one subset each). Preloading six faces delays the CSS that is also on the critical path.
- The preloaded URL must match the @font-face URL byte for byte, including unicode-range implications; preloading a full file while the CSS requests a subset wastes the preload.

## Measuring instead of guessing

- Test with DevTools network throttling (Slow 4G and a simulated cold cache) and watch when text paints and when it re-renders.
- Track layout shift: Cumulative Layout Shift attributed to font swaps shows up in field data (web vitals). If font swaps dominate CLS, fix fallback metrics before touching font-display.
- Watch the swap period behavior: with fallback/optional on a fast connection the font almost always wins the race; on a slow connection the fallback sticks around, which is the point.
- Test repeat views with the font cached; optional degrades gracefully only if caching is configured so the font actually persists.

## Interaction with fallback metrics

font-display choices are half the story; the other half is how different the fallback looks:

- A metric-matched fallback (via size-adjust, ascent-override, descent-override) shrinks the visible jump under swap and fallback to near-nothing, which is what makes swap safe on content pages.
- With an unmatched system fallback, swap on a slow connection shows a full typographic re-layout, which users read as brokenness even when CLS stays under thresholds.
- For CJK and other large-subset content, optional is often the only sane choice for self-hosted fonts, because the slices may arrive late; the system stack looks native anyway.

## Common mistakes

- font-display: block everywhere "so the brand always shows"; on a slow day the page is a blank wall.
- font-display: optional without preload and without caching headers, so the font essentially never appears on first view and sometimes not after.
- Leaving auto in place while believing a strategy was chosen; auto is not a neutral, it is block in practice.
- Preloading every weight "to be safe", delaying first paint and wasting bytes on faces first paint never uses.
- Judging strategies on a fast office connection; the differences only appear under throttling and real mobile conditions.
- Pairing swap with an unstyled fallback and measuring nothing; the strategy is only as good as the fallback behind it.

## Decision rules

- Default to swap for any text users came to read, with metric-matched fallbacks.
- Use optional only for faces where absence is acceptable (brand flourishes, decorative numerals) and only with preload plus long-lived caching.
- Use fallback when you want a compromise without per-face tuning, and verify behavior under throttling.
- Never ship block on user-facing content; if a stakeholder demands it, show them the blank-page recording first.
- Re-evaluate whenever the font stack changes: strategies that fit a 30 KB latin file do not fit a 300 KB variable one.

## Comparison table

| Value | Block period | Swap window | Invisible text? | Layout shift | Fits |
| --- | --- | --- | --- | --- | --- |
| auto | browser-chosen (block in practice) | - | possible | yes | nothing deliberate |
| block | about 3 s | infinite | yes, until font or timeout | yes | nothing user-facing |
| swap | effectively 0 | infinite | no | one reflow on arrival | body and content text |
| fallback | about 100 ms | about 3 s | a blink | small | text where absence is tolerable |
| optional | about 100 ms | none | a blink | none after the block | brand polish, returning visitors |

Two derived behaviors worth memorizing:

- optional is the only value that cannot shift layout after first paint: if the font misses the block window it is not used for this page load at all, and the browser may keep downloading it for the next visit.
- fallback degrades to "system font for good" on slow connections: once the about-3-s swap window closes, a late font never swaps in. That is stability by design, and a trap for faces you promised the reader.

## Worked example

Cold cache, throttled to Slow 4G: CSS at 300 ms, first paint at 350 ms, body font at 1.5 s. Same page, four strategies:

- swap: text paints at 350 ms in the fallback; one reflow at 1.5 s. With a metric-adjusted fallback the reflow is invisible; without one, the column rewraps.
- block: the column is blank until 1.5 s. The reader sees a header and nothing else.
- fallback: fallback text from 350 ms; the 1.5 s arrival is inside the 3 s window, so the swap happens and the result matches swap.
- optional: the font misses the 100 ms race on this cold load; the page stays on the system font and looks native. The download continues in the background for next time.

Repeat the visit with the font cached and all four converge, which is why cold and warm loads must be tested separately; the strategies differ only when something is late.

## Code notes

One strategy per face, declared explicitly:

```
@font-face {
  font-family: "Inter";
  src: url("/fonts/inter-latin-400.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;          /* content text */
  unicode-range: U+0000-00FF, U+2000-206F, U+20AC;
}

@font-face {
  font-family: "Brand Display";
  src: url("/fonts/brand-display-latin.woff2") format("woff2");
  font-weight: 700;
  font-style: normal;
  font-display: optional;      /* polish face; absence acceptable */
}
```

Preload only the face first paint needs, and only when the strategy benefits:

```
<link rel="preload" href="/fonts/inter-latin-400.woff2"
      as="font" type="font/woff2" crossorigin>
```

## Field notes

- The display timeline starts when layout first needs the face, not at navigation; a font discovered late (fonts.css fetched after render) starts its clock late too.
- Very old engines ignore font-display entirely and behave like auto; every claim here is a current-browser claim.
- The Google Fonts CSS API exposes the choice as the display query parameter (display=swap); self-hosted CSS must set font-display explicitly on every face.
- font-display on a metric-adjusted fallback face is meaningless: that face is local() and never downloads.
- Under HTTP/2 or HTTP/3, preloaded fonts contend with CSS and images for connection bandwidth; preload fewer faces on multiplexed protocols, not more.
- A screen recording of block on a throttled cold load ends stakeholder debates about "the brand must always show" faster than any argument.

## Quick reference

- Body text users came to read: swap, with metric-adjusted fallback.
- Display face whose absence is survivable: optional, with preload and immutable caching.
- Compromise without per-face tuning: fallback, verified under throttling.
- Never block on user-facing content; never auto by omission.
- Measure cold and warm loads separately; they are different products.

## Common failure modes

- Blank text for seconds on a content page: font-display: block (or untouched auto) plus a slow font. Switch to swap and invest in the fallback instead.
- The webfont never appears with optional: no preload, or cache headers that expire the file between visits. optional is a contract that requires both.
- A visible double render on every load even with swap: the "fallback" is the generic serif the browser picked, not a designed system font. Name a real fallback before the generic keyword.
- CLS persists after adding metric overrides: the shift source is not the font swap; check images without dimensions, injected banners, and late CSS before blaming typography.
- Preload works locally but not in production: the CDN rewrites font URLs (versioned paths, query strings) so the preloaded URL and the @font-face URL no longer match byte for byte.

## Cross-references

- [Font loading pipeline](font-loading-pipeline.md)
- [Fallback metrics and CLS](fallback-metrics-and-cls.md)
- [Font-face and CSS](font-face-and-css.md)
- [Low vision and zoom](../accessibility/low-vision-and-zoom.md)

Compiled 2025 as part of the Fontlore project.
