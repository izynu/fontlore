# Latin and Extended Coverage

What this reference covers: How Latin coverage is tiered in practice, what subset labels like "latin-ext" actually promise, and how to verify diacritics render well rather than just exist. It concentrates on European Latin plus the Vietnamese edge cases that subset labels routinely hide.

## The practical coverage tiers

Treat Latin coverage as five tiers and require each tier explicitly. A font that "has Latin" usually means tier 2, and the gap shows up the moment a Polish or Vietnamese name enters the database.

- Tier 1, basic Latin: A-Z, a-z, digits, and core punctuation. Every font has this.
- Tier 2, Latin-1 Supplement: Western European accents, German umlauts and sharp s, French guillemets, Spanish inverted marks, Icelandic thorn and eth.
- Tier 3, Latin Extended-A: Polish, Czech, Slovak, Hungarian, Baltic, Turkish, Welsh, Maltese letters.
- Tier 4, Latin Extended-B and Latin Extended Additional: Romanian comma-below letters, Vietnamese precomposed characters, many rare forms.
- Tier 5, combining diacritical marks: needed when text arrives decomposed rather than precomposed.

Tier 4 is where most failures live. Vietnamese stacks two or even three marks over one letter, and a font can contain every codepoint yet place the stacked marks clumsily.

## What subset labels promise

Google Fonts splits many families into unicode-range files: latin, latin-ext, cyrillic, greek, vietnamese, and script-specific subsets. The label tells you which codepoints are included, not whether they are well drawn.

- latin covers tiers 1-2. latin-ext covers roughly tier 3 plus parts of tier 4.
- The vietnamese subset flag is the reliable signal for Vietnamese support, not latin-ext.
- When self-hosting a variable font file directly, subset labels do not exist; you inherit everything in the file, and you must check coverage yourself.

Decision rule: if any user-facing string can contain a Polish, Czech, Turkish, Romanian, or Vietnamese character, test tier 3 and tier 4 before shortlisting, not after.

## Codepoint checklist for high-risk languages

Because layout QA needs something scriptable, verify these codepoints render with correct positioning, not tofu:

- Polish: U+0105 and U+0104 (a with ogonek), U+0142 (l with stroke), U+0119 (e with ogonek), U+00F3, U+015B, U+017A, U+0107, U+0144.
- Czech and Slovak: U+0159 (r with caron), U+011B (e with caron), U+0165, U+017E, U+016F, U+00FD, U+013E (l with caron).
- Turkish: U+011F (g with breve), U+0131 (dotless i), U+0130 (I with dot above), U+015F (s with cedilla). The dotless i breaks naive `text-transform: uppercase`; use `:lang(tr)` so case mapping is locale-aware.
- Romanian: U+0218 through U+021B (comma-below s and t). Older fonts ship only the cedilla forms U+015F and U+0163, which Romanian readers consider wrong.
- Icelandic and Faroese: U+00DE (thorn), U+00F0 (eth), U+00E6, U+00F6.
- German: U+00DF (sharp s) and the capital form U+1E9E, which many fonts still miss.
- Vietnamese: the whole U+1EA0-1EFF range, plus U+01A0 and U+01AF (horn o and horn u). Spot check the worst stackers: e with circumflex and dot below, a with breve and hook above, u with horn and tilde.

For full sentences, pull real text from the Unicode consortium's Universal Declaration of Human Rights translations at https://www.unicode.org/udhr/index.html or the language edition of Wikipedia, rather than inventing strings from memory.

## Diacritics testing, step by step

1. Paste a mixed-language sample into a specimen page at body size and at 12 px UI size.
2. Check horizontal balance first: do ogoneks and carons collide with descenders of the line above at your production line-height?
3. Check the uppercase forms: many fonts have weaker, auto-generated caps for extended letters.
4. Set line-height tight, around 1.15, and check for clipping; extended Vietnamese stacks are the tallest Latin forms in common use.
5. Test bold and italic too. Extended coverage in regular weight does not imply it in italic, and faux italic of accented caps usually looks broken.
6. Normalize input text to NFC in your pipeline so precomposed characters are used where the font has them.

## Vietnamese pitfalls in detail

Vietnamese is Latin script, but it behaves like a complex script typographically.

- Marks stack vertically: a vowel can carry a tone mark plus a vowel-quality mark plus a dot below, so the vertical metrics demand exceeds German or French text by a wide margin.
- Horn letters (o with horn, u with horn) need extra width; fonts drawn only for Western Europe squeeze them.
- Some pipelines send decomposed text; if the font lacks combining-mark anchors, marks land side by side instead of stacked.
- Web: the Google Fonts "vietnamese" subset is separate from latin-ext, so a site that loads only latin and latin-ext will fall back mid-word for Vietnamese.

