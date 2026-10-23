# Web and SaaS Interfaces

What this reference covers: Typography for product UI: the working size range, dense menus and form controls, cross-platform rendering realities, and the small decisions (inheritance, tracking, weights) that separate a crisp interface from a mushy one. This is the default context for most teams and the one with the least room for display-font indulgence.

## The working sizes

- Body and primary UI text: 14 to 16 px. Below 14 px, test on Windows specifically; some UIs legitimately run 13 px dense tables.
- Secondary text (labels, captions, metadata): 12 to 13 px. This is the floor; 11 px only for tracked uppercase micro-labels with verified contrast, never for sentences.
- Buttons and inputs: 14 to 16 px, and critically at least 16 px on iOS, where smaller input font sizes trigger automatic zoom on focus.
- Nav and menus: 14 to 15 px with generous hit areas; menus are scanning surfaces, so weight (500) and spacing do more work than size.

Rule of thumb: as sizes drop, weights rise. A 12 px label wants 500 or 600; a 16 px paragraph wants 400.

## Choosing the family

UI faces are judged at 13 px, not at 64 px. What matters:

- Solid small-size rendering: open apertures, generous x-height, sturdy strokes; Inter, Source Sans 3, IBM Plex Sans, Public Sans, and system stacks all pass this test; high-contrast display faces fail it.
- Real weights: 400, 500, 600, 700 minimum for a UI system; medium and semibold carry buttons and labels so bold can stay reserved for headings.
- Tabular figures: a hard requirement for any product that shows data; check before shortlisting.
- Coverage: the full language matrix, including the Latin-ext tier and whatever scripts the roadmap mentions, not just what ships today.
- Variable or static: either works; variable gives the weight granularity UI systems actually use (a 550 button weight is a real thing in practice).

The system-ui stack is a legitimate choice: zero bytes, native feel per platform, and the typographic personality of the OS. Choose it deliberately (enterprise tools, keyboard-heavy apps) or against it (brand differentiation), not by accident.

## Cross-platform rendering

- Windows with ClearType renders hinted fonts crisply and unhinted fonts mushy at small sizes; check the candidate face at 13 px on Windows before committing. This is the single most common "looks great on my Mac" failure.
- macOS applies heavy smoothing; thin weights look thinner on Windows than in a Mac design review.
- Linux/Android render through FreeType with variable results; the big open families are tested there by enormous user bases, another argument for them.
- If the product ships a desktop app (Electron or similar), the same checks apply, plus OS font smoothing settings users control; test with defaults.

## The small decisions that add up

- Inheritance: form controls do not inherit font-family by default; the reset that fixes this is the oldest CSS trick in the book and is still missed. Audit inputs, buttons, and selects after any font change.
- Tracking: negative tracking on UI labels hurts at small sizes; reserve tight tracking for display. Uppercase micro-labels get positive tracking (0.05 to 0.08em), never body text.
- Line-height in controls: set explicitly; font defaults differ per family and inflate buttons inconsistently across scripts.
- Numbers: tabular figures everywhere data aligns; monospace for IDs and codes.
- Focus and selection: the new font changes text width; verify focus rings, ellipsis, and truncation points still behave.

## Common mistakes

- Shipping the brand display face for UI text because it was already licensed; display faces are built for 24 px and up.
- 11 px gray body text failing contrast while everyone admires how clean the spacing looks.
- Negative letter-spacing on 13 px labels, visually jamming letters that were already tight.
- Forgetting the form-control reset, so half the UI renders in Times on some platforms.
- Choosing a face with 400 and 700 only, then synthesizing "medium" with faux bold or color hacks.
- Testing on one platform; the Windows 13 px check is the one that predicts real users' experience.

## Decision rules

- Default recommendation: Inter, Source Sans 3, IBM Plex Sans, Public Sans, or the system stack; all are proven at UI sizes with full weight ranges.
- Dense data product: narrow the candidates to faces with excellent tabular figures and a true 500 and 600.
- Keyboard-heavy enterprise tool: the system stack is often the right answer; spend the differentiation budget on layout.
- Any face decision: render the actual product strings at 13, 14, and 16 px on Windows before sign-off; a specimen page is not evidence.
- Every additional weight must justify itself in the design system; weights are tokens, and unused tokens are waste.

## Comparison table: the four workhorses

| Family | Weights | Tabular figures | Character | Watch-outs |
| --- | --- | --- | --- | --- |
| Inter | 100-900 variable (opsz since v4) | yes | neutral, tall x-height, the default of its decade | so common that personality must come from layout |
| Source Sans 3 | 200-900 | yes | humanist, slightly condensed, warmer | less neutral than Inter at display sizes |
| IBM Plex Sans | 100-700 | yes | engineered voice with quirks; wide script family | no 800 or 900 weights; plan heroes accordingly |
| Public Sans | 100-900 | yes | civic plainness, Franklin-derived | personality budget low by design |
| System stack | per platform | varies | SF Pro, Segoe UI, Roboto; native feel | metrics and feature support differ per platform |

- All four open families pass the small-size test: open apertures, tall x-height, sturdy strokes at 13 to 14 px on Windows.
- tnum is dashboard insurance: Inter, Source Sans 3, IBM Plex Sans, and Public Sans all ship tabular figures; system-stack support varies per platform.
- IBM Plex Sans's 700 ceiling matters if your system uses 800 or 900 for heroes; add a display face for heroes or pick a family with the full range.
- Source Sans 3 is the pick when a product feels clinical in Inter; it warms without losing transparency.
- Public Sans suits government, civic, and compliance-heavy products, where plainness is a feature.
- Variable files cover the weight axis cleanly; static instances exist for every family when embedding rules demand statics.
- The system stack is a deliberate choice for keyboard-heavy enterprise tools; write the decision down so it never looks like an accident.

