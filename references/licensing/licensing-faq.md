# Font Licensing FAQ

What this reference covers: The fifteen questions teams actually ask about font licensing, answered precisely with pointers to primary sources and honest notes on uncertainty. It is written for product teams, agencies, and freelancers who need a defensible answer today rather than a law review article.

## How to use this FAQ

- Answers are general guidance, not legal advice; for high-value or ambiguous cases, ask the foundry in writing and keep the reply as license evidence.
- "OFL" means the SIL Open Font License 1.1; the open-font-license reference analyzes the full text.
- Where practice varies across commercial foundries, the answer says so and names the clause to check in your specific license.

## The fifteen questions

### 1. Can I use this font on my client's website?

It depends on the license class and on whose name is on the license.

- OFL and other open licenses: yes, the client's site can serve the font with no further paperwork.
- Commercial webfont licenses are often sold to a single named entity; an agency purchasing on a client's behalf must either license in the client's name or confirm the license permits use for the benefit of a client.
- The test: whose site is it, and does the license name or expressly permit that entity?
- Record the license holder in the license register at handoff; the client-handoff-licensing reference covers the full pattern.
- When the license text is silent on client use, ask the foundry in writing before launch.

### 2. Do I need a license for a logo?

Yes. Rendering a logotype is a use of the font software, and it needs a license that covers logo use.

- Most desktop licenses include logo use; some foundries sell logo or exclusive-mark rights separately for prominent marks, and a few price logos above ordinary desktop use.
- OFL fonts carry no restriction: drawing a logo with an OFL font does not make the logo open source and creates no obligation to release anything.
- Converting the finished mark to outlines does not retroactively erase the need for a license to make it.
- Keep the license evidence with the brand assets; the logos-and-trademark-use reference has the details.

### 3. Can I embed fonts in a PDF I send to a printer?

OFL: yes, explicitly; embed subsets as usual. Commercial desktop licenses: usually yes, but verify first.

- Check the embedding clause in the license and the fsType embedding-permission bits in the font file.
- A PDF with embedded subsets does not require the printer to have the font installed.
- Send the PDF, not the editable source: handing the printer a live file with fonts is sharing font software and needs rights your license may not include.
- If the print workflow genuinely demands editable files, that transfer is its own licensing conversation with the foundry.

### 4. Can my developers install the font locally?

Commercial desktop licenses are seat-based, so count everyone who installs the font, including engineers.

- One seat per person who installs the font; developers who install it to build or run the product count.
- Build and CI servers that render text with the font (PDF generation, image services) typically need a separate server or application license; server-side rendering is a distinct licensing category, not a free extension of desktop seats.
- OFL fonts impose nothing: anyone may install and use them, including on CI.
- Practical rule: count engineering in the seat total at purchase time, not after legal asks; the desktop-and-app-licensing reference covers the seat math.

### 5. What does OFL actually allow?

The OFL is one of the most permissive licenses in use, with three firm limits.

- Allowed: use for any purpose, personal or commercial; study and modification; redistribution of originals and of modifications; embedding in documents and applications; bundling with software and products that you sell.
- Not allowed: selling the font files by themselves; using a declared Reserved Font Name for modified versions; redistributing with the license and copyright stripped.
- Modifications must be renamed when an RFN is declared, unless the holder grants written permission.
- Primary source: the OFL text itself and the official FAQ at https://openfontlicense.org; read both rather than trusting summaries, including this one.

### 6. Can I use an OFL font in a paid product?

Yes. The OFL explicitly permits selling apps, themes, templates, hardware, and any other product that bundles OFL fonts.

- The limits are narrow: the font file itself cannot be the thing you sell, you cannot present the font as your own work, and modified builds must respect Reserved Font Names.
- This is why OFL fonts are the safe default for commercial templates and app bundles.
- One nuance: "bundled with a product" covers distribution with your product; hosting the font as a standalone download for your customers to grab is a different use and deserves a second look.

### 7. Do webfont licenses expire?

Usually not by themselves, but they can die indirectly.

- Self-hosted webfont licenses are typically perpetual for the licensed version, domains, and pageview tier.
- Pageview tiers must be upgraded as traffic grows; entitlements bought through a subscription die with the subscription.
- Hosted services are the real expiry risk: when the subscription lapses, the service stops serving fonts, and the production failure mode is silent fallback to system fonts.
- Track renewal and expiry dates in the license register; the license-audit-checklist reference has the exact fields to log.

### 8. Can I convert a font to outlines?

Yes, but outlining does not remove licensing obligations; it only changes the artifact.

