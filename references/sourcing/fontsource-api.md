# Fontsource REST API

What this reference covers: How Fontsource packages and its REST API work, and when to prefer them over the Google Fonts CDN or raw repository files. It covers npm package conventions, the list and single-font endpoints, variable font packages, and version pinning for reproducible builds.

Fontsource is a packaging layer for open-source fonts: it turns Google Fonts and other open families into npm packages you can self-host with a bundler. Because everything is versioned on npm, it is the cleanest path to reproducible typography in modern web stacks.

## What Fontsource actually is

- Each family becomes one or more npm packages: static packages like @fontsource/inter split weights and subsets into CSS entry points, while variable packages like @fontsource-variable/inter ship a single variable file.
- Packages are built from upstream sources and re-versioned as upstream releases. Checking the npm changelog is a reasonable proxy for "the font changed".
- Because files live in your own bundle and origin, you control caching, subsetting downstream, and availability. No third-party CDN request is required at runtime.
- The project covers more than Google Fonts; several independent open-source families that never joined Google Fonts are packaged too.
- Licensing travels with the package: OFL and Apache fonts include their license files, which keeps due-diligence simple.

## Package conventions

- Static families: install one package, then import weight CSS files, for example @fontsource/inter/400.css or @fontsource/inter/700.css. Each import declares font-face rules with unicode-range subsets so browsers only fetch what they render.
- Subset-specific entry points exist for most families (for example latin-only or latin-ext files) when you want to trim requests further.
- Variable families: @fontsource-variable/inter exposes the full weight range by default, with separate entry points for axis combinations on some families. Import once and set font-weight freely in CSS.
- Italic styles in static packages are separate imports, which surprises teams used to Google's combined requests.
- Component-library authors can re-export Fontsource imports so downstream apps inherit correct licensing and files without manual font management.

## REST API endpoints

The Fontsource API at api.fontsource.org gives you machine-readable metadata without installing anything. Two endpoints do most of the work:

```
GET https://api.fontsource.org/v1/fonts?family=inter
GET https://api.fontsource.org/v1/fonts/inter
```

- The list endpoint accepts filters such as family, subsets, weights, and styles, and returns an array of font objects. Use it to answer "which families cover Latin-ext with a 300 weight".
- The single-font endpoint returns one font object: the family id, category, subsets, weights, styles, and a variable flag. Treat the exact response schema as the source of truth rather than memorizing fields.
- The API also exposes variable-font listings and download helpers; consult the API documentation on fontsource.org for the current endpoints instead of guessing at URLs.
- The family id in the API matches the npm package suffix, which makes scripts that go from "API result" to "install command" trivial to write.
- Responses are JSON and cacheable; for bulk work, paginate or cache results locally rather than hammering the endpoint in a loop.

## Version pinning

- Pin exact versions in package.json (no caret or tilde) when typography must be reproducible across environments and teammates.
- Record the version you validated in your font manifest. A design review that approves version A should not be silently upgraded to version B by a dependency bump.
- Renovate-style bots are useful, but route font package updates through the same review as code changes: glyph changes are user-visible.
- When upstream releases a new weight or script coverage, the Fontsource package updates after the packaging pipeline runs; the API and npm can briefly lag the upstream release.
- For total determinism, vendor the files into the repository and record the upstream version and license in a manifest; npm pinning is usually enough, vendoring is for regulated contexts.

## Choosing between delivery paths

- Google Fonts CDN: fastest to start, zero build integration, no version pinning, third-party origin request.
- Fontsource npm packages: reproducible, in-bundle, subset-aware, easy licensing audit; requires a bundler.
- google/fonts repository files: the upstream truth, good for design tools and audits; you manage formats and subsetting yourself.
- Foundry self-host kits: needed for commercial fonts; Fontsource does not package proprietary families.
- For most product teams the decision is CDN for prototypes and marketing sites, Fontsource or vendored files for applications.

## Workflow

1. Search the Fontsource website or the API list endpoint for the family and confirm subsets and weights match the brief.
2. Install the package (static or variable) and import the entry points you need.
3. Pin the exact version and add family, version, and license to the project font manifest.
4. Verify rendering at target sizes and scripts, including numeral alignment and diacritics.
5. Set a dependency-update policy for font packages; treat glyph-affecting updates as user-visible changes.

## Common mistakes

- Importing every weight "just in case"; each import is real bytes in the bundle.
- Mixing the CDN and Fontsource for the same family, producing two different versions in one product.
- Reading the API schema from memory instead of the current documentation; fields evolve.
- Forgetting that italic static styles are separate imports and shipping a family without its true italic.
- Assuming a package exists because the family exists; niche independent fonts may not be packaged, and the answer is vendoring, not improvising.
- Upgrading font packages silently during routine dependency sweeps.

## Comparison table: delivery paths

The same family usually reaches a product through one of four paths, and they differ in pinning, origin, and auditability. Mixing two paths for one family is how a codebase ships two versions of the same typeface without noticing.

