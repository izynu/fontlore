# The google/fonts Repository

What this reference covers: How to use github.com/google/fonts, the canonical source repository behind Google Fonts, for verification and deeper research. It covers repository layout, METADATA.pb files, license files, the axis registry, and how to trace a family back to its upstream source.

The google/fonts repository is where the Google Fonts catalog actually lives. When a catalog page, an npm package, and a repository disagree, the repository is the arbiter. Reading it fluently turns vague "I found it on Google Fonts" claims into verifiable evidence.

## Repository layout

- Families are organized into top-level directories by license: ofl/, apache/, and ufl/. The directory a family sits in already tells you its license.
- Each family gets one directory containing font binaries (TTF, including variable builds), a METADATA.pb file, a DESCRIPTION.en_us.html, and license text such as OFL.txt.
- Variable fonts are stored as single files with axis tags in the filename, for example a family name followed by wght or wdth,wght in brackets.
- Git history is meaningful: blame and log on a family directory show when glyphs, axes, or metadata last changed. This is the version signal the website itself does not surface.
- The repository tooling (Apache 2.0) is separate from the fonts' licenses; the fonts remain under the license in their directory.

## METADATA.pb fields

Every family directory carries a METADATA.pb, a protobuf-text file with the family's catalog metadata. Fields worth reading:

- name: the family name as served by the catalog. Mismatches between this and the font's internal name tables are a red flag.
- designer: the credited designer or designers. Often a foundry name rather than an individual.
- license: ofl, apache, or ufl. This should match the top-level directory and the LICENSE file present.
- category: the catalog bucket (Serif, Sans Serif, Display, Handwriting, Monospace). Trust it no more than the website's bucket.
- date_added: when the family entered the catalog. Useful for separating veterans from newcomers.
- subsets and languages: coverage declarations. Newer entries favor language lists; older ones list legacy subset names.
- axes: for variable families, the axis tags, ranges, and default values. Compare against the font file itself when the numbers matter.
- Some entries include a source block with an upstream repository URL, which is the fastest way to find the foundry's own project.

## License files

- OFL families carry OFL.txt with the full Open Font License text, including copyright line and any Reserved Font Name declarations. Read it, do not assume.
- Apache-licensed families carry LICENSE.txt (Apache 2.0). Roboto is the classic example of an Apache family in the collection.
- Ubuntu family fonts sit under ufl/ with the Ubuntu Font License text.
- The copyright line inside OFL.txt tells you who to credit in legal-file inventories and who holds the rights you are relying on.

## The axis registry

- Registered axis tags live in the googlefonts/axisregistry project: wght, wdth, opsz, slnt, and italic are the core set, each with defined ranges and fallback names.
- Custom axes use uppercase four-character tags chosen by the designer, like SOFT and WONK on Fraunces. They are legal but less portable across tooling.
- When auditing a variable family, compare METADATA.pb axis ranges against the font file's own fvar table; mismatches mean stale metadata or a stale file.
- Axis registry entries document fallback instances, which is what tools use when a requested value is not a named style.

## Using the repository for verification

- Cross-check version signals: the font file's internal version (from name table or font inspection tooling), METADATA.pb, the npm package version on Fontsource, and the git log date. They should tell one consistent story.
- Confirm license claims from third parties. If a site says "free font", find the family here or in the foundry's own repo and read the actual OFL.txt.
- Trace upstream: the source block or the foundry's website links to the design's origin, which matters when you need to report bugs, request glyphs, or check for updates.
- When a family disappears or a file changes unexpectedly, git history answers what changed and when.

## Workflow

1. Start from the family's catalog page; find its directory in the repo (search by family name under ofl/ first).
2. Read METADATA.pb: license, designer, axes, subsets, date_added.
3. Read OFL.txt or LICENSE.txt; note copyright holders and any Reserved Font Name lines.
4. Check git log for the family directory to see recent changes and the last update date.
5. Record repository path, commit or date inspected, and license notes in your font manifest.

## Common mistakes

- Quoting "from Google Fonts" as a license; the license is the OFL, Apache, or UFL text in the family directory, not the fact of Google's hosting.
- Ignoring METADATA.pb and then being surprised by axes or subsets that differ from a third-party package.
- Treating the latest git state as the version your users have; CDN and npm builds can lag or pin older revisions.
- Missing a Reserved Font Name declaration and later shipping a renamed fork incorrectly.
- Copying fonts out of the repo without the license file; a font without its license is an audit liability.

## Quick reference: paths and commands

The repository rewards people who can move around it without cloning the whole thing (it is large; a full clone is thousands of files).

```
git clone --depth 1 --filter=blob:none --sparse https://github.com/google/fonts
cd fonts && git sparse-checkout set ofl/fraunces ofl/inter
git log -3 --format="%h %ci %s" -- ofl/inter/
git log -1 --format=%ci -- ofl/inter/METADATA.pb
```

