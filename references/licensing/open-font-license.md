# Open Font License in Practice

What this reference covers: How the SIL Open Font License 1.1 works when you actually use fonts: what you may do, the four obligations you take on, how Reserved Font Names work, bundling and selling rules, and the misunderstandings that cause most licensing arguments.

The OFL is the license behind most of the good free type in the world, from Google Fonts to SIL's own catalog. It is short, readable, and almost universally misquoted. This guide replaces folklore with the actual terms.

## What the OFL is

- The SIL Open Font License version 1.1 was written by SIL International, the language-development organization, and released in its current form in 2007.
- It governs the font software: the outlines, the tables, the code inside the file. It is not a design patent and it does not cover the abstract letterforms.
- Thousands of families ship under it, including nearly all of Google Fonts' catalog, SIL's fonts, and most independent open-source foundry work.
- The license text lives at openfontlicense.org and travels inside every OFL font package as OFL.txt; reading it once is a professional obligation.

## What you may do without asking anyone

- Use the fonts commercially, in any project, for any purpose, forever. There are no per-seat fees, no pageview tiers, no renewal dates.
- Install on any number of machines and distribute to any number of team members within your organization.
- Embed the fonts in documents (PDFs, ePubs), in applications, on devices, and serve them as webfonts, subject only to the license accompanying the distribution.
- Study the font files, modify them, subset them, rename them (with the RFN rules below), and build derivative designs.
- Bundle OFL fonts inside software you sell, as long as the fonts remain under the OFL and are not the thing being sold by themselves.

## The four obligations you take on

- Keep the license with the font: any redistribution of the font files must include the OFL text. A font shipped without its license is a broken distribution.
- Keep copyright notices: do not strip the copyright statements from the font's name table or license file.
- Respect Reserved Font Names: modified versions must not carry the original's reserved name (see the deep dive referenced below).
- Distribute modifications under the OFL: if you distribute a Modified Version, it must be licensed under the OFL too. The copyleft applies to font files, not to documents rendered with them.

## Reserved Font Names in brief

- The OFL header may declare one or more Reserved Font Names (RFNs). Anyone modifying the font must pick a new name that does not contain the reserved one.
- The RFN mechanism protects users from confused forks trading on the original's reputation; it does not restrict unmodified use in any way.
- Practical consequence for teams: if you subset or modify a font with an RFN and redistribute the result publicly, you must rename it. Internal use does not trigger this.
- The OFL FAQ at openfontlicense.org is the authoritative interpretation source and is genuinely readable.

## Bundling and selling

- You may include OFL fonts in paid products (apps, themes, templates, hardware) because the font is part of a larger work, not the item of sale.
- You may not sell the font files by themselves as your product; that would be resale, which the license forbids.
- Charging for delivery media, bundles, or services around the font (installation, support, customization) is permitted; the font itself stays free.
- Templates and design products that embed OFL fonts must carry the license and attribution notes for each font; make that a packaging checklist item.

## Common misunderstandings, corrected

- "You must credit the designer in your app's about page." False. The OFL requires keeping the license and copyright with the font files, not public attribution in your product UI.
- "OFL fonts cannot be used in logos." False. The license explicitly permits any use, including logo artwork.
- "Commercial use requires a paid upgrade." False for genuine OFL fonts; that pitch usually signals a trial license or an aggregator mislabeling a font.
- "Modifying an OFL font and shipping it violates the license." False if you follow the obligations: keep the OFL, keep notices, rename if an RFN exists.
- "Google Fonts CDN usage needs attribution." False legally; attributions are courteous, not required.
- "OFL is viral for my project." False. The copyleft attaches to modified font files, never to your documents, apps, or designs.

## Workflow

