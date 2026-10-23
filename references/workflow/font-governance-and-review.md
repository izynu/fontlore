# Font Governance and Review

What this reference covers: Team-level font governance: maintaining an approved-fonts list with license evidence, running a request process for new families, keeping a license register with renewal dates, assigning an owner per product surface, deprecating fonts deliberately, and handling legacy fonts that cannot be relicensed. Includes agency-specific guidance for multi-client work and lightweight templates for small teams.

Governance is what makes font decisions boring in the good way: the approved list answers most questions before they are asked, the register prevents license surprises, and the review cadence catches drift. The license-audit-checklist reference is the periodic deep check; this reference is the standing structure it audits.

## Why governance exists

- Without it, fonts arrive through side doors: a designer's trial font in a mockup, a freelancer's file in a handoff, a dependency added during a hack week.
- The failure mode is never aesthetic; it is legal and operational: unlicensed use discovered at launch, subscriptions lapsing silently, orphaned files nobody can explain.
- Governance does not need to be heavy. Its minimum form is four artifacts: an approved list, a register, a named owner, and a review date. Everything else scales from there.

## The approved-fonts list

- One entry per family: name, exact license identity (OFL-1.1, Apache-2.0, UFL-1.0, or the commercial license title), license scope granted, approved surfaces, and pinned version.
- License evidence travels with the entry: the license file in the repository, or the stored PDF and invoice reference for commercial licenses. The open-source-due-diligence reference defines what counts as evidence.
- Approved surfaces are explicit: "web (all domains), desktop (design team), app (iOS and Android)". "Anywhere in the company" is not an approval.
- Mark each entry with its last review date; a list that is not current is decorative.
- The list lives in the design-system repository or governed docs, version-controlled, not in a chat thread or a personal note.
- Entries record the adoption rationale in one or two lines, so future reviewers know why the family exists in the system at all.

## Requesting a new family

- A short intake form: what need the current system fails to meet, the proposed family with upstream source, license class and scope, surfaces requested, and the requester's name.
- The review applies the standard filters: license scope covers the request, provenance verified, script coverage checked, overlap with the approved list considered, and the personality case argued once, briefly.
- Timebox the review to one or two rounds; the point is a decision with a record, not a committee.
- Outcomes are trinary and recorded: approved (with scope), rejected (with reason, so the same case is not re-argued monthly), or deferred pending evidence.
- The written rationale joins the entry on the approved list; adoption without recorded reasoning is how governance decays into folklore.
- Fast path for OFL equivalents: if the request is "same role as an approved face but open licensed", the review is mostly a due-diligence pass and can clear in a day.

## The license register

- One row per license the organization holds or relies on: family, license identity, entitlement scope (seats, domains, pageview tiers, platforms), purchase reference, renewal or expiry date, and the owner.
- Subscription entries carry the failure mode in writing: what stops working when the subscription lapses, and who gets notified.
- Pageview-tier entries carry current traffic, the tier ceiling, and an alert threshold; the licensing FAQ explains why tiers are contractual rather than technical.
- Renewal dates get calendar reminders with lead time; a renewal discovered on the expiry date is a negotiation held at gunpoint.
- The register and the approved list must agree; disagreement between them is an audit finding in itself.
- Register rows link to evidence the same way approved-list entries do, so an auditor can walk from either side.

## Ownership per surface

- Every surface that ships fonts has a named owner: website, native apps, email, print and packaging templates, documents, embedded devices.
- The owner answers the operational questions: which fonts and versions this surface uses, whether changes shipped cleanly, and whom to call when rendering breaks.
- Owners are individuals, not teams; a team name is how ownership becomes fiction.
- Surface ownership and license ownership are different roles; one person can hold both, but the register should say so explicitly.
- Owner changes are events: hand over the register row, the evidence links, and the current known issues in the same week.

## Deprecation process

- Deprecate in three stages: freeze (no new uses; existing uses documented), migrate (replacement named, surfaces switched, progress tracked), remove (files and entries deleted on a stated date).
- The deprecation record names the reason: superseded by a better match, license terms changed, upstream abandoned, or brand change.
- Removal includes the environment sweep: CSS, packages, design libraries, and templates all lose the family. Partial removals leave zombies that return in audits.
- Buffer time between migration and removal catches the long tail: archived materials, printed templates, and the one service nobody remembered.
- The deprecation entry links to the replacement's adoption entry, so the story reads cleanly in one place.

## Audit cadence

