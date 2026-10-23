# Branding and Logotypes

What this reference covers: Separating the wordmark from the UI type system, the licensing questions logo use raises, and how to build a brand type system from one or two families. Brand typography is a governance problem as much as an aesthetic one: the system must survive handoffs, vendors, and five years of staff turnover.

## Wordmark versus UI type

Two different objects with different rules:

- The wordmark or logotype: a fixed rendering of the brand name, set once, drawn or carefully kerned, used as an image or SVG, never retyped. It can be a licensed display face at one weight, a heavily modified cut, or custom lettering. It has no italic, no body text, no reflow.
- The UI or system type: the families and scales used everywhere the brand speaks: product, site, documents, decks. This needs weights, features, scripts, licensing breadth, and documentation.

The classic failure is using the wordmark face as the UI face: display faces (high contrast, tight spacing, one weight) fail at 14 px and in paragraphs. The second classic failure is the reverse: a workhorse UI face as a wordmark, which reads generic.

Wordmark craft notes: tracking is usually tightened slightly (not crushed), letter-spacing is set optically per pair, and the wordmark is exported with outlines (SVG paths), so nobody needs the font file to reproduce it; that also sidesteps embedding rights questions for the mark itself.

## Licensing questions logo use raises

- Open Font License fonts: use in a logo is permitted, including commercial use, but the license's reserved font names clause means you cannot promote the font's name as part of your trademark; renaming inside the OFL terms has its own requirements (see the OFL reserved names reference). Keep the license file with the brand assets.
- Commercial desktop licenses: check that logo use is covered; some licenses carve out logo or trademark use, and a wordmark rendered from a licensed font may require a specific tier. Read the license, or ask the foundry in writing.
- The safe pattern: wordmark as outlined artwork (SVG/EPS) means the font itself stops traveling; vendors, printers, and agencies reproduce the mark without needing a license.
- Trademark: the brand name's protection is a legal matter; the font's license governs the typeface software. Conflating the two causes real disputes.

## Building the system from one or two families

One family, done well: choose a family with enough weight range and (ideally) variable axes to carry display and UI roles; define display, text, and label styles as instances. Examples that support this pattern: Inter (neutral product brands), Source Sans 3, IBM Plex Sans (with its serif and mono siblings as a system), Public Sans, Manrope.

Two families, the classic split: a display or serif voice for brand moments plus a workhorse sans for UI. Examples: Fraunces plus Public Sans; Playfair Display plus Source Sans 3; Fraunces plus Karla; Literata plus Inter. The pairing rules are the same as editorial: shared skeleton, distinct voices.

- Freeze the axes: if the display family is variable (Fraunces SOFT, WONK), the brand defines exact axis values for the wordmark-adjacent styles; "any value" is not a brand system.
- Define the don'ts: which weights are banned, which tracking is banned, minimum sizes, where the wordmark face may never appear.
- Provide the files with licenses: a brand type kit contains font files, license texts, usage one-pager, and the tokens or style definitions for web and print.
- Internationalize: if the brand operates in scripts beyond Latin, decide the per-script partners now (Noto siblings are the default answer), not during a market launch.

## Governance that outlives the rebrand

- The approved list lives with the design tokens; a request process (see the governance reference) handles exceptions.
- Version pinning applies to brands too: record exact font versions in the brand guidelines; a silent variable-font upgrade changes the wordmark's neighborhood.
- Deprecation: when a family is replaced, publish migration notes and a grace period; brands accumulate "temporary" fonts that never leave.

## Common mistakes

- Retyping the wordmark in the font instead of using outlined artwork, then discovering a vendor does not have the license.
- A brand kit with fonts but no licenses; the first audit or due diligence finds it.
- Three families "for flexibility"; brands with a display, a text, a UI, a mono, and a slab have a wardrobe, not a system.
- No minimum sizes for the display face, so it appears at 16 px in emails and fails there.
- Choosing a display face for the wordmark without checking it has the letters the brand needs (accents, ampersand character, local-language forms) at logo quality.
- Letting each team pick its own weights because the kit only documented the family name.

## Decision rules

