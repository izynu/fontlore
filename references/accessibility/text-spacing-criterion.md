# Text Spacing Criterion

What this reference covers: WCAG 1.4.12 Text Spacing: exactly what the criterion requires, the CSS architecture that makes overrides safe, how to test with bookmarklets and devtools, and the component patterns that fail. The criterion is about user overrides, not about your design's chosen spacing, and that distinction changes how you build.

## What 1.4.12 actually requires

WCAG 1.4.12 (Text Spacing, AA) says: no loss of content or functionality when users set these properties:

- Line height to at least 1.5 times the font size.
- Paragraph spacing to at least 2 times the font size.
- Letter spacing to at least 0.12 times the font size.
- Word spacing to at least 0.16 times the font size.

The user (via a browser extension, user stylesheet, or assistive tech) applies these overrides globally. Your job is that the page still works: nothing clipped, nothing overlapping, no information lost. The criterion does not mandate your design use those spacings by default.

## Why pages fail

Failures come from three CSS habits:

- Fixed heights: text inside height-fixed cards, buttons, or line-clamped containers. Doubling line height overflows the box and clips or overlaps.
- Pixel units: line-height: 20px does not scale with user font-size or spacing overrides the way unitless values do.
- Overflow hidden on text containers: combined with the above, overrides silently hide content with no visual cue.
- Decorative z-index sandwiches: absolutely positioned elements that sit above text and collide once line boxes grow.
- Scroll-snap and carousel tracks with fixed item widths: spacing overrides widen text inside fixed-width slides.

A subtler failure: absolute-positioned overlays sized to measured text that no longer match once spacing changes, and data tables with cell heights set in px.

## CSS architecture that passes

- Use unitless line-height (1.5, not 24px) so it scales with any font size.
- Size text in rem; set heights with min-height, padding, or intrinsic sizing, never fixed height on text-bearing elements.
- Prefer max-height with visible overflow for clamping, or better, line-clamp with an accessible full-text path.
- Do not set letter-spacing on long body text; short tracked labels can keep their tracking, but ensure the component has room to grow.
- Leave enough horizontal room in components (buttons, nav items, chips) that 0.12em letter and 0.16em word spacing cannot force wrapping into broken states; test with the override applied, not imagined.
- Vertical rhythm components (list rows, form rows) should tolerate line boxes roughly doubling without breaking their layout.
- Data tables get horizontal overflow with keyboard access instead of px cell heights; the reflow rules cover the reading-order requirements.
- Put the override snippet in version control next to the component tests; the numbers are the criterion, so they are code, not tribal knowledge.

## Testing method

