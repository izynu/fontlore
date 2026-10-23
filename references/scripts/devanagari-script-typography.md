# Devanagari Script Typography

What this reference covers: How Devanagari builds words from consonants, matras, and conjuncts; why shaping quality matters more than glyph count; and how to pair Latin with Devanagari families such as Mukta, Hind, Halant, and Eczar. Aimed at web and product teams shipping Hindi, Marathi, Sanskrit, or Nepali text.

## How the script assembles

Devanagari is an abugida: each consonant letter carries an inherent vowel that vowel signs (matras) then modify. Four mechanisms drive typography:

- Matras: vowel signs attached above, below, before, or after the consonant. The short-i matra (U+093F) is stored after its consonant in Unicode but renders before it; reordering is done by the shaper, and a font that fails this test fails everywhere.
- Halant (virama, U+094D): placed between consonants to suppress the inherent vowel, which usually forms a conjunct. Half forms and stacked forms both arise from it.
- Conjuncts: combinations like k + virama + s (ksha), t + virama + r (tra), j + virama + n (jna), d + virama + v. Quality fonts contain hundreds of GSUB substitutions (feature tags like akhn, half, cjct, rphf) that replace letter sequences with single designed ligatures.
- Nukta (U+093C): a below-base dot modifying some consonants into additional sounds; optional in most modern Hindi but needed for Marathi conventions in some words.

Everything is handled by the shaping engine (HarfBuzz or CoreText) reading the font's tables. The browser needs no plugin; the font needs real OpenType shaping tables. This is why "Devanagari support" varies so much between fonts that superficially contain the same codepoints.

## The shirorekha and vertical rhythm

The shirorekha is the horizontal headline connecting letters along the top of each word. It creates a strong continuous band that dominates the texture of a page, and it drives several decisions:

- Adjacent fonts with shirorekha of different thickness or height look obviously mismatched; keep Latin and Devanagari within one system or carefully matched pairs.
- Matras stack above the shirorekha and hang below the baseline, so Devanagari needs more vertical room than Latin. Body text reads well around 1.5 to 1.7 line-height; tightly leaded Latin paragraphs clip Devanagari matras.
- In headlines, the shirorekha is where display personality lives; check that thick or thin shirorekha choices survive bolding.

## Pairing Latin with Devanagari families

The safest pattern is a single family that ships both scripts, because the Latin was drawn to match:

- Mukta, Hind, Halant: Indian Type Foundry families released through Google Fonts, each with a full weight range and a coherent Latin. Mukta is the general-purpose workhorse; Hind is slightly narrower and UI-friendly; Halant is a serif-leaning text face.
- Eczar: a Rosetta release (Vaibhav Singh) with distinctive, slightly angled display energy; its Latin matches its Devanagari.
- Noto Sans Devanagari and Noto Serif Devanagari: neutral defaults with wide weight ranges, and the natural connective tissue when other scripts are in play.
- Poppins, Teko, Rajdhani, Khand, Baloo 2: Devanagari-supporting display and rounded voices from ITF and others; useful for brand moments.
- Martel: a text serif option with modest, bookish proportions.

When the Latin brand face has no Devanagari, pick a Devanagari family and match in this order: apparent weight, x-height/proportion of the Latin half, stroke contrast, then width. Expect to tune sizes separately; Devanagari often needs to run one or two points larger than Latin to match perceived size, because Latin capitals inflate its apparent scale.

## Testing checklist

1. Shaping smoke test: paste words containing ksha, tra, jna, and dva conjuncts, plus a reph word (r + virama before a consonant) and a short-i word. Reordering and stacking must be correct.
2. Matra clearance: set body text at your production line-height; check upper matras do not collide with the line above and lower matras clear descenders.
3. Bold parity: many Devanagari families have strong regular weights but coarse bolds; compare at 16 px and at 40 px.
4. Latin half quality: run your actual Latin UI copy through the family; some paired Latins are serviceable but bland, and some are excellent.
5. Digits: Devanagari digits are U+0966-096F; decide whether content uses them or Western digits, per locale, and format with your i18n library.
6. Marathi and Nepali extras: check nukta forms and the Sanskrit-specific vowel-vowel combinations if those languages are in scope.

## Common mistakes

- Pairing a Latin-only brand face with "any Devanagari font" chosen for its headline style; the mixed lines read as two unrelated products.
- Applying Latin-tuned line-height (1.3) globally and clipping matras; or fixing it with a global 1.7 that balloons Latin pages. Use `:lang(hi)` scoped rules instead.
- Letter-spacing on Devanagari: positive tracking splits the shirorekha into floating dashes and destroys word integrity. Never track Devanagari body or labels.
- Assuming codepoint coverage means quality: a font can map all of U+0900-097F and still substitute almost no conjuncts, producing awkward half-form chains.
- Uppercase styling for labels; Devanagari has no case, so hierarchy must come from weight and size.
- Testing Hindi only, then discovering Marathi or Sanskrit content uses combinations the font renders poorly.

