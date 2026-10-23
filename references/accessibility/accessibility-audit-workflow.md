# Accessibility Audit Workflow

What this reference covers: A repeatable workflow for auditing typography accessibility as part of normal design review, not as an annual event. It defines stage gates, owners, artifacts, and the checklist each gate runs, so audit results feed back into tokens and components instead of piling up as tickets.

## Principles

- Audit early, at the artifact level: contrast pairs and type scales are design decisions; testing them on built pages finds them too late to fix cheaply.
- Automate the deterministic checks (contrast ratios, rem usage, fixed heights); human-test the behavioral ones (zoom, overrides, screen readers).
- Record outcomes as artifacts (screenshots, token audit reports, signed checklists), not meeting notes.
- Tie every failure to a fix location: a token, a component, a template, or content. "Somewhere in the page" fixes never ship.

## The four gates

Gate 1, design stage (owner: design lead):

- Type scale documented with roles, minimum sizes, and rem units; leading per role; measure targets for reading surfaces.
- Color tokens annotated with contrast results per intended size class; large-text exceptions listed explicitly.
- Hierarchy review: every tier differs by at least two of size, weight, case, position; grayscale mock passes.
- Multilingual plan: which scripts ship, which leading and measure rules they need, fallback stacks defined.

Gate 2, component review (owner: component author plus design reviewer):

- Component survives the four text-spacing overrides with no clipping (screenshot at override state).
- Component text scales with browser font-size preference (rem check); no px type without a written exception.
- Focus indicator passes 3 to 1 against both background themes and survives 200 percent zoom.
- Long-content behavior: wrap, clamp with full-content path, never fixed height.

Gate 3, template or release review (owner: QA plus a11y champion):

- Full template run of the typography audit: 200 percent and 400 percent zoom, font-size override, spacing bookmarklet, grayscale, forced colors.
- Contrast spot-check on real rendered pairs including states (hover, focus, disabled, placeholder).
- Keyboard-only pass at high zoom on the template's key tasks.
- Findings filed with screenshots and exact reproduction settings.

Gate 4, periodic audit (owner: a11y champion, quarterly):

- Re-run gate 3 on the top templates plus any changed since last audit.
- Token audit refresh: new pairs introduced since last cycle are tested and documented.
- Screen reader spot check with real content in each shipped language.
- Real-user session: at least one participant who uses zoom or spacing overrides daily, on a rotating template.
- Trend review: recurring failure classes get systematic fixes (a lint rule, a component change), not another ticket.

## The checklist (condensed)

- [ ] All type in rem; no px text without a documented exception.
- [ ] Unitless line-height; per-language leading rules present for shipped scripts.
- [ ] Text containers use min-height or intrinsic sizing; no fixed heights on text.
- [ ] 200 percent zoom: no loss of content or function.
- [ ] 400 percent zoom: one-column reflow, no horizontal scrolling.
- [ ] Browser font-size at 24 px: every element scales.
- [ ] 1.4.12 spacing overrides: nothing clips or overlaps.
- [ ] Contrast: every token pair passes for its size class, states included.
- [ ] Grayscale: hierarchy and links read without color.
- [ ] Forced colors: usable; tokens remap.
- [ ] Focus indicators: visible, 3 to 1, unclipped at zoom.
- [ ] lang and dir correct on the page and on translated segments.
- [ ] Screen reader: pronunciation switches with lang; structure sane.

## Artifacts and records

- The living checklist (this file, adapted per project) with dated sign-offs per gate.
- A screenshot archive: 400 percent reflow, spacing-override state, grayscale, forced colors, per template and release.
- The token contrast report generated from the design tokens, regenerated when tokens change.
- A decisions log for documented exceptions (px wordmark, locked hero), each with an owner and a revisit date.

## Common mistakes

- Treating the audit as a one-time certification; typography regressions arrive with every redesign and rebrand.
- Running only gate 3 (late testing) and skipping gate 1, so every finding is a rework of shipped CSS.
- Checklists without artifacts: "passed" claims nobody can reproduce.
- Auditing the marketing site while the app, docs, and emails (the surfaces users actually read) never get audited.
- No owner: gates exist only when someone specific runs them on a cadence.
- Letting exceptions pile up without revisit dates; a documented exception is a decision, an undocumented one is a bug.

## Decision rules

- A gate fails: the artifact goes back to the owning stage; gates do not pass "with known issues" for typography criteria (contrast, zoom, overrides).
- A component library change: gate 2 re-runs on changed components, not the whole library.
- A new language ships: gates 1 and 3 re-run for that language's templates before launch.
- Quarterly audit finds a repeat failure class: promote the fix to CI (lint, token check, component change) and delete the manual check that kept catching it.
- Stakeholder pressure to skip a gate: escalate with the most recent screenshot archive; artifacts beat arguments.

## Quick reference: WCAG 2.2 numbers the audit uses

