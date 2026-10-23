# Subsetting and Performance

What this reference covers: Subsetting fonts with pyftsubset and glyphhanger, combining subsets with unicode-range, realistic size budgets, latin versus latin-ext versus full coverage costs, and how to measure actual gains rather than assume them. Subsetting is the highest-leverage performance move in web typography.

## Why subset

A retail font file carries glyphs for markets you may never serve: a "full" Latin family can include Cyrillic, Greek, and hundreds of symbols; a variable file adds interpolation data on top. Subsetting keeps only what your content needs, cutting transfer size, parse time, and cache pressure. It also reduces risk: fewer codepoints means fewer unreviewed glyphs.

## pyftsubset, the workhorse

The fonttools package provides pyftsubset. A representative command:

- pyftsubset SourceSans3-Regular.ttf --unicodes="U+0000-00FF,U+0131,U+0152-0153,U+2013-2014,U+2018-201D,U+20AC" --layout-features="*" --flavor=woff2 --output-file=SourceSans3-latin-subset.woff2

Key points:

- --unicodes takes explicit ranges; --text can take a string of actual content; --text-file reads a corpus. Unicode-range files for a font stack are generated this way, one call per subset.
- --layout-features="*" keeps OpenType features (kerning, ligatures, tabular figures). The default drops some features to save bytes; audit what the default keeps before shipping a UI font that must have tnum.
- --flavor=woff2 requires the brotli package installed. Without it you get uncompressed output; do not ship that.
- Keep the original file as source of truth in the repo; subsets are build artifacts, regenerated, not hand-edited.

## glyphhanger, subset to what you use

glyphhanger crawls your pages or text files, extracts the codepoints actually used, and can drive pyftsubset directly. It is ideal for apps with fixed copy: the subset then contains exactly the strings that can render. Its limits: user-generated content breaks the assumption, so reserve usage-based subsetting for controlled surfaces (UI chrome, marketing pages, price strings) and keep a broader subset for anything users type.

## Budgets that hold up in review

Set byte budgets per surface and verify in the network panel, not in build logs:

- UI body face, one weight, latin subset: 15 to 40 KB woff2. If a "latin" file is 80 KB, check what it actually contains.
- Each additional style or weight: roughly the same again; a four-weight latin system is 60 to 160 KB total and is usually over-shipped.
- Variable file, latin: 50 to 300 KB depending on axes; compare against the sum of statics you would actually use.
- latin-ext adds a modest file if split via unicode-range; folding it into one file roughly doubles the latin cost whether or not a given page needs it.
- CJK: slices of 5 to 60 KB each via unicode-range; a full weight is megabytes and is not a budget item, it is an architecture decision.

Total page font budget guidance: under about 100 KB for a typical marketing page, under about 200 KB for a data-heavy app is a defensible default; state your numbers in the performance budget and enforce them in CI with a bundle check.

## Subset layers that work together

1. Base latin subset: always loaded, covers the UI language plus punctuation and figures.
2. latin-ext file with its own unicode-range: downloads only when a Polish or Czech character appears.
3. Additional per-script files (cyrillic, greek, vietnamese, arabic) exactly matching your language matrix.
4. A monospace or display face subset only for the strings it renders (numerals, labels), not its full latin set.

This structure means the common case pays only for the common case, and rare scripts pay on appearance. It also maps cleanly to hosting providers that already slice this way.

## Measuring gains

- Network panel with cache disabled: record bytes before and after, per file and total; convert to a percentage for the review document.
- Lighthouse or equivalent for the second-order effects: fewer font bytes reduces contention with critical CSS and images on slow connections.
- Parse cost: measure main-thread time around font loads on a mid-tier Android device; large variable files cost parse time that byte counters hide.
- Caching: subsets change when content changes, so keep subsets content-stable where possible (fixed language-based subsets, not per-page subsets) or returning users re-download.
- Report honestly: a 70 percent smaller file that never loads on the critical path matters less than a 10 percent saving on the face that blocks first paint.

## Common mistakes

- Subsetting away glyphs the content will need later (the brand launches in Poland; the latin subset has no ogoneks) and discovering it in production. Derive subsets from the language matrix, not the homepage.
- Stripping layout features with default settings, silently losing tabular figures or essential ligatures.
- Hand-editing unicode-range declarations instead of generating them, creating phantom ranges and missing-glyph bugs.
- Per-page micro-subsets that destroy caching; users pay again on every page.
- Measuring file size on disk and calling it performance; wire size, compression, and load timing are different numbers.
- Subsetting an already-subset hosted file; work from the original source files you license.

## Decision rules

