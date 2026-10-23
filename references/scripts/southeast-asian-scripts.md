# Southeast Asian Scripts

What this reference covers: Thai, Lao, Khmer, and Myanmar typography for web and product work: overlapping marks, the line-height these scripts actually demand, and the Cadson Demak and Noto families that solve them. Vietnamese is Latin script with complex-script problems and is covered by the Latin reference; this file handles the true Southeast Asian scripts.

## Shared structural facts

These Brahmic-derived scripts share three traits that wreck Latin-tuned layouts:

- Stacked diacritics: vowels and tone marks can occupy two levels above the base letter and one or two below. Two-level stacks are normal text, not edge cases.
- No letter case: hierarchy cannot use caps; weight, size, and spacing carry it.
- Tall vertical demands: line-height below roughly 1.5 starts clipping; Khmer and Myanmar routinely need 1.7 or more. Set generous leading for these languages via `:lang()` scoped rules rather than inflating the whole page.

Letter-spacing must not be applied to any of these scripts; it pulls apart letters that may carry shared marks and reads as broken text.

## Thai

Thai chains consonants, stacked vowels, and tone marks; tone marks (U+0E48-0E4B) must clear characters with tall upper parts such as U+0E1B and U+0E2D, and stack above the nikhahit vowel (U+0E4D) when both occur.

- Two style worlds: looped (traditional, with small loops on letter heads) and loopless (modern geometric, common in signage and tech brands). Mixing them at random across an interface reads as inconsistent.
- Cadson Demak, the Bangkok foundry, dominates open Thai typography. On Google Fonts: Prompt and Kanit (loopless, geometric), Sarabun (looped, the basis of the Thai government standard style), Mitr, Bai Jamjuree, Chakra Petch, Trirong (looped serif-flavored), KoHo, and K2D.
- IBM Plex Sans Thai and IBM Plex Sans Thai Looped provide matched IBM Plex Latin; Noto Sans Thai and Noto Serif Thai are neutral defaults.
- Thai digits U+0E50-0E59 exist, but Western digits dominate modern usage; both usually appear in one font.
- Test tone marks over tall consonants and over stacked vowels at your production sizes; this is the single most common Thai rendering failure.

## Lao

Lao shares Thai's structure with different letterforms and fewer complications in practice.

- Line-height demands match Thai; stacked vowels and marks need room.
- Reliable open fonts: Noto Sans Lao and Noto Serif Lao; Phetsarath, the government standard, is widely available for documents.
- Verify tone marks and the vowel stacking pairs before committing a display face; coverage beyond a core set is thinner than for Thai.

## Khmer

Khmer is the heaviest of the four: two series of consonants, vowel signs that wrap around bases, and subscript consonants.

- Subscripts are produced with the coeng sign U+17D2 preceding a consonant; the shaper converts the pair into a subscript form. A font with weak coeng handling produces visibly wrong clusters.
- Stacks of three levels occur in ordinary words; line-height of 1.7 to 1.9 is a realistic body range.
- Reliable open fonts: Noto Sans Khmer and Noto Serif Khmer (modern shaping), Kantumruy Pro (a contemporary UI face), Battambang (text), Moul (display, used for headings and formal contexts).
- Test: subscript chains, two-vowel stacks, and punctuation like the Khmer sign sets in U+17D4-17DD; older fonts often miss the newer codepoints.

## Myanmar

Myanmar adds its own risks because the script went through a long non-Unicode era.

- Use Unicode text only. Legacy "Zawgyi" encodings still circulate in old content and produce mojibake in any modern font; detect and convert rather than trying to support both.
- Stacked consonants, kinzi (a historical mark rendered above via a virama sequence), and medials make shaping intensive; Padauk (SIL) and Noto Sans Myanmar are the reference implementations, with Tharlon a common text alternative.
- Line-height 1.7 or more; Myanmar is also one of the scripts where font size needs a bump relative to Latin to match perceived size.
- Test digits (Myanmar has its own, U+1040-1049) and mixed Myanmar-Latin runs in the same paragraph.

## Choosing a family system

- Thai-first products: Prompt or Sarabun with their built-in Latin; add IBM Plex Sans Thai if the brand already uses IBM Plex.
- Neutral multilingual stacks: Noto per-script fonts (Noto Sans Thai, Noto Sans Lao, Noto Sans Khmer, Noto Sans Myanmar) plus one Latin face. This is the only approach that scales to ten languages without redesign.
- Display moments: Moul for Khmer formality, Trirong for Thai editorial flavor; test display faces at large sizes for mark collisions.
- Budget line-height per language: define `:lang(th)`, `:lang(lo)`, `:lang(km)`, `:lang(my)` rules with 1.5 to 1.8 leading rather than one global compromise.

## Common mistakes

