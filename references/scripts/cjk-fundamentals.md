# CJK Fundamentals

What this reference covers: The structural facts of Chinese, Japanese, and Korean typography that control font decisions: glyph counts and file sizes, Han unification and the JP/KR/SC/TC variant problem, how Noto CJK is organized, subsetting strategies, and when webfonts are actually viable versus system font stacks.

## Glyph counts and why size dominates

CJK fonts are an order of magnitude larger than Latin fonts, and every decision follows from that:

- Japanese: JIS X 0208 defines 6,355 kanji; practical fonts include more, and full releases run 20,000 glyphs or more once kana and Latin are added.
- Simplified Chinese: GB2312 defines 6,763 hanzi; the modern common-use table lists 3,500 for everyday literacy.
- Traditional Chinese: Big5-era sets cover roughly 13,000 characters.
- Korean: Hangul syllables number 11,172; a complete font covers all of them plus Hanja if desired. Hangul-only fonts are far smaller than hanzi fonts.

A full CJK weight is measured in megabytes per weight, not kilobytes. Nothing else in web typography has this cost structure, so CJK strategy is a size strategy first.

## Han unification and the variant problem

The same Unicode codepoint can have regionally different glyph shapes: characters like the one for "bone" or "straight" are drawn differently in Japanese, Simplified Chinese, Traditional Chinese, and Korean conventions. Consequences:

- You cannot buy one "CJK font"; you choose per-language faces. Noto Sans JP, Noto Sans KR, Noto Sans SC, and Noto Sans TC are separate families, not instances of one font.
- Language tags matter: `lang="ja"`, `lang="zh-Hans"`, `lang="zh-Hant"`, `lang="ko"` let shaping and font selection do the right thing, and let the locl feature select regional forms inside multi-variant fonts.
- Korean text mixes Hangul with spacing-based word separation; Japanese adds kana and different punctuation widths; Chinese uses fullwidth punctuation throughout. These texture differences mean a "neutral" choice rarely exists.

## Noto CJK structure

The Noto CJK releases are the open-source backbone of the ecosystem:

- Regional families: Noto Sans CJK and Noto Serif CJK exist as SC, TC, JP, KR, and HK regional builds, sharing one design system with region-correct forms.
- Google Fonts serves them as separate per-region families (Noto Sans JP, Noto Sans SC, and so on), each with its own weights.
- Desktop distribution often packages several regions in one OpenType Collection (OTC) file, which is convenient for installed fonts but irrelevant to the web.
- Weights: the CJK families have unusually complete weight ranges (Light through Black), which matters because faux bold in CJK looks particularly bad.

## Subsetting: how the web actually serves CJK

- Google Fonts CSS for CJK families ships dozens to over a hundred unicode-range slices; the browser downloads only the slices containing characters actually used on the page. A page with 200 unique hanzi transfers a few slices, not megabytes. This is why Google-hosted CJK webfonts are viable while self-hosting naively is not.
- Self-hosting requires a deliberate subset: choose a frequency list (3,500 common hanzi for SC; 2,136 joyo kanji for Japanese; the common-use Hangul syllables for KR), then generate with pyftsubset and serve as woff2. For a UI, subsetting to the actual strings (app copy, navigation, product names) is often the winning move because the set is small and stable.
- User-generated content breaks fixed subsets: if users can type arbitrary text, plan for system-font fallback of uncovered characters, and make that fallback look intentional (see the mixed-script reference).
- Keep the mapping of subset to codepoints documented; a subset that silently grows is a maintenance trap.

## When webfonts are viable

- Viable: headings and brand moments (small, fixed strings); dynamic headings via unicode-range slicing from a hosted service; icons and numerals; campaigns where the copy is known.
- Usually not viable as primary choice: body text in a full range of characters, especially for content sites with UGC or search results. The size cost and the fallback mismatch outweigh brand benefits.
- Practical default stacks (system fonts, no download):
  - Simplified Chinese: "PingFang SC" (Apple), "Microsoft YaHei" (Windows), "Noto Sans CJK SC" (Android, Linux).
  - Japanese: "Hiragino Kaku Gothic ProN" (Apple), "Yu Gothic" and "Meiryo" (Windows), "Noto Sans CJK JP" (Android, Linux).
  - Korean: "Apple SD Gothic Neo" (Apple), "Malgun Gothic" (Windows), "Noto Sans CJK KR" (Android, Linux).
- Serif defaults for long reading exist per platform too (Songti/SimSun traditions, Hiragino Mincho, Batang); test before promising a serif look.

## Layout facts that surprise Latin-trained teams

