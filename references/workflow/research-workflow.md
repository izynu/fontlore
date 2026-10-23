# Research Workflow

What this reference covers: A structured research process for font selection: where to search (catalogs by type), how to gather evidence from real-world usage, and how to verify metadata against primary sources. Research is where taste gets evidence; without it, selection is vibe-driven and unrepeatable.

## Search in three layers

Layer 1, catalogs by need:

- Open web fonts: Google Fonts (largest, per-subset labels, language filters), Fontshare (ITF's quality free tier), Font Squirrel (curated free-and-clear), the Fontsource catalog for npm delivery.
- Script-specific needs: Noto's catalog and SIL's language-oriented families for breadth; regional catalogs for depth.
- Commercial: MyFonts and the foundries themselves (Klim, Colophon, Grilli, DJR, Rosetta, Typotheque, and so on) for quality ceilings and precise licensing.
- Search by what the project needs: script coverage first, then classification and weight range, then personality. Reverse order produces dead ends.

Layer 2, evidence of real-world use:

- Fonts In Use documents real projects across media with searchable type credits; it answers "what does this face look like in a dense editorial layout" better than any specimen.
- Typewolf curates site picks and pairings; useful for seeing web rendering at various sizes and for pairing conventions.
- Foundry "in use" pages and type specimens from design studios show disciplined application.
- Look for use in contexts resembling yours: a face proven in dashboards is evidence for dashboard work; a face proven in fashion editorials is not.

Layer 3, the foundry and author:

- The foundry's own pages carry the truth about versions, axes, language support, and licensing; every aggregator is a copy that can be stale.
- Designer and author context matters for open fonts: an actively maintained GitHub repository with recent commits is a different risk profile than a 2015 release with no issues answered.

## Verification against primary sources

Catalog metadata drifts; verify before shortlisting:

- Weights and styles claimed versus shipped: count the actual files.
- Language support claimed versus subset labels versus cmap reality; the testing reference has the method.
- Version numbers: name table in the file versus the foundry page versus the GitHub release; mismatches explain mysterious rendering differences.
- License text: read the actual OFL or commercial terms from the foundry, not a summary; record the URL and date accessed in your notes.
- Variable axes claimed versus present in the file (Wakamai Fondue or FontDrop confirms in a minute).

## Recording research

Keep a research log that future-you (and the audit) can read:

- Per candidate: name, author/foundry, license with URL, version, formats available, script coverage found, evidence links (Fonts In Use entries, live sites), and one paragraph of assessment against the constraint sheet.
- Record where you found it, not just what you found; provenance is what separates research from bookmarking.
- Mark verification status per fact: verified (primary source), claimed (catalog only), unknown. Unknowns become verification tasks, not assumptions.
- The log feeds the shortlist and later the decision documentation; nothing in the final decision should lack a source.

## A concrete pass in one afternoon

1. Re-read the constraint sheet; write the hard filters (scripts, license class, budget) at the top of the doc.
2. One hour: sweep the relevant catalogs with the filters; collect 15 to 25 candidates with links.
3. One hour: for the survivors, check primary sources (foundry page, repo, license text) and kill anything that fails verification; expect to lose a third.
4. One hour: gather evidence (Fonts In Use, Typewolf, live sites) for the remaining 8 to 12; note rendering contexts.
5. Write the log entries; hand the shortlist (aim for 5 to 8) to the comparison workflow.

## Common mistakes

- Searching Google Images for "best fonts" and landing on aggregator or pirated-font sites; provenance unknown means provenance failed.
- Trusting subset labels and language-support claims without opening the file; the testing reference exists because labels lie by omission.
- Recording nothing: the shortlist becomes unreproducible and the decision undocumented.
- Treating a font's popularity (top-ten lists) as evidence; popularity is context-free, your constraint sheet is not.
- Skipping commercial options because "open is fine"; the budget line exists to be used, and the right commercial face often costs less than a day of engineering a workaround.
- Researching the display face first; the text face carries the product and should be researched first.

## Decision rules

- A candidate with no verifiable primary source: out. Availability is not provenance.
- A candidate that fails one hard constraint from the sheet: out, recorded with the reason; beauty does not reopen a closed gate.
- Two candidates equally evidenced: prefer the one with active maintenance and a version history.
- Evidence found only in contexts unlike yours: downgrade to "possible, unproven for this use" and test harder in the comparison phase.
- Research time-boxed: if the sweep has not produced 5 to 8 viable candidates, the filters are wrong; revisit the constraint sheet, not the search patience.

## Quick reference: source tiers

| Tier | Sources | What they can evidence |
| --- | --- | --- |
| 1, primary | Foundry pages, upstream repositories, license files, the font file itself | Versions, axes, license terms, true language support |
| 2, curated | Open Foundry, UNCUT, Typewolf, Fontshare, Font Squirrel | Existence, quality signal, upstream links |
| 3, catalogs | Google Fonts, Fontsource, MyFonts | Distribution, subsets, popularity; metadata needs checking |
| 4, commentary | Fonts In Use, blogs, Fontesk | Real-world context; never license or version facts |
| 5, unverified | Aggregator scrapes, image-search results, download sites | Nothing; presence here is itself a finding |

Record a fact's tier with the fact: "Literata, OFL" is a tier 1 claim only after reading the license file, and stays tier 3 hearsay until then. Every fact in a decision record must trace to tier 1 or 2.

The tiers also price research time honestly: a tier 1 verification costs minutes, while a tier 3 guess can cost a release. When a fact matters to the decision, walk it up the tiers before it is used, not after it is challenged.

One habit ties the tiers together: record how you found each source, not just the source. The path that located a foundry page (which catalog linked it, which search phrase worked) is reproducible knowledge; the bare URL is not.

## Worked example: one research log entry

A real entry, produced by the log template above:

- Family: Literata. Author: Veronika Burian and Jose Scaglione, TypeTogether. Found via Google Fonts, then traced upstream to TypeTogether's own Literata pages.
- License: OFL 1.1, verified from the license file shipped with the release; URL and access date recorded.
- Version: the Google Fonts build and the foundry build differ in packaging; the foundry page is the version of record for retail files, and the Fontsource build noted separately.
- Formats and axes: woff2 statics plus a variable build carrying optical size and weight axes, confirmed by opening the file rather than by the catalog listing.
- Coverage: Latin plus Cyrillic and Greek subsets per the foundry's documentation; Vietnamese confirmed in the file itself.
- Evidence of use: designed as the default reading face for Google Play Books, exactly the long-form reading context the project needed; recorded as tier 4 context, with the commissioning fact cited from TypeTogether's own case study.
- Assessment: fits the constraint sheet (open license, reading-optimized, true italic, variable optical size for size-tuned rendering). Risks: less distinctive than editorial serifs at display sizes. Verdict: enters the shortlist for body face. Verification status: verified.
- Time cost: fifteen minutes including the file inspection.
- Weights and styles: statics at 400, 500, 600, 700 plus true italics verified by opening the files; the variable build's optical-size behavior at text sizes converted into a comparison-phase test rather than assumed.
- Open question: whether the npm/Fontsource build stays pinned to the same version as the self-hosted files; assigned to engineering as a verification task.
- Red flags: none blocking; noted that stale copies of the family circulate on aggregator sites, which is exactly why the foundry page was made the version of record.

The entry took fifteen minutes because the layers were searched in order; the same entry attempted from an image-search result would have started at tier 5 and cost an hour to confirm or disprove.

The log holds the failures too, which is what makes it research: a later candidate, a lively display serif, died at the hard filters (no precomposed Vietnamese, no true italic) after thirty minutes, and its entry records the two gate failures and the date. Six months later the same face resurfaced in a stakeholder pitch, and the entry ended the conversation in one line.

## Field notes: research habits that pay off

- Bookmark release pages, not marketing pages: the release page carries the version history, and the version history predicts the foundry's maintenance habits.
- Read a candidate's repository issues before adopting an open font: shaping bugs and missing-glyph complaints surface there months before they surface in your QA.
- Record the date accessed next to every URL; catalogs change, and an undated claim is unreproducible in an audit.
- Search the family name plus the word "variable" before assuming a family is static-only; many older favorites gained variable builds quietly.
- When a foundry page and a catalog disagree, note both readings; the disagreement itself is information, and it usually means the catalog caches an old release.
- Time-box the evidence layer: three context-relevant Fonts In Use entries are enough to enter the shortlist; reading every entry is a rabbit hole.
- Keep the log as you search, not after: retroactive logs are where provenance gets invented.
- Verify the italic before the shortlist: synthesized obliques pass catalog listings and fail editorial briefs; open the italic file.
- Read the foundry's changelog or release notes; version notes such as "improved Vietnamese diacritics" are free evidence about the maintainers' priorities.
- When the only copies of a face live on download sites, search the family name plus "OFL" or "github"; the upstream is usually one page away, and adopting a site copy adopts whatever was done to the file.
- Check the file's name table for version and copyright strings; mismatches against the listing reveal re-packaged or modified copies.
- Screenshot or archive the foundry page at research time; pages move, and the evidence record should survive the move.
- Track the search phrases that worked in a scratch file; the second sweep starts from proven queries instead of cold guesses.
- When a foundry offers both retail and open versions of a family, note which build the project actually tested; the two are not always identical.
- For open fonts, glance at the repository's recent activity (commits, merged issues); it is the fastest maintenance signal research can buy.
- Verify claimed variable axes in the file itself; catalogs describe axes that some builds lack, especially older releases reissued as variable.

## Audit checklist: candidate admission to the shortlist

- [ ] Primary source located: foundry page or repository, with URL and access date recorded.
- [ ] License class verified from the license file itself; Reserved Font Names noted if OFL.
- [ ] Version recorded from the file or the release notes.
- [ ] Each hard constraint from the sheet checked and marked pass or fail with evidence.
- [ ] Claimed language support checked in the actual file (cmap or a test render), not from the listing.
- [ ] At least one evidence-of-use link in a context resembling the project's.
- [ ] The log entry names fit, risks, and tuning needs, not just impressions.
- [ ] Verification status marked (verified, claimed, unknown) per fact; unknowns converted to tasks.
- [ ] The italic file opened and confirmed as a true italic wherever italics are in scope.
- [ ] The candidate answers at least one named constraint from the sheet; no candidates collected "for later".
- [ ] How the candidate was found is recorded, not only where it lives.
- [ ] Any fact still at tier 3 at shortlist time carries an explicit verification task with an owner.
- [ ] The name table's version and copyright strings match the claimed version.
- [ ] Log entries dated; the shortlist notes which entries are current and which are stale.
- [ ] The entry names what would change the verdict (a new version, a license change, a new market).
- [ ] The shortlist handed to the comparison workflow carries only entries whose facts are verified or explicitly flagged.

## Cross-references

- [Brief to constraints](brief-to-constraints.md)
- [Testing and comparing shortlists](testing-and-comparing-shortlists.md)
- [Inspecting font files](../technical/inspecting-font-files.md)
- [Keeping current safely](keeping-current-safely.md)

Compiled 2025 as part of the Fontlore project.
