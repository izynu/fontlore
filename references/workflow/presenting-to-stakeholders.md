# Presenting to Stakeholders

What this reference covers: Presenting font decisions to stakeholders: showing three options with tied-down rationale, converting taste arguments into testable claims, documenting the decision so it survives personnel changes, and handling the revision loop without churn. Stakeholder management is half of typography in organizations.

## Present three options, not thirty

The comparison workflow produces ranked candidates; the stakeholder presentation shows three:

- The recommended option, clearly labeled as the recommendation, with its evidence summarized.
- A strong alternative that differs meaningfully (different voice or different logistics), not a near-duplicate.
- A safe fallback (the system stack, or the incumbent) so the "do nothing" path is explicit and costed.

For each: one live specimen page with real copy, one line of license and cost implications, one line of coverage facts, and the two or three risks. Stakeholders decide between framed options; they do not rank forty typefaces, and showing forty signals that no work was done.

## Converting taste into claims

Taste arguments ("it feels more premium") cannot be decided; claims can:

- "Premium" becomes: does the higher-contrast option pass legibility at our 13 px UI sizes? Show the ramp.
- "More friendly" becomes: which brand values does each option's voice serve, scored by the group in the matrix?
- "Our competitor uses it" becomes: is differentiation or convergence the goal here, stated as a requirement before the meeting?
- "Too common" becomes: is distinctiveness worth the licensing and coverage risk of the rarer option?

Structure every claimed property as something the specimen page can show or the matrix can score. If a claim cannot be made testable, name it as preference and let the decision owner weigh it explicitly.

## The meeting format

- Fifteen minutes of artifacts, thirty minutes of decision; longer meetings breed redesigns.
- Live specimen pages, not screenshots: stakeholders type their own names and product strings; ownership of the copy builds ownership of the choice.
- Show the failure cases honestly: the language block where option B clips, the table where option C wobbles. Presenting only strengths hides the tradeoffs that will resurface as bugs.
- State the constraints from the constraint sheet at the start; the meeting decides inside the envelope, not about the envelope.
- End with a decision and an owner, recorded in the meeting notes; "we'll circle back" is how font projects consume quarters.

## Documenting the decision

Write the decision record while the meeting is fresh, in a form like:

- Context: the constraint sheet summary and the problem being solved.
- Options considered: the three, with matrix scores and links to the comparison artifacts.
- Decision: the family (or families), versions, licenses, and the tuning assumptions (sizes, leading, per-language rules).
- Consequences: what this enables, what it forecloses, and the conditions that would reopen the decision (new market, rebrand, license change).
- Links: comparison page, license documents, version records.

File it where design decisions live (an ADR folder, the design system repo); a decision that cannot be found will be re-litigated within a year.

## Handling revisions without churn

- Revisions happen; the discipline is batching them: one revision round after the decision, with all feedback collected, rather than weekly drips.
- Each revision request gets the same treatment: convert to a claim, test it, record the outcome. "Can we try something softer" becomes a scored second look at the alternative, not an open-ended search.
- The decision record notes the revision and the reason; three revisions without a recorded reason means the decision was never actually made.
- Post-launch, revisit on the governance cadence (quarterly or per release), not whenever someone new joins; new-stakeholder opinions enter through the request process, not through ad-hoc swaps.

## Common mistakes

- Presenting specimens from foundry marketing pages: those show the font at its best and the stakeholder at their most impulsive.
- Burying the recommendation among equal options; stakeholders read equality as "no one did the work".
- Arguing from taste in the meeting: it delegitimizes the evidence and invites every opinion to be weighed equally.
- No decision owner: the loudest voice becomes the owner by default.
- Skipping the license and cost slide: discovering the budget conflict after the excitement is how decisions get reversed late.
- Not recording the loss: the rejected options and why are as valuable as the winner, because the same options return with the next rebrand.

## Decision rules

- Any option presented must have passed every hard gate in the matrix; unviable options are not presented as variety.
- If stakeholders reject the recommendation: the decision owner picks between the recorded alternatives with reasons on the record; the process survives the disagreement.
- New constraints appear mid-meeting (a new market, a licensing limit): pause, update the constraint sheet, reconvene; deciding on stale constraints produces reversals.
- The decision record is written before the next meeting happens; memory is not documentation.
- Reopen a decided choice only through the governance process with new facts; reopen it ad hoc and every future choice inherits the instability.

## Worked example: a type decision for a banking app

Scenario: a retail banking app replaces its default UI font. Constraint sheet facts: WCAG 2.2 AA committed, five languages at launch including Vietnamese, a licensing budget exists, iOS and Android native.

1. The three options: the recommended (a text-first sans with tabular figures and a strong 500 weight), the alternative (a warmer humanist sans, one license tier cheaper but weaker at tiny sizes), and the fallback (keep the system font: zero cost, zero migration).
2. The specimen page used the app's real strings: a balance in tabular figures, a transaction list at 13 px, an error banner, Vietnamese and Polish paragraphs, and the longest product name.
3. The claims: legibility at 13 px shown as a size ramp; brand voice scored 1 to 5 by the six people in the room; migration effort estimated in engineering days from the token audit.
4. The failure cases shown deliberately: the alternative's Vietnamese diacritics clipped at compact leading; the recommended option's stiffer personality. Both notes entered the record.
5. Decision: the recommended option, recorded with versions, license seats, and the tuning notes (600 not 700 for emphasis at small sizes, 1.45 leading in dense lists). The fallback stayed in the record as the documented "do nothing" path with its real cost.
6. The revision round: one request to see a rounder alternative; it was converted to a claim ("friendlier"), scored in the matrix, lost, and the record shows it.
7. Artifacts archived: the specimen pages, matrix scores, and screenshots stored beside the decision record, with the font versions tested named in the record.
8. Four weeks later: the governance review checked adoption (tokens used, no rogue weights) rather than reopening taste; the decision stayed closed.

