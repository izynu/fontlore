# Choosing Display Typefaces

What this reference covers: How to select typefaces for headlines, hero sections, and oversized moments: personality, contrast, optical sizes, tracking, and the discipline of knowing when a display face should not be used. It includes named examples and a selection workflow.

Display faces are allowed to be difficult: tight spacing, high contrast, quirky details. Those same qualities disqualify them from small sizes. The craft is pairing that difficulty with restraint about where it appears.

## What display means

- Display faces are designed for large sizes: tighter letter spacing, higher contrast where the genre calls for it, and details that reward attention.
- Optical sizing formalizes this: families with an opsz axis (Fraunces is a strong variable example) shift contrast and spacing as size changes, so one file serves both ends.
- Families without optical sizes force a compromise: either a text face stretched up (safe but flat) or a display face pushed down (dangerous).
- A display face used at 16px is a legibility bug, not a style choice.

## Personality and contrast

- High contrast (thick-thin strokes, hairlines) reads as editorial, fashion, or luxury: Playfair Display, Abril Fatface, Bodoni-derived faces.
- Low contrast with sturdy strokes reads as dependable and modern: most grotesques and geometric faces.
- Quirky details (unexpected terminals, off-axis stress, charm in the details) carry brand personality; Fraunces' SOFT and WONK axes exist precisely to dial personality in and out.
- Texture matters at display sizes: what reads as "even" in text reads as "boring" at 96px, and what reads as "lively" at 96px reads as "noise" at 14px.

## Tracking and spacing

- Display sizes tolerate and often need negative tracking; text sizes do not. A face pre-tightened for display should not be re-tightened further.
- All-caps headlines usually want positive tracking regardless of size; caps are wider and denser than lowercase.
- Check the face's built-in kerning on awkward pairs (AV, To, Ly) in your actual headline vocabulary; quirky faces often hide surprises there.
- Tight leading (line-height around 1.0 to 1.15) suits display lockups; never carry that leading into body text.

## When to avoid display faces

- Body copy, obviously, but also: UI labels, buttons, forms, data tables, and anything that wraps unpredictably.
- Long headline strings: quirky details fatigue over 60 characters. Save the display face for the 3-to-8-word moments.
- Highly regulated or accessibility-critical text: contrast extremes and tight apertures cut legibility for low-vision readers.
- Mixed-script contexts where the display face has no real coverage; a display Latin with fallback Latin for "special" glyphs is a visible seam.

## Proven display choices

- Fraunces: variable serif with opsz, SOFT, and WONK axes; can swing from old-style warmth to fatface display.
- Playfair Display: transitional-didone flavor, widely available, strong in editorial contexts.
- Abril Fatface: poster fatface for short, bold statements.
- Cooper Black: the friendly heavyweight; ironic warmth when that is the brief.
- League Gothic: condensed sans for tall, narrow headlines; a free classic.
- Space Grotesk and Space Mono: quirky-technical voices from Colophon Foundry for tech brands.
- Commercial display work at scale: GT Sectra (Grilli Type) and Degular (OH no Type Company) show how foundries build display systems with optical discipline.

## Workflow

1. Write the headline vocabulary first: the 20 phrases your product actually says. Display faces must survive those, not lorem ipsum.
2. Shortlist faces by intended tone, then test each phrase at final size, in final color, on final background.
3. Check caps, numerals, and punctuation; headlines use them disproportionately.
4. Set the display face against the intended body face and verify the pair does not fight (two strong voices usually do).
5. Define usage rules in the design system: minimum size, max length, allowed weights, tracking offsets.

## Common mistakes

- Using one display face for every heading level, including small eyebrows and captions.
- Choosing personality so strong that the face ages with the trend cycle it came from.
- Ignoring optical sizes and shipping a text-optical cut at hero scale (or the reverse).
- Letting a display face into forms and tables because the design file "needed variety".
- Picking by alphabet-soup trend rather than by fit to the actual headline vocabulary.
- Forgetting to check that the display face's numerals and currency glyphs exist and match the brand's prices.

## Decision rules

- Headlines under 10 words with brand voice to spare: display face, high personality.
- Headlines that wrap to two lines or more on mobile: pull personality back, favor sturdier cuts.
- One-voice systems (single family): use a family with a wide opsz axis instead of bolting on a separate display face.
- If the display choice needs a paragraph of explanation to justify, it is probably wrong for the audience, right for the portfolio.

## Comparison table

Orientation for common display candidates. The comfort zone column is the size band where the face stops needing apologies, assuming normal rendering and tested sizes.

| Face | Genre | Designer or origin | Axes to know | Comfort zone | Voice |
| --- | --- | --- | --- | --- | --- |
| Fraunces | Old-style to fatface serif | Undercase Type | opsz, wght, SOFT, WONK | 24px to hero scale | Warm, wonky, archival-modern |
| Playfair Display | Transitional-didone serif | Claus Eggers Sorensen | wght | 32px and up | Editorial, literary, fashion |
| Abril Fatface | Fatface poster serif | TypeTogether | wght | 40px and up | Loud, short, poster statements |
| Newsreader | Text-to-display serif | Production Type | opsz, wght | 20px to hero via opsz | Literary, news, restrained drama |
| Space Grotesk | Grotesque sans | Florian Karsten | wght | 20px and up | Technical, wry, engineered |
| Montserrat | Geometric sans | Julieta Ulanovsky | wght | 20px and up | Urban, confident, startup-default |
| Poppins | Geometric sans | Indian Type Foundry | wght | 20px and up | Rounded geometry, monolinear |
| Nunito | Rounded sans | Vernon Adams | wght | 20px and up | Soft, approachable, consumer |
| League Gothic | Condensed sans | League of Moveable Type revival | wght | 28px and up | Tall, urgent, poster |
| Zilla Slab | Typewriter slab | Typotheque for Mozilla | wght | 24px and up | Engineering voice with warmth |
| Archivo | Grotesque with width axis | Omnibus-Type | wght, wdth | 24px and up | Press, poster, flexible width |
| Space Mono | Quirky mono accent | Colophon Foundry | wght | 18px and up | Technical branding, deliberate friction |
| Cooper Black | Friendly heavyweight | Oswald Bruce Cooper | Static | 36px and up | Ironic warmth, retro retail |
| GT Sectra | Calligraphic-broad-nib display | Grilli Type | wght | 28px and up | Sharp, literary with an edge |
| Degular | Grotesque display system | OH no Type Company | wght, opsz | Full range via opsz | Contemporary American grotesque |