- Punctuation is fullwidth: a Chinese comma occupies a full em square, which changes measure calculations and wrapping.
- Line breaking can occur between any two hanzi; there are no spaces to break at. Overflow and rag control work differently; avoid text-align: justify habits from Latin except where CJK convention expects flush edges.
- Line-height conventions run taller than Latin body text; 1.7 to 2.0 is common for CJK reading comfort.
- Vertical writing (writing-mode: vertical-rl) is a real requirement for some Japanese contexts but is complex on the web; treat it as a project of its own, not a CSS flourish.
- Bold in CJK: use a real weight; synthetic bold smears strokes and is instantly recognizable.

## Common mistakes

- Self-hosting a full CJK webfont for body text and wondering why the page weighs several megabytes.
- Choosing Noto Sans SC for a Japanese page (or vice versa); the regional forms are wrong for the audience even though most characters "work".
- Serving CJK text without language tags, so mixed Latin/CJK lines pick inconsistent variant forms.
- Using synthetic bold because only two weights were loaded.
- Ignoring fullwidth punctuation in width calculations and measure settings.
- Subsetting to the homepage copy and shipping the same subset to a knowledge base with arbitrary text.

## Decision rules

- Marketing or product site with fixed copy: hosted CJK webfont with unicode-range slicing for headings, system stack for body.
- Web app with localized UI: subset to UI strings, ship woff2, fall back to the system stack per language.
- Content platform with UGC: system stack for body; brand webfont only where strings are controlled.
- Korean-only service: Hangul-complete fonts are affordable enough that webfonts are realistic for headings and even UI text.
- Long-form CJK reading: system serif stacks or hosted serif webfonts for headings; keep line-height generous and measures around 35 to 45 characters.

## Comparison table

The four regional Noto families next to the system fonts they fall back to. Weights shown are the Google Fonts ranges:

| Region | Webfont family | Weights | macOS default | Windows default | Android/Linux default |
| --- | --- | --- | --- | --- | --- |
| Japanese | Noto Sans JP | 100-900 | Hiragino Kaku Gothic ProN | Yu Gothic, Meiryo | Noto Sans CJK JP |
| Simplified Chinese | Noto Sans SC | 100-900 | PingFang SC | Microsoft YaHei | Noto Sans CJK SC |
| Traditional Chinese | Noto Sans TC | 100-900 | PingFang TC | Microsoft JhengHei | Noto Sans CJK TC |
| Korean | Noto Sans KR | 100-900 | Apple SD Gothic Neo | Malgun Gothic | Noto Sans CJK KR |

Reading the table:

- Serif counterparts exist for every row (Noto Serif JP, KR, SC, and TC, roughly 200-900), and system serifs follow the same regional split: Hiragino Mincho for Japanese, the Songti and SimSun traditions for Chinese, Batang for Korean. Test before promising a serif look, because Windows serif defaults are inconsistent.
- Stack-order rule: put the Latin brand face before the CJK face. CJK system fonts include Latin glyphs of their own and will happily draw your English copy if they come first in the list.
- The regional families share one design skeleton but differ in conventions for shared codepoints; substituting SC for JP (or vice versa) changes stroke forms even when the text "renders fine".
- On desktop, Noto CJK also ships as an OpenType Collection bundling all regions plus Noto Sans Mono CJK; that packaging is irrelevant on the web, where only per-region families and unicode-range slices exist.

## Worked example

A Japanese e-commerce storefront with fixed marketing copy and dynamic product data:

1. Requirements: Japanese-first, English secondary, a Latin brand sans already chosen, marketing headlines are fixed strings, product titles and descriptions arrive from a feed.
2. Body strategy: system stack (Hiragino Kaku Gothic ProN, Yu Gothic, Meiryo, Noto Sans CJK JP, sans-serif) - zero download cost and native reading comfort.
3. Heading strategy: Noto Sans JP 500 and 700 served through the hosted CSS, which slices the family into unicode-range files; a headline with a few dozen unique kanji pulls a couple of slices, not megabytes.
4. Language tags: lang="ja" on the Japanese locale so regional forms and punctuation behavior resolve correctly; the English locale keeps its own tree.
5. Metrics: body line-height 1.8, measure around 35 to 45 characters, and measure math that treats fullwidth punctuation as a full em wide, or line lengths drift from the design.
6. Weights: 400, 500, and 700 loaded as real weights; synthetic bold was rejected after a side-by-side showed smeared strokes on dense kanji.
7. Dynamic-text guard: the product feed is sampled for rare kanji; uncovered characters fall back to the system stack, which was tuned so the weight seam is not visible at body sizes.
8. Punctuation audit: price strings, dates, and address blocks are checked for fullwidth forms and consistent spacing conventions.
9. Regional-form spot check: characters whose Japanese and mainland forms differ are rendered to confirm the JP family is actually serving them.
10. Cross-browser pass: Chromium, Firefox, and Safari verified, because the CJK fallback chain behaves differently once the webfont slices miss a character.

