# Common Font Selection Mistakes

What this reference covers: The twelve mistakes that most often derail font selection, each with its symptom, the reason it keeps happening, and the concrete fix. Written as a pre-mortem: read it before a selection project starts, not after one of these has already happened to you.

The same twelve failures recur across teams of every size because each one is a reasonable-looking shortcut in the moment. Knowing the failure shape is usually enough to avoid it; each fix points at the reference that goes deeper.

## The twelve mistakes

### 1. Choosing on the catalog preview alone

- Symptom: a face that looked stunning on its specimen page produces cramped, dull, or broken text in the actual product.
- Why it happens: previews are set in ideal copy at flattering sizes with tuned spacing; they are advertisements, not evidence. After an hour of browsing, the prettiest specimen wins instead of the best fit.
- Fix: test every shortlisted face with your real copy at your real sizes; the testing-and-comparing reference is the method. No pick is final until it has rendered your strings.
- Watch for: the pick being defended with the specimen again. If the argument restarts from the catalog, the test never happened.

### 2. Ignoring license scope until launch

- Symptom: legal review blocks the launch, emergency purchases happen at list price, or a face gets pulled two days before release.
- Why it happens: licensing feels like paperwork, and all the momentum belongs to the aesthetics conversation.
- Fix: license scope is a hard constraint on the sheet from day one. The brief-to-constraints reference makes it non-negotiable, and the licensing FAQ answers the questions teams tend to defer.
- Watch for: "we will sort licensing at the end" said by the most senior person in the room. That is the moment to put the constraint on the sheet.

### 3. Pairing two display faces

- Symptom: every headline competes with every other headline, the page reads as shouting, and hierarchy collapses.
- Why it happens: both faces were chosen at specimen size, where display faces shine, and the body role was never assigned a voice of its own.
- Fix: one display voice, one or more text voices. Pair display with a face designed for reading at size, and check the pairing at both extremes of the size range before committing.
- Watch for: a second display face added for "campaign moments"; campaigns inherit the primary system or the system fragments.

### 4. Using too many weights

- Symptom: eight font files in the payload, a hierarchy nobody can explain, and faux-bold artifacts where a requested weight was never actually loaded.
- Why it happens: "more options" thinking during selection, then nobody prunes because every weight has one defender.
- Fix: three to four weights maximum, each mapped to a named role in the token system. The design-tokens reference turns the weight list into an enforceable contract.
- Watch for: a weight used exactly once, in one component; that weight is a candidate for removal, not for retention.

### 5. Defaulting to the same overused family for everything

- Symptom: the product, the docs, the marketing site, and the pitch deck all use the same default UI sans, and nothing signals intent anywhere.
- Why it happens: familiarity reads as safety, and the default is never actually chosen, just inherited from the boilerplate.
- Fix: make the default a decision with written rationale. Run a deliberate personality pass once, so inheritance becomes a choice that can be defended in a review.
- Watch for: the rationale being "everyone else uses it"; that is the mistake wearing a different hat.

### 6. Ignoring script coverage for internationalization

- Symptom: Vietnamese diacritics render from a fallback face, Devanagari conjuncts break, or the localized site silently looks nothing like the flagship.
- Why it happens: the team tests in English and treats other scripts as a later problem, usually until localization week.
- Fix: list exact languages on the constraint sheet, verify coverage in the actual files because catalog labels lie by omission, and test with native strings and native readers.
- Watch for: coverage claims made about the family while the deployed file is a subset; the file, not the family, is what renders.

### 7. Trusting identification tools without verification

- Symptom: the team buys or adopts what a tool named, and it turns out to be a sibling weight, a revival, or a lookalike clone.
- Why it happens: tools return confident single answers, and confidence feels like correctness when a deadline is near.
- Fix: verify letterform by letterform against primary sources before acting on any match. The documenting-identification reference defines the verification bar a match must clear.
- Watch for: purchasing a license for the wrong family entirely; the receipt is then evidence of the mistake, not of the right.

### 8. Shipping 400px of webfonts for one headline

- Symptom: a page whose text payload rivals its images, slow first paint, and visible layout shift as late fonts swap in.
- Why it happens: full-family downloads "just in case", no subsetting, and no budget anyone enforces.
- Fix: subset, ship woff2, limit weights, use unicode-range, and hold a font weight budget per page. The subsetting and font-loading references carry the numbers and the pipeline.
- Watch for: the italic style loaded on every page while one page uses it once; italics are the most common stowaway.

### 9. Hard-coding px sizes

