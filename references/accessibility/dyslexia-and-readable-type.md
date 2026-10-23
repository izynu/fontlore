# Dyslexia and Readable Type

What this reference covers: What research actually supports about type and dyslexia, why "dyslexia fonts" are a poor centerpiece, and the spacing, structure, and user-control practices that reliably help. Written to prevent teams from shipping gimmicks while genuinely improving reading comfort.

## What the evidence says

Peer-reviewed studies comparing "dyslexia-specific" fonts (OpenDyslexic and similar) with common standard fonts have repeatedly failed to find reliable reading benefits for the specialized fonts; some studies found no significant differences, others found slight advantages for ordinary sans serifs. The honest summary: there is no solid evidence that any particular typeface fixes dyslexia-related reading difficulty, and claims that one does should be treated as marketing.

What does help, per the research and practitioner guidance:

- Larger text and more line spacing: consistently reported as helpful by readers with dyslexia.
- Letter and word spacing: modest increases can improve word recognition; this is why WCAG 1.4.12's overridable spacing matters so much here.
- Shorter line lengths and left-aligned text: reduces place-loss and overshoot on return sweeps.
- Avoiding justified text: uneven word spacing creates rivers that disrupt tracking.
- Clear structure: headings, lists, and short paragraphs reduce cognitive load more than any glyph change.
- Consistent, familiar letterforms: highly stylized or experimental faces add decoding work.

The British Dyslexia Association's style guidance reflects this: clear sans serifs, generous spacing, left alignment, and good structure, rather than any proprietary font.

## Designing without gimmicks

- Offer control rather than prescription: a reading settings control (text size, spacing, sometimes theme) serves dyslexic readers better than baking one "helpful" style into the design, because needs vary per person and per context.
- Never claim a font is dyslexia-friendly in product copy unless you can cite evidence; the claim is checkable and currently unsupported for the commercial "dyslexia fonts".
- Do not encode assumptions in the type system (forced large spacing site-wide); instead make defaults sensible and overrides available.
- Beware accessibility theater: swapping in a special font while shipping justified 110-character lines with 1.3 leading is a net negative.

## Type choices that are genuinely defensible

Given no magic font exists, choose on the factors with real support:

- Familiar, open sans serifs for reading-heavy UIs: Inter, Source Sans 3, Verdana-lineage designs; nothing exotic required.
- Good lowercase differentiation and open apertures; test the face at your actual sizes.
- Real bold for emphasis rather than color alone or underlining (underline is reserved for links).
- Line length 45 to 75 characters, line-height around 1.5, left-aligned ragged right.
- If body text is serif, a sturdy text serif (Source Serif 4, Literata, PT Serif) rather than a high-contrast display serif.
- A face with real weights rather than a two-weight family; emphasis built from genuine 600 beats synthetic bold, which blurs at exactly the sizes dyslexic readers use most.

## Beyond type: structure carries the load

Dyslexia-friendly reading is mostly an information-architecture practice:

- Front-load meaning in headings and first sentences.
- Break long content with subheadings every few paragraphs.
- Use lists over dense prose when enumerating.
- Keep link text meaningful out of context ("read the pricing guide", not "click here").
- Provide text alternatives and consistent navigation so re-reading is cheap.

## Common mistakes

- Shipping a "dyslexia mode" that just switches the font and nothing else; spacing, size, and structure are the levers with evidence.
- Believing the font vendor's study; most are internal, uncontrolled, and unpublished.
- Forcing a special font on everyone; some readers find the letterforms harder, and the claim alienates the audience it names.
- Justified text with large word gaps on content pages.
- Ignoring the spacing overrides criterion; dyslexic readers are among the primary users of such overrides.
- Treating dyslexia as a niche: it is common (estimates around 5 to 10 percent of people, with wider reading-difficulty ranges), so these practices are mainstream usability, not edge-case accommodation.
- Measuring success by shipping the panel; measure by whether readers change settings and finish long pages, then iterate.
- Applying the reading recipe to interface chrome; buttons, navigation, and forms follow UI rules, not reading rules.

## Decision rules

- Request for "a dyslexia font": respond with a reading-settings proposal (size, spacing, measure) and cite the evidence gap; do not buy a specialist font on that basis.
- Default type for a content product: a clear, familiar sans or sturdy text serif at 16 px or more, 1.5 leading, 45 to 75 character measure, left-aligned.
- Any accessibility claim in marketing about type: must trace to a citable source or be removed.
- Evaluating a proposal that cites a specialist font's benefits: ask for peer-reviewed evidence; absent that, redirect the effort to spacing and structure work.
- Everything user-facing: pass the text-spacing override test, because that is the accommodation this audience actually uses.
- When any accessibility claim about type is proposed: write the source next to the claim in the design system docs; an unsourced claim is removed, not softened.

## Comparison table: claims versus evidence

| Intervention | State of the evidence | Practical verdict |
| --- | --- | --- |
| Specialist dyslexia fonts | Peer-reviewed comparisons find no reliable benefit over well-set standard faces | Do not build a product claim on one |
| Larger default text | Consistently reported as helpful by readers | Ship 17 to 18 px on reading surfaces |
| Increased letter and word spacing | Modest support; needs vary per reader | Offer as a user control |
| Line height 1.5 or above | Supported | Default 1.5 to 1.8 for body text |
| Left-aligned, ragged right | Supported | Always for reading text |
| Justified text | Creates rivers and uneven word spacing | Avoid on reading surfaces |
| Tinted backgrounds and overlays | Mixed and highly individual | Optional theme at most, never the default |
| Familiar letterforms | Reported as reducing decoding effort | Prefer proven, open faces |

