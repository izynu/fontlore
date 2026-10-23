# Choosing Body Typefaces

What this reference covers: The criteria that separate typefaces that read comfortably in paragraphs from ones that only work in headlines. It covers x-height and aperture, spacing and weight range, screen rendering behavior, and a testing method for body text specifically.

Body text is where typefaces earn their keep and where most failures hide. A face can look distinguished in a specimen and exhausting after two paragraphs. The criteria below predict that difference before your users suffer it.

## The physical criteria

- X-height should be moderate to tall for screen body text. Small-x-height faces like classic Garamond revivals need larger point sizes to match the perceived size of Georgia or Inter, and UI budgets rarely allow that.
- Aperture matters more than most reviewers realize. Open apertures (as in Source Sans or Verdana) keep small letters distinct; nearly closed apertures (some grotesques) fuse c, e, and s at 12px.
- Even color beats drama. Body faces want consistent stroke weights so paragraphs read as texture; high stroke contrast belongs to display sizes.
- Sturdy, slightly generous letter spacing survives hinting and rasterization; tightly spaced display cuts shred at small sizes.
- Ascenders and descenders should be long enough to distinguish letters but not so long they force loose line spacing to avoid collisions.

## Weight and family range

- A body face needs a true regular that is neither thin nor heavy on your background and a bold that is clearly bolder at 14px, not just at 48px.
- Check that the bold works in running text, not just headings; many display-derived bolds are too tight to read in sentences.
- True italics are a requirement for editorial content. Obliques (slanted romans) betray a face that was never designed for text emphasis.
- If the product needs 300 or 500 weights, confirm they exist and render well; a family with one regular cannot carry a system.
- Subheads and small caps are bonuses; body fitness is the requirement.

## Screen rendering behavior

- Hinting still matters at text sizes on Windows and low-density displays. Test on the worst screen you support, not a Retina display.
- Very thin hairlines drop out at small sizes on some displays; strokes need a minimum weight that survives rasterization.
- Variable fonts render well in modern browsers, but check whether intermediate weights snap to sensible instances on older platforms.
- Dark mode inverts the rendering problem: light text on dark spreads optically, so faces that rely on delicate strokes may need a weight bump or a different cut.
- Compare the face against a known benchmark (Georgia, Verdana, or Inter) at identical sizes and x-heights before judging.

## Proven body families

- Serif: Charter and its derivatives (including Charis SIL), Source Serif, Literata (designed for Google Play Books), PT Serif, Merriweather, and Georgia remain the reference screen serifs.
- Sans: Inter (designed by Rasmus Andersson for screens), Public Sans (built for US government design system work), Source Sans 3, IBM Plex Sans, Atkinson Hyperlegible (commissioned by the Braille Institute for legibility research).
- Slab: Bitter was designed for ebook reading and holds up in long-form web text.
- This is a starting set, not a verdict; your copy, sizes, and rendering stack decide.

## Testing with real copy

- Test the actual content: legal text, error messages, prices, names with diacritics. Marketing copy flatters every typeface.
- Read two full screens of body text in the candidate. Discomfort accumulates over minutes, not seconds; a glance proves nothing.
- Set the same paragraph in the incumbent and the candidate at matched x-height, not matched point size, to compare fairly.
- Check the paragraph as a shape: even gray, no rivers, no strobe effect from uneven stems.

## Decision rules

- Long-form reading (articles, documentation): favor moderate contrast, generous x-height, open apertures, true italics.
- Interface labels and data: favor even widths and tabular numerals; personality is secondary.
- If the face fails at 13 to 14px in your worst rendering environment, it fails, regardless of how it looks in a design tool.
- When in doubt between two candidates, pick the one with more weights and a true italic; body systems grow.

## Common mistakes

