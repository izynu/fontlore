# Cyrillic and Greek Coverage

What this reference covers: What Cyrillic and Greek coverage actually require beyond the subset label, including Serbian italic conventions, Macedonian letters, and polytonic Greek. It lists reliable open families and a codepoint checklist you can run before committing.

## The two Cyrillic tiers

Google Fonts labels Cyrillic support in two levels, and the split matters:

- cyrillic: the core set used by Russian, Ukrainian, Belarusian, Serbian, Bulgarian, and Macedonian, roughly U+0410-044F plus the national additions up to U+04FF. In practice the core subset covers the letters these languages need day to day.
- cyrillic-ext: extended and historic letters, including Old Church Slavonic forms and combining marks, roughly U+0460-052F plus combining ranges.

If your content is modern Slavic languages, the plain cyrillic subset is usually enough. Historic or liturgical text needs cyrillic-ext, and coverage there is patchy outside dedicated families.

## Language-specific letters to verify

- Russian: the full basic alphabet, including hard and soft signs U+044A and U+044C, and the i-kratkoye pair U+0439 and U+0419.
- Ukrainian: U+0454 (Ukrainian ye), U+0456 (Byelorussian-Ukrainian I), U+0457 (yi), and U+0491 (ge with upturn), the letter most often missing in fonts with thin Cyrillic.
- Serbian: U+0402, U+0405, U+0408, U+0409, U+040A, U+040B, U+040F and lowercase counterparts. Serbian also has its own italic conventions, discussed below.
- Macedonian: U+0403 (gje) and U+045C (kje) on top of the Serbian set.
- Bulgarian: standard Cyrillic, but Bulgarian traditionally uses paired low and high quotation marks; check the glyph shapes if quotes matter.

## Serbian italic: the classic trap

In Serbian typographic tradition, italic Cyrillic uses cursive letterforms that look very different from the upright forms: letters such as b, g, d, p, and t become handwritten-style shapes, and a Serbian reader can parse them at speed while a Russian-style italic can look foreign or wrong.

- Few families implement these as true alternates; when they exist they are usually wired to the locl feature and triggered by the Serbian language tag.
- Test: set a Serbian string in italic with `lang="sr"`, then compare with `lang="ru"`. If the glyphs are identical, the font is not offering Serbian forms.
- Families worth checking for this include PT Sans and PT Serif, Literata, Noto Serif, and a few ParaType releases. If the font lacks Serbian italic forms, decide explicitly whether that is acceptable, and document it.

## Greek coverage and polytonic

Greek likewise splits into two tiers:

- greek: monotonic Greek, U+0370-03FF, used for all modern Greek text. This is what most sites need.
- greek-ext: Greek Extended, U+1F00-1FFF, the polytonic system with breathing marks and layered accents used for Ancient Greek and traditional texts.

Verify on any candidate font:

- Final sigma U+03C2 exists and is distinct from sigma U+03C3.
- The Greek question mark U+037E, which looks like a semicolon, renders correctly.
- Accented capitals and the diaeresis combinations: U+0386, U+0388-038A, U+038C, U+038E-038F.
- For polytonic work, spot check layered marks such as U+1F04 or U+1F71-adjacent forms; many display serifs draw these poorly or omit them.

Families with genuinely good Greek: Gentium Plus (SIL, excellent polytonic), GFS Didot (Greek Font Society), Cardo (strong polytonic, aimed at classics scholarship), Noto Sans and Noto Serif, Literata, EB Garamond, and Source Serif 4 for monotonic text. PT Sans and PT Serif also carry solid monotonic Greek.

## Reliable Cyrillic families

- PT Sans, PT Serif, PT Mono: ParaType designs from the "Public Types of Russian Federation" project by Alexandra Korolkova and colleagues; workhorse quality at every size.
- Golos Text: Paratype's contemporary UI-style sans with strong Russian roots.
- Literata: TypeTogether's book serif with confident Cyrillic, a good body choice.
- Lora: a widely used serif with mature Cyrillic from Cyreal.
- Playfair Display: high-contrast display serif with usable Cyrillic headlines.
- Fira Sans, Source Sans 3, Inter, Roboto, Manrope: UI sans families with Cyrillic included, each slightly different in voice.
- Noto Sans and Noto Serif: neutral defaults when you need Cyrillic alongside many other scripts.

