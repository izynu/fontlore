# WCAG Baseline for Type

What this reference covers: The WCAG 2.2 success criteria that constrain typography, separated into what a font choice can influence and what it cannot. The goal is a shared baseline for designers and engineers: know which requirements live in CSS, which live in font selection, and which live in neither.

## The criteria that touch typography

- 1.4.3 Contrast (Minimum), AA: text contrast at least 4.5 to 1; large text (at least 24 px, or 18.66 px bold) at 3 to 1.
- 1.4.6 Contrast (Enhanced), AAA: 7 to 1, or 4.5 to 1 for large text.
- 1.4.1 Use of Color: color cannot be the only visual means of conveying information; hierarchy and status need more than hue.
- 1.4.4 Resize Text, AA: text resizes to 200 percent without loss of content or functionality.
- 1.4.10 Reflow, AA: at 320 CSS px width (equivalent to 1280 px at 400 percent zoom), content reflows without two-dimensional scrolling.
- 1.4.11 Non-text Contrast, AA: UI components and graphical objects need 3 to 1; this covers focus indicators, icons, and borders around inputs.
- 1.4.12 Text Spacing, AA: user agents must be able to override line height, paragraph spacing, letter spacing, and word spacing without breaking content.
- 1.4.8 Visual Presentation, AAA: among other settings, line length at most 80 characters and line spacing at least 1.5.
- 3.1.1 and 3.1.2 Language of Page and Parts: lang attributes so screen readers pronounce content correctly.
- 1.3.1 Info and Relationships: headings, lists, and emphasis must be real structure, not styled paragraphs.
- 2.5.8 Target Size (Minimum), AA (new in 2.2): pointer targets, including text buttons and links, at least 24 by 24 CSS px.
- 2.4.11 Focus Not Obscured (Minimum), AA (new in 2.2): sticky headers, footers, and banners must not fully hide the focused element.

## What font choice can fix

Font selection affects legibility factors that WCAG mostly treats indirectly, but which show up in real usability:

- Distinctive letterforms: a face where uppercase i, lowercase l, and digit 1 are distinguishable, and where 0 is distinct from O, prevents real errors in codes, serials, and addresses. Some faces ship alternates (character variants) precisely for this.
- x-height and aperture: open apertures (the gap in c, e, s) and a tall x-height help at small sizes and for low-vision readers; closed, high-contrast designs hurt.
- Weight availability: a family with real medium and semibold weights lets you build hierarchy without dropping contrast; thin weights at small sizes fail in practice even when the color ratio technically passes.
- Script coverage: correct marks, shaping, and diacritics are an accessibility issue for multilingual audiences; tofu and broken shaping make content unreadable.
- Character alternates: some faces ship alternate glyphs (a tail on lowercase l, a distinct zero form) precisely to improve disambiguation; enabling them in tokens is a font-side accessibility win.

## What font choice cannot fix

- Contrast ratios: contrast is a property of color values, not fonts. A "high-legibility font" does not exempt gray-on-gray text from 1.4.3.
- User spacing overrides: if line-height is hardcoded in pixels or text sits in fixed-height containers, 1.4.12 fails regardless of the typeface. The fix is CSS architecture.
- Zoom and reflow: px-locked layouts and horizontal scrolling at 400 percent zoom fail 1.4.4 and 1.4.10 no matter the font.
- Justified text with rivers, all-caps paragraphs, and 120-character lines: these are CSS and layout decisions; 1.4.8 exists because they matter more than the face.
- Pronunciation: screen readers need lang attributes; no font affects pronunciation.
- Currency and punctuation coverage for launch markets: a missing rupee sign is not fixable by a fallback stack; coverage is a selection-time check, not a CSS patch.

## Practical baseline for a project

Adopt these as non-negotiables and put them in the design system documentation:

- Body text at 16 px minimum with line-height at least 1.5, sized in rem.
- Contrast checked at the token level: every text color pair used by components passes for its size class.
- No text in fixed-height containers; use min-height or padding, so spacing overrides cannot clip.
- Letter and word spacing left to the font's defaults in body text; user overrides must survive.
- lang on the html element and lang switching for translated content.
- Hierarchy via size, weight, and spacing; color and case alone never carry meaning.
- Record the conformance target (AA or AAA, and which criteria) next to the type tokens; audits need a target, not a vibe.
- Re-verify the baseline whenever the palette or the family changes; both silently move every number above.
- Treat disabled and placeholder states as part of the audited pair list even where the criterion exempts them; legibility does not take exemptions.

## Common mistakes

- Treating a "dyslexia-friendly" or "accessible" font as an accessibility feature that offsets failing contrast or fixed layouts. It offsets nothing.
- Meeting contrast only in default state: link hover, placeholder, disabled, and focus states fail silently.
- Scaling headings but not body text under zoom, or clamping rem sizes with px bounds so user font-size preferences stall.
- Reading 1.4.12 as "our design must use those spacings"; the criterion is about user overrides working, which is different.
- Auditing with automated tools only: contrast and structure are checkable, but zoom behavior and spacing overrides need human testing.
- Reading the large-text allowance as "anything bold at 18 px"; the criterion means 18.66 px bold, and synthetic bold does not qualify.
- Citing a Lighthouse score as conformance for typography criteria; it does not test the behavioral criteria at all.
- Treating the baseline as one-time setup; criteria evolve (WCAG 2.2 added the target-size floor), so the baseline needs a review date.

## Decision rules

- Choosing between two faces: if both pass license and coverage, prefer the one with better small-size rendering (open apertures, taller x-height, real bold range), because that is the accessibility contribution a font can make.
- If contrast fails with the brand color: change the color token, not the font, and never thin the weight to compensate.
- If a criterion conflicts with a visual requirement (fixed-height cards, tracked-out caps body text): the criterion wins; redesign the component.
- Anything below 16 px in a UI: re-check contrast (smaller text needs the full 4.5 to 1) and test the specific face at that size on Windows.

