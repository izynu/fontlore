# Dynamic Type and Preferences

What this reference covers: How user-level font-size preferences work across browsers and operating systems, why prefers-reduced-motion is not a typography setting, and how to build fluid type that scales with preferences instead of against them. The theme: the user's size preference is an input to your type system, not a rival to it.

## Clearing up the motion confusion

prefers-reduced-motion is a motion media query: it exists so animation and transitions can be dialed back for users with vestibular sensitivities. It has nothing to do with typography; there is no standard "prefers larger text" media query to detect a user's size preference. Teams conflate these and end up with a motion toggle where a text-size control was needed. Treat motion and type as separate preference systems.

## Where size preferences live

- Browser default font size: changes the rem base; affects all rem-based CSS. This is the primary web mechanism and it must simply work.
- Browser text-only zoom (Firefox) and page zoom elsewhere: scale rendered text; page zoom scales layout px too.
- iOS Dynamic Type: system-level text sizes; native apps expose them via text styles. Safari on iOS does not directly map Dynamic Type to web rem, but Safari's own text size controls (and page zoom) do; iOS also auto-zooms form fields whose font-size is below 16 px, which is a preference mechanism in disguise.
- Reader modes and reading extensions (browser reader views, pocket-style extractors): they re-render your content in their own type system, which is a feature for your readers and a reason your semantic HTML must be clean.
- Android font size and display size settings: scale apps; Chrome on Android respects page zoom and font size settings similarly.
- Windows and macOS display scaling: change the effective CSS px density; pages built in rem and relative units scale cleanly.

Practical rule: honor the browser mechanisms (rem, zoom, sane inputs) and do not try to reimplement OS settings in JavaScript.

## Building a type system that respects preferences

- All type in rem; one --font-size-root or default 16 px base; never px for text.
- Fluid display type via clamp() with rem bounds: clamp(2rem, 1.2rem + 3vw, 4.5rem). The rem terms keep user preferences in the calculation; a px-based middle term or bounds would ignore them.
- Minimum floors: never set readable text below 16 px equivalent unless it is a deliberate, contrast-checked micro-label; and even then leave it scalable.
- Line-height unitless and tuned per role; when a user doubles sizes, leading scales automatically, keeping the same relative texture.
- Components must tolerate growth: buttons wrap or grow, not clip; nav items reflow; the text-spacing override test covers this from the other direction.
- If the design demands fixed proportions (a wordmark, a hero), lock only those elements, and let everything around them scale.
- Give every locked exception a written reason, an owner, and a revisit date; locked-without-a-date becomes permanently frozen.
- When testing preferences, also test with a user stylesheet or extension that forces a larger base; power-user setups are legal configurations, not edge cases.

## Fluid type without breaking preferences

The classic mistake: fluid scales that look great at 1440 px and become unreadably small on phones because the vw term dominates. Design the scale so:

- The preferred term (the vw part) is a nudge, not the whole size; the rem base term carries the bulk.
- The minimum is a readable size at the smallest supported viewport and the largest user preference.
- Test at three configurations: default preferences, maximum browser font size, and minimum supported viewport width with maximum font size. The third combination is where most fluid systems fail.
- Keep the fluid middle term rem-dominant; a vw-dominant term makes the design a slave to viewport width and a stranger to the user's preference.

## Detecting and offering control

- There is no reliable CSS media query for user font-size preference; do not fake one by measuring computed styles and rewriting everything.
- For products with long reading sessions (documentation, reader modes), offer an explicit text-size control that adjusts a root variable; it composes with, rather than replaces, browser mechanisms.
- Persist the choice; respect it across the product; document it as part of the design system rather than a page-local hack.

## Common mistakes

- px-based type with a rem only for headings, so user preferences scale headlines while body text stays frozen.
- clamp() built entirely in px, silently capping the preference.
- A "large text" toggle implemented by multiplying font sizes in JavaScript per element, fighting cascade and missing half the UI.
- Confusing prefers-reduced-motion with type preferences and shipping the wrong control.
- iOS input zoom bugs "fixed" with maximum-scale=1, which blocks zoom for everyone (see the zoom reference).
- Designing and reviewing only at default settings; preference-respecting behavior is invisible unless you change the settings during review.
- Shipping a text-size control that multiplies per-element sizes while the root stays capped by px media queries; the control fights itself.
- Building five size steps when three serve; more options is more QA surface, not more accessibility.

## Decision rules

- Every text element: rem or em, no exceptions without a written reason.
- Fluid scales: rem-bounded clamp, preferred term dominated by rem, tested with maxed user font size.
- Long-form reading surfaces: add an explicit size control; do not rely on users discovering browser settings.
- Form inputs: 16 px minimum font-size, which prevents iOS auto-zoom and serves the preference at once.
- Review artifacts: include screenshots at default and 200 percent font size; if the design looks wrong at 200 percent, the design is wrong.

## Code notes: preference-safe patterns