1. Install or bookmark a text-spacing bookmarklet (the UK government digital service's alphagov text-spacing bookmarklet is the standard tool) or write a DevTools snippet applying the four property overrides to all elements.
2. Apply it to every key template: home, content page, form, table, checkout, mobile breakpoints.
3. Look for: clipped text, overlapping elements, buttons that cut off labels, truncated table cells, tooltips and badges that collapse.
4. Test with browser font size raised as well (200 percent zoom is a separate criterion); the two overrides compound.
5. Record failures with screenshots per component; fix CSS architecture, not the bookmarklet.

## Interaction with your typography choices

- Tight leading (1.15-1.2) display styles survive overrides fine because the user override replaces them; nothing to do there, but verify headings do not collide with adjacent elements when 1.5 applies.
- Complex scripts raise the stakes: Thai, Devanagari, and Arabic text needs more vertical room by default; when overrides add more, components designed at Latin-tight spacing break first in those languages. Test the spacing override on localized pages, not just English.
- Tabular data: with letter and word spacing overridden, columns widen; horizontal scroll is acceptable for tables under reflow rules if a logical reading order survives.
- Buttons and badges with uppercase micro-labels: extra letter spacing can double their width; give them flexible width.

## Common mistakes

- "Fixing" the criterion by designing everything at 1.5 line height and calling it done; the audit still applies user overrides and finds the fixed-height cards.
- Applying overrides only to paragraph text in the test snippet and missing buttons, nav, and form labels, which are where clipping happens.
- Ignoring third-party embeds (chat widgets, forms) that fail overrides; they are in scope for the page.
- Treating overflow-hidden truncation as acceptable when the truncation itself hides meaning under overrides; provide a real full-content path.
- Testing spacing overrides only on desktop Chrome; mobile Safari and Firefox extend/zoom behaviors differ.
- Fixing a failure by editing the override snippet's values; the values are the standard, and changing them to make a component pass is how 1.4.12 gets quietly abandoned.

## Decision rules

- Any component containing text: it must survive the four overrides at your smallest supported breakpoint; that is a design-review gate, not a pre-release nicety.
- Fixed height on a text container: treat as a bug in review, even when it passes visually in default conditions.
- Localized product: run the spacing override on the heaviest script you ship (Thai, Khmer, Devanagari) before sign-off.
- If a stakeholder design requires fixed heights: propose min-height with the same visual result; it passes both.
- New component library: add the spacing-override render to the component test suite (a screenshot pass with overrides applied).

## Code notes: override-safe CSS patterns

Text containers grow; clamps keep a visible escape hatch:

```css
/* Intrinsic sizing: never height on text-bearing elements */
.card { padding: 1rem; }

/* Line clamp with a real full-content path elsewhere */
.teaser {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Tracked labels keep room to grow */
.chip { padding-inline: 0.75rem; min-width: max-content; }
```

The audit snippet itself, using the exact criterion values:

```css
/* WCAG 1.4.12 overrides, verbatim */
* {
  line-height: 1.5 !important;
  letter-spacing: 0.12em !important;
  word-spacing: 0.16em !important;
}
p { margin-bottom: 2em !important; }   /* paragraph spacing: 2x font size */
```

Note the em units: each override is a multiple of the element's own font size, which is how the criterion is written; px approximations test something else.

## Audit checklist: the 1.4.12 sweep

Run with the overrides applied, at the smallest supported breakpoint, on real content:

- [ ] Navigation items and menus: no wrapped or clipped labels.
- [ ] Buttons, chips, badges: labels fully visible, no overlap with icons.
- [ ] Form labels, inputs, helper text: nothing clips; inputs grow with text.
- [ ] Cards and tiles: text visible, no overlap with footers or calls to action.
- [ ] Tables: cells wrap or scroll; no px cell heights anywhere.
- [ ] Tabs and pagination: labels fit; controls stay operable.
- [ ] Toasts, tooltips, dialogs: text visible and scrollable when taller.
- [ ] Hero and overlay text: no collision with images or buttons.
- [ ] Third-party embeds (chat, video, forms): same checks; they are in scope.
- [ ] Localized pages: run the sweep again on the tallest script you ship.
- [ ] Combinations: overrides plus 200 percent zoom; the two compound.

## Worked example: the pricing cards that clipped

A three-column pricing grid shipped looking immaculate at default settings. The audit applied the overrides and found:

- The plan name, clamped to one line, pushed its overflow into the price below; the clamp hid the overflow but the layout assumed one line.
- Feature list rows were 24 px tall with height instead of padding; the fourth feature overlapped the fifth.
- The call-to-action label wrapped and clipped: fixed height plus white-space: nowrap.

Fixes, in order of cost: the plan name got a second clamp line plus a min-height; row heights became padding plus line-height; the button grew with its content and dropped nowrap. Visual diff at default settings: nearly identical. Under overrides: everything visible. That asymmetry is the whole lesson; the fixed values were invisible debt that only the override test surfaced.

## Quick reference: where overrides bite first

Ranked by how often each element class fails the sweep in practice:

1. Fixed-height cards and tiles (height, not min-height).
2. Buttons and chips with nowrap labels.
3. Data tables with px cell heights.
4. Line-clamped titles with no full-content path.
5. Absolutely positioned badges and flags pinned to measured text.
6. Tracked uppercase micro-labels in narrow navigation items.
7. Toast and dialog components sized to content at default spacing.
8. Third-party embeds, which no amount of your own CSS can fix.

Items 1 through 4 are CSS architecture; 5 through 8 are component design. None are font problems, and no font change will fix any of them.

## Cross-references

- [WCAG baseline for type](wcag-baseline-for-type.md)
- [Line length and reading](line-length-and-reading.md)
- [Testing typography accessibility](testing-typography-accessibility.md)
- [Web and SaaS interfaces](../applications/web-and-saas-interfaces.md)

Compiled 2025 as part of the Fontlore project.