## Weight and style parity checks

Cyrillic and Greek often receive less design attention than Latin within the same family, so compare across styles before you commit:

- Set the same string in regular and bold; look for soft, mushy bolds or caps that are too wide.
- Check italic: some families fake it or ship italic with reduced coverage.
- Compare Cyrillic x-height with Latin x-height in mixed lines such as product names; mismatched proportions read as a mistake.
- Check digits and currency: tables mixing Latin and Cyrillic should keep tabular figures aligned across both.

## Common mistakes

- Assuming a famous Latin family has Greek; many popular UI families ship Latin and Cyrillic but no Greek, or Greek only in a separate sibling release.
- Testing Cyrillic with Russian only, then shipping to a Serbian or Macedonian audience with missing letters.
- Using Russian italic for Serbian text and calling it a style choice; Serbian readers notice immediately.
- Grabbing a beautiful display serif for Ancient Greek without checking Greek Extended coverage, then discovering breathing marks are tofu.
- Mixing two fonts' Cyrillic of different design generations in one interface; the seam is visible even to non-readers.

## Decision rules

- Russian or Bulgarian content, neutral tone: Noto Sans, PT Sans, or Inter are safe defaults.
- Editorial Cyrillic: Literata or Lora for body, Playfair Display or a ParaType display for headlines.
- Ukrainian audience: run the U+0491 check first; it eliminates many candidates instantly.
- Serbian with meaningful italic use: shortlist families that implement locl Serbian italics, and verify visually.
- Modern Greek only: monotonic coverage from Noto, Literata, Source Serif 4, or GFS Didot is enough.
- Ancient or polytonic Greek: Gentium Plus or Cardo; do not improvise with display serifs.

## Comparison table

Open families compared on the dimensions that decide this category. Cyrillic and Greek columns describe the practical depth, not just subset presence:

| Family | Cyrillic | Greek | Voice | Watch-outs |
| --- | --- | --- | --- | --- |
| PT Sans, PT Serif, PT Mono | Core set, mature | Solid monotonic | Institutional workhorse | The reference implementation of Serbian italic tradition; verify locl |
| Golos Text | Russian-focused, contemporary | none | Modern UI sans | Latin is secondary to the Cyrillic |
| Literata | Core set, confident | Monotonic | Book serif for reading | Display cuts need spot checks |
| Lora | Core set, mature | none | Editorial serif | No Greek; do not use for Greek audiences |
| Playfair Display | Usable headline Cyrillic | none | High-contrast display | Caps-heavy Cyrillic needs review |
| Inter | Core plus extended | Monotonic plus extended | Neutral UI sans | Many alternates behind features; check defaults |
| Source Sans 3 | Core plus extended | Monotonic | Humanist sans | Good all-rounder for mixed audiences |
| Fira Sans | Core set | Monotonic | Humanist UI sans | Check current weight list before committing |
| Noto Sans, Noto Serif | Core plus extended | Both tiers, strong | Neutral connective tissue | Blandness is the price of coverage |
| Gentium Plus | Extended | Polytonic, excellent | Scholarly text face | Not a UI face; text sizes only |
| GFS Didot, Cardo | Minimal or none | Didot tradition; polytonic classics | Greek-first designs | Check Cyrillic before mixed use |

Notes on the table:

- "None" in the Greek column is common and not a defect; it only becomes one when a Greek locale ships without a Greek-capable font in the stack, and the platform serif quietly substitutes.
- The cyrillic-ext tier is where families diverge most; Noto Serif and Gentium Plus are the reliable choices for historic or liturgical text.
- Weight lists change between releases; re-check the weight range of any family here before locking a system that needs hairline or black cuts.

## Worked example

A documentation site serving Russian, Ukrainian, and Serbian readers, with code blocks and bold/italic prose:

