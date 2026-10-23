# Documenting Identification Results

What this reference covers: How to record identification work so it survives handoffs and audits: evidence fields, confidence levels, alternative candidates worth keeping, and the license implications that flow from what you identified. Documentation turns a private hunch into a reusable organizational asset.

Identifications get re-litigated every time the record is missing. The person who finds the font next year should inherit your evidence, not your mystery.

## Why the record matters

- Identification drives money: purchases, license scopes, and design-system decisions all ride on what you concluded.
- Unwritten conclusions decay; in six months, "I think it was that grotesque from the finance deck" is worthless, while a record with crops and tool outputs is decisive.
- Records enable reuse: the same font will be asked about again in a different project, and a good record answers instantly.
- In agency settings, the record protects the team: it shows diligence when a client disputes a later license finding.

## The evidence record fields

- subject: what was identified, with the artifact (screenshot, photo, print piece) and its source.
- sample: the archived original image and the crops used, with dates.
- tools: every identifier run, each tool's top candidates, and the date.
- analysis: the letterform evidence you observed (terminals, g and a forms, numerals) and what eliminated candidates.
- conclusion: the identified family, version impression, and the foundry or publisher.
- verification: overlay results, specimen checks, any foundry or community confirmation, and Fonts In Use links.
- confidence: the tier (confirmed, probable, possible, unknown) with one sentence of justification.
- license: what you learned about the license at the source, and whether it fits the intended use.
- next actions: purchase path, open questions, or the reason the case was closed as unresolved.

Keep the template short enough that people actually fill it; a record that takes an hour will not get written twice.

## Confidence levels

- Confirmed: foundry confirmation or overlay-identical evidence. Act on it.
- Probable: multiple independent signals agree; no contradictions. Act with a paper trail.
- Possible: one signal, or partial agreement. Do not purchase; keep hunting or label every downstream use as provisional.
- Unknown: memory, heavy stylization, or unresolved contradictions. Document the dead end so it is not retraced.
- Downgrade on any contradiction; a single mismatched diagnostic letter outweighs three agreeing tools.

## Recording alternatives

- Keep the top three to five candidates from the tools, not just the winner; projects change budgets and the runner-up often becomes the adoption.
- Note which alternatives are free and open (OFL or similar) versus commercial; a budget cut should not reopen the investigation.
- Record why each alternative lost, in one line each; these notes are the difference between a decision and a coin flip next time.
- For custom lettering conclusions, record the closest retail relatives and what distinguishes the lettering from them.

## License implications of the result

- The identification determines the purchase path: an identified commercial font leads to foundry or marketplace licensing with scope decisions; an identified open font leads to license-file verification and self-hosting.
- If the identified font is commercial, record the scope the project needs (desktop, web pageviews, app, logo) before contacting anyone; quotes depend on scope.
- If the identified font is free, verify the license at the source (not the aggregator) and record the exact license name; "free" is not a license.
- If the conclusion is custom lettering, no font license applies to the logo itself, but the supporting system still needs licensed fonts; separate the two in the record.
- If the identification is uncertain, purchases wait; a wrong-font purchase is a sunk cost that also creates a false audit entry.

## Workflow

1. Fill the record as you work, not after; tool outputs and observations are perishable.
2. Attach the original sample, crops, and screenshots of tool results.
3. Assign the confidence tier with a one-sentence justification.
4. Record alternatives with reasons, and the license findings at the source.
5. Close the case with next actions and an owner, or file it as unresolved with what would resolve it.
6. Store records where the team actually looks (the font manifest or design repo), not in personal notebooks.

## Common mistakes

- Writing the conclusion without the evidence, producing an assertion nobody can check.
- Recording the winner only, losing the alternatives that become relevant when budgets change.
- Marking memory-based conclusions as confirmed because the stakeholder nodded.
- Forgetting the license field entirely; identification without license status is half a record.
- Storing evidence in chat threads or personal drives, guaranteeing loss at the next reorg.

## Decision rules

- No confidence tier, no record: an untiered conclusion is a rumor.
- Possible or unknown tiers block purchases automatically.
- If two records contradict (two people identified different fonts for the same artifact), the record with verification evidence wins, and the loser gets re-run.
- Re-open a closed record only with new evidence; opinions are not evidence.

## Comparison table

Confidence tiers, their evidence bars, and what each permits downstream:

| Tier | Evidence bar | Permitted actions |
| --- | --- | --- |
| Confirmed | Foundry confirmation in writing, or overlay-identical metrics and shapes | Purchase, adopt, add to the design system |
| Probable | Two or more independent signals agree; hand check passes | Proceed with a paper trail; purchases allowed with a note |
| Possible | One signal, or partial agreement, no contradictions | No purchases; label every downstream use as provisional |
| Unknown | Memory, heavy stylization, or unresolved contradictions | Document the dead end; nothing downstream may depend on it |

