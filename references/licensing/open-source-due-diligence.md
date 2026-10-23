# Open-Source Font Due Diligence

What this reference covers: Verifying that a font really is open source before it enters a project: locating the upstream source, reading the actual license file and copyright headers, cross-checking metadata against the Fontsource API, and spotting relicensed or abandoned families. Use it whenever a font arrives from any channel other than the primary source, and before any due-diligence or audit sign-off.

"Open source" is a claim until you have seen the license where it lives. Aggregators host stale, renamed, and sometimes illegally redistributed files; catalogs drift from upstream; families change licenses between releases. Thirty minutes of verification is what separates a font you can defend in an audit from a font you found somewhere once.

## Why provenance fails

- Aggregator sites and "free font" blogs repack files without license texts, strip the copyright entries from the name table, and serve years-old versions carrying obsolete permissions.
- Families move between licenses across versions: early Noto releases shipped under Apache-2.0 while later releases are SIL OFL 1.1, and the Liberation fonts relicensed from GPL with a font exception to OFL 1.1 at version 2.0.
- The practical consequence: verify the license of the exact version you deploy, not of the family in general.
- Projects go quiet: a family whose repository saw its last commit years ago and whose issues go unanswered has nobody to ask when a question appears later.
- Files get renamed and re-hosted: "Inter Regular free download" on a random CDN is evidence that someone uploaded a file, nothing more.
- Catalogs lag or lead upstream: Google Fonts and Fontsource are generally accurate, but both are packaging layers, and the authoritative source remains the upstream repository or the foundry page.

## The ten-minute pre-check

Before any deeper verification, four quick signals sort most candidates:

- Does the family appear in the google/fonts repository or in a foundry's own repository with a license file next to the fonts? If yes, proceed; if no, find out why.
- Does the file's name table carry a copyright statement matching a real designer or foundry? Blank or generic copyright strings are a red flag.
- Does the offered file format match the story? A "Google Fonts family" offered only as a zipped TTF on a download portal, with no repo link, is not established as that family.
- Does the claimed license class match the directory or package metadata? OFL claimed on a page while the package says "freeware" is a contradiction worth resolving before anything else.

These signals do not replace the steps below; they decide how much scrutiny each candidate earns.

## The three tiers of upstream evidence