- Choosing a display face for body text because it photographs well in the portfolio.
- Judging at 16px on a laptop and shipping to phones without testing.
- Ignoring numerals in a data-heavy product until tables wobble.
- Using a face without a true italic and shipping faux italics to editorial content.
- Matching point sizes across faces with wildly different x-heights and wondering why one "looks smaller".
- Overloading body text with weights (200 for elegance) that render as gray mush.

## Comparison table

A first-pass map of proven body faces. The x-height column is relative feel, not a measurement; treat rows as orientation and verify any candidate at your final sizes before trusting it further.

Sans candidates:

| Family | Class | Designer or origin | X-height feel | True italic | Standing |
| --- | --- | --- | --- | --- | --- |
| Inter | Neo-grotesque sans | Rasmus Andersson | Very tall | Yes | The screen-default sans; variable, wide weight range |
| Source Sans 3 | Humanist sans | Adobe (Frank Griesshammer) | Tall | Yes | Adobe's first open-source family; built for UI and text |
| IBM Plex Sans | Neo-grotesque-leaning sans | IBM with Bold Monday | Tall | Yes | Technical voice; completes with Plex Serif and Plex Mono |
| Public Sans | Neo-grotesque sans | US government design system | Tall | Yes | Neutral civic register; derived from Libre Franklin |
| Work Sans | Grotesque sans | Wei Huang | Tall | Yes | More warmth than Inter; variable |
| Roboto | Neo-grotesque sans | Google | Tall | Yes | Ubiquitous through Android; dependable everywhere |
| Nunito | Rounded sans | Vernon Adams | Tall | Yes | Rounded friendliness for consumer products |
| Verdana | Screen sans | Matthew Carter | Very tall | Yes | The historical benchmark for small screens |
| Atkinson Hyperlegible | Grotesque sans | Braille Institute | Very tall | Yes | Letterforms shaped by legibility research |

Serif candidates:

| Family | Class | Designer or origin | X-height feel | True italic | Standing |
| --- | --- | --- | --- | --- | --- |
| Literata | Transitional serif | Commissioned for Google Play Books | Moderate | Yes | Built for sustained ebook reading |
| Source Serif | Transitional serif | Adobe | Tall | Yes | Sturdy text serif from the Source system |
| Merriweather | Transitional-leaning serif | Sorkin Type (Eben Sorkin) | Tall | Yes | Sturdy serifs and open forms made for screens |
| Newsreader | Text-to-display serif | Production Type | Moderate | Yes | News-reading serif with an optical size axis |
| Lora | Contemporary serif | Cyreal | Moderate | Yes | Curves rooted in calligraphy; variable |
| PT Serif | Transitional serif | ParaType (Alexandra Korolkova) | Tall | Yes | Broad language coverage at zero budget |
| Bitter | Slab | Designed for ebook reading | Tall | Yes | The slab that survives long-form text |
| Charter | Transitional serif | Matthew Carter | Moderate | Yes | The print-to-screen benchmark lineage |
| Charis SIL | Old-style-leaning serif | SIL International, Charter-derived | Moderate | Yes | Long-standing use in accessibility and ebooks |

Reading notes: sans rows carry interface weight, serif rows carry editorial weight, and the two groups are compared at matched x-height, never at matched point size. Rows are entry points, not rankings.

## Worked example

Shortlisting a body face for a developer documentation site. Constraints: 16px target body size, mandatory dark mode, code blocks interleaved with prose, open-source-only dependency policy, and readers who spend 20 minutes at a stretch in API reference text.

