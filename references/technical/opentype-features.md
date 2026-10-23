# OpenType Features

What this reference covers: What OpenType layout features are, the common four-character tags and what each does, how to enable them in CSS with high-level properties first, and how to discover which features a given font actually ships. Features are the difference between a font installed and a font used well.

## What features are

OpenType features are named substitutions and positionings inside the font, stored in GSUB (substitutions: alternate glyphs, ligatures) and GPOS (positioning: kerning, mark placement). Some are on by default in browsers (kerning, standard ligatures, contextual alternates); most are off and must be enabled. Which features exist is a per-font fact: two fonts can both "have OpenType features" and share almost none.

## The tags worth knowing

- liga: standard ligatures (fi, fl), on by default. dlig: discretionary ligatures (st, ct flourishes), off by default, display use only.
- calt: contextual alternates, usually on; adjusts glyphs in running text.
- smcp: true small caps (lowercase to small capitals). c2sc: capitals to small capitals, combined with smcp for all-small-caps lines.
- lnum and onum: lining versus old-style figures. pnum and tnum: proportional versus tabular figures. These four are the backbone of numeric typography.
- frac: built fractions from digit-slash-digit; numr and dnom: numerator and denominator glyph forms for custom fractions; ordn: ordinals (1st with a proper superscript); sups and sinf: superiors and scientific inferiors; zero: slashed zero.
- ss01 through ss20: stylistic sets, family-specific alternates (single-story a, alternate ampersands, disambiguated Il1 sets). cv01 through cv99: character variants, finer-grained per-glyph choices.
- salt: stylistic alternates in general; swsh and cswh: swashes; case: punctuation for all-caps settings.
- locl: localized forms, applied automatically per language tag (Serbian italic Cyrillic forms are the famous example).
- mark and mkmk: mark-to-base and mark-to-mark positioning; these plus abvm/blwm are the machinery behind complex scripts and should never be manually disabled.

## Enabling in CSS, high-level first

- Numbers: font-variant-numeric: tabular-nums, lining-nums, oldstyle-nums, proportional-nums, slashed-zero, diagonal-fractions, ordinal. These compose: tabular-nums lining-nums is a normal declaration.
- Caps: font-variant-caps: small-caps or all-small-caps. If the font lacks smcp, browsers synthesize scaled capitals, which looks acceptable at best; check for real smcp before styling small-caps-heavy layouts.
- Ligatures: font-variant-ligatures: common-ligatures no-discretionary-ligatures; no-common-ligatures for code or data where fi ligatures cause search problems.
- East Asian variants: font-variant-east-asian exists for JIS forms; rarely needed, but real.
- Named alternates: define @font-feature-values for a family, then use font-variant-alternates: styleset(fancy-caps); this keeps feature numbers out of component code.
- Low-level: font-feature-settings: "ss01" 1, "cv05" 2. Use it only where high-level properties cannot reach (custom sets, character variants), and keep it out of the way of the font-variant properties on the same element, since it overrides them wholesale.

## Discovery: finding what a font actually has

- Wakamai Fondue: drop the font file, get a full feature list with toggles and live previews; the fastest way to see whether the small caps are real.
- FontDrop: inspect the GSUB table directly; useful when you need to know which script systems and languages a feature covers.
- Google Fonts specimen pages list supported features per family for hosted fonts.
- The foundry's specimen PDF or type tester: authors usually demonstrate their best features.
- For automation: fonttools can dump feature tags, and Wakamai Fondue's output can anchor a design-system decision record.

## What belongs in a design system

Document per role, not per element: body text gets defaults plus (for editorial faces) onum where it reads well; tables and dashboards get tnum; kickers and labels get case plus tracking but no dlig; display moments may enable chosen stylistic sets. Encode these as tokens or utility classes so features are decisions, not folklore. Note that features must be tested per font version: an upgrade can renumber stylistic sets, which is one more reason version pinning matters.

## Common mistakes

- Enabling every stylistic set "to get the most out of the font"; sets are curated per family and several are mutually exclusive or situational.
- Using discretionary ligatures in body text; search and copy-paste remain text, but reading suffers.
- Assuming small-caps will be real small caps; without smcp the browser fakes them, and the fake is obvious at headline sizes.
- font-feature-settings: "kern" 0 or disabling ligatures globally out of superstition; kerning should stay on for text, and liga exists for good reason.
- Relying on font-feature-settings alone and fighting inheritance; high-level properties exist because they compose.
- Testing features in one tool and shipping to another; browser support for individual CSS properties (font-variant-alternates in particular) should be verified in your actual target browsers.

## Decision rules

- Data-dense UI: tnum is a hard requirement; check before shortlisting, not after.
- Editorial body: onum only if the font's old-style set is well drawn; a clumsy onum is worse than lining.
- Brand display: pick up to two stylistic sets or alternates as part of the brand, and freeze them in tokens.
- Code and technical strings: disable ligatures deliberately; fi in "config" causing search misses is a real bug report.
- Complex scripts: never disable mark positioning features; if marks render badly, change fonts, do not fight the shaper.

