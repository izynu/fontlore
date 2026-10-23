# Presentations and Slides

What this reference covers: Typography for decks: the sizes that work from the back of the room, contrast and weight choices that survive projectors, how font embedding behaves in PowerPoint, Keynote, and Google Slides, and the cross-machine safety practices that stop a deck from reflowing on the venue laptop. Slides are typography at its most constrained: one screen, one shot, unknown hardware.

## Sizes for the room

- Body text: 24 pt minimum on a 16:9 slide; 28 to 32 pt is the comfortable zone. If a slide needs 18 pt, it is a document, and it belongs in a handout.
- Titles: 36 to 54 pt; section dividers larger. Title weight at 600 to 700 with a real bold cut; thin display weights vanish from distance.
- Labels, captions, sources, chart annotations: 14 to 16 pt floor; smaller text is decoration, not information.
- The distance rule: if the back row cannot read it, it is not on the slide; when in doubt, cut words rather than size.
- Line length on slides: 6 to 8 words per line, 3 to 4 lines per block; slides are not paragraphs. Bullets: phrase fragments, parallel structure, no wrapping if avoidable.

## Contrast and projectors

- Projectors wash out: assume the venue device is dimmer, yellower, and blurrier than your laptop. Contrast targets exceed web norms: dark text on light backgrounds or the reverse, never mid-gray on mid-gray.
- Thin weights and light grays fail first on projection; bump weights one step versus print instinct.
- Saturated reds and blues on dark backgrounds vibrate or disappear; test the palette by projecting it, not by looking at a laptop screen.
- High ambient light (daytime, windowed rooms) favors light backgrounds; dark decks look great in a dark room and vanish in a bright one. If the venue is unknown, a light deck is the safer default.
- Rooms with poor color calibration: do not encode meaning in subtle hue shifts; size and weight carry hierarchy (the same rule as the web accessibility work, for the same reasons).

## Embedding and cross-machine safety

- PowerPoint on Windows and macOS can embed fonts (File, Options, Save, Embed fonts in the file). It embeds TrueType-flavored fonts reliably; CFF/PostScript-flavored (most .otf) and variable fonts are historically unreliable or rejected. If the deck must embed, prefer TTF statics.
- Keynote keeps fonts working across Macs with the same fonts installed; for machines without them, export behaviors vary, so treat embedding as unguaranteed and plan accordingly.
- Google Slides renders only the Google Fonts catalog for text (plus uploads as images); custom brand fonts outside that catalog silently fall back. This is the most common "my deck looks wrong" cause in shared-drive workflows.
- The universal safety net: export a PDF with fonts embedded for distribution and for the venue; present from PDF if the machine is unknown. PDF embedding is reliable across engines.
- Bring the font files (with license permitting installation) on the presentation machine or a stick; installing takes a minute and eliminates the fallback lottery.
- Charts and diagrams exported as images from other tools carry their own fonts; flatten them or accept the mismatch.

## Working with brand fonts in decks

- Template, not per-deck choices: the master slides carry the type system (title, body, caption styles), and authors inherit rather than pick.
- Limit the weights shipped in the template to those licensed and needed: a deck template with twelve weights invites twelve.
- If the brand face is commercial, check that the license covers presentation use and installation on employee machines; most desktop licenses do, but per-seat counting matters in enterprises.
- For external decks (sales, conferences), consider a web-safe or system fallback variant of the template for recipients outside the organization.

## Charts, tables, and data slides

- Numbers in charts: tabular figures in axis labels and tables; the same tnum discipline as web dashboards applies.
- Table type: 18 to 20 pt minimum in a slide table; cut rows before cutting size.
- Chart text inherits the template styles in good tools; in tools that default elsewhere (matplotlib exports, spreadsheet charts), restyle before shipping or export as image.

## Common mistakes

- Presenting from Google Slides with a brand font that is not in the Google catalog, then discovering the fallback on the venue screen.
- Thin display weights and gray body text on a dim projector.
- 14 pt body text and a call to action nobody in the room can read.
- Sending a .pptx relying on fonts the recipient does not own, without a PDF fallback.
- One-off decks with hand-picked fonts that never enter the template, so the organization's decks drift apart.
- Embedding variable fonts and hoping; use static TTFs for embedding paths.

## Decision rules

- Unknown venue machine: present from a PDF export, or install the fonts beforehand; never present from an unverified fallback.
- Template fonts: TTF statics for anything that must embed; variable fonts only where the rendering is guaranteed (your own machine).
- New slide size decision: if text drops below 24 pt to fit, the content is wrong for a slide; move it to a handout.
- Dark decks only for controlled dark rooms; light decks as the organizational default.
- Every organizational deck flows from the master template; ad-hoc fonts require the same governance request as any other brand surface.

## Comparison table: where fonts survive

| Surface | Custom fonts render? | Reliability | Practice |
| --- | --- | --- | --- |
| PowerPoint with embedding | TTF statics yes | high for TTF; CFF-flavored .otf and variable fonts historically unreliable | embed before sending the deck |
| Keynote | only if installed | no reliable embedding across machines | install fleet-wide or export PDF |
| Google Slides | Google Fonts catalog only | guaranteed for that catalog; silent fallback otherwise | pick a catalog stand-in or accept images |
| PDF export | yes, embedded subsets | reliable across engines | the venue and distribution safety net |
| Flattened slide images | baked in | total | loses accessibility and editing; for social clips only |