The meeting ran forty-five minutes because the artifacts were ready. The same decision attempted without the matrix and the specimen page had already failed once in a prior quarter.

What the record prevented: at the next rebrand the same options resurfaced by memory, and the record's rejected-options list with their scores retired them in one paragraph instead of one meeting.

## Quick reference: the six-slide deck

The presentation that works is short and artifact-driven:

- Send a five-minute pre-read: the constraint summary and the three options with costs. Meetings that open with "what are we deciding" never finish on time.

| Slide | Content | Purpose |
| --- | --- | --- |
| 1. The problem | The constraint summary and what the current type fails at | Frames the decision inside the agreed envelope |
| 2. The three options | One live specimen link each, with license class and cost | Shows the work without forty candidates |
| 3. The evidence | Size ramps, language blocks, matrix scores | Moves the argument from taste to testable claims |
| 4. The risks | Two or three honest risks per option, with mitigations | Pre-empts the objection that hides until launch |
| 5. The recommendation | One option named, with tuning notes and migration steps | Stakeholders expect a recommendation, not a poll |
| 6. The decision | Owner, record location, revision process | Ends the meeting with a decision on the record |

Fifteen minutes of slides, then discussion. Every slide is an artifact that already exists from the comparison workflow; a deck that requires new work to build is a signal the decision is not ready to present.

Keep the deck to artifacts: each slide above is a document the constraint, research, and comparison workflows already produced. Leave the last five minutes to draft the decision record in the room; a record drafted live is corrected in minutes, while one reconstructed next week is contested for months.

## Field notes: questions stakeholders actually ask

Prepare a one-sentence answer for each; they recur in every organization:

- "Why not Google Fonts? They are free." Answer: quality ceiling and differentiation; the recommendation either beats the catalog on a named dimension or the fallback wins.
- "Can we use the font from that competitor's site?" Answer: licensing is per company and per scope; identify the face, check its license class, and note that convergence is a brand decision, not a font decision.
- "Will it slow the site down?" Answer: the payload number from the constraint sheet, in kilobytes, against the budget.
- "What happens if legal objects?" Answer: the license class and the evidence record; licenses in this class clear procurement routinely.
- "Who else uses it?" Answer: the Fonts In Use entries gathered in research; evidence of context, not of quality.
- "My partner hates it." Answer: collect it as a revision, convert it to a claim, score it in the next round; the process absorbs opinions without reversing decisions.
- "It does not feel like us." Answer: voice is a scored entry in the matrix; the score, not the feeling, is what gets recorded and revisited.
- "Can we decide next quarter?" Answer: the cost of delay from the constraint sheet (trial expiry, launch date, license renewal); a delay is a decision too, and it gets recorded as one.
- "Why this one over the one with the nicer 'a'?" Answer: the matrix scored whole families against the corpus; a single glyph is a revision request, not a decision.
- "Will marketing need a separate license?" Answer: the license scope line from the sheet, restated; scope questions asked in the meeting get answered from the record, not guessed.
- "What if the font goes away?" Answer: the fallback plan (the safe option, the system stack) is on the table and costed; continuity was part of the score.
- "Can we see it on the real dashboard first?" Answer: yes, that is the pilot path written into the decision record; a time-boxed pilot with checkpoints beats an open-ended trial.
- "Who maintains this after launch?" Answer: the owner named in the record and the governance cadence; ownership is decided here, not discovered later.

The pattern: every answer cites an artifact (a number, a license class, a link, a recorded score). Answers that cite only opinion train the room to treat typography as opinion.

## Audit checklist: before the meeting

- [ ] The constraint sheet circulated in advance; no constraints introduced for the first time in the meeting.
- [ ] Specimen pages load offline or on the local network; foundry hotlinks fail at the worst moment.
- [ ] All three options passed every hard gate; unviable options were removed, not presented for variety.
- [ ] The license and cost line verified against the current price sheet, not memory.
- [ ] Failure cases prepared deliberately for each option.
- [ ] The decision record template pre-filled with everything except the decision.
- [ ] A named decision owner invited, and the meeting ends with their call on the record.
- [ ] The revision process stated up front: one batched round, claims only, recorded outcomes.
- [ ] The three options differ meaningfully; no near-duplicates presented as variety.
- [ ] Cost lines include renewals and seat growth, not just year one.
- [ ] The revision round has a scheduled date before the meeting ends.
- [ ] The specimen pages reflect the tuning notes from the comparison phase, not browser defaults.
- [ ] The matrix scores are in the pre-read so the meeting argues about weights, not about facts.
- [ ] The decision record template is open on screen when the decision lands.
- [ ] Anyone whose sign-off is required was invited; missing approvers reopen decisions.
- [ ] The meeting is scheduled after the specimen pages were verified on local assets, not before.

## Cross-references

- [Testing and comparing shortlists](testing-and-comparing-shortlists.md)
- [Brief to constraints](brief-to-constraints.md)
- [Font governance and review](font-governance-and-review.md)
- [Worked examples](worked-examples.md)

Compiled 2025 as part of the Fontlore project.