## Comparison table

| Tag | Name | Default | Reach it with |
| --- | --- | --- | --- |
| kern | kerning | on | font-kerning: auto |
| liga | standard ligatures | on | font-variant-ligatures: common-ligatures |
| calt | contextual alternates | on | font-variant-ligatures: contextual |
| dlig | discretionary ligatures | off | font-variant-ligatures: discretionary-ligatures |
| smcp | small caps | off | font-variant-caps: small-caps |
| c2sc | capitals to small caps | off | font-variant-caps: all-small-caps |
| lnum | lining figures | font default | font-variant-numeric: lining-nums |
| onum | oldstyle figures | font default | font-variant-numeric: oldstyle-nums |
| pnum | proportional figures | font default | font-variant-numeric: proportional-nums |
| tnum | tabular figures | font default | font-variant-numeric: tabular-nums |
| frac | fractions | off | font-variant-numeric: diagonal-fractions |
| ordn | ordinals | off | font-variant-numeric: ordinal |
| sups | superiors | off | font-variant-position: super |
| zero | slashed zero | off | font-variant-numeric: slashed-zero |
| ss01-ss20 | stylistic sets | off | font-feature-settings or @font-feature-values |
| cv01-cv99 | character variants | off | font-feature-settings |
| salt | stylistic alternates | off | font-feature-settings |
| swsh, cswh | swashes | off | font-variant-alternates: swash() |
| case | case-sensitive forms | off | font-feature-settings: "case" 1 |
| locl | localized forms | auto per language | the lang attribute, not CSS |
| mark, mkmk | mark positioning | on | leave alone |

## Code notes

Tables and data, composed with high-level properties:

```
table, .metric, .price {
  font-variant-numeric: tabular-nums lining-nums;
}
```

Editorial body on a face whose oldstyle figures are well drawn:

```
article p {
  font-variant-numeric: oldstyle-nums proportional-nums;
}
```

Search-safe code blocks (an fi ligature inside "config" breaks text search on some engines):

```
pre, code, kbd {
  font-variant-ligatures: none;
}
```

All-caps labels: the case feature swaps in punctuation sized for capitals:

```
.label {
  text-transform: uppercase;
  font-feature-settings: "case" 1;
}
```

Named alternates keep the numeric tag in exactly one place:

```
@font-feature-values "Brand Serif" {
  @styleset { quirky: 3; }        /* binds to ss03 */
}
.display { font-variant-alternates: styleset(quirky); }
```

Standing rule: on one element, font-feature-settings overrides font-variant-* wholesale; set one layer per element, never both.

## Worked example

A finance dashboard is built on a new UI face. The numeric requirements, walked:

1. Requirement: currency columns align, percentages compare, and zero must not read like capital O.
2. Check the face actually ships tnum and zero before shortlisting (Wakamai Fondue feature list, or FontDrop on the GSUB table). The CSS property is a request, not a capability.
3. Apply at the container: table { font-variant-numeric: tabular-nums slashed-zero; }.
4. Verify with real strings in the browser: 1,234.56 stacked over 876.54 and 98.7; the digits must share advance widths.
5. Keep the decision in a token (for example --numeric: tabular-nums slashed-zero) so tables, inputs, and chart labels inherit the same setting.
6. Record the feature tags the UI depends on; the font-quality-tooling reference diffs these tags on every font upgrade.

## Field notes

- Tags are per-family facts: ss02 in one family has nothing to do with ss02 in another. Tokens should bind family and tag together, never a bare tag.
- Feature support is per-version too: an upgrade can renumber stylistic sets, and the page keeps rendering with different glyphs, silently.
- Browsers enable kern, liga, and calt by default; font-feature-settings: "kern" 0 in a reset is superstition with a real cost in text quality.
- Without smcp in the file, the browser fakes small caps by scaling capitals; acceptable at caption sizes, obviously wrong at display sizes.
- Google Fonts specimen pages list supported features per family; for self-hosted files, trust only the file itself.

## Quick reference

- Numbers in tables and data UI: font-variant-numeric: tabular-nums.
- Editorial body: oldstyle-nums proportional-nums, on a face that draws them well.
- Code blocks: font-variant-ligatures: none, so text search survives ligatures.
- All-caps labels: text-transform: uppercase plus "case" 1.
- Small caps: only when smcp exists in the file; otherwise choose another treatment.
- Stylistic sets: through @font-feature-values, one definition per family, tokens over raw tags.
- Never disable kern, mark, or mkmk; they are load-bearing in running text and complex scripts.

## Cross-references

- [Numerals and notation](../scripts/numerals-and-notation.md)
- [Variable fonts and axes](variable-fonts-and-axes.md)
- [Inspecting font files](inspecting-font-files.md)
- [Editorial and news](../applications/editorial-and-news.md)

Compiled 2025 as part of the Fontlore project.
