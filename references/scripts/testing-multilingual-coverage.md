# Testing Multilingual Coverage

What this reference covers: A concrete testing method for multilingual typography: codepoint checklists per script, missing-glyph detection, shaping smoke tests, and how to use real copy from the project instead of lorem ipsum. It turns "does this font support our languages" from a guess into a procedure.

## Why specimen-based testing fails

Font specimens and catalog previews show hand-picked, well-shaped strings. They hide exactly the failures that matter: the letter that renders as tofu, the conjunct that never forms, the tone mark that collides. Real testing uses your languages' hardest cases and your project's actual copy.

Ground rule: this reference names test material by description and codepoint rather than by pasting script text, so the checklists below stay reusable in any pipeline. Build the actual test strings once from the sources listed, save them in your repo, and reuse them for every font evaluation.

## Codepoint checklists per script

Build one text file per language with the characters and words most likely to fail. Minimums:

- Latin-extended (Polish, Czech, Turkish, Romanian): ogonek letters U+0105/U+0119, stroke L U+0142, carons U+0159/U+011B, Turkish U+011F/U+0131/U+0130, Romanian comma-below U+0218-U+021B, plus each language's full alphabet.
- Vietnamese: the U+1EA0-1EFF block with the worst stackers (e with circumflex and dot below; a with breve and hook above; u with horn and tilde).
- Cyrillic: Russian base set; Ukrainian U+0454/U+0456/U+0457/U+0491; Serbian U+0402/U+0405/U+0408-040C/U+040F; Macedonian U+0403/U+045C.
- Greek: U+03C2 final sigma, U+037E question mark, accented capitals U+0386-038F; polytonic needs U+1F00-1FFF spot checks.
- Arabic: lam-alef sequences (U+0644 followed by U+0623, U+0625, U+0627, U+0622), hamza carriers, and Persian extras U+067E/U+0686/U+0698/U+06AF if Persian is in scope.
- Hebrew: the five final forms, geresh/gershayim U+05F3/U+05F4, and a fully pointed sample using niqqud from U+0591-05C7.
- Devanagari: conjuncts k+virama+s (ksha), t+virama+r (tra), j+virama+n (jna), d+virama+v; short-i reordering (U+093F); nukta forms; digits U+0966-096F.
- Thai: tone marks U+0E48-0E4B over tall consonants such as U+0E1B and U+0E2D, and over stacked vowels; Thai digits U+0E50-0E59.
- Khmer: coeng U+17D2 plus consonant subscript chains, multi-level stacks, serial punctuation U+17D4-17D7.
- Myanmar: stacked consonants via U+1039, medials, and Myanmar digits U+1040-1049; Unicode text only, never legacy Zawgyi.
- CJK: pick per region, including the characters whose regional forms differ (for example the "bone", "straight", and "grass" radicals' variants) so you can confirm you loaded the right regional font.

## Where to get real sentences

- The Unicode consortium hosts Universal Declaration of Human Rights translations in hundreds of languages at https://www.unicode.org/udhr/index.html; one paragraph per language is ideal because it is natural, unpoetic text.
- The Wikipedia edition of each target language: take a lead paragraph from an article about something your product resembles.
- Google Fonts specimen pages have a language selector that renders sample strings per language; useful for a first pass, never sufficient alone.
- Your own product: exported menu labels, address forms, order histories, names from support tickets. This is the copy that will actually ship, and it contains the mixed-script cases no pangram covers.

## Missing-glyph detection

- Tofu (hollow boxes) is the visible end of a missing cmap entry; the browser walks your font stack and then system fonts before giving up, so tofu in testing means every candidate failed.
- Hexboxes (a box with hex digits) appear on some platforms for defined-but-unshaped cases; treat them as failures too.
- Detection methods: paste the checklist file into a specimen page using only the candidate font; use Wakamai Fondue's glyph list to check coverage before rendering; use fonttools to dump the cmap and diff against your required codepoint set; or automate with a script that renders each codepoint and detects the .notdef glyph.
- Beware silent substitution: a missing character may render from a system font with different weight and proportions. Compare mixed strings at small size, where seams show.

## Shaping smoke tests

Coverage is necessary but not sufficient; shaping tables must work. Per script, check:

- Arabic: lam-alef renders as one ligature; medial forms actually connect on both sides; Persian/Urdu letters take correct isolated and joined forms.
- Devanagari: the short-i matra appears before its consonant; ksha/tra/jna conjuncts render as designed ligatures; reph sits on the following consonant.
- Thai: tone marks clear tall consonants and stack over the nikhahit combination; no floating marks between lines at production line-height.
- Khmer: coeng sequences become real subscripts; two-level stacks stay inside the line box.
- Myanmar: stacked consonants and kinzi render; digits and medials are positioned correctly.
- Cross-check with hb-shape (HarfBuzz's command-line tool) when a browser result looks wrong; it shows exactly which glyphs a shaper selects, separating font bugs from browser bugs.

## Making it a repeatable workflow

1. Maintain a per-language test file in the repo (codepoint checklist plus one real paragraph each).
2. For every shortlisted font, render the checklist on a static specimen page at three sizes: 12, 16, and 32 px equivalent.
3. Record pass/fail per language in the shortlist matrix; a hard fail (tofu, broken shaping) eliminates the font for that language, a soft fail (mark collisions at one size) needs a note.
4. Re-run the checklist when upgrading a font version; coverage and shaping tables change between releases.
5. Add any new language to both the test files and the font requirements before choosing fonts for its features.

## Common mistakes

- Testing with pangrams only; pangrams are Latin-script folk artifacts and do not exercise stacking or shaping.
- Trusting the Google Fonts subset label without rendering the checklist; labels say codepoints exist, not that they are placed correctly.
- Testing only in Chrome on a developer Mac; shaping engines and installed fallback fonts differ across platforms.
- Forgetting digits, currency, and punctuation; the letters pass and the table still wobbles.
- Using lorem ipsum for layout testing in a multilingual product; it has no script complexity and no real names.
- Treating one passing version as permanent; font updates change coverage quietly.

## Decision rules

- Any hard failure in a shipping language: eliminate the font for that product, whatever its beauty.
- Soft failure at display sizes only: acceptable if display text in that language is limited to short, checked strings.
- New language added mid-project: run the full checklist against the incumbent stack before committing; if the stack fails, treat it as a scoped migration, not a quick fix.
- Two candidate fonts pass everything: prefer the one that also passes in your heaviest language at small sizes, not the one with the prettier specimen.

## Comparison table

Detection and shaping tools compared. None replaces real copy; all of them make failures visible earlier than a stakeholder demo will:

| Tool | Interface | What it shows | Best for |
| --- | --- | --- | --- |
| Wakamai Fondue | Web, upload a font file | Glyph list and count, OpenType features, variable axes | Fast coverage and feature audit before rendering |
| fonttools / ttx | CLI | cmap dump, table dumps, diffable text output | Scripted CI checks and version-to-version diffs |
| hb-shape | CLI | Exact glyph names a HarfBuzz shaper picks for a string | Separating font shaping bugs from browser bugs |
| Browser rendered-fonts inspector | DevTools panel | Which face actually drew each run on the page | Live fallback detection per locale |
| document.fonts.check() | JavaScript | Whether a loaded face covers a string | Automated tests for required coverage |
| hb-view | CLI | Renders a string with a given font to an image | Visual shaping proof outside the browser |
| FontDrop | Web, upload a font file | Raw table data viewer | Deep inspection of cmap, name, and metric tables |
| Google Fonts language selector | Web | Sample strings rendered per language | First-pass screening only |

Reading the table:

- The inspector and check() answer "what did the browser actually do"; Fondue, fonttools, and hb-shape answer "what can this file do". A multilingual QA loop needs both directions.
- The Google Fonts language selector renders curated samples, which is exactly why it must never be the final gate; curated strings hide the failures.
- hb-shape output names glyphs: when a browser shows a broken cluster, hb-shape on the same string and font tells you whether the shaper itself was wrong or the browser layer interfered.
- File-level tools need the actual font file, which is trivial for self-hosted faces and a download for hosted ones; keep the exact versioned files used in production in a fixtures directory so audits reproduce.

## Worked example

Adding Japanese to an English-only product, using the procedure instead of optimism:

1. Test file first: a Japanese file is built with a joyo-kanji sample paragraph, kana, fullwidth punctuation, and the characters whose JP and mainland forms differ; it is saved in the repo, not in a chat thread.
2. Baseline run: the incumbent stack (one Latin webfont, no CJK face) renders the file; text appears, but macOS pulls Hiragino, a teammate's Windows pulls Yu Gothic, and the CI Linux box pulls something else entirely - three fonts, three conventions, no policy.
3. Decision: system stack for body text (native comfort, zero bytes) plus Noto Sans JP through the hosted sliced CSS for headings and brand moments.
4. Language tags: lang="ja" lands on the Japanese tree and on inline Japanese runs inside English pages, so regional forms resolve correctly.
5. Rendering check: the test file is re-rendered; the region-differing characters now come from the JP family, confirmed with the rendered-fonts inspector.
6. Metrics pass: a :lang(ja) leading token of 1.8 is added, and measure math is redone counting fullwidth punctuation as full em.
7. Weight audit: headings load real 500 and 700 weights; synthetic bold is verified absent on dense kanji.
8. Regression wiring: the checklist page joins the repo, the shortlist matrix records the pass with the font version and date, and the font-upgrade rule (re-run on every version bump) is noted.
9. Fixture discipline: the exact font files pulled from production are stored with the checklist, so a coverage audit next quarter reproduces today's result.
10. Platform sweep: the checklist runs once on a low-end Android device, where fallback chains differ most from developer machines.

Outcome: Japanese ships with a documented stack, correct regional forms, measured leading, and a repeatable gate for the next locale.

## Coverage checklist

Run this at every launch, locale addition, and font version bump:

- Every shipping language has a test file in the repo: codepoint checklist plus one real paragraph plus product strings with real names.
- The checklist renders at 12, 16, and 32 px equivalents, in regular and bold, on a page that loads only the candidate stack.
- Shaping smoke tests pass per script: lam-alef for Arabic, conjuncts and short-i for Devanagari, tone marks over tall consonants for Thai, coeng chains for Khmer, stacked consonants and kinzi for Myanmar.
- Digits, currency symbols, and punctuation are in the checklist per locale, not just letters.
- The fallback path is audited on purpose: no-webfont rendering checked on each supported platform with the rendered-fonts inspector.
- Subsets and slices are re-verified after any font version bump; coverage and shaping tables change quietly between releases.
- Mixed-script seams (names, addresses, paths, receipts) are reviewed with real data, not synthetic samples.
- Results are recorded in the shortlist matrix with pass or fail, font version, and date, so the next team can see why a decision was made.
- A new language entering scope triggers the full checklist against the incumbent stack before feature work, not after.
- Versioned fixtures: production font files are archived next to the checklist so audits are reproducible.
- The browser matrix includes one low-end Android device, not just developer machines.

## Quick reference

- Commands worth keeping in the repo notes: ttx -t cmap font.ttf for a codepoint dump; hb-shape font.ttf "sample string" for shaper output; document.fonts.check('16px "Noto Sans JP"', sample) for coverage assertions in tests.
- Test sources: the Unicode consortium's UDHR translations for natural paragraphs, the target language's Wikipedia for domain-adjacent text, and your own product exports for the strings that actually ship.
- Pass and fail definitions: a hard fail (tofu, hexbox, broken shaping) eliminates a font for that language; a soft fail (mark collisions at one size) needs a written note and a scope decision.
- Cadence: full re-run on font upgrades, on new locales, and before launches; spot checks otherwise.
- Matrix discipline: one row per language, one column per candidate, dates and versions recorded; a matrix without versions is a rumor.
- The two-direction principle: file-level tools (Fondue, fonttools, hb-shape) prove capability; page-level tools (inspector, check()) prove what users actually get.
- Ground rule: if a test can pass with lorem ipsum, it is not a multilingual test.
- Fixtures: keep the exact production font files beside the test files; version drift invalidates old passes.
- Screenshot discipline: capture each checklist render at the three sizes and archive the images with the matrix entry.

## Cross-references

- [Latin and extended coverage](latin-and-extended.md)
- [Arabic script typography](arabic-script-typography.md)
- [Inspecting font files](../technical/inspecting-font-files.md)
- [Testing and comparing shortlists](../workflow/testing-and-comparing-shortlists.md)

Compiled 2025 as part of the Fontlore project.
