# Low Vision and Zoom

What this reference covers: How low-vision users actually enlarge and read web content, the WCAG zoom and reflow requirements, and the sizing and layout practices (rem-based type, ch-based measures, zoom-tolerant components) that keep a page intact from 100 to 400 percent. Zoom failures are layout failures, not font failures, which is exactly why typographers must own them.

## The requirements

- WCAG 1.4.4 Resize Text (AA): text can be resized up to 200 percent without loss of content or functionality. Browser zoom satisfies this if the layout survives it.
- WCAG 1.4.10 Reflow (AA): at 320 CSS px width (1280 px viewport at 400 percent zoom), content reflows into one column with no two-dimensional scrolling. This is the criterion that actually breaks designs.
- Related: 1.4.11 Non-text Contrast covers focus indicators and input borders, which become the primary navigation aids at high zoom; and 1.4.12 Text Spacing means overrides must not clip content.

## How the zoom stack works

Users enlarge text through several mechanisms, and your CSS must cooperate with all of them:

- Browser zoom: scales the CSS px; well-built layouts simply get bigger. This is the default behavior and the baseline to protect.
- Text-only zoom (Firefox): scales text relative to rem; rem-based sizes grow, px sizes do not. Hardcoding px locks those elements against this preference.
- Browser default font size: changes the rem base. If all type is in rem, a user raising the default grows the whole type system coherently.
- OS-level display scaling and screen magnifiers: work outside the page, but reveal the same tolerance requirements (nothing depends on exact pixel positions).
- Windows display scaling at 125 and 150 percent is the common real-world configuration, not 100 percent; text hinting and layout behave differently there, so those are the settings to test.

## Sizing practices

- Type in rem exclusively, including components, so one preference scales the system. Exceptions are rare and deliberate.
- Spacing and dimensions in rem or percentages where they wrap text; borders and decorative hairlines may be px.
- Minimum body size 16 px equivalent (1rem) for content; UI labels may go to 13 to 14 px but must pass contrast and stay zoom-scalable.
- Avoid text-size-adjust hacks and user-scalable=no in the viewport meta; disabling zoom fails 1.4.4 outright on mobile.
- Fluid type with clamp() is fine if the bounds are in rem, so user font-size preferences still move the result; px bounds freeze the type and break the preference.
- Set scroll-margin-top in rem for anchored headings, so in-page links survive a header of any size.
- Prefer real text over images of text at every size; images of text neither reflow nor respect preferences (WCAG 1.4.5 covers that rule itself).
- When a component must hold a fixed aspect (a badge, a logo tile), lock the box, not the text: the text inside still scales, or the box grows.

## Layout practices for reflow

- One-dimensional scrolling only: at 400 percent zoom, a two-column marketing page must become one column, tables must scroll or collapse, and sticky elements must not consume the viewport.
- max-width on text containers in ch (a measure of the digit width) or rem, not px, so the comfortable measure survives zoom.
- Media queries that restructure at narrow widths serve zoomed desktop users identically to phone users; test desktop at 400 percent zoom, not just a phone emulator.
- Fixed-position headers shrink or auto-hide at high zoom; a 200 px header on a 320 px viewport makes every page a scrolling exercise.
- Modals, dialogs, and toasts must be fully visible and scrollable at 400 percent; fixed-size dialogs are a classic reflow failure.
- Data tables at 400 percent may scroll horizontally (they are excepted from reflow), but the scroll container needs keyboard focus and a label; a table trapped in an unfocusable div is a found bug.
- Run the sticky-element inventory at every review: headers, footers, cookie banners, chat bubbles, "back to top" links; each one is a viewport thief until proven otherwise.

## Testing method

1. Desktop browser, 400 percent zoom on a 1280 px viewport (equivalent to 320 CSS px): no horizontal scrolling, no clipped content, everything operable.
2. 200 percent zoom at typical laptop width: no loss of function, no overlapping.
3. Raise the browser default font size to 24 px: the whole type system scales if rem-based; anything that stayed fixed is a bug.
4. Firefox text-only zoom at 150 and 200 percent: px-locked text stands out immediately.
5. Mobile pinch zoom with the viewport meta sane: zoom enabled, content reflows.
6. Keyboard navigation at high zoom: focus indicators visible (1.4.11), no focus lost off-screen, nothing fully obscured by sticky elements (2.4.11).

## Common mistakes

