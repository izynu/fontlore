# Google Fonts Catalog

What this reference covers: How to use fonts.google.com as a research tool instead of a download page. It covers the filter system, specimen and type tester workflow, language coverage checks, and the basics of the CSS and Developer APIs. The goal is to turn a catalog of well over a thousand families into a defensible short list.

Google Fonts has been the default first stop for open-source typefaces since 2010. Every family in the catalog ships under a free license (OFL, Apache 2.0, or the Ubuntu Font License), which makes the catalog safe to test from, but its size and mixed quality mean that filters and verification matter more here than anywhere else.

## Navigating with filters

- The Category filter buckets families into Serif, Sans Serif, Display, Handwriting, and Monospace. Treat the buckets as hints rather than ground truth; classification is fuzzy and several display faces hide inside the Serif and Sans Serif groups.
- The Language filter is the most underused control in the catalog. Selecting a language such as Vietnamese, Greek, or Devanagari restricts results to families with real coverage of that script, which instantly removes hundreds of Latin-only candidates.
- Fonts properties includes a Variable toggle and a Number of styles control. Variable families survive design-system weight requests without shipping a separate file per weight.
- Sort orders do different jobs: Trending and Popular surface safe, heavily used families; Newest surfaces experimental work; Number of styles finds complete families suitable for editorial systems.
- The search box matches family, designer, and foundry names. Searching a foundry name such as Cadson Demak or ITF is a legitimate discovery route when you trust a publisher's quality bar.
- Pairing suggestions on family pages are editorial and uneven. Use them as leads to inspect, never as conclusions to copy.

## Specimen pages and the type tester

- Every family page opens on a specimen view where you can edit the sample text and drag size, line-height, and spacing controls. Replace the default text with your real project copy before judging anything.
- The type tester supports multiple rows. Build a small board: your headline, a body paragraph, a UI label row, and a numeral-heavy row with dates, prices, and account numbers.
- Test at your real sizes. A family that looks brilliant at 48px in the specimen can collapse at 14px, and some quiet text faces bloom when scaled up.
- The glyph grid shows the full character set. Look for real punctuation, accented characters for your languages, tabular numerals if the interface needs column alignment, and symbol coverage if the content requires it.
- Download family gives you the current static fonts or the variable build. Use it for offline testing in design tools, but do not treat the download as a stable archive; versions move as upstream projects update.

## The About panel

- The About section lists the designer, the foundry or publisher, the license, and for many families the upstream repository. This is the metadata you will re-verify later against Fontsource and the google/fonts repository.
- Read the license line explicitly. Google Fonts only hosts free licenses, but the exact license determines what you may do with modified versions and how you document your use.
- The description often names the classification and inspiration, for example a revival of a historical design or a companion to another family. This context feeds classification and tone work.
- Version information on the website is thin. The google/fonts repository and Fontsource carry stronger version signals when you need to pin.

## Language and script coverage

- The supported language count is a floor, not a verdict. A family can list a language while setting it clumsily, with poor diacritic placement or awkward spacing in accents.
- For mixed-script projects, judge each script's family separately. Many multilingual families are excellent in one script and merely adequate in the others.
- Paste text in the target language into the type tester and check diacritics, numerals, and punctuation, not just the base alphabet.
- If a script matters strategically, cross-check dedicated script foundries and catalogs before settling; specialist publishers often beat generalist coverage.

## Variable axis playground

- Families with axes expose sliders on the specimen page: wght and wdth are common, opsz appears on families designed with optical sizes, and custom axes such as SOFT and WONK on Fraunces appear when present.
- Move one axis at a time and watch where the design holds together. Axis extremes are where otherwise good families fall apart.
- If the UI needs intermediate weights like 450 or 550, a variable family avoids shipping extra weight files and keeps rendering consistent across states.
- Note which axes are registered (wght, wdth, opsz, slnt, italic) versus custom; custom axes usually need explicit support in tooling.

## API basics

The CSS API is the delivery mechanism most projects use without thinking about it. Knowing its shape helps you debug and reason about cost.

```
https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap
https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,300..700
```

- Multiple axes are requested in alphabetical order after italic. Axis order errors are the most common reason a request returns a 400 error.
- The display parameter controls font-display behavior for the served CSS. Choose a strategy deliberately instead of copying it mindlessly.
- Served CSS contains unicode-range subsets, so the browser downloads only the files it needs. This makes the CDN efficient but version-unstable: you always get the latest revision of every family.
- The Developer API webfonts list endpoint returns JSON for every family, including subsets, variants, axes, and file URLs. It requires an API key and is the right tool when coverage needs to be enumerated programmatically.
- The CSS API offers no version pinning. If reproducibility matters, self-host via Fontsource packages or files from the google/fonts repository.

## Workflow

1. Write the brief constraints first: scripts needed, size range, tone words, and license requirements.
2. Filter by language and category, then by Variable and style count if the system needs ranges.
3. Shortlist 8 to 12 families; open each specimen and paste real copy into the type tester.
4. Check the About panel for designer, foundry, license, and upstream links; record them.
5. Eliminate families that fail at body size or lack required glyphs; keep 3 to 5 for scoring.
6. Log the source, the date checked, and the version signal for every candidate while the session is fresh.

## Common mistakes