- The sparse clone pulls just the family directories you name, which is enough to read metadata, license text, and font files locally.
- `git log` on a family directory is the version signal the website does not surface: last change date and what changed.
- Browsing on GitHub works too: search a family name, land in its directory, and use the file view and history tab for one-off checks.
- To find a Reserved Font Name declaration, read the OFL.txt in the family directory; the RFN line is a copyright statement, not a separate file.

## Worked example: verifying a variable family end to end

Scenario: a design system wants Fraunces for editorial headlines, and the team must record defensible evidence.

1. Locate `ofl/fraunces/` and read METADATA.pb: name, designer (Undercase Type), category, date_added, and the axes block.
2. Compare the declared axes against the font file's own fvar table using a font inspector; Fraunces carries ital, opsz (9 to 144), wght (100 to 900), plus custom SOFT and WONK axes. Any mismatch means stale metadata or a stale file.
3. Read OFL.txt: note the copyright line and whether a Reserved Font Name is declared, since the team plans a re-weighted internal build later.
4. Run `git log` on the directory and record the last change date; check whether recent commits touched glyphs or only metadata.
5. Download the current file from the repository, not from a blog, and record the commit or date inspected in the manifest.
6. Cross-check the same facts against the Fontsource package version; agree on which channel is the deployment source before anyone writes CSS.

The output is a one-paragraph evidence record: family, license, RFN status, axes, last-change date, deployment channel. That paragraph answers every audit question in less time than one meeting.

## Reading git history usefully

- Commit messages in the repository are terse; the diff is the information. Check whether a commit touched the font binary, METADATA.pb, or the description file.
- A burst of commits usually means a version bump or a glyph fix; a silent directory means the family is stable or dormant upstream.
- If a family moved between license directories or was renamed, history shows the trail; this matters when old links in blog posts stop resolving.
- Upstream fixes flow into the repository after the foundry or maintainer submits them, so repo date is a floor for "how new is this", not a ceiling on the foundry's own release.

## Signals to trust

- Agreement between METADATA.pb, the license file in the directory, and the font file's internal name table; three-way agreement is the definition of a clean record.
- A source block pointing at an active upstream repository with visible issue activity.
- Git history showing maintenance within the last year for a family you plan to depend on.

## Signals to distrust

- Third-party download sites claiming "the official Google Fonts file"; go to the repository and stop guessing.
- Metadata describing more axes or subsets than the shipped file contains; trust the file.
- A family directory untouched for years while its category peers update; dormancy is not disqualifying, but it is a recorded risk.

## Field notes

- The repository does not tag releases per family; "version" means the font file's internal version string plus the commit date you inspected.
- Some families live in the repository before they are prominent on the website, and a few website features lag the files; the repository is the leading indicator.
- DESCRIPTION.en_us.html is the human-readable blurb; it is useful context, but it is editorial text, not verified metadata.
- When filing a glyph bug, the source block or the foundry's repository is the right place; the google/fonts maintainers generally route fixes upstream rather than patching in place.
- Keep your own record of the commit date you downloaded from; "latest" is not a version, and future-you will want the number.

## Worked example: tracing a renamed family

Scenario: a blog post links to a Google Fonts family that no longer appears in the catalog, and a team member wants to know whether it is safe to use a downloaded copy.

1. Search the repository for the family name, including case variations; if it is not there, search git history and the foundry's own repository.
2. Check the foundry's site or repository for a rename, a version jump, or a move to a different license; families do get relicensed or superseded.
3. If the old file is what you have, read its internal name table and license string; the file itself says what it is, regardless of what the blog claimed.
4. Decide with evidence: either adopt the current version of the family from the repository with a fresh record, or drop the candidate and note the dead link in the rejection log.
5. Record the whole trail; a family with a history of renames deserves a fuller evidence record than a stable one.

## Tool notes

- GitHub's web search over the repository finds family directories fast; for bulk work, a sparse clone beats the web UI.
- `git log --follow` on a family directory survives renames and moves within the repository.
- Font inspectors open the downloaded TTF directly and read the name table, fvar table, and internal version; keep one bookmarked next to the repository tab.
- For licensing questions, the search box on the OFL text is faster than any summary: search "Reserved" and read the line in context.
- The repository's own tooling and tests are open source too; when a metadata field confuses you, reading the tooling source settles what it means.

## Cross-references

- [Google Fonts Catalog](google-fonts-catalog.md)
- [Evaluating catalog metadata](evaluating-catalog-metadata.md)
- [Open-source due diligence](../licensing/open-source-due-diligence.md)
- [OFL reserved font names](../licensing/ofl-reserved-font-names.md)

Compiled 2025 as part of the Fontlore project.
