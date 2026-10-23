# Serif, Sans, or Slab

What this reference covers: A decision framework for the biggest classification choice: serif, sans serif, or slab. It weighs medium, size, tone, and tradition, and ends with named pairings and an explicit decision table.

The serif-sans-slab decision shapes everything downstream, so it deserves more than habit. None of the three is modern or old-fashioned by definition; each is a bundle of behaviors you either want or do not.

## What each choice commits you to

- Serif: joins and terminals guide the eye along lines of text; tradition supports long-form reading; details reward attention at large sizes. Costs: more optical complexity at tiny sizes, and cheap serifs read as dated faster.
- Sans: fewer strokes to rasterize, more forgiving on low-DPI screens, naturally neutral in tone. Costs: harder to carry warmth and heritage; the neutrality that helps UI erases brand voice.
- Slab: serifs without the fuss; sturdy, direct, and loud when heavy. Costs: slab body text reads heavy; slabs skew marketing and poster-like, which is either the point or the problem.

## Medium considerations

- Print longform still favors serifs by tradition and by evidence: the serifs help eye movement in continuous text, and centuries of book design built the expectation.
- Screens at small sizes favor sans for resilience; at high DPI the advantage shrinks, and quality serifs render beautifully on modern devices.
- E-readers and reading apps: both work; serif carries the book association, and many readers prefer it for novels.
- Mixed media (print and product from one brand): either pick a superfamily with both (IBM Plex, Source) or accept one family with a defined primary medium.

## Size and function

- Body text: all three can work; sans and text-serifs dominate. Slab body text needs a light, well-spaced design (Bitter exists for exactly this).
- Interface labels, buttons, forms: sans, nearly always. The functional register of UI is baked into sans conventions.
- Headlines: free choice; the serif-sans decision here is tone, not legibility, at modern sizes.
- Data and tables: sans or mono; serifs in table cells fight alignment conventions and rasterization budgets.

## Tone and tradition