- Shipping a Thai font chosen for its loopless brand look, then discovering tone marks collide with tall consonants in body text.
- Applying a global line-height of 1.3 tuned on Latin and clipping Khmer stacks; or a global 1.8 that makes the English interface airy to the point of feeling broken.
- Accepting Zawgyi-encoded Myanmar content into a Unicode pipeline; the failure appears later as unfixable mojibake.
- Using letter-spacing on Thai or Khmer labels.
- Assuming the Cadson Demak families are interchangeable; each has a distinct voice and weight range, and some are loopless while others are looped.
- Testing only headlines; mark collisions appear most in dense body text and small UI labels.

## Decision rules

- One Southeast Asian language only: use its strongest single family (Thai: Prompt/Sarabun; Khmer: Kantumruy Pro or Noto Sans Khmer).
- Several languages: Noto per-script fonts for everything except brand moments.
- Government or formal contexts: prefer the standards-adjacent choices (Sarabun in Thai practice, Phetsarath for Lao).
- Display headlines in any of these scripts: verify at final size with real words, including a tall-consonant plus tone-mark sequence, before approving.

## Comparison table

The four scripts compared on the layout demands that decide design systems:

| Script | Stacking reality | Body leading | Open exemplars | Watch-outs |
| --- | --- | --- | --- | --- |
| Thai | Two-level stacks are ordinary text | 1.5-1.7 | Prompt, Sarabun, Kanit, Noto Sans Thai, IBM Plex Sans Thai | Tone marks over tall consonants; looped versus loopless voice |
| Lao | Similar to Thai, slightly simpler in practice | 1.5-1.7 | Noto Sans Lao, Noto Serif Lao, Phetsarath | Thinner display selection; verify tone mark pairs |
| Khmer | Three-level stacks occur in ordinary words | 1.7-1.9 | Noto Sans Khmer, Noto Serif Khmer, Kantumruy Pro, Battambang, Moul | Coeng subscripts; newer punctuation codepoints missing in older fonts |
| Myanmar | Stacked consonants plus kinzi plus medials | 1.7+ | Padauk (SIL), Noto Sans Myanmar, Tharlon | Legacy Zawgyi content; size bump versus Latin |

Weight facts for the Cadson Demak era of open Thai: Prompt spans 100-900, Kanit spans 100-900 with italics, Sarabun spans 100-800, Mitr 200-700, Bai Jamjuree 200-700, Chakra Petch 300-700, and Trirong 100-900 for a looped serif-flavored voice. IBM Plex Sans Thai runs 100-700 in both looped and loopless editions, and Noto Sans Thai runs 100-900. Thai digits U+0E50-0E59 exist in all of them, but Western digits dominate modern Thai usage.

## Worked example

A Thai-first e-commerce storefront with English secondary:

1. Requirements: Thai body text and marketing headlines, English account and checkout chrome, product data from a feed, mobile-heavy audience.
2. Font plan: Sarabun for body (looped, familiar from the Thai government standard style) and Prompt for headings (loopless, geometric); the looped-body-plus-loopless-heading combination is a deliberate decision, signed off by a Thai-reading reviewer rather than an accident of font shopping.
3. Language scoping: lang="th" on Thai trees; :lang(th) sets line-height 1.7 and keeps Latin tokens untouched.
4. Controls: buttons, inputs, and price rows get fixed heights; the Thai line box was inflating list rows before explicit control heights landed.
5. Tone-mark gate: tone marks U+0E48-0E4B are rendered over tall consonants (U+0E1B, U+0E2D) and over stacked vowels at 12, 16, and 32 px equivalents; the 13 px price labels caught a collision the desktop proof missed.
6. Digits: prices use Western digits per market convention; Thai digits U+0E50-0E59 are confirmed present for legal copy, and the decision is recorded.
7. Feed audit: product titles are sampled for tone-mark density, because catalog names exercise the stacks harder than marketing copy.
8. Cross-browser pass: Chromium, Firefox, and WebKit, plus a low-end Android device, since Thai shaping quality differences show up where fonts fall back.
9. Input test: Thai is typed, not pasted, into search and address fields on mobile, because keyboard composition exercises mark placement differently than paste.

Outcome: a coherent looped-plus-loopless system with per-language leading, no clipped marks at any production size, and a documented digit convention.

## Field notes

