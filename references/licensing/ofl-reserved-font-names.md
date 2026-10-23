# OFL Reserved Font Names

What this reference covers: A working deep dive on Reserved Font Names under the SIL Open Font License: what the declaration means, exactly what it forbids and what it does not, how to name forks, and worked examples of getting it right and wrong.

Reserved Font Names are the OFL's single most misunderstood mechanism. The rules are short; the folklore around them is long. This guide keeps the rules and drops the folklore.

## What an RFN is

- An OFL copyright statement may include a line reserving names, in the form "Copyright 20xx The Example Authors, with Reserved Font Name Example."
- The reserved names belong to the original authors; the reservation tells everyone that modified versions may not use those names.
- The mechanism exists to protect users: a fork calling itself by the original's name would silently misrepresent its provenance and quality.
- RFNs are declared per font in its OFL.txt; check the file rather than assuming. Many major families reserve their names; Apache-licensed fonts (like Roboto) use no such mechanism at all.
- The declaration lives in the copyright paragraph, which is why reading the whole header matters; the reservation is easy to miss if you skim to the grant text.
- When a family reserves multiple strings, every one of them is off-limits for modified versions; check the list, not just the first name.
- The absence of an RFN declaration is itself information: modified versions may then keep the original name, though renaming remains courteous and clearer for users.

## What an RFN forbids

- Distributing a Modified Version under a name that contains the reserved name, in whole or in part. Prefixes and suffixes count: "Example Sans Pro" violates a reservation on "Example Sans".
- The restriction binds the font's name as users encounter it: the family name in the name table, the file names, and the public identity of the modified font.
- It applies to anyone modifying and redistributing; internal unmodified use never touches the mechanism.
- The trigger is distribution, and npm publish, CDN hosting for the public, and template marketplaces all count; a partner-only private registry is a gray zone best answered by the authors in writing.
- Modification includes deletions, not just additions: a trimmed subset is a Modified Version, which surprises teams who think of subsetting as extraction rather than authorship.
- It does not prevent you from modifying the font, subsetting it, or building on it; it only prevents borrowing the original's name for the result.

## What an RFN does not forbid

- Using the unmodified original under its reserved name in any project, commercial or not; the reservation constrains modified versions, not use.
- Mentioning the original font in documentation: describing your fork as "based on Example Sans" in the readme or copyright notice is accepted practice and what the license's attribution language anticipates.
- Using the reserved name to refer to the original in comparisons, reviews, and specimen discussions.
- Selling services or products around the font; the reservation is about the font's name, not about commerce.
- Keeping the original font installed alongside your fork; both can coexist as long as the fork carries its own name.
- Using the original's specimens or documentation as reference material for your fork's documentation, with attribution.

## Fork naming in practice

- Pick a clearly distinct name that does not contain the reserved string, and ideally signals the fork's purpose.
- Check the name table: the fork must carry the new name internally (family name in the name table), not just in filenames.
- Keep the provenance line: state in the copyright or readme that the font is a modification of the original, respecting the original's copyright and license.
- Rename consistently everywhere: file names, CSS font-family values, package names, and documentation.
- If the fork stays internal with no distribution, RFNs do not trigger; document that reasoning so the next maintainer does not rediscover it nervously.

## Worked examples

- If a font's header reads "with Reserved Font Name Meridian": a bug-fixed subset redistributed publicly must be renamed (for example "Meridian SF" fails; "Midline" works), must ship under the OFL, and should credit the original.
- If you subset an RFN font for web use and serve the subset from your own origin without distributing it as a font package (no public repo carrying the files), you are not redistributing a Modified Version in the triggering sense; internal serving is use.
- If your team forks a font for a custom corporate cut and the design system publishes that fork in an internal-only registry, document the nondistribution reasoning; if the registry later becomes public, the rename must happen first.
- Apache-licensed fonts (Roboto) have no RFN regime; renaming derivatives is courteous there, not required, which confuses people who apply OFL habits everywhere.
- A fourth case: merging two OFL fonts into one hybrid release. The result is a Modified Version of both, so every reserved name from both parents is off-limits.
- A fifth case worth writing down: translating a font's metadata or renaming files without touching outlines. If the font software itself changed (name table is part of it), treat it as modification; when in doubt, rename.

## Verification workflow

1. Read the OFL.txt of every font before modifying it; note any "with Reserved Font Name" line and the exact reserved strings.
2. Decide the distribution status of any modification: internal use, private serving, or public redistribution.
3. For public redistribution, choose and apply the new name across name table, files, CSS, and docs; keep the "based on" attribution.
4. Record the fork decision in the font manifest: base font, base version, modifications, new name, date, and who decided.
5. When in doubt about a specific clause, consult the OFL FAQ at openfontlicense.org or ask the original authors; their answer is authoritative and usually fast.
6. Re-run the check when the upstream font updates; new versions can change license headers, including RFN declarations.

## Common mistakes

- Renaming a fork "OriginalName Pro" or "OriginalName Alternative" and believing the suffix avoids the reservation; it does not.
- Stripping the copyright line while renaming, which violates the license independently of RFNs.
- Applying OFL renaming rules to Apache fonts (harmless but confused) or assuming Apache fonts have RFNs (they do not).
- Distributing modified files publicly without noticing the RFN because nobody read the license header.
- Overcorrecting: renaming fonts that were never modified, or refusing to redistribute unmodified OFL fonts out of misplaced fear.
- Updating the filename but not the name table, or vice versa; users see whichever record their tools read, and disagreement looks like corruption.
- Assuming a private npm registry is automatically outside the RFN's reach; distribution to third parties is distribution regardless of the door it uses.

## Decision rules

