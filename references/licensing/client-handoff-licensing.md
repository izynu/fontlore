# Client Handoff Licensing

What this reference covers: Getting fonts correctly licensed when work moves from agency or freelancer to client: who needs which rights, the scope mismatches that cause post-handoff incidents, and the workflows that make handoffs clean. Most handoff failures are scope failures, not paperwork failures.

The agency bought the font, the client uses the font, and a year later an audit finds the license never covered the client. Everything in this guide exists to prevent that sentence.

The fix is structural, not heroic: a memo template, a proposal line item, and one quarter-after review, applied to every engagement, make handoffs boring in the useful way.

## Who needs which rights

- The agency needs licenses for its own use: designer desktop seats for creating the work, possibly webfont scope for staging and demos.
- The client needs licenses for its use: marketing team desktop seats, production webfonts, app embedding, and any print vendor scenarios.
- These are usually separate licenses from the same foundry, not a transfer of one license; most font licenses are non-transferable between legal entities.
- Open fonts (OFL and friends) collapse the problem: everyone can use the same files with license retention, which is a real argument for open fonts in agency work.
- The deliverable list drives the license list; build both from the same document.
- Size client seats from the client's org chart, not from the project team; the twelve-person marketing department outlives the six-week engagement.
- Webfont scope belongs to whoever operates the production domain, which is usually the client's IT or marketing org, not the agency.
- When the client has an existing enterprise subscription (Monotype Fonts, Adobe Fonts), check it before buying anything; the face may already be covered.
- For OFL faces, the only deliverable is documentation: license files, sources, and version records travel with the files.

## Common scope mismatches

- Desktop seat count: agency bought 2 seats, client's in-house team is 12. The fix is a client-side purchase sized to their org, budgeted at proposal time.
- Domain scope: webfonts licensed to the agency's demo domain, production site launched on the client's domain outside the grant.
- Pageview tier: agency-sized traffic assumptions versus client reality; the client's Q4 campaign doubles traffic.
- App embedding: prototype built with desktop-licensed fonts, shipped app still containing them.
- Logo usage: font chosen for the mark under a license that excludes logo use; discovered during trademark filing.
- Vendor scenarios: print shops and outside production partners need their rights sorted; most licenses cover output received from the client, but verify for unusual workflows.
- Pitch decks: fonts trialed for the pitch live in the deck forever unless replaced; decks get forwarded, and forwarded decks carry unlicensed fonts.
- Slide and document templates: the client's internal template library will outlive the project; check what fonts it embeds.
- Localization vendors: translators and typesetters receiving font files are users under most licenses; include them in the seat count.

## What typically transfers and what does not

- Font files plus license rights: generally do not transfer unless the license explicitly allows assignment.
- Rendered artwork (PDFs, images, outlined logos): flows to the client under the agency's licenses, since producing artwork is what desktop licenses cover.
- Webfont hosting responsibilities: move to whoever operates the production site, with licenses purchased accordingly.
- Open fonts: everything transfers trivially; just keep license files and documentation with the files.
- Subscriptions (Adobe Fonts, Monotype Fonts): they never transfer; the client needs its own subscription or perpetual purchases.
- Design source files: they transfer, but any font files inside them do not; deliver sources with fonts removed or with the memo explaining the licensing status.
- Documentation and specimens: transfer freely, and they are often the most valuable part, because they carry the reasoning that audits need.
- Modified font files (a customized cut made for the brand): transfer only with the modification and naming story written down, or leave them out entirely.

## The agency workflow

1. At proposal time, list deliverables and the font licensing each requires; quote client-side licensing as a line item, not a surprise.
2. During production, use open fonts for exploration where possible, reserving commercial purchases for the chosen direction.
3. Before handoff, produce the font licensing memo: per font, per use context, who holds what, what the client must still buy.
4. Deliver open fonts with their license files and a manifest; deliver commercial fonts only as licensed to the client, never as shared files.
5. Schedule a licensing review one quarter after launch; real traffic and real teams change the scope math.
6. Deliver the memo in a format the client can maintain (their wiki, their repo), not only as a PDF attachment.
7. Archive the same memo in the agency's records; future teams will be asked what was delivered and why.

