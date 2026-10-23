# Localization and RTL Accessibility

What this reference covers: The accessibility side of localized typography: lang attributes and their effect on screen reader pronunciation, the dir attribute and logical CSS properties for right-to-left content, bidi isolation for mixed text, and the layout pitfalls that appear only in translated pages. Language tags are the cheapest accessibility feature in web typography.

## Language tags: pronunciation and more

- WCAG 3.1.1 (Language of Page) requires a lang attribute on the html element; 3.1.2 (Language of Parts) requires lang on any content in a different language.
- Screen readers select voice and pronunciation rules from lang: an untagged Arabic paragraph read by an English voice is gibberish; with lang="ar" it becomes intelligible. The same applies to Cyrillic, Greek, Hebrew, Thai, and every non-Latin script, and to Latin-script languages with different pronunciation rules (German, Polish, Turkish).
- lang also drives hyphenation dictionaries (hyphens: auto), locale-aware case mapping (Turkish dotted and dotless i), font selection for Han variants (zh-Hans versus zh-Hant), and the locl OpenType feature.
- Use correct tags: ar for Arabic, fa for Persian, he for Hebrew, hi for Hindi, ja, ko, th, vi; zh-Hans and zh-Hant for the Chinese scripts. Region subtags are rarely needed for text rendering; language subtags carry the work.
- Tag user-generated content too: a profile field, a review, a comment. dir="auto" plus lang detection on render is the practical pattern; per-language lang on mixed segments is the thorough one.

## Direction: dir and logical properties

- Set dir="rtl" on html or on sections for Arabic, Hebrew, Persian, Urdu; dir="ltr" explicitly where needed. dir="auto" on unpredictable user content lets the first strong character decide.
- The dir attribute flips the inline base direction; layout follows when CSS is written logically:
  - Use margin-inline-start instead of margin-left; padding-inline-end instead of padding-right; text-align: start instead of left.
  - Flex and grid order flows with direction automatically; borders become border-inline-start, and so on.
  - Physical properties (left, right, top, bottom) do not flip and are the source of most RTL layout bugs.
- Icons and controls that encode direction (chevrons, "next" arrows, progress direction) should flip under [dir="rtl"] selectors; text and logos must not be mirrored.
- Numbers, dates, and Latin brand names inside RTL text remain left-to-right runs; the Unicode bidirectional algorithm handles them when the text is real Unicode and the base direction is set. Do not reverse strings in code.

## Bidi isolation for mixed content

Mixed-direction text (an English filename inside an Arabic sentence, a Hebrew product name in a French list) is where bidi goes wrong:

- Wrap user-generated or unpredictable segments in bdi elements, or use the Unicode isolate characters; they stop the segment's direction from leaking into surrounding punctuation and layout.
- Test the classic cases: trailing Latin punctuation in an RTL sentence; a URL in an Arabic paragraph; a phone number list in a Hebrew interface; parentheses around mixed runs.
- For fields whose content is directional (filenames, IDs), dir="auto" on the element plus bdi in lists covers most cases.

## Typography adjustments per language

- Line-height: scripts with tall marks need more room; scope with :lang(th) { line-height: 1.7; } and similar rules rather than inflating globally (see the per-script references).
- Letter-spacing: never on Arabic or Devanagari; subtle on Latin labels only.
- Justification: Arabic justification is conventionally done with kashida or word spacing by the shaper, not letter-spacing; hyphens: auto is meaningless for Arabic and harmful-looking in Thai (which has no spaces and relies on dictionary line breaking).
- Measures: a 66ch English article is roughly 30 to 35 hanzi in Japanese; per-language measures are content decisions, not one number.
- Fonts: per-language font stacks with unicode-range subsets; the fallback ordering is a design decision documented in tokens.

## Screen reader and QA specifics