- The audit checklist runs quarterly or before major launches; governance is what makes those audits short, because the evidence is already organized.
- An annual deep audit re-verifies license documents at their sources, not just internal records, because upstream facts drift.
- Audit findings get owners and dates in the register; unowned findings are how audits become theater.
- The audit also reviews governance itself: was the intake process used, are review dates current, did any surface lose its owner.
- Keep the audit outputs; a history of clean, dated audits is the asset clients and legal teams actually want to see.

## Legacy fonts that cannot be relicensed

- Some fonts in active use have no obtainable license: the foundry is gone, the rights are tangled, or the file predates everyone in the building.
- Name the situation in the register instead of hoping: family, where used, why the license cannot be established, and the risk acceptance signed by someone with authority to accept it.
- Set a substitution plan even for accepted risks: a documented open alternative, an estimated migration cost, and a trigger that would force the swap.
- Interim risk controls: no new surfaces adopt the legacy font, no redistribution of the file, and the file does not leave the organization's controlled systems.
- Do not launder legacy fonts by re-creating metadata or renaming files; provenance problems survive cosmetics.

## Agencies handling multiple clients

- Licenses are per-client: agency-held licenses rarely extend to client use, so the default is licensing in the client's name; the client-handoff reference covers the mechanics.
- Keep a register per client, never one blended register; cross-client font reuse is a recurring source of breaches.
- No carrying fonts between projects: a face licensed for client A does not appear in client B's mockup, however convenient.
- Contract language allocates the duties: the agency warrants it used licensed fonts and will hand over evidence; the client verifies scope before launch.
- At engagement end, the register row closes with a handoff memo: what was licensed, in whose name, and where the evidence lives.

## Lightweight templates for small teams

- A one-page register is enough: family, license, scope, renewal date, owner, evidence link. A dozen rows cover most small products.
- One approver role instead of a committee; the approver uses the same filters, just faster.
- Approved list and manifest can be one file at this scale; split them when a second product or a second brand appears.
- The quarterly review is a 30-minute calendar event with the register open; the output is a dated note, even when nothing changes.
- Scale governance with risk, not with headcount: the first commercial license or the first client engagement is the moment to formalize.

## The intake form, as a template

A new-family request fits in six fields; here is the template verbatim:

```
1. Need: what the current system fails to do (one sentence, concrete)
2. Proposal: family, designer/foundry, upstream source URL
3. License: exact license identity, scope requested (surfaces, seats, domains)
4. Alternatives: OFL equivalents considered, and why they do not fit
5. Evidence: link to the verified license file and provenance notes
6. Requester and date
```

- Field 1 is the one reviewers push back on; a real need names the failure, not the desire.
- Field 4 is where most requests resolve themselves: half the time, an approved face already covers the need.

## The register row, as a template

One row per license, with these fields:

```
family / license identity / scope (seats, domains, tiers, platforms)
purchase or adoption reference / renewal or expiry date
owner (named person) / evidence link
last verified (date) / notes (failure mode if a subscription lapses)
```

- OFL families get rows too; the scope field simply reads "OFL-1.1, no scope limits", and the row records which version is pinned.
- The notes field is where tier alerts and negotiation lead times live.

## Signals governance is working

- New fonts arrive through the intake form in practice, not only in the documentation.
- Renewals happen with lead time; nobody has been surprised by an expiry in the last two cycles.
- The audit takes the timebox it was given, because the evidence was where the register said it would be.
- A departing owner's successor picks up the surface from the artifacts alone.

## Common mistakes

- An approved list without evidence, which is a wishlist, not governance.
- Renewal dates in someone's memory instead of the register; subscriptions lapse silently and take production fonts with them.
- Ownership by team name, dissolving accountability exactly when a rendering break needs a decision.
- Deprecation as rumor: a family quietly stops being used but is never removed, so every audit rediscovers it.
- Governance built for a 200-person company inside a 6-person team, which guarantees the process is ignored within a quarter.
- Treating the first audit finding as a scandal instead of as the process working.

## Decision rules

- A font not on the approved list does not ship; the request process exists to be fast, so use it instead of the side door.
- No license evidence, no approval; enthusiasm is not evidence.
- Legacy risk is accepted in writing once, by an owner, with a trigger; it is never ignored indefinitely.
- When register and approved list disagree, the license document at the source wins and the records get corrected the same day.
- Governance that cannot be run by a successor from its own artifacts is governance in name only.

## Cross-references

- [License audit checklist](../licensing/license-audit-checklist.md)
- [License families compared](../licensing/license-families-compared.md)
- [Presenting to stakeholders](presenting-to-stakeholders.md)
- [Brief to constraints](brief-to-constraints.md)

Compiled 2025 as part of the Fontlore project.
