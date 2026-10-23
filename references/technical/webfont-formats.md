# Webfont Formats

What this reference covers: The real differences between WOFF2, WOFF, and raw TTF/OTF, which browsers need which format today, how unicode-range splitting changes the picture for multilingual and CJK content, and what to actually ship. The short answer is WOFF2 only, but the details decide how well it works.

## The three formats that matter

- TTF/OTF: the desktop formats. Uncompressed, served as-is they waste most of their bytes over the wire. They exist in web contexts mainly as the source files you convert from, and as the format iOS/Android native apps and desktop apps consume.
- WOFF: zlib compression plus a wrapper with metadata; roughly 40 percent smaller than raw TTF. Its era was IE9 through IE11 and early mobile browsers.
- WOFF2: Brotli compression plus font-specific table transforms; typically 20 to 30 percent smaller than WOFF and dramatically better for variable and CJK data. Support landed in Chrome 36, Firefox 39, and Safari 10, so every browser in realistic use today handles it.

Serving raw TTF or OTF as a webfont is a mistake in almost every case: bigger downloads, no compression benefit, and no table transforms. The only reason to keep a TTF in the pipeline is as the editable source for subsetting.

## What to ship

- Default: WOFF2 only. Every browser your analytics will show supports it.
- If a legacy browser truly matters (enterprise IE11, old Android WebView): add a WOFF fallback second in the src list. Do not add a TTF "just in case".
- One file per weight per style, or one variable file per family when using variable fonts; never ship both formats of the same face to the same browser.
- Set correct MIME types on the server: font/woff2 for .woff2. Wrong types cause console warnings and, on some CDNs, double-compression issues.

## Unicode-range splitting

The @font-face rule accepts a unicode-range descriptor: the browser downloads that face only when it encounters characters in the range. This turns one big multilingual file into several small ones:

- Google Fonts applies this automatically: a request for a family returns CSS declaring separate latin, latin-ext, cyrillic, cyrillic-ext, greek, vietnamese (and per-script) files with explicit ranges. A German page downloads only the latin file.
- CJK families are split into dozens of slices for the same reason; a page using a few hundred hanzi downloads a few slices, not megabytes.
- When self-hosting, replicate the pattern: split per subset (or per unicode-range slice for CJK), declare ranges precisely, and keep the mapping documented.
- The browser fetches each range file independently and in parallel once needed; the CSS itself must still arrive first, so keep @font-face declarations out of render-blocking bundles where possible (see the loading pipeline reference).

## Compression and caching realities

- WOFF2 is already Brotli-compressed; server-level gzip or brotli of .woff2 files wastes CPU for no gain. Exclude font extensions from compression rules.
- Fonts are cached like any static asset: hash the filename per version and serve with long-lived immutable caching. Combined with unicode-range, most returning visitors download nothing new.
- The crossorigin attribute matters even for same-origin fonts because fonts are fetched in CORS mode; a preload without crossorigin fetches the font twice.
- Sizes to expect, for calibration: a latin static weight of a UI sans lands around 15 to 40 KB as woff2; a full variable latin file around 50 to 300 KB depending on axis count; a CJK slice 5 to 60 KB; a full CJK weight in the megabytes. Compare against these before believing a size claim.

## Browser support notes that still matter

- Variable font support is universal in current browsers; the differences are in which named instances and axis behaviors work, not in whether the file loads.
- unicode-range is supported everywhere current; no feature detection needed.
- If you must support environments that cannot do WOFF2 (some webviews in kiosk hardware, ancient corporate builds), feature-detect via the CSS Font Loading API or simply accept the WOFF fallback for everyone, since the src list is evaluated per browser.
- iOS Safari ignores `text-size-adjust` in some modes and applies its own font inflation to small text; that is a sizing behavior, not a format issue, but it surfaces during format testing.

## Common mistakes

- Shipping TTF "because the foundry's download was a TTF" without converting; every foundry offers or permits web formats for licensed web use.
- Adding local() sources pointing at installed system fonts with the same family names; on machines with the font installed you get an uncontrolled version, and some browsers mishandle matching. Prefer remote sources only, unless you specifically want local reuse.
- Gzipping WOFF2 files at the CDN level; it changes nothing and burns CPU.
- One @font-face per weight with a new family name ("InterBold"), which breaks font-weight selection and synthesis logic; use one family name with weight descriptors.
- Forgetting crossorigin on preload, causing a duplicate download.
- Serving CJK content from a full-file self-hosted webfont because "Google Fonts slices seemed hacky"; the slicing is the solution, not the problem.

## Decision rules

- New project, no legacy constraints: WOFF2 only, one family, subset deliberately.
- Enterprise with IE11: WOFF2 plus one WOFF fallback, and test on the actual corporate build, not a simulator.
- Multilingual site: use per-subset files with unicode-range; treat "latin plus one script" as the normal case, not an exception.
- CJK: use a hosted sliced service or a documented self-hosted subset; never a full file for body text.
- Variable font in play: confirm the file's actual size against its static alternatives before committing; variable is not automatically smaller for a single weight.

## Comparison table

