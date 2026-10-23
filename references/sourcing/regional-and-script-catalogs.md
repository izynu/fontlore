# Regional and Script Catalogs

What this reference covers: Foundries and catalogs that lead in non-Latin scripts: India (ITF, Ek Type), Thailand (Cadson Demak), and multi-script specialists like Rosetta, TypeTogether, Boutros, and 29LT, plus practical pointers for Arabic, Hebrew, and Thai sourcing. Latin-only teams get the audit skills to judge script quality honestly.

Script expertise is not evenly distributed. A foundry that has designed within a script's traditions for decades will beat a Latin foundry adding a script for checkbox coverage. This guide maps who to trust for which scripts and how to evaluate their work.

## Why script specialization matters

- Complex scripts carry shaping rules, conjuncts, contextual forms, and historical styles that cannot be improvised from a Latin design.
- Coverage counts lie: a font can include Devanagari code points while setting them with broken conjuncts or mismatched optical weight against its Latin.
- Specialist foundries publish in both directions (script plus Latin) because real documents mix them, which is exactly the pairing quality generalist catalogs miss.

## India: ITF and Ek Type

- The Indian Type Foundry built its reputation on Indian scripts plus Latin. Its Google Fonts work includes Poppins (with Jonny Pinhorn and Ninad Kale) and the Hind series, all pairing Devanagari with Latin under open licenses.
- Fontshare, ITF's free platform, carries bilingual families such as Panchang alongside retail-grade Latin-only designs like Satoshi.
- Ek Type, the Mumbai collective, published Baloo (a multi-script heavy rounded family) and Mukta (Devanagari plus Latin) on Google Fonts.
- When a project needs Devanagari with Latin that actually matches in color and scale, start here rather than with a Latin family's token Devanagari.

## Thailand: Cadson Demak

- Cadson Demak is the reference Thai foundry, with a long catalog of Google Fonts families including Prompt, Kanit, Mitr, Chakra Petch, Bai Jamjuree, and Sarabun.
- Thai type divides into looped traditional styles and loopless modern styles; Cadson Demak helped define the contemporary loopless genre that suits UI and signage.
- Thai rendering interacts with tone marks and vowels above and below the base line; verify mark positioning at small sizes and with stacked combinations, not just single characters.

## Multi-script independents

- Rosetta, founded by David Brezina, specializes in multi-script families built from research (Skolar is its best-known system), with genuine attention to how scripts harmonize.
- TypeTogether (Veronika Burian and partners) publishes text-focused families like Bree, Adelle, and Literata, the latter commissioned for Google Play Books, with a track record in script extensions.
- Boutros brings decades of Arabic and Latin corporate typography, with emphasis on Arabic-Latin compatibility for brand systems.
- 29LT, founded by Pascal Zoghbi, publishes contemporary Arabic families such as Bukra and Zarid designed natively in Arabic rather than adapted from Latin.
- These foundries price like commercial foundries because the engineering is commercial-grade; budget accordingly instead of forcing a free fallback.

## Arabic, Hebrew, and Thai pointers

- Arabic: 29LT and Boutros for brand-grade work; Google Fonts' Arabic filter for open options; verify shaping in a browser, not a design tool.
- Hebrew: the open-source Culmus project collects Hebrew fonts; Google Fonts Hebrew filter for modern faces; check niqqud (vowel point) handling if liturgical or educational text is in scope.
- Thai: Cadson Demak's catalog plus the Google Fonts Thai filter; test line breaking, since Thai has no spaces between words and relies on dictionary-based breaking.
- For depth beyond catalogs, Noto provides a structural baseline per script, and SIL covers literacy-oriented depth for some languages.

## Workflow

1. List the scripts and languages in the brief, including growth markets, not just current content.
2. For each script, shortlist one specialist source and one generalist fallback (Noto layer).
3. Test with real paragraphs in the script, at real sizes, in the real rendering stack.
4. Check numerals policy: Arabic-Indic vs European digits, and whether the family offers both.
5. Record the specialist foundry, license, and version for each script in the manifest.

## Common mistakes