- The single most common Thai failure is a loopless brand font chosen for its look, discovered later to collide tone marks with tall consonants in dense body text; the gate is the test string, not the specimen.
- Sarabun's familiarity comes from its basis in the Thai government standard style; formal and civic contexts should default to it, not to a tech-brand geometric.
- IBM Plex Sans Thai and IBM Plex Sans Thai Looped pair with the wider IBM Plex system; they are the natural choice when the brand already runs Plex Latin.
- Lao's open selection is thinner than Thai's: Noto Sans Lao and Phetsarath are the dependable names, and a display-face ambition in Lao needs a coverage proof before commitment.
- Khmer subscripts come from the coeng sign U+17D2 preceding a consonant; weak coeng handling produces visibly wrong clusters, so the subscript chain belongs in every Khmer test file.
- Khmer serial punctuation and sign sets in U+17D4-17DD are newer codepoints; older fonts miss them and paragraphs fall back mid-sentence.
- Myanmar content must be Unicode; Zawgyi-encoded text produces unfixable mojibake in modern stacks, so detect and convert at ingest rather than trying to render both.
- Padauk (SIL) and Noto Sans Myanmar are the reference implementations for Myanmar shaping; Tharlon is a common text alternative, and size usually needs a bump versus Latin.
- Legacy TIS-620-encoded Thai still surfaces in old databases; it is a smaller-scale version of the Zawgyi problem and should be converted at ingest, not rendered through hacks.
- Letter-spacing must never be applied to Thai, Lao, Khmer, or Myanmar; shared marks and stacked levels make tracking read as broken text.
- Vietnamese is Latin script with complex-script problems (stacked tone marks); it belongs to the Latin coverage reference, not this one.
- Prompt and Kanit are both loopless and geometric, but Kanit ships italics and Prompt does not; slanted Thai needs that check before a design promises it, because faux italic is worse than none.
- Noto Sans Lao Looped exists alongside Noto Sans Lao; the looped versus loopless split applies to Lao too, not just Thai, and mixing the two without intent reads the same way it does in Thai.
- Padauk's coverage extends across Myanmar-script languages beyond Burmese, which makes it the deep-coverage reference when minority-language content is in scope.
- Thai line breaking is dictionary-based because words run together without spaces; browsers break with ICU dictionaries, so prices, codes, and identifiers need nowrap or non-breaking characters to control where lines split.
- Khmer breaks the same way (no inter-word spaces, dictionary-based); the same nowrap discipline applies to Khmer prices and reference numbers.
- The uppermost mark in a Thai stack needs the most leading: a tone mark above a vowel above a consonant is the tallest ordinary text in the script, and it is why the display-size proof and the 13 px label proof must both run.
- Sarabun and Prompt both include Latin, and their Latins differ in personality; make the pairing decision with real Thai-Latin mixed lines rather than solo specimens.
- Thai keyboards emit combining marks as separate keystrokes mid-composition; type into real search and checkout fields on mobile rather than only pasting.
- Noto Serif Khmer is a modern-shaping design; older Khmer fonts predate current shaping expectations and should not enter new stacks regardless of familiarity.
- Mitr and Bai Jamjuree share Prompt's loopless modern voice with narrower weight ranges; choosing among them is a width and weight decision rather than a voice one.

## Quick reference

- Leading tokens per language via :lang(): Thai and Lao 1.5-1.7, Khmer 1.7-1.9, Myanmar 1.7 or more; never one global value.
- Hard gates: Thai tone marks over tall consonants and stacked vowels; Khmer coeng chains and multi-level stacks; Myanmar stacked consonants, kinzi, and digits U+1040-1049.
- Never: letter-spacing on any of these scripts; uppercase-transform-based hierarchy (there is no case); global Latin-tuned leading.
- Defaults: Thai Prompt or Sarabun; Lao Noto Sans Lao; Khmer Kantumruy Pro or Noto Sans Khmer; Myanmar Padauk or Noto Sans Myanmar; Noto per-script faces for multilingual stacks.
- Display: Trirong for Thai editorial flavor, Moul for Khmer formality; verify at final size with real words including mark-heavy sequences.
- Myanmar policy: Unicode text only; detect and convert Zawgyi at ingest.
- Digits: Thai U+0E50-0E59 and Myanmar U+1040-1049 exist; the Western-versus-local digit decision is per locale in the i18n layer.
- Verification: real body paragraphs plus price labels at small sizes, three browser engines, one low-end Android device.
- Line-break control: Thai and Khmer words carry no spaces, so dictionary-based breaking decides; wrap prices, codes, and IDs in nowrap or non-breaking characters.
- Italic check: Kanit ships italics, Prompt does not; verify the family before promising slanted Thai, and reject faux italic.
- Looped policy: decide looped versus loopless per role (body, headings, brand) and keep the choice coherent across surfaces.
- Type-test gate: Thai and Khmer typed into real search and checkout inputs, not just pasted.
- Mixed-line proof: Thai plus Latin in one line for every face whose built-in Latin is being relied on.
- Weight planning: Prompt and Kanit reach 900, Sarabun stops at 800; match the design's heaviest weight token to the family before committing.

## Cross-references

- [Devanagari script typography](devanagari-script-typography.md)
- [Latin and extended coverage](latin-and-extended.md)
- [Mixed script fallbacks](mixed-script-fallbacks.md)
- [Subsetting and performance](../technical/subsetting-and-performance.md)

Compiled 2025 as part of the Fontlore project.
