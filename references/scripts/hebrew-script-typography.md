# Hebrew Script Typography

What this reference covers: Hebrew's structural facts that drive font decisions, niqqud and when vertical space must grow, and how to pair Latin and Hebrew faces so one page does not look like two projects. It stays practical: what to check, which open families to trust, and what goes wrong.

## Structural facts that matter

Hebrew differs from Arabic in ways that simplify some decisions and add others:

- No joining: letters do not connect, so shaping is far simpler than Arabic. Isolated-letter testing is actually meaningful here.
- No letter case: there are no capitals, so text-transform: uppercase is a no-op and "small caps hierarchy" tricks do not exist. Hierarchy must come from size, weight, and spacing.
- Right to left: same `dir="rtl"` handling as Arabic; numerals and Latin runs inside Hebrew remain left to right.
- 22 consonant letters plus 5 final forms (sofit letters: kaf, mem, nun, pe, tsadi in their word-final shapes). Check the five finals in any font; rare but real omissions exist.

## Niqqud and vertical space

Niqqud are the combining vowel and cantillation marks in the range U+0591-05C7, placed above and below consonants, with internal points (dagesh, shin and sin dots) inside the letter body.

- Modern secular Hebrew is written unpointed; body text in most products needs no niqqud and no extra leading.
- Pointed text (children's books, prayer books, learning tools, biblical text) needs generous line-height, commonly 1.7 or more, plus mark positioning quality: a font can contain niqqud codepoints yet place them off-center or colliding.
- Test with a fully pointed string such as Genesis 1:1 and check: sheva and hataf vowels under letters, dagesh centered inside letters, shin and sin dots placed on the correct side, and marks clearing the line above.
- Geresh and gershayim (U+05F3, U+05F4) mark abbreviations and acronyms; they are part of everyday text, so confirm coverage.

## Latin-Hebrew pairing

Most Hebrew-reading users see Latin brand names, numbers, and UI chrome mixed with Hebrew text, so the pairing decision is the central one.

Strategy A, one family for both: many open Hebrew families ship a matched Latin. Rubik, Heebo, Assistant, Alef, Secular One, Miriam Libre, Frank Ruhl Libre, David Libre, and the Noto Sans Hebrew and Noto Serif Hebrew releases all include Latin designed to work with their Hebrew. This is the lowest-risk route and usually the best default.

Strategy B, brand Latin plus Hebrew companion: when a Latin brand face has no Hebrew, pick a Hebrew face and match these properties, in order of visual importance:

1. x-height and overall vertical proportion; Hebrew letters occupy a narrow vertical band, so a tall-x Latin next to a small Hebrew reads as imbalance.
2. Weight range: ensure the Hebrew face has real bold at the same apparent weight, not a heavier-than-needed bold.
3. Aperture and stroke contrast: pair humanist Latin with open Hebrew designs rather than high-contrast Latin with monoline Hebrew.
4. Width: Hebrew is naturally wider per "letter" than Latin; do not force optical parity by scaling, align baselines and let widths differ.

Set the two faces at slightly different sizes if needed: Hebrew often benefits from a half-point to one-point bump at small UI sizes.

## Reliable open families

- Frank Ruhl Libre: a contemporary take on the classic Frank-Ruehl book style; the natural serif-leaning default.
- David Libre: derived from the David Hebrew style used in Israeli printing; bookish and familiar.
- Heebo, Rubik, Assistant, Secular One, Alef, Miriam Libre, Varela Round (Hebrew extended): sans voices ranging from neutral UI to rounded and geometric.
- Noto Sans Hebrew and Noto Serif Hebrew: neutral workhorses with wide weight ranges, useful as the connective tissue in multilingual stacks.

Heebo and Rubik are particularly common for UI work; Frank Ruhl Libre and David Libre for editorial; Noto Sans Hebrew when one system must serve many scripts.

## Metric compatibility and UI details

- Digits in Hebrew text are Western Arabic numerals running left to right; in tables, figures stay aligned regardless of direction, but column headers in Hebrew flip. Test a numeric table with `dir="rtl"`.
- Buttons and inputs containing Hebrew: the same elements often contain Latin placeholders too; check both directions of a form.
- Mixed-name lists (a Latin first name, Hebrew surname) are where bidi handling shows cracks; wrap user-generated segments in bdi.
- If the design uses letter-spacing for labels, Hebrew tolerates it better than Arabic (no joins), but keep it subtle; wide tracking on Hebrew reads as alien.

## Common mistakes

- Pairing a thin, high-contrast Latin display face with a sturdy Hebrew sans because "both are modern"; the mismatch reads strongest in mixed headlines.
- Declaring a font "supports Hebrew" from its subset label, then discovering niqqud collide at production line-height.
- Using uppercase Latin labels next to sentence-case Hebrew and expecting the same visual hierarchy; rework the hierarchy per language instead.
- Forgetting the five sofit forms in a display face check; their absence is a hard blocker for real text.
- Applying Arabic-style assumptions (joins, kashida, no tracking) to Hebrew or vice versa; the two scripts share direction, little else.

## Decision rules

- Product UI with Hebrew plus Latin: Rubik, Heebo, or Assistant as the single family; Noto Sans Hebrew when the stack must scale to more scripts.
- Editorial Hebrew: Frank Ruhl Libre for body, Secular One or a heavier Rubik for display.
- Pointed text for learning or liturgy: test niqqud placement explicitly; Noto Serif Hebrew and Frank Ruhl Libre are reasonable first checks.
- Brand Latin without Hebrew: choose Noto Sans Hebrew or Miriam Libre, match x-height and weight, and size Hebrew up slightly at small sizes.

## Comparison table

Open Hebrew families compared on voice, weights, and the checks that decide shortlists:

| Family | Voice | Latin included | Weights | Typical use |
| --- | --- | --- | --- | --- |
| Rubik | Contemporary sans, slightly rounded corners | Yes | 300-900 | Product UI, marketing |
| Heebo | Neutral UI sans, familiar Israeli web voice | Yes | 100-900 | Product UI |
| Assistant | Humanist UI sans, open apertures | Yes | 200-800 | Product UI, dashboards |
| Alef | Sturdy, simple | Yes | 400, 700 | Simple sites, documentation |
| Secular One | Display-leaning single weight | Yes | 400 | Headlines, accents |
| Miriam Libre | Clean text sans | Yes | 400, 700 | Text and labels |
| Frank Ruhl Libre | Serif-leaning book style | Yes | 300-900 | Editorial body, headlines |
| David Libre | Bookish, Israeli printing tradition | Yes | 400, 500, 700 | Editorial, formal text |
| Noto Sans Hebrew | Neutral workhorse | Yes | 100-900 | Multilingual stacks |
| Noto Serif Hebrew | Neutral serif | Yes | 100-900 | Books, pointed text checks |
| Varela Round | Rounded, single weight | Yes | 400 | Friendly accents, logos |

Reading the table:

- Single-weight families (Secular One, Varela Round) are accents, not systems; a product that needs a bold must not lean on them.
- Weight parity across the family is the check that matters most: Hebrew bolds that overshoot the Latin bold are the common failure in mixed headlines.
- Every family here ships a matched Latin, which is why the single-family strategy dominates Hebrew-Latin product work.

## Worked example

A Hebrew-English B2B SaaS with an existing Latin brand face that has no Hebrew:

1. Requirements: Hebrew UI and English marketing, numeric tables, mixed user names, and a glossary feature that includes pointed Hebrew terms.
2. Strategy decision: the brand Latin cannot carry Hebrew, so strategy B applies; the Hebrew companion must match x-height proportion first, weight second, contrast third.
3. Companion choice: Rubik for UI (weight range covers the brand's 400 and 600 slots) and Noto Sans Hebrew in the stack as the deliberate safety net.
4. Direction: dir="rtl" on the Hebrew locale; logical properties throughout; user names wrapped in bdi because Latin and Hebrew names interleave in lists.
5. Numeric tables: Western digits stay left-to-right inside RTL; column headers flip while figure columns hold alignment, verified with dir="rtl" on a real table.
6. Niqqud gate: the glossary's pointed terms are set at production line-height with the scoped 1.7 leading; sheva and hataf vowels, dagesh centering, and shin/sin dot sides are all checked.
7. Sizing: Hebrew runs a half-step larger than Latin at small UI sizes after side-by-side proofing showed it reading smaller.
8. Bidi stress: an English product name inside a Hebrew sentence, and a Hebrew file name inside an English path, both rendered as clean isolated runs.
9. Cross-browser pass: Chromium, Firefox, and WebKit, with the rendered-fonts inspector confirming no silent substitution.

Outcome: a coherent two-family system (brand Latin plus Rubik), RTL-safe components from one codebase, and pointed text that survives production line-height.

## Field notes

- Unpointed Hebrew is the norm for products; pointed text (children's books, prayer, learning tools) is a distinct project with its own leading and font requirements.
- The rendered-fonts inspector settles pairing doubts quickly: mixed Hebrew-Latin runs show exactly which face drew which segment.
- Geresh and gershayim (U+05F3, U+05F4) appear in ordinary text - abbreviations, acronyms, quotations - so their absence shows up fast in real content.
- Numeric expressions with separators (ranges, dates, decimal commas) can reorder visually in RTL layouts; wrapping computed numeric output in dir="ltr" is the standard fix.
- Desktop system stacks carry Hebrew in Arial and Segoe UI cuts, and Android falls back to Noto Sans Hebrew; audit the no-webfont path rather than assuming it is fine.
- Wide tracking reads as alien on Hebrew faster than on Latin; if a label system tracks uppercase Latin, define an untracked Hebrew variant.
- Frank Ruhl Libre and David Libre both descend from named Israeli printing traditions; choosing between them is a voice decision a Hebrew reader should make, not a metrics decision.
- Sofit forms are the display-face trap: poster and display fonts sometimes omit or deform the five final forms, and they occur in ordinary words.
- Hebrew quotation and punctuation conventions differ from English (gershayim inside acronyms, gershayim-based quotation marks); test real strings rather than transliterated samples.
- Weight-based hierarchy works well in Hebrew because there is no case; a design system that communicates hierarchy through weight and size ports over cleanly.
- Monospace and terminal fonts rarely cover Hebrew; Hebrew inside logs or code output falls back to the UI face, so width expectations in log views should assume the seam.
- Latin descenders (g, y, p) make mixed Hebrew-Latin lines look uneven even at matched x-heights; check a mixed-name list rather than single-script lines.
- Hebrew-calendar year abbreviations attach a geresh or gershayim to letters; if any date UI touches the Hebrew calendar, include one in the test strings.
- Email renders without webfonts in most clients, so the system Hebrew fallback is the actual email design; audit it rather than the webfont.
- Niqqud leading interacts with size: large display sizes need relatively less extra leading than 14 px body text, so scope pointed-text leading by size as well as language.
- Fixed row heights keep Latin-only and Hebrew-only rows visually identical in mixed lists; content-driven row heights let metric differences make lists visibly breathe.

## Quick reference

- Direction: dir="rtl" for Hebrew; dir="auto" plus bdi for unpredictable mixed content; logical properties everywhere.
- Hierarchy: weight and size only; no uppercase transforms exist.
- Niqqud: unpointed needs no extra leading; pointed text wants 1.7 or more scoped by :lang(he), plus mark-placement checks.
- Hard gates: the five sofit forms, U+05F3 and U+05F4, dagesh centering, shin/sin dot sides.
- Digits: Western digits left-to-right inside Hebrew; wrap numeric output in dir="ltr" when separators scramble.
- Defaults: Rubik, Heebo, or Assistant for UI; Frank Ruhl Libre and David Libre for editorial; Noto Sans Hebrew for multilingual stacks.
- Sizing: Hebrew often benefits from a half-step bump at small sizes; verify with side-by-side mixed lines.
- Pairing order: x-height proportion, then weight range, then aperture and contrast, then width; align baselines and let widths differ.
- Tracking: keep any letter-spacing subtle and define an untracked Hebrew variant for tracked Latin labels.
- Verification: real pointed strings, numeric tables under dir="rtl", and mixed-name lists in three browser engines.
- Mixed-run tests: a Hebrew file name inside an English path, and an English product name inside a Hebrew sentence, both as standing cases.
- Email: assume no webfonts render; the platform Hebrew fallback is the design that most subscribers see.
- Row heights: fixed heights for mixed lists so Hebrew-only and Latin-only rows align identically.

## Cross-references

- [Arabic script typography](arabic-script-typography.md)
- [Mixed script fallbacks](mixed-script-fallbacks.md)
- [Localization and RTL accessibility](../accessibility/localization-and-rtl-accessibility.md)
- [Web and SaaS interfaces](../applications/web-and-saas-interfaces.md)

Compiled 2025 as part of the Fontlore project.
