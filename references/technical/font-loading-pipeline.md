# Font Loading Pipeline

What this reference covers: The end-to-end delivery of fonts: self-hosting versus CDN, preload done correctly, Fontsource as an npm workflow, caching headers, and avoiding render-blocking pitfalls. The pipeline, not the font choice, is where most real-world font performance is won or lost.

## Self-host versus third-party CDN

- Self-hosting (fonts in your repo or origin): full control of caching and subsetting, no third-party requests, no privacy exposure. A German regional court ruling in 2022 made the privacy angle concrete: loading fonts from a third-party CDN exposed visitors' IP addresses, and sites moved to self-hosting en masse. Treat self-hosting as the default for production.
- Third-party hosting (Google Fonts CSS API and similar): convenient, sliced per unicode-range, globally cached; but it adds a third party to every page view, a privacy dependency, and a version you do not control. Acceptable for prototypes and internal tools.
- Fontsource sits in between: fonts as npm packages, self-hosted through your build, with per-weight and variable packages and consistent file naming. For bundler-based projects it is the least-friction self-hosting path: import "@fontsource/inter/400.css" or "@fontsource-variable/inter" and the build pipeline handles files and versions.

## Preload, done right

Preload promotes a font fetch to critical path priority:

- link rel="preload" as="font" type="font/woff2" href="/fonts/inter-latin-400.woff2" crossorigin
- crossorigin is required even for same-origin fonts because font fetches are CORS-mode requests; omitting it causes a double download.
- Preload only what first paint actually renders: usually one or two faces, one subset each (the latin body face; the heading face if it paints immediately).
- The preloaded URL must match the @font-face URL exactly, including any query string. A mismatched preload is pure waste.
- Do not preload CJK slices or fallback-subset files; they load on demand by design.

## CSS delivery matters more than the font tag

- Keep @font-face declarations in the main stylesheet or inline them early; a separate fonts.css fetched late delays font discovery past first paint.
- Avoid @import for font CSS: it serializes requests (CSS must be fetched, parsed, then the import fetched) and is effectively a render-blocking chain. Bundle or inline instead.
- font-display: swap pairs with this pipeline so text is never invisible while the (well-prioritized) font arrives.
- For single-page apps, ensure the font CSS is in the initial chunk, not a lazily loaded route chunk, or the first paint falls back on every hard navigation.

## Caching and versioning

