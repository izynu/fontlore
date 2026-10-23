# Mixed Script Fallbacks

What this reference covers: Building font stacks for pages where a single line can contain Latin, Cyrillic, Arabic, Devanagari, Thai, or CJK; how per-character fallback actually works; metric and baseline matching between fonts; and how Noto serves as connective tissue. This is the reference for multilingual products, not for single-language sites.

## How fallback really works

The browser resolves fonts per character (effectively per grapheme cluster), walking the font-family list and then the system's fallback mechanism until one font covers the character. Three consequences:

- You cannot assign a font "per element" and be done: an Arabic user name inside an English sentence gets its glyphs from whatever covers Arabic on that element.
- A missing entry in your list is not fatal; the system will substitute something. The question is whether the substitute is coherent with your design or visibly alien.
- Punctuation, digits, and spaces usually come from your primary font even inside foreign-script words, which is usually what you want.

Your explicit font-family list is therefore a design decision about which fonts should cover which characters, in priority order, for that element.

## The three stacking strategies

Strategy 1, one multilingual family: families like Noto Sans cover Latin, Cyrillic, and Greek in a single file; many others cover specific script pairs. Lowest effort, moderate personality, guaranteed internal coherence. Best default for UI chrome.

Strategy 2, primary brand font plus Noto connective tissue: your Latin brand face first, Noto Sans second, then per-script Noto faces (Noto Sans Arabic, Noto Sans Hebrew, Noto Sans Devanagari, Noto Sans Thai, and so on). The brand font shapes Latin; Noto catches everything else with a design that was made to match across scripts. This is the pragmatic standard for multilingual products.

Strategy 3, curated per-script pairing: separate families per script, deliberately matched (for example, a Latin editorial serif with a matched Arabic Naskh). Highest quality ceiling, highest maintenance; each pair needs its own size, weight, and line-height tuning, usually via `:lang()` scoped rules.

## Metric and baseline matching

Mixed-script lines align on a shared baseline, and differences in vertical metrics cause visible wobble:

- Check x-height/proportion: set a mixed Latin-Arabic line, then Latin-Devanagari; letters should sit in one visual row, not bounce.
- Arabic and Nastaliq fonts often carry enormous default line boxes; in single-line controls (buttons, list rows, inputs) that inflates element height. Test controls per language, and set explicit line-height on controls rather than trusting defaults.
- Pick the page's line-height from the tallest demand in the content languages: Latin around 1.4-1.5, Thai and Devanagari 1.5-1.7, Khmer and Myanmar 1.7+. If one page serves all of them, either accept the tall leading or scope leading by language with `:lang()`.
- Weight parity: a 600 in the primary font must not sit next to a visually heavier 700 fallback. Compare real mixed strings in bold.
- The size-adjust, ascent-override, and descent-override descriptors exist to nudge fallback metrics toward a primary font (for reducing layout shift); they can also reconcile a slightly oversized fallback, but prefer choosing better-matched fonts first.

## A worked stack template

For a multilingual web app with a Latin brand sans (Inter, say) and content in many languages:

- font-family: Inter, "Noto Sans", "Noto Sans Arabic", "Noto Sans Hebrew", "Noto Sans Devanagari", "Noto Sans Thai", "Noto Sans CJK SC", sans-serif
- Load only the Noto faces for scripts your analytics or content requirements actually show; each additional face is real bytes.
- Add `:lang(ar)` and `:lang(th)` etc. rules for line-height and any size bumps.
- Let emoji resolve to the platform emoji font; do not try to control emoji in the stack.

For a Latin-plus-one-script product (English plus Vietnamese, say), you often need no fallback font at all: choose a primary family with proper Vietnamese coverage and skip strategy 2 entirely.

## Common mistakes

- Assuming one `font-family` declaration "supports" every script because a fallback appears; untested fallbacks are usually the wrong weight and proportion.
- Forgetting that digits and punctuation come from the primary font inside foreign text; a tabular-figures table can still wobble if Cyrillic text uses a different font's digits.
- One global line-height chosen for Latin, clipping Arabic marks, Thai tone stacks, or Devanagari matras.
- Loading ten Noto faces "to be safe" and shipping megabytes; load per-script faces deliberately.
- Mixing a display face for Latin with a Noto fallback for other scripts in headlines; display Latin plus neutral Cyrillic in one headline reads as a rendering bug.
- Testing mixed-script rendering only in one browser; shaping engines differ and occasionally disagree.

## Decision rules

