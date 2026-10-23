# Choosing Monospace

What this reference covers: How to choose a monospace face for code, data tables, terminals, and technical branding. It covers the criteria that matter (digit and letter disambiguation, ligature options, vertical rhythm), named examples across free and commercial sources, and the zero-style and ligature decisions teams argue about.

Monospace is the rare category where technical constraints and aesthetics genuinely intertwine. The right choice depends on what the text is: code, numbers, receipts, or identity.

## Where monospace belongs

- Code editors and terminal UIs: alignment is structural, so equal widths are functional, not stylistic.
- Data tables and financial figures: tabular alignment prevents digit jitter; a mono companion for numerals is often cleaner than forcing a proportional face into tabular mode.
- Receipts, logs, invoices, and status output: mono signals "machine truth" and reads as credible for raw data.
- Technical branding: a mono accent (labels, eyebrows, metadata) communicates engineering care without committing the whole system.
- Where monospace does not belong: body paragraphs, marketing copy, and anything long-form. Uniform width fights reading rhythm; use it as an accent, not a foundation.

## The criteria that matter

- Disambiguation is the core test: I (capital i), l (lowercase L), and 1 (one) must be instantly distinct, as must O (letter) and 0 (zero). Faces fail their users here first.
- Punctuation needs presence: braces, brackets, and semicolons carry syntax; cramped punctuation makes code harder to scan than font choice ever helps.
- Vertical rhythm: editors stack lines tightly, so the face needs consistent line metrics and no clipped diacritics or box-drawing glyphs.
- Box-drawing and powerline glyph coverage matters for terminal customization; check coverage before standardizing on a face for CLI tooling.
- Weight range: a bold that is clearly bolder at code-comment sizes, and ideally a light for commentary; most monos ship 400 and 700 only.
- Italic exists in modern monos (JetBrains Mono, IBM Plex Mono) and matters for editor syntax themes.
- Variable builds are rare in mono because spacing constraints limit axes; do not expect a wdth axis.

## Named examples