- Unmodified use: RFNs are irrelevant; use freely.
- Modified and redistributed publicly: rename fully, keep the license, keep attribution.
- Modified and kept internal: document the nondistribution reasoning; revisit if distribution status changes.
- Unclear whether a subset or patch counts as a Modified Version: treat it as one until the FAQ or the authors say otherwise; renaming is cheap, incidents are not.
- When forking for a client, put the naming decision and its rationale into the client-facing documentation; forks without visible reasoning attract audits.
- Prefer not modifying at all when the modification is cosmetic; an unmodified dependency is easier to maintain and entirely outside the RFN conversation.

## Comparison table: what an RFN touches

| Action | RFN applies? | Why |
| --- | --- | --- |
| Using the unmodified font in any project | No | Use is never restricted |
| Subsetting for your own site's private serving | No | Use, not redistribution |
| Publishing a subset or fork publicly under the same name | Yes | Modified Version carrying reserved name |
| Publishing under a distinct new name with OFL and attribution | No | The compliant fork path |
| Writing "based on Inter" in your fork's README | No | Attribution is expected, not forbidden |
| Selling a product that bundles the unmodified font | No | Commerce is not the subject |
| Renaming your fork "Inter Pro" or "InterCompat" | Violation | Reserved string contained in the new name |
| Apache-licensed fonts (Roboto, Open Sans) | N/A | No RFN mechanism exists there |

The table's edge cases are where audits go wrong: the violation is about the name string, and it triggers on public redistribution of modified files, not on use.

## Worked example: forking Inter

A product team needs a customized build of Inter: slightly heavier middots, a taller x-height override on digits, and a trimmed charset. The fork walk:

- Step one: read Inter's OFL.txt and note the Reserved Font Name declaration; the reserved string is "Inter".
- The build pipeline subsets and modifies the files for private serving inside the product; internal use triggers nothing, and the team documents that reasoning in the font manifest.
- A year later the team wants to publish the customized build as an npm package for a partner. Publication is public redistribution of Modified Versions, so the RFN rules engage.
- The team renames the family to a string that does not contain "Inter" (the name must change in the name table, not just in filenames), keeps the OFL license, and keeps an attribution line stating the font is based on Inter, respecting the original's copyright and license.
- CSS, package name, file names, and docs are updated to the new name in one commit; a grep for the reserved string verifies nothing was missed.
- The manifest records: base font and version, modifications, new name, date, decision owner, and the license text shipped with the package.
- The partner's audit later asks why the family name differs from the upstream project; the manifest's one-paragraph answer closes the question.
- The counterfactual: had the team published the build still named Inter, the package would have been a live OFL violation with a public paper trail.

## Tool notes: checking and changing names

- Read the RFN declaration from the font's own OFL.txt; it follows the copyright statement in the pattern "with Reserved Font Name ...".
- Inspect name records with FontDrop or with ttx: the family name (name ID 1), full name (ID 4), and PostScript name (ID 6) are the records users encounter.
- When renaming a fork, update all three records consistently, plus IDs 16 and 17 (typographic family and subfamily) where present; inconsistent records produce fonts that install under two names.
- fonttools can edit name records programmatically, which matters when a fork script must be repeatable; hand-edited name tables do not survive pipeline reruns.
- After renaming, render a specimen and check that the font installs and resolves under the new name in a clean environment; a rename that only lives in one record is a half rename.

## Field notes

- Many high-profile open families reserve their names (Inter does, Lato does), while some reserve nothing; the check is per font, never per reputation.
- The RFN mechanism protects users, not foundries' markets: a fork called by the original's name misrepresents provenance to people who chose the original in good faith.
- Renaming is cheap and incidents are not; when in doubt, treat a published modification as needing a new name until the OFL FAQ or the original authors say otherwise.
- Forks that stay internal need a note, not a rename; the note should say why distribution never happens, so the next maintainer inherits reasoning instead of anxiety.
- If you ask the original authors about an edge case, archive the reply with the font; their interpretation is the most authoritative one available.
- Corporate "brand cuts" of open fonts are the classic RFN case: legal as internal use, renamed when published, and undocumented at their peril.
- When upstream projects rename or rebrand, fork documentation should reference both the old and new reserved strings; the license history does not reset.
- The word "contains" is the whole test: if the reserved string appears anywhere in the new name, the reservation is engaged. Teams that grep for exact equality will miss it.

## Quick reference: the fork decision

1. Read the OFL.txt; list the reserved strings exactly.
2. Classify the artifact: use, private modification, or public distribution.
3. Private: document the reasoning, set a reminder to revisit if distribution changes.
4. Public: pick a name containing no reserved string, update name table, files, CSS, and docs.
5. Ship with the OFL text, the original copyright, and a "based on" attribution line.
6. Record base font, version, modifications, new name, date, and decision owner in the manifest.

Six steps, one grep, and the fork is clean; every RFN incident on record skipped at least one of them.

## Questions to ask before publishing a modification

- Does this font's OFL.txt declare Reserved Font Names, and which strings exactly?
- Is our artifact a Modified Version under the license's definition (subset, instance, conversion, merge)?
- Will the artifact be redistributed publicly, and under what name?
- Does the new name contain any reserved string, in whole or in part?
- Do the name table records, file names, CSS, package names, and documentation all carry the new name consistently?
- Does the distribution include the OFL text and the original copyright statement, with attribution noting the base font?

## Cross-references

- [Open Font License in practice](open-font-license.md)
- [Variable font licensing](variable-font-licensing.md)
- [Logos and trademark use](logos-and-trademark-use.md)
- [The google/fonts repository](../sourcing/google-fonts-repository.md)

Compiled 2025 as part of the Fontlore project.