- Converting text to vector outlines is still use of the font software: the obligation sits with whoever creates the outlines.
- OFL: unrestricted.
- Commercial: outline and logo clauses vary, and a few foundries require separate logo licensing even for outlined marks.
- Outlining destroys hinting and editability, so embed rather than outline for documents.
- Outlining final packaging artwork is common print practice and is license-safe when the underlying license covers the use.
- Never treat outlining as a way to license after the fact.

### 9. Can I share font files with a freelancer?

Per-seat commercial licenses: generally no; OFL fonts: freely.

- The freelancer needs their own license for commercial fonts; some licenses permit contractors to install under the client's account, many do not.
- Emailing files "just for this project" is usually a breach, however normal it feels.
- OFL fonts: share freely, since the license travels with the file.
- Clean patterns: the freelancer buys their own seat and re-bills the client; or the collaboration runs on OFL equivalents until final production happens in-house under the proper license.
- The client-handoff-licensing reference covers contractor arrangements in depth.

### 10. What happens if I go over my pageview limit?

For self-hosted fonts, nothing technical, which is exactly why the limit gets missed.

- The tier is contractual, not enforced by the file, so exceeding it is a live breach you surface by upgrading.
- Hosted services vary: some bill overage automatically, some stop serving.
- Google Fonts serving has no pageview caps at all.
- Fix the process, not the incident: track traffic against licensed tiers with alert thresholds in the license register, and upgrade before the tier breaks rather than after.
- A breach discovered at renewal is negotiated from weakness; one discovered by your own monitoring is negotiated from a plan.

### 11. Can I use fonts in an email template?

Technically and legally, email is hostile territory for webfonts.

- Most email clients strip or ignore @font-face, so webfonts rarely render in email; body copy should use system font stacks regardless.
- Most webfont licenses cover serving from your web domains; embedding font files as attachments is distribution, which many licenses do not cover.
- Images of text are usually covered like any other graphic but carry accessibility costs and fail dark-mode testing.
- Check the license for an explicit email clause; when it is silent, use system stacks and put the question to the foundry in writing.

### 12. Can I bundle fonts in an open-source project?

OFL and Apache-2.0 fonts: yes. Trial and commercial fonts: no.

- Committing and redistributing open fonts is fine; your project's license (MIT, GPL, anything) does not apply to the font files, so keep the font's own license and copyright notice in its directory.
- If you modify and redistribute, follow the Reserved Font Name rules.
- Never commit trial or commercial fonts to a public repository: that is unlicensed redistribution with the repository history as evidence.
- Record every bundled family in the project manifest with its exact license; the open-source-due-diligence reference covers verifying what you bundle.

### 13. Is Google Fonts really free for commercial use?

Yes, with the caveats any free thing carries.

- Every family in the Google Fonts catalog is distributed under an open-source license, mostly OFL 1.1 with some Apache-2.0 and UFL.
- Free for commercial use, with no pageview caps, including serving from Google's CDN.
- The license still applies when you self-host: keep license texts and respect RFNs.
- A font that merely resembles a Google Fonts family but arrived from elsewhere has no such status.
- Verify any downloaded file against the google/fonts repository before treating it as covered; the due-diligence reference is the method.

### 14. What about fonts in videos?

Video titling is a distinct use category, and it is the one teams forget to clear.

- Many desktop licenses are silent on video or restrict broadcast-style distribution; some foundries include video in desktop, others sell separate video or broadcast tiers.
- OFL fonts have no restriction, including monetized video.
- For commercial faces, get the video use confirmed in writing before the title sequence is locked, because retrofitting rights after publication costs more.
- Static frames exported as images usually fall under normal graphic use; distributed moving text is the case that needs clearing.
- State the uncertainty in your notes until the foundry answers.

### 15. Who is responsible when a license is violated?

The licensee: whoever downloaded, installed, or deployed the font.

- In client work that usually means the client, though the agency can carry liability through its own contracts and conduct.
- "The freelancer supplied the file" is not a defense for the party using the font.
- Contracts should allocate the duties explicitly: designers warrant that fonts are licensed for the deliverable, and clients verify scope before launch.
- After a violation, remediation is usually retrospective licensing; willful or repeated infringement costs far more and reaches the brand, not just the budget.

## Decision rules

- If the license text does not explicitly grant a use, treat it as ungranted until the foundry says otherwise in writing.
- Open license beats interpretation: when a use case keeps generating questions, an OFL equivalent is often cheaper than the legal review.
- Uncertainty is recorded, never averaged: an answer with a named primary source outranks a confident-sounding guess from a forum.
- Any answer here that changes money or launch dates gets re-verified against the actual license document, not against this summary.

## Cross-references

- [The SIL Open Font License](open-font-license.md)
- [License families compared](license-families-compared.md)
- [License audit checklist](license-audit-checklist.md)
- [Open-source due diligence](open-source-due-diligence.md)

Compiled 2025 as part of the Fontlore project.