## Worked example: a field-service SaaS

Scenario: a scheduling and dispatch product for field teams: dense tables, keyboard-heavy workflows, Windows-first enterprise IT policies, nine locales, and a marketing site that wants its own voice.

- Product type: Source Sans 3 variable, weights 400 to 700 in the interface; body 14 px, tables 13 px, labels and metadata 12 px at 500, page titles 22 px at 600.
- Numerals: font-variant-numeric: tabular-nums on every table and status board; job codes and IDs in IBM Plex Mono at 12.5 px with copy buttons.
- Forms: inputs at 16 px to stop iOS zoom-on-focus; labels above fields at 13 px 500; the form-control font-family reset audited after the swap.
- Tracking: nothing negative below 20 px; uppercase micro-labels at 0.05em positive tracking, three words maximum.
- Line-height: 1.5 for body and tables, 1.2 for controls and chips, declared as tokens rather than inherited from font defaults.
- Marketing site: Fraunces for hero headlines at 40 to 72 px with Source Sans 3 body; the product never imports Fraunces, keeping the app payload lean.
- Windows proof: the full interface at 13 px on Windows with ClearType defaults; Source Sans 3 held, where a fashion-grotesque candidate had fallen apart in trials.
- Buttons: 14 to 15 px at 600 with explicit line-height tokens; the 550-weight trick from the variable axis stayed in the tokens for one component only.
- Fallbacks: the stack ends in system-ui, so a blocked font degrades to something native instead of Times.
- Rejected: Inter (nothing wrong with it; the team wanted visual distance from three competitor products that use it) and a condensed face for tables (saved columns, lost 13 px legibility).
- Aftermath: one variable file per script subset, tokens documented, and no line-height surprises in German or Vietnamese for the localization team.

## Field notes

- The 13 px Windows check predicts the real user experience better than any specimen page.
- Form controls do not inherit font-family by default; the oldest reset in CSS is still the most forgotten.
- Faux bold appears when a weight is missing; pick families with real 500 and 600 cuts.
- Font swaps shift every width; re-verify ellipsis, truncation, focus rings, and column widths after any change.
- Variable axes allow a 550 button weight; if the system wants it, it becomes a token, not a per-component secret.
- Line-height defaults differ per family; declared tokens keep buttons and rows consistent across scripts.
- Uppercase labels need positive tracking and shorter strings; negative tracking is for display, never UI text.
- Tabular figures belong in the table component, so every page inherits the fix once.
- Dark themes re-rank faces; what is crisp on white can smear at 12 px on near-black, so re-check both.
- Localization adds height and width: Vietnamese diacritics stress line-height, German compounds stress column widths; test both.
- The marketing face never leaks into the app; two payload budgets, two systems, one boundary.
- Browser zoom to 200 percent is an accessibility baseline; the type system must survive zoom, not just device pixel ratios.
- Subsetting per script keeps payload sane; a full unicode-range file serves glyphs the page never uses.
- font-display behavior matters on flaky networks; metrics-matched fallbacks reduce layout shift while the real font loads.
- Icon fonts compete with text fonts for payload and accessibility; inline SVG icons decouple the two.
- Text rendered in canvas (charts, exporters) needs explicit font declarations; inheritance stops at the canvas edge.
- Every additional weight is a token to maintain; unused tokens get deleted, not archived.
- The interface is read at arm's length all day; comfort at 14 px outranks personality at 64 px.

## Quick reference: UI type floors

- Body and primary UI: 14 to 16 px; dense tables 13 px, tested on Windows.
- Secondary text: 12 to 13 px; 11 px only for tracked-caps micro-labels.
- Inputs: 16 px on iOS to prevent zoom-on-focus.
- Weights: 400 body, 500 labels, 600 emphasis and buttons, 700 page titles.
- tabular-nums wherever numbers align; mono for identifiers.
- Positive tracking for caps labels (0.05 to 0.08em); negative tracking only above 20 px.
- Explicit line-height tokens for body, tables, and controls.
- Form-control font reset audited after every family change.
- Contrast 4.5 to 1 for all text, in both themes.
- Shortlist: Inter, Source Sans 3, IBM Plex Sans, Public Sans, or the system stack.
- Real product strings at 13, 14, and 16 px on Windows before sign-off.
- One family for the product; the marketing face stays on the marketing site.
- Subsets per script; unicode-range tuned; payload reviewed at each release.
- Canvas and SVG text declare the UI family explicitly.
- Zoom to 200 percent as part of the standard test pass.
- Unused weight tokens deleted at each design-system review.
- Table text 12 to 13 px with tabular-nums; row height from spacing tokens.
- Nav and menu text 14 to 15 px at weight 500; spacing and hit areas do the rest.
- Buttons keep one size per level; primary and secondary differ by weight and fill, not by font.
- Micro-labels: 11 px only as tracked uppercase, never for sentences.
- Feature settings (tnum, case) live in components; pages inherit.
- Test with OS font smoothing defaults, not with a designer's tweaked settings.
- Keep the fallback stack metrics-close where possible; layout shift is a font decision.
- Per-locale review (German length, Vietnamese height, Polish diacritics) before each release.
- Icons via SVG; icon fonts double payload and break with text scaling.
- The product's type sizes mirror the design tokens; no per-page values.
- 13 px is a density choice, not a default; most UIs belong at 14 to 16 px.

## Cross-references

- [Dashboards and data-dense UI](dashboards-and-data-dense-ui.md)
- [Font-face and CSS](../technical/font-face-and-css.md)
- [Low vision and zoom](../accessibility/low-vision-and-zoom.md)
- [Numerals and notation](../scripts/numerals-and-notation.md)

Compiled 2025 as part of the Fontlore project.