The pattern is consistent: the interventions with evidence are spacing, size, and structure, which are layout and control decisions. The typeface is a supporting actor.

## Field notes: building a reading-settings panel

The control that serves dyslexic readers is a small panel on reading surfaces (articles, docs, lessons), not a site-wide theme switch:

- Text size: three steps mapping to 100, 112.5, and 125 percent on the root, implemented in rem so browser preferences still compose with it.
- Line spacing: three steps, 1.5, 1.75, and 2, scoped to article containers, not to buttons and navigation.
- Letter and word spacing: one toggle applying a gentle increase (for example 0.015em letter and 0.06em word spacing), never the 1.4.12 stress values, which exist for override testing, not default design.
- Face: the default plus one alternative, offered without claims; Atkinson Hyperlegible is a defensible alternative because its design goals are documented for low vision, and Lexend exists for readers who prefer its spacing-tuned forms.
- Persistence: the choice stored with the user or locally and applied before first paint, so there is no flash of default text.
- Do not: swap fonts automatically based on a dyslexia assumption, force the settings on, or label the panel "dyslexia mode".
- Respect prefers-contrast and forced-colors in the same panel so high-contrast needs are met without JavaScript guesswork.

## Code notes: the reading-surface recipe

```css
/* Reading surfaces: the defaults that follow from the evidence */
article {
  font-size: 1.125rem;      /* 18 px, respects the user's rem base */
  line-height: 1.7;
  max-width: 64ch;
  text-align: left;         /* ragged right; no justification */
  letter-spacing: normal;   /* never tracked body text */
}
article p { margin-block: 0 1em; }    /* visible paragraph separation */
article strong { font-weight: 600; }  /* real semibold, not color emphasis */
```

The same values ship as design tokens (a reading-size, a reading-leading, a reading-measure) so product and marketing surfaces inherit them instead of re-deciding per page.

## Worked example: answering the "dyslexia font" request

A product manager forwards a vendor email: a specialist font, licensed per seat, "clinically shown to help dyslexic readers". A defensible response, written once and reused:

1. Ask for the peer-reviewed evidence behind the claim; the studies that exist are typically internal and uncontrolled.
2. Present the evidence summary from this reference: no reliable advantage for specialist fonts over well-set standard faces.
3. Offer the alternative plan: reading-settings panel, 17 to 18 px body, 1.5 to 1.8 leading, structured content, text-spacing override support.
4. Cost it against the font license; the settings panel is usually cheaper and helps every reader, not only the diagnosed ones.
5. If the organization still wants the font, offer it as an optional user choice inside the panel, with no claims attached, and record the decision.

The outcome that matters: the reader gets knobs that help, the company avoids an unsupported marketing claim, and the money buys structure instead of a ligature.

## Quick reference: numbers for reading surfaces

The defaults below summarize the evidence and guidance cited above; the WCAG column is the override test the page must survive, not a recommended default:

| Setting | Default to ship | Override test it must survive |
| --- | --- | --- |
| Body size | 1.0625rem to 1.125rem (17 to 18 px) on reading surfaces; 1rem floor elsewhere | User raises the browser base font size well above default |
| Line height | 1.5 to 1.8 for body text | 1.4.12 line-height at 1.5x font size |
| Paragraph spacing | Visible margin of 0.5em to 1em between paragraphs | 1.4.12 paragraph spacing at 2x font size |
| Letter spacing | normal for body | 1.4.12 letter spacing at 0.12x font size |
| Word spacing | normal | 1.4.12 word spacing at 0.16x font size |
| Measure | 45 to 75 characters | Reflow at 320 px width keeps text intact |
| Alignment | Left, ragged right; never justified | Not applicable |
| Emphasis | Real 600 weight from the font files | Forced-colors mode remaps colors without breaking meaning |

The distinction matters: shipping 0.12x letter spacing everywhere because the criterion tests for it confuses the accommodation (users may override) with the default (keep it normal; readers who want it will set it, which is why the criterion exists).

## Audit checklist: reading surfaces

- [ ] Body text at or above 1rem, 1.5 leading or more, 45 to 75 character measure.
- [ ] Left-aligned; text-align: justify absent from article and long-form containers.
- [ ] Paragraph separation visible without relying on spacing alone.
- [ ] Emphasis uses real bold (600 or 700) from the font files, not synthetic bold and not color alone.
- [ ] Links distinguishable without color (underline or weight) and nothing else is underline-decorated.
- [ ] Headings break up long content every few paragraphs; heading levels nest without skips.
- [ ] The 1.4.12 override sweep passes on every reading template, screenshots filed.
- [ ] Any reading-settings panel offers size and spacing as user choices, persists them, and applies before first paint.
- [ ] No product or marketing copy claims a typeface is "dyslexia-friendly" without a citable source.
- [ ] Enumerations use lists; link text is meaningful out of context.

## Cross-references

- [WCAG baseline for type](wcag-baseline-for-type.md)
- [Text spacing criterion](text-spacing-criterion.md)
- [Line length and reading](line-length-and-reading.md)
- [Common mistakes](../workflow/common-mistakes.md)

Compiled 2025 as part of the Fontlore project.
