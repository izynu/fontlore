# Arabic Script Typography

What this reference covers: How Arabic joining works, the major calligraphic style families and which open fonts embody them, numeral conventions, vertical metric realities, and the RTL layout basics that keep text from breaking. It is a working reference for web and product teams, not a calligraphy history.

## How joining works

Arabic is cursive by rule: most letters connect to their neighbors, and each letter has up to four contextual shapes (isolated, initial, medial, final). Three facts drive everything else:

- Text is stored in logical order, one codepoint per letter. The shaping engine, HarfBuzz in Chromium, Firefox, and Android; CoreText in Safari, picks contextual forms via the font's GSUB table (features like init, medi, fina, and rlig).
- The lam-alef combination is a mandatory ligature in virtually all fonts; if it renders as two joined-but-separate letters, shaping is broken.
- Because the font and the shaper do the work, the browser does not need "Arabic support" beyond a font and a shaper; but old pipelines that reverse text manually produce garbage. Never reverse Arabic strings in code.

Consequence: you cannot judge an Arabic font by pasting letters individually. Always test real words.

## Style families and representative open fonts

- Naskh: the book hand, dense and horizontal, best for running text. Amiri (Khaled Hosny, based on the Amiria Press types), Noto Naskh Arabic, Scheherazade New and Lateef (SIL), Harmattan (SIL, West African style).
- Kufi: geometric and architectural; modern kufi is a common brand voice. Reem Kufi, Noto Kufi Arabic.
- Ruqaa: handwriting-derived, informal. Aref Ruqaa.
- Modern sans/flat designs for UI: Cairo, Tajawal, Almarai, IBM Plex Sans Arabic, Readex Pro (also covers Latin), Changa.
- Display and poster voices: Lalezar, Rakkas, Jomhuria.
- Persian and Urdu: Nastaliq is the expected literary style; Noto Nastaliq Urdu is the main open option and demands enormous vertical space. Persian adds four letters (pe, che, zhe, gaf, roughly U+067E, U+0686, U+0698, U+06AF); Urdu adds several more (U+0679, U+0688, U+0691, U+06BA, U+06BE, U+06D2 among others). Check these before using a Naskh font for Persian or Urdu.