| Criterion | Requirement | What the auditor does |
| --- | --- | --- |
| 1.4.3 Contrast (Minimum) | 4.5:1 for normal text; 3:1 for large text (24 px regular or 18.66 px bold and above) | Measure every token pair in its size class, states included |
| 1.4.6 Contrast (Enhanced) | 7:1 normal text; 4.5:1 large text | Only when the project committed to AAA |
| 1.4.11 Non-text contrast | 3:1 for focus indicators, icons, form borders | Test focus rings against both themes |
| 1.4.4 Resize text | 200 percent zoom with no loss of content or function | Zoom the browser, walk the key tasks |
| 1.4.10 Reflow | No two-dimensional scrolling at 320 CSS px width (400 percent zoom on a 1280 px window) | Narrow the window, check for horizontal scroll |
| 1.4.12 Text spacing | Survives line-height 1.5x, paragraph spacing 2x, letter spacing 0.12x, word spacing 0.16x | Apply the overrides, screenshot every component |
| 3.1.1 / 3.1.2 Language | lang on html; lang on parts in another language | View source, then the screen reader voice-switch test |
| 1.4.5 Images of text | Content text is real text, not rasterized type | Check banners, social cards, and hero art for baked-in copy |
| 1.4.8 Visual presentation (AAA) | Line width 80 characters or fewer; line spacing 1.5; paragraph spacing 1.5x line spacing | Only when AAA is committed; measure the reading surfaces |

Pin these numbers in the audit document itself. An audit finding that says "passes contrast" without the ratio and the criterion number is not reproducible, and an unreproducible pass is indistinguishable from an unchecked one.

## Audit checklist: the 1.4.12 sweep, step by step

The text-spacing criterion is the one typography fails most and teams test least. Run it identically every time:

- [ ] Apply the bookmarklet or user stylesheet with the four override values (line-height 1.5x, paragraph spacing 2x, letter spacing 0.12x, word spacing 0.16x).
- [ ] Walk every template at the override state, at default width and at 320 px.
- [ ] Screenshot every failure: clipped button labels, truncated card text, overlapped badges, nav items colliding.
- [ ] Classify each failure: fixed height, fixed width, line-clamp without an expand path, or absolute positioning. The class names the fix.
- [ ] File against the component, not the page; re-run the component in isolation after the fix.
- [ ] Record the sweep in the artifact archive with the date and the values used.
- [ ] Include hover, focus, and disabled states in the sweep; overrides expose state styling too.
- [ ] Re-run the sweep on the RTL variants of any template that ships right-to-left locales.
- [ ] Confirm the override stylesheet actually applies; a page rule with higher specificity silently voids the test.

A component that passes this sweep almost always survives larger user font sizes too, because the failure modes are the same: containers that assume exactly one line of text.

## Worked example: gate 3 on a checkout template

A checkout template (summary card, address form, payment panel) audited at gate 3:

1. Contrast: the placeholder text measured 2.9:1; placeholders are real text and were failed, then darkened in the input token. The disabled state sat at 2.6:1 and was recorded as a documented exception with the reasoning noted, since 1.4.3 exempts disabled controls.
2. Zoom: at 200 percent the promo-code input kept a 40 px fixed height and clipped its label; the fix converted the height to min-height in rem. At 400 percent the three-column summary reflowed to one column cleanly because the grid was already auto-fit.
3. Text spacing: with the overrides applied, the badge on the saved-card chip overlapped its label; the chip width was fixed in px and became padding plus intrinsic sizing.
4. Grayscale: the selected payment method was indicated by border color alone; grayscale made the two states identical. Added a check icon, which also satisfied 1.4.11 at 3.2:1.
5. Language: the address form contained a Welsh county name inside an otherwise English page; a lang="cy" span was added after the screen reader mangled it in the English voice.
6. Leading: the summary card's key-value rows were set at 1.3; raised to 1.4 through the role's leading token, which also resolved the row overlap the spacing sweep had found.

Four component fixes, one token change, and the artifacts (six screenshots, one token diff) filed with the release. The audit took two hours; the same template without the gate 1 artifacts would have taken a day and found less.

## Field notes: what audits actually find

Across repeated typography audits, the same failure classes recur, roughly in this order of frequency:

- Placeholder and disabled text below 4.5:1: the most common contrast failure, because placeholders are styled apologetically by default.
- Fixed heights on text containers: the single cause behind most 1.4.12 and zoom failures; one min-height conversion resolves whole families of tickets.
- Focus indicators that pass 3:1 on the light theme only: the light theme was tested, the dark theme shipped.
- Line-clamped content with no full-content path: the clamp is fine; the missing expand affordance is the failure.
- px type in components built before the rem rule: audits catch them where reviews did not, usually in legacy or vendor blocks.
- Missing lang on translated segments: pages pass every visual check and fail the first screen reader listen.
- Tracked all-caps labels colliding when word-spacing overrides land: letter-spacing baked into non-reflowing lockups is the cause.
- Data tables at 400 percent zoom: without a card-mode or scroll strategy, reflow fails first on the densest table, not on the prose.
- Small print and legal copy: set below 12 px and forgotten, then the first zoom test finds a wall of 10 px text that cannot grow without breaking its container.

None of these are exotic. Every one is a deterministic check that gate 2 should have caught, which is the standing argument for running gates 1 and 2 at all instead of only testing built pages.

## Cross-references

- [Testing typography accessibility](testing-typography-accessibility.md)
- [WCAG baseline for type](wcag-baseline-for-type.md)
- [Font governance and review](../workflow/font-governance-and-review.md)
- [Design tokens for type](../workflow/design-tokens-for-type.md)

Compiled 2025 as part of the Fontlore project.