Outcome: a payload of a few slices on typical pages, native body comfort, brand-consistent headings, and no megabyte download anywhere in the waterfall.

## Field notes

- The classic silent bug is loading Noto Sans SC for a Japanese site because it sat first in a shared stack; the text renders, but the forms are mainland conventions. Detect it with characters known to differ across regions.
- Korean-only services are the affordable CJK case: Hangul-complete faces are far smaller than hanzi-bearing faces, so webfonts are realistic beyond headings.
- Standard subset targets worth memorizing: 2,136 joyo kanji for Japanese, 3,500 common-use hanzi for Simplified Chinese, all 11,172 Hangul syllables for Korean.
- Fullwidth digits and letters (the U+FF00 block) leak in from Japanese and Chinese office documents; a content scan for fullwidth Latin and digits catches copy-paste artifacts before they render oddly.
- pyftsubset is the self-hosting path: pick a frequency list, subset, serve woff2, and document the covered codepoints; a subset that silently grows is a maintenance trap.
- Vertical writing (writing-mode: vertical-rl) is real Japanese typography, not a CSS flourish; treat it as a scoped project with its own testing if the design requires it.
- Justify habits from Latin do not transfer; CJK breaks between any two characters, and the punctuation-compression rules browsers approximate are part of why ragged edges are the safe default.
- If a design needs monospace CJK, plan for a system mono plus a per-region CJK fallback; Noto Sans Mono CJK exists only in desktop packaging, not as a webfont.
- Font-feature behavior differs per region: some CJK conventions are controlled by locl and language tags, so a page missing lang attributes can mix conventions inside one paragraph.
- Text with furigana (ruby) needs the HTML ruby element and fonts whose metrics tolerate the annotation; most UI CJK faces handle it, but test dense body text.
- Hong Kong is its own regional case: Noto Sans HK is a separate Google Fonts family for Traditional Chinese as used in Hong Kong, and an HK-first audience deserves that build rather than TC by default.
- Self-hosting a variable CJK file means shipping megabytes; the slicing approach is what makes either the hosted CSS or a homegrown unicode-range split viable.
- Large numbers in Japanese and Chinese prose lean on four-digit-based units (man and oku; wan and yi); let the i18n layer decide between plain digits and unit-based rendering, and keep table columns in plain formatted digits.
- Korean jamo can arrive decomposed; NFC normalization composes conjoining jamo into precomposed syllables, so run the same NFC pipeline you use for Latin over Korean content.
- Some platform CJK fonts render thin weights poorly at small sizes and in dark UI; bumping the weight one step for CJK text is a common, defensible adjustment.
- Weights inside Japanese system fonts can carry unusual names across OS versions; when pinning a system stack, verify the exact family and weight names on each OS release you support.
- A CJK font's built-in Latin is serviceable but characterful; if the brand Latin must survive inside CJK pages, the stack order rule does the work, and a quick mixed-line proof confirms it.

## Quick reference

- Language tags: lang="ja", lang="zh-Hans", lang="zh-Hant", lang="ko" - set them, because variant selection and punctuation behavior depend on them.
- Sizes to remember: 6,355 JIS kanji; 2,136 joyo kanji; 6,763 GB2312 hanzi; 3,500 common-use hanzi; 11,172 Hangul syllables.
- Reading metrics: line-height 1.7-2.0, measure 35-45 characters, no text-align: justify by default.
- Weight rule: load real weights (the Noto CJK ranges run Light through Black); never ship synthetic bold to CJK text.
- Delivery: hosted CSS with unicode-range slicing for anything dynamic; pyftsubset plus woff2 for fixed app strings; full files only for installed or bundled contexts.
- System stacks: keep the per-region default table inside your tokens file; it is the path every real user hits when slices miss or scripts are off.
- Regional-form test: include characters whose JP, SC, TC, and KR forms differ so a wrong-family substitution is visible rather than theoretical.
- Measurement: count fullwidth punctuation as full em when computing measure; a Latin-calibrated character count is wrong for CJK lines.
- Inline language: when the document lang is en but a run is Japanese, wrap the run in span lang="ja" so variant selection still applies at the character level.
- Loading: font-display: swap is the sane default for CJK slices; blocking render on a large CJK file is worse than a brief fallback flash.
- Serif caveat: system serif CJK is the least consistent path across platforms; prove it per platform before designing around a serif look.

## Cross-references

- [Subsetting and performance](../technical/subsetting-and-performance.md)
- [Webfont formats](../technical/webfont-formats.md)
- [Mixed script fallbacks](mixed-script-fallbacks.md)
- [Testing multilingual coverage](testing-multilingual-coverage.md)

Compiled 2025 as part of the Fontlore project.