- The viewport meta with user-scalable=no or maximum-scale=1, usually added by a framework default or to fix an iOS input-zoom quirk; fix the root cause (input font-size below 16 px triggers iOS auto-zoom) instead of blocking zoom.
- px everywhere "for precision", producing a page that ignores the browser font-size preference entirely.
- clamp() with px bounds, which caps user preferences invisibly.
- Testing zoom only in a phone emulator at 100 percent; the failures live at desktop 400 percent.
- Sticky headers and cookie banners with px heights that eat the viewport at high zoom.
- Carousels and tabs whose arrows or dots become untouchable or invisible at 400 percent.

## Decision rules

- New layout: pass the 400 percent desktop reflow test before visual polish; reflow failures are architecture, and late fixes are rewrites.
- Any px font-size in a component: convert to rem or document why the element must not scale (almost never a real reason).
- A stakeholder asks to "disable zoom": refuse and fix the iOS input size; blocking zoom is an accessibility failure and a WCAG failure.
- Fluid type: rem-bounded clamp() only, with the minimum at or above the component's accessible size.
- Design review artifact: include one screenshot of the page at 400 percent zoom; it communicates more than any checklist.

## Code notes: zoom-tolerant patterns

```css
/* Fluid type with rem bounds: user preference always moves it */
h1 { font-size: clamp(1.75rem, 1.2rem + 2.5vw, 3rem); }

/* Sticky header stands down when space runs out */
@media (max-width: 40rem) {
  .site-header { position: static; }
}

/* Anchored headings survive a header of any size */
:target { scroll-margin-top: 5rem; }

/* Dialogs scroll instead of clipping */
.dialog {
  max-width: min(40rem, 100% - 2rem);
  max-height: 85vh;
  overflow-y: auto;
}

/* Measure in ch so the comfortable line length survives zoom */
.prose { max-width: 66ch; }
```

Scrollable tables need keyboard access to their scroll container:

```html
<div class="table-wrap" role="region" aria-label="Pricing detail" tabindex="0">
  <table>...</table>
</div>
```

```css
.table-wrap { overflow-x: auto; }
.table-wrap:focus-visible { outline: 2px solid var(--focus); }
```

## Quick reference: units cheat sheet

| What | Use | Why |
| --- | --- | --- |
| Font sizes | rem | Scales with the user's base size |
| Line height | unitless | Scales with whatever font size wins |
| Measures | ch or rem | Comfortable line length survives zoom |
| Component padding | rem or em | Proportions hold as text grows |
| Layout widths | percent, min(), max(), clamp() with rem bounds | One-dimensional reflow at 320 px |
| Borders, hairlines, radii | px allowed | Decorative; nothing textual depends on them |
| Viewport units | cautiously, in clamp() middle terms only | Raw 100vw text ignores user preferences |

The one-line version: if a value participates in text layout, it is relative; if it is decoration, px is fine.

## Worked example: the header that ate the viewport

A marketing site kept a 96 px sticky header and a 64 px cookie banner on screen at every width. At 400 percent zoom the 1280 px viewport became 320 CSS px; header plus banner consumed half of it, and every scroll was two fingers of travel. The fixes, in order:

- The cookie banner moved to the bottom as a normal-flow block that dismisses; it stopped stealing the top of the viewport.
- The header switched to static below 40rem and shrank (padding, not font size) above it.
- The in-page anchor offset, previously a hardcoded px value, became scroll-margin-top in rem so headings are not hidden under whatever header remains.
- The hero heading was clamp() with px bounds and sat frozen at 44 px at high zoom; rem bounds restored scaling.

Re-test at 400 percent: one column, one scrolling dimension, focus always visible. The page needed no visual redesign at 100 percent.

## Field notes: what magnifier users hit

Screen magnification (Windows Magnifier, ZoomText, macOS zoom, iOS Zoom) behaves differently from browser zoom, and the failures differ:

- Magnifier windows and lenses follow focus and the pointer; hover-only menus and tooltips vanish between input and display.
- Full-screen magnification at 200 to 400 percent is effectively the reflow test; the same one-column requirement applies.
- Parallax and scroll-jacking make the magnified window lose position; keep scrolling native.
- Custom cursors and faint focus indicators are magnified too: make focus fat and obvious.
- Content revealed only on hover has no equivalent for a magnifier user working a keyboard; everything interactive needs focus parity.
- Text inside canvas or images does not reflow under any magnifier; prefer real text everywhere.

Test one flow with Windows Magnifier docked at 300 percent; the bugs found in ten minutes will reshape your opinion of hover patterns.

## Cross-references

- [WCAG baseline for type](wcag-baseline-for-type.md)
- [Dynamic type and preferences](dynamic-type-and-preferences.md)
- [Testing typography accessibility](testing-typography-accessibility.md)
- [Fallback metrics and CLS](../technical/fallback-metrics-and-cls.md)

Compiled 2025 as part of the Fontlore project.