- Treating Arabic as right-to-left Latin and shipping a face with graceful Latin and cramped Arabic.
- Judging script quality from glyph coverage listings instead of shaped paragraphs.
- Ignoring vertical metrics mismatches between scripts, which wreck line rhythm in mixed-script paragraphs.
- Assuming a Latin family's "supports Devanagari" claim means quality Devanagari; it usually means coverage.
- Skipping the numerals question until localization QA fails.

## Decision rules

- One dominant non-Latin script with brand importance: hire or license the specialist foundry for that script.
- Long tail of many scripts: Noto layers for structure, specialists for the two or three scripts users see most.
- Budget-constrained and multilingual: prefer open-source families designed by specialists (ITF, Ek Type, Cadson Demak on Google Fonts) over Latin-first families with token coverage.
- Any mixed-script system: define per-script stacks deliberately; never let a single font-family declaration try to do everything.

## Comparison table: scripts and specialists

| Script | Specialist sources | Open-source starting points | What to test |
| --- | --- | --- | --- |
| Devanagari | ITF, Ek Type | Poppins, Hind, Mukta, Baloo 2, Tiro Devanagari Hindi | Conjuncts, matras, danda, Latin-Devanagari color match |
| Tamil and other Indic | Ek Type's Mukta series branches | Mukta Malar (Tamil), Mukta Mahee (Gurmukhi), Mukta Vaani (Gujarati), Noto per-script | shaping of reph and vowel signs, numerals |
| Thai | Cadson Demak | Prompt, Sarabun, Mitr, Chakra Petch, IBM Plex Sans Thai | Tone-mark stacking, looped versus loopless style, word breaking |
| Arabic | 29LT, Boutros | Cairo, Amiri, IBM Plex Sans Arabic, Almarai, Noto Naskh Arabic | Shaping in a browser, RTL punctuation, digit policy |
| Hebrew | Culmus project | David Libre, Frank Ruhl Libre, Heebo, Rubik | Niqqud placement if liturgical or educational text is in scope |
| Vietnamese | TypeTogether and text foundries | Be Vietnam Pro, Literata, Source Sans 3 | Stacked tone marks on lowercase and capitals at small sizes |

The Mukta series is the pattern to notice: one design language expressed per script by a specialist team, which is exactly the bilingual quality generalist catalogs rarely hit.

## How to audit a script you cannot read

- Recruit a native reader before the audit, not after; a thirty-minute review with a real reader beats a week of glyph-grid staring.
- Compare against reference setting: national newspapers, government portals, and leading publishers in that language show what competent setting looks like.
- Test in the browser with the production stack. Design tools apply their own fallbacks and hide shaping failures that users will hit.
- Push the extremes: stacked marks, long unbroken strings, all-caps Latin next to the script, numerals inside the script's text, and the smallest size the UI will ever use.
- Check vertical metrics by paragraph, not by glyph: line rhythm between scripts is where mismatched ascenders and descenders show up.
- Write down what the reader approved and at what sizes; "a native speaker said it looks fine" is only evidence when it is dated and specific.

## Worked example: Arabic-Latin brand system

Scenario: a brand designed in Latin needs equal-quality Arabic across signage, web, and packaging.

1. Decide the pairing strategy: a bilingual family designed natively in both scripts (29LT families pair Arabic with Latin by design), or a matched pair such as IBM Plex Sans Arabic with IBM Plex Sans, engineered as companions.
2. Reject any Arabic that is a Latin design with added Arabic code points; the toothpaste-tube tell is disconnected letters with Latin rhythm and cramped joins.
3. Test mixed-direction paragraphs: Latin product names inside Arabic sentences, punctuation at direction boundaries, and numerals in both policies (Arabic-Indic and European digits).
4. Verify optional diacritics behavior if religious or educational content might appear, since diacritic placement quality separates serious Arabic faces from marketing ones.
5. Confirm the license covers the markets and media in the brand plan; several specialist foundries price regions and media separately.
6. Record the Arabic and Latin families as one system decision with one evidence trail, because they will be replaced together if either fails.

## Field notes

