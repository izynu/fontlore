# Fallback Metrics and CLS

What this reference covers: Why font swaps shift layout, the metric override descriptors (size-adjust, ascent-override, descent-override, line-gap-override), how to compute and generate metric-compatible fallbacks, and how this fits into keeping Cumulative Layout Shift low. This is the craft that makes font-display: swap safe.

## The problem in one paragraph

With font-display: swap, text paints in the fallback font and reflows when the webfont arrives. If the fallback's metrics differ, every line rewraps: buttons resize, headings move, text jumps under the reader's eye. That movement is Cumulative Layout Shift, and font swaps are a classic CLS source. The fix is not to abandon swap; it is to make the fallback occupy nearly the same box as the webfont.

## The four descriptors

Applied inside the fallback font's @font-face rule, these descriptors reshape the fallback to approximate the primary font:

- size-adjust: scales the fallback's glyph size by a percentage. The main lever: raise a small-x fallback so its text occupies the same space as the primary.
- ascent-override and descent-override: replace the fallback's ascent and descent with percentages of its em box, controlling where text sits in the line box.
- line-gap-override: usually set to 0% to stop the fallback adding its own leading.

They affect only that @font-face, so you create a dedicated fallback face, for example a family named "Inter-fallback" wrapping Arial with adjusted metrics, placed first in the stack after Inter.

## Computing the values

The arithmetic: for each metric, the override percentage is the primary font's metric divided by the fallback's metric. Concretely, if the primary has ascent 0.969 em and the fallback 0.905 em, ascent-override is about 107%. Size-adjust compares the primary's glyph proportions (cap height and x-height matter most) to the fallback's.

Doing this by hand for every pair is error-prone, so automate:

- Fontaine: an npm tool that inspects your fonts and generates metric-adjusted fallback @font-face declarations automatically.
- next/font: Next.js's font component generates metric-compatible fallbacks and self-hosts fonts as part of its output; if you are on Next.js, this is largely solved for you.
- Wakamai Fondue reports a font's ascent, descent, and suggested size-adjust values for common fallbacks, which is enough to hand-roll one declaration when tooling is overkill.
- capsize addresses the same problem from the other side: trimming the extra space above cap height and below baseline so chosen line-heights are exact; it pairs well with metric-adjusted fallbacks.

## Choosing the fallback font

- Pick a system font with broadly similar proportions to the primary: Arial or Helvetica for neo-grotesques, Georgia for transitional serifs, Segoe UI on Windows-targeted stacks.
- system-ui is unpredictable: it resolves differently per OS, so a fallback tuned for it is only correct on some machines. A named, metric-stable font makes the tuning meaningful.
- Tune one fallback per primary face, not one per page. The overrides live in the fallback's @font-face and are reused everywhere.
- For multilingual content, remember the fallback only matches Latin metrics; complex scripts fall to their own system fonts, and their swap behavior is governed by line-height headroom rather than these descriptors.

## Verifying the result

- DevTools: render the page, then block the font request (Network request blocking) and compare screenshots; the pre-swap and post-swap layouts should differ by a few pixels at most.
- Record CLS in the field (web vitals) before and after adding adjusted fallbacks; font-swap CLS should drop to near zero.
- Check heading sizes especially: large text magnifies metric differences, so the headline is where residual shift shows.
- Re-verify when either font changes: a primary font upgrade invalidates the computed overrides.

## Interaction with everything else

- Metric-adjusted fallbacks make font-display: swap safe on content pages; without them, swap on slow connections reflows visibly.
- They do not fix glyph-level differences: the fallback's letterforms differ, and readers see a style change on swap; that is acceptable, layout stability is the goal.
- They are a webfont-era technique: if you serve system fonts only, there is nothing to adjust.
- Subsetting interacts: adjusted fallbacks are declared against your fallback face regardless of subsets, but keep unicode-range on the primary consistent so the fallback is used only during the gap.
- Browser support for the descriptors is good in current engines; degrade harmlessly elsewhere, since a non-supporting browser just behaves as before.

## Common mistakes

- Tuning size-adjust while ignoring ascent-override, so text lines sit visibly higher in the fallback and every line box moves on swap.
- Applying override descriptors to the primary font's @font-face; they belong to the fallback.
- Using system-ui as the tuned fallback, making the tuning correct only on some platforms.
- One global fallback for a multi-family system: each primary face deserves its own adjusted fallback.
- Assuming CLS tooling will attribute the shift clearly; font swaps often get lumped into "unknown" sources, so verify with request blocking rather than trusting labels.
- Setting line-gap-override nonzero and re-introducing the leading differences you were removing.

## Decision rules

- Any webfont with font-display: swap on a content page: metric-adjusted fallback is mandatory, not optional polish.
- App shells where fonts arrive with the first bundle: still add them; cold caches exist.
- Multi-family brand systems: one adjusted fallback per family, generated by tooling and committed with the fonts.
- When a font upgrade ships: regenerate overrides as part of the upgrade checklist.
- If shifts persist after tuning: the fallback font is too different in width; pick a closer-natured fallback before chasing decimals.