- Symptom: text ignores user font-size preferences, browser zoom enlarges everything except the type, and WCAG 1.4.4 checks fail.
- Why it happens: design tools export px, px feels precise, and the tokens were never connected to the components.
- Fix: rem-based size tokens everywhere, with px reserved for hairlines and media. The design-tokens reference shows the scale and the migration path.
- Watch for: rem values computed against a hand-tuned root font-size hack; the token system should survive a default browser, not fight it.

### 10. Mixing metrics-incompatible fallbacks

- Symptom: every load reflows the page as the webfont swaps in, with cumulative layout shift concentrated on the most-viewed pages.
- Why it happens: the fallback stack was whatever the boilerplate had, chosen before the primary face existed and never revisited.
- Fix: choose fallbacks deliberately, tune them with size-adjust, ascent-override, and descent-override, and measure the swap. The fallback-metrics reference has the technique and the tooling.
- Watch for: local testing hiding the problem because the primary font is installed on every machine in the studio.

### 11. Treating popularity as quality

- Symptom: shortlists collapse into the same three fashionable families regardless of brief, or a genuinely fitting but less-hyped face is dismissed because "nobody uses it".
- Why it happens: popularity is a real signal of safety, so it substitutes for analysis whenever analysis feels expensive.
- Fix: score candidates against your constraints, not against rankings. The scoring-and-shortlisting reference exists to keep popularity in its lane as one input among several.
- Watch for: popularity arguments arriving as "proven in production" without a single context resembling yours.

### 12. Not testing with real copy at real sizes

- Symptom: launch-week surprises, orphaned headlines, numerals that wobble in tables, and a body size that read fine in the mockup and fails in the product.
- Why it happens: lorem ipsum is always available and always misleading; placeholder copy has no edge cases, no proper nouns, and no real length.
- Fix: assemble a standard test-copy set early, including product strings, worst-case labels, and accented or non-Latin samples, and render every shortlisted face against it before deciding.
- Watch for: testing only headlines. Body sizes, table numerals, and button labels are where real products spend their time.

## Triage: from symptom to mistake

When a problem has already appeared, this table routes it back to the mistake above:

- Text looks worse in the product than in the pitch: mistakes 1 and 12.
- Legal blocked the launch: mistake 2, and read the license-audit-checklist reference next.
- The page is loud and unreadable: mistakes 3 and 4.
- Localized pages look broken or foreign: mistake 6.
- Slow text rendering or layout shift: mistakes 8 and 10.
- Type ignores accessibility settings: mistake 9, verified against the wcag-baseline reference.
- Every option discussed is one of the same three famous families: mistake 11.

## Pre-flight checklist

Run this ten-point check before any selection project starts; each item maps to a mistake above.

1. The constraint sheet exists and includes license scope, exact languages, and surfaces.
2. Every shortlisted face has a verified upstream source and a readable license file.
3. Test copy is real: product strings, worst-case labels, non-Latin samples.
4. Testing happens at the real sizes the tokens define, on real devices.
5. One display voice and at least one text voice are planned, not improvised.
6. The weight list is capped and each weight maps to a role.
7. The fallback stack is chosen after the primary face, and metrics were checked.
8. A font weight budget exists for the page.
9. Sizes are rem-based tokens, and components consume only semantic tokens.
10. Someone owns the decision record: manifest entry, license evidence, rationale.

Ten minutes with this list prevents the majority of launch-week font emergencies.

## Patterns worth noticing

- Eight of the twelve are process failures, not taste failures: the fix is a constraint, a checklist, or a review, not a better eye.
- Most mistakes are cheaper to prevent than to detect: a test copy costs an afternoon; launch-week rework costs weeks.
- The recurring root cause is testing with materials that are not yours: catalog previews, placeholder copy, boilerplate fallbacks, popularity charts.
- Mistakes compound: hard-coded px plus metrics-incompatible fallbacks produces a slow, shifty, inaccessible page where no single decision looks fatal.
- The mistakes recur because each one is invisible in the moment it is made; the pre-flight list exists to make them visible while they are still cheap.

## Decision rules

- A candidate that has not rendered your real copy is not a candidate; it is a bookmark.
- Any font decision that cannot cite the constraint it serves gets deferred until it can.
- If two mistakes are about to interact, fix the process before fixing either symptom; interaction bugs come back.
- When a mistake has already happened, write down which one it was and add its check to the next selection project; the list above is the starting corpus, not the final one.

## Cross-references

- [Brief to constraints](brief-to-constraints.md)
- [Testing and comparing shortlists](testing-and-comparing-shortlists.md)
- [Font-face and CSS](../technical/font-face-and-css.md)
- [WCAG baseline for type](../accessibility/wcag-baseline-for-type.md)

Compiled 2025 as part of the Fontlore project.