## The client-side checklist

- Confirm every font in the delivered files is named, versioned, and licensed in the memo.
- Purchase the licenses the memo says you lack, sized to your organization.
- Store license documents with the font files in a governed location.
- Add fonts to the internal audit inventory so renewals and pageview tiers are tracked.
- When new use contexts appear (new app, new market site), re-run the scope check against the memo.
- Name an internal owner for the register; the memo's value decays the moment nobody owns it.
- Reconcile the memo against the actual files: unzip the deliverables and confirm the fonts inside match the rows.
- Diarize the renewal and tier dates the memo lists; a memo nobody calendared is a finding waiting for a date.

## Common mistakes

- Treating the agency's licenses as covering the client because "we paid for the project".
- Handing over font files with no license documents, guaranteeing a future audit scramble.
- Delivering Adobe Fonts-designed artwork plus a request that the client "keep using those fonts"; the client needs its own entitlements.
- Forgetting that campaign microsites and email templates count as new web properties for scope purposes.
- Not budgeting font licensing at proposal time, then eating the cost silently or cutting corners.
- Delivering the memo to a person instead of a place; people change jobs, places persist.
- Treating the quarter-after review as optional; it is the step that catches the client's real traffic and real team size.
- Assuming the client's procurement understands font licenses; write the memo for a smart generalist, not for a foundry veteran.
- Handing over trial or evaluation fonts with the deliverables because they were "already in the files"; trials are not client-side licenses at any price.
- Forgetting the agency's own rights end where the engagement ends; removing agency work from client surfaces that outlive the contract is part of the same checklist.

## Decision rules

- If the client will operate anything the fonts touch, the client needs its own license scope; there is no family plan that covers both entities by default.
- Prefer OFL fonts for long-lived client systems unless the design genuinely requires a commercial family; governance follows the files.
- Ambiguity about a clause at handoff: ask the foundry in writing and attach the answer to the memo.
- The handoff memo is a deliverable; if it is not written, the handoff is not done.
- When the deliverable is a design system, the licensing memo belongs in the system's documentation, versioned like any other token layer.
- Freelancers and small studios: the same discipline applies at smaller scale, and the memo can be one page; the discipline is the point, not the length.
- If the client refuses to budget licensing, the deliverable list shrinks to what the client can legally operate; put that tradeoff in writing rather than absorbing the risk.
- Duplicate brands across regions: license per entity that uses, not per brand; a brand used by three subsidiaries is three users.
- Handoffs to another agency happen too; the memo serves the incoming agency exactly as it serves the client.
- When the client's own customers touch the fonts (a platform client whose users see the brand), trace the chain to the entity that serves or embeds; scope follows use, not proximity to the contract.
- Keep the memo's language plain: "the client must buy X before launch" reads better in an audit than "licensing considerations apply".

## Quick reference: the handoff in six moves

1. Proposal: licensing as a line item, sized to the client's org.
2. Production: OFL for exploration, commercial only for the chosen direction.
3. Memo: one row per font, one page if possible, delivered to a durable place.
4. Purchase: the client buys what the memo says, before launch.
5. Register: the client adds fonts to their inventory with owners and dates.
6. Review: one quarter after launch, scope and traffic re-checked against the memo.

Agencies that run these six moves every time stop having licensing conversations during crises; the conversations happen during proposals, where they are cheap.

## The handoff memo, as a template

The memo is the deliverable that makes handoffs auditable. One section per font, in this shape:

- Family and version: exact family name, version string from the name table, and the file names as delivered.
- License identity: OFL-1.1, Apache-2.0, ITF-FFL-1.0, or the commercial document title; never "free" or "open source".
- Who holds what: the agency's grants (seats, demo domains), the client's existing grants, and the gaps the client must fill.
- Required purchases: per use context (web, desktop, app, print vendor), sized to the client's org, with the foundry or marketplace named.
- Open questions: anything the foundry must confirm in writing, with the question text included so the client's answer can be attached later.
- Excluded uses: what the deliverables do NOT cover (broadcast, packaging, merchandising) so the client's next project re-opens the check deliberately.
- Attachments: license files, entitlement PDFs, purchase references, and the written foundry answers collected during production.
- Versioning: a date, an author, and a change log, because handoff memos get re-read during audits years later.

A memo that fits on two pages and answers eight questions outranks a data room nobody reads.

## Worked example: the twelve-seat gap

An agency builds a brand system for a client using Inter (OFL) and a commercial display serif. The handoff walk:

- Proposal stage: the agency quotes "font licensing, client side" as a line item with a placeholder range, so the cost is visible before signatures.
- Production stage: designers work with the commercial serif under the agency's two desktop seats; exploration uses OFL faces wherever possible.
- Discovery at handoff: the client's in-house team is twelve people who will all touch the files, and the display serif is licensed to the agency, not to the client.
- The memo records the gap: twelve desktop seats plus a webfont license for the client's domain, quoted to the client with the foundry's own pricing page attached.
- Inter needs no purchase; the memo still documents it, with the license file and the note that any public redistribution of modified Inter files triggers the Reserved Font Name rules.
- The client's procurement asks why they cannot just use the agency's license; the memo cites the license's entity clause and offers the foundry contact for confirmation, which ends the debate in writing.
- Post-launch, the client adds the fonts to their own register and schedules their first internal audit; the agency's obligation ends, the documentation continues.
- The pattern to copy: no file moves without a memo row, and no memo row exists that the client cannot act on.
- The project ran on an OFL sans for exploration; the commercial serif entered only after the direction was chosen, which is why the licensing line item was small enough to approve without escalation.
- The agency's own seats were right-sized after handoff: two seats continued for the retainer work, and the extra trial installs were cleaned out of the studio machines.
- When the client later launched a microsite, their team checked the memo's domain row first, added the host to the license, and updated the register; the process worked because the memo named the process.

## Field notes

- The most common handoff failure is not missing paperwork; it is files that moved through channels nobody logged (a designer's personal Dropbox, a Slack DM, a zip on a shared drive).
- Agencies that standardize on open fonts for exploration cut their handoff risk dramatically: the only files that need entity-level licensing are the final choices.
- Subscription-held fonts (Adobe Fonts, Monotype Fonts) must be flagged in the memo as non-transferable, with the client's own path to the same faces named, or the client will "keep using them" into an incident.
- The memo should state the font versions delivered; a client who later "updates" a font to a new version has changed metrics and possibly license terms without knowing either.
- When the client operates in multiple countries, check whether their entity structure means several legal entities are using the fonts; multi-entity use is a scope question, not a footnote.
- Keep the memo in the client's repository, not only in email; the document that lives where the fonts live is the document that gets read during audits.
- A good test of the memo: hand it to a new hire on the client side and ask "what are we allowed to do with these fonts?" If they cannot answer from the memo alone, the memo is not done.
- Memos that include the foundry contact (with permission) turn future questions into one email instead of an archaeology project.
- The best agencies send the memo before the final invoice; it signals that licensing is part of the work, not an afterthought to the work.
- When a project spans years, reissue the memo at each phase gate; a 2022 memo describing a 2025 deliverable is a finding in itself.

## Cross-references

- [License audit checklist](license-audit-checklist.md)
- [Webfont embedding rights](webfont-embedding-rights.md)
- [Marketplace license models](marketplace-license-models.md)
- [Open Font License in practice](open-font-license.md)

Compiled 2025 as part of the Fontlore project.
