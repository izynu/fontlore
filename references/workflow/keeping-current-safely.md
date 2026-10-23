# Keeping Current Safely

What this reference covers: Tracking font releases and typography news without churning production: pinning npm font packages and the Google Fonts CSS API, reviewing variable font updates for breaking axis changes, monitoring changelogs, running a quarterly review cadence, and documenting why families were adopted or deprecated. The goal is a typography stack that improves deliberately instead of drifting.

Typography is a dependency like any other, with one twist: glyph changes are user-visible and never caught by unit tests. A dependency bot that bumps a font package can change every heading on the site with nobody noticing. Staying current is valuable; staying current carelessly is how a Tuesday update becomes a redesign nobody approved.

## What actually changes upstream

- Glyph sets and language support: new subsets, fixed diacritics, revised letterforms. These change rendering for real users.
- Variable axis changes: weight ranges extended or shifted, new axes added, rarely axes removed. Axis range changes are breaking changes for any layout tuned to the old range.
- Metrics: a font update can shift advance widths and line spacing, which shows up as layout shift and reflowed text.
- Packaging metadata: Fontsource re-versioning, subset entry points added or renamed, license file updates.
- None of these arrive with a changelog unless the project keeps one, which is why monitoring is a team practice, not an individual habit.
- Releases also arrive without announcement at all: packaging pipelines re-package silently, and a quiet npm version bump is sometimes the only signal that upstream moved.

## Pinning npm font packages

- Pin exact versions in package.json for every font package: no caret, no tilde. A validated design review approved version A; a range lets any fresh install ship version G.
- Record the validated version in the project font manifest so the design review and the dependency list agree; the manifest lives with the license evidence.
- Route font package updates through the same pull-request review as code: render the diff visually, then merge.
- What the review of a font-bump pull request actually covers:
  - Numerals in tables and prices, because numeral revisions are the most common quiet change.
  - Diacritics and any non-Latin strings you ship, even one sample per script.
  - Weight rendering at the sizes your tokens define, especially semibold and medium.
  - Table alignment and line counts on a dense page, since metrics can shift.
  - A before/after screenshot pair attached to the pull request, so the review is of pixels, not of a version number.
- Renovate-style bots are welcome if font packages are labeled and held for visual review rather than auto-merged.
- For regulated contexts, vendor the files into the repository with the upstream version and license recorded. npm pinning is usually enough; vendoring is the maximal form.

## Pinning Google Fonts CSS v2

- The css2 endpoint, for example https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap, always serves the current upstream files; there is no version parameter. URL pinning does not exist on the CDN.
- Treat the CDN as appropriate for prototypes and marketing pages, and self-host for anything where rendering must be reproducible.
- Self-host by vendoring files from the google/fonts repository at a specific commit, or by using pinned Fontsource packages; either way the bytes stop moving until you move them.
- If the CDN must stay, monitor rendering: a scheduled screenshot pass on key pages catches upstream changes within a review cycle instead of via user reports.
- Record in the manifest which families are CDN-served and therefore unpinned. Unpinned is a decision, not an accident.

## Reviewing variable font updates