- Cadson Demak's reach extends beyond Thai: the studio has contributed open Thai-Latin systems like IBM Plex Sans Thai in looped and loopless variants, which is why IBM's Thai presence looks native rather than appended.
- Sarabun descends from the Thai government's official document face lineage; for bureaucratic contexts it reads as native infrastructure, which can be a feature.
- Amiri, by Khaled Hosny, revives the Bulaq Press type tradition; it is the reference open Naskh for book-length Arabic and religious scholarship.
- Ek Type's Baloo began as a single heavy rounded design and later grew into the multi-script Baloo 2; check which generation your source ships, since the old single-style files still circulate.
- Thai has no spaces between words, so line breaking depends on dictionary-based algorithms; test paragraph-level breaking, not just glyph-level rendering.

## Signals to trust

- Foundries whose teams live inside the script's traditions: published research, native-speaker designers, and catalogs spanning decades of the script.
- Bilingual families designed in both directions at once, where Latin and script share weight structure and optical scale by design.
- Google Fonts entries from specialist foundries (ITF, Ek Type, Cadson Demak): open licenses plus specialist craft is the best value in multilingual typography.
- Reference setting in the target language's leading publications, which shows the traditions your choice will be judged against.

## Signals to distrust

- Coverage checkboxes on Latin-first families; "supports Arabic" often means code points, not craft.
- Specimen images instead of live text; images hide shaping and can be generated in any tool.
- Claims of unified multilingual families that behave identically everywhere; per-script strengths and weaknesses are the norm, not the exception.
- Rendering tests done only in design tools; shaping engines differ, and browsers are where most users live.

## Questions to ask a specialist foundry

- Which weights and styles exist for the non-Latin scripts, and do they match the Latin range we need?
- How does the family handle mixed-script paragraphs: are vertical metrics tuned for them, or do we adjust line height per script?
- What numeral policies are supported (European digits, script digits, both), and how are they selected?
- Is there guidance for our rendering stack (web, iOS, Android, print), and who has shipped this family at scale in our context?
- What does support look like when a shaping bug appears: response time, fix path, and version policy?

## Quick reference: the contact sheet

A one-look version of who leads where, with the first question to put to each:

| Script | First contacts | Ask first about |
| --- | --- | --- |
| Devanagari plus Latin | Indian Type Foundry, Ek Type | Bilingual weight matching and conjunct quality at UI sizes |
| Other Indic scripts | Ek Type's Mukta branches; Tiro Typeworks' open releases | Per-script designs, not one pan-Indic file |
| Thai | Cadson Demak | Looped versus loopless choice and mark stacking at small sizes |
| Arabic | 29LT, Boutros | Native Arabic design, digit policy, brand-grade weight range |
| Hebrew | Culmus project, Google Fonts Hebrew filter | Niqqud handling if vowelized text is in scope |
| Multi-script systems | Rosetta, TypeTogether | Vertical metric tuning across scripts in mixed paragraphs |
| Structural baseline | Noto, SIL | Fallback coverage beneath the specialist faces |

Tiro Typeworks' open releases (the Tiro Devanagari and sibling families on Google Fonts) are reference-grade starting points for several Indic scripts, which is why they appear in the comparison table above even though the studio is not a volume retailer.

## Audit checklist: non-Latin adoption gate

- [ ] Each script in the brief has a named specialist source and a named fallback (the Noto layer) in the manifest.
- [ ] Real paragraphs, not glyph grids, tested in the production browser stack at production sizes.
- [ ] A native reader reviewed the setting; the review is dated and specific about sizes and content.
- [ ] Mixed-script paragraphs checked for line rhythm: ascender and descender clashes between Latin and the script.
- [ ] Mark stacking tested with two- and three-level combinations, not single characters.
- [ ] Numerals policy decided per script and confirmed available in the family.
- [ ] Weights and italics available in the script match the Latin token scale, or the gap is documented.
- [ ] Vertical metrics of the chosen faces compared; per-script line-height rules written as tokens.
- [ ] License verified per script family; specialist faces are frequently priced per script or per region.
- [ ] Failure plan recorded: which face covers glyphs the primary lacks, declared in the CSS stack.

## Cross-references

- [Noto and SIL fonts](noto-and-sil-fonts.md)
- [Fontshare and ITF free fonts](fontshare-and-itf.md)
- [License families compared](../licensing/license-families-compared.md)
- [Choosing body typefaces](../selection/choosing-body-typefaces.md)

Compiled 2025 as part of the Fontlore project.