1. When adopting an OFL font, archive the OFL.txt and note the copyright line and any RFN declarations.
2. Record the exact license name (OFL-1.1) in the font manifest, never just "open source".
3. Plan redistribution: webfont subsets served from your origin are fine; public repos carrying modified files need the rename check.
4. For product bundling, add the license file to the package's legal directory with the other third-party notices.
5. Re-check RFN status before any public fork or redistribution of modified files.

## Common mistakes

- Shipping OFL fonts without the license file in the bundle or repository.
- Modifying a font with an RFN and redistributing it under (or containing) the reserved name.
- Confusing aggregator "free font" pages with OFL grants and skipping the source verification.
- Writing "Google Fonts license" into legal documents instead of naming the OFL, Apache, or UFL explicitly.
- Assuming an OFL font found on a random site is current; version and file verification is part of due diligence.

## Decision rules

- Any project needing free commercial use, embedding, and modification rights: OFL fonts are the default answer.
- Need to redistribute modified outlines publicly: check RFNs first, then rename and relicense correctly.
- Disagreement about an OFL clause: resolve it with the license text and the official FAQ, not with blog folklore.
- When a stakeholder asks "are we allowed to...?", the answer almost always begins with "yes, because the OFL permits...", with the four obligations checked.

## The license text, clause by clause

Reading OFL.txt takes five minutes and settles most arguments. Its structure, in order, with the parts teams actually trip over:

- The preamble states the intent: fonts released under it may be used, studied, modified, and redistributed freely, with protection limited to keeping the license intact and respecting reserved names.
- Numbered definitions follow: Font Software (the set of files released under the license, including source files, build scripts, and documentation), Reserved Font Name, Original Version, Modified Version, and Author (designers, engineers, programmers, technical writers, and other contributors).
- "Modified Version" is defined broadly: adding to, deleting, or substituting components in part or in whole, changing formats, or porting to a new environment all count. Subsetting counts. Publishing a woff2 conversion counts.
- The binding requirements: distribute copies bundled with the license and copyright notices preserved; do not use a Reserved Font Name for a Modified Version except to note its origin; do not sell the font files by themselves.
- The termination clause: "This license becomes null and void if any of the above requirements are not met." Breach converts an open font into an unlicensed copy; it is not a technicality.
- An as-is disclaimer with no warranty of any kind follows, which is why provenance and quality checks are the user's job, not the licensor's.
- Status notes worth recording: OFL 1.1 has been the current version since 2007 (there is no 1.2 to wait for), and it sits on the OSI list of approved open-source licenses, which settles "is this a real open-source license" in policy reviews.
- The official FAQ at openfontlicense.org supplements the text with worked interpretations and is maintained by SIL; when a blog post and the FAQ disagree, the FAQ wins.
- When citing the license in a manifest or NOTICE file, write OFL-1.1 and quote the copyright statement from the font's own OFL.txt rather than paraphrasing it.

## Worked example: shipping a paid template

A studio sells a website template bundling Inter, Literata, and JetBrains Mono, all OFL families. The licensing walk:

- Bundling is permitted: the fonts ride inside a larger work, and the template, not the fonts, is what the customer buys.
- Each font directory ships with its OFL.txt and copyright notices intact; the release checklist treats a missing license file as a ship blocker.
- The build pipeline subsets the webfonts. Subsetting deletes components, so a subset is a Modified Version under the license's own definition.
- Inter declares "Inter" as a Reserved Font Name, so the public template cannot carry a subset still named Inter. Options, in order of simplicity: ship the unmodified files with the license (no rename needed); rename the subset family to a string that does not contain "Inter" and update the name table, CSS, and docs; or skip bundling and instruct buyers to load the family from Google Fonts, which many template sellers do.
- Internal builds of the same subset need no rename, because use is not redistribution.
- Before generalizing the workflow, read each family's own OFL.txt: Reserved Font Name declarations are per font, and assuming they match across a bundle is how forks get published wrongly named.
- The verification step that catches most problems: unzip the shipped template and confirm every font directory contains its license, and that the family name inside each file matches the manifest.
- If the template later grows a "premium" variant that ships additional weights, the same obligations apply to the new files; the check belongs in the release checklist, not in memory.
- Documenting the decision (which fonts, which subsets, which names, which date) in the template's repo turns a future audit from an investigation into a lookup.