- Verify screen reader language switching: with correct lang attributes, VoiceOver and NVDA switch voices mid-page; this is the single best test for 3.1.2.
- Check heading structure in translated pages: translations lengthen (German runs 20 to 35 percent longer than English), and headings that fit one line in English wrap awkwardly elsewhere; structure must tolerate it.
- Test with the actual locales: an RTL audit with English content proves nothing; audit with real Arabic or Hebrew copy.
- Include localized pages in the zoom, reflow, and text-spacing audits; multilingual pages fail accessibility checks faster than English ones.

## Common mistakes

- Text-align: left and margin-left throughout the stylesheet, producing mirrored pages held together by per-element overrides.
- Missing lang on translated pages, so screen readers read everything in the site's default voice.
- Setting lang="ar" but leaving dir="ltr", or vice versa; both attributes are needed and they do different jobs.
- Reversing Arabic or Hebrew strings in JavaScript to "fix" rendering; it breaks selection, search, copy-paste, and screen readers simultaneously.
- Forgetting lang on user-generated content, so a multilingual comment thread reads as one flat pronunciation.
- Mirroring icons that contain text or logos, and flipping chevrons that indicate "expand" (which is often not directional) along with "next" (which is).

## Decision rules

- Any localized launch: lang plus dir on the page, logical properties audited, per-language leading and measure rules in tokens, screen reader spot check with real copy.
- Mixed-direction UI: bdi on all user-generated list items and fields by default.
- RTL support: decide at the component-library level, not page by page; retrofitting logical properties across a shipped product is a migration.
- If full RTL is out of scope for a release: say so in the locale's documentation; a half-mirrored page is worse than an honest LTR page with correct lang and fonts.
- Any new script added to the product: update the accessibility audit to run on that language's pages before launch.

## Code notes: tags, direction, and isolation

```html
<!-- Page level: both attributes, always -->
<html lang="ar" dir="rtl">

<!-- Language of parts -->
<p>Read the <span lang="en">privacy policy</span> for details.</p>

<!-- Unpredictable user content: isolation plus auto direction -->
<li><bdi dir="auto">{{ username }}</bdi></li>

<!-- A Latin brand name inside RTL text: no reversal, just isolation -->
<p dir="rtl">Product: <bdi>Acme Widget</bdi> - 25 units</p>
```

```css
/* Logical properties: one stylesheet serves both directions */
.nav-item { margin-inline-start: 0.5rem; text-align: start; }
.card { border-inline-start: 3px solid var(--accent); }

/* Directional icons flip; text and logos never do */
.chevron-next { transform: scaleX(1); }
[dir="rtl"] .chevron-next { transform: scaleX(-1); }

/* Per-language leading lives next to the family tokens */
:lang(ar) { line-height: 1.7; }
:lang(th) { line-height: 1.8; }
:lang(hi) { line-height: 1.7; }
```

## Comparison table: per-script typography adjustments

| Script | Leading floor | Letter spacing | Line breaking | Notes |
| --- | --- | --- | --- | --- |
| Latin | 1.5 | Subtle on labels only | Spaces; hyphens with lang | The default all rules are scoped against |
| Arabic, Persian | 1.6 to 1.8 | Never | Spaces; kashida or word-space justification | Justification belongs to the shaper |
| Hebrew | 1.6 | Rarely | Spaces | Vocalized (nikud) text needs more room |
| Devanagari and Indic | 1.7 to 1.8 | Never | Spaces | Conjuncts and matras above and below |
| Thai, Lao, Khmer | 1.8 | Never | Dictionary-based; no hyphens | Mark clipping is the classic failure |
| Han, Kana, Hangul | 1.7 to 1.9 | No | No spaces; strict rules | Count characters, not ch |

The table is a floor, not a spec: verify with native readers and real copy, because within any script the demands vary by face and by content type.

## Worked example: auditing an Arabic product page

A product page localized to Arabic, audited with real copy and a native reviewer:

1. Page shell: lang="ar" and dir="rtl" on html; the stylesheet audited for physical left and right properties; eleven margin-left and two padding-right instances found and converted to logical properties.
2. Bidi: the price row ("AED 1,299") rendered correctly only after the amount was isolated; without bdi the trailing punctuation jumped to the wrong end.
3. Typography: leading raised to 1.7 via :lang(ar); letter-spacing reset to normal because the Latin label tracking had been inherited; the display face swapped for a stack partner with real Arabic coverage, because the brand face had none.
4. Mirroring: "next" chevrons flipped; the "bold" icon did not, because emphasis is not directional; the logo stayed unmirrored.
5. Overrides: the 1.4.12 sweep re-run in Arabic; taller leading plus overrides exposed the same fixed-height cards the English pass had missed.
6. Screen reader: VoiceOver switching voices between the Arabic sections and an embedded English testimonial; the testimonial lacked lang="en" and was fixed.

Six checks, one afternoon, and a page that went from half-mirrored to first-class.

## Quick reference: attributes and when they matter

| Attribute | Where | What it does |
| --- | --- | --- |
| lang | html and any content in another language | Pronunciation, hyphenation, case mapping, font selection, locl |
| dir | html or sections | Inline base direction; pairs with logical CSS |
| dir="auto" | User-generated or unpredictable text | First strong character decides |
| bdi | Usernames, filenames, mixed list items | Isolates the segment so direction cannot leak |
| translate="no" | Brand names, code, product IDs | Keeps machine translation from mangling them |

The last row is the quiet one: without translate="no", translators and browser translation mangle product names and code identifiers in ways that also break screen reader pronunciation and search.

## Field notes: what RTL launches actually surface

- The physical-property audit pays instantly: one search for "left" and "right" in the CSS typically finds dozens of hits, and most are genuine bugs once dir="rtl" ships, each one a mirrored-margin defect in production.
- Punctuation at direction boundaries is the classic bidi bug: a trailing period or a currency sign jumps to the wrong end. Isolating the Latin or numeric run with bdi fixes it without touching the string.
- Form fields are the second wave: inputs for emails and phone numbers keep LTR content direction while their labels flip; the fix is dir="ltr" on those specific inputs, not on the whole form.
- Carousels and steppers are where mirroring rules get debated: "next" flips, "play" does not, and the decision should be written down per icon rather than re-litigated per sprint.
- Translated headings run longer and wrap: a one-line hero in English becomes two lines in German and three in Finnish, and any height-capped hero shows it first.
- Screen reader voice switching is the fastest end-to-end check: one listen through a localized page with mixed content finds missing lang attributes faster than any markup review.
- Numerals are a quiet decision: an interface that mixes European digits with Arabic-Indic content needs a stated policy, or each component invents its own.

## Audit checklist: localized launch gate

- [ ] html carries the correct lang and, for RTL locales, dir="rtl".
- [ ] Every segment in another language carries lang; user-generated content carries bdi and dir="auto".
- [ ] A search for physical properties (margin-left, margin-right, padding-left, padding-right, text-align: left, text-align: right, left, right offsets) returns zero unreviewed hits.
- [ ] Directional icons flip under [dir="rtl"]; text, logos, and non-directional icons do not.
- [ ] :lang() rules for leading and size adjustments exist for every shipped script and live in the token layer.
- [ ] Numerals policy decided (European, Arabic-Indic, script-specific) and rendering matches the decision.
- [ ] Mixed-direction test cases pass: Latin product names in RTL sentences, URLs, phone numbers, quoted strings with punctuation.
- [ ] translate="no" on brand names, product IDs, and code identifiers.
- [ ] Screen reader pass with real copy: voice switches at language boundaries; headings and lists announce sanely.
- [ ] Zoom, reflow, and the 1.4.12 spacing sweep re-run on the localized templates, not just the English ones.

## Cross-references

- [Arabic script typography](../scripts/arabic-script-typography.md)
- [Mixed script fallbacks](../scripts/mixed-script-fallbacks.md)
- [WCAG baseline for type](wcag-baseline-for-type.md)
- [Testing typography accessibility](testing-typography-accessibility.md)

Compiled 2025 as part of the Fontlore project.