```css
/* The base: a percent root keeps the user's default and allows an in-product control */
html { font-size: 100%; }

/* Everything textual is rem; spacing that wraps text is too */
body { font-size: 1rem; line-height: 1.5; }
.button { font-size: 1rem; padding: 0.5rem 1rem; min-height: 2.75rem; }

/* Fluid display type: rem terms so preferences keep working */
.display-1 { font-size: clamp(2rem, 1.3rem + 2.5vw, 4rem); }

/* An in-product control shifts the base; browser preferences still compose */
html[data-text-size="lg"] { font-size: 112.5%; }
html[data-text-size="xl"] { font-size: 125%; }

/* Inputs: 16 px equivalent prevents iOS focus zoom and serves preferences */
input, select, textarea { font-size: 1rem; }
```

Unitless line-height travels with any size change. If a token system fixes leading in px next to px sizes, both are wrong together; convert the pair to rem plus unitless in one migration.

## Comparison table: preference mechanisms

| Mechanism | What it scales | Your obligation |
| --- | --- | --- |
| Browser default font size | The rem base | Type and text-wrapping spacing in rem |
| Browser page zoom | CSS px wholesale | Nothing fixed-height; reflow at 320 px |
| Firefox text-only zoom | rem-based text only | rem for text, or this preference finds nothing to move |
| OS display scaling | Effective CSS px density | Relative units throughout |
| iOS Dynamic Type | Native app text styles | Not the web's mechanism; Safari text size and zoom are |
| Reader modes and extensions | Re-render in their own type | Keep semantic HTML so extraction stays clean |
| In-product text-size control | Your root percentage | Tokens on rem; persist the choice |

No single mechanism reaches every user; the rem base plus page zoom plus a product control covers the realistic set without JavaScript reimplementations of any of them.

## Worked example: a docs site text-size control

A documentation site with long sessions added a three-step control in the sidebar:

- Implementation: a data attribute on html setting the root to 100, 112.5, or 125 percent; the choice persisted and applied pre-paint.
- Scope: everything, because the whole type system is rem; one rule changed one number.
- Composition: a user with the browser default font size raised still got their preference multiplied in; the control shifts the base, it does not replace it.
- Guards: line-clamped code snippets gained an "expand" affordance because lines grow; the sidebar became collapsible at the top step on small screens.
- Verification: the test matrix ran default, maxed browser preference, and xl control plus 200 percent zoom; the third cell is where the sidebar first broke.

Ship the control with the type tokens, documented as part of the design system, so the next product surface inherits it rather than reinventing a per-page toggle.

## Field notes: what breaks when sizes grow

Raise the browser font size to 24 px on any mature product and a predictable sequence appears:

- Navigation bars overflow first; items were sized to fit at 16 px with no wrap strategy.
- Buttons stay button-sized because their labels were px; the mismatch reads as a bug at a glance.
- Badge and chip text overflows its pill because the pill width was fixed.
- Modals with px max-widths clip the content that grew; max-width in rem or min() keeps them honest.
- Tables hold their layout while cell text wraps to three lines; row-height tokens absorb it only if they are rem-based.
- Hero headings, rem-based, grow beautifully while the px-tagged caption under them stays small; the hierarchy inverts.
- Tooltips anchored to measured text drift off their triggers.

Every one of these is a px value where a relative value belonged. The audit is one setting change and one scroll; the fix is usually one unit swap.

## Quick reference: the preference test matrix

Run every reading surface through these five configurations and keep a screenshot per cell:

| Configuration | How to set it | What must hold |
| --- | --- | --- |
| Default | Fresh profile, default font size | The design as intended |
| Browser font size raised | Default font size up two sensible steps (for example a 24 px base) | All text scales; nothing clips or overlaps |
| Page zoom 200 and 400 percent | Ctrl or Cmd plus | 1.4.4 holds at 200 percent; reflow holds at 400 percent on a 1280 px window (320 CSS px) |
| Text-spacing overrides | 1.4.12 bookmarklet: line-height 1.5x, paragraph spacing 2x, letter spacing 0.12x, word spacing 0.16x | No clipped or overlapping text |
| Max font size at 320 px width | The two stress settings combined | Body text stays readable and inside its container |

The last cell is the honest one: a fluid type scale that only works at desktop width and default preferences is a specimen, not a system.

## Audit checklist: preference respect

- [ ] Every font-size declaration is rem, em, or percent; grep for px font sizes and justify each hit in writing.
- [ ] clamp() bounds and preferred terms are rem-based; no px bounds anywhere.
- [ ] Root font-size is percent or rem, never a px value that caps the user base.
- [ ] Form controls at 1rem or larger (16 px equivalent) so iOS does not zoom inputs on focus.
- [ ] No maximum-scale or user-scalable=no in the viewport meta tag.
- [ ] Text containers sized by content (min-height at most); no fixed heights.
- [ ] Long-reading surfaces have an in-product text-size control that persists and applies before first paint.
- [ ] prefers-reduced-motion is wired only to motion, never to type.
- [ ] The five-configuration matrix above has current screenshots on file.

## Cross-references

- [Low vision and zoom](low-vision-and-zoom.md)
- [WCAG baseline for type](wcag-baseline-for-type.md)
- [Design tokens for type](../workflow/design-tokens-for-type.md)
- [Variable fonts and axes](../technical/variable-fonts-and-axes.md)

Compiled 2025 as part of the Fontlore project.
