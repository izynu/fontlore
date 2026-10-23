# Testing Typography Accessibility

What this reference covers: A practical audit procedure for typography decisions: the exact checks to run (zoom, font-size overrides, text-spacing overrides, contrast, forced colors), the tools to run them with, and how to record results so fixes happen. Automation catches a third of the issues; this file is about the human half.

## The audit in one list

Run these on key templates (home, article, form, table, checkout, mobile breakpoint) before sign-off:

1. 200 percent browser zoom: no loss of content or function (WCAG 1.4.4).
2. 400 percent zoom at 1280 px viewport: reflows to one column, no horizontal scrolling (1.4.10).
3. Browser default font size raised to 24 px (or text-only zoom in Firefox): every text element scales (rem check).
4. Text-spacing overrides applied (1.4.12 bookmarklet or snippet): nothing clips or overlaps.
5. Contrast audit on real rendered pairs, including states (1.4.3, 1.4.11).
6. Grayscale check: hierarchy and links survive without color (1.4.1).
7. Forced-colors / high-contrast mode: content remains usable; backgrounds and text remap sanely.
8. Keyboard-only pass at high zoom: focus indicators visible and not clipped.
9. Screen reader spot check with correct lang attributes: pronunciation and structure sane.

## Tools for each check

- Zoom and reflow: browser zoom plus the devtools device toolbar set to a 320 px width; screenshot at 400 percent for the record.
- Font-size overrides: browser settings (raise default size) and Firefox text-only zoom; both in one pass.
- Text spacing: the alphagov text-spacing bookmarklet, or a console snippet setting line-height 1.5em, letter-spacing 0.12em, word-spacing 0.16em, and paragraph margin 2em on all elements. Apply globally, including embeds.
- Contrast: browser extensions and built-in devtools contrast checkers for rendered pairs; token-level scripts for CI; manual sampling over images and gradients.
- Grayscale: devtools rendering emulation (or OS grayscale filters); the point is color-independence of hierarchy.
- Forced colors: Windows High Contrast or the devtools forced-colors emulation; check that text tokens and focus styles remap.
- Screen readers: VoiceOver (macOS/iOS), NVDA (Windows), TalkBack (Android); verify lang switching on multilingual content, not full navigation testing.

## What to record

- Per template: pass/fail per check, with screenshots for failures. Screenshots of the 400 percent reflow and the spacing-override state communicate to stakeholders faster than any writeup.
- Per component library: the component list with its smallest supported text size and its contrast pair tokens; this becomes the design system's accessibility appendix.
- Open issues filed with the exact reproduction (zoom level, override state, viewport), because these failures are configuration-specific and "works on my machine" arguments are common.

## Common failure patterns to expect

- Fixed-height cards clipping text under spacing overrides; the single most common 1.4.12 failure.
- px-locked labels that ignore browser font-size changes while headings scale.
- Focus indicators invisible at 200 percent because they are 1 px outlines on 1 px layouts, or clipped by overflow hidden.
- Placeholder-only form labels at low contrast.
- Tables that scroll horizontally at 400 percent without a logical alternative reading order.
- Multilingual pages failing everything above faster than English (taller scripts + overrides compound).

## Involving real users

Automated and self-testing covers mechanics; real low-vision and dyslexic readers catch usability issues mechanics miss:

- Recruit a handful of participants who use zoom, magnification, or spacing overrides daily; a 30-minute session on your key flows is worth more than another checklist pass.
- Ask them to change their settings first, then use the product; observe where the layout fights their settings.
- Compensate participants; treat findings as design defects, not user error.
- Keep a standing invitation: one recurring session beats an annual audit for catching regressions.

## Making it routine

- Fold checks 1-7 into the design-review template as checkbox items with screenshot slots; checks 8-9 into pre-merge QA for changed templates.
- Automate the token-level contrast check and the rem-only lint in CI.
- Re-run the full audit on: new templates, type system changes, dark mode additions, new language launches.
- Version the audit itself; record which tool versions and browser builds were used so failures are reproducible later.
- Keep the corpus and the snippet in the repo next to the tests; the audit is a fixture, and fixtures get version control.
- Pair every new component with its override-state screenshot in the pull request; review without the artifact is rubber-stamping.

## Common mistakes