- UI chrome, many languages: strategy 2 (brand Latin plus Noto per-script) is the default; document the stack in tokens so every surface uses it.
- Single extra script: find one family covering both scripts well (many exist for Latin-plus-Vietnamese, Latin-plus-Cyrillic, Latin-plus-Greek) before adding fallback complexity.
- Editorial with an Arabic or Hebrew audience: strategy 3, with a per-script size and leading plan reviewed by a reader of that language.
- Control elements (buttons, inputs, nav): fix line-height explicitly per script; never leave control height to font default metrics.
- Anything user-generated: design the fallback on purpose, because the substitute fonts will be seen.

## Comparison table

The three strategies compared side by side, then the per-script faces that strategy 2 leans on:

| Strategy | Effort | Coherence | Byte cost | Use when |
| --- | --- | --- | --- | --- |
| One multilingual family | Lowest | Guaranteed within the family | One file per weight | UI chrome, moderate script count |
| Brand Latin plus Noto per-script | Moderate | Strong: brand voice up front, neutral elsewhere | Per-script files, real bytes each | Multilingual products, unknown future locales |
| Curated per-script pairing | Highest | Highest ceiling | Several tuned faces | Editorial and brand surfaces with few scripts |

Per-script Noto faces and what they demand from the layout. Extra leading is relative to a 1.4 Latin baseline:

| Script | Noto face | Extra leading | Watch-outs |
| --- | --- | --- | --- |
| Arabic | Noto Sans Arabic | Tall, 1.6+ | Joins, no tracking, RTL |
| Hebrew | Noto Sans Hebrew | Moderate | Sofit forms, niqqud when pointed |
| Devanagari | Noto Sans Devanagari | Tall, 1.5-1.7 | Shirorekha weight, conjuncts |
| Thai | Noto Sans Thai | Tall, 1.5-1.7 | Tone mark stacks |
| Khmer | Noto Sans Khmer | Very tall, 1.7-1.9 | Coeng subscripts, three-level stacks |
| Myanmar | Noto Sans Myanmar | Very tall, 1.7+ | Legacy Zawgyi content, size bump |
| CJK | Noto Sans JP/KR/SC/TC | Tall, 1.7-2.0 | Region choice, fullwidth punctuation |

## Worked example

A global HR product: English UI, employee-generated content in Arabic, Thai, Japanese, Hindi, and Polish:

1. Inventory: locale analytics and support tickets list the scripts actually seen; unknown future locales are assumed, which rules out strategy 1.
2. Strategy: number 2 - the Inter brand face first, Noto Sans second for Latin-adjacent coverage, then Noto Sans Arabic, Noto Sans Hebrew, Noto Sans Devanagari, Noto Sans Thai, Noto Sans JP, sans-serif.
3. Loading discipline: only the per-script faces the inventory justifies are loaded; each additional face is real bytes, so Myanmar waits until a Myanmar-speaking market exists.
4. Tokens: the stack lives in a design token, and leading lives in per-language tokens - Latin 1.4, Arabic and Hindi 1.6, Thai 1.7, Japanese 1.8 - applied through :lang() rules.
5. Controls: buttons, inputs, and list rows get fixed heights and explicit line-height, because the Arabic and Thai line boxes resize controls when the interface language flips.
6. Bidi: dir="auto" on user-generated fields and bdi around displayed names; one mixed-name list renders a Latin first name next to a Thai surname as a clean row.
7. Verification: each locale is opened with the rendered-fonts inspector to confirm which face drew each run; bold parity is checked in mixed strings; Chromium, Firefox, and WebKit all pass.
8. Documentation: the stack, the per-language leading tokens, and the per-script faces with their rationale are recorded in the tokens file so new surfaces inherit the system instead of inventing one.

Outcome: one stack that survives a new locale arriving mid-quarter, with fallback that looks intentional because it was designed.

## Field notes

