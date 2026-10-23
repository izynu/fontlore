# Noto and SIL Fonts

What this reference covers: The two workhorse sources for script coverage: Google's Noto project and SIL International's font catalog. It covers how each project is organized, when to reach for which, and how to use them to fill coverage gaps that mainstream families cannot.

When a project needs scripts beyond polished Latin, most commercial families fail you. Noto and SIL fonts exist precisely for this situation: Noto aims at uniform coverage across every script, while SIL publishes literacy-focused fonts with deep extended Latin, IPA, and minority-language support.

## The Noto project structure

- Noto's goal is famously "no more tofu": a family for every script, with matching weights and consistent metrics so mixed-script text does not lurch between styles.
- The project is organized per script. Historically you picked Noto Sans Devanagari, Noto Sans Thai, Noto Sans Hebrew, and so on, each a separate family with its own releases.
- Development happens in per-script repositories under the notofonts GitHub organization, with releases, issue trackers, and QA per script family.
- Newer unified builds merge many scripts into single variable fonts that share a design language across scripts; check current releases because this area evolves quickly.
- Noto Sans and Noto Serif anchor the Latin, Greek, and Cyrillic core; Noto Sans Mono covers code; Noto Emoji and Noto Color Emoji cover symbols.
- Variable builds typically expose weight and width, letting one file serve a whole UI system.

## Using Noto for coverage

- Treat Noto as the fallback layer of record: define your primary family for each script, then let Noto cover the long tail of unexpected characters and languages.
- Because per-script families share metrics and weight structure, pairing Noto Sans Devanagari with your Latin sans is far less jarring than pairing two unrelated families.
- Check shaping quality in a real shaping engine, not a design tool preview. Noto's per-script repos ship test suites, and complex scripts (Indic, SEA, Arabic) must be tested with their actual shaping rules.
- For CJK, Noto Sans JP/KR/SC/TC derive from Source Han fonts, jointly developed with Adobe. Coverage is excellent; file size and subsetting strategy become the real design problem.

## The SIL catalog

- SIL International is a language-development non-profit and the author of the SIL Open Font License itself. Its fonts are OFL-licensed and free for any use including commercial.
- Gentium Plus, by Victor Gaultney, is a graceful serif with exceptional extended Latin and IPA coverage, built for literacy and linguistics work.
- Charis SIL and Doulos SIL both descend from Matthew Carter's Charter design; Charis is the text workhorse, Doulos the companion with a more traditional look. Both carry deep diacritic coverage.
- Andika, also by Victor Gaultney, is designed explicitly for beginning readers: large x-height, open apertures, and letterforms that match how children are taught to write.
- Scheherazade New is SIL's Arabic entry, a traditional Naskh with wide coverage and support for OpenType and Graphite smart font features.
- SIL fonts frequently support Graphite in addition to OpenType, which matters in niche rendering environments (notably some language-software stacks) where OpenType coverage is thin.

## When to choose SIL over Noto

- Minority languages and extended Latin: SIL's diacritic engineering is deeper for unusual combinations (tone marks, double diacritics, rare letters).
- Literacy and education contexts: Andika exists specifically because beginner readers need unambiguous letterforms that most text faces do not provide.
- IPA and linguistic publishing: Gentium Plus is the de facto standard for linguistics documents.
- Arabic with traditional flavor: Scheherazade New offers a classical Naskh where modern Arabic sans faces would look wrong.
- For a consistent product-wide system, Noto usually wins; for script depth in specific languages, SIL often wins. Many projects use both.

## Workflow

1. Inventory every script and language your content touches, including edge cases like IPA, transliteration, and archaic characters.
2. Pick a primary family per script from your normal sourcing process.
3. For gaps, search Noto first for structural consistency, then SIL for diacritic and literacy depth.
4. Test real content through a real text stack: shaping, fallback order, line breaking, and numeral contexts.
5. Record which family covers what, so future maintainers know why Noto Sans Armenian sits in the stack.

## Common mistakes

- Assuming one "global" family covers everything equally well; every multilingual family has strong and weak scripts.
- Testing coverage in a design tool only, where fallback silently hides shaping failures.
- Forgetting Noto Emoji-style symbol fonts when content includes emoji, then shipping tofu in production.
- Using a literacy font like Andika as a general brand face; it is built for a specific job.
- Mixing too many fallback families, producing ransom-note body text; prefer metric-compatible Noto layers for the tail.

## Decision rules

- Product UI with unpredictable user content: primary family for Latin, Noto layers for everything else.
- Educational or linguistic publishing: start from SIL (Andika or Gentium Plus), add Noto for remaining scripts.
- Arabic with traditional reading contexts: Scheherazade New over geometric Arabic sans faces.
- If coverage is the whole brief, prioritize the family with the deepest language list in the google/fonts metadata and confirm in specimens.

## Comparison table: Noto versus SIL

| Dimension | Noto | SIL International |
| --- | --- | --- |
| Mission | Uniform coverage across every script | Literacy, linguistics, minority-language depth |
| Strength | Breadth and metric consistency | Extended Latin, IPA, diacritic engineering |
| Organization | Per-script families plus unified builds | Focused catalog of text-oriented families |
| Rendering | OpenType shaping | OpenType plus Graphite smart fonts |
| License | OFL / Apache per project | OFL (SIL wrote the license) |
| Best role | Fallback layer and multi-script baseline | Deep coverage for specific languages |