- Running the audit on polished marketing pages only; forms, tables, and checkout fail more and matter more.
- Testing overrides by setting them "a bit", rather than at the exact 1.4.12 values; the criterion defines the numbers.
- Trusting a contrast extension's verdict on gradient or image backgrounds; those need sampled measurement.
- Treating the audit as a release gate only; design-stage checks catch the architecture problems (fixed heights, px type) while they are cheap.
- Never testing forced-colors mode, then discovering the product is a gray-on-gray wall for its users.
- Recording results as prose without screenshots; unverified claims do not drive fixes.
- Treating a passed template as permanently passed; every redesign, dark mode, and language launch resets the clock.

## Decision rules

- Any new component: passes checks 1-7 in isolation before it enters the library.
- Any failure on a shipped template: file with screenshot and reproduction settings; block the release only for criteria failures (contrast, reflow, spacing), not for polish.
- Multilingual launch: re-run the full audit on the new language's pages; scripts with tall demands fail first.
- Time-boxed audit: prioritize forms, tables, checkout, and one long-form template; that covers most real reading and most real failures.

## Code notes: the exact override snippet

Save as a snippet in DevTools and toggle per template:

```css
/* WCAG 1.4.12 values, verbatim */
*, *::before, *::after {
  line-height: 1.5 !important;
  letter-spacing: 0.12em !important;
  word-spacing: 0.16em !important;
}
p { margin-bottom: 2em !important; }   /* paragraph spacing: 2x font size */
```

Notes for honest results: apply to all elements including embeds; combine with 200 percent zoom for the compound test; remember the values are multiples of each element's own font size, which is why em is correct and px is not.

The alphagov bookmarklet does the same job portably; the snippet's advantage is that it lives in version control next to the tests.

## Comparison table: the nine checks and their tools

| Check | Criterion | Tool | Automation ceiling |
| --- | --- | --- | --- |
| 200 percent zoom | 1.4.4 | Browser zoom, manual pass | None; behavioral |
| 400 percent reflow | 1.4.10 | DevTools 320 px width, manual pass | None |
| Font-size preference | 1.4.4 | Browser settings, Firefox text-only zoom | None |
| Spacing overrides | 1.4.12 | Bookmarklet or snippet | None |
| Rendered contrast | 1.4.3, 1.4.11 | DevTools pickers, extensions | Partial; states and images need humans |
| Color independence | 1.4.1 | Grayscale emulation or print | None |
| Forced colors | 1.4.11 territory | Windows High Contrast, DevTools emulation | None |
| Keyboard at zoom | 2.4.7 and related | Manual keyboard pass | None |
| Language switching | 3.1.1, 3.1.2 | VoiceOver, NVDA spot check | None |

One of nine is partially automatable; that is why this file exists next to the token linters.

## Field notes: an afternoon audit schedule

A realistic single-day pass over four templates, run by one person with a second for triage:

- 09:00: environment setup; bookmarklet installed, forced-colors emulation verified, screenshot tooling ready.
- 09:30: home page; zoom, reflow, spacing, grayscale; file as you go.
- 10:30: sign-up or checkout form; contrast of labels, errors, placeholders; keyboard at zoom.
- 11:30: dashboard or table template; the worst-offender class; cell heights, truncation, tabular checks.
- 13:30: long-form template; measure, leading, overrides, forced colors.
- 14:30: mobile browser rerun of everything that failed on desktop; Safari finds its own set.
- 15:30: triage; every failure gets component, criterion, screenshot, and reproduction settings.
- 16:00: report-out; the two or three architecture-level fixes named, with owners.

Ten working hours finds the bulk of what matters on a mature codebase; the point of the schedule is that it ends with filed artifacts, not vibes.

## Worked example: one finding, end to end

Finding: the checkout summary card clips the delivery-instructions text under spacing overrides.

1. Reproduce: bookmarklet on, 375 px viewport, screenshot showing the fourth line cut mid-word.
2. Classify: 1.4.12 failure, component class "summary card", architecture cause (fixed height set to keep the grid even).
3. File: ticket with screenshot, reproduction settings, and the component name; not "spacing looks broken on checkout".
4. Fix: min-height on the card, height removed, grid rows allowed to grow; the default-settings visual barely changes.
5. Verify: overrides again, plus 200 percent zoom, plus the longest real instruction text the form allows.
6. Promote: the component test suite gains an override-state screenshot so the class of bug cannot return silently.

The loop from reproduce to promote is the whole point; a finding that ends at "fixed the page" leaves the component armed to fail again elsewhere.

## Cross-references

- [WCAG baseline for type](wcag-baseline-for-type.md)
- [Text spacing criterion](text-spacing-criterion.md)
- [Low vision and zoom](low-vision-and-zoom.md)
- [Accessibility audit workflow](accessibility-audit-workflow.md)

Compiled 2025 as part of the Fontlore project.