- Fixed-copy surfaces (marketing, pricing, UI chrome): usage-based subsetting is worth the tooling.
- UGC or search-driven content: language-based subsets plus an intentional system fallback for the rest.
- Multilingual products: build the subset pipeline around the language matrix from day one; retrofitting subsets into a shipped product is migration work.
- Budgets exceeded: cut weights and styles before cutting glyphs; an unused 600 weight costs more than latin-ext.
- Any doubt about a subset: ship the wider subset and measure; correctness beats a few kilobytes.

## Code notes

The workhorse invocation, with the flags that matter:

```
pyftsubset SourceSans3-Regular.ttf \
  --unicodes="U+0000-00FF,U+0131,U+0152-0153,U+2013-2014,U+2018-201D,U+20AC" \
  --layout-features="*" \
  --flavor=woff2 \
  --output-file=SourceSans3-latin.woff2
```

- --flavor=woff2 needs the brotli package; without it the output is silently uncompressed.
- --layout-features="*" keeps kern, liga, tnum and company; the default drops some to save bytes.
- --text and --text-file subset to actual copy; --unicodes-file reads ranges from a file.
- --desubroutinize can improve compression for CFF-based fonts; measure the output before keeping it.

glyphhanger driving a subset from crawled copy:

```
glyphhanger https://example.com/pricing --subset=SourceSans3-Regular.ttf --formats=woff2
```

Read the output's coverage back to derive the unicode-range declaration:

```
ttx -t cmap SourceSans3-latin.woff2
```

Keep subsets language-based, not per-page, so each URL and its cache entry stay stable across releases.

## Comparison table

| Strategy | Input | Caching | Risk | Fits |
| --- | --- | --- | --- | --- |
| Language-based subsets | Unicode blocks per script | stable across pages | wider than strictly needed | content sites, UGC, most products |
| Usage-based subsets | the copy actually shipped | breaks when copy changes | new copy, missing glyphs | fixed UI strings, pricing |
| Per-page micro subsets | one page's text | worst: re-downloads per page | everything | almost never |
| Hosted sliced CSS (Google Fonts) | the service's slicing | theirs, good | third-party dependency | prototypes, internal tools |

## Worked example

A product site ships English, German, and Polish from one UI family, four static weights:

1. Language matrix: en and de need latin; pl needs latin-ext, where the ogoneks and stroke l live.
2. Per weight, two subsets built from the original licensed files: latin and latin-ext, both with --layout-features="*" and --flavor=woff2.
3. From each subset's cmap, generate the unicode-range declarations; the build emits the @font-face blocks.
4. Budget check against the numbers above: latin at 15-40 KB per weight, latin-ext smaller; the whole system stays inside the page font budget.
5. Verify with cache disabled in the network panel: an English page fetches only the latin files; opening the Polish pricing page pulls latin-ext on demand.
6. Commit the originals and the build config; subsets are artifacts, never hand-edited.
7. Record the subset recipe (command, unicode lists) in the repo so the next maintainer regenerates instead of guessing.

## Field notes

- The classic incident: the brand launches in Poland, latin-only subsets ship, and ogoneks render as tofu or fall back mid-word to system fonts. Subsets derive from the language matrix, not from the homepage.
- "Latin" is not one definition: the Google Fonts latin range includes punctuation, currency, and the common quote and dash codepoints; a hand-rolled U+0000-00FF-only subset loses typographic quotes and dashes that real copy uses.
- Subsetting an already-subset file (a hosted or vendor-shipped webfont) silently loses glyphs; always subset from the originals you license.
- Parse time is the second cost: large files cost main-thread time on mid-tier Android even on fast networks; measure, do not only count bytes.
- When in doubt, widen: a few kilobytes of latin-ext is cheaper than a migration when the second language lands.

## Quick reference

- Default command: pyftsubset with --unicodes, --layout-features="*", --flavor=woff2, brotli installed.
- Coverage to CSS: derive unicode-range from the subset's cmap, never by hand.
- Strategy: language-based subsets for content and UGC; usage-based only for fixed copy.
- Budgets: latin 15-40 KB per weight as woff2; enforce in CI, verify in the network panel.
- Cache: content-stable subset URLs; per-page subsets destroy caching.
- Sources: always subset the original licensed files, never an already-subset webfont.
- CJK: sliced unicode-range files are architecture, not an optimization knob.
- Regenerate: only from originals, and only when the language matrix or the font version changes.
- Gains: measured as bytes on the wire with cache disabled, not as file size on disk.

## Cross-references

- [Webfont formats](webfont-formats.md)
- [Font loading pipeline](font-loading-pipeline.md)
- [CJK fundamentals](../scripts/cjk-fundamentals.md)
- [Latin and extended coverage](../scripts/latin-and-extended.md)

Compiled 2025 as part of the Fontlore project.