- Digits and punctuation usually come from the primary font even inside foreign-script words; usually right, but a Cyrillic or Arabic run inside a tabular-figures table deserves a glance at the digit shapes.
- The rendered-fonts inspector shows font per run; document.fonts.check() offers programmatic verification when you need the check in tests rather than in a browser panel.
- A Linux CI screenshot can render different fallbacks than a user's macOS; test the no-webfont path on purpose on each platform you support.
- Emoji: let the platform emoji font win; forcing emoji coverage into the stack costs bytes and never keeps up with the Unicode cadence.
- size-adjust, ascent-override, and descent-override can reconcile a slightly oversized fallback face; prefer choosing better-matched fonts first and keep overrides as the last-mile tool.
- Loading every Noto script "to be safe" is the most common sizing mistake in multilingual products; the fallback chain works, but the download bill is real.
- Display faces plus neutral fallbacks collide hardest in headlines: a characterful Latin display next to neutral Noto Cyrillic reads as a rendering bug, so scope display fonts to scripts they genuinely cover.
- Stack order encodes policy: primary Latin first, then a Latin-wide family, then script-specific faces, then the generic family. Every reorder is a decision, not a cleanup.
- bdi is the HTML tool and the Unicode isolate characters are the string-level tool; both prevent a foreign run from flipping surrounding punctuation.
- When a locale is added, re-run the whole verification loop: the incumbent stack was tuned for its original script list, and seams appear at the new script's boundaries.
- Fallback resolves per grapheme cluster, not per codepoint: a Devanagari conjunct or a Thai stack is one user-perceived character, so a font can cover the codepoints and still not shape the cluster. That is why shaping smoke tests ride along with coverage tests.
- Punctuation inside foreign runs usually comes from the primary face; a guillemet inside Russian text drawn by your Latin face is normally the right call, but it deserves one glance per script.
- A roster of real names (Arabic, Thai, Polish, and Japanese in one list) is the standing stress test; it exercises fallback, bidi, leading, and sorting in one screen.
- Type IME input in real inputs, not just pasted text: partial clusters render mid-composition, and input behavior differs from paste in ways that paste tests never see.
- Copying and exporting (PDF generation, document export) re-picks fonts outside the browser; test the export path with multilingual content or the exports will ship with different typography than the app.
- Self-hosted unicode-range stacks: generate the ranges from the subset files and confirm on the network panel that each locale loads only its expected slices.
- Reflow and text-resize obligations apply to every script: zoom tests at 200 percent with tall-leading languages catch clipping that Latin-only reflow passes hide.
- text-align: start and end beat left and right in anything that can flip direction; hard-coded left/right values are the bugs that appear only in the Arabic locale.
- Figure and feature requests apply to whatever face draws the text: a fallback face that lacks tabular figures silently ignores the request, so numeric columns in multilingual tables need per-script verification.
- Bidi selection is logical-order: selecting an Arabic phrase inside an English sentence and copying it out surprises people; test copy-out, because ticket systems and logs receive what the clipboard holds.
- Search normalization (NFC, case folding) parallels the font pipeline; a search box that finds nothing for decomposed text is a data bug that surfaces in the same QA pass.
- When row height follows content, Arabic and Thai list rows run taller and lists visibly breathe; fixed row heights are the quiet fix.
- The font-display swap flash shows the system font for a moment; in mixed-script apps that moment is per script, so preview it per locale instead of judging it on the English page.
- Self-hosted subset files deserve checked-in manifests: file name mapped to codepoints and locale, because mystery font files outlive their authors.

## Quick reference

- Stack template: primary Latin face, "Noto Sans", then per-script Noto faces (Arabic, Hebrew, Devanagari, Thai, CJK per region), then sans-serif.
- Load rule: one face per script you actually serve; add a script only when a locale justifies it.
- Leading tokens per language via :lang(): Latin 1.4, Arabic and Devanagari 1.6, Thai 1.7, Khmer and Myanmar 1.7-1.9, CJK 1.7-2.0.
- Controls: fixed heights and explicit line-height on buttons, inputs, and rows; never trust font default metrics for control height.
- Direction hygiene: dir="auto" on unpredictable fields, bdi on displayed user names, dir="ltr" on computed numeric output that scrambles.
- Verification kit: rendered-fonts inspector per locale, mixed-line wobble check, bold parity in real strings, three browser engines.
- Metrics last resort: size-adjust and the ascent/descent-override descriptors, used to reconcile a near-miss fallback, documented when applied.
- Documentation: stack, faces, leading tokens, and the per-script rationale live in the design tokens, not in one component's CSS.
- Standing stress test: a real-names roster page covering every served script, refreshed from customer data each release.
- IME gate: Thai and Devanagari typed into real inputs, verified for composition behavior, not just pasted.
- Export gate: the PDF or document export path renders the same roster, because export re-picks fonts outside the browser.
- Alignment: start and end over left and right anywhere direction can flip.
- Multilingual tables: verify each script's fallback face honors the tabular-figures request.
- List rows: fixed heights so Arabic and Thai rows do not breathe taller than Latin rows.
- Manifest: every self-hosted subset file mapped to its codepoints and locale in a checked-in file.
- Swap flash: preview font-display behavior per locale, because the fallback moment differs per script.

## Cross-references

- [Fallback metrics and CLS](../technical/fallback-metrics-and-cls.md)
- [Testing multilingual coverage](testing-multilingual-coverage.md)
- [Localization and RTL accessibility](../accessibility/localization-and-rtl-accessibility.md)
- [CJK fundamentals](cjk-fundamentals.md)

Compiled 2025 as part of the Fontlore project.