1. Requirements: three Slavic languages, technical content, tables of identifiers, no Greek in scope.
2. Checklist first: the Ukrainian ge with upturn U+0491, the Serbian letters U+0402/U+0405/U+0408/U+0409/U+040A/U+040B/U+040F, and the Macedonian pair U+0403 and U+045C are run against every candidate before design opinions form.
3. Serbian italic test: the same Serbian sentence is set in italic with lang="sr" and lang="ru". One strong serif candidate renders identical glyphs for both, meaning no Serbian cursive forms; the decision to accept or reject is made consciously and recorded.
4. Shortlist outcome: a book serif from the reliable list for body text and a neutral UI sans for interface chrome, both confirmed on the full checklist.
5. Bold parity: Cyrillic bolds are compared against Latin bolds in mixed headings; one candidate's Cyrillic bold runs visibly wider and is rejected for navigation labels.
6. Digits and identifiers: tabular figures hold alignment across Cyrillic and Latin strings in the same table column.
7. Language tags: lang="ru", lang="uk", lang="sr" are set per locale so locl-driven behavior has a chance to work.
8. Cross-browser proof: Chromium, Firefox, and WebKit, because locl support and fallback behavior differ.

Outcome: one stack that passes all three languages, with the Serbian italic compromise either resolved by family choice or documented as a known limitation.

## Field notes

- The rendered-fonts inspector plus the lang attribute is the fastest locl test: flip lang="sr" to lang="ru" on an italic string and watch which glyphs change.
- Bulgarian quotation convention favors paired low and high marks, and readers notice Latin-style quotes; test with real Bulgarian strings rather than assuming the Russian convention transfers.
- Uppercasing Greek text must map final sigma U+03C2 to regular capital sigma; browsers do this correctly for properly tagged text, but hand-rolled case transforms can get it wrong.
- Cyrillic bold tends to widen more than Latin bold in some families; navigation and button labels are where the widening shows first.
- Historic Cyrillic (yat, yer forms, Old Church Slavonic) lives in cyrillic-ext and is patchy; only dedicated families and Noto Serif are dependable there.
- Monotonic Greek is nearly universal in good families; polytonic is where breathing marks and layered accents fail, and display serifs fail most often.
- Mixing Cyrillic from two design generations (a ParaType-era text face next to a modern geometric sans) reads as a seam even to non-readers; keep one Cyrillic voice per surface.
- Ukrainian text with a font that lacks U+0491 falls back per character, producing a hybrid alphabet in the middle of words; this failure is invisible until a real Ukrainian string is rendered.
- Greek text embedded in Latin UI labels: keep lang="el" on the run so the question mark and sigma behavior stay correct inside foreign context.
- When a family's Greek exists but is visibly less finished than its Latin (shaky accents, uneven widths), treat it as a soft fail and compare against Noto before deciding.

## Quick reference

- Subsets: cyrillic versus cyrillic-ext; greek versus greek-ext. Modern Slavic languages need the plain tier; polytonic Greek needs greek-ext.
- Ukrainian gate: U+0454, U+0456, U+0457, U+0491. Serbian gate: U+0402, U+0405, U+0408, U+0409, U+040A, U+040B, U+040F. Macedonian adds U+0403 and U+045C.
- Greek gate: U+03C2 final sigma, U+037E question mark, accented capitals U+0386 through U+038F; polytonic adds U+1F00-1FFF spot checks.
- Language tags: lang="ru", lang="uk", lang="sr", lang="bg", lang="mk", lang="el" - they drive locl and case behavior.
- Serbian italic test: same string, lang="sr" versus lang="ru"; identical glyphs mean no Serbian cursive forms.
- Defaults: Noto Sans or PT Sans for neutral UI; Literata or Lora for editorial body; Gentium Plus or Cardo for polytonic; GFS Didot for Greek classical voice.
- Weight parity: compare Cyrillic and Latin bolds side by side in mixed strings before freezing weights.
- Verification: rendered-fonts inspector in three browser engines, plus hb-shape when a locl result looks suspicious.

## Cross-references

- [Latin and extended coverage](latin-and-extended.md)
- [Testing multilingual coverage](testing-multilingual-coverage.md)
- [OpenType features](../technical/opentype-features.md)
- [Localization and RTL accessibility](../accessibility/localization-and-rtl-accessibility.md)

Compiled 2025 as part of the Fontlore project.
