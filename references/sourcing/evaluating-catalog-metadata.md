# Evaluating Catalog Metadata

What this reference covers: How to compare metadata across catalogs and packages, spot stale or wrong metadata, pin versions, and run a verification workflow against the Fontsource API and the google/fonts repository. It is the difference between "I found a font" and "I have evidence about this font."

Every catalog displays metadata, and every catalog gets some of it wrong: stale versions, wrong designers, missing axes, optimistic subset claims. Cross-checking three independent sources catches most of it in minutes.

## The fields that matter

- Version: the font file's internal version string, the npm package version, and the repository commit date. Three names for the same underlying fact, and they drift.
- License: the exact license name (OFL-1.1, Apache-2.0, UFL-1.0, ITF-FFL-1.0), not the word "free". The license determines every downstream decision.
- Designer and foundry: needed for credits, audits, and contacting humans. Verify against the foundry site or the OFL copyright line.
- Subsets and languages: what the family claims to cover. Cross-check against specimen glyphs, because listings overstate.
- Axes: for variable fonts, the declared tags and ranges. Compare against the font file's fvar table.
- Date fields: catalog date_added, npm publish dates, repository git dates. Freshness of metadata is itself a quality signal.

## Comparing across catalogs

- The same family commonly shows different versions on the Google Fonts site, in the google/fonts repo, on Fontsource, and on the foundry's own page. Differences of a minor revision are normal; divergent axes or weights lists are not.
- npm versions on Fontsource track upstream releases, so the npm changelog is a legitimate version signal for packaged families.
- Foundry-direct pages usually carry the newest version; catalogs lag by days or months. For commercial fonts, the foundry page is the version of record.
- Aggregator sites (blogs, free-font lists) almost never carry version data at all; that absence is the reason their links rot.

## Spotting stale or wrong metadata

- A family page whose described styles do not match the downloadable files (page lists 12 styles, download has 8) means the metadata or the files are stale; trust the files.
- Wrong or missing designer credits: cross-check the OFL copyright line and the foundry's site. Catalog typos propagate widely because sites copy each other.
- Variable flag mismatches: a site calling a family variable when only a subset of axes is served, or listing axes that the actual file lacks.
- Subset overclaiming: a family marked as covering a language where the specimens show missing diacritics or unshaped script behavior.
- Dead upstream links: a METADATA.pb or catalog entry pointing at a vanished repository means maintenance risk, and you should record that risk.
- License mislabels: "free for commercial use" pasted onto what is actually a trial or personal-use license. This single error causes most free-font incidents.

## Version pinning strategies

- npm: pin exact versions in package.json for font packages; a caret on a font dependency is an unreviewed glyph change waiting to ship.
- Self-hosted files: name files with the version (acme-sans-2.3.0.woff2) or keep a manifest mapping files to versions, sources, and dates.
- Record the version you approved in the design system's documentation; a review that approved version 2.1 should be re-opened when 2.4 lands.
- For CDN usage you cannot pin; that limitation is one of the strongest arguments for self-hosting in production.
- When upstream releases meaningful changes (new scripts, axis changes), schedule the upgrade as a visible design change, not a silent dependency bump.

## Verification workflow

