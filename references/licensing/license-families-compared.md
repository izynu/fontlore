# License Families Compared

What this reference covers: The practical differences between the license families teams actually encounter: OFL, Apache 2.0, Ubuntu Font License, MIT-style permissive font licenses, and the ITF Free Font License. Each gets real examples and the consequences that matter in projects.

"Is it free?" is the wrong question. The useful question is "what may I modify, redistribute, and bundle, and what must I keep intact?" This guide answers it per license family, with fonts you will recognize.

A useful mental model: open-source families (OFL, Apache, UFL, MIT/BSD) attach duties to redistribution; free-use families (FFL) attach limits to use itself. Most licensing surprises come from treating a free-use font as if it were open source.

## The OFL

- The SIL Open Font License 1.1 is the dominant free font license: nearly all of Google Fonts, SIL's catalog, and most independent open foundries use it.
- Grants: commercial use, unlimited installation, embedding, web serving, modification, and redistribution, all free.
- Conditions: keep the license with redistributed files, keep copyright notices, respect Reserved Font Names for modified versions, and license modifications under the OFL.
- Character: permissive for users, mildly copyleft for derivative font files. Documents, apps, and designs rendered with the font are untouched.
- Examples: Inter, Source Sans 3, JetBrains Mono, Literata, Gentium Plus, Fraunces.
- The obligations are lightweight enough to satisfy in one step: keep the OFL.txt beside the files and check RFN status before any public modification, and you are compliant.
- Because the ecosystem is large, tooling assumes OFL by default: Fontsource, Google Fonts, and most audits treat it as the baseline case.
- For teams comparing candidates, an OFL font removes an entire procurement conversation that a commercial family would require.

## Apache 2.0 fonts

- Some major families ship under the Apache License 2.0 instead of the OFL: Roboto is the flagship example, along with Open Sans, older Noto releases, and the Arimo, Tinos, and Cousine metric-compatible set.
- Grants are similar in practice to the OFL for ordinary use: free commercial use, redistribution, and modification.
- Differences that matter: Apache carries an explicit patent grant and does not use the OFL's Reserved Font Name mechanism; renaming is still good practice for derivatives but is not a license requirement in the same form.
- Apache fonts also require preserving license and notice files on redistribution, and state changes in modified files.
- In practice most teams notice only one Apache difference: there is no Reserved Font Name check to run before publishing a modified build, which can lull OFL-habituated teams into skipping name hygiene that is still worth keeping.
- When mixing Apache and OFL fonts in one repo, per-directory license files prevent the two regimes from being averaged into "open source" in the README.
- Do not convert Apache to OFL in your records; the license identity matters for audits even when practical effects overlap.

## Ubuntu Font License

- The Ubuntu font family, designed by Dalton Maag, ships under Canonical's Ubuntu Font License 1.0.
- Grants free use, modification, and redistribution, with a renaming requirement for modified versions comparable in spirit to OFL Reserved Font Names.
- The UFL is font-specific and not one of the standard open-source licenses; some corporate policy lists flag it as non-standard, which matters in strict governance environments.
- Practical guidance: treat UFL fonts as free to use everywhere, but check your organization's open-source policy before redistributing modified versions.
- The UFL's renaming condition echoes the OFL's RFN mechanism, so teams that already handle OFL forks can apply the same habit.
- Ubuntu fonts embedded in Linux distributions travel far; a modified copy that leaks into a product needs the renaming treatment regardless of how it got there.
- Examples: Ubuntu and Ubuntu Sans family members; recent Ubuntu releases should be verified against the current license text.

## MIT and BSD-style font licenses

- Occasionally a typeface ships under MIT or a BSD-style license, mainly in developer-tool ecosystems; the Go fonts by Charles Bigelow and Kris Holmes are the classic permissive-license example (BSD three-clause).
- Grants are maximal: use, modify, sublicense, redistribute, with attribution kept in notices; no copyleft, no renaming regime.
- The practical risk is different: because such fonts often live in code repositories rather than foundry channels, provenance and version discipline are weaker; apply the open-source due-diligence workflow extra carefully.
- Treat MIT and BSD font licenses as equivalent to each other in practice; both are more permissive than the OFL.
- Because attribution lives in notice files rather than a dedicated license regime, teams used to OFL headers should add a "keep the LICENSE and any NOTICE file" step to their intake checklist for these fonts.
- Developer ecosystems frequently ship fonts under these licenses as part of larger tools; when you adopt the tool, adopt the font's license record too, or you will have a font in production with no entry in the register.