- Filenames should carry a content hash; Cache-Control: max-age=31536000, immutable makes every revisit free.
- On version upgrades, the new hash forces refetch; keep the old files around briefly if you must, but immutable plus new hash is the standard pattern.
- Record the font version you vendored (from the font's name table or the package version) next to the files; silent upgrades change metrics and features.
- For Fontsource, the package version in package.json plus your lockfile is the version record; pin exactly and update deliberately, not via floating ranges.

## A reference pipeline

1. Choose faces and subsets from the language matrix; generate woff2 subsets with documented tooling (or take Fontsource packages).
2. Commit font files with license files included; record version and source URL in a fonts manifest.
3. Declare honest @font-face blocks with unicode-range, font-display: swap, and metric-adjusted fallbacks.
4. Preload the one or two faces that paint first, with crossorigin.
5. Serve with hashed filenames and immutable caching; exclude woff2 from recompression.
6. Verify under throttling: no invisible text, minimal layout shift, no duplicate downloads, no fonts on the critical path that first paint does not use.

## Common mistakes

- Third-party CDN in production with no privacy review; the cost is not performance, it is data protection.
- Preloading four weights and a display face, starving the CSS and JS that first paint needs.
- @import chains for font CSS, then blaming the font for slow text.
- Missing crossorigin on preload, doubling the download of the exact file you tried to prioritize.
- Serving fonts from a cookieless different domain without CORS headers; the fetch fails silently and the fallback sticks forever.
- No version pinning: a CDN-hosted family updates, metrics shift, and layouts drift with no change on your side.

## Decision rules

- Production site of any kind: self-host; use Fontsource or vendored files.
- Prototype or internal tool: hosted CSS API is fine; keep the swap to self-hosting cheap by keeping declarations centralized.
- App shell with known UI strings: subset to usage, preload the body face, immutable cache.
- Content site with many pages and scripts: unicode-range slicing plus swap, preload only the latin body face.
- Any pipeline change: re-run the throttled-load checklist; font regressions arrive quietly.

## Comparison table

| Delivery model | Control | Third party per view | Versioning | Fits |
| --- | --- | --- | --- | --- |
| Vendored files in the repo | full | none | your content hashes | production default |
| Fontsource npm packages | full | none | package.json plus lockfile | bundler projects |
| Google Fonts CSS API | low | Google sees each visitor IP | theirs, moving | prototypes, internal tools |
| Commercial hosted service | medium | the vendor | theirs | existing enterprise contracts |

## Worked example

Shape of the waterfall, same page, same font, two pipelines. Times are illustrative; the order of events is the point.

Self-hosted with preload:

1. t=0: HTML arrives; the head inlines the font declarations.
2. t=100 ms: the preload starts the font fetch at high priority, alongside CSS.
3. t=350 ms: CSS parsed, layout needs Inter, fetch already in flight.
4. t=400 ms: first paint renders with the webfont; no fallback phase exists.

Self-hosted behind @import:

1. t=0: HTML arrives.
2. t=100 ms: base CSS fetched.
3. t=200 ms: @import discovered; fonts.css fetched.
4. t=250 ms: font fetch begins, after two CSS round trips.
5. t=600 ms: first paint falls back; the swap lands later and reflows.

The fix is structural, not a faster server: inline or bundle the declarations, preload the one face first paint needs. Times vary per network; the ordering of events never does.

## Code notes

```
<link rel="preload" href="/fonts/inter-latin-400.woff2"
      as="font" type="font/woff2" crossorigin>
```

crossorigin is required even for same-origin files: font fetches are CORS-mode requests, and a preload without it fetches the same file twice.

```
location /fonts/ {
  # fonts are immutable and already compressed
  add_header Cache-Control "public, max-age=31536000, immutable";
  gzip off;
}
```

```
<link rel="preconnect" href="https://fonts.example.com" crossorigin>
```

preconnect warms a connection to an origin you genuinely need; it is not a substitute for self-hosting, and declaring it for unused origins wastes connections.

## Field notes

- Chrome warns in the console when a preloaded resource goes unused; that warning is how most mismatched preload URLs get discovered.
- The Munich regional court ruling of January 2022 treated serving Google Fonts from Google's CDN as transmitting personal data (the visitor's IP address) without consent; European production sites have largely treated self-hosting as mandatory since.
- Single-page apps: font declarations belong in the initial chunk. A route-level chunk means every hard navigation to that route starts the font clock late.
- A CDN in front of self-hosted fonts is fine; the privacy cost appears when the third party is the font origin, not the cache.
- A version bump needs no cache purge with hashed filenames: immutable plus a new hash is the entire story.
- Measure on a mid-tier Android with throttling on: desktop throttling hides most font pipeline problems.
- Fonts and images share one connection budget: a preloaded hero image plus two preloaded fonts is real contention on 4G, so sequence deliberately.
- A font URL change in a redesign re-downloads the file for every visitor; versioning is a deliberate act, not an accident of the build.

## Common failure modes

- The font loads twice: preload without crossorigin, or a preload URL that differs from the @font-face URL. One file, one URL, byte for byte.
- The fallback sticks forever: the font fetch failed (missing CORS headers on the font origin, a blocked domain, a 404) and swap has nothing to swap in. Check the network panel for the failed request before touching CSS.
- Layout shifts on every route change in an SPA: font declarations live in a lazily loaded chunk, so each hard navigation re-runs discovery and loading. Move them to the initial chunk.
- A "performance fix" moved fonts to a separate domain and made things worse: new DNS and TLS handshakes plus CORS overhead outweighed any cache sharing; same-origin wins unless the CDN is genuinely justified.
- Hosted CSS API left in production: the provider's outage or redesign becomes your text rendering; migrate declarations in-repo before launch, while the swap is still a one-file change.
- Fonts load in dev but never in staging: the asset host strips CORS headers or serves a different path. Font fetch failures are silent, so assert font loading in smoke tests.
- The font cache is cold on every visit: Cache-Control is missing or overridden by a CDN default. Check the response headers, not the config file.

## Quick reference

- Production: self-host (vendored files or Fontsource), hashed filenames, immutable cache.
- Preload: one or two faces maximum, exact URL match, crossorigin always.
- Font CSS: inline early or in the main stylesheet; never behind @import.
- font-display: swap with metric-adjusted fallbacks for content text.
- Never preload CJK slices or fallback-subset files; they load on demand by design.
- Verify: throttled cold load, no duplicate downloads, no invisible text, minimal shift.

## Cross-references

- [Font display strategies](font-display-strategies.md)
- [Webfont formats](webfont-formats.md)
- [Fallback metrics and CLS](fallback-metrics-and-cls.md)
- [CSS handoff snippets](../workflow/css-handoff-snippets.md)

Compiled 2025 as part of the Fontlore project.