- The failure mode is always silent: the deck opens, the font is missing, and the fallback reflows every carefully fitted line.
- OFL faces solve the license half (install anywhere, embed freely); they do not solve the rendering half, which is format and tool dependent.
- If co-editing happens in Google Slides and the brand face is outside the catalog, choose the stand-in explicitly (Space Grotesk and Manrope are in the catalog) instead of accepting the default fallback.
- Bring font files on a stick plus a PDF; installing two fonts takes a minute and removes the lottery.
- Charts pasted from spreadsheets carry their own fonts; restyle them in the tool or flatten them knowingly.
- The PDF doubles as the handout; design sizes so it reads at 100 percent on a laptop.

## Worked example: a conference deck

Scenario: a design lead presents at a conference on an unknown venue laptop, then distributes the deck to three hundred attendees, using a brand system of Space Grotesk and Inter.

- Template: master slides carry the system; titles in Space Grotesk 700 at 40 to 48 pt, body Inter 400 at 26 to 28 pt, labels and sources Inter 500 at 16 pt.
- Weights shipped in the template: three; a template with twelve weights invites twelve.
- Embedding: static TTF instances installed and embedded through PowerPoint's embed option; variable versions were kept off the deck machine because embedding them is historically unreliable.
  - The static instances were generated once and stored with the template, so every future deck embeds the same builds.
- Fallback: a PDF export with embedded fonts travels with the pptx; the venue plan is to present from the PDF if the preview screen looks wrong.
- Room check: the palette was projected once in a bright room and once in a dark one; 300-weight accents were bumped to 500 after the bright-room test.
- Numbers: chart tables at 18 to 20 pt with tabular figures, axis labels at 16 pt; nothing below 16 pt survives the back row.
- Slide discipline: six to eight words per line, three to four lines per block; if a draft needs 18 pt body text, its content moves to a handout.
- Speaker notes: set in the same template at 12 to 14 pt; notes are documents, not slides.
- Remote delivery: video-call compression eats thin strokes; the same 500-weight bump that survived the projector survived the codec.
- Upload limits: embedding grows files, so the template ships three weights rather than the whole family.
- Rejected: presenting from a borrowed machine with neither fonts installed nor a PDF fallback, thin display weights on an unknown projector, and a 4:3 remix the night before.
- Aftermath: the deck rendered identically on the venue machine and in every attendee's download; the PDF became the canonical handout.

## Field notes

- The venue laptop is a hostile environment: unknown OS, unknown Office version, unknown aspect ratio, and a cable from another decade.
- Projectors wash out contrast and saturate color; the palette must be projected, not admired on a laptop.
- Light decks are the organizational default; dark decks belong to dark rooms and keynote moments.
- Thin weights disappear first, then gray text, then anything under 16 pt.
- Slide masters are governance: authors inherit type styles instead of picking fonts from a dropdown at 11 p.m.
- Hand-picked fonts in one-off decks are how organizations grow five brand voices; the request path exists for a reason.
- Embedded fonts grow files; a deck that exceeds conference upload limits fails before the projector does.
- Embedding licenses: most desktop licenses permit document embedding, but verify the clause for commercial faces.
- If recipients will edit the deck, they need the fonts licensed too; OFL faces make that a non-question.
- Aspect ratio changes reflow everything; fit text only after the final ratio is locked.
- Live captions and translation overlays eat bottom-of-slide space; keep the bottom margin clear.
- Remote presentations compress aggressively; thick strokes and high contrast survive the codec.
- Animated text reveals stress your leading; line-height that works statically can collide mid-animation.
- The back-row test is literal: measure the room or stand at the back before finalizing sizes.
- Print requests always come; a 6-per-page handout style with real 10 pt text beats scaling a slide PDF.
- Kiosk and looping decks run unattended: larger sizes, higher contrast, and no reliance on hover states.
- Font substitution on a client's machine is silent; open the deck on a clean machine before shipping it.
- Decks age into archives; the PDF with embedded fonts is the only version guaranteed to open correctly in five years.

## Quick reference: deck pre-flight

- Body text 24 pt minimum; 28 to 32 pt comfortable; below 24 pt means handout.
- Titles 36 to 54 pt at 600 to 700; thin weights stay off the deck.
- Labels, sources, captions: 14 to 16 pt floor.
- Embed static TTFs in PowerPoint; install fonts locally as a second layer.
- PDF export with embedded fonts travels with the deck, always.
- Fonts plus a license note on the stick.
- Project the palette in a bright room before finalizing.
- Light background as the default; dark decks only for dark rooms.
- Tabular figures in any table or chart numbers.
- Chart text restyled or flattened; library defaults rejected.
- Six to eight words per line; three to four lines per block.
- Bottom margin kept clear for captions and overlays.
- Venue aspect ratio confirmed before fitting text.
- Recipients get fonts or a PDF; never a bare file with private fonts.
- Notes at 12 to 14 pt in the same template.
- Handout style defined once (6 per page, real 10 pt text), not improvised per request.
- Preview screen checked before the audience enters the room.
- Font files installed on the presenting machine even when embedded.
- Charts exported as images keep their fonts; charts kept live get restyled.
- Slide titles and body from master styles only; hand-picked fonts blocked by governance.
- Dark rooms justify dark decks; bright daytime rooms do not.
- 16 pt is the floor for any text meant to be read; smaller is decoration.
- Table rows cut before table text shrinks.
- The PDF handout named and versioned like a release.
- A rehearsal run on the venue hardware (or a stand-in) catches the reflows.

## Cross-references

- [Branding and logotypes](branding-and-logotypes.md)
- [Presenting to stakeholders](../workflow/presenting-to-stakeholders.md)
- [Contrast and hierarchy](../accessibility/contrast-and-hierarchy.md)
- [Dashboards and data-dense UI](dashboards-and-data-dense-ui.md)

Compiled 2025 as part of the Fontlore project.
