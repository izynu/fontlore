# Editorial and News

What this reference covers: Typography systems for editorial publications: the division of labor between display and text faces, a complete hierarchy from kicker to caption, figure and pull-quote conventions, and the byline-and-metadata layer. Editorial is where typographic hierarchy earns its keep, because the hierarchy is the product.

## Display versus text: the division of labor

Editorial systems run on two families (or a superfamily) with opposite specializations:

- The display face owns headlines, section openers, and pull quotes: high contrast, tight spacing, personality at 28 px and up. It is judged at headline sizes and never set below about 20 px.
- The text face owns body copy: sturdy, open-apertured, large x-height, forgiving at 16 to 18 px across long sessions. Newsreader, Source Serif 4, Literata, PT Serif, Lora, and Noto Serif are the proven open text faces; Playfair Display, Fraunces, and Libre Caslon serve the display end.
- The test of a pairing: set a real headline at 40 px and the same article's body at 17 px; if both look like they belong to one publication, the pairing works. Shared skeleton (proportions, terminal style) matters more than matching era.

Newspaper tradition adds a third voice for captions, bylines, and kickers, usually a sans or the text face italic; modern systems often standardize this on one UI sans (Inter, Source Sans 3) for cross-platform crispness at 12 to 13 px.

## The hierarchy, layer by layer

A complete editorial hierarchy, from top to bottom, each with its own typographic rules:

- Kicker or eyebrow: 12 to 13 px sans, tracked uppercase, one section name or beat; short strings only.
- Headline: display face, 28 to 48 px (responsive), tight leading 1.1 to 1.2, sentence case in most modern systems; headline case styles must survive long strings, so test the longest headline in the CMS, not the average one.
- Deck or standfirst: 18 to 22 px text face, regular weight, 1.4 leading, one or two sentences summarizing the piece.
- Byline and dateline: 13 px sans, byline name at 500 or 600 weight; small caps are traditional and safe because strings are short.
- Body: text face 17 to 18 px, 1.6 leading, 60 to 70ch measure, left-aligned or justified-with-hyphenation.
- Subheadings inside articles: 20 to 24 px, either face; consistency beats cleverness.
- Pull quotes: display face 24 to 32 px, quoted or ruled, never centered mid-paragraph without separation.
- Captions and credits: 12 to 13 px sans, credit right-aligned or after an em-space rule (in ASCII terms, a separator), italic optional and consistent.
- Folios, section labels, timestamps: 12 px sans, tabular figures for anything numeric.

## Body text specifics

- Old-style figures in running prose suit literary work; news and data journalism keep lining figures so numbers do not dance. One decision per publication, applied everywhere.
- Bold in body: reserved for real emphasis, set at 600 or 700 with a real bold cut; link styling is underlined text-face, never color alone.
- Paragraphs: either first-line indent with no paragraph space (book tradition) or spaced paragraphs (web tradition); do not mix.
- Drop caps: a display-roman tradition that needs careful baseline math; if the CMS cannot guarantee them, skip them rather than fake them.
- Lists and blockquotes inherit the body leading and measure; blockquotes get an indent and a rule or weight change, not a size change.

## Designing for the CMS reality

- Headlines are written by humans at all lengths: set hard maximums in the template and check the longest real headlines monthly; truncation rules for lists must match.
- Articles include what templates forget: tables, footnotes, block quotes with attribution, code (for tech desks), and mathematical or currency notation. Each needs a defined style before launch, or the desk invents one.
- Style guides at the publication level (headline case, byline format, caption format) are typography documents; keep them with the design tokens, not in a PDF.

## Common mistakes

- One family doing everything: display faces shatter at body sizes and text faces go limp at headline sizes; the division of labor exists for a reason.
- Kicker and caption styles applied to long strings; tracked caps die beyond a few words.
- Deck and body too close in size (20 versus 17) with no weight or style change; the deck disappears.
- Body measure drifting to 90 or 100 characters on wide screens because the article container inherits the layout width.
- Captions larger than the byline, or six sizes of sans doing the metadata jobs; collapse metadata to one style with weight variation.
- Pull quotes in the middle of a column with no vertical separation, so readers cannot tell article voice from quoted voice.

## Decision rules

- New publication: choose the text face first (it carries the reading), then the display face (it carries the brand), then the metadata sans.
- Pairing check: shared proportions and skeleton at two sizes beat any "era matching" folklore.
- Any new element type (recipe cards, live blogs, explainers): define its full stack of styles before the first one ships.
- Long-form product (features, longreads): consider a separate, larger body size and looser measure; features and briefs may share a system but not the same values.
- If hierarchy feels weak: add weight and spacing before adding a third family.

## Comparison table: open text faces for news reading

The text face carries the publication; choose it first and test it hardest:

| Face | Weights | Optical sizes | Character | Watch-outs |
| --- | --- | --- | --- | --- |
| Newsreader | 200-800 | opsz 6 to 72 | editorial serif with a calligraphic touch | pin the text range; the display end is high contrast |
| Source Serif 4 | 200-900 | opsz axis | sturdy, transparent, excellent at 17 px | even-tempered to the point of generic at display sizes |
| Lora | 400-700 | weight only | brushed, warm, genuinely expressive italics | four weights; no light or black |
| Merriweather | 300 to 900 | none | very large x-height, built for screens | runs wide on dense grids and phone columns |
| PT Serif | 400, 700 | none | pragmatic, Cyrillic-first | narrow range; limited styling options |