| Format | Compression | Table transforms | Relative size | Era and role today |
| --- | --- | --- | --- | --- |
| TTF/OTF | none of its own | none | baseline | source files; native apps |
| WOFF | zlib (deflate) | none | about 60% of raw TTF | IE9-IE11 era; legacy fallback only |
| WOFF2 | Brotli | glyf/loca and hmtx rewritten, restored on decode | WOFF minus another 20-30% | every current browser; ship this |

WOFF2's edge is not compression alone: the transforms restructure TrueType outlines and metrics so Brotli can squeeze them further, which is why variable and CJK files benefit most. The transforms are lossless: the browser restores the original table data on decode, so WOFF2 is a container optimization, not a redraw.

## Code notes

src is evaluated in order; the browser fetches the first format it supports:

```
@font-face {
  font-family: "Inter";
  src: url("/fonts/inter-400.woff2") format("woff2"),
       url("/fonts/inter-400.woff") format("woff");
  font-weight: 400;
  font-display: swap;
}
```

Modern browsers never request the WOFF line; it exists for the legacy tier you actually support, and only then. One format per face also keeps the src list honest: a woff2-only list is complete for every browser that can render the design.

Server configuration: correct MIME types, no re-compression:

```
location /fonts/ {
  types { font/woff2 woff2; font/woff woff; }
  # already compressed; do not re-compress at the edge
  gzip off;
  add_header Cache-Control "public, max-age=31536000, immutable";
}
```

The CSS Fonts 4 specification adds tech() keywords (for example format("woff2") tech("variations")); plain format("woff2") remains the interoperable form and is all a static or variable face needs today.

## Worked example

A two-weight family (400 and 700) goes from foundry download to production:

1. Source: the original TTFs from the foundry or the official repository; they stay in the repo as the source of truth.
2. Subset per the language matrix with pyftsubset --flavor=woff2; verify the output really is woff2 and not a silent uncompressed fallback.
3. Bytes: a latin static weight lands in the 15-40 KB range as woff2; the same files as raw TTF would be several times larger.
4. Declare one @font-face per weight with woff2-only src, font-display: swap, and unicode-range generated from the subsets.
5. Legacy tier: analytics shows IE11, so the WOFF line goes second in src and WOFF files are built for that tier only. No TTF is served.
6. Preload the 400 latin file with crossorigin; hashed filenames and immutable caching make repeat visits free.
7. Confirm in the network panel: exactly two font requests, both woff2, no WOFF fallback fetches, no TTF anywhere.

## Field notes

- If a font appears twice in the network panel, the preload URL did not match the @font-face URL, or crossorigin was missing.
- WOFF files can carry XML metadata (rights and license text); pipelines usually strip it, and its presence or absence is not license evidence either way.
- iOS Safari ignores text-size-adjust in some modes and inflates small text; the behavior surfaces while testing formats but is a sizing behavior, not a format issue.
- Serving raw TTF to keep it simple costs several times the bytes and skips the transforms; conversion is one command with fonttools.
- Never list both WOFF and WOFF2 for the same face and then serve only one: dead src entries are confusion, not compatibility.
- Converting with fonttools needs the brotli package for --flavor=woff2; a missing dependency yields silently uncompressed output.
- A WOFF fallback maintained out of habit, for a browser your analytics stopped showing years ago, is pure build and cache overhead; retire it deliberately.

## Common failure modes

- The WOFF fallback loads on modern browsers: woff2 was misspelled in the format hint or the order was inverted. First supported wins; check the network panel for which file actually fetched.
- Text renders but looks wrong on machines with the family installed: a local() source picked up an old desktop version instead of your files. Drop local() from primary faces.
- The preload downloads the font twice: crossorigin missing, or a URL mismatch down to the query string.
- A giant first load on a multilingual page: one full file instead of sliced subsets; replicate the unicode-range pattern self-hosted.
- WOFF2 served as application/octet-stream: wrong MIME invites wrong compression and caching behavior at edges; set font/woff2 explicitly.
- A variable file declared but statics render: two @font-face blocks share the family name and weight, and the later rule wins. Keep one system per family and style.
- The format list keeps a TTF third "just in case": it inflates the CSS, adds maintenance, and modern browsers never touch it. Delete it.
- WOFF and WOFF2 of one face drift apart in coverage: build both from the same subset recipe so the legacy tier never silently loses glyphs.

## Quick reference

- Ship WOFF2 only; add WOFF second in src only for a named legacy tier, decided from analytics and documented.
- TTF and OTF are source files, not webfonts.
- font/woff2 MIME type, no edge re-compression, hashed filenames, immutable cache.
- WOFF2 means Brotli plus table transforms; WOFF means zlib only; TTF means neither.
- Verify the format with the network panel or the file's magic bytes (woff2 files start with wOF2), not by extension.
- When a legacy tier exists, test on the actual browser build; a WOFF fallback that was never exercised is dead weight.
- unicode-range splitting is orthogonal to format choice: it composes with WOFF2, WOFF, or (never) TTF alike.
- One format per face per browser: a woff2-only src list is complete for every current engine.

## Cross-references

- [Font-face and CSS](font-face-and-css.md)
- [Subsetting and performance](subsetting-and-performance.md)
- [CJK fundamentals](../scripts/cjk-fundamentals.md)
- [Font loading pipeline](font-loading-pipeline.md)

Compiled 2025 as part of the Fontlore project.
