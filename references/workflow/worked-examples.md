# Worked Examples

What this reference covers: Four complete font-selection walks using the Fontlore workflow end to end: a B2B SaaS dashboard, an editorial long-read magazine, a bilingual Hindi-English government service site, and an artisan bakery brand identity. Each walk shows the brief, the derived constraints, the hard filters, the shortlist with rejection reasons, the final pick with pairing, the license check, and the implementation notes.

Every example follows the same spine: constraints before fonts, hard filters before taste, verification before commitment. Read them as decision records; the goal is not to copy the picks but to copy the reasoning, which is reusable when your brief differs.

## Example 1: B2B SaaS dashboard with dense tables

The brief: an analytics dashboard for a 14-person team, tables everywhere, IDs and currency values, one frontend, no budget approved for fonts.

Constraints derived from the brief:

- Latin only at launch, with no near-term markets on the roadmap.
- Web only; no app, no print, no email embedding in scope.
- Zero budget, so open licenses only.
- Long sessions reading small dense text, so small-size legibility matters more than display character.
- Heavy numeral use requiring column alignment, which means real tabular figures.
- Dark and light themes both required.

Hard filters applied:

- License must be OFL or Apache.
- Tabular numerals (the tnum feature) must exist in the actual file, not the catalog copy.
- At least regular, medium, and semibold weights; variable preferred.
- Proven verifiable upstream source.

Shortlist with rejections:

- Inter: kept. Strong tabular numerals, variable, excellent small-size legibility, permissive license.
- IBM Plex Sans: kept. True tabular figures, neutral-but-distinct voice, deep weight range.
- Source Sans 3: kept. Solid tables and a humanist voice, slightly warmer than the brief asked for.
- SF Pro: rejected. Apple's system font; not licensed for self-hosting on arbitrary web products.
- Roboto: rejected. Reliable but visually defaults the product; the brief asked for a considered identity.
- Lato: rejected. Tabular-numeral support is missing, which fails a hard filter for this brief.

Final pick and pairing: Inter for all UI and table text (400, 500, 600) plus JetBrains Mono for IDs, codes, and raw values.

- The mono face doubles as a data-integrity signal: monospace means "copy this value".
- Weights beyond semibold were deliberately left out of scope to keep the payload small.

License check result: Inter is SIL OFL 1.1 in its upstream repository; JetBrains Mono is OFL 1.1. Bundling and self-hosting permitted, no pageview tiers, license texts stored with the files per the due-diligence reference.

Implementation notes:

- font-variant-numeric: tabular-nums on every table and metric, set once in the tokens.
- 13-14px base for dense tables at 1.3-1.4 line-height; larger for narrative panels.
- Load via pinned Fontsource variable packages; latin subset only.
- Test with real data: negative currency, long IDs, localized decimal separators.

## Example 2: Editorial long-read magazine site

The brief: a weekly long-form publication, 4,000-word features, strong brand personality, an advertising-free reading experience.

Constraints derived from the brief:

- Latin plus Vietnamese on the 12-month roadmap; both must work day one or be a documented, planned addition.
- Web and static page surfaces only.
- Small budget, with one paid family allowed if justified.
- Display and body roles with distinct voices; italics essential for editorial tone.
- Reading comfort at 1,000-word stretches is the success metric.

Hard filters applied:

- Full Vietnamese coverage in every shipped file, verified in the files, not just the catalog claim.
- True italics, not sloped romans.
- Optical sizing or a proven display-to-text range.
- License compatible with a reader-funded site.

Shortlist with rejections:

- Fraunces: kept for display. Variable with opsz, SOFT, and WONK axes; wonky warmth at display sizes.
- Newsreader: kept for text. Designed for long-form reading with a real optical-size axis and true italics.
- Source Serif 4: kept as the alternative body face; variable, opsz, Vietnamese support.
- Playfair Display: rejected. Overused for premium-editorial, and its high-contrast didone strokes fatigue at long-read text sizes.
- PT Serif: rejected. Static files only; no optical sizing and a weaker Vietnamese story.
- Lora: rejected as primary for being the category's safe default; kept as a fallback reading face.

Final pick and pairing: Fraunces for headlines and pull quotes; Newsreader for body text and captions.

- The two faces share editorial temperament (warm, slightly old-style) while occupying clearly separated roles.
- This is the one-voice-per-role discipline: display sings, text disappears.

License check result: both families are SIL OFL 1.1 in the google/fonts repository; italics and all axes verified in the actual files rather than catalog copy; the evidence chain is recorded in the manifest.

Implementation notes:

- font-optical-sizing: auto, so opsz follows the rendered size.
- Fraunces at SOFT 0 and WONK 0 for restraint; WONK 1 reserved for section openers.
- Body at 1.125-1.25rem, 1.6 line-height, 60-70ch measure.
- Vietnamese strings reviewed by a native reader before launch; latin and vietnamese subsets both shipped.

## Example 3: Hindi and English bilingual government service site

The brief: a public services portal, Hindi and English of equal importance, a huge audience on low-end Android devices, procurement that requires open-source fonts only.

Constraints derived from the brief:

- Devanagari plus Latin with equal first-class treatment; neither script is a fallback.
- OFL-only, stated as a procurement requirement, so license class is a hard filter.
- Web on slow networks; payload discipline matters.
- Accessibility commitments including the text-spacing criterion.
- A strictly neutral voice, appropriate for government.