- Judging families on the default specimen text instead of your own content.
- Trusting the category label and never verifying the classification yourself.
- Assuming the largest style count is the best family; unused bloat is a cost, not a feature.
- Hotlinking the CDN without deciding a font-display strategy or a fallback plan if a family changes.
- Ignoring the About panel and later being unable to name the designer, foundry, or license during an audit.
- Testing only headlines because they look impressive, then discovering the body setting is the weak point.
- Confusing a family's language listing with proven rendering quality in that language.

## Decision rules

- Start filters from the brief, not from taste: script coverage first, category second, properties third.
- If you need pinned, reproducible builds, go straight to self-hosting and treat the catalog as a discovery layer.
- When two families look interchangeable, keep the one whose weight and width ranges match the system you actually described in the brief.

## Filter promises versus reality

Filter labels make claims that are directionally true and individually unreliable. Read them as triage; production decisions still need specimen and glyph-grid verification.

| Filter result | What it actually guarantees | What it does not guarantee |
| --- | --- | --- |
| Language: Vietnamese | Code points for Vietnamese letters exist | Tone marks stack cleanly; the design was built for the language |
| Category: Sans Serif | The catalog bucket says sans | The face is neutral or text-suitable; display sanses hide here |
| Variable toggle | A variable build is served | Every axis you need is present; many builds are wght-only |
| Popular | Heavy usage across live sites | Fit for your brief; popularity tracks age as much as quality |
| Number of styles: high | Many static styles exist | True optical sizes, real italics, or the weights you need |
| Search by foundry | Families credited to that foundry | The foundry's complete catalog; only what Google hosts |

Rule of thumb: a filter result earns a slot on the shortlist; nothing earns a production slot until the specimen and the glyph grid confirm it.

## Worked example: shortlisting for a Vietnamese news product

Brief: long-form reading on mobile and desktop, Vietnamese and English mixed, ad-supported so payload matters, open licenses only.

1. Apply the Language filter for Vietnamese plus the Serif category for the reading face; the result set drops from well over a thousand families to a few dozen.
2. Body-text candidates: Literata, Source Serif 4, Noto Serif, Lora, Merriweather. Paste three paragraphs of real Vietnamese copy at 17 to 19 px.
3. Check stacking on vowels that carry both a vowel mark and a tone mark, and on capitals with marks at small sizes; several candidates cramp or clip here.
4. Literata tends to survive this test: commissioned for Google Play Books with deliberate Vietnamese coverage and a variable optical size axis.
5. For UI labels, repeat with Sans Serif plus Vietnamese: Be Vietnam Pro, Source Sans 3, and a couple of Inter-class candidates, checking capital diacritics in button-sized type.
6. Cross-check the finalists in the google/fonts repository, then log license, version, and tested sizes in the evidence record.

The loop generalizes to any language brief: language filter, real copy, mark stacking at real sizes, repository verification.

## Signals to trust

- An About panel whose designer and foundry match the foundry's own site; consistent metadata predicts a maintained family.
- A source block in the repository metadata pointing to an active upstream project with recent commits.
- Variable builds whose axis ranges cover the design system without forcing the ends of the range.
- Specimens that render your language correctly by default, capitals, numerals, and punctuation included.

## Signals to distrust

- Pairing suggestions on family pages; they are editorial leftovers that often date from launch.
- Popularity as a quality proxy; trend lists reward names that were simply early.
- The Handwriting category; it mixes casual scripts, brush faces, and connected scripts with wildly different fitness for use.
- Glyph grids missing ordinary punctuation variants (curly quotes, en and em dashes) on a face meant for body text; that signals a thin character set.

## Quick reference: request patterns

```
css2?family=Inter:wght@400;500;700&display=swap
css2?family=Inter:ital,wght@0,400;0,700;1,400&display=swap
css2?family=Fraunces:ital,opsz,wght@0,9..144,100..900;1,9..144,100..900
css2?family=Inter&text=Dashboard
```

- Line 1 requests discrete weights. Line 2 uses italic tuples, each tuple starting with the italic flag. Line 3 requests variable ranges; axis names must appear in alphabetical order with lowercase registered axes before uppercase custom ones (Fraunces adds SOFT and WONK after wght). Line 4 uses the text parameter to subset the served file to exact characters, the smallest possible payload for fixed strings.

## Field notes

- The css2 endpoint rejects wrong axis ordering with a 400 but silently ignores some other malformed pieces; when a weight goes missing in production, re-read the request URL character by character before blaming the font.
- Debug with curl and a real browser user agent: that shows the actual woff2 files a user's browser downloads, not the CSS you see in the view-source of your dreams.
- Families change on Google's schedule, not yours; a glyph revision can shift a pinned headline by a pixel or two. Self-hosting is the fix, not complaint tickets.
- For CJK families, the CSS API's unicode-range slicing is what makes them usable at all; self-hosting the same monolithic file without subsetting is a performance incident waiting to happen.

## Questions to ask while filtering

- Does the brief need scripts the Language filter can express, or a tone the category filter cannot? Write the missing filter as an explicit test.
- Does the variable build cover the axis ranges the design tokens demand, or only the showcase range?
- Does the style count match the roles in the brief (text, display, captions, mono), or is it just big?
- What is the licensing nuance: plain OFL, OFL with a Reserved Font Name, Apache, or UFL?
- Is there an upstream repository to file issues against when a glyph turns out to be wrong?

## Cross-references

- [Fontsource REST API](fontsource-api.md)
- [The google/fonts repository](google-fonts-repository.md)
- [Evaluating catalog metadata](evaluating-catalog-metadata.md)
- [Choosing body typefaces](../selection/choosing-body-typefaces.md)

Compiled 2025 as part of the Fontlore project.
