# Font Quality Tooling

What this reference covers: Building a quality practice around fonts: linting with Fontspector and fonttools, hinting and small-size rendering, missing-glyph audits, shaping verification, and version pinning discipline. These checks prevent the quiet failures: a weight that renders mushy on Windows, an upgrade that renumbers stylistic sets, a subset that loses tabular figures.

## The quality pipeline in outline

Treat fonts like any other dependency: verify on the way in, monitor over time, control upgrades. Four stages:

1. Intake: lint the file (Fontspector), check provenance (name table, license), diff coverage against your language matrix.
2. Integration: confirm features and metrics feed the CSS layer correctly (feature lists, fallback metrics), record the version.
3. Runtime verification: render real copy at real sizes on real platforms; watch shaping and small-size rendering.
4. Upgrade control: pin versions, review releases deliberately, re-run checks on every bump.

## Fontspector and fonttools checks

Fontspector (the maintained successor to FontBakery) runs a profile of checks per font: required tables present, name table sanity, license string consistency, cmap oddities, metric ranges, and script-specific checks for the systems the font claims to support. Run it at intake and in CI for any font your team maintains or regenerates.

fonttools covers the manual layer:

- ttx -t cmap file.ttf: dump coverage; diff against your required codepoint list.
- ttx -t name file.ttf: version, foundry, license strings; the basis of your version register.
- fonttools subset: regenerate subsets and diff the output cmap and feature list against the previous build; surprises here are release blockers.

## Hinting and small-size rendering

Hinting is grid-fitting instructions that make TrueType outlines render crisply at small sizes, especially on Windows with ClearType. It matters when your type lives at 12 to 14 px:

- Fonts from major foundries and the big open catalogs (Google Fonts pipeline) are usually well hinted; fonts from small foundries or converted from other formats sometimes are not.
- Check on a Windows machine (real or VM) at 12, 13, and 14 px with ClearType on: mushy strokes, uneven stems, or blurry small text indicate hinting problems.
- TTFAutohint (Werner Lemberg) is the standard tool if you control the font source and need to add hinting; most teams should instead prefer better-hinted fonts rather than rehinting.
- Variable fonts complicate hinting (hints apply per outline, and interpolation moves them); the practical check is the same: render small on Windows and judge.
- On macOS, grayscale smoothing forgives unhinted outlines; do not judge small-size quality on a Mac alone.

## Missing-glyph and shaping audits

- Maintain the per-language codepoint checklist from the testing reference; run it against every new version, not just the first adoption. Coverage changes between releases more often than anyone expects.
- Automated option: a small script that loads the cmap with fonttools and asserts your required codepoints exist; wire it into CI where fonts or subsets are built.
- Shaping verification: render the shaping smoke strings (lam-alef, Devanagari conjuncts, Thai mark stacking) through hb-shape or a headless browser screenshot test; a regression here ships broken text to real users.
- Watch .notdef: a subset that silently drops required glyphs produces tofu; the cmap diff catches it before users do.

## Version pinning discipline

- Record, per font in use: family, exact version string (from the name table or package version), source (foundry page, GitHub tag, Fontsource package version), files and hashes, license, and the date adopted.
- Pin exactly: package.json exact versions for Fontsource; vendored files with hashes for self-hosted fonts; no floating ranges.
- Subscribe deliberately: foundry release notes, GitHub releases for open families, or the Fontsource changelog. Review on a cadence (quarterly is realistic) rather than continuously.
- When upgrading: diff coverage, re-run Fontspector, recompute metric fallback overrides, re-render the specimen matrix, and check that stylistic set numbers you rely on have not moved.
- Keep one version across a family: mixing 1.0 files with a 1.2 italic produces weight mismatches that look like design bugs.

## What "good enough" looks like

For most teams: Fontspector clean at intake, a pinned version register, a codepoint CI check, a Windows small-size spot check, and a quarterly release review. That is an afternoon of setup and prevents the classic incidents: silent metric drift, lost features after subsetting, and coverage gaps found by users instead of CI.

## Common mistakes

- Adopting a font from a random "free fonts" site without provenance checks; the file may be an old version, a clone, or worse, and every later check inherits the problem.
- Judging rendering quality only on the design team's Macs; small-size hinting failures are a Windows phenomenon.
- Never recording versions, then being unable to answer "which Inter is this layout tuned for".
- Treating upgrades as non-events: metric overrides, feature numbers, and coverage all move between versions.
- Checking glyph coverage by scrolling a specimen instead of diffing cmaps; the missing codepoint is never the one you scroll past.
- Skipping the shaping strings because "the font says it supports Arabic"; support claims are not shaping guarantees.

## Decision rules

- Any new font in the stack: full intake (lint, provenance, coverage diff, version record) before it reaches main.
- Any subset regeneration: cmap and feature diff against the previous build; human review only on the diff.
- Upgrade requests: batch them on the review cadence; emergency upgrades only for security or legal issues.
- A check fails and the font is load-bearing: do not "fix in CSS"; fix the version, the subset, or the choice.
- No Windows access: use a VM or CI screenshot service for the small-size check; it is the one platform-specific check that cannot be skipped.

