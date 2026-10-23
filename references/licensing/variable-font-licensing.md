# Variable Font Licensing

What this reference covers: Licensing notes specific to variable fonts: whether variable and static builds differ legally, what counts as a modification when you generate instances or subsets, how commercial foundries price variable families, and the pitfalls teams hit when shipping variable builds.

Variable fonts complicate licensing less than people fear and more than people hope. The file format changes; most license logic does not. The interesting cases are instances, subsets, and commercial pricing.

## The baseline: same license, different artifact

- For open fonts, the license covers the font software regardless of file format: an OFL variable font and its OFL static siblings are the same grant.
- A variable font is one file with many instances inside; licensing it is not "licensing all the styles" in a way that differs from buying the static set under an open license.
- Google Fonts serves variable builds under the same OFL terms as static builds; nothing special is happening legally.
- Commercial foundries treat variable builds as a licensing product decision: some include VF files in standard licenses, some price them as a superset; check the family's license options rather than assuming either way.
- When a foundry's license text predates variable fonts, the silence is ambiguity, not permission; modern foundry pages usually state VF coverage explicitly.
- Record in the manifest whether the deployed file is a VF or statics; audits ask, and the file's fvar table is the answer.

## When instances become modifications

- Generating static instances from an open variable font (freezing weights with a tool) creates derived font software.
- If you keep the instances internal (render your app's weights at build time), you are using, not redistributing; open license obligations are minimal.
- If you redistribute the instances publicly (a repo, an npm package, a design resource), you are distributing Modified Versions: the OFL requires the license, the notices, and a rename if the font reserves names.
- Subsetting is the same story: subsetting a variable font for web use and serving it privately is use; redistributing the subset publicly is distribution of a modification.
- Practical rule of thumb: private pipelines are free; public redistribution inherits the full OFL obligations.
- Instancing tools vary in how they write name tables; validate the output's name records before treating the instance as final.
- Keeping a private instance pipeline has a maintenance cost: regenerated instances must be re-validated on every upstream update, which is a recurring review task, not a one-time setup.

## Web serving and CDNs

- Serving variable fonts from your origin under an open license is ordinary use; scope worries from commercial webfont licensing do not apply.
- Commercial variable fonts: webfont licenses cover the variable file the same as statics in most modern foundry licenses, but older license texts predate variable fonts; when the text is silent, ask.
- Pageview tiers do not change because the file is variable; the tiers count pages, not files.
- Some foundries license per-axis ranges (for example, weight range only versus full opsz range); verify which portions of the VF your license covers.
- Serving a VF with more axes than the license covers is a scope breach even if the UI uses only the covered axes; trim the file or extend the grant.
- The pageview tier question interacts with unicode-range subsetting: sliced variable files are still the same license object, sliced for delivery, not for rights.

## Commercial pricing patterns

- Many foundries price a variable font as equivalent to (or slightly above) the full static family, reflecting that it contains everything.
- Some price by style count within the VF's range; buying a VF and using two instances can cost more than buying two static styles, which makes the static route rational for narrow needs.
- Enterprise deals increasingly prefer variable builds for their file-management simplicity; negotiate the VF explicitly in the contract rather than assuming it rides along.
- Trial and early-access variable fonts carry the same trial restrictions as statics; VF trials are still trials.
- When comparing static versus VF pricing, compare entitlements, not file counts: the VF may include weights and axes your static purchase would never cover.
- Enterprise agreements increasingly treat VF files as the default deliverable; ask for explicit VF language even when the salesperson says it is included.

## Technical pitfalls with licensing consequences

- Instancing tools sometimes alter name tables; check that redistributed instances carry correct license metadata and renamed families where RFNs apply.
- Subsetting can drop the license-friendly name table entries if done crudely; validate after processing.
- Repackaging variable fonts into formats (woff2) is still redistribution of the font software when published; the same obligations apply as for any file.
- App bundles: a VF inside an app is embedding; the same app-licensing logic applies as for statics, with open fonts staying simple.
- Version pinning: variable fonts update as one file, so a dependency bump can change every instance at once; treat VF updates as family-wide design changes in review.
- Subsetting variable fonts interacts with the license question: a subset for private serving is use, while publishing the subset is modification, and the subset may also drop feature tables the license assumed you would keep.
- Keep the processing recipe (tools, flags, versions) in the manifest; license questions about processed files are answerable only with the recipe.

## Workflow

1. Record whether each adopted family is used as a VF, as instanced statics, or both, and keep the pipeline documented.
2. For open fonts: note RFN status before any public instance or subset redistribution; rename when required.
3. For commercial fonts: confirm the license covers the VF explicitly, including axis coverage if ranges are licensed separately.
4. Validate processed files (instanced, subsetted, converted) for intact license and name metadata before publishing anywhere.
5. Treat VF dependency upgrades as design-visible changes in the release process.

## Common mistakes

- Assuming a public npm package of self-instanced statics needs no license attention; it is a Modified Version distribution.
- Subsetting an RFN font for a public repo without renaming.
- Buying a static style set and shipping the VF file in an app because "it came with the download".
- Ignoring per-axis commercial licensing and using axes the entitlement does not cover.
- Letting one VF upgrade silently change dozens of rendered weights in production.

## Decision rules

- Public redistribution of any processed open font: run the OFL obligations checklist (license, notices, rename on RFN) before publishing.
- Commercial VF in production: explicit VF coverage in the license or a written foundry answer; silence is not coverage.
- Pipeline choice (instance at build time vs ship the VF): a technical decision, not a licensing one, for open fonts; for commercial fonts, check both paths' coverage.
- Any doubt about whether processing counts as modification: it does; act accordingly.

## Comparison table: artifacts and obligations

| Artifact | License view | Obligations when public |
| --- | --- | --- |
| Unmodified VF served from your origin | Use of the font | None beyond license retention for open fonts |
| Unmodified VF bundled in an app | Embedding | App-licensing logic for commercial; retention for open |
| Static instances generated at build time, kept private | Use | None |
| Instances or subsets published (npm, repo, template) | Modified Version distribution | OFL license, notices, rename if RFN |
| Subset with trimmed GSUB/GPOS | Modified Version | Same as any published modification |
| woff2 conversion published | Modified Version | Same obligations; conversion changes nothing legally |
| Commercial VF with licensed axis ranges | Contract scope | Use only the axes and ranges entitled |

The table's core message: the variable format does not create a new licensing category; the modification and redistribution questions are the same as they ever were, with more ways to modify.

## Worked example: the public npm package

A platform team maintains a public npm package of webfonts for partner sites. One family is an open variable font with a declared Reserved Font Name. The walk:

- The team's first instinct was to publish instanced statics (400, 500, 700) generated from the VF; a check against the license showed that publishing instances is publishing Modified Versions.
- The pipeline was rebuilt around three compliant options: publish the unmodified VF as-is (no rename needed), publish renamed instances with the OFL and attribution, or point users to the upstream package and vendor nothing.
- The team chose shipping the unmodified VF: one file, no rename, no maintenance of a derivative, and partners get continuous weights.
- Size was checked against the alternative: the VF was acceptable for the use case, and the subsetting that would have saved kilobytes would have created a rename obligation for marginal gain.
- The package's README documents the license, the upstream project, and the decision not to modify; the manifest mirrors it.
- When the upstream font released a new version, the team diffed axes and metrics before bumping, because one file updates every partner at once.
- The decision record ends with the general rule the team adopted: never publish a modified open font under its reserved name, and prefer not modifying at all.
- Size verification was done with real network numbers, not the file's disk size; the served woff2 was the number that mattered.
- The package also ships the upstream license file and a provenance note, so partner audits find their answers inside the package instead of filing questions.
- When a partner requested a trimmed subset, the team declined to publish it and instead documented the private-subsetting recipe the partner could run themselves; the line between use and distribution stayed clean.

## Questions to ask

- Does our license explicitly cover the variable file, or does the text predate variable fonts and stay silent?
- If the foundry licenses axis ranges separately, which ranges are we entitled to, and are we using only those?
- Are our instancing and subsetting tools preserving the name table and license metadata we depend on?
- Does any public surface (npm, CDN, template marketplace) receive modified artifacts of open fonts?
- When the VF updates upstream, what is our review process for a file that changes every rendered weight at once?
- For commercial VFs in apps, does the embedding grant name the variable file explicitly?

## Field notes

- Foundry pricing for variable families varies more than any other licensing dimension: full-family pricing, per-style pricing, and per-axis pricing all exist; read the family's actual license options page before comparing quotes.
- Per-axis licensing is the case that catches teams: a license covering wght does not automatically cover wdth or custom axes.
- VF trials are still trials; the format does not soften restrictions.
- A VF dependency bump is a design event wearing a version number; route it through the same review as any family-wide change.
- When packaging open VFs, unmodified shipping is almost always simpler than instancing, and it keeps you outside the RFN conversation entirely.
- If your pipeline instances VFs at build time, log the tool and version in the manifest; instancing behavior differs between tool releases, and reproducibility is part of license hygiene.
- For open VFs with RFNs, the cheapest compliant public artifact is the unmodified file; every processing step you add moves you toward the rename conversation.
- Licenses that name axis ranges should be checked at renewal; entitlements written before an axis existed may not cover it.
- The registry of truths for a VF project is short: the fvar table (what axes exist), the license (what axes are granted), and the manifest (what we shipped). When the three disagree, the license wins.

## Quick reference: the compliance walk for processed VFs

1. Classify the artifact: unmodified file, private instance, or public derivative.
2. Private artifact: document the pipeline and move on.
3. Public derivative of an open font: check RFNs, rename if declared, keep the OFL and attribution.
4. Public artifact of a commercial font: confirm the license covers the artifact class explicitly, in writing.
5. Validate name tables and license metadata after every processing step.
6. Record tools, versions, and recipes in the manifest so the walk is repeatable.

Teams that internalize the walk stop treating variable fonts as a licensing mystery; the format added axes, not exemptions.

## Cross-references

- [OFL reserved font names](ofl-reserved-font-names.md)
- [Open Font License in practice](open-font-license.md)
- [License families compared](license-families-compared.md)
- [Variable fonts and axes](../technical/variable-fonts-and-axes.md)

Compiled 2025 as part of the Fontlore project.
