# Social Media Graphics

What this reference covers: Typography inside social content: legibility at thumbnail sizes, which fonts you can and cannot control per platform, brand consistency when custom fonts only exist inside images, and the accessibility basics for text-in-graphics. Social type is read while scrolling fast, at sizes nobody chose.

## The thumbnail reality

- Feed images render small and shrink further on mobile: design for the smallest realistic render, roughly 150 to 300 px wide, then verify at that size before shipping.
- One message per graphic: a headline of up to about 6 words at a size that survives the thumbnail; secondary lines belong in the caption, not the image.
- Test procedure: export the graphic, place it in a grid beside competing posts at feed size, and read it from arm's length on a phone. If the headline does not win, increase size or cut words.
- Stroke weight matters more than family choice at these sizes: medium and bold weights with open counters survive; thin, high-contrast display faces turn to lint.
- Contrast over imagery: a scrim, gradient, or solid panel behind text is usually required; busy photos defeat text at any size. The contrast rules from accessibility work apply to graphics too, and platform compression further muddies edge contrast.

## Platform font constraints

- Native text (posts, captions, profiles) uses platform fonts; you do not control them, and "fancy fonts" achieved through Unicode lookalike characters are a trap: screen readers read them as gibberish, search cannot index them, and some codepoints render as tofu on common devices.
- Custom brand typography enters social only inside images and videos: quote cards, banners, story frames, video titles. Plan which strings are baked in and which live in the caption.
- Design tools (Canva, Figma exports, Adobe templates) hold the licensed brand fonts; check that team seats and template use are covered by the license, and that brand kits in those tools point at approved files.
- Video: baked-in titles must respect safe areas (platform UI crops edges) and caption overlays; provide real captions (SRT or platform captioning) rather than relying on burned-in text, which is both an accessibility and a localization failure.
- Platform crops vary per surface (feed, story, profile grid): keep text inside central safe zones and re-check each placement.

## Brand consistency without native control

- Since native text cannot carry the brand face, consistency comes from graphics templates: a small set of layouts with fixed type styles (headline, subhead, CTA) that anyone on the team can apply.
- Template discipline beats font proliferation: one display style, one label style, fixed margins and scrims; a social kit with ten styles produces ten brands.
- The brand type system (see the branding reference) defines which face and weights social graphics use; social is a surface of the brand, not a parallel brand.
- Localization: social graphics get translated; templates must reserve room for German-length strings and check per-script rendering if markets use non-Latin scripts.

## Accessibility basics for text-in-graphics

- Alt text carries the words: if the message is in the image, the alt text must state it (platforms support alt text on images; write it as part of publishing, not as an afterthought).
- Do not bake essential information (dates, prices, accessibility details) solely into imagery; repeat it in the caption text.
- Contrast on graphics follows the same 4.5 to 1 target for body-size text; decorative headline text still deserves real contrast.
- Avoid Unicode lookalike fonts in text entirely; they are an accessibility and search failure in one move.

## Workflow that scales

- Build the social kit as templates with locked type styles and swappable content; export presets handle sizes per platform.
- A two-person rule for quality: creator plus one reviewer checking thumbnail legibility, contrast, safe areas, and alt text before publishing.
- Keep a library of past graphics sorted by performance; the templates that keep winning define the system's evolution, judged by engagement and legibility, not novelty.
- Archive source files with font versions; a campaign refresh a year later should not hunt for which weight was used.

## Common mistakes

- Full sentences inside feed images at sizes that render illegibly; the caption exists, use it.
- Low-contrast text over busy photography with no scrim.
- Unicode "fancy fonts" in captions and bios, breaking screen readers and search.
- Ignoring safe areas, so headlines hide behind platform UI on stories and reels.
- Baked-in text with no alt text, excluding screen reader users from the entire message.
- One-off graphics with ad-hoc fonts, so the brand's social presence drifts from every other surface.
- Forgetting translation overflow: a headline sized for English clips in German or wraps badly in Vietnamese.

## Decision rules

- Every graphic: one primary message, thumbnail-tested, with the words duplicated in caption or alt text.
- Type style: from the brand kit only; new styles require the same approval as any brand surface.
- Text over photos: scrim or panel always; contrast verified at the worst point of the image, not the average.
- Video titles: real caption files plus burned-in titles, sized for the smallest surface the video ships to.
- Any new platform or format: re-run the thumbnail and safe-area checks; crop assumptions do not transfer.

## Comparison table: platform text realities

| Platform | Native text font | Custom brand type | Notes |
| --- | --- | --- | --- |
| Instagram | the platform's own set for captions and stories | images, story templates, reels | keep story text clear of roughly the top and bottom 250 px |
| TikTok | in-app text options only | burned into video frames | use the platform caption tooling for accessibility |
| X | platform font for posts | in images | alt text supported; unicode lookalikes break it |
| LinkedIn | platform font for posts | in images; document posts rasterize your PDF, keeping typography intact | document posts are the one native surface where brand type survives |
| YouTube | platform font for titles and descriptions | thumbnails, end screens, burned-in titles | thumbnail text must survive phone-scale rendering |