## Comparison table: folklore versus the license

| Belief | What the license actually says |
| --- | --- |
| "You must credit the designer in your app UI." | No public attribution is required; keep the license and copyright with the files. |
| "OFL fonts cannot be used in logos." | Logo use is permitted like any other use. |
| "Commercial use requires a paid upgrade." | No such tier exists; the pitch signals a trial or a mislabeled font. |
| "Modifying and shipping a build violates the license." | Allowed when the four obligations are met. |
| "The OFL is viral for my project." | Copyleft attaches to modified font files only, never to documents or apps. |
| "Google Fonts CDN usage needs attribution." | Not legally; courtesy only. |
| "Reserved names restrict who may use the font." | They restrict naming of modified versions, not use of the original. |
| "Selling a product that bundles OFL fonts is resale." | Bundling with a larger work is permitted; selling the files alone is not. |
| "A subset served from my own origin is a Modified Version I must rename." | Serving privately is use; public redistribution of the subset is the trigger. |
| "I must publish my design source files if I modify the font." | The OFL covers font software; nothing obliges releasing unrelated source. |
| "The OFL expires or needs renewal." | It is perpetual for the fonts it covers; there is nothing to renew. |
| "I cannot charge a client for work set in an OFL font." | Charging for design work is unaffected; only selling the font files alone is barred. |

## Field notes

- SIL's own catalog (Gentium Plus, Andika, Scheherazade New, Lateef, Harmattan) is the reference implementation of OFL hygiene: every download carries the license, and naming discipline is strict.
- The google/fonts repository carries each family's license text; when a downloaded archive arrives without OFL.txt, fetch it from there rather than from wherever the file came from.
- Some foundries publish custom OFL-based texts with one clause changed: extra naming rules, no-modification terms, or field-of-use limits. Those are not the OFL; read the whole document before writing "OFL-1.1" into a manifest.
- The license travels with the file: fonts copied onto a shared drive carry the obligation to keep the license text along, even inside one organization.
- Version 1.0 of the OFL exists historically and differs from 1.1; a file declaring 1.0 is legitimate but rare, and the difference is another reason to record the exact license identifier.
- Translations of the OFL exist for convenience, but the English text is the operative one; do not license-audit from a translation.
- The OFL governs font software, not names or designs: writing "set in Inter" in a book needs no permission, while shipping a renamed build of Inter does follow the RFN rules.
- Package managers show why the license travels: Fontsource npm packages include the license file, and a font dependency without one is a packaging bug worth reporting upstream.
- Teams adopting many OFL families should keep one canonical licenses directory rather than letting each product copy drift.
- When a stakeholder asks whether "open source" fonts are safe for a regulated product, the OSI approval and the license's fixed text are the answer; hand them the document, not a summary.
- The license's short text is a feature for audits: an auditor can read the whole grant in one sitting, unlike most commercial EULAs.

## Quick reference: the four obligations

1. Keep the license: any redistribution of the font files includes the OFL text.
2. Keep notices: copyright statements stay intact in the name table and the license file.
3. Respect RFNs: modified versions must not carry reserved strings, in whole or in part, except to note origin.
4. License modifications under the OFL: distributed Modified Versions are OFL fonts too.

Everything else people remember (about-page credit lines, paid upgrades, share-back duties for documents) is folklore, not license.

## Cross-references

- [OFL reserved font names](ofl-reserved-font-names.md)
- [License families compared](license-families-compared.md)
- [Open-source due diligence](open-source-due-diligence.md)
- [Google Fonts Catalog](../sourcing/google-fonts-catalog.md)

Compiled 2025 as part of the Fontlore project.