- Newsreader's optical size axis is the most useful in the group: one file serves captions and headlines with appropriate contrast at each size.
- Source Serif 4 and Source Sans 3 share a skeleton, which hands you a matched metadata sans almost for free.
- Merriweather earns its keep on harsh displays and old hardware; on retina it reads heavy next to a crisp sans.
- Lora's italics carry opinion writing; for desks that italicize generously, it is the pick.
- PT Serif stays the pragmatic fallback when a desk needs maximum compatibility with minimum files.
- All five are open licensed; pair with a grotesque display (Archivo, Space Grotesk) for a modern news voice, or a serif display (Fraunces, Playfair Display) for a traditional one.
- Audition candidates with your own worst strings: census tables, compound German headlines, and the longest byline in the archive.

## Worked example: a metro news site relaunch

Scenario: a city newspaper rebuilds its site: briefs to 4,000-word features, a growing data desk, no commercial font budget, and a CMS that has already shipped every element type except the ones being read here.

- Body: Source Serif 4 at 17 px, 1.6 leading, 66ch measure, weight 400; optical sizing left to the browser's automatic behavior.
- Display: Archivo at 600 for headlines, clamped 28 to 48 px, leading 1.12; one grotesque voice keeps briefs and features in one family.
- Metadata: Archivo again at 12 to 13 px (kickers at 500, bylines at 600), tabular figures for timestamps; one sans doing three jobs beats three sanses doing one each.
- Subheads: Source Serif 4 at 21 px, weight 600; the text face at a heavier weight keeps the article one voice.
- Deck: Source Serif 4 at 20 px, regular, 1.4 leading, one or two sentences.
- Captions and credits: 12.5 px Archivo, credit after a separator, italic use consistent; folios and section labels at 12 px tabular.
- Data stories: tables in Archivo with tabular-nums at 13 px, right-aligned numerals; chart labels the same style.
- Pull quotes: Archivo 600 at 24 to 28 px with a rule above; never centered mid-column.
- Longest-headline test: a CMS query for the longest real headline per section runs monthly; clamp values and truncation rules update from it.
- Rejected: Merriweather for body (too wide for the 360 px phone column) and Fraunces for display (it pulled the site toward features and away from metro urgency).
- License posture: all OFL, versions pinned in the repository; the print edition negotiates its own paper-grade files.
- Aftermath: one body file, one display file, one metadata style, and a desk that stopped arguing because every element had a written rule.

## Field notes

- The hierarchy is the product; readers navigate by size, weight, and rhythm long before they notice the family.
- Kickers die beyond three or four words; a tracked-caps style is a length contract with the desk.
- Bylines and captions want one style with weight variation, not six sizes of sans.
- Decks barely larger than body disappear; if size is unaffordable, change face or weight.
- Justified text without hyphenation makes rivers; justified with hyphenation needs language support the CMS must declare.
- Drop caps fail silently when the CMS wraps the first word in a link; spec the fallback before the feature.
- Footnotes, tables, and code blocks arrive after launch, guaranteed; style them in the template, not in the incident.
- Live blogs reflow every minute; tabular timestamps and fixed metadata heights keep the page from jittering.
- Related-article modules reuse headline styles at smaller sizes; test the style at 18 px before blessing it at 40 px.
- Print heritage still pays: small caps for bylines, rules above captions, consistent quote handling.
- RSS and reader modes strip styles; the words must carry hierarchy without you.
- Ampersands and numerals in headlines are glyph auditions; check the display face's ampersand against the masthead's tone.
- Dashes, quotes, and diacritics appear in real headlines more than in specimens; proof in the CMS, not the design file.
- Section fronts are scanning surfaces: same styles, tighter spacing, stricter truncation.
- Comment counts, share counts, read times: tabular figures, or the numbers dance on every load.
- Article pages host ads and embeds; the type system needs rules for third-party blocks or the ads will set them.
- Archive pages (decade-old articles) render through the same system; test a 2005 article before declaring the relaunch done.
- Whatever the desk writes, the template must set; typography that only works for well-behaved copy is not done.

## Quick reference: editorial spec card

- Kicker: 12 to 13 px sans, 500 to 600, tracked caps, three words maximum.
- Headline: display face 28 to 48 px, leading 1.1 to 1.2, sentence case by default.
- Deck: text face 18 to 22 px, regular, 1.4 leading.
- Byline and dateline: 13 px sans, name at 500 or 600, tabular dates.
- Body: text face 17 to 18 px, 1.6 leading, 60 to 70ch, left or justified-with-hyphens.
- Subheads: 20 to 24 px, consistent face and weight.
- Pull quotes: 24 to 32 px display, rule or indent, never centered mid-column.
- Captions and credits: 12 to 13 px sans, italic consistent, credit separated.
- Folios and timestamps: 12 px, tabular figures.
- Display face floor: never below 20 px.
- Metadata: one style plus weights, not a second family per job.
- News and data journalism: lining figures; old-style only by explicit literary policy.
- The longest-string test runs monthly against the live CMS.
- Choose the text face first, display second, metadata sans third.
- Weak hierarchy: add weight and spacing before adding a third family.
- Every new element type gets a full style stack before its first article ships.
- Deck and body separated by face or weight, not size alone.
- Links in body are underlined text-face links; color alone never carries them.
- Blockquotes keep body size; hierarchy via indent and rule.
- Bold in body reserved for real emphasis at a true 600 or 700 cut.
- Paragraph convention: indent or space, never both.
- Timestamps and counters tabular everywhere they appear.

## Cross-references

- [Line length and reading](../accessibility/line-length-and-reading.md)
- [Numerals and notation](../scripts/numerals-and-notation.md)
- [OpenType features](../technical/opentype-features.md)
- [Worked examples](../workflow/worked-examples.md)

Compiled 2025 as part of the Fontlore project.