Read the tiers as ratchets, not grades: corroboration moves a record up, contradiction moves it down, and time moves it nowhere. A probable tier plus a documented foundry inquiry functions almost like confirmed in practice, because the attempt itself is evidence.

The second axis worth tabulating is evidence type, because mixing them is how records rot: tool output, letterform observation, provenance documents, and human testimony are different currencies, and a record should name which currency each claim is paid in. "Two tools agree" is weaker than "two tools agree and the g matches by hand", and both are weaker than a written foundry reply.

## Worked example

A filled record for a screenshot of a SaaS pricing page headline, condensed to show what "enough" looks like:

- subject: pricing page headline, screenshot from the vendor's marketing site, captured the day the request came in.
- sample: original PNG archived in the project evidence folder, plus two crops: one wide for tools, one tight on g, a, and t for the hand check.
- tools: WhatTheFont's top five led with Inter, Roboto, and three near-identical UI sans faces; Matcherator returned Inter first and Roboto second; Fonts Ninja read the live page as declaring Inter with woff2 files served.
- analysis: the sample's g is single-story, which eliminates Roboto (double-story g) and the grotesque candidates; apertures are open and the x-height is very tall, both consistent with Inter.
- conclusion: Inter, regular weight, by Rasmus Andersson; the site serves the current open release.
- verification: Ninja's declared family agrees with the pixel evidence, and a metrics overlay of the headline against Inter Regular matched widths across the full string.
- alternatives: Roboto lost on the g form; the three lookalike faces lost on aperture and x-height; each carries a one-line reason in the record.
- confidence: confirmed; two tools, one DOM read, and one overlay agree with no contradictions.
- license: SIL OFL 1.1, verified at the Inter GitHub repository rather than through an aggregator page.
- next actions: case closed; the record lives in the team font manifest under the vendor's name.

Note the shape of the analysis entry: every claim names a letter or a measurement. "Looked like Inter" is worthless in a record; "single-story g, which Roboto's double-story g rules out" is checkable by anyone in ten seconds.

The same case, done badly, for contrast:

- conclusion only: "It's Inter." No tools, no dates; six months later nobody can tell whether the g was ever checked.
- evidence replaced by memory: "I ran a few identifiers." Which ones, on what crop, is gone.
- winner-only logging: the Roboto candidate and the reasons it lost are missing, so a budget change reopens the entire hunt.
- license field blank: the team learns at adoption time that nothing was verified at the source.
- confidence omitted: the reader cannot tell confirmed from a hunch, so they either distrust everything or trust everything.

The bad version takes two minutes to write and costs the next person the whole investigation; the good version takes ten minutes and never needs writing twice.

## Field notes

Practices that separate records people trust from records people ignore:

- Capture tool outputs as screenshots at run time; rankings shift as catalogs change, and a dated screenshot is evidence while a retelling is not.
- Name the weight impression early; a large share of identification disputes turn out to be about weight, not family.
- Record what the artifact is made of (screen render, print scan, photo of signage), because it sets the ceiling on what any tool could prove.
- When a stakeholder "recognizes" the font, log it as context, not verification; recognition is a lead, not evidence.
- Write the license field even when the answer is unknown at this time; an explicit unknown invites the follow-up, a blank field hides it.
- Store the record next to the artifact it describes, not in the thread where the question was asked; threads scroll, repositories do not.
- When a case closes unresolved, write down the one piece of evidence that would settle it; dead ends with exit signs are the most valuable records of all.
- Version-note the conclusion: "Inter as served in early 2025" ages honestly, while a bare family name quietly claims timelessness it does not have.

## Quick reference

The minimum record as a checklist; nine fields, one line each, five minutes total:

1. subject: what was identified and where it came from, with the artifact named.
2. sample: where the original image and the crops are archived.
3. tools: which identifiers ran, their top candidates, and the dates.
4. analysis: the letterform evidence, naming actual letters.
5. conclusion: family, weight impression, foundry or publisher.
6. verification: overlays, specimens, confirmations, Fonts In Use links.
7. confidence: the tier plus a one-sentence justification.
8. license: the license name verified at the source, and its fit for the use.
9. next actions: owner, purchase path, or the closed-unresolved note.

Rules of thumb that keep records honest:

- Write the analysis field before the conclusion field; the order forces evidence first.
- If a field has nothing to say, write why rather than leaving it blank.
- One screen per record; anything longer gets skipped by the next reader.
- Attach the artifacts (crops, tool screenshots, confirmation emails) rather than describing them.
- Revisit dates go on any record below confirmed, since sources, versions, and URLs drift.

## Cross-references

- [Verifying an identification](verifying-an-identification.md)
- [Identification workflow overview](identification-workflow-overview.md)
- [License audit checklist](../licensing/license-audit-checklist.md)
- [Free font risks](../licensing/free-font-risks.md)

Compiled 2025 as part of the Fontlore project.