## ITF FFL

- The ITF Free Font License governs Fontshare fonts: free for personal and commercial use, with redistribution, resale, and most modification excluded.
- It is a free-use license, not an open-source license: you cannot legally push Fontshare files into public repos or fork the designs.
- Examples: Satoshi, General Sans, Switzer, Clash Display, and the rest of the Fontshare catalog.
- The FFL's no-redistribution clause has concrete consequences: no npm packages of the files, no CDN republishing, no committing them to public design-system repos, even with attribution.
- Fontshare's own delivery (their API and direct downloads) is the sanctioned distribution; linking to Fontshare rather than repackaging keeps the arrangement clean.
- Teams that love an FFL face but need redistribution rights should commission the foundry or pick the nearest open equivalent; the license is not negotiable per project.
- Record it explicitly (ITF-FFL-1.0) in manifests so nobody later "fixes" a repo by uploading the files somewhere public.
- The FFL also excludes most modification, so instancing, subsetting-for-publication, or customizing Fontshare files is out of bounds; private use without modification is the safe lane.
- When a client's brand guide mandates a Fontshare face, deliver usage guidance that says how the client may obtain the files themselves, rather than transferring files, which the license does not cover.

## Choosing by consequence

- Need to modify and redistribute font files publicly: OFL (with RFN care), Apache, MIT, or BSD; never FFL.
- Need to embed in shipped products: all of the above permit it; the difference is paperwork (OFL keeps license text; Apache keeps notices; FFL needs a closer read).
- Need zero governance overhead: OFL and Apache families from reputable sources win on documentation culture.
- Need a specific design only available under a restrictive free license (FFL): adopt it, but fence the files inside the organization and document why.
- Need fonts that can move between vendors and contractors without paperwork: OFL and Apache again; the license travels with the file by design.
- Need proof for a security or procurement questionnaire: permissive licenses with canonical sources produce evidence in minutes, which is part of the decision.

## Common mistakes

- Writing "open source" in the manifest for an FFL font; auditors and maintainers will treat it as redistributable.
- Assuming Apache and OFL are interchangeable in policy documents; name the actual license.
- Ignoring the UFL's non-standard status in organizations with strict open-source review.
- Treating MIT-licensed fonts found in random repos as trustworthy without checking upstream provenance.
- Copying license text from one font's repo into another font's directory; mismatched licenses are audit gold.
- Treating "the marketplace sells it, so it is licensed" as the whole answer; the marketplace summary describes scope, and the underlying license document still governs.
- Letting one product's font list be copied to a new product without re-running the eligibility check for the new distribution model.
- Describing licenses to stakeholders by nickname ("the Google Fonts thing") until nicknames harden into policy; use exact identifiers from the first mention.

## Decision rules

- Default to OFL when multiple candidates qualify; the ecosystem around it (tooling, docs, FAQ) is the strongest.
- For orgs with patent-sensitive legal teams: Apache 2.0 fonts have an edge; note it in the decision record.
- When the candidate is UFL or FFL: read the actual text once, store a copy with the files, and write one paragraph on allowed uses in the manifest.
- Never let a marketplace's marketing word ("free", "open") substitute for the license name in records.
- When a favorite font exists only under a restrictive family, mirror the decision logic above in writing: what was rejected, why, and which open alternative was chosen instead.
- Re-run the family comparison at major platform changes (new store, new console, new open-source release); license consequences change with distribution, not with design.

## Comparison table

| Family | Examples | Sell files alone | Modify and redistribute | Rename derivatives | Notes |
| --- | --- | --- | --- | --- | --- |
| OFL 1.1 | Inter, Literata, JetBrains Mono, Gentium Plus | No | Yes, under the OFL | Required when an RFN is declared | Keep license and notices with the files |
| Apache 2.0 | Roboto, Open Sans, Arimo, Tinos, Cousine | No | Yes, under Apache | Not a license requirement | Explicit patent grant; preserve NOTICE files |
| UFL 1.0 | Ubuntu family (Dalton Maag for Canonical) | No | Yes, with renaming | Required for modified versions | Non-standard; may trip policy reviews |
| MIT / BSD | Go fonts (BSD three-clause, Bigelow and Holmes) | Depends on the text | Yes | No regime | Provenance discipline is entirely on you |
| ITF FFL 1.0 | Fontshare catalog (Satoshi, General Sans, Switzer, Clash Display) | No | No | Not applicable | Free use only; no public redistribution or forks |