- Default shape: one display family for brand moments plus one workhorse family; add a mono only if the brand genuinely publishes code or data.
- Wordmark: outlined artwork from a licensed or custom-drawn design; the font file never leaves the brand kit.
- Any face entering the brand kit: license review (logo use, embedding, app, webfont), script coverage, and version record, in that order, before aesthetics.
- Rebrand or refresh: audit actual font usage across properties first; the gap between documented and used fonts is the real brief.
- If the brand must speak in a new script: adopt the Noto partner for that script and document it as canonical, rather than licensing five regional exclusives.

## Comparison table: brand faces versus UI workhorses

Most durable brand systems pair one display voice with one UI workhorse. Open-license candidates for each role, with the trade-offs that matter once the wordmark is drawn:

| Display candidates | Voice | Weight range | Italics | Natural fit |
| --- | --- | --- | --- | --- |
| Space Grotesk | techy grotesque with mono-derived details | 300-700 | no | developer tools, startups, protocol brands |
| Sora | geometric, open, airy | 100-800 | no | fintech, climate, infrastructure |
| Manrope | semi-geometric, economical | 200-800 | no | product brands wanting one face for display and UI |
| Archivo | workhorse grotesque with a width axis | 100-900 | yes | editorial, sports, cultural institutions |
| Playfair Display | sharp high-contrast display serif | 400-900 | yes | luxury, publishing, fashion-adjacent brands |
| Fraunces | soft old-style display serif, wonk optional | 100-900 with opsz, SOFT, WONK | yes | food, craft, publishing, warm consumer brands |

| UI workhorses to pair | Why they pair well |
| --- | --- |
| Inter | neutral, tall x-height, sits quietly under geometric displays |
| Source Sans 3 | humanist warmth and a 200-900 range; defers to a loud display face |
| IBM Plex Sans | engineered voice with quirks; the Plex Mono sibling covers code |
| Public Sans | plain civic clarity; it disappears while the brand face speaks |
| System stack | native feel; the enterprise default when personality lives in layout |

- Every family listed is OFL: the brand kit ships files and license texts with no seat counting and no procurement review.
- Variable ranges collapse into fewer static styles; check a family's static weight list before promising eight weights to stakeholders.
- The grotesque display faces here are not UI workhorses at 13 px; pair them with a workhorse rather than stretching them downward.
- Personality check at wordmark scale: set the real company name at 200 px and at 48 px before committing; quirks that charm in a specimen can fight a legal-sounding name.
- If the brand voice needs italics, Space Grotesk, Sora, and Manrope are disqualified; Archivo, Playfair Display, and Fraunces carry true italics.
- OFL modified builds must respect declared Reserved Font Names; a brand that forks a family records the rename obligation in the kit.
- Pairing audition: display at 40 px above UI at 14 px with real copy; if the seam shows, change the UI face, not the display voice.

## Worked example: a fintech rebrand on open licenses

Scenario: a payments startup rebrands. Procurement refuses per-seat font budgets, the product UI is already Inter and nobody will fund changing it, markets are English and German, and the wordmark must hold from a 16 px favicon to a two-meter conference banner.

- Wordmark: the company name set in Sora at weight 700, tracking tightened slightly, letter pairs kerned by hand, then converted to outlines as SVG. Three locks (full name, monogram, stacked) live in the kit; nobody retypes them.
  - The outline export also settles vendor rights: the mark travels as paths, so printers and agencies never need the font.
- Axis freeze: the brand sheet names exact instances, wordmark 700, section headers 600, hero moments 800, everything else banned. "Use the variable axis freely" is not a system.
  - The sheet also records the static TTF instances used for decks and documents, because embedding paths prefer statics.
- Display voice: Sora at 40 to 72 px with leading of 1.05 to 1.15. German compounds were tested at weight 800 because the family runs wide when heavy; one hero layout was rebuilt around the longest German word.
  - Hero moments cap at 72 px; above that, Sora's counters tighten visually and the wordmark's neighborhood changes.
- UI voice: Inter stays exactly as shipped. The two faces share tall x-heights and similar stroke rhythm, so a Sora headline above an Inter form reads as one system; no third family was introduced.
  - Inter keeps its own token scale; the brand sheet never redefines UI sizes, only display ones.
- Rejected: Space Grotesk for the wordmark, because its mono-derived details read as "developer tool" to bank-adjacent customers in stakeholder reviews.
- Rejected: Archivo Expanded for display, because the width axis invited every designer to stretch something different within a month.
- Rejected: Fraunces, because the serif warmth contradicted the product's data-forward positioning despite winning the aesthetics round.
  - It stayed on the shortlist as the voice for a warmer sub-brand (savings products) if one ever ships.