| Path | Version pinning | Served from | Subsetting | License evidence |
| --- | --- | --- | --- | --- |
| Google Fonts CDN | None; always the latest revision | Google origin | Automatic unicode-range | Not shipped to you; keep your own copy |
| Fontsource npm | Exact npm version | Your bundle and origin | unicode-range plus subset entry points | License file inside the package |
| google/fonts files | You tag or vendor the commit | Your origin | You subset (pyftsubset or similar) | OFL.txt beside the file |
| Foundry self-host kit | Per foundry terms | Your origin | Per kit | Purchase documents |

For product teams the pattern is CDN for prototypes and marketing pages, npm packages or vendored files for applications where reproducibility is a requirement.

## Worked example: pinning a family end to end

Scenario: a product team standardizes on Inter for UI, needs weights 400 through 700, and requires reproducible builds across environments.

1. Query before installing: `curl https://api.fontsource.org/v1/fonts/inter` and read subsets, weights, styles, and the variable flag from the JSON response.
2. Choose static versus variable: explicit weight imports keep the payload minimal; the variable package suits systems that want intermediate weights such as 450 or 550 for hover and pressed states.
3. Install with an exact version in package.json (no caret, no tilde) and import only the weight CSS files the design review approved.
4. Add subset-scoped entry points (the latin-ext variants) when content is European multilingual, so diacritic coverage arrives without extra requests.
5. Record family, exact version, license (OFL-1.1 for Inter), and the review date in the font manifest.
6. Route future font-package updates through the same review as code changes; a dependency bot bump that shifts glyphs is a user-visible change, not housekeeping.
7. Verify in the browser: rendered text resolves to Inter, woff2 files load from your own origin, and no fonts.googleapis.com request appears anywhere.

## Quick reference: install patterns

```
npm install @fontsource/inter --save-exact
npm install @fontsource-variable/inter --save-exact
```

- Static pattern: import `@fontsource/inter/400.css`, `@fontsource/inter/700.css`, and `@fontsource/inter/400-italic.css` when a true italic is approved. Each import carries unicode-range rules, so browsers fetch only the subsets they render.
- Variable pattern: one import exposes the full weight axis; confirm the default axis configuration matches the weights named in your tokens before deleting the static fallbacks.

## Tool notes

- List endpoint queries answer coverage questions before anyone falls in love with a face: a subsets query on the v1 fonts endpoint returns families with that coverage declared.
- `npm view @fontsource/inter versions --json` shows release cadence; the npm publish date is a legitimate "the font changed" signal for packaged families.
- Read the LICENSE file inside `node_modules/@fontsource/<family>/` during review; the license travels with the package, so due diligence is a local file read rather than a web hunt.
- The API's variable listings surface variable families separately; treat that metadata as a claim, then confirm the actual axes in the shipped file with an inspector such as fontdrop or Wakamai Fondue.

## Signals to trust

- The family id in the API response matching the npm package suffix exactly; that correspondence is the API's most reliable contract.
- Declared subsets that match what the glyph grid actually shows when you open one shipped file.
- Upstream release notes whose dates line up with npm publish dates.

## Signals to distrust

- Memory of the response schema; fields have changed before and will again, so read the current docs or a live response.
- Assuming a package exists because the family is famous; niche independent families are often unpackaged, and the right answer is vendoring, not improvising a fork.
- Assuming the variable package and the static package render identically; axis defaults can differ from the named static styles.

## Field notes

- Static italic is a separate import: an approval of weights 400 and 700 does not include a true italic unless you import it, and synthetic oblique is what ships otherwise.
- Packaging lags upstream releases by days sometimes; a glyph fix you need immediately may mean vendoring from the google/fonts repository until the package catches up.
- Bundle math is real: every imported weight file is bytes on the wire, so nine weights "just in case" is a measurable performance decision.
- Version discipline pays at audit time: an exact pin plus a manifest entry turns "which Inter is this?" into a one-line answer.
- If a family is on Fontsource but not Google Fonts, it is often an independent open-source project; verify the upstream repository yourself instead of assuming Google-grade maintenance.

## Questions to ask before adopting

- Which delivery path does this family take in each environment (local dev, CI, production), and is it the same path everywhere?
- Who reviews font-package updates, and what makes a glyph change trigger a design review rather than an automatic merge?
- Do we need the variable build's full range, or would three static weights cover the system with less payload?
- Which subsets do our real users need versus what the package declares?
- Where does the license file live in the repository, and who owns keeping it current?

## Cross-references

- [Google Fonts Catalog](google-fonts-catalog.md)
- [The google/fonts repository](google-fonts-repository.md)
- [Evaluating catalog metadata](evaluating-catalog-metadata.md)
- [Webfont embedding rights](../licensing/webfont-embedding-rights.md)

Compiled 2025 as part of the Fontlore project.