- The rule underneath the table: native text is platform typography, and no setting changes it.
- Unicode "fancy fonts" are not fonts; they are lookalike codepoints that screen readers spell out and search cannot index.
- Custom type travels only inside pixels; every graphic or video frame bakes the font in, which is why templates matter more here than anywhere else.
- Design-tool brand kits (Canva teams, Figma libraries) need the same license review as any other deployment; team seats and template use are licensed uses.
- Crops differ per surface: a 1080x1350 design re-cropped to 1080x1920 moves every text block relative to the platform UI.

## Worked example: a developer-tools quote card system

Scenario: a developer-tools company posts three times a week (quote cards, tip graphics, release announcements) produced by one designer and one marketer on an IBM Plex brand system.

- Two templates only: a 1080x1350 quote card and a 1080x1920 story frame, both built in the design tool with locked text styles.
- Quote style: IBM Plex Sans 600 at 56 to 64 px, leading 1.15, maximum twelve words; attribution in IBM Plex Mono 400 at 24 px with the author handle.
- Padding: 96 px all around; text inside a central safe zone that survives both feed and story crops.
- Scrim: a solid brand-color panel behind all text; photography never sits directly under type.
- Thumbnail test: both templates previewed at 200 px wide before publishing; the quote must read at that size or words are cut.
- Alt text: the full quote in the alt field, written at publish time; the caption repeats it as plain text for search.
- Localization reserve: one extra line of vertical room in the quote block; German and Vietnamese translations overflow English in both directions.
- Week-one catch: a 300-weight display variant chosen for style dissolved at feed size after platform compression; the style lock moved to weight 600 permanently.
- Release announcements: the version number in Plex Mono, changelog highlights in the caption, never in the image; the image says the version and the date.
- Carousel option: one idea per card, the same headline style, page numbers in tabular figures; carousels are typography at presentation scale.
- Video tip posts: burned-in titles at 60 px equivalent inside safe areas, plus platform caption files; the burned-in text is decoration, the captions are the content.
- Aftermath: three post types, two templates, zero ad-hoc fonts, and an archive folder that carries source files with font versions noted.

## Field notes

- The scroll is the adversary: a graphic gets a fraction of a second, and the headline either wins at thumbnail size or does not exist.
- Compression is universal; platforms re-encode aggressively, and thin strokes with low-contrast text are the casualties.
- Safe areas are observed crops, not official specs; check each placement because story, feed, and grid crop differently.
- One message per graphic is a typography constraint before it is a marketing rule; thumbnail type cannot carry two ideas.
- Burned-in captions fail accessibility and localization at once; platform caption files exist, so use them.
- Video titles live in a smaller, cropped, moving context; size for the smallest surface the video ships to.
- Unicode lookalikes are the most tempting and most harmful shortcut in social type.
- Profile grids crop to squares on some surfaces; center-critical text stays central.
- Link previews override your typography with the platform's; the card image is the only controllable surface.
- Story text tools change yearly; templates in your design tool outlive platform feature churn.
- Hashtag strings are metadata, not display text; never bake them into graphics.
- Alt text is part of publishing, not an afterthought; it belongs in the checklist step, not the apology.
- Dark mode inverts platform chrome; text near UI elements can lose its assumed contrast.
- Two-person review (creator plus checker) catches thumbnail failures that the creator's full-size screen hides.
- Translated headlines grow or shrink unpredictably; templates reserve room and the review re-runs per market.
- Quote cards with more than about twelve words become articles; cut the quote or make the post a caption.
- Fonts in team design tools drift when one member has a local font the others lack; brand kits point at shared, licensed files.
- The graphics library is a type specimen over time: when a template stops winning, audit its typography before its content.

## Quick reference: social type floors

- One message per graphic; six-word headline target.
- Design for 150 to 300 px rendering; test at that width.
- Weights 500 to 700 over imagery; thin faces turn to lint.
- Scrim or panel behind text, always; contrast checked at the worst point of the image.
- Padding classes around 96 px; story text clear of roughly 250 px top and bottom.
- Alt text carries every word in the image.
- No unicode lookalike fonts, ever.
- Real caption files for video; burned-in text is decoration.
- Templates with locked styles; new styles go through brand review.
- Export presets per platform; no manual re-crops.
- Thumbnail test at 200 px before publishing.
- Translation overflow re-check per market.
- Source files archived with font versions.
- Version numbers and data strings in a mono voice; prose in the brand sans.
- Carousels: one idea per card, consistent headline style, tabular page numbers.
- The caption repeats what the image says; search and screen readers never see pixels.
- Headline weight 600 to 700; medium is the floor, thin is invisible.
- Quote cards cap at about twelve words; longer quotes become carousels or captions.
- Attribution and handles in a distinct style; mono works for technical brands.
- Release and data graphics put numbers in tabular figures even at display sizes.
- The two-person review checks thumbnail legibility, contrast, safe areas, and alt text together.
- Platform-native text never pretends to be brand type; bios and captions stay platform.
- Story frames tested in both feed and story placement before publishing.
- Video titles sized for the smallest target surface first.
- Every template names its fonts and weights in the file description.
- The archive stores the exported file and the source file together.

## Cross-references

- [Branding and logotypes](branding-and-logotypes.md)
- [Contrast and hierarchy](../accessibility/contrast-and-hierarchy.md)
- [Chat and messaging UI](chat-and-messaging-ui.md)
- [Presenting to stakeholders](../workflow/presenting-to-stakeholders.md)

Compiled 2025 as part of the Fontlore project.