- Kit contents: Sora and Inter files with their OFL license texts, the axis-freeze sheet, SVG wordmark locks, favicon-scale test renders, and a one-pager rule that Inter never appears above 32 px, where Sora takes over.
  - The one-pager also names IBM Plex Mono for code and data moments, adopted the day the engineering blog started publishing code.
- Handoff: the kit README names the exact family versions behind approved artwork, so the client's first audit two years later finds zero drift.
- Aftermath: the quarterly seat-count review disappeared, vendors reproduce the mark from SVG without touching a font file, and the product team shipped the rebrand without changing a component.

## Field notes

- A wordmark is drawn once; a brand face is specified. Conflating the two is how live font files end up retyped into slide masters and forwarded to vendors who hold no license.
- Strong systems look over-specified on paper (frozen axes, banned weights, minimum sizes) and completely consistent in the wild; the paperwork is what survives staff turnover.
- Rebrands fail quietly in email signatures, deck masters, and shared-drive templates. Budget a day to hunt template fonts across the company; that is where dead faces hide.
- When the brand face is variable, record named instances ("Heading: weight 600"), never adjectives like "light to bold as needed". Instances are checkable; adjectives are not.
- Logos get outlined; UI does not. The kit explains which is which, because the first engineer asked to "add the brand font" will otherwise embed the display face into the product.
- Wordmark spacing is optical, not metric: tracking set per letter pair, then frozen in the SVG; nobody re-kerns the mark per context.
- Social platforms will not load your brand face for native text; design templates so the voice survives where the font cannot follow.
- Favicon and app-icon moments strip typography to one or two letterforms; test the wordmark's initials as shapes, because the full name never renders there.
- A mono companion earns its place the first time the brand publishes code, prices, or data; add it then, not preemptively.
- Trademark screening happens on the drawn mark, not on the font: two companies can both set their wordmarks in Sora, and neither owns the family.
- When the display face lacks a script (Greek, Cyrillic), the policy decision (substitute face or avoided contexts) is written down before the first localized campaign, not after.
- Keep the wordmark source file with the font version noted; a re-render two years later without the pinned version drifts by a few points of tracking.
- Brand guidelines carry one personality note per family ("Sora: airy, runs wide at heavy weights"), because the next designer inherits judgment, not taste.
- Print vendors ask for fonts or outlines; the kit's answer is always outlines for fixed artwork, and that answer belongs in the vendor onboarding document.
- Legacy surfaces (old decks, printed stationery) keep the previous face until they cycle out; the migration note lists them so they are tracked, not discovered.
- The most common kit gap is scripts: the Latin system is beautiful, then a market launch asks for a banner in a new script and nobody knows the policy.

## Quick reference: the brand type kit

- Font files for every family and weight in the system, license texts beside each one.
- SVG or outlined EPS wordmark locks; the live font file never leaves the kit.
- Axis-freeze or named-instance sheet for any variable face, with banned weights explicit.
- Minimum sizes per face: display faces typically floor around 20 to 24 px, so state it.
- Role bans for UI faces, so the workhorse never impersonates the display voice above its ceiling.
- Approved pairings table: which face for headlines, body, labels, data, and code.
- Script partners for every market language, decided once and written down.
- Version records: exact family versions behind approved artwork, so reprints and re-renders match.
- Size and contrast floors for legal and regulatory text on physical goods.
- A request path for exceptions, so one deck in an unapproved face does not become precedent.
- A short don'ts list: banned combinations, banned tracking, banned contexts.
- Pairing audition renders (display over UI at real sizes) included in the kit.
- A change log page for the kit itself: what changed, when, and why.
- A file naming convention (family-weight-style), so files do not multiply under aliases.
- One named owner for the kit, because unowned kits rot within a year.

## Cross-references

- [Packaging and retail](packaging-and-retail.md)
- [Presenting to stakeholders](../workflow/presenting-to-stakeholders.md)
- [Brief to constraints](../workflow/brief-to-constraints.md)
- [Font governance and review](../workflow/font-governance-and-review.md)

Compiled 2025 as part of the Fontlore project.