- Heritage, academia, law, literature, journalism: serif carries institutional memory (Times New Roman's ubiquity is itself an argument against and for it).
- Technology, government services, transport, healthcare UI: sans is the expected register; deviation needs a reason.
- Marketing, datasheets, western or industrial themes, playful brands: slab is the natural home; Roboto Slab, Zilla Slab, and Archer show the range from tech-friendly to friendly-heritage.
- Brands that must read "human" often choose humanist sans rather than serif; humanism does not require serifs.

## Decision table

- Long-form reading, print or reading app, editorial brand: serif (old-style or transitional).
- Product UI, dashboards, forms, small labels: sans (neo-grotesque or humanist).
- Landing pages with personality to spare, or brands with industrial-retail voice: slab for headings, sans for UI.
- Legal and academic documents where tradition matters: transitional serif; do not innovate here without a mandate.
- One-family brands that need warmth plus neutrality: look for a superfamily (serif plus sans sharing proportions) before choosing a compromise.

## Named pairings

- Source Sans 3 for UI plus Source Serif for long-form: the Adobe superfamily pattern, both open source.
- Inter for product plus Literata for documentation: neutral UI, warm reading.
- IBM Plex Sans plus IBM Plex Mono for technical brands; Plex Serif when print enters the system.
- Roboto Slab for marketing headlines plus Roboto for product: cheap to obtain, hard to make distinctive.
- Public Sans (built for US government use) plus a serif of choice for long-form: reliability-first pairing.

## Common mistakes

- Choosing sans by default for everything, then wondering why the brand has no voice.
- Choosing a serif by default for "credibility" and shipping it into a UI it was never built for.
- Slab body text in long documents; slabs are usually a display and marketing tool.
- Treating the decision as permanent; brands re-scope (new product line, new market) and the framework should be re-run, not inherited.
- Pairing a serif and a sans from unrelated eras and proportions, producing a two-font system that looks like an accident.

## Decision rules

- Decide by primary reading medium first, tone second, trend never.
- If the product is UI-heavy and the brand needs warmth, buy warmth through weight and humanist design, not through a serif pasted onto UI.
- If print is the primary medium, start from serif and justify the departure, rather than the reverse.
- Whatever you choose, the choice is a system decision: document it with reasons so the next designer inherits a decision, not an accident.

## Comparison table

The three choices across the dimensions that actually decide projects. No row is a verdict; the columns are bundles of behavior to want or not want.

| Dimension | Serif | Sans | Slab |
| --- | --- | --- | --- |
| Rasterizes at 13px | Details can close; test serifs | Forgiving; the safe default | Sturdy; often reads heavy at body sizes |
| Long-form reading | The tradition, print and ebook | Works well with modern text designs | Needs a light, well-spaced design |
| UI labels and forms | Rarely the register | The expected voice | Too loud for controls |
| Tables and data | Fights alignment conventions | Natural fit | Only in mono form |
| Headline tone | Heritage, editorial, literary | Neutral to technical | Direct, industrial, friendly-loud |
| Print heritage | Centuries of book design | 20th-century institutional | 19th-century poster and jobbing |
| Numerals flavor | Old-style figures common in text designs | Lining figures standard | Lining, sturdy |
| Dating risk | Cheap revivals date fastest | Neutrality ages slowly | Retro slabs date in cycles |
| Free exemplars | Literata, Source Serif, Merriweather, PT Serif | Inter, Source Sans 3, Public Sans, Work Sans | Roboto Slab, Zilla Slab, Bitter |
| Commercial exemplars | Minion, Times New Roman | Helvetica, Univers, Frutiger | Rockwell, Archer |

Mixed-media brands resolve most rows by picking a superfamily rather than compromising one family; see the superfamily reference before settling for a middle ground.

## Worked example

Deciding for a developer platform with a data-heavy app, a large documentation corpus, and PDF exports. The decision is run as a system decision, not a single-family decision.

1. Inventory the surfaces: dashboard, settings, forms, marketing pages, long documentation, PDF exports of that documentation.
2. Medium rule: screen-first with heavy UI pulls the default register toward sans for the product surface.
3. Docs rule: 20-minute reading sessions in the documentation pull toward a text serif for article bodies.
4. Tone words from the brief ("engineered, calm, trustworthy") support the sans register for product; the serif carries the calm of long reading.
5. Slab considered for marketing headlines and rejected: it fights the "calm" trait and adds a third voice to a two-voice system.
6. Didone considered and rejected for the same reason; drama in a trust product needs a mandate the brief does not give.
7. Decision: sans for product UI, serif for documentation body, one mono for code.
8. Superfamily first: the Source family covers sans, serif, and code with shared proportions and open licenses; the shortcut is taken.
9. Alternative check: IBM Plex covers the same jobs with a stronger technical voice; it is recorded as the runner-up system.
10. The serif is verified at reading sizes: Source Serif holds at 17px with 1.6 line-height over a 68-character measure.
11. The sans is verified at UI sizes: 13px labels keep open apertures on the worst display in the fleet.
12. Numerals policy agreed across both families: tabular in tables, proportional in prose, recorded once in tokens.
13. Governance: all three members are open source, pinned by version, with license files committed alongside the fonts.
14. The decision is documented with reasons in the design system docs so the next designer inherits a decision, not an accident.

The reusable pattern: medium first, tone second, trend never; then verify at real sizes and record the reasons.

## Field notes

- The serif-sans decision for headlines is tone; for body it is behavior. Separate the two questions or the debate never ends.
- Sans-by-default brands often have no voice; the default is a decision too, and it deserves a written reason.
- Serif-in-UI is where credibility projects go to look dated; the register of UI is baked into sans conventions.
- Slab body text needs a light, open design built for it (Bitter exists for exactly this); heavy slabs in paragraphs read as shouting.
- Print heritage cuts both ways: serifs carry credibility and 1990s corporate memory equally well.
- On high-DPI screens the sans advantage mostly disappears; on the worst 1x laptop it is still real.
- If print is the primary medium, start from serif and justify the departure, not the reverse.
- Warmth in UI comes from humanist design and weight, not from pasting a serif onto controls.
- Pairing a serif and sans from unrelated eras reads as an accident; match proportions or use a superfamily.
- Georgia is the bridge case: a serif that behaves like a UI face; it earned that by being designed for screens.
- Data-heavy screens want sans or mono in cells; serifs in table cells fight alignment and rasterization budgets.
- One-family brands with warmth needs should look at superfamilies before compromising a single choice.
- Test the decision at the edges: legal text, error messages, and empty states expose register mismatches fast.
- Re-run the framework when scope changes; a decision right for the dashboard can be wrong for the new marketing site.
- The "serif equals credible" reflex is real and wrong often enough to test every time.
- Document the choice per surface (product, docs, marketing); the system is the decision, not the family.

## Quick reference

- Decide by primary reading medium first, tone second, trend never.
- Product UI, forms, dashboards, small labels: sans, nearly always.
- Long-form reading, print or reading app, editorial brand: serif, old-style or transitional.
- Marketing headlines with personality to spare, industrial or retail voice: slab for headings, sans for UI.
- Legal and academic documents where tradition matters: transitional serif; do not innovate without a mandate.
- Data and tables: sans or mono; never proportional serifs in cells.
- Slab body text only with a light, well-spaced design built for reading.
- Warmth needs in UI: humanist sans design, not a serif pasted onto controls.
- Mixed media: prefer a superfamily (Source, IBM Plex) over a compromise single family.
- Free starting points: Inter, Source Sans 3, Public Sans for sans; Literata, Source Serif, Merriweather, PT Serif for serif; Roboto Slab, Zilla Slab, Bitter for slab.
- Check numerals modes across the chosen faces before committing.
- Verify every choice at 13px on the worst display you support.
- Re-run the framework when the product's scope or audience changes.
- Document per-surface choices with reasons in the design system docs.
- Whatever you choose, name it in tokens so the choice survives team turnover.
- If two options still tie, pick the one with better governance and broader coverage.

## Cross-references

- [Classification primer](classification-primer.md)
- [Choosing body typefaces](choosing-body-typefaces.md)
- [Superfamily and family systems](superfamily-and-family-systems.md)
- [Personality and tone](personality-and-tone.md)

Compiled 2025 as part of the Fontlore project.