- Tier 1, the repository. For Google Fonts families, the google/fonts repository (https://github.com/google/fonts) holds one directory per family under ofl/, apache/, or ufl/, each containing the font files and the license text shipped with them. For independent families, the designer's or foundry's own repository or website.
- Tier 2, the packaging layer. Fontsource npm packages and the Fontsource API (https://api.fontsource.org/v1/fonts) re-version upstream releases. Good evidence for what you will actually deploy; never the sole evidence for what the license is.
- Tier 3, mirrors and aggregators. Download portals, convenience CDNs, blog attachments. Not evidence at all; a font that only exists here fails due diligence.
- Rule: verify at tier 1, deploy from tier 2, never adopt from tier 3.

## Step 1: Find and verify the upstream source

- For a family in the Google Fonts catalog, open its directory in the google/fonts repository and confirm three things: the font files are there, the license text is there next to them, and the path prefix (ofl, apache, ufl) agrees with the license file inside.
- The path prefix is itself a license signal: ofl/ means SIL OFL 1.1, apache/ means Apache-2.0, ufl/ means the Ubuntu Font Licence. A mismatch between prefix and license file is a stop signal.
- For independent open families, find the designer's or foundry's own repository or website. Inter lives at https://github.com/rsms/inter and JetBrains Mono at https://github.com/JetBrains/JetBrainsMono; an active repository with tagged releases beats any catalog page.
- Prefer the foundry's own download over any mirror, including well-meaning ones.
- Record the upstream URL and the date you checked it; this becomes the first entry in the evidence chain.
- If a font's only home is an aggregator, treat provenance as failed and pick a documented alternative rather than negotiating with a copy.

## Step 2: Read the actual license and the copyright headers

- Open the license file shipped next to the fonts (OFL.txt, LICENSE.txt, or similar) and read it in full; OFL 1.1, Apache-2.0, and UFL are all short documents.
- Confirm the copyright statement names a real rights holder (a designer or foundry) and a year range plausible for the family's history.
- OFL check: the text should be the unmodified OFL 1.1 with the copyright block inserted.
- Note any Reserved Font Name declared in the copyright block; it constrains derivative versions later, and the ofl-reserved-font-names reference explains the rules.
- The canonical OFL text lives at https://openfontlicense.org; a modified OFL is not the OFL, so diff if in doubt.
- Apache-2.0 check: the full Apache license text, plus any NOTICE file shipped alongside.
- Inspect the font file's name table as well: the copyright and license entries inside the file should agree with the sidecar license. The inspecting-font-files reference covers how to read name tables.
- Disagreement between the file and the paper is a finding, not a technicality.
- A file with no license anywhere in the package is not open source, whatever the download page says.

## Step 3: Cross-check the Fontsource API and the package you will ship

- Query https://api.fontsource.org/v1/fonts?family=inter for a filtered list, or https://api.fontsource.org/v1/fonts/inter for a single font.
- Compare the response against what you verified upstream: subsets, weights, styles, category, and variable status should match file reality, not just marketing copy.
- The family id in the API matches the npm package suffix, so a clean match tells you the package you would ship (@fontsource/inter or @fontsource-variable/inter) exists and is maintained.
- Open the npm package itself: its metadata declares a license, and the package ships the license file, so a due-diligence pass can be run straight from the tarball when that is the delivery path.
- Handle mismatches deliberately:
  - If the API claims weights the upstream repository does not ship, trust the repository and record the discrepancy.
  - If the package lags a major upstream release, record the lag as a known limitation with a re-check date.
- Keep API checks reproducible: save the JSON response with its retrieval date next to the rest of the evidence.

## Step 4: Spot relicensed and abandoned families

- Compare the version you found against the version history. Where a license changed between releases (Noto and Liberation are the canonical cases), the version line in your manifest becomes the license line: pin it and record it.
- Check repository activity: last commit date, release cadence, and whether maintainers respond to issues.
- Silence for years is not automatically disqualifying, but it changes the risk profile and forces a substitution plan.
- Watch for quiet commercial pivots: a repository whose releases stop while a paid version appears on a foundry site means the free line may be frozen or deprecated.
- Look for takedowns: a family removed from a catalog (repository directories deleted, catalog pages gone) usually signals a rights problem. Do not adopt something catalogs are retreating from.
- For abandoned families you still want, remember what actually protects you: a fully licensed copy, with its license text, in your own repository.
- Openness is judged on the copy you hold, not on the project's future.

## Step 5: Document the evidence chain

Keep one manifest entry per family, in the governed location the audit checklist describes:

```
family: Inter
version_verified: 4.1
upstream: https://github.com/rsms/inter
accessed: 2025-01-15
license: SIL OFL 1.1 (copy stored at assets/fonts/inter/OFL.txt)
rfn: none declared
package: @fontsource-variable/inter, pinned to the validated version
verified_by: your name here
```

- Store the license text physically with the font files; a license that lives only in a bookmark is not evidence.
- Record Reserved Font Name status even when the answer is "none"; future forks depend on it.
- Add the Fontsource or npm version, so a dependency bump can be checked against what was verified.
- Include the verification date and the verifier's name; anonymous verification is unverifiable verification.
- For families with version-split licenses, record the version-to-license mapping explicitly, so a future bump cannot silently cross a license boundary.
- The test of the chain: a successor can re-walk every step without asking you anything.

## When provenance is unclear

- Stop before "cleaning up" the file. Fixing metadata on a font of unknown origin does not create a license; it destroys the only trail that existed.
- Check the identification references first: if the family cannot even be named with confidence, provenance is twice removed.
- Contact the plausible rights holder once, in writing, with a date-stamped copy of the question.
- No reply within the project's timeline counts as unresolvable.
- Replace with a documented open alternative; the sourcing references list equivalents by category, and the substitution should itself get a full due-diligence pass.
- Never ship an unclear font because a deadline is close. Emergency re-licensing under launch pressure costs more than any replacement.

## Workflow

1. Locate the upstream source (tier 1) and record URL and access date.
2. Read the shipped license and the name table; confirm they agree and name the license exactly.
3. Cross-check the Fontsource API or npm package against upstream facts; resolve mismatches toward the repository.
4. Check version history for license changes and repository activity for abandonment risk.
5. Write the evidence-chain entry into the manifest and store the license file with the fonts.
6. Only now does the family enter selection, handoff, or production.

## Common mistakes

- Trusting a download page's badge instead of reading the license file; badges are written by whoever uploaded the file.
- Verifying the family once and deploying different versions forever; versions carry licenses.
- Storing fonts without their license text, turning every future audit into a research project.
- Accepting "it was on Google Fonts" as provenance for a file that came from somewhere else entirely.
- Ignoring the name table because the sidecar license looked right; the two can disagree, and the disagreement is the finding.
- Treating a single verified download as a standing approval for later versions.
- Running the check informally with no record, so nobody can tell, a year later, whether it ever happened.
- Treating the Fontsource package as the license source of truth; the package is a copy, and copies inherit staleness.

## Decision rules

- No readable license at the upstream source: not open source, out.
- The shipped license text differs from the canonical text it claims to be: out until clarified with the rights holder.
- Provenance unclear after a bounded verification pass: replace the candidate with a documented open alternative.
- Upstream dead but license verifiable: usable, with a substitution plan and the copy-plus-license protection in place.
- Mismatch between catalog metadata and the repository: the repository wins, and the discrepancy is noted in the manifest.
- Every production font ships with its license file; a font without its license in the repository is an audit finding, not a formality.

## Cross-references

- [The SIL Open Font License](open-font-license.md)
- [License audit checklist](license-audit-checklist.md)
- [Free font risks](free-font-risks.md)
- [Research workflow](../workflow/research-workflow.md)

Compiled 2025 as part of the Fontlore project.