Hard filters applied:

- OFL-1.1 exactly, per procurement.
- Full Devanagari conjunct coverage verified in the files.
- At least 400, 500, 600, and 700 weights.
- A single-family or matched-family system, so Hindi and English pages share one voice.

Shortlist with rejections:

- IBM Plex Sans Devanagari plus IBM Plex Sans: kept. A matched family system, consistent weights, designed together for co-rendering.
- Noto Sans Devanagari plus Noto Sans: kept. Maximum coverage and long-term maintenance, deliberately neutral voice.
- Mukta: kept. A lighter single-family alternative covering Devanagari and Latin.
- Baloo 2: rejected for the core system; its rounded warmth fights the neutrality requirement, noted as the choice for public campaign pages.
- Mangal and Nirmala UI: rejected. Proprietary Windows system fonts; no redistribution rights.
- Kohinoor Devanagari: rejected. Commercial family, incompatible with the procurement constraint.

Final pick and pairing: IBM Plex Sans Devanagari for Hindi text, IBM Plex Sans for Latin, with Noto Sans Devanagari as the declared fallback in the stack.

- One foundry system keeps Hindi and English feeling like one product.
- The fallback is named in the stack and in the register, so it is a decision, not an accident.

License check result: IBM Plex families are SIL OFL 1.1; Noto Sans Devanagari current releases are OFL 1.1, while early Noto releases were Apache-2.0, so the deployed version is pinned and recorded per the due-diligence reference.

Implementation notes:

- html lang set per page so the correct family leads the stack.
- Devanagari line-height at 1.6 or taller to clear matras above and below the shirorekha.
- unicode-range subsetting so English-only pages never download the Devanagari file.
- Test strings covering conjuncts, nukta forms, and candrabindu, reviewed with native readers.
- WCAG 1.4.12 text-spacing verified, because Devanagari tolerates forced spacing worse than Latin.
- Low-end device testing under throttled network conditions.

## Example 4: Artisan bakery brand identity

The brief: a neighborhood bakery with a new brand, packaging and shelf presence, menus, a small website, essentially no font budget, and a personality that should read handmade rather than corporate.

Constraints derived from the brief:

- Print packaging and web both in scope, with packaging as the technically harder surface.
- Zero budget, stated firmly.
- Warm, slightly nostalgic personality.
- Ingredient labels need tiny-size legibility and legal clarity.
- Final artwork goes to a print vendor as PDF.

Hard filters applied:

- OFL only, for the simplest license story on a brand asset that will live for a decade.
- A display face with genuine character, not just "a serif".
- A durable workhorse for labels and body.
- Files verified at upstream sources before adoption.

Shortlist with rejections:

- Yeseva One: kept. High-personality display serif, one weight, warm rather than corporate.
- Karla: kept for labels, menus, and web body. Variable weight axis, sturdy at small sizes, quirky without whimsy.
- DM Serif Display: kept as the alternative display; more conventional, safer if the client balks at Yeseva One's character.
- Abril Fatface: rejected. Poster-didone drama competes with product photography on packaging.
- Lobster and Pacifico: rejected. Script defaults with dated, template-era associations.
- Recoleta: rejected. Commercial, and the zero-budget constraint is real; recorded as the paid upgrade path if the brand grows.
- Clash Display: rejected. Reads contemporary-tech, the wrong temperature for a bakery.

Final pick and pairing: Yeseva One for the wordmark support, packaging headlines, and hero moments; Karla for ingredient labels, menus, and all web text.

- One loud voice, one reliable voice, no third opinion.
- The single weight of Yeseva One is treated as a feature: it forces restraint.

License check result: both families are SIL OFL 1.1 on Google Fonts, verified in the google/fonts repository with license copies stored in the brand asset folder; packaging embedding is permitted by the OFL.

Implementation notes:

- Display used only where it can breathe; never below 20px equivalents.
- Ingredient labels and legal text always Karla, at 6-8pt on packaging, tested on actual print proofs.
- Final print artwork outlined at handoff, which the OFL permits, while the editable source keeps live fonts.
- Shelf test at one and two meters before approval.
- Web uses the same two families so the site and the shelf match.

## Patterns across the examples

- Constraints killed more candidates than taste did; in all four walks the hard filters removed roughly half the shortlist before aesthetics were discussed.
- Pairings worked when the two faces shared temperament but not role; matching role is what produces the two-display-faces problem.
- The license check was never a formality: example 3 changed the font choice entirely, and example 4 recorded an upgrade path instead of pirating convenience.
- Every pick named its fallback and its substitution plan; fonts are living dependencies, not one-time decisions.

## Decision rules

- If the constraint sheet would have rejected the pick, the pick is wrong, however good it looks in a specimen.
- A pairing needs a reason to exist; if either face could be swapped without the design changing, the pairing is decorative.
- Zero-budget briefs get the best OFL faces and a documented commercial upgrade path, never a trial font in production.
- Bilingual systems are picked as systems; evaluating the Latin face alone fails the brief.

## Cross-references

- [Brief to constraints](brief-to-constraints.md)
- [Research workflow](research-workflow.md)
- [Testing and comparing shortlists](testing-and-comparing-shortlists.md)
- [Scoring and shortlisting](../selection/scoring-and-shortlisting.md)

Compiled 2025 as part of the Fontlore project.
