# Inspecting Font Files

What this reference covers: The tools that open a font file and tell the truth about it: Wakamai Fondue, FontDrop, Samsa, Axis-Praxis, and Fontspector, plus the fonttools command line. Each reveals different facts; knowing which tool answers which question is the skill. Use these before licensing decisions, during CSS work, and when something renders oddly.

## Wakamai Fondue: the overview tool

Drop a font on the site and get: character set and language coverage, OpenType features with live toggles, variable axes with ranges and named instances, vertical metrics, and suggested fallback metrics including size-adjust values.

- Use it when shortlisting: does this face have real small caps, a tnum set, the axes the design calls for?
- Use it during CSS work: its fallback-metrics output feeds adjusted fallback declarations directly.
- Limits: it shows what is in the file, not whether the drawing is good; and web tools should not receive unreleased or confidential fonts (see the caution below).

## FontDrop: the table browser

FontDrop exposes the raw structure: cmap (which codepoints map to which glyphs), name (version, foundry, license strings), OS/2 and head (metrics), GSUB/GPOS (feature tables), and a glyph inspector.

- Use it to answer precise questions: is U+20B9 (rupee) in the cmap? What version string does the name table carry? Does the license field match what the vendor said?
- The glyph inspector shows actual outlines and components, useful when a suspicious glyph (a badly drawn mark, a broken conjunct) needs confirming as a font issue rather than a rendering issue.
- It is also the tool for forensics on fonts of unclear origin: version strings, designer credits, and embedded license text often reveal whether a "free download" site distributed something legitimately.

## Samsa: the variable font inspector

Samsa loads a variable font, exposes every axis, and renders arbitrary axis combinations plus the named instances; it also shows how interpolation moves outlines.

- Use it when evaluating a variable family: does the wght axis interpolate smoothly, does opsz change texture convincingly, do custom axes do anything worth using?
- It renders single glyphs at large sizes, which is exactly how you catch interpolation defects (kinks, broken overlaps) that browser rendering at text sizes hides.
- Pair with Axis-Praxis, a playground for driving variable axes interactively across a set of fonts; good for demos and for stress-testing how a family behaves between default instances.

## Fontspector: the quality linter

Fontspector is the maintained successor to FontBakery: a check suite that lints fonts for structural and quality issues (missing tables, problematic name table entries, cmap coverage gaps, metrics anomalies, license-string consistency) and reports failures with explanations.

- Use it in due diligence on an open font before adopting it, and in CI for any font your team maintains or subsets.
- It complements the visual tools: Fondue tells you what is there, Fontspector tells you what is wrong.

## fonttools on the command line

The Python toolkit underlies most of the above:

- ttx dumps any font to XML tables: ttx -t cmap font.ttf for coverage, ttx -t name for version strings.
- fonttools subset (pyftsubset) is the subsetting engine; fonttools varLib handles variable font work.
- hb-shape (from HarfBuzz) is the shaping counterpart: it shows which glyphs a shaper selects for a string, which separates font bugs from browser bugs when complex scripts misbehave.

Use local tools whenever the font is unreleased, client-supplied under NDA, or proprietary; web inspectors mean uploading the file, which is a confidentiality decision, not a technical one.

## Which tool when

- Shortlisting a font: Wakamai Fondue for features and axes; FontDrop cmap for the specific codepoints your languages need.
- Debugging rendering: hb-shape for shaping questions; FontDrop glyph inspector for outline questions; Samsa for axis questions.
- Due diligence: Fontspector checks, FontDrop name table for provenance, cmap diff against your language matrix.
- Building fallbacks: Wakamai Fondue metrics output, verified with a side-by-side render.
- CI for maintained or subsetted fonts: Fontspector plus a cmap diff in the pipeline.

## Common mistakes

- Trusting catalog metadata over the file: vendor pages and aggregator listings are marketing; the name table and cmap are facts.
- Uploading confidential or client fonts to web tools without thinking; use fonttools locally instead.
- Evaluating variable fonts only at default instances in a browser; interpolation defects live between instances, which is what Samsa is for.
- Reading feature lists as quality guarantees: a font can list smcp and ship ugly ones. Features are present-or-not; good is a visual judgment.
- Skipping the name table version check before reporting a bug upstream; the first question any foundry asks is which version you have.
- Using one tool as the whole answer; each tool sees one slice of the file, and the slices disagree more often than you would guess.

## Decision rules

- Before a licensing decision: name table (provenance), cmap (coverage), Fontspector (structural health). Ten minutes, no exceptions for "well-known" fonts.
- Before writing CSS against a face: Fondue for features and fallback metrics.
- Before adopting a variable family: Samsa pass across axis extremes, not just defaults.
- Before debugging "the font is broken": hb-shape to establish whether shaping selects the right glyphs at all.
- Any web-tool upload: confirm the font's license and confidentiality status first.

## Comparison table

