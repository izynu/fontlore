# Brief to Constraints

What this reference covers: Translating a project brief into hard typographic constraints before any font is looked at: license scope, scripts and languages, media and embedding needs, size budgets, and schedule. Constraint-first selection prevents the most expensive failure in font work: falling in love with a face that cannot legally or technically ship.

## Why constraints come first

Font selection fails backwards: someone sees a beautiful face, proposes it, and the project then discovers it lacks Vietnamese, cannot be embedded in the app, or costs more than the engagement. Constraint-first inverts the order: define the envelope, then search inside it. A face that fails a hard constraint is out regardless of beauty; this is what makes the shortlisting phase fast and defensible.

## Extracting the constraints

Interrogate the brief (and the stakeholders) for each of these, and write the answers down:

- Scripts and languages: what must render on day one, and what is on the 12-month roadmap? "English only" usually means "English and whatever the next market is"; check the product's actual user data, support tickets, and expansion plans. List exact languages, not scripts ("German, Polish, Vietnamese", not "Latin").
- Media and surfaces: web (which browsers?), native apps (iOS, Android, desktop?), email, print, packaging, presentations, documents? Each surface carries different format and license needs. Embedded use in apps and devices is a distinct licensing category from web and desktop.
- License scope: how many seats for desktop use, which products embed fonts, is the product open source, are vendors and agencies involved, is the company in a regulated industry where provenance matters?
- Size and performance budgets: page-weight limits, performance budgets already agreed, whether CJK or other heavy scripts are in scope.
- Brand constraints: existing brand guidelines, mandated families, a parent brand system, accessibility requirements already committed.
- Budget: zero (open fonts only), modest (one commercial family), or open (full foundry range)? Budget is a constraint, not a preference; state it numerically if possible.
- Timeline: trial licenses have terms; variable font subsetting takes tooling work; script-specific QA (Arabic, Devanagari) takes real time with real readers.

## The constraint sheet

Write a one-page constraint sheet with these fields, and treat it as the input to every later decision:

- Languages required at launch and planned: exact list.
- Surfaces: web, app, email, print, other; with the technically hardest surface named.
- License musts: seat count, embedding rights, vendor/redistribution needs, open-source requirements.
- Performance: max total font weight per page, per-file limits.
- Accessibility commitments: minimum sizes, contrast regime, any WCAG conformance target.
- Brand: must-keep, must-avoid, existing assets.
- Budget and timeline: numbers and dates.
- Open questions: anything the brief does not answer, with an owner per question.

Circulate it for sign-off. The constraint sheet is what turns later taste debates into rule-checking: every candidate either fits the sheet or is rejected with a citation.

## Red flags in briefs

- "Make it look premium" with no budget line: premium usually means commercial licensing; surface the conflict now.
- "All languages" with no list: nobody means all; force the actual list and a phase two list.
- "Same font everywhere" including a native app with embedding rights and an email campaign: these surfaces have different technical ceilings; negotiate the system, not the slogan.
- A design already approved from a specimen: ask whether the approval survives the constraint sheet; if not, restart the conversation with the sheet.
- Silence on accessibility: add the minimum sizes and contrast regime yourself; they constrain the type system more than aesthetics do.

## Common mistakes

- Starting from inspiration (dribbble shots, font aggregator homepages) and working backwards to justify it.
- Treating the roadmap's "maybe Vietnamese" as ignorable, then migrating the entire type system in six months.
- Forgetting surfaces that embed fonts: the mobile app, the PDF reports, the e-reader export; each is a license line item.
- Writing constraints as preferences ("would prefer open source") instead of hard lines; preferences lose to beauty, constraints do not.
- Not signing off the sheet: constraints nobody agreed to get renegotiated the week before launch.

## Decision rules

- Any hard constraint discovered after shortlisting starts: stop, update the sheet, re-derive the shortlist; sunk-cost shortlists are how bad fonts ship.
- Two constraints conflict (all scripts, zero budget): resolve explicitly with the stakeholder, in writing, before searching.
- The hardest surface defines the search: if an embedded device needs specific formats, that rules before the website does.
- Constraint sheet version-controlled with the project: decisions get audited against the version that existed when they were made.

## Worked example: constraint sheet for a multilingual SaaS

A B2B product (dashboard plus marketing site) writing its sheet before any font search:

- Languages at launch: English, German, Polish. Phase 2 within 12 months: Vietnamese, then Arabic. Arabic is flagged now because it changes the whole system decision (dir support, a real Arabic family, bidi QA) even though it ships later.
- Surfaces: web app, marketing site, transactional email (system stacks only, so not a font constraint), and PDF exports generated server-side. The PDF generator is named as the hardest surface: server-side rendering carries its own licensing category, so open-source-only is provisionally selected.
- License musts: unlimited seats preferred to avoid per-seat accounting; app embedding not needed this year; the product is closed source, but bundled fonts still ship with their license texts.
- Accessibility commitments: WCAG 2.2 AA targeted; body floor 1rem; contrast pairs at 4.5:1 (3:1 for large text); the 1.4.12 spacing overrides must not break layouts, which rules out fixed-height text containers as a pattern.
- Performance: 120 KB total font payload per page on the app; variable fonts preferred to hold weight ranges in one file per family.
- Brand: no mandated family; the incumbent is Inter and the brief asks for more personality in display while keeping body neutral.
- Budget and timeline: zero license spend for phase 1 (open fonts), commercial allowed for phase 2 Arabic if justified; launch inside one quarter, so no custom work.
- Open questions: who owns the Arabic decision (assigned to the design lead with localization), and whether the PDF generator can embed variable fonts (assigned to engineering).
- Stakeholders and owners: the decision owner named (design lead), with engineering and content signed on as reviewers of the sheet rather than recipients.
- Success criteria: what "better" means measurably (legibility at production sizes, coverage across the language list, payload inside budget), written before any specimen is seen.
- Reuse: the sheet feeds the design-system documentation and becomes the intake template for the next project.
- Review cadence: the sheet is re-read at each phase gate, not only at kickoff; constraints drift as the product learns.
- Sign-off note: one revision was made (the payload budget dropped from 150 to 120 KB after the performance audit) and the revision stayed part of the record; a sheet that never changed was probably never read.

The sheet took one meeting plus forty minutes of writing. It eliminated three popular candidates before the search started (two lack Vietnamese, one has no true italic for the editorial surfaces), and the shortlist that followed was built entirely inside the envelope.

The hard filters derived from this sheet:

- License class: open license (OFL or equivalent) for phase 1; commercial only with a named budget line.
- Scripts: Latin with precomposed Vietnamese diacritics; any face without them is rejected unread.
- Formats: woff2 for web plus files the PDF generator can embed; variable builds preferred where one file serves both.
- Weights and styles: 400, 600, 700 minimum, with a true italic for editorial surfaces.
- Accessibility: legible at production sizes and stable under the 1.4.12 spacing overrides without layout repair.
- Payload: no more than four font files per family on a page; beyond that needs a written case.
- Delivery: a path to unicode-range subsets or npm delivery must exist; a face available only as one monolithic file fails the payload line.
- Maintenance: evidence of an active upstream, or a governance plan to fork; an abandoned face is a liability the sheet should price.

## Quick reference: default constraint values

When the brief is silent, these defaults are defensible starting points; write them into the sheet as decisions rather than leaving fields blank:

| Field | Sensible default | Why |
| --- | --- | --- |
| Body size floor | 1rem (16 px); 1.125rem (18 px) for long reading | Input zoom, iOS form behavior, readability |
| Leading | 1.5 unitless for body; down to 1.1 for display | 1.4.12 tests at 1.5x; display tolerates tighter |
| Measure | 45 to 75 characters | Comprehension and return-sweep accuracy |
| Contrast | 4.5:1 text, 3:1 large text and UI (AA) | WCAG 2.2 criteria 1.4.3 and 1.4.11 |
| Zoom and reflow | 200 percent zoom; reflow at 320 CSS px | WCAG 2.2 criteria 1.4.4 and 1.4.10 |
| Font payload | 100 to 150 KB per page, woff2, two families | A performance budget most teams can hold |
| Weights | 400, 500 or 600, 700; add 300 only with cause | Every extra weight is bytes and QA surface |
| Language list | Launch languages plus the 12-month roadmap | Late script additions force system migrations |
| Italic policy | True italic wherever editorial voice exists | Synthetic italics are a rendering penalty, not a style |
| Fallback stack | Defined at sheet time, not launch week | The fallback is what users see first and on failure |
| Trial licenses | Paired with a purchase decision date | Trials used for production design expire before launch |
| Locale detail | Dialects named where they change rendering (pt-BR versus pt-PT) | Locales alter hyphenation, quoting, and case rules |
| Size floors | 12 px floor for UI, 16 px for body and inputs | Below these, zoom and input behaviors misfire |