Pairing with Latin: several modern families ship matched Latin and Arabic (IBM Plex Sans Arabic, Readex Pro, Cairo's Latin). Otherwise pair an Arabic family with a Latin one of similar weight range and openness, and expect to tune sizes separately; Arabic typically reads best slightly larger than Latin at the same nominal size.

## Numerals

- Western digits (0-9) are common in Gulf and business contexts.
- Arabic-Indic digits U+0660-0669 are standard in much of the Arabic-speaking world.
- Eastern Arabic-Indic digits U+06F0-06F9 are the Persian and Urdu forms.
- Decide per locale, not per site. A bilingual product often shows Western digits in the Latin locale and Arabic-Indic in the Arabic locale; format numbers with your i18n library rather than hardcoding.
- Digits within Arabic text still read left to right; the bidi algorithm handles this. Do not "fix" it by reversing strings.

## Vertical metrics and line-height

Arabic fonts carry tall ascenders (alif, lam, marks) and deep descenders, and many include generous default line gaps.

- A line-height tuned for Latin, around 1.3, will often clip hamza marks and stacked diacritics in Arabic. Start around 1.6 for body text and check display sizes individually.
- Mixed Latin-Arabic lines align on a shared baseline; the huge Arabic line box can make single-line UI elements (buttons, list rows) taller than expected. Test buttons and inputs containing Arabic explicitly.
- Noto Nastaliq Urdu needs dramatically more leading; treat its default metrics as the floor, not something to compress.
- Avoid letter-spacing on Arabic entirely: positive tracking cuts the connections between letters and destroys the script's texture. Justification is done with the shaper and kashida (tatweel, U+0640) or word spacing, not letter-spacing.

## RTL layout basics

- Set direction with the `dir` attribute on the document or section: `dir="rtl"` for Arabic, Persian, Urdu. Use `dir="auto"` on user-generated content whose script you cannot predict.
- Use CSS logical properties: padding-inline-start, margin-inline-end, text-align: start. Physical left/right values break the moment direction flips.
- Text containing mixed runs (a Latin brand name inside Arabic) is handled by the Unicode bidirectional algorithm; wrap unpredictable user content in bdi elements or Unicode isolate characters to keep it from leaking direction.
- Punctuation and mirrored brackets come out correctly only when the text is real Unicode; beware content pasted from sources that "pre-mirrored" parentheses.
- Icons and progress indicators that imply direction (arrows, next/chevrons) should flip in RTL contexts; type should not be mirrored.

## Common mistakes

- Letter-spacing on Arabic UI labels, visually chopping the joins between letters.
- Judging an Arabic font from isolated letters in a specimen app instead of real shaped words.
- Assuming uppercase transforms make sense; Arabic has no letter case, and text-transform is a no-op there.
- Using Arabic Presentation Forms codepoints (U+FB50-FDFF, U+FE70-FEFF) in content; they are compatibility encodings and defeat proper shaping.
- Tight Latin line-height applied globally, clipping Arabic marks; or fixing it by inflating line-height globally, which then balloons Latin pages.
- Choosing a Gulf-brand geometric font for a Quranic or classical text; style mismatch is a content failure, not just an aesthetic one.
- Testing only in one browser; shaping is engine-dependent and CoreText vs HarfBuzz differences occasionally surface.

## Decision rules

- Long-form reading: Amiri or Noto Naskh Arabic for classical or literary content; Scheherazade New where very clear, open letterforms matter.
- Product UI: IBM Plex Sans Arabic, Readex Pro, Cairo, Almarai, or Tajawal; check the Latin half if the same family must cover both scripts.
- Brand voice: Reem Kufi for geometric-modern, Lalezar or Rakkas for display energy, Aref Ruqaa for informality.
- Persian or Urdu: verify the extra letters first; then Noto Nastaliq Urdu for literary text or a Sans-style Arabic with confirmed coverage for UI.
- Multilingual system: build the stack around Noto (Noto Sans for Latin/Cyrillic/Greek, Noto Sans Arabic, and so on) for metric coherence across scripts.

## Comparison table

Choosing among the open Arabic voices is easier with the trade-offs side by side. Line-height floor is the minimum leading that keeps marks intact in body text; headlines are verified separately:

| Style | Open exemplars | Voice | Best for | Line-height floor |
| --- | --- | --- | --- | --- |
| Naskh, classical | Amiri | Bookish, dense, scholarly | Classical and literary text, religious content | 1.6 |
| Naskh, contemporary | Noto Naskh Arabic, Scheherazade New | Clear Naskh for modern reading | Long-form body text, documentation | 1.6 |
| Naskh, South Asian | Lateef (SIL) | Simplified Naskh for the region | Urdu and South Asian Arabic-script languages | 1.6 |
| Naskh, West African | Harmattan (SIL) | Regional book style | Fulfulde, Hausa, and related languages | 1.6 |
| Kufi, modern | Reem Kufi, Noto Kufi Arabic | Geometric, architectural | Brand marks, headings, short labels | 1.5 |
| Ruqaa | Aref Ruqaa | Handwriting-derived, informal | Casual accents, pull quotes, short moments | 1.5 |
| Nastaliq | Noto Nastaliq Urdu | Flowing Persian and Urdu literary tradition | Urdu and Persian literary content | font metrics as floor; dramatically tall |
| Persian UI | Vazirmatn | Contemporary Persian UI sans | Persian-first products and apps | 1.5-1.6 |
| Quranic | Amiri Quran | Specialized mushaf conventions | Quranic text and religious apps | font metrics as floor |
| UI sans | IBM Plex Sans Arabic, Cairo, Tajawal, Almarai, Readex Pro | Flat, contemporary, compact | Product UI, dashboards, marketing sites | 1.5-1.6 |
| Display | Lalezar, Rakkas, Jomhuria | Poster energy, loud, compact | Headlines, campaigns, short strings | verify per size |

Facts to check before locking weights and regions:

- IBM Plex Sans Arabic ships 100-700; Cairo is variable 200-1000; Almarai offers 300, 400, 700, and 800; Tajawal covers 200-900 but skips 600; Readex Pro is variable 160-700 with matched Latin; Noto Sans Arabic runs 100-900 while Noto Naskh Arabic stops at 700.
- Regional rows exist because regional audiences notice: using a Gulf-market geometric face for West African or South Asian text is a courtesy failure, not just an aesthetic one.
- The floors are starting points; run your own content at production sizes before freezing a leading token.

## Worked example

A bilingual English/Arabic analytics dashboard, one codebase, equal fidelity in both locales:

1. Requirements: real RTL layout, numeric tables, mixed Arabic/Latin strings (product names, user names), and a Latin brand face already in place (IBM Plex Sans).
2. Fonts: IBM Plex Sans Arabic as the Arabic primary for its shared design language with IBM Plex Sans; Noto Sans Arabic at the end of the stack as a deliberate safety net.
3. Direction: the Arabic locale sets dir="rtl" at the root; every component uses logical properties (padding-inline, margin-inline, text-align: start), so no component carries an RTL fork.
4. Leading: a line-height token per language - Latin 1.4, Arabic 1.6 applied through :lang(ar) - instead of one global compromise that clips hamza stacks or balloons the English side.
5. Controls: buttons, inputs, and list rows get fixed heights and explicit line-height so the taller Arabic line box cannot resize them when the locale flips.
6. Numerals: the i18n layer formats Western digits for en and Arabic-Indic U+0660-0669 for ar; table columns request tabular figures, and the Arabic face's digit forms are checked against the same table style.
7. Mixed runs: user-generated segments are wrapped in bdi; an English product name inside an Arabic sentence must read as a clean isolated run, not scrambled punctuation.
8. Shaping verification: lam-alef renders as one ligature; medial forms join on both sides; a real navigation string is proofed by an Arabic-reading reviewer in both directions.
9. Digit-system audit: every surface uses one digit system per locale, with no Western and Arabic-Indic digits mixed inside a single component.
10. Browser verification: Chromium, Firefox, and WebKit all pass; the rendered-fonts inspector confirms no silent system-font substitution in either locale.

Outcome: one component tree, two direction values, per-language leading tokens, and no mirrored typography - only direction-aware icons flip.

## Field notes

- If the stack omits an Arabic webfont, platform substitutes differ sharply: Android defaults to Noto Naskh Arabic, macOS to Geeza Pro, Windows covers Arabic inside Segoe UI. Audit the no-webfont path on purpose; it is what blocked CDNs and low-end devices show.
- Kashida justification is unreliable through CSS; engines implement it differently or not at all. Justify by word spacing if you must justify, or accept ragged edges as the typographically honest default.
- Users sometimes type tatweel (U+0640) to stretch a word for emphasis or alignment; do not strip it in text normalization pipelines.
- Amiri carries extensive support for Quranic composition conventions and annotation; content containing Quranic text should be proofed with real surah strings, not ordinary prose samples.
- Scheherazade New trades compactness for clarity and breadth; it runs visually large for its nominal size, so size it down a step when matching against Latin neighbors.
- Vazirmatn is the widely used open Persian UI face; verify the four Persian letters and Eastern digits U+06F0-06F9, and remember Persian sets dir="rtl" identically to Arabic.
- Urdu content adds letters and carries Nastaliq expectations that a Naskh UI font will not satisfy; decide explicitly whether Urdu gets literary-style treatment or a documented compromise.
- The rendered-fonts inspector is the fastest way to catch silent fallback with the wrong weight inside an otherwise correct layout.
- Testing join quality with isolated letters is worthless; paste connected words, ideally drawn from your own domain vocabulary and real user names.
- Arabic has no letter case, so hierarchy must come from weight, size, and spacing; uppercase-transform-based hierarchy systems simply stop working in the Arabic locale.
- A font can map the whole Arabic block and still shape poorly; GSUB quality for contextual forms and ligatures is the real variable between superficially similar Naskh faces.
- Watch icon libraries: many ship Western-centric arrow and progress metaphors that need direction-aware variants, while typographic elements must never be mirrored.
- Numeric cells with ranges or separators (dates, totals, phone-style strings) can reorder inside an RTL layout; wrap computed numeric output in dir="ltr" when the visual order breaks.
- Arabic webfonts are small enough to self-host whole; if you do subset, keep the layout features intact (--layout-features="*" in pyftsubset terms) or the contextual forms and ligatures silently break.
- Template-generated strings (errors, confirmations, receipts) embed Latin variables inside Arabic sentences; test the rendered template output, not just the static copy.
- Display scale steps need separate proofing per language; an Arabic headline scale reused verbatim from Latin usually needs its own size and leading checks at the top of the scale.

## Quick reference

- Direction: dir="rtl" on the document or section; dir="auto" on unpredictable user content; bdi around embedded foreign segments.
- Layout: logical properties only (padding-inline, margin-inline, text-align: start); flip directional icons and progress indicators, never mirror type.
- Leading: Arabic body starts at 1.6; Nastaliq takes the font's own metrics as the floor.
- Never: letter-spacing on Arabic, string reversal in code, Presentation Forms codepoints U+FB50-FDFF and U+FE70-FEFF in content, uppercase assumptions on caseless text.
- Digits: per locale - Western, Arabic-Indic U+0660-0669, or Eastern U+06F0-06F9 - formatted in the i18n layer, never hardcoded.
- Shaping smoke test: lam-alef as one ligature, medial forms joining on both sides, real words rather than isolated letters.
- Stack pattern: Arabic primary first, Noto Sans Arabic as safety net last; expect digits and punctuation to come from the primary face.
- Pairing check: match Latin and Arabic on apparent size, weight, and aperture; expect to size Arabic up slightly at equal nominal size.
- RTL form check: every input, placeholder, validation message, and button label tested in the Arabic locale before sign-off.
- Persian and Urdu gate: the four Persian letters plus Eastern digits for Persian; the full letter inventory plus a Nastaliq decision for Urdu.
- Justification: word spacing or ragged edges; kashida only where the engine genuinely supports it.
- Documentation: record the chosen digit system, direction handling, and leading tokens alongside the font stack in the design tokens.
- Re-proof shaping after any font version bump; foundries quietly change contextual forms and ligature sets between releases.

## Cross-references

- [Mixed script fallbacks](mixed-script-fallbacks.md)
- [Hebrew script typography](hebrew-script-typography.md)
- [Localization and RTL accessibility](../accessibility/localization-and-rtl-accessibility.md)
- [Web and SaaS interfaces](../applications/web-and-saas-interfaces.md)

Compiled 2025 as part of the Fontlore project.