## Decision rules

- General product UI: Mukta or Noto Sans Devanagari, sized up slightly relative to Latin.
- Editorial reading: Halant or Martel for text, Eczar for headlines.
- Brand display: Eczar, Teko, or Baloo 2, tested at real sizes for conjunct quality before falling in love.
- Multilingual stack (Hindi plus Tamil plus Arabic, say): build on Noto per-script fonts plus one Latin face, and accept that you are maintaining a system, not choosing one font.
- If legal or scholarly text needs maximum conjunct fidelity: Noto Sans Devanagari and Noto Serif Devanagari are the benchmark.

## Comparison table

Devanagari families compared on the dimensions that actually decide shortlists. Weight ranges are the Google Fonts lists:

| Family | Character | Latin included | Weights | Best for |
| --- | --- | --- | --- | --- |
| Mukta | General-purpose workhorse sans | Yes | 200-800 (seven cuts) | Product UI, general reading |
| Hind | Slightly narrower, UI-friendly | Yes | 300-700 | Interface text, dense layouts |
| Halant | Serif-leaning text face | Yes | 300-700 | Editorial body text |
| Eczar | Distinct display energy, slightly angled | Yes | 400-800 variable | Headlines, brand moments |
| Noto Sans Devanagari | Neutral, benchmark shaping | Yes | 100-900 | Multilingual stacks, legal text |
| Noto Serif Devanagari | Neutral serif | Yes | 100-900 | Books, scholarly text |
| IBM Plex Sans Devanagari | Enterprise UI sans | Matched Plex Latin | 100-700 | Corporate products with Plex Latin |
| Teko | Condensed display | Yes | 300-700 variable | Sports, headlines, tight spaces |
| Rajdhani | Squared, technical | Yes | 300-700 | Tech branding, labels |
| Baloo 2 | Rounded, friendly | Yes | 400-800 variable | Playful brands, children's products |
| Martel | Modest bookish serif | Yes | 300-800 in five cuts | Long-form reading |
| Poppins | Geometric sans with Devanagari | Yes | 100-900 | Marketing surfaces |

Reading the table:

- Weight range matters more than usual: many Devanagari designs are strongest at regular and weaken at the extremes, so a design requiring a hairline or black cut needs that cut verified in real Hindi strings.
- The Latin half is drawn to match in every family above; when the brand Latin is fixed and absent from this list, match in the order the pairing section describes and expect to size the Devanagari up slightly.
- Conjunct fidelity differs even within the same nominal style; two sans faces can both "support Devanagari" while one substitutes almost no designed conjuncts.

## Worked example

A Hindi-English government service portal, open licenses only, low-end devices in the audience:

1. Requirements: Hindi and English with equal fidelity, legal-grade long text, form-heavy UI, OFL-only fonts, and performance on low-end Android.
2. Fonts: IBM Plex Sans Devanagari as primary because its Latin matches the existing IBM Plex Sans brand; Noto Sans Devanagari closes the stack as the shaping benchmark and safety net.
3. Language tags: lang="hi" on Hindi trees so :lang(hi) scoping works; the English side keeps its own tokens.
4. Leading: line-height 1.6 scoped to :lang(hi), with the Latin side untouched at 1.4; the compromise value of 1.5 was tested and clipped stacked matras at 13 px form labels.
5. Sizing: side-by-side proofing showed the Devanagari reading a step smaller than the Latin at equal nominal size, so the Hindi UI scale bumps one step where the two scripts sit side by side.
6. Conjunct smoke test: words containing the ksha, tra, jna, and dva conjuncts, a reph word, and a short-i word are rendered at 13, 16, and 32 px; reordering and stacking must be exact.
7. Form controls: inputs, buttons, and labels get fixed heights and explicit line-height; the taller Devanagari line box was resizing rows before the fix.
8. Digits: the portal standardizes on Western digits for both locales, with Devanagari digits U+0966-096F available in the font should the convention change; the decision is recorded.
9. Device verification: low-end Android is a first-class target, because shaping engine differences and font fallbacks surface there first.
10. Case handling: no text-transform anywhere in the Hindi UI; hierarchy comes from weight and size tokens.

Outcome: one component tree with per-language leading and sizing tokens, verified conjunct rendering on real content, and no Latin-only assumptions left in the UI layer.

## Field notes