- Diff axes before glyph looks: extract the fvar table from old and new files (Wakamai Fondue at https://wakamaifondue.com, or fontTools in a small script) and compare axis tags, ranges, and defaults.
- A widened weight range is usually safe; a shifted default or a narrowed range breaks styles that assumed the old geometry.
- Check whether the update changed named-instance names or axis ordering; both can break tooling that reads fonts programmatically.
- Named instances change more often than axes; any UI that offers preset instances needs re-verification after an update.
- Keep the previous file in the repository until the new one passes review; rollback should be a checkout, not a research project.

## Changelog monitoring that works

- google/fonts repository: watch the family directories you depend on. The commit history per directory is the closest thing to an upstream changelog for Google Fonts families.
- Independent families: watch GitHub releases on the upstream repository; Inter and JetBrains Mono both publish real release notes. Release notifications are cheap and signal-rich.
- Fontsource packages: the npm version feed is a proxy for upstream change; a jump in the package version means the packaging pipeline processed something new.
- Foundry newsletters for commercial faces: license terms and version entitlements change too, and those changes arrive by email, not by commit.
- Aggregate the checks into one owner per review cycle; scattered individual watching is how signals get missed.
- Keep the watching surface small: the ten or so families your products actually ship, not the whole catalogs you browsed once.
- Archive signals into the research log when they arrive, even if no action follows; a release you noticed but did not record is a release nobody noticed.

## Quarterly review cadence

- Once a quarter, one hour with the font manifest open: for each family, compare the pinned version against the latest upstream, and record "current" or "update pending" with an owner.
- Review the quarter's incidents: layout shift reports, missing glyphs, fallback rendering screenshots from the wild.
- Re-check license facts that move: pageview tiers against actual traffic, subscription renewal dates, domains covered.
- Sweep for orphaned fonts: families still shipped but no longer used by any surface. These go to the deprecation process, not to silent neglect.
- Output of the review is a dated note in the repository, even when the conclusion is "no changes". The record of deliberate inaction is what separates review from ritual.

## A quarterly review, walked through

A concrete agenda for the one-hour pass, with a ten-font product as the example:

1. Open the manifest and the register side by side; confirm every family has an owner, a license, and a pinned version.
2. Fifteen minutes: for each family, check the upstream repository or package feed for releases since the last review; note anything newer.
3. Fifteen minutes: inspect the incidents list, including any layout shift or missing-glyph reports, and attach screenshots to the review note.
4. Ten minutes: check pageview tiers against traffic trends and subscription renewal dates against the calendar.
5. Ten minutes: decide. Batch the updates that passed inspection into one reviewed upgrade, or extend pins with explicit re-check dates.
6. Five minutes: write the dated note and post it where the team reads; file follow-up items with owners.

The rhythm matters more than the depth: a shallow review that always happens beats a deep one that happens twice a year.

## Evaluating new releases against real needs

- Start from the constraint sheet the family was originally chosen against; a new release is evaluated on whether it serves those constraints better, not on whether it is new.
- Improvements to scripts you do not ship are noise; improvements to your primary script and to legibility at your actual sizes are signals.
- Read the release notes for intention: "refined spacing" is routine; "revitalized the design" means your approved look just changed under you.
- Test the new version with the standard test copy at standard sizes; the testing reference has the method, and it applies to updates as much as to new selections.
- Adopt updates on a schedule you chose, batched and reviewed, rather than one at a time as they appear.
- Cap the batch: one review cycle absorbs a handful of font updates comfortably; a season of accumulated updates is a migration, and should be planned as one.

## News without churn

Staying informed is separate from staying current; you can read everything and change nothing.

- Follow the field for taste and context, not for dependencies: Fonts In Use for real-world applications, Typewolf for conventions, foundry journals for what serious shops are wrestling with.
- When news surfaces a family that fits a known future need, record it in the research log with the link and one line of assessment; the log, not memory, is the queue.
- Distinguish reading from shopping: a font that appears in your notes three times across different projects has earned a real evaluation; one that appeared once in a roundup has not.
- Keep typography news out of production conversations unless it crosses one of the defined triggers: a license change, a release for a family you ship, or a constraint change in the brief.

## Avoiding hype-driven swaps

- A new family generating attention is not evidence it serves your product; popularity is context-free and your constraints are not.
- No family swaps within a settled product's first year without a failure driving the change; identity needs time to mean anything.
- Require a written rationale for any swap: what problem exists today that the current family fails, and evidence the candidate solves it better.
- Beware redesign-by-font: if the case for swapping rests on novelty rather than on a measured deficiency, file the candidate in the research log and move on.
- Deprecation is the honest response to a genuine mismatch, and it has its own process; swapping without it is how teams end up running two type systems.

## Documenting adoption and deprecation

- Adoption entry in the manifest: family, version, license, evidence links, the constraint match that justified it, and the date. Future maintainers inherit the reasoning, not just the dependency.
- Deprecation entry: what is being replaced, why, the migration target, the removal date, and which surfaces still consume it.
- When a family is deprecated because upstream changed character or terms, link the exact commit or announcement; the record should survive team turnover.
- The deprecation process itself (freeze, migrate, remove with a buffer) lives in the governance reference; the documentation habit is the same: dated, owned, findable.
- Review the adoption notes at every deprecation: if the original rationale no longer makes sense, the deprecation is on schedule; if it still does, question the swap.

## Common mistakes

- Treating the CDN decision as permanent; a prototype that grew into a product should not keep prototype-grade delivery.
- Reviewing font updates only after user complaints; by then the shift has been live for weeks.
- Updating one surface (web) and leaving another (email templates, native app) on the old version, so the product renders two different fonts.
- Letting dependency bots auto-merge font package bumps; glyph changes are user-visible and no test suite catches them.
- Assuming the Google Fonts CDN is pinned because the URL is stable; the URL is stable, the bytes are not.
- Reviewing variable font updates by eyeballing headings only; numerals, small sizes, and the axes you actually use are where breaks live.
- Running reviews that produce no record; an undocumented "all fine" is indistinguishable from no review at all.
- Adopting a new release because it is new, then shipping a blend of old and new files across surfaces.
- Deprecating nothing ever: the manifest grows until nobody can tell what is real.

## Decision rules

- Pinned and reviewed beats current and surprised; freshness is only a value when the project can absorb rendering changes.
- An update that changes axis ranges or defaults is a breaking change and follows the breaking-change path: review, batch, migrate.
- If an upstream change would alter the approved look of the product, it is a design decision, routed to design review, not a dependency bump.
- No swap without a written deficiency; no deprecation without a named replacement and a removal date.
- When in doubt, extend the pin and add a re-check date; urgency in typography is almost always manufactured.
- The review that finds nothing still ships a record; "checked, current, no action" with a date is the deliverable.
- News items without a matching trigger stay in the research log; production conversations are for the families you actually ship.

## Cross-references

- [Research workflow](research-workflow.md)
- [CSS handoff snippets](css-handoff-snippets.md)
- [Font-face and CSS](../technical/font-face-and-css.md)
- [License audit checklist](../licensing/license-audit-checklist.md)

Compiled 2025 as part of the Fontlore project.