## Quick reference: the numbers that matter

| Criterion | Level | The number | Where it is fixed |
| --- | --- | --- | --- |
| 1.4.3 Contrast (Minimum) | AA | 4.5 to 1; 3 to 1 for text at least 24 px, or 18.66 px bold | Color tokens |
| 1.4.6 Contrast (Enhanced) | AAA | 7 to 1; 4.5 to 1 for large text | Color tokens |
| 1.4.11 Non-text Contrast | AA | 3 to 1 for focus indicators, icons, and input borders | Component CSS |
| 1.4.12 Text Spacing | AA | 1.5 line height, 2 paragraph spacing, 0.12 letter spacing, 0.16 word spacing (multiples of font size) | CSS architecture |
| 1.4.4 Resize Text | AA | 200 percent enlargement without loss of content or function | Units and layout |
| 1.4.10 Reflow | AA | One-column behavior at 320 CSS px width (1280 px viewport at 400 percent zoom) | Layout |
| 1.4.5 Images of Text | AA | Real text instead of text baked into images, except logos and essential cases | Content and design |
| 1.4.8 Visual Presentation | AAA | Measure at most 80 characters; line height at least 1.5 | Layout and tokens |

Read the table as a division of labor: no font swap satisfies any row by itself, but font choice decides how comfortably each row is met, through real weights for hierarchy, open apertures at small sizes, and tabular figures for aligned data.

## Comparison table: what the font contributes

| Criterion | Font contribution | Honest size of it |
| --- | --- | --- |
| 1.4.3 and 1.4.6 Contrast | None; ratios are a property of colors | Zero |
| 1.4.12 Text Spacing | None directly; loose default spacing tolerates overrides slightly better | Minor; the CSS architecture decides |
| 1.4.4 and 1.4.10 Resize and Reflow | None; units and layout decide | Zero |
| 3.1.1 and 3.1.2 Language | None; lang attributes decide | Zero |
| 1.4.11 Non-text Contrast | Indirect: sturdier strokes keep icons and rings legible | Minor |
| Perceived legibility (not scored by WCAG) | Large: x-height, apertures, distinct 1/l/I and 0/O, real bolds | The row where the typeface leads |

The last row is the trap and the opportunity: WCAG scores pass-fail on things fonts barely touch, while day-to-day usability depends heavily on things WCAG barely scores. Both halves are mandatory.

## Worked example: one settings screen, end to end

A product settings page: a title, four labeled inputs, a save button, a footnote. This audit order finds the most failures first:

1. Token contrast: the footnote gray measures 3.9 to 1 at 13 px and fails 1.4.3; the pair is re-tokened, not the weight reduced.
2. Structure: labels exist only as placeholder text, which disappears on input; real labels are added and placeholders demoted to hints.
3. Units: one caption is hardcoded 13 px; converted to rem, it now scales with the browser font-size preference.
4. Containers: the save row is height: 40px; under the 1.4.12 overrides the button label clips; min-height with padding replaces the fixed height.
5. Spacing overrides: the four criterion values are applied; the footnote collides with the button row; fixed positioning gives way to spacing tokens.
6. Zoom: at 400 percent the two-column form forces horizontal scrolling; a narrow-width media query stacks the columns.
7. Focus: the ring passes 3 to 1 on the light theme and fails on dark; a second ring token is added per theme.
8. Language: the page also ships in German; lang="de" plus a translated template run through the same seven checks.

Total CSS changed: about four rules. Nothing about the typeface changed, because the typeface was never the failure; the audit exists to locate the real fault before someone "fixes" the font.

## Tool notes and field notes

Tools, and what each one actually catches:

- Browser DevTools contrast checkers (Chrome, Firefox, Edge): rendered pairs including opacity compositing; check per state, not per token.
- axe DevTools, Lighthouse, and WAVE: structure and static contrast; they catch missing labels, missing lang, and plain-background failures; they cannot test zoom, overrides, or forced colors.
- The alphagov text-spacing bookmarklet: applies the exact 1.4.12 values to every element; the standard first pass for that criterion.
- Wakamai Fondue: inspects what the chosen file actually ships (tabular figures, alternates, weight range) before you commit.
- WebAIM contrast checker and similar web checkers: token-level sign-off before components exist.
- Forced-colors emulation in DevTools, or Windows High Contrast mode: the only real test that tokens remap sanely.
- NVDA, VoiceOver, TalkBack: a five-minute lang and structure spot check, not a full navigation audit.

Where audits find the real failures:

- Placeholder-only labels, whose contrast and programmatic association both vanished into the placeholder.
- Enabled controls styled to look disabled; 1.4.3 exempts inactive components, but gray-out-as-hierarchy fails real text.
- Focus rings dropped in a rebrand because the new accent fails 3 to 1 and nobody re-tested on dark backgrounds.
- Fixed-height rows in pricing tables, found only because the bookmarklet ran on the pricing page and not on the demo page.
- Missing lang on embedded translated quotes, so screen readers switch voices mid-sentence, or never switch when they should.
- Everything passing until the browser default font size was raised; px-locked metadata stayed invisible until that check.

## Cross-references

- [Text spacing criterion](text-spacing-criterion.md)
- [Contrast and hierarchy](contrast-and-hierarchy.md)
- [Low vision and zoom](low-vision-and-zoom.md)
- [Fallback metrics and CLS](../technical/fallback-metrics-and-cls.md)

Compiled 2025 as part of the Fontlore project.