Good open families with known Vietnamese strength include Be Vietnam Pro, Archivo, Barlow, Mulish, Source Sans 3, Roboto, Inter, and Noto Sans. Literata and Newsreader are strong text serifs with vietnamese coverage.

## Common mistakes

- Declaring success after checking French and German, then shipping without Polish or Vietnamese testing.
- Using `text-transform: uppercase` for Turkish content without a `lang` attribute, producing wrong dotted and dotless i forms.
- Trusting the latin-ext label while never looking at how stacked Vietnamese marks are anchored.
- Setting a tight display line-height tuned on plain English headlines, then clipping Vietnamese and Czech headlines in production.
- Importing latin and latin-ext subsets but letting third-party embeds (forms, widgets) render Vietnamese with system fallback fonts, creating a visible mismatch.

## Decision rules

- Need Western Europe only: almost any reputable family works; check sharp s and guillemets.
- Need Central Europe or Turkey: require latin-ext and run the codepoint checklist above.
- Need Vietnamese: require the vietnamese subset or verified U+1EA0-1EFF coverage, and eyeball the stacked marks at two sizes.
- Mixed audience with unknown languages: pick a family from the Noto or Source lineages, which are designed for wide coverage from the start.

## Comparison table

Subset reality for widely used open families. The middle columns report what the Google Fonts subset list covers; they say nothing about how well the stacked marks are drawn, which is what the eyeball pass is for:

| Family | Subsets on Google Fonts | Vietnamese | Notable for |
| --- | --- | --- | --- |
| Inter | latin, latin-ext, cyrillic, cyrillic-ext, greek, greek-ext, vietnamese | yes | UI default with wide reach |
| Roboto | latin, latin-ext, cyrillic, cyrillic-ext, greek, greek-ext, vietnamese | yes | The everywhere font |
| Open Sans | latin, latin-ext, cyrillic, cyrillic-ext, greek, greek-ext, hebrew, vietnamese | yes | Adds Hebrew to the wide set |
| Source Sans 3 | latin, latin-ext, cyrillic, cyrillic-ext, greek, vietnamese | yes | Humanist workhorse |
| Noto Sans | Per-script system plus Latin | yes | The connective tissue |
| Literata | latin, latin-ext, cyrillic, cyrillic-ext, greek, greek-ext, vietnamese | yes | Book serif for reading |
| Montserrat | latin, latin-ext, cyrillic, cyrillic-ext, vietnamese | yes | Display sans |
| Barlow | latin, latin-ext, vietnamese | yes | Grotesque with Vietnamese strength |
| Be Vietnam Pro | latin, latin-ext, vietnamese | yes | Drawn for Vietnamese first |
| Lato | latin, latin-ext | no | Popular, but a Central European and Vietnamese gap |

Reading the table:

- The vietnamese column is the one most teams get wrong: latin-ext alone does not cover Vietnamese, and the failures are mid-word fallbacks that only a real Vietnamese string reveals.
- Subset lists expand between releases; re-check at decision time instead of relying on an old screenshot of the catalog.
- Self-hosting a raw font file bypasses subset labels entirely: you inherit every codepoint in the file, and the coverage check becomes yours.
- Open Sans is the rare mainstream family whose subset list includes Hebrew alongside the wide Latin set; a reminder that subset lists reward a fresh look whenever the locale list grows.

## Worked example

A B2B SaaS adding Polish, Czech, Turkish, and Vietnamese to an English-only product:

1. Requirements matrix: four new locales, UI labels plus user-generated names, an existing brand sans under review.
2. First filter: any candidate without the vietnamese subset or verified U+1EA0-1EFF coverage is out; this eliminates more candidates than any other gate.
3. Checklist render: the codepoint checklist for all four languages is pasted into a specimen page using only the candidate font, at 12 px and 16 px.
4. Clip test: line-height is forced to 1.15 and the Vietnamese stacked forms are inspected; ogonek and dot-below collisions with the line above are noted.
5. Turkish gate: uppercase transform is run with lang="tr" set; dotless i behavior is verified against the expected dotted and undotted forms.
6. Bold and italic: the checklist is re-rendered in bold and italic, because extended coverage in regular does not imply it in the other styles.
7. Pipeline: input text is normalized to NFC so precomposed characters are used where the font has them; the normalization point is documented in the i18n layer.
8. Third-party audit: embedded forms and widgets are found to declare their own font stacks, so a Vietnamese fallback font is defined for each embed or the embed inherits the page stack.
9. Decision: the candidate with correct comma-below Romanian forms and clean Vietnamese stacks wins; the runner-up's cedilla-form fallback is recorded as the reason.
10. Regression: the checklist page is added to the repo and re-run on every font version bump.