## Worked example

A blog body face is Inter with Arial as the system fallback. Build the adjusted fallback face step by step.

1. Measure both files (Wakamai Fondue, or ttx on the OS/2 and hhea tables): ascent, descent, cap height, x-height, per em.
2. Compute ratios in em units. The figures from "Computing the values" above: ascent 0.969 divided by 0.905 gives a ratio of about 1.07, so ascent-override: 107%. Run the same division for descent. Size-adjust compares glyph proportions: if the fallback draws small relative to the primary, raise it by the ratio of x-heights.
3. Declare a dedicated face that never downloads; it only carries overrides:

```
@font-face {
  font-family: "Inter-fallback";
  src: local("Arial");
  /* size-adjust: measured x-height ratio, usually near 100% */
  ascent-override: 107%;
  /* descent-override: primary descent divided by fallback descent */
  line-gap-override: 0%;
}
```

4. Place the face directly after the primary in every stack:

```
body { font-family: "Inter", "Inter-fallback", Arial, sans-serif; }
```

The browser uses Inter-fallback only while Inter loads; once the real face is available it wins the match.
5. Verify: block the woff2 request in DevTools (Network request blocking), reload, screenshot; unblock, screenshot; overlay them. Line endings, button widths, and heading positions should not move. Then compare field CLS before and after.

Note on local(): the webfont-formats reference warns against local() sources for primary faces, because an installed copy bypasses your version control. A metric-adjusted fallback is the accepted exception: the face exists only to host overrides for a font the user already has, and nothing is served from your origin.

## Code notes

A minimal CLS logger that attributes shifts without recent user input:

```
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (!entry.hadRecentInput) {
      console.log("layout-shift", entry.value, entry.startTime);
    }
  }
}).observe({ type: "layout-shift", buffered: true });
```

Generation: Fontaine (npm) emits adjusted fallback declarations for each font declared in a bundler build; next/font does the same inside Next.js. Hand-rolling is fine for one or two families; automate once the count grows.

Verification procedure (DevTools, not CI): block requests matching woff2, capture document height and a full-page screenshot, unblock, capture again, diff. Movement above a pixel or two at body sizes means a ratio is off; large headings magnify the error, so check them first.

To attribute a field shift to the swap specifically, pair the layout-shift log with font load timing: shifts that cluster at the moment a font finishes loading and are absent while it is blocked are font-swap shifts.

## Quick reference

| Descriptor | Unit | Reshapes | Typical role |
| --- | --- | --- | --- |
| size-adjust | percentage | glyph scale of the fallback | match width and apparent size |
| ascent-override | percentage of em | top of the line box | match vertical position |
| descent-override | percentage of em | bottom of the line box | match vertical position |
| line-gap-override | percentage of em | extra leading | usually 0% |

- All four are @font-face descriptors: they apply to one face, inherit to nothing, and belong on the fallback, never the primary.
- They fix metrics, not letterforms: readers still see the fallback's shapes until the webfont arrives.
- One adjusted fallback per primary face, not per page: the overrides are reused wherever the stack appears.
- A computed size-adjust far from 100% usually means the wrong fallback pair; switch the fallback font before tuning decimals.

## Common failure modes

- Layout looks stable and CLS is low, but headings still "jump": antialiasing and rendering differences between the two faces, not layout shift. Metric overrides cannot remove a rendering artifact, and no Core Web Vitals metric measures it.
- Overrides written on the primary's @font-face: the primary's real metrics get clobbered and the fallback stays untouched. They belong only on the fallback face.
- A fallback tuned once, then the primary font upgraded a year later: every ratio is stale. Tie override regeneration to font upgrades, not to CSS reviews.
- Glyphs visibly larger or smaller during load even though lines do not move: size-adjust compensated scale but fixed line-height in CSS pins the boxes. Match x-height ratios rather than em size.
- Page still shifts with font-display: optional: the shift source is not the font; audit images, ads, and late CSS before blaming typography.
- Overrides silently ignored: the fallback declaration was duplicated later in the cascade (last matching @font-face wins) or placed inside a media query that did not match at load.
- Numerals-only surfaces (tickers, timers, price badges) tuned with letter metrics: digit advance widths dominate there; tune against figure strings instead.
- Two-line buttons and badges shift more than paragraphs because each line rewraps independently; verify interactive components with their real fixed strings, not just body copy.

## Cross-references

- [Font display strategies](font-display-strategies.md)
- [Font-face and CSS](font-face-and-css.md)
- [Mixed script fallbacks](../scripts/mixed-script-fallbacks.md)
- [Testing typography accessibility](../accessibility/testing-typography-accessibility.md)

Compiled 2025 as part of the Fontlore project.