Rows are entry points, not rankings; a face that tops this table can still be wrong for your headline vocabulary. Check italic availability separately: Space Grotesk and League Gothic builds, for example, are commonly used without one.

## Worked example

Choosing a display face for a fintech landing page. Constraints: headlines of 4 to 8 words, a trust-heavy audience, body text set in Inter, and a hero that must survive 320px-wide phones.

1. Translate the brief's tone words ("confident, precise, human") into traits: moderate contrast, no gimmick details, a controlled hint of warmth.
2. Candidate set: Fraunces, Playfair Display, Space Grotesk, Montserrat. Each receives the same five headlines marketing actually runs, not a specimen alphabet.
3. Size-band test at the smallest real display size, 28px on the narrow phone: Playfair's hairlines thin out and it drops.
4. Pairing test against Inter: Space Grotesk and Inter compete for the same neutral-technical job, and the page reads as a lab rather than a brand; it drops.
5. Differentiation check: Montserrat passes every legibility gate and fails the voice one; it reads as the default startup face of the last decade.
6. Fraunces survives all gates, so the test narrows to axis settings rather than family choice.
7. opsz is anchored: hero sizes take the display end of the axis, sub-heads take the text end, and both are named stops in the token set.
8. SOFT is dialed to a moderate value: enough warmth to read human, not enough to read novelty.
9. WONK stays off in trust-critical moments (pricing, security) and on in brand moments (hero, campaign banners); the rule is written into component specs.
10. Numerals and currency are checked in the actual price strings, including the tallest and cheapest amounts in the catalog.
11. Usage rules are recorded: minimum 24px, maximum 10 words, tracking 0 to -0.01em, weights 400 and 600 only, all-caps settings with +0.02em.
12. The runner-up (Space Grotesk) is documented with its rejection reason; it is the first candidate if the brand ever pivots technical.
13. A quarterly display review is scheduled: the five real headlines re-run whenever marketing's vocabulary shifts materially.

The reusable pattern: traits from tone words, real headline vocabulary, smallest-size gate, pairing gate, differentiation gate, then axis discipline.

## Signals to trust

- The face stays legible in your worst environment at your smallest real display size, not the designer's specimen size.
- Kerning holds across your actual headline vocabulary, including the awkward capital pairs your product names create.
- Numerals, currency, and punctuation exist in the weights you ship and match the brand's price strings.
- The pair with the body face passes a squint test: hierarchy reads before any single word does.
- The face has a stable upstream: releases, documentation, and a license that covers display use everywhere you ship.
- Axis behavior is documented with named stops, not left as a free dial every designer tweaks per slide.
- Caps look intentional: all-caps headlines were tested, not just lowercase specimens.
- The face earns its keep in two seconds; a stranger can name the brand's voice from one headline.
- Usage rules exist and are enforced by tokens or linting, so the face cannot drift into small sizes.
- The face's quirk has a purpose you can state in one sentence tied to the brief.
- Optical sizing is real (a genuine opsz axis) or the size range is honestly bounded and documented.
- The display face survived the marketing team's longest real headline without wrapping badly on mobile.
- The face reads at a glance in grayscale; display work gets recolored by campaigns, and contrast must survive flattening.

## Signals to distrust

- Specimen pages: they are art-directed with hand-tuned sizes, colors, and spacing you will not reproduce in product.
- Hero-scale screenshots alone: personality at 120px says nothing about the 28px sub-heads where the face will live most.
- Trend-fit arguments ("it looks like the face that successful brand uses"): it will date you to that brand's cycle.
- "Optical size" claims without a genuine opsz axis; some families only mean "we tightened the spacing".
- Specimens that never show numerals; pricing headlines are where quirks bite hardest.
- Portfolio-only evidence: the face photographed well once, in someone else's brand, at someone else's sizes.
- Download pages without clear licensing; display faces get used in campaigns, and campaign use is where license gaps surface.
- A specimen set entirely in caps when your headlines are sentence case, or the reverse.
- Designer endorsements from teams whose products look nothing like yours.
- "It won an award": juries reward novelty, and novelty is the first thing to age.
- A face whose appeal needs a paragraph of explanation; if the audience cannot feel it, they will not remember it.
- Any sample text you did not write; write your own five headlines and let them argue.
- Pairing screenshots where the display face sits next to a body face it will never touch in your system.

## Cross-references

- [Classification primer](classification-primer.md)
- [Width, density, and spacing](width-density-and-spacing.md)
- [Choosing body typefaces](choosing-body-typefaces.md)
- [Personality and tone](personality-and-tone.md)

Compiled 2025 as part of the Fontlore project.