## Comparison table

| Tool | Kind | Answers | Interface |
| --- | --- | --- | --- |
| Fontspector | linter | structural health, table sanity, license strings, script checks | CLI, CI |
| fonttools / ttx | dump and fix | exact cmap coverage, name table facts, metric values | CLI |
| hb-shape | shaper probe | which glyphs HarfBuzz picks for a string | CLI |
| TTFAutohint | fixer | adds TrueType grid-fitting to unhinted fonts | CLI |
| Wakamai Fondue | inspector | features, axes, metrics, fallback suggestions | web, upload |
| FontDrop | inspector | raw tables and glyph outlines | web, upload |

## Worked example

Upgrading a vendored family from v1.0 to v1.1 as a checklist that fits in a pull request:

1. Record what arrived: ttx -t name on the new file; note the version string and the file hash; the old hash stays in the manifest for comparison.
2. Lint: Fontspector with the profile matching the font class; new WARN and FAIL lines are findings, not noise.
3. Coverage diff: dump the cmaps of both versions and diff them; added codepoints are a bonus, removed ones are a release blocker until explained.
4. Feature diff: dump the GSUB tags of both versions; a stylistic set that moved (ss02 now means what ss03 meant) breaks shipped CSS with no error anywhere.
5. Metrics: recompute the adjusted fallback overrides; a small ascent change moves every line on the page.
6. Render: the specimen matrix at 12, 13, and 14 px plus the shaping smoke strings.
7. Ship: new hash, updated manifest entry, changelog note.

## Code notes

```
ttx -t name MyFont-v1.1.ttf
ttx -t cmap MyFont-v1.1.ttf

hb-shape MyFont-v1.1.ttf "find"                      # default features
hb-shape --features="-liga" MyFont-v1.1.ttf "find"   # liga off
```

A CI check that required codepoints survive every build:

```
from fontTools.ttLib import TTFont

REQUIRED = [0x0105, 0x0142]  # a with ogonek, l with stroke (Polish)
missing = [hex(cp) for cp in REQUIRED
           if cp not in TTFont("MyFont-latin.woff2").getBestCmap()]
assert not missing, f"missing glyphs: {missing}"
```

fontTools reads woff2 when the brotli package is installed; wire the check next to wherever subsets are built.

## Field notes

- Some foundries never bump the name-table version string across releases; the file hash is the only reliable identity, so track both.
- Per-weight files of one family often carry identical version strings; treat the family as a single versioned unit and never mix 1.0 files with 1.1 italics.
- The default pyftsubset feature set is the classic way tabular figures vanish; a diff of feature tags catches it, scrolling a specimen does not.
- Fontspector findings on a font you do not maintain are still useful: they document why a file was rejected or accepted.
- Web inspectors mean uploading the file; keep unreleased, client-confidential, or NDA work on the CLI tools.
- Fontspector profiles differ (default, googlefonts, per-script); pick the profile that matches the font class, and treat a profile change as a check-suite upgrade to review.

## Common failure modes

- The upgrade that "changed nothing": metrics moved by a percent, long articles reflowed, and nobody kept the old file to compare against. Hashes and table dumps make upgrades reviewable.
- Renumbered stylistic sets after an upgrade: the CSS still compiles and the glyphs change silently. Diff GSUB tags, not only the cmap.
- Subsetting dropped tabular figures: dashboards misalign a week after a "size optimization". Diff feature tags alongside coverage.
- Windows-only mush at small sizes: unhinted outlines from a small foundry, invisible on the design team's Macs. The one platform check that cannot be skipped.
- A shaping regression reached production: smoke strings were never re-rendered after the upgrade. Keep shaping strings on the release checklist, not in tribal memory.
- The check suite runs only on fonts the team builds, so vendored third-party files never get linted; run the intake checks on every file regardless of origin.
- CI passes because it asserts only cmap coverage; feature and metric diffs are missing, which is exactly where the silent regressions live.

## Quick reference

- Intake: Fontspector pass, name table read, cmap diff, version and hash recorded.
- The minimum manifest entry: family, version string, source URL, file hash, license, adoption date.
- Subsets: cmap diff plus feature tag diff on every rebuild.
- Rendering: Windows spot check at 12-14 px; shaping strings through hb-shape.
- hb-shape prints glyph names and advances; diff two runs to see exactly what a feature or version change does.
- Upgrades: batched on the review cadence; emergencies only for security or legal.
- One version across a family, always.

## Cross-references

- [Inspecting font files](inspecting-font-files.md)
- [Subsetting and performance](subsetting-and-performance.md)
- [Keeping current safely](../workflow/keeping-current-safely.md)
- [Testing multilingual coverage](../scripts/testing-multilingual-coverage.md)

Compiled 2025 as part of the Fontlore project.