Read the table as grants plus duties: every family here is free to use commercially; what separates them is what you may do to the files and what must stay attached to them.

The rows that generate the most argument are the rename column and the redistribute column. Rename matters only when you modify and then publish; redistribute matters the moment files leave your control. A font can be free to use and still forbidden to republish, which is exactly the FFL row's shape.

## Worked example: one agency, three products

An agency runs client websites, a paid template product sold publicly, and an internal scheduling tool. The font list mixes license families, and each product treats them differently:

- Client websites: OFL families (Inter, Source Sans 3) go anywhere; Fontshare families (Satoshi, General Sans) are fine under the ITF FFL as long as the agency does not republish the files; Adobe Fonts-driven work stays inside the subscription.
- The paid template: OFL only. The template is redistributed to unknown buyers, which the FFL forbids and which no subscription covers. The manifest records OFL-1.1 per family, and the license files ship inside the package.
- The internal tool: the least constrained surface; FFL and subscription fonts are usable internally, but the team documents them anyway so that a future open-sourcing decision re-runs the check before, not after.
- When a client mandates an Apache-licensed family (Roboto for an Android-adjacent brand), the record says Apache-2.0, not OFL, because the audit compares records against files.
- A client in a strict open-source-review industry asks for Ubuntu Sans: the UFL gets read once, a paragraph on permitted use goes into the manifest, and legal signs off in writing.
- The recurring lesson: the product's distribution model, not the design brief, decides which license families are eligible.
- Pricing follows too: an FFL font is free to acquire but cannot be amortized into a redistributed product, so the "free" option can be the expensive one when the deliverable ships publicly.
- When two products share a font list but differ in distribution (internal tool and public template), keep two manifests; a shared manifest inherits the strictest product's constraints.
- Re-check family eligibility whenever a product changes hands: a template acquired by another company is still redistribution to unknown parties.

## Field notes

- License identity is also metadata: the name table carries license description and license URL fields (name IDs 13 and 14), and a mismatch with the shipped license file is a finding worth investigating rather than ignoring.
- Noto is the cautionary tale for era drift: older releases shipped under Apache 2.0 and newer ones under the OFL, so two Noto files from different years can carry different licenses while sharing a family name. Verify per file, not per family.
- SPDX identifiers (OFL-1.1, Apache-2.0, UFL-1.0, MIT, BSD-3-Clause) are worth adopting in manifests because package ecosystems and legal tooling speak them.
- The Liberation fonts are a documented relicensing case (historically GPL with a font exception, later the OFL); relicensed families are common enough that "it was always this license" is never an argument.
- The license text file in the package outranks the website summary, which outranks the marketplace badge, which outranks memory, in that order.
- Aggregators frequently mislabel license families; the aggregator saying "open source" about a Fontshare font is a documented, repeatable error.
- Subscription platforms obscure license identity: a font activated through a subscription has no file-level license document, which is why the subscription terms and entitlement records substitute for it.
- When a foundry offers both a free tier and a paid tier of the same family, the tiers are different licenses, not different prices for the same rights; record which tier each file came from.
- Fonts embedded in third-party components (UI kits, icon sets, HTML templates you bought) arrive with their own font licenses; your license families list must include what ships inside purchased assets.
- "Same family, two sources" (a GitHub repo and a foundry download) can mean two licenses or two versions; pin one source per family and document why.

## Questions to ask

- Which exact license document governs this file, and where does that document live in our records?
- Does our use involve modification, redistribution, or bundling? Each answer changes which families are even eligible.
- If we redistribute, what must travel with the files: license text, notice files, NOTICE entries, attribution notes?
- Does anyone in policy or legal treat the UFL or FFL as acceptable, and is that decision recorded somewhere better than a chat thread?
- For Apache fonts, is our notice handling (app about screens, documentation) actually preserving the required notices?
- If this font's project disappeared tomorrow, could we prove from our own records what we are licensed to do?
- When a family ships in multiple repositories or marketplaces, which source did our file come from, and does that source's license text match what we recorded?
- If legal rejects one family (the UFL, say), is there a documented open alternative ready, or does the roadmap stall?
- Who maintains this comparison as families relicense and platforms change terms, and how often is it re-checked?

## Cross-references

- [Open Font License in practice](open-font-license.md)
- [OFL reserved font names](ofl-reserved-font-names.md)
- [Open-source due diligence](open-source-due-diligence.md)
- [Fontshare and ITF free fonts](../sourcing/fontshare-and-itf.md)

Compiled 2025 as part of the Fontlore project.