- Platform substitutes differ: Windows ships Nirmala UI for Indic scripts, macOS uses Devanagari Sangam MN, Android falls back to Noto Sans Devanagari. The no-webfont path should be audited deliberately.
- Devanagari faces are modest in size next to CJK, so aggressive subsetting is rarely worth the risk; if you subset, preserve the layout features that drive conjuncts and half forms.
- The shirorekha is the fingerprint: adjacent fonts with different headline thickness read as a mismatch instantly, so one Devanagari voice per surface is the rule.
- Marathi content leans harder on nukta forms; Sanskrit content exercises vocalic matras (U+0943, U+0944) and avagraha (U+093D) that everyday Hindi rarely hits. Include those strings when the language is in scope.
- Nepali belongs in the test set alongside Hindi; conventions differ enough that a Hindi-only proof is not a Nepali proof.
- Bold parity is a real trap: strong regulars with coarse bolds are common. Compare bolds at both 16 px and 40 px before freezing weights.
- Devanagari digits U+0966-096F exist in every serious family; the digit decision is a content-policy decision, not a coverage one.
- Half forms are a style variable: some families prefer explicit half forms while others stack aggressively; proof a page of real prose, not a conjunct alphabet, to judge which reads better for your content.
- Font-feature support (akhn, half, cjct, rphf) is what you are actually buying; a cmap dump can show full coverage while the shaping tables do half the work.
- Mixed Latin-Devanagari headings expose x-height mismatches faster than body text; proof headlines separately.
- Nukta sequences have a compatibility corner: some pipelines emit precomposed codepoints U+0958-095F while others emit consonant plus U+093C; shapers handle both, but test whichever form your content actually contains.
- The perceived-size bump is family-specific, not a universal constant: some Devanagari designs run large and others compact, so measure the bump per family during proofing.
- At 12-13 px, conjuncts compress before coverage fails; the smallest production size is the one that needs the conjunct set, because legibility collapses first.
- Devanagari in terminal or monospace contexts falls back to the UI face, since mono fonts rarely cover the script; width alignment in mixed log output cannot be guaranteed, so design log views for that reality.
- Justify Hindi by word spacing if at all; the continuous shirorekha makes stretched letter relationships visible faster than in Latin.
- Conjunct spellings vary by tradition and font: the same word can be drawn with a stacked or a horizontal conjunct depending on the font's GSUB design; pick a house style and prefer fonts consistent with it.
- Western digits inside Hindi sentences are drawn by whichever face the stack order hands them to; check which face actually draws them, because digit shapes differing from the surrounding text read as noise.
- Very light Devanagari cuts lose shirorekha definition on light backgrounds; before using a hairline in large marketing type, check the headline stroke at the real background and size.
- Hindi separates words with spaces, so justification behaves conventionally; the shirorekha band makes rivers visible quickly, so proof justified Hindi before enabling it.
- Search result snippets and link previews render Hindi with fonts outside your control; the webfont is not the only surface users see, and the system-font impression counts too.

## Quick reference

- Shaping gates: ksha, tra, jna, dva conjuncts; reph placement; short-i reordering (U+093F); nukta forms.
- Leading: 1.5-1.7 for body, scoped with :lang(hi); never a global value tuned on Latin.
- Never: letter-spacing (it shatters the shirorekha), text-transform-based hierarchy, global tight leading.
- Digits: Western versus Devanagari U+0966-096F, decided per locale in the i18n layer.
- Language tags: lang="hi", lang="mr", lang="sa", lang="ne" as scope requires.
- Defaults: Mukta or Noto Sans Devanagari for UI; Halant or Martel for text; Eczar for display; Noto Serif Devanagari for legal and scholarly.
- Weight check: compare regular and bold at 16 px and 40 px in real words before freezing.
- Stack pattern: Devanagari primary first, Noto Sans Devanagari last; match Latin by apparent weight and proportion, then contrast, then width.
- Proofing set: a page of real prose plus form labels plus one headline, in every language in scope, at three sizes.
- Nukta corner: precomposed U+0958-095F versus consonant plus U+093C; test the exact form your pipeline emits.
- Small-size gate: the conjunct set must survive the smallest production size, not just body text.
- Conjunct style: stacked versus horizontal is a font design decision; set a house preference and proof candidates against it.
- Digit source: decide whether Western digits inside Hindi runs come from the Devanagari face or the Latin face, and pin the stack order accordingly.
- Justified Hindi: proof for rivers along the shirorekha band before enabling text-align: justify.

## Cross-references

- [Southeast Asian scripts](southeast-asian-scripts.md)
- [Mixed script fallbacks](mixed-script-fallbacks.md)
- [OpenType features](../technical/opentype-features.md)
- [Worked examples](../workflow/worked-examples.md)

Compiled 2025 as part of the Fontlore project.