1. Collect the claims: catalog page, package metadata (npm or API), and repository metadata (METADATA.pb or foundry release).
2. Compare version signals; note the newest and the one you actually deploy.
3. Compare weights, styles, axes, and subsets across all three; every mismatch goes into the notes.
4. Open the license file at the source (OFL.txt, LICENSE.txt, or the foundry's license PDF) and record the exact license name and any Reserved Font Names.
5. Spot-check rendering claims in specimens: weights that exist, diacritics that render, numerals that align.
6. Write the evidence record: sources, dates, versions, discrepancies, and the confidence level you can defend.

## Common mistakes

- Trusting one source because it is the most convenient; convenience is not corroboration.
- Recording "Google Fonts" as the license instead of OFL, Apache, or UFL.
- Comparing the CDN's current rendering against a pinned npm version and concluding the font "changed randomly".
- Ignoring date fields, then defending a decision with metadata two years older than the font.
- Copying catalog descriptions into internal docs instead of writing evidence-based summaries.
- Treating subset listings as verified coverage without opening the glyph grid once.

## Decision rules

- Two sources agree, third disagrees: investigate the third; do not average.
- Metadata conflict on license or designer: the license file and the foundry win over any catalog.
- Version conflict without explanation: assume the newest repository commit is current and treat others as lagging, but verify in the actual file.
- If verification takes more than a few minutes, the missing fact becomes a named task with an owner, not a footnote.

## Cross-check matrix

| Claim | Check it at | What confirms it |
| --- | --- | --- |
| License | OFL.txt or LICENSE.txt in the google/fonts directory, or the foundry's license PDF | Exact license name and any Reserved Font Name line |
| Version | Font file's internal version string, git log date, npm publish date | Three signals telling one consistent story |
| Designer | Foundry site plus the OFL copyright line | Agreement across both, not a catalog's typo |
| Axes | The font file's fvar table via a font inspector | Tags and ranges match the metadata claims |
| Subsets | The glyph grid of an actual shipped file | Real glyphs, not a list on a page |
| Language support | Specimen text in that language | Correct diacritics and shaped text, not a count |
| Variable flag | The served file, opened in an inspector | Declared axes exist in the file you deploy |

Any row that cannot be checked becomes a named risk in the record, not a silent assumption.

## Worked example: resolving a version conflict

Scenario: a team sees different kerning between the CDN version of a family and their pinned npm package, and someone claims "the font changed randomly".

1. Collect the three signals: the npm package version and publish date, the git log date of the family directory in google/fonts, and the font file's internal version string from the deployed file.
2. Compare axes and weights lists across sources; a missing axis or weight in one source usually explains the visual difference without any mystery.
3. Check the upstream release notes or issue tracker for the family; glyph and kerning fixes are usually documented somewhere between upstream and the packaging layer.
4. Conclude with a decision, not a shrug: pin both environments to the same channel and version, or accept and document the drift deliberately.
5. Write the incident into the font manifest so the next person knows the CDN and the npm package were on different revisions, and why the team standardized.

The resolution is always organizational in the end: one channel of record per family per product, and a review path for version changes.

## Signals to trust

- The license file read at the source, with the exact license name and Reserved Font Names recorded.
- Three-way agreement between repository metadata, package metadata, and the font file's own tables.
- Foundry-direct pages for commercial fonts; they carry the newest version and the authoritative scope.
- Dated evidence: records that say when each fact was checked.

## Signals to distrust

- Three sources agreeing when two of them copied the third; catalogs and aggregators syndicate descriptions widely, so apparent corroboration can be one claim echoed.
- "Free for commercial use" as a license name; it is a marketing phrase, and its most common referent is a trial license.
- Aggregator sites for version data; their absence of version information is the reason their links rot.
- Subset and language listings treated as coverage; listings overstate, specimens do not.

## Field notes

- Date fields deserve more attention than they get: a catalog page describing a family accurately but two years stale is still a liability during an audit.
- The npm changelog is the cheapest version proxy for packaged families; for unpackaged families, git log in the source repository does the same job.
- When a foundry and a catalog disagree on designer credit, the OFL copyright line usually settles it in one read.
- Keeping a three-column comparison (catalog, package, repository) as a screenshot with the date visible is a five-minute habit that rescues months-later arguments.
- Metadata quality tracks maintenance quality; families with sloppy metadata tend to be families with slow fixes, which is itself selection information.

## Questions to ask during verification

- Which of these sources is actually authoritative for this field, and does everyone on the team know that?
- What version is deployed right now, and can you name it without opening a ticket?
- If the license turned out to be different tomorrow, what breaks first?
- Which mismatch on this list blocks launch, and which is a documented quirk?
- Who signs off that the verification is complete, and where does the record live?

## Tool notes

- Font inspectors (fontdrop, Wakamai Fondue, or a desktop font inspector) read the deployed file directly, which is the only way to settle axes and version questions.
- `git log` against the google/fonts family directory gives the last-change date in seconds; it is the cheapest verification step in this entire reference.
- The npm CLI answers package-side questions locally: exact installed version, publish date, and file list without opening a browser.
- Keep a saved diff or side-by-side screenshot when versions disagree; the visual evidence is what persuades the meeting that "it looks the same to me" is not a resolution.

## Mismatch triage

| Mismatch found | Most likely cause | Action |
| --- | --- | --- |
| Version differs by a minor revision | Normal packaging lag | Note it; pin one channel of record |
| Weights list differs | Metadata stale or partial package | Trust the shipped file; file an issue upstream if wrong |
| Axes present in metadata, absent in file | Stale metadata or wrong file deployed | Re-verify deployment source immediately |
| Language listed but diacritics broken | Coverage overclaim | Record as risk; test with native reader before launch |
| License named differently across sources | Syndicated summaries | Read the license file; the file wins |

## Cross-references

- [The google/fonts repository](google-fonts-repository.md)
- [Fontsource REST API](fontsource-api.md)
- [Building a font shortlist with sources](building-a-font-shortlist-source.md)
- [Open-source due diligence](../licensing/open-source-due-diligence.md)

Compiled 2025 as part of the Fontlore project.