- JetBrains Mono: tall x-height, ligature support, generous character set, free and open source; a strong default for editors.
- Fira Code: the face that popularized programming ligatures; extended by the community from Fira Mono (Erik Spiekermann's Fira family for Mozilla).
- Cascadia Code: Microsoft's editor face for Windows Terminal and Visual Studio, with ligature variants and an italic.
- IBM Plex Mono: part of the IBM Plex system; ideal when the brand already speaks Plex, and distinctive in marketing contexts.
- Source Code Pro: Adobe's mono companion to Source Sans; quiet, professional, widely packaged.
- Space Mono: Colophon Foundry's quirky mono for Google Fonts; a branding favorite when personality is wanted.
- Consolas (Lucas de Groot) and Menlo (Bitstream Vera lineage): the platform defaults many users already know; familiarity is a feature.
- Ubuntu Mono: compact and distinctive; tuned for Ubuntu's ecosystem.
- Berkeley Mono: a commercial success story showing mono-as-brand demand; proprietary and paid.
- Courier: historically foundational and still ubiquitous in printing conventions; too thin and light for modern screens as a body face.

## Ligatures

- Programming ligatures merge glyph sequences like !=, =>, and >= into single joined glyphs. Fira Code made them mainstream; JetBrains Mono and Cascadia Code offer them with toggles.
- They are a preference, not a feature upgrade: teams split roughly in half, so make the choice configurable in editor settings rather than mandated.
- Ligatures can obscure what is literally in the file, which matters in code review, interviews, and teaching contexts; many educators disable them.
- For data display (not code), avoid ligatures entirely; sequences like => or != in logs should render as the characters they are.
- Stylistic sets usually provide a no-ligature variant; document the chosen set in editor config or font-feature-settings so the team sees the same screen.

## Zeros and lookalikes

- Zero styles: slashed (a diagonal stroke through the 0), dotted (a dot inside), or plain. Slashed is the most common in modern monos; dotted appears in some platform faces.
- Choose one convention and hold it across the product; a slashed zero in the terminal and a dotted zero in the UI is the kind of inconsistency users notice without being able to name.
- Many faces expose the alternate zero via a stylistic set or character variant; verify in the feature list rather than assuming.
- The same discipline applies to I/l/1 designs: some faces serif the capital I, some slab the 1, some add tails; pick the treatment that survives your smallest size.

## Terminal aesthetics and branding

- A mono accent layer (labels, code snippets, IDs, timestamps) is a cheap way to add technical credibility to marketing pages and documentation.
- Pair the mono with the system's sans carefully: IBM Plex Mono with IBM Plex Sans shares DNA; Space Mono with almost anything creates deliberate friction that can either sharpen or clash.
- In dashboards, mono numerals plus tabular proportional text is often better than all-mono; test both with real data density.
- Terminal-themed branding (fake shells, ASCII decoration) dates quickly; the mono choice should outlive the gimmick it came with.

## Decision rules

- Default editor face for a team: JetBrains Mono or Fira Code, with ligature policy written down.
- Data-heavy product: proportional UI face plus a mono companion for IDs and figures; decide which fields get mono, not everything.
- Brand with engineering identity: a distinctive mono (Space Mono, Berkeley Mono, IBM Plex Mono) as the accent voice.
- If the face fails the I/l/1 or O/0 test at your smallest size, it fails, regardless of reputation.

## Workflow

1. List every mono context in the product: editor, terminal, tables, receipts, marketing accents.
2. Shortlist three faces covering the strictest context; check character coverage (box drawing, powerline, math) against that context.
3. Run the disambiguation gauntlet: I l 1 O 0 rn m at target sizes, in the real rendering stack.
4. Decide ligature and zero policies; encode them in configs and design tokens.
5. Verify licensing and packaging (Fontsource or vendored files) and record versions in the manifest.

## Common mistakes

- Shipping ligature-enabled faces into data displays and logs where sequences must read literally.
- Choosing a mono for its specimen beauty and discovering missing box-drawing or math glyphs in production terminals.
- Inconsistent zero styles across products and platforms.
- Using Courier out of habit and suffering thin strokes on modern displays.
- Mono for body text because "it looks technical", exhausting readers within a paragraph.
- Forgetting italic availability, then faking italics in editor themes.

## Comparison table

Orientation across widely used monos. "Ligatures" means programming ligatures designed into the face; editor settings toggle the rendering behavior either way.

| Face | Origin | Italic | Programming ligatures | Standing |
| --- | --- | --- | --- | --- |
| JetBrains Mono | JetBrains | Yes | Yes | Tall x-height, 8 weights, built for code reading |
| Fira Code | Community extension of Fira Mono (the Fira family for Mozilla) | No | Yes, the trend-setter | Ligature-first design |
| Cascadia Code | Microsoft | Yes, in recent versions | Yes, with variants | Ships with Windows Terminal |
| IBM Plex Mono | IBM with Bold Monday | Yes | No | The Plex system voice; distinctive in marketing |
| Source Code Pro | Adobe (Paul D. Hunt) | Yes | No | Quiet professional default; widely packaged |
| Space Mono | Colophon Foundry for Google Fonts | Yes | No | Branding personality with deliberate friction |
| Roboto Mono | Google | Yes | No | Neutral companion to Roboto; widely packaged |
| Ubuntu Mono | Tuned for the Ubuntu ecosystem | Yes | No | Compact width, distinctive shapes |
| Consolas | Lucas de Groot | Yes | No | Windows platform default users already know |
| Menlo | Bitstream Vera lineage | Yes | No | macOS platform default |
| Courier | Typewriter ancestor, open revivals | Yes | No | Historically foundational; too light for modern screens |
| Berkeley Mono | Berkeley Graphics, commercial | Check the license terms | Check the spec | The mono-as-brand success case |

Check glyph coverage (box drawing, powerline, math) against your strictest terminal context before standardizing; a beautiful face missing box-drawing glyphs breaks CLI layouts in ways no specimen reveals.

## Worked example

Choosing a mono for a data-heavy B2B product with audit logs, invoices, and a terminal-styled status page. Constraints: dark mode, 12px minimum table figures, and no ligatures anywhere data is displayed.

1. Contexts listed: code blocks in docs, a log viewer, invoice figures, and the status page accent layer. The strictest context is the log viewer at 12px on low-DPI displays.
2. Shortlist: JetBrains Mono, Source Code Pro, IBM Plex Mono; all three pass the I/l/1 and O/0 gauntlet at 12px in the real rendering stack.
3. Ligature policy: logs must read literally, so ligature features are disabled in the log viewer config and left available in editor config; the policy lives in shared font-feature-settings tokens, not personal preferences.
4. Coverage check: box-drawing and powerline glyphs are verified for the status page; JetBrains Mono covers both, which closes the accent-layer decision.
5. Invoice figures: worst-case amounts are set in both the mono and the incumbent sans with tabular figures; the mono aligns without jitter and wins amounts, IDs, and timestamps.
6. Zero policy: slashed zero chosen once, recorded in the design tokens, and verified in every context where the mono appears.
7. Italic check: editor themes want a true italic for comments and strings; all three finalists ship one, and the check is recorded so nobody fakes it later.
8. Packaging: the mono is vendored with a pinned version and an exact license file; the version goes in the manifest so editor updates cannot drift silently.
9. Editor rollout: the default profile sets the face at 13px, line-height 1.5, ligatures per the policy; the config file is shared, so the whole team sees the same screen.
10. Marketing accent: the same mono at 14 to 16px for labels and IDs on the status page, paired with the system sans; the mono is never used for body copy.
11. Outcome: one mono across editor, logs, invoices, and accents, with ligature, zero-style, and size policies written down and enforced by config rather than taste.

The reusable pattern: list contexts, shortlist against the strictest one, decide ligature and zero policies once, verify coverage, pin the version.

## Field notes

- The zero-style argument is a governance problem wearing an aesthetics costume; decide once, encode it, stop relitigating it.
- Editors re-render ligatures per theme and plugin, so the only reliable policy is one written into shared config, not into a wiki page.
- Mono at 12px is where hinting quality shows; test on the worst screen before standardizing.
- Teams underestimate italic demand: review comments, syntax themes, and teaching material all want a true italic eventually.
- A mono accent layer (labels, IDs, timestamps) is the cheapest technical credibility a marketing page can buy.
- If a face's specimen shows only code, assume its prose punctuation was an afterthought; check quotation marks before using it in accents.
- Numeric-heavy screens benefit more from a tabular-figure sans than from an all-mono layout; test both with real data density.
- Platform defaults (Consolas, Menlo) are familiarity features; switching away costs user goodwill for marginal beauty.
- Character width, not point size, determines how much code fits; compare faces by characters per line at your editor size.
- Bold in mono is for errors and highlights; if bold does not read distinctly at 12px, the face is out.
- Ligature discussions reach religious intensity; the escape is policy, not persuasion.
- Terminal themes recolor everything; test the face against your actual theme backgrounds, including high-contrast modes.
- Licensing for mono includes app embedding; verify the license covers bundling if the mono ships inside a desktop app or CLI.

## Quick reference

- Disambiguation first: I, l, and 1 must separate cleanly, as must O and 0, at your smallest size.
- Ligatures: available in editors by choice, disabled in logs and data displays by rule.
- Zero style: pick slashed or dotted once; encode it in tokens; verify the alternate via stylistic sets.
- Coverage: box drawing, powerline, and math glyphs verified before CLI standardization.
- Sizes: 12 to 14px for code and tables; 14 to 16px for mono accents in marketing.
- Line-height: 1.45 to 1.6 for code blocks; tight enough to stack, loose enough to avoid clipped diacritics.
- Italic: require a true italic if editor themes or documentation will ever need it.
- Bold: must read distinctly at your smallest size for errors and highlights.
- Weight range: 400 and 700 minimum; more only if rendering proves they earn it.
- Pairing: mono with its own system sans (Plex with Plex) shares DNA; a quirky mono anywhere is a deliberate friction choice.
- Packaging: pin the version, keep the license file, record both in the manifest.
- Never body text: uniform width fights reading rhythm; mono is an accent, not a foundation.

## Cross-references

- [Classification primer](classification-primer.md)
- [Width, density, and spacing](width-density-and-spacing.md)
- [Superfamily and family systems](superfamily-and-family-systems.md)
- [Choosing body typefaces](choosing-body-typefaces.md)

Compiled 2025 as part of the Fontlore project.