## Named families worth knowing

- Noto Sans and Noto Serif anchor the Latin, Greek, and Cyrillic core; Noto Sans Mono covers code; use these as the spine of a fallback stack.
- Noto Sans JP, KR, SC, and TC descend from the Source Han project developed jointly with Adobe; coverage is excellent and subsetting strategy becomes the real engineering problem.
- Noto Sans Devanagari, Noto Sans Thai, Noto Sans Hebrew, and Noto Sans Arabic are the per-script workhorses for UI fallback.
- Noto Emoji and Noto Color Emoji cover symbols; monochrome Noto Emoji suits print and single-color UI.
- Noto Sans Math and Noto Sans Symbols plug specific gaps that otherwise produce tofu in scientific or technical content.
- Gentium Plus (Victor Gaultney) is the de facto standard serif for linguistics publishing, with deep IPA and extended Latin coverage.
- Charis SIL and Doulos SIL descend from Matthew Carter's Charter design; Charis is the text workhorse, Doulos the more traditional companion.
- Andika, also by Victor Gaultney, is built for beginning readers: large x-height, open apertures, letterforms matching how children are taught to write.
- Scheherazade New provides a traditional Naskh Arabic with wide coverage; Abyssinica SIL covers Ethiopic; Awami Nastaliq covers Nastaliq with Graphite-dependent features, so verify your stack supports it.

## Worked example: fallback stack for a Hindi-English product

Scenario: a government-facing web product runs English UI copy with Hindi content, on a stack where users may paste anything.

1. Set the Latin primary deliberately (say IBM Plex Sans), then declare Noto Sans Devanagari explicitly for Devanagari ranges; never rely on generic `sans-serif` fallback luck.
2. Test conjunct forms and matras with real words, not the glyph grid: conjunct clusters, post-base and above-base matras, and the danda character.
3. Raise line-height for Devanagari-heavy text; the shirorekha and stacked marks need more vertical room than Latin defaults, commonly 1.5 and up at body sizes.
4. Decide the numerals policy: Devanagari digits, European digits, or both, and verify the chosen family offers the forms the content requires.
5. Add Noto Sans Mono for code contexts if the product shows any, and Noto Color Emoji if user content can include emoji; missing symbol coverage is the classic late-stage surprise.
6. Record per-script coverage in the manifest so the next maintainer knows why each Noto family sits in the stack.

## Field notes

- Noto's per-script repositories under the notofonts GitHub organization release independently; a fix in one script does not imply anything about another script's timeline.
- For CJK, file size is the design problem: pick the region-specific family (JP, KR, SC, TC) and lean on unicode-range subsetting rather than shipping a monolith.
- Graphite support in SIL fonts matters in niche language-software stacks, but most browsers only honor OpenType; a Graphite-only feature will fail silently on the web.
- Using a literacy font like Andika as a general brand face undersells the design and the brand; it is built for a specific job.
- Mixed-script vertical metrics differ; when body text lurches in line height between scripts, check ascender and descender values rather than guessing at line-height hacks.

## Questions to ask when coverage fails

- Which code point exactly is failing: is it missing from the font, present but wrongly shaped, or shaped correctly but positioned badly?
- Does the failure reproduce in a real browser with the production font stack, or only in a design tool with its own fallback behavior?
- Is there a Noto family covering the script, and does its weight range match the primary family's used weights?
- For minority languages, does SIL have deeper coverage than Noto, and do the required features need Graphite?
- Who on the team can read the script well enough to judge the fix, or can we recruit a native reviewer?

## Signals to trust

- Per-script repositories with active issue trackers and releases; Noto's development is unusually public for a font project of this size.
- SIL's documentation, which explains design intent, coverage decisions, and rendering requirements (OpenType versus Graphite) in plain language.
- Metric compatibility within the Noto per-script families, which is deliberate engineering and the reason they make reliable fallback layers.
- Specimens that show real paragraphs in the target language, which both projects provide in quantity.

## Signals to distrust

- The assumption that any one Noto build covers everything equally; per-script quality and coverage vary, and the project says so.
- Coverage counts as quality; a glyph list does not tell you whether shaping rules work in your stack.
- Design-tool previews for complex scripts; they apply private fallback logic that hides what browsers will actually do.
- Treating a literacy or linguistics font as a general-purpose brand face; these designs carry a specific job in their letterforms.

## Tool notes

- Render test pages in a real browser with the exact production stack: declare the font-family list precisely and paste real content, including numerals and punctuation.
- For shaping checks, compare against the per-script repository's own test data where available; Noto's repos ship test suites that encode the tricky cases.
- unicode-range maps in your CSS should mirror the subsets you actually serve; generating them from the font files beats hand-maintaining ranges.
- When CJK payloads matter, measure: subset the family with pyftsubset or use region-specific builds, and record which variant you shipped, because SC and TC files are different products, not translations.

## Cross-references

- [Regional and script catalogs](regional-and-script-catalogs.md)
- [Google Fonts Catalog](google-fonts-catalog.md)
- [Open Font License in practice](../licensing/open-font-license.md)
- [The google/fonts repository](google-fonts-repository.md)

Compiled 2025 as part of the Fontlore project.