1. License and packaging first: only OFL or Apache-2.0 candidates with a maintained package stay in the round; anything proprietary drops before aesthetics are discussed.
2. Structure filter: a true italic is required for inline emphasis inside prose, which quietly removes every oblique-only candidate.
3. Weight filter: 400 and 600 minimum, with the variable build checked for sensible intermediate instances on older browsers.
4. Read test: the same 700-word authentication guide set in Inter, Source Sans 3, and IBM Plex Sans at 16px, line-height 1.55, measure capped at 70 characters.
5. Small-size test: sample paragraphs at 13px equivalent on a low-DPI laptop, the worst supported environment; apertures must stay open and counters distinct.
6. Dark-mode test: light-on-dark at the same sizes; Source Sans 3 keeps the most even color, while the others need a small weight bump to stop thin strokes spreading.
7. Numerals check: version numbers, port numbers, and status codes run inline throughout; all three finalists keep an even figure rhythm.
8. Coverage check: the product ships Czech and Turkish locales, so Latin extended coverage is verified against rendered diacritics, not assumed from the subset list.
9. Pairing check: the documentation face is tested against the incumbent UI face at matched x-height so 13px labels and 16px prose read as one system.
10. Governance check: upstream activity, release cadence, and packaging health are scored; a maintained face beats a prettier abandoned one.
11. Outcome: Source Sans 3 carries documentation body text; Inter stays as the UI layer with tabular figures for tables; sizes, weights, and line-heights are recorded in tokens.
12. Rejection reasons are written down: the serif finalists lost on dark-mode color at 13px, not on taste, and that record is what survives the next redesign debate.

The reusable pattern: license filter, structure filter, real-copy read test, worst-environment render test, numerals and coverage checks, matched-x-height reconciliation.

## Field notes

- Matched point sizes lie; matched x-heights are the only fair fight between an old-style serif and a screen sans.
- The bold that looks crisp in a headline often turns to ink-blots in a paragraph; always test bold in running text, not in isolation.
- Faux italics are a visible defect in editorial copy and easy to miss in a design tool that synthesizes slants for you.
- Print-designed faces arrive with spacing logic that assumes ink gain; on screens they read loose, and the fix is size discipline, not tracking changes.
- Two full screens of reading is the minimum test; discomfort accumulates around minute three, not in the first paragraph.
- Rivers show up in justified settings and narrow columns, not in the specimen row; test the worst measure, not the best.
- Prices, IDs, and timestamps expose figure-width failures before anything else; put a row of amounts in every comparison page.
- Line length changes color: the same face at 90 characters reads lighter than at 60, so hold the measure constant when comparing.
- Dark mode is a different font problem, not just inverted colors; judge candidates in both modes or you will judge them wrongly in one.
- Hinting still separates faces on low-DPI Windows; verify the packaged build, not the design-tool rendering.
- If marketing insists on a body face you doubt, run the two-screen test with them in the room; it settles more arguments than any memo.
- The face you can license, package, and govern beats the slightly nicer face you cannot; body text is infrastructure.

## Quick reference

- X-height: 50 to 55 percent of the em is the working zone for UI body text on screens.
- Measure: 45 to 75 characters per line; the low 60s is the common target for articles and documentation.
- Sizes: 14 to 16px for UI body, 16 to 20px for long-form reading, 11 to 13px for captions and small labels.
- Line-height: 1.4 to 1.6 for body; taller x-heights and longer measures push toward the top of the range.
- Weights: a 400 that is neither thin nor heavy on your background, and a 600 or 700 that is visibly bolder at 14px.
- Numerals: proportional for prose, tabular for tables; confirm both exist before adopting.
- Italics: true italics for editorial content; obliques only where the register is functional.
- Apertures: open enough that c, e, and s stay distinct at 13px on a low-DPI screen.
- Rendering: test on the worst screen you support before judging on a Retina display.
- Variable builds: check that intermediate weights render as sensible instances on older platforms.
- Benchmarks: compare any candidate against Inter or Georgia at matched x-height before deciding.
- Governance: record family, version, license, and weight set in the manifest at adoption.

## Cross-references

- [Classification primer](classification-primer.md)
- [X-height and legibility](x-height-and-legibility.md)
- [Serif, sans, or slab](serif-sans-or-slab.md)
- [Scoring and shortlisting](scoring-and-shortlisting.md)

Compiled 2025 as part of the Fontlore project.