Outcome: a locale expansion with no mid-word fallbacks, no clipped stacks, and a repeatable gate for the next language.

## Field notes

- Romanian comma-below versus cedilla is a dating service: fonts drawn before the U+0218-021B codepoints existed often map the Romanian letters to cedilla forms or miss them; Romanian readers consider the cedilla forms wrong.
- The German capital sharp s U+1E9E is still missing in otherwise complete fonts; German uppercase text traditionally doubles the s instead, but decide the policy explicitly rather than discovering tofu.
- Turkish dotless i is the classic case-mapping bug: without lang="tr", uppercase and lowercase transforms produce wrong dotted and undotted forms; the lang attribute is the entire fix.
- The Catalan geminated l (l-l with middle dot U+00B7) is covered by Latin-1, so coverage is never the issue; line-breaking is, because the middle dot is not a word boundary to every engine.
- Vietnamese keyboards and pipelines mostly emit precomposed NFC text, but copy-paste from some sources arrives decomposed; a font without combining-mark anchors stacks those marks side by side or misplaces them.
- Tone marks survive uppercase in Vietnamese; the check is whether the diacritic anchors hold on capital letters, which is a different drawing problem than lowercase stacking.
- Third-party embeds (forms, chat widgets, maps) declare their own font stacks; audit them per locale or the page's Vietnamese coverage stops at the embed boundary.
- Horn letters (o and u with horn) need width that Western-Europe-only designs never budgeted; squeeze shows up in headlines first.
- Uppercase display settings tuned on English headlines are the most common clipping report: Czech and Vietnamese headlines need the tight-leading clip test at display sizes too.
- Welsh is the frequent hole in otherwise-good latin-ext fonts: w and y with circumflex (U+0174-0177) are Latin Extended-A, and their absence shows as tofu in a language teams forget to list.
- Maltese needs the dotted forms c with dot above, g with dot above, and z with cedilla-style z (U+010B, U+0121, U+017C) plus capitals; the g-h digraph uses plain letters, so only the dotted trio is a coverage risk.
- The Nordic languages are the safe end of the scale: a, o with diaeresis and ring, slashed o, and ae are all Latin-1, so Scandinavian failures point at a genuinely broken font, not a coverage tier.

## Quick reference

- Tier gates: Latin-1 for Western Europe; latin-ext for Central Europe and Turkey; the vietnamese subset flag for Vietnamese; Latin Extended Additional (U+1E00-1EFF) coverage for the worst stackers.
- Codepoint gates: Polish U+0105/U+0104 and U+0142; Czech U+0159/U+011B; Turkish U+011F/U+0131/U+0130; Romanian U+0218-021B; German U+00DF plus U+1E9E; Vietnamese U+1EA0-1EFF plus U+01A0 and U+01AF.
- Language tags: lang="tr" for case mapping; lang="ro", lang="vi", lang="pl", lang="cs" for scoping and proofing.
- CSS habits: :lang(tr) before any uppercase transform on mixed content; NFC normalization in the pipeline; clip test at line-height 1.15 for display sizes.
- Subset loading: load latin, latin-ext, and vietnamese explicitly when the Google Fonts CSS is self-configured; a missing subset file is a mid-word fallback.
- Test material: real sentences from the UDHR translations or the language's Wikipedia, plus your own product strings with real names.
- Edge gates worth adding when the locale list grows: Welsh U+0174-0177 and Maltese U+010B, U+0121, U+017C; Nordic needs only Latin-1 and is rarely the failure.
- Verification: bold and italic included, three sizes, and the rendered-fonts inspector to catch silent substitution.
- Re-audit on locale growth: subset lists change between releases, and a family that lacked Vietnamese a release ago may carry it now.

## Cross-references

- [Testing multilingual coverage](testing-multilingual-coverage.md)
- [Subsetting and performance](../technical/subsetting-and-performance.md)
- [Font-face and CSS](../technical/font-face-and-css.md)
- [Testing and comparing shortlists](../workflow/testing-and-comparing-shortlists.md)

Compiled 2025 as part of the Fontlore project.