Defaults are placeholders for a decision, not decisions themselves. The sheet is done when every field holds a project-specific value or an explicit "default accepted".

## Field notes: constraints teams discover too late

- The email program: discovered at launch that the webfont never renders in most email clients; emails revert to system stacks, so the brand voice the brief promised was never in email at all. State email reality in the sheet.
- The embedded PDF: server-side report generation needed embedding rights the chosen commercial license did not include at that tier; the team either upgraded the license or swapped the report face. Both cost more than a constraint line.
- The 12-month market: Vietnamese was "maybe" in the brief and certain in reality; the chosen Latin display face had no precomposed Vietnamese diacritics, and the marketing site migrated faces a quarter after launch.
- The trial license: a 30-day trial was used to design the whole system, then the purchase was not approved in time and the launch shipped fallback fonts. Pair any trial in the sheet with a purchase decision date.
- The webview: the mobile app's help center rendered in a webview, which counted as web for licensing but behaved like the app for users; nobody had written down which rules applied.
- The procurement review: a security review asked for font provenance and licenses; the project had none on file and lost a week reconstructing it. The signed, versioned constraint sheet is the artifact they wanted.
- The rebrand: a mid-project rebrand reopened every constraint; the versioned sheet made the delta explicit instead of triggering a full re-litigation.
- The third-party embed: an embedded survey tool rendered its own text, outside the design system and outside the licenses anyone had checked; the sheet gained a "surfaces we do not control" line.
- The open-sourced theme: releasing the documentation theme made every bundled font a redistribution question; the open-license-only constraint, written months earlier, had already answered it.
- The contractual turn: an enterprise customer required WCAG 2.2 AA in the contract, and the type system's contrast and override promises became binding overnight; commitments in the sheet are cheaper than commitments in a contract.
- The seat surprise: desktop seats were counted for designers only, then engineering installed the font to build PDF exports; the sheet's seat line had said "everyone who installs" and the register followed the sheet.
- The handoff gap: constraints stopped at font choice and never named who maintains tokens, so six months later nobody owned the per-language rules; ownership is a constraint too.

## Audit checklist: reviewing a constraint sheet

- [ ] Every field filled or explicitly defaulted; no blanks that mean "nobody asked".
- [ ] Languages listed as exact languages with a phase split, not as script families.
- [ ] Every surface that renders text named, including PDF, email, webviews, and exports.
- [ ] The hardest surface named, and the search order derived from it.
- [ ] Accessibility commitments written as numbers (contrast ratios, size floors, WCAG target version), not as adjectives.
- [ ] License scope covers seats, embedding, vendors, and redistribution, each with a number or an explicit "none".
- [ ] Budget stated numerically, including zero as a deliberate choice.
- [ ] Open questions each have an owner and a due date.
- [ ] The sheet is version-controlled and carries sign-off from the decision owner.
- [ ] Each red flag in the brief (premium with no budget, all languages, same font everywhere) answered in writing.
- [ ] Every constraint carries its source: brief, stakeholder answer, regulation, or an accepted default.
- [ ] The 12-month language roadmap confirmed with product, not assumed.
- [ ] Trial licenses, if any, carry purchase decision dates.
- [ ] Engineering and content reviewed the sheet, not only design.
- [ ] The hard filters derived from the sheet are written down beside it and sanity-checked against one known candidate.
- [ ] Open questions closed or re-owned before shortlisting starts.
- [ ] A fallback plan exists for the hardest surface: what ships if no candidate passes, and who decides.
- [ ] The sheet's version history shows at least one reviewed revision; unchanged sheets are usually unreviewed sheets.

## Cross-references

- [Research workflow](research-workflow.md)
- [Worked examples](worked-examples.md)
- [Presenting to stakeholders](presenting-to-stakeholders.md)
- [Font governance and review](font-governance-and-review.md)

Compiled 2025 as part of the Fontlore project.