| Tool | Interface | Reveals | Upload needed |
| --- | --- | --- | --- |
| Wakamai Fondue | web | features with live toggles, axes, instances, metrics, fallback suggestions | yes |
| FontDrop | web | raw tables: cmap, name, OS/2, head, GSUB, GPOS; glyph outlines | yes |
| Samsa | web | variable design space, axis extremes, per-glyph interpolation | yes |
| Axis-Praxis | web | interactive axis driving across a set of fonts | yes |
| Fontspector | CLI | lint profile: structure, tables, license strings | no |
| fonttools / ttx | CLI | any table as XML; subsetting; variable instancing | no |
| hb-shape | CLI | shaping decisions: which glyphs a shaper picks | no |

## Code notes

```
ttx -t name MyFont.ttf     # version, foundry, license strings
ttx -t cmap MyFont.ttf     # coverage: codepoint to glyph map
ttx -t OS/2 MyFont.ttf     # fsType embedding bits, weight class
ttx -t hmtx MyFont.ttf     # advance widths for fallback metric math
```

Variable font work without a browser:

```
fonttools varLib.instancer MyFont-VF.ttf wght=550 -o MyFont-wght550.ttf
fonttools ttLib.woff2 compress -o MyFont-wght550.woff2 MyFont-wght550.ttf
```

hb-shape separates font bugs from browser bugs: if it selects the expected glyphs but the browser does not, the bug is in the CSS or the browser; if hb-shape also selects wrong glyphs, it is the font.

## Worked example

Provenance check on a font that arrived from a "free fonts" aggregator, before anyone uses it:

1. Name table (ttx -t name): read the version string (name ID 5), the PostScript name (ID 6), and the license fields (IDs 13 and 14). A license URL pointing to a foundry other than the seller, or a version older than the vendor's current release, is a finding.
2. Embedding permission (OS/2 fsType): 0 means installable embedding, 2 means restricted, 4 means preview and print, 8 means editable. A "free" file declaring restricted embedding is a contradiction to resolve before use, not after.
3. Coverage: dump the cmap and diff it against the official character set of the family (the upstream repository or the foundry specimen). Missing ranges mean an old, stripped, or rebuilt file.
4. Structure: a Fontspector pass for table sanity.
5. Verdict: any failed step means the file is not what the vendor says it is; go upstream and license from the source.

## Field notes

- Name IDs 1 and 2 are the family and subfamily the OS groups by; IDs 16 and 17 carry the typographic family and subfamily for designs with more than four styles. When a font "splits into two families" in an application, these fields disagree.
- fsType is advisory in practice (many tools ignore it), but it is written evidence of intent, which makes it useful in a license audit.
- ttx output is XML and diffs cleanly in code review; keep dumps of shipped fonts in the repo so upgrades produce reviewable diffs.
- Wakamai Fondue and FontDrop are the fastest human tools, but they are uploads; for confidential files the CLI tools cover the same ground.
- Samsa at large glyph sizes exposes interpolation kinks that browser rendering at text sizes hides; check axis extremes, not just the default instance.
- Keep one ttx dump per shipped font in the repo; the upgrade diff becomes a reviewable artifact instead of a memory test.
- Samsa and Axis-Praxis come from the same author, and their axis handling is consistent; they make good companions for variable font work.

## Quick reference

- "What features and axes does this file have?" - Wakamai Fondue.
- "Is codepoint X in the cmap?" - FontDrop, or ttx -t cmap.
- "Which version and license strings?" - ttx -t name; read name IDs 5, 13, and 14.
- "Why does interpolation look wrong between instances?" - Samsa at glyph size.
- "Is the file structurally sound?" - Fontspector.
- "Font bug or browser bug?" - hb-shape first, then the glyph inspector.
- "Can this file be legally embedded?" - fsType in OS/2 plus the license text, then the foundry in writing.
- "Which axis ranges does the variable file span?" - Fondue's axes panel, or ttx -t fvar.
- "What kerning pairs ship?" - ttx -t GPOS, then search the kern lookup.
- "Who designed and manufactured this?" - name IDs 9 and 8 in the ttx dump; useful in provenance work.

## Common failure modes

- A verdict formed from one tool: Fondue shows features, not drawing quality; Fontspector shows structure, not aesthetics. Cross-check before deciding.
- A bug report sent upstream without the version string: the first reply asks for it, and a round trip is wasted. Read name ID 5 before filing.
- Confidential client work uploaded to a web inspector "for a quick look"; the CLI tools answer the same questions offline.
- Interpolation judged only at the default instance; defects live between instances, which is what Samsa exposes.
- Vendor metadata trusted over the file: the cmap and the name table are facts, the shop page is marketing.
- A file that opens in every GUI tool is assumed fine: corrupt files sometimes open with warnings the inspector forgives; Fontspector catches what the GUI hides.
- The cmap read as "everything the font can render": coverage is not capability; marks, conjuncts, and positioning may still be required for correct text.

## Cross-references

- [Font quality tooling](font-quality-tooling.md)
- [Variable fonts and axes](variable-fonts-and-axes.md)
- [Testing multilingual coverage](../scripts/testing-multilingual-coverage.md)
- [Research workflow](../workflow/research-workflow.md)

Compiled 2025 as part of the Fontlore project.
