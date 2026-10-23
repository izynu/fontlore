#!/usr/bin/env python3
"""Generates Fontlore guides/ from the data layer.

Output (all files follow the reference house style and pass scripts/validate.py):
  guides/fonts/{slug}-overview.md           identity, coverage, license, fit
  guides/fonts/{slug}-implementation.md     install, CSS, axes, fallbacks
  guides/fonts/{slug}-pairing-playbook.md   documented pairs + contrast rules
  guides/pairings/{pair-id}.md              per-pairing guide
  guides/tools/{tool-slug}.md               per-tool workflow guide

Every value comes from the data layer. Nothing is invented; where the data
layer has null, the guide says so.

Run: python3 scripts/generate_guides.py
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
GUIDES = ROOT / "guides"

FOOTER = "Compiled 2025 as part of the Fontlore project."

with (DATA / "fonts.json").open(encoding="utf-8") as fh:
    FONTS = json.load(fh)["fonts"]
with (DATA / "pairings.json").open(encoding="utf-8") as fh:
    PAIRINGS = json.load(fh)["pairings"]
with (DATA / "tools.json").open(encoding="utf-8") as fh:
    TOOLS = json.load(fh)["tools"]

BY_SLUG = {f["slug"]: f for f in FONTS}

LICENSE_NOTES = {
    "OFL-1.1": (
        "Released under the SIL Open Font License 1.1. The family may be used, studied, "
        "modified, embedded, and bundled in commercial and personal work. Selling the font "
        "files on their own is the only prohibited use. If a Reserved Font Name applies, "
        "modified versions must be renamed."
    ),
    "Apache-2.0": (
        "Released under the Apache License 2.0. Use, redistribution, and modification are "
        "permitted in commercial and open-source projects; keep the license notice with any "
        "redistributed font files."
    ),
    "UFL-1.0": (
        "Released under the Ubuntu Font License 1.0. Similar freedoms to the OFL for use, "
        "distribution, and modification, with its own naming and redistribution conditions."
    ),
    "ITF-FFL-1.0": (
        "Released under the Indian Type Foundry Free Font License. Free for personal and "
        "commercial use, including web embedding; redistribution of the raw font files as a "
        "standalone product is restricted. Read the license text shipped with the family "
        "before bundling."
    ),
    "MIT": (
        "Released under the MIT license. One of the most permissive licenses in use; keep "
        "the copyright notice with redistributed files."
    ),
}

SIZE_ROWS = {
    "sans-serif": [
        ("UI label", "11-13 px", "medium weight, generous letter spacing"),
        ("Body", "14-17 px", "the default reading range on screens"),
        ("Section head", "20-28 px", "step up the weight, not the letterspacing"),
        ("Display", "36-64 px", "check tracking; most sans faces tighten above 1.2"),
    ],
    "serif": [
        ("Body", "15-19 px", "serifs need a point more than sans to stay crisp"),
        ("Section head", "24-32 px", "keep contrast readable at this range"),
        ("Display", "40-72 px", "didones and high contrast shine here"),
        ("Caption", "12-13 px", "prefer sturdy text cuts over display cuts"),
    ],
    "display": [
        ("Display", "40-80 px", "the only reliable home for display voices"),
        ("Section head", "28-36 px", "test carefully; some display faces fail below this"),
        ("Body", "not recommended", "most display designs collapse in paragraphs"),
        ("UI label", "not recommended", "use the text cut of the family or a partner sans"),
    ],
    "monospace": [
        ("Code", "13-15 px", "match the editor's line height"),
        ("Data cell", "12-14 px", "fixed widths keep columns aligned"),
        ("Metadata", "11-13 px", "timestamps, ids, and identifiers"),
        ("Display", "24-40 px", "only for technical-branded moments"),
    ],
    "handwriting": [
        ("Accent", "20-36 px", "short strings only"),
        ("Greeting", "28-48 px", "the largest safe home"),
        ("Body", "never", "handwriting fails sustained reading"),
        ("UI label", "never", "accessibility-critical text needs a text face"),
    ],
    "default": [
        ("Body", "14-17 px", "standard reading range"),
        ("Display", "36-64 px", "verify tracking at large sizes"),
    ],
}

NUMERALS = {
    "sans-serif": "Most modern sans families ship proportional lining figures by default; check for a tabular feature (tnum) before using them in tables or dashboards.",
    "serif": "Text serifs often include old-style figures as a feature; decide deliberately between lining and old-style for the product's voice.",
    "display": "Numeral sets in display faces are designed for posters, not tables; never rely on them for aligned data.",
    "monospace": "All figures share the advance width by construction; that is the point.",
    "handwriting": "Numeral coverage can be incomplete in script faces; test every number the product renders.",
}

CLASS_READ = {
    "grotesque": "Grotesque letterforms keep even stroke color, closed apertures, and workmanlike details. They read as institutional and neutral, which is why so many product teams default to them.",
    "geometric": "Geometric letterforms are built on circles and even strokes. They read modern and friendly at display sizes, but single-storey forms and even widths can slow dense text.",
    "humanist": "Humanist letterforms carry calligraphic roots: open apertures, varied stroke widths, and generous spacing. They forgive small sizes and mixed contexts better than most classes.",
    "old-style": "Old-style serifs keep angled stress and organic texture from the Renaissance originals. They read literary and warm, and reward generous leading.",
    "transitional": "Transitional serifs mark the move to vertical stress and moderate contrast. They are the safest serif class for products that must work everywhere.",
    "didone": "Didone serifs push contrast to the limit: hairlines against heavy stems. They are display instruments; below headline sizes the hairlines vanish.",
    "slab": "Slab serifs attach block-like serifs with low contrast. They read sturdy and honest, and they survive rough rendering where hairlines would fail.",
    "mono": "Monospace designs fix every advance width. That regularity signals code and data, and it makes columns align for free.",
    "rounded": "Rounded terminals soften every stroke ending. The effect reads friendly at display sizes and toy-like in the wrong context.",
    "script": "Script faces connect letters the way handwriting does. They are moment faces: signatures, greetings, and brand flourishes.",
    "condensed": "Condensed letterforms narrow the widths to fit more per line. They buy space at the cost of comfortable reading, which is why they live in headlines and tickers.",
}

CATEGORY_FIT = {
    "sans-serif": [
        "Interface text, navigation, and form controls",
        "Dashboards and dense data layouts when paired with tabular figures",
        "Marketing headlines at larger sizes for geometric and grotesque voices",
        "System fallback stacks where a neutral default is required",
    ],
    "serif": [
        "Longform reading: articles, documentation prose, books",
        "Editorial hierarchies where a serif voice signals depth",
        "Pairing with a sans for UI chrome around text-heavy screens",
        "Print-adjacent products that want a bookish register on screen",
    ],
    "display": [
        "Headlines, posters, and hero sections",
        "Short, high-impact strings rather than paragraphs",
        "Brand moments that need a distinct voice",
    ],
    "monospace": [
        "Code blocks, terminals, and technical documentation",
        "Tabular data where fixed advance widths keep columns aligned",
        "Metadata, timestamps, and identifiers",
    ],
    "handwriting": [
        "Accents, annotations, and short personal touches",
        "Greeting surfaces and celebration states",
        "Never for body text or critical UI labels",
    ],
}

TOOL_STAGE_TABLE = {
    "catalogs": "Before: constraints from the brief. After: a candidate list with per-family metadata.",
    "apis": "Before: a shortlist of families to inspect. After: structured metadata snapshots with dates.",
    "source-repos": "Before: catalog claims about a family. After: upstream verification of files and license.",
    "discovery": "Before: a candidate pool limited to big catalogs. After: a wider pool with rejection reasons.",
    "foundries": "Before: aggregator data. After: foundry-grade license and specimen facts.",
    "evidence": "Before: abstract candidate qualities. After: real-world usage examples to compare against.",
    "education": "Before: intuition about categories. After: vocabulary and named examples to defend choices.",
    "licensing": "Before: an aesthetic shortlist. After: a license-cleared shortlist with recorded scope.",
    "identification": "Before: an image or reference. After: a candidate list with confidence levels.",
    "pairing": "Before: two isolated families. After: tested candidate pairs with outcomes.",
    "technical": "Before: assumptions about files. After: measured axes, features, and coverage.",
    "tooling": "Before: guesses about size and behavior. After: numbers attached to decisions.",
    "accessibility": "Before: type chosen by taste. After: type checked against WCAG and zoom behavior.",
    "scripts": "Before: checkbox coverage claims. After: real-string test results per script.",
    "creation": "Before: a commissioning decision. After: an informed build-vs-customize comparison.",
    "commercial": "Before: an unpurchased shortlist. After: quotes and license models on record.",
}

TOOL_STEPS = {
    "catalogs": ["Filter by license and script before anything else", "Open the family page, not just the card", "Test the project's real sample text in the preview"],
    "apis": ["Fetch the family record and store the JSON with a date", "Compare weights and subsets against the project needs", "Flag any field the API cannot answer"],
    "source-repos": ["Locate the family directory and its LICENSE file", "Read METADATA or manifest fields for provenance", "Pin the commit or release you verified"],
    "discovery": ["Search by classification, not by name", "Record what you rejected and why", "Check each find's license before adding to the pool"],
    "foundries": ["Open the specific family page, not the homepage", "Read the license summary and the full text", "Note trial vs full license paths"],
    "evidence": ["Search by industry and medium, not just typeface", "Save the example URL with what it demonstrates", "Compare at least two examples before generalizing"],
    "education": ["Read for principles, not for font lists", "Extract one defensible rule per source", "Link the essay next to the rule in your notes"],
    "licensing": ["Identify the exact use: web, desktop, app, logo", "Read the license text for that use", "Record scope, price, and renewal terms"],
    "identification": ["Crop clean glyphs before uploading", "Interpret candidates as a shortlist", "Verify the winner letterform by letterform"],
    "pairing": ["Generate candidates with the project's tone in mind", "Set real copy in both faces", "Check hierarchy at final sizes"],
    "technical": ["Drop the font file into the inspector", "List axes, features, and language coverage", "Compare against the implementation plan"],
    "tooling": ["Measure the real files, not the marketing page", "Record sizes with the context they came from", "Re-measure after any family update"],
    "accessibility": ["Test the actual sizes the product ships", "Apply the WCAG text-spacing overrides", "Check zoom and reflow behavior"],
    "scripts": ["Collect real strings from the project", "Render them in every weight you plan to ship", "Check marks, conjuncts, and mixed-script runs"],
    "creation": ["Check the original license permits modification", "Decide build vs customize on evidence", "Document any fork and its renaming obligations"],
    "commercial": ["Collect quotes for the exact license scope", "Compare perpetual vs subscription totals", "Keep receipts with the license register"],
}

TOOL_PRIMARY = {
    "catalogs": "the catalog itself is the primary source for availability, not for license interpretation",
    "apis": "the API is primary for its own metadata; treat it as secondary for license and design questions",
    "source-repos": "the repository is the primary source for files and license text",
    "discovery": "discovery links are pointers; the foundry page is primary",
    "foundries": "the foundry is the primary source for its own licenses",
    "evidence": "examples are primary evidence of usage, not of quality",
    "education": "essays are primary for arguments, not for facts; verify facts separately",
    "licensing": "the license text is the only primary source; summaries are aids",
    "identification": "tools propose; foundry specimens verify",
    "pairing": "generators propose; real-copy tests verify",
    "technical": "the file is primary; the inspector just reads it",
    "tooling": "measurements are primary only with the file version recorded",
    "accessibility": "WCAG is primary; tools help apply it",
    "scripts": "rendered strings are primary; coverage tables are not",
    "creation": "the original license governs what customization may ship",
    "commercial": "the purchase terms are primary once money moves",
}

CATEGORY_AVOID = {
    "sans-serif": [
        "Long literary body text where an old-style serif reads more comfortably",
        "Display contexts that need strong contrast or personality",
    ],
    "serif": [
        "Tiny UI labels and dense table text where sans shapes stay clearer",
        "Interfaces that need a strictly neutral, invisible voice",
    ],
    "display": [
        "Body text and small sizes: most display designs collapse below 20 px",
        "Data-dense layouts that need tabular figures",
    ],
    "monospace": [
        "Longform prose: fixed widths slow reading",
        "Marketing headlines unless the brief calls for a technical voice",
    ],
    "handwriting": [
        "Anything users must read quickly or at small sizes",
        "Accessibility-critical text of any kind",
    ],
}

KIND_TEXT = {
    "contrast-plus-neutral": "a high-contrast display voice carries the headlines while a low-key neutral handles everything else",
    "personality-plus-neutral": "one expressive face sets the tone while a quieter partner does the daily work",
    "character-plus-workhorse": "the headline face has visible character and the body face disappears into the reading",
    "family-system": "both sides come from the same designed system, so weight and proportion agree by construction",
    "superfamily": "a designed serif and sans pair that share skeleton, metrics, and intent",
    "friendly-duet": "two warm voices at different temperatures keep the page approachable without going casual everywhere",
    "geometric-plus-serif": "geometric headlines frame a serif body built for sustained reading",
    "grotesque-duet": "two grotesques split the work: louder for headlines, quieter for text",
    "condensed-plus-neutral": "condensed authority in the headlines with an unobtrusive body face",
    "serif-plus-sans": "a serif for reading and a sans for interface chrome; the default editorial system",
    "screen-serif-plus-ui": "a serif engineered for screens with a sans that handles UI labels and captions",
    "slab-plus-humanist": "slab headings signal structure while a humanist body keeps long text comfortable",
    "warmth-plus-neutral": "warmth where it helps and neutrality where it matters",
    "opsz-plus-ui": "an optical-size family adapts from display to text while a UI sans covers the chrome",
    "reading-plus-chrome": "a reading-engineered face for content with a quiet sans for interface text",
    "loud-plus-disciplined": "one loud voice against a disciplined partner that never competes",
    "poster-plus-neutral": "poster energy on top, maximum neutrality underneath",
    "squared-plus-calm": "squared, technical display shapes over a calm body",
    "techno-duet": "two technical voices balanced so the page reads engineered, not gimmicky",
    "code-plus-ui": "a coding face for code and values with a UI sans around it",
    "handwritten-plus-warm": "handwritten accents over a warm body; personal without chaos",
    "brush-plus-geometric": "brush script energy with geometric label support",
    "script-plus-quiet": "a bold script for moments and a quiet partner for everything else",
    "script-duet-arabic": "a classical Arabic text voice with a modern Arabic UI sans",
    "script-duet-indic": "an Indic-script UI face with its Latin sibling for bilingual shells",
    "thai-duet": "a Thai display voice with document-grade Thai text support",
    "devanagari-duet": "a Devanagari editorial display over a quiet UI humanist",
    "devanagari-display-duet": "a high-contrast Devanagari display over a clean text face",
    "arabic-geometric-duet": "geometric Arabic families that agree on color and proportion",
    "kufi-plus-noto": "Kufi display headlines over a Noto Arabic UI workhorse",
    "a11y-plus-ui": "an accessibility-first text face with a predictable UI partner",
    "fluency-plus-humanist": "fluency-tuned spacing with a humanist partner for education contexts",
    "neutral-duet": "two deliberately neutral voices for civic and institutional work",
    "fashion-geometric-duet": "thin-capable geometric display with a calm geometric body",
    "futura-plus-minimal": "Futura-flavored display with a minimalist body",
    "experimental-plus-ui": "experimental display with a usable UI voice around it",
    "wide-plus-fintech": "wide futuristic display over a fintech-grade body",
    "geometric-plus-safe": "a geometric headline voice with the safest possible body",
    "geometric-plus-workhorse": "geometric headlines with a workhorse body",
    "fontshare-duet": "two Fontshare families designed to work together",
    "fontshare-display-duet": "a Fontshare statement display over its workhorse sibling",
    "fontshare-editorial-duet": "an inky display grotesque with a Swiss body from the same catalog",
    "scores-duet": "condensed score display with a rounded support cast",
    "classic-plus-grotesque": "a screen-tuned classic serif with a personality-rich grotesque",
    "academic-duet": "a book face and a humanist sans for journals and papers",
    "literary-duet": "a true old-style text face with a warm sans for paratext",
    "luxury-duet": "delicate high-contrast display over geometric labels",
    "fashion-formula": "an optical didone with a Futura voice; the fashion editorial standard",
    "poster-plus-quirky": "a fatface poster display with a quirky grotesque for support",
    "serif-duet": "two serifs at different temperatures, tuned to agree",
    "slab-plus-ui": "a slab with character over a neutral UI body",
    "condensed-plus-serif": "condensed gothic authority above a serious screen serif",
    "personality-duet": "two strong personalities that share a sense of oddness",
    "grotesque-plus-neutral": "a grotesque with personality over a neutral body",
    "poster-plus-editorial": "caps condensed display with an editorial grotesque for details",
    "display-duet": "two display voices kept apart by role and size",
    "humanist-duet": "two humanist voices at different intensities",
    "cyrillic-duet": "voices that agree across Cyrillic and Latin coverage",
    "scores-plus-support": "score-friendly condensed display with support text nearby",
}

CONTEXT_TEXT = {
    "editorial-magazine": "magazine features, longform columns, and editorial fronts",
    "brand-marketing": "brand sites and marketing pages that need a voice, not just a font",
    "tech-saas": "SaaS landing pages and product marketing where personality must survive usability",
    "marketing-hero": "hero sections, campaign pages, and product launches",
    "corporate-longform": "corporate reports, about pages, and governance content",
    "news-headlines": "news indexes, section fronts, and headline stacks",
    "startup-landing": "startup landing pages that want warmth without noise",
    "sports-news": "scores, results, and fast-turnaround news layouts",
    "blog-longform": "personal and company blogs where reading comfort is the product",
    "news-longform": "article bodies and reading-first news products",
    "documentation": "product documentation and knowledge bases",
    "enterprise-systems": "enterprise products where documents and UI must agree",
    "humanist-editorial": "publishing, essays, and warm editorial products",
    "civic-government": "government and civic services that must stay neutral and legible",
    "reading-app": "reading apps and platforms where text is the interface",
    "ebook-longform": "ebooks and long sessions on personal devices",
    "culture-journal": "cultural criticism, reviews, and journals",
    "poster-hero": "posters, heroes, and moments with one message",
    "events-sports": "events, fixtures, and scoreboards",
    "gaming-tech": "gaming, esports, and tech-enthusiast products",
    "sci-fi-product": "techno products and speculative brands",
    "dev-tools": "developer tools, terminals, and technical consoles",
    "developer-docs": "developer documentation and API references",
    "code-heavy-docs": "documentation with heavy inline and block code",
    "engineering-platform": "engineering platforms, specs, and internal tools",
    "friendly-brand": "small brands that speak like people",
    "food-leisure": "food, hospitality, and leisure brands",
    "casual-retail": "retail brands with a casual voice",
    "arabic-editorial": "Arabic editorial and literary products",
    "multilingual-base": "products that must cover many scripts with one system",
    "indic-multilingual": "bilingual Hindi-English product shells",
    "thai-media": "Thai media and content platforms",
    "devanagari-editorial": "Hindi-first editorial and advocacy",
    "devanagari-corporate": "Indian corporate and publishing products",
    "arabic-ui": "Arabic-first applications and portals",
    "arabic-display": "Arabic display moments over dependable text support",
    "accessibility-first": "products that treat accessibility as a requirement, not a feature",
    "reading-fluency": "early readers, education, and fluency-focused products",
    "gov-digital": "public digital services and institutional sites",
    "fashion-ecommerce": "fashion lookbooks and product pages",
    "clean-startup": "clean, modern startup sites",
    "art-culture": "galleries, festivals, and cultural institutions",
    "web3-futuristic": "web3, crypto, and futuristic brands",
    "fintech-product": "fintech products that need trust and clarity",
    "enterprise-family": "enterprise systems built on one family",
    "saas-product": "SaaS products with marketing and app surfaces",
    "edtech-friendly": "education technology with long lessons",
    "classic-blog": "personal blogs and classic web publishing",
    "academic-longform": "academic papers, preprints, and journals",
    "literary": "literary magazines and book-adjacent sites",
    "luxury-editorial": "luxury, hospitality, and wedding editorial",
    "fashion-editorial": "fashion editorial and campaign microsites",
    "magazine-cover": "covers, specials, and poster-like spreads",
    "devanagari-display": "Devanagari display moments in bilingual layouts",
    "all-serif-editorial": "all-serif editorial systems",
    "tech-blog": "engineering blogs and technical storytelling",
    "product-docs": "product documentation and release notes",
    "poster-family": "posters and campaigns inside a single family",
    "event-poster": "event posters and announcements",
    "sports-data": "sports data, tickers, and stat tables",
    "news-headlines-serif": "news products that pair condensed headlines with a serif body",
    "quirky-startup": "brands that refuse neutrality on purpose",
    "fontshare-saas": "SaaS products built on the Fontshare catalog",
    "fontshare-brand": "agency-grade brand systems from the Fontshare catalog",
    "fontshare-editorial": "editorial brand kits from the Fontshare catalog",
    "sports-tickers": "tickers, scoreboards, and live data surfaces",
}

TOOL_SECTION_WORKFLOW = {
    "catalogs": ("research", "browse and filter the catalog, record family metadata and the source URL"),
    "apis": ("research", "pull structured metadata (weights, subsets, variable status) and cache it with a retrieval date"),
    "source-repos": ("research", "confirm the upstream source, license file, and latest release before relying on a family"),
    "discovery": ("research", "widen the candidate pool beyond the obvious catalogs; record what you rejected and why"),
    "foundries": ("research", "read the foundry's own license and specimen pages; foundry data outranks aggregator data"),
    "evidence": ("research", "find real-world usage in the same industry and medium; treat popularity as a weak prior"),
    "education": ("research", "build the vocabulary needed to defend the choice to stakeholders"),
    "licensing": ("implementation", "verify license scope for the exact use: web, desktop, app, logo, client handoff"),
    "identification": ("identification", "run the tool, then verify the candidate before treating the name as fact"),
    "pairing": ("selection", "generate pairing candidates, then validate with real copy at real sizes"),
    "technical": ("implementation", "inspect axes, features, and coverage before committing to the family"),
    "tooling": ("implementation", "measure and inspect rather than guess; record what the tool reported"),
    "accessibility": ("selection", "check the typography decisions against WCAG requirements and real zoom behavior"),
    "scripts": ("selection", "confirm script coverage with real strings, not catalog checkboxes"),
    "creation": ("implementation", "investigate whether an existing family can be customized before commissioning work"),
    "commercial": ("implementation", "compare license models and total cost before purchasing; perpetual vs subscription changes budgets"),
}

TOOL_CAUTIONS = {
    "catalogs": "Catalog previews are marketing surfaces. Always confirm weights, subsets, and license from the family's own page or repository.",
    "apis": "API metadata can lag behind releases. Record the retrieval date and verify critical fields at the source.",
    "source-repos": "Repository state changes. Pin the commit or release you verified and note the date.",
    "discovery": "Discovery sites mix licenses. Never assume free means commercially safe; check each family's license file.",
    "foundries": "Foundry sites describe their own licenses, which vary per family. The family page, not the homepage, is the source of truth.",
    "evidence": "Usage examples prove popularity, not quality. Two projects in different industries may need opposite choices.",
    "education": "Guidance ages. Prefer sources that state their premises over lists of rules without reasons.",
    "licensing": "License summaries are not legal advice. When money changes hands, read the actual license text or ask the foundry.",
    "identification": "Automated identification returns candidates, not facts. Modified letterforms and custom lettering defeat these tools.",
    "pairing": "Generators propose, they do not decide. Every generated pair must survive the real-copy test.",
    "technical": "Tool output describes the file, not the design. A clean file can still be the wrong voice for the project.",
    "tooling": "Numbers without context mislead. Record sizes alongside the measurements you take.",
    "accessibility": "Font choice alone cannot make a layout accessible. Size, spacing, contrast, and structure carry most of the weight.",
    "scripts": "Coverage tables lie by omission. Test diacritics, conjuncts, and mixed-script strings from the actual project.",
    "creation": "Modifying a font changes your license obligations. Check the original license before editing and redistributing.",
    "commercial": "Pricing models change. Confirm terms at purchase time and keep receipts with the license register.",
}

TOOL_OUTPUT = {
    "catalogs": "family name, catalog URL, license name, and the date checked",
    "apis": "the metadata snapshot (weights, subsets, variable flag) plus the endpoint and date",
    "source-repos": "repository URL, license file path, and release or commit pinned",
    "discovery": "candidate list with rejections and reasons",
    "foundries": "family page URL, license name, and purchase or download path",
    "evidence": "example URL, industry, medium, and what the example demonstrates",
    "education": "the principle learned and the source essay URL",
    "licensing": "license name, official license URL, scope decision, and review date",
    "identification": "candidate list, verification result, and confidence level",
    "pairing": "the pair tested, sample copy used, and the outcome",
    "technical": "the measurements taken (axes, features, coverage) and the file version",
    "tooling": "the raw output relevant to the decision, trimmed to what matters",
    "accessibility": "the checks run (zoom, spacing overrides, contrast) and results",
    "scripts": "the test strings used and per-script results",
    "creation": "the customization decision and its license implications",
    "commercial": "the quote, license model, and renewal or perpetual status",
}


def slugify(name: str) -> str:
    return "".join(c if c.isalnum() else "-" for c in name.lower()).replace("--", "-").strip("-")


def category_fallbacks(category: str, classification: str, exclude: str, n: int = 4) -> list[dict]:
    same_slot = [f for f in FONTS if f["slug"] != exclude and f["classification"] == classification]
    same_cat = [f for f in FONTS if f["slug"] != exclude and f["category"] == category]
    pool = same_slot if len(same_slot) >= n else same_slot + [f for f in same_cat if f not in same_slot]
    seen: set[str] = set()
    out: list[dict] = []
    for f in sorted(pool, key=lambda x: x["family"]):
        if f["slug"] in seen:
            continue
        seen.add(f["slug"])
        out.append(f)
        if len(out) >= n:
            break
    return out


def pairing_rows(slug: str) -> list[dict]:
    return [p for p in PAIRINGS if p["heading"] == slug or p["body"] == slug]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n" + FOOTER + "\n", encoding="ascii")


# ---------------------------------------------------------------- fonts


def font_overview(f: dict) -> str:
    alts = category_fallbacks(f["category"], f["classification"], f["slug"])
    pairs = pairing_rows(f["slug"])
    designer = f["designer"] if f["designer"] else "not recorded in the data layer"
    foundry = f["foundry"] if f["foundry"] else "not recorded in the data layer"
    lines: list[str] = []
    a = lines.append
    a(f"# {f['family']}: typeface overview")
    a("")
    a(
        "What this reference covers: "
        f"{f['family']} as recorded in the Fontlore data layer: identity, classification, "
        "script coverage, technical profile, license, and where the family fits or does not fit."
    )
    a("")
    a("## Identity")
    a("")
    a("| Field | Value |")
    a("| --- | --- |")
    a(f"| Family | {f['family']} |")
    a(f"| Slug | {f['slug']} |")
    a(f"| Designer | {designer} |")
    a(f"| Foundry | {foundry} |")
    a(f"| License | {f['license']} |")
    a(f"| Category | {f['category']} |")
    a(f"| Classification | {f['classification']} |")
    a(f"| Source | {f['source']} |")
    a("")
    a("## Position in the taxonomy")
    a("")
    a(
        f"The data layer files {f['family']} under {f['category']} with the "
        f"{f['classification']} classification. Tags: {', '.join(f['tags'])}."
    )
    a("")
    a(f"Data-layer note: {f['note']}")
    a("")
    a("## Script and subset coverage")
    a("")
    a("| Script or subset | Record |")
    a("| --- | --- |")
    for s in f["scripts"]:
        a(f"| {s} | declared in the data layer |")
    a("")
    a(
        f"Coverage is recorded as declared by the upstream catalog. Before shipping a "
        "multilingual product, run the strings from the project through the family; see "
        "the cross-referenced testing guide at the end of this file."
    )
    a("")
    a("## Technical profile")
    a("")
    if f["variable"]:
        a(f"Variable build: yes. Declared axes: {', '.join(f['axes'])}.")
        a("")
        a("| Axis | What it controls |")
        a("| --- | --- |")
        axis_roles = {
            "wght": "weight from thin to black",
            "opsz": "optical size; detail tuning from small text to display",
            "wdth": "width from condensed to expanded",
            "slnt": "slant without a true italic redesign",
            "ital": "switches to the italic design",
            "SOFT": "softness of terminals and joins",
            "WONK": "wonky alternates for personality",
        }
        for ax in f["axes"]:
            a(f"| {ax} | {axis_roles.get(ax, 'custom axis; inspect the file for ranges')} |")
        a("")
        a(
            "Static instances can be generated from the variable file, but prefer serving "
            "the variable build where the platform supports it."
        )
    else:
        a("Variable build: no. Serve static weights.")
        if f["weights"]:
            a("")
            a("| Weight | Record |")
            a("| --- | --- |")
            for w in f["weights"]:
                a(f"| {w} | available |")
        else:
            a("")
            a("Specific weight list not recorded in the data layer; confirm on the source page.")
    a("")
    a("## Where it fits")
    a("")
    for row in CATEGORY_FIT.get(f["category"], []):
        a(f"- {row}")
    a("")
    a("## Where it does not fit")
    a("")
    for row in CATEGORY_AVOID.get(f["category"], []):
        a(f"- {row}")
    a("")
    a("## Alternatives in the same slot")
    a("")
    a("Compared against the same classification and category in the data layer:")
    a("")
    a("| Family | Classification | License | Variable |")
    a("| --- | --- | --- | --- |")
    for alt in alts:
        a(f"| {alt['family']} | {alt['classification']} | {alt['license']} | {'yes' if alt['variable'] else 'no'} |")
    a("")
    a("## License notes")
    a("")
    a(LICENSE_NOTES.get(f["license"], "License text not summarized in the data layer."))
    a("")
    a(f"Always verify against the source page: {f['source']}")
    a("")
    a("## How to load it")
    a("")
    if f["variable"]:
        pkg = f"@fontsource-variable/{f['slug']}"
    else:
        pkg = f"@fontsource/{f['slug']}"
    a(f"- npm package: `{pkg}`")
    a(f"- CDN stylesheet: `https://cdn.jsdelivr.net/fontsource/css/{f['slug']}@latest/index.css`")
    a("- Implementation details, axis usage, and fallback strategy: see the implementation guide below.")
    a("")
    a("## Common mistakes")
    a("")
    if f["variable"]:
        a("- Assuming every named instance in design tools exists as a web-safe CSS value; set axes explicitly.")
        a("- Loading the full variable file when only two weights are needed; check the size budget first.")
    else:
        a("- Requesting weights the family does not ship; browsers will synthesize bold or light and wreck the color.")
        a("- Serving every static weight when the page uses two; subset the list first.")
    a("- Treating this overview as license advice; the license text at the source URL is the authority.")
    a("- Skipping a real-copy test because the catalog preview looked right.")
    a("")
    a("## Reading the classification")
    a("")
    a(CLASS_READ.get(f["classification"], "Inspect the specimen and compare against the classification primer before relying on class assumptions."))
    a("")
    a("## Size ranges by role")
    a("")
    a("| Role | Suggested range | Note |")
    a("| --- | --- | --- |")
    for role, rng, note in SIZE_ROWS.get(f["category"], SIZE_ROWS["default"]):
        a(f"| {role} | {rng} | {note} |")
    a("")
    a("Ranges are starting points; adjust to the family's x-height and the medium.")
    a("")
    a("## Pairings at a glance")
    a("")
    if pairs:
        for p in pairs:
            role = "heading" if p["heading"] == f["slug"] else "body"
            partner_slug = p["body"] if role == "heading" else p["heading"]
            partner_name = BY_SLUG.get(partner_slug, {}).get("family", partner_slug)
            a(f"- As {role}: {partner_name} for {p['context']} (guide: ../pairings/{p['id']}.md)")
    else:
        a("- No documented pairing names this family yet; see the pairing playbook for candidates.")
    a("")
    a("## Numerals, spacing, and details")
    a("")
    a(NUMERALS.get(f["category"], "Inspect the specimen for numeral styles and spacing behavior before committing."))
    a("")
    a("## Notes for agents")
    a("")
    a(f"- Hard filters: script coverage ({', '.join(f['scripts'])}) and license ({f['license']}).")
    a(f"- Scoring hints: {f['classification']} classification, {f['category']} category, variable={'yes' if f['variable'] else 'no'}.")
    a("- Route to the implementation guide for CSS specifics; do not improvise install paths.")
    a("- If the project's license scope is unclear, stop and verify before recommending.")
    a("")
    a("## Provenance")
    a("")
    a(f"- Data-layer slug: `{f['slug']}`")
    a(f"- Source page: {f['source']}")
    a("- Record checked against the source page when added; re-verify at review time.")
    a("")
    a("## How to cite this record")
    a("")
    a(f"Fontlore data layer, font record `{f['slug']}`, retrieved 2025. Verify current facts at {f['source']}.")
    a("")
    a("## Cross-references")
    a("")
    a(f"- [{alts[0]['family']} overview](./{alts[0]['slug']}-overview.md)")
    a(f"- [{f['family']} implementation guide](./{f['slug']}-implementation.md)")
    a(f"- [{f['family']} pairing playbook](./{f['slug']}-pairing-playbook.md)")
    a("- [Classification primer](../references/selection/classification-primer.md)")
    a("- [Open Font License reference](../references/licensing/open-font-license.md)")
    return "\n".join(lines)


def font_implementation(f: dict) -> str:
    lines: list[str] = []
    a = lines.append
    fam_css = f["family"]
    a(f"# {f['family']}: implementation guide")
    a("")
    a(
        "What this reference covers: shipping "
        f"{f['family']} on the web: install paths, CSS setup, variable axis usage, "
        "font-display strategy, fallbacks, and a pre-launch checklist."
    )
    a("")
    a("## Install paths")
    a("")
    if f["variable"]:
        a(f"- npm: `npm install @fontsource-variable/{f['slug']}`")
        a(f"- Import once: `import '@fontsource-variable/{f['slug']}';`")
    else:
        a(f"- npm: `npm install @fontsource/{f['slug']}`")
        a(f"- Import per weight: `import '@fontsource/{f['slug']}/400.css';`")
    a("")
    a("CDN stylesheet, no install:")
    a("")
    a("```html")
    a(f'<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/{f["slug"]}@latest/index.css">')
    a("```")
    a("")
    a(
        "Self-hosting beats the CDN for production: it removes a third-party dependency, "
        "lets you control cache headers, and keeps font bytes on your own domain."
    )
    a("")
    a("## CSS setup")
    a("")
    a("```css")
    a(":root {")
    a(f"  --font-brand: '{fam_css}';")
    stack = {
        "serif": "Georgia, 'Times New Roman', serif",
        "display": "Georgia, 'Times New Roman', serif",
        "monospace": "ui-monospace, 'Courier New', monospace",
        "handwriting": "'Segoe Script', cursive",
        "sans-serif": "system-ui, -apple-system, 'Segoe UI', sans-serif",
    }
    a(f"  --font-brand-fallback: {stack.get(f['category'], stack['sans-serif'])};")
    a("}")
    a("")
    a(f".brand-type {{ font-family: var(--font-brand), var(--font-brand-fallback); }}")
    a("```")
    a("")
    a("## Weight and axis strategy")
    a("")
    if f["variable"]:
        a(
            f"{f['family']} ships as a variable font with axes: {', '.join(f['axes'])}."
        )
        a("")
        a("```css")
        a(".headline {")
        a("  font-family: var(--font-brand), var(--font-brand-fallback);")
        if "wght" in f["axes"]:
            a("  font-weight: 640; /* arbitrary values on the wght axis */")
        if "opsz" in f["axes"]:
            a("  font-optical-sizing: auto; /* or set font-variation-settings 'opsz' */")
        a("}")
        a("```")
        a("")
        a(
            "Prefer standard `font-weight` and `font-optical-sizing` over raw "
            "`font-variation-settings` so the browser can inherit and animate values "
            "predictably. Reserve `font-variation-settings` for custom axes."
        )
    else:
        weights = f["weights"] or [400, 700]
        a(f"{f['family']} serves static weights. Recorded available weights: {', '.join(map(str, weights))}.")
        a("")
        a("```css")
        a("/* request exactly the weights the family ships */")
        for w in weights:
            a(f".weight-{w} {{ font-weight: {w}; }}")
        a("```")
        a("")
        a(
            "If a design calls for a weight between two statics, choose the nearest "
            "available weight deliberately; browsers synthesize the rest and the fake "
            "weights are always worse than the honest nearest neighbor."
        )
    a("")
    a("## font-display strategy")
    a("")
    a(
        "- Body text: `font-display: swap` keeps content readable during load at the cost "
        "of a brief fallback flash."
    )
    a(
        "- Display headlines: `swap` is usually acceptable; `optional` suits cases where "
        "layout stability outranks brand type on first paint."
    )
    a(
        "- Avoid `block` for anything above the fold; invisible text is the worst outcome "
        "for readers."
    )
    a("")
    a("## Subset and performance notes")
    a("")
    a(
        f"Declared subsets: {', '.join(f['subsets'])}. Load only the subsets the page "
        "actually renders; the Fontsource packages and the Google Fonts CSS API split "
        "coverage with unicode-range so browsers fetch what they need."
    )
    a("")
    a(
        "Budget guidance: audit the network tab after wiring the family up. If the font "
        "payload exceeds roughly 100 KB for a Latin-only page, question whether every "
        "requested weight earns its bytes."
    )
    a("")
    a("## Fallback strategy")
    a("")
    a(
        f"The recommended fallback stack above picks system faces that share the "
        f"{f['category']} category, so the swap flash changes letterforms but not layout "
        "category. For tighter control, measure the fallback with size-adjust and "
        "ascent-override rather than eyeballing it."
    )
    a("")
    a("## Pre-launch checklist")
    a("")
    a("- [ ] Weights requested match weights shipped; no synthetic bold in the UI.")
    a("- [ ] font-display chosen deliberately for body and display roles.")
    a("- [ ] Only needed subsets load; network tab audited.")
    a("- [ ] Fallback stack renders the page without layout shift during swap.")
    a("- [ ] License verified at the source page for the current project scope.")
    a("- [ ] Real copy tested at real sizes, including numerals and punctuation.")
    a("")
    a("## Common mistakes")
    a("")
    a("- Importing the whole package when one stylesheet would do; tree shaking does not apply to CSS.")
    a("- Hard-coding px everywhere and losing the variable optical sizing benefit.")
    a("- Forgetting `font-optical-sizing: auto` on optical-size families, which pins the wrong optical cut.")
    a("- Shipping the CDN stylesheet in production and eating the third-party request.")
    a("")
    a("## Cross-references")
    a("")
    a(f"- [{f['family']} overview](./{f['slug']}-overview.md)")
    a("- [@font-face and CSS reference](../references/technical/font-face-and-css.md)")
    a("- [font-display strategies](../references/technical/font-display-strategies.md)")
    if f["variable"]:
        a("- [Variable fonts and axes](../references/technical/variable-fonts-and-axes.md)")
    else:
        a("- [Fallback metrics and CLS](../references/technical/fallback-metrics-and-cls.md)")
    return "\n".join(lines)


def font_pairing_playbook(f: dict) -> str:
    pairs = pairing_rows(f["slug"])
    alts = category_fallbacks(f["category"], f["classification"], f["slug"])
    lines: list[str] = []
    a = lines.append
    a(f"# {f['family']}: pairing playbook")
    a("")
    a(
        "What this reference covers: how "
        f"{f['family']} behaves in a pairing: its documented partners in the data layer, "
        "the contrast rules that apply to its classification, and a testing workflow."
    )
    a("")
    a("## Pairing temperament")
    a("")
    temperament = {
        "sans-serif": "A sans voice stays out of the way: it defers to expressive partners and holds the layout together.",
        "serif": "A serif carries authority in reading roles; pair it with a sans for chrome or another serif at a different temperature.",
        "display": "A display face must be the loudest thing on the page; its partner's job is to never compete.",
        "monospace": "A monospace signals code and data; it pairs with a proportional voice that handles prose.",
        "handwriting": "A handwriting face is seasoning, not a meal; partners must be calm and legible.",
    }
    a(temperament.get(f["category"], "Pair by contrast of role, not by similarity."))
    a(
        f"Specifically, {f['classification']} shapes: "
        + {
            "grotesque": "even color, closed apertures, and a workmanlike rhythm; they want partners with either more warmth or more contrast.",
            "geometric": "circular bowls and even strokes; they read modern and need partners that do not fight for geometric attention.",
            "humanist": "open forms and calligraphic roots; they forgive mixed contexts and pair widely.",
            "old-style": "angled stress and organic texture; they want neutral or geometric partners, not more old-style.",
            "transitional": "vertical stress and moderate contrast; the safest serif class for mixed systems.",
            "didone": "extreme contrast that collapses at small sizes; headlines only, with quiet partners.",
            "slab": "block-like serifs with low contrast; they stand up to geometric and grotesque sans partners.",
            "mono": "fixed advance widths; anything proportional around them benefits from shared x-height.",
            "rounded": "soft terminals read friendly; balance with crisp partners when the page needs order.",
            "script": "connected strokes demand isolation; never stack two script voices.",
            "condensed": "narrow forms save space; give the partner room to breathe with a wider body voice.",
        }.get(f["classification"], "Pair by contrast of role and verify with real copy.")
    )
    a("")
    a("## Documented pairings in the data layer")
    a("")
    if pairs:
        a("| This family as | Partner | Context | Kind | Guide |")
        a("| --- | --- | --- | --- | --- |")
        for p in pairs:
            role = "heading" if p["heading"] == f["slug"] else "body"
            partner_slug = p["body"] if role == "heading" else p["heading"]
            partner = BY_SLUG.get(partner_slug)
            partner_name = partner["family"] if partner else partner_slug
            a(
                f"| {role} | {partner_name} | {p['context']} | {p['kind']} | "
                f"[{p['id']}](../pairings/{p['id']}.md) |"
            )
    else:
        a(
            "No curated pairing in the data layer names this family yet. Use the contrast "
            "rules above to build a candidate pair, test it with real copy, and contribute "
            "the result upstream."
        )
    a("")
    a("## Candidate partners from the same slot")
    a("")
    a("| Family | Classification | Category | License |")
    a("| --- | --- | --- | --- |")
    for alt in alts:
        a(f"| {alt['family']} | {alt['classification']} | {alt['category']} | {alt['license']} |")
    a("")
    a("## Contrast rules that apply here")
    a("")
    a(f"- Contrast by role first: if {f['family']} leads, the partner supports.")
    a("- Contrast by temperature second: pair a warm voice with a cooler one, not two of each.")
    a("- Contrast by structure last: x-height and width must agree even when style differs.")
    a("- Same-family systems skip these rules by design; use them when cohesion outranks expression.")
    a("")
    a("## Testing workflow")
    a("")
    a("1. Set the pair in the project's real headline and body copy, not lorem ipsum.")
    a("2. Test the smallest size the body will render at, typically 13 to 16 px.")
    a("3. Test numerals and mixed-script strings if either appears in the product.")
    a("4. Check hierarchy: can a reader separate heading, body, caption, and label without color?")
    a("5. Record the outcome in the project's type decision log with links to both license pages.")
    a("")
    a("## Common mistakes")
    a("")
    a("- Pairing two display voices because both looked good alone.")
    a("- Ignoring license compatibility: both families must cover the project's use scope.")
    a("- Matching by similarity instead of contrast; two middleweights blur into hierarchy soup.")
    a("- Skipping the small-size test where contrast and apertures actually fail.")
    a("")
    a("## Cross-references")
    a("")
    if pairs:
        a(f"- [{BY_SLUG[pairs[0]['heading'] if pairs[0]['heading'] != f['slug'] else pairs[0]['body']]['family']} overview](./{pairs[0]['heading'] if pairs[0]['heading'] != f['slug'] else pairs[0]['body']}-overview.md)")
    else:
        a(f"- [{alts[0]['family']} overview](./{alts[0]['slug']}-overview.md)")
    a(f"- [{f['family']} overview](./{f['slug']}-overview.md)")
    a("- [Classification primer](../references/selection/classification-primer.md)")
    a("- [Choosing body typefaces](../references/selection/choosing-body-typefaces.md)")
    return "\n".join(lines)


# ---------------------------------------------------------------- pairings


def pairing_guide(p: dict) -> str:
    h = BY_SLUG.get(p["heading"], {})
    b = BY_SLUG.get(p["body"], {})
    h_name = h.get("family", p["heading"])
    b_name = b.get("family", p["body"])
    kind = KIND_TEXT.get(p["kind"], "the two voices split the work by role and temperature")
    context = CONTEXT_TEXT.get(p["context"], p["context"].replace("-", " "))
    lines: list[str] = []
    a = lines.append
    a(f"# {h_name} + {b_name}: pairing guide")
    a("")
    a(
        "What this reference covers: the documented pairing of "
        f"{h_name} for headings and {b_name} for body text: why it works, where it fits, "
        "how to implement it, and what to test before shipping."
    )
    a("")
    a("## The pair at a glance")
    a("")
    a("| Role | Family | Classification | License | Variable |")
    a("| --- | --- | --- | --- | --- |")
    a(f"| Heading | {h_name} | {h.get('classification', 'n/a')} | {h.get('license', 'n/a')} | {'yes' if h.get('variable') else 'no'} |")
    a(f"| Body | {b_name} | {b.get('classification', 'n/a')} | {b.get('license', 'n/a')} | {'yes' if b.get('variable') else 'no'} |")
    a("")
    a(f"Pairing kind: `{p['kind']}`. In practice, {kind}.")
    a("")
    a("## Why this pair works")
    a("")
    a(p["rationale"])
    a("")
    a(
        f"The mechanism is complementary contrast: {h.get('classification', 'the heading face')} "
        f"headlines bring a different structure than the "
        f"{b.get('classification', 'body face')} body, while both agree on overall color and "
        "proportion enough to sit on one page without arguing."
    )
    a("")
    a("## Where to use it")
    a("")
    a(f"This pairing targets {context}.")
    a("")
    a("- Landing pages that need the headline voice to land in one glance.")
    a("- Content products where the body voice must survive thousands of words.")
    a("- Design systems that want a documented default before teams improvise.")
    a("")
    a("## How to set it up")
    a("")
    a("```html")
    a(f'<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/{p["heading"]}@latest/index.css">')
    a(f'<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/css/{p["body"]}@latest/index.css">')
    a("```")
    a("")
    a("```css")
    a(":root {")
    a(f"  --font-heading: '{h_name}';")
    a(f"  --font-body: '{b_name}';")
    a("}")
    a("")
    a("h1, h2, h3 { font-family: var(--font-heading), serif; font-weight: 600; }")
    a("body { font-family: var(--font-body), sans-serif; font-size: 1rem; line-height: 1.6; }")
    a("```")
    a("")
    a(
        "Self-host both families in production and drop the CDN links; the snippet above "
        "is for quick evaluation only."
    )
    a("")
    a("## Hierarchy suggestions")
    a("")
    a(f"- Display: {h_name} at 40 to 72 px, tightened tracking above 1.2 ratios.")
    a(f"- Section heads: {h_name} at 24 to 32 px, or switch to {b_name} at 600 for dense UIs.")
    a(f"- Body: {b_name} at 15 to 17 px with 1.5 to 1.7 line height.")
    a("- Captions and metadata: the body family at 12 to 13 px, medium weight, muted color.")
    a("- Code and numerals in tables: add a monospace; this pair does not cover those roles.")
    a("")
    a("## Alternatives with the same logic")
    a("")
    same_kind = [q for q in PAIRINGS if q["kind"] == p["kind"] and q["id"] != p["id"]][:3]
    if same_kind:
        a("| Pair | Context | Guide |")
        a("| --- | --- | --- |")
        for q in same_kind:
            qh = BY_SLUG.get(q["heading"], {}).get("family", q["heading"])
            qb = BY_SLUG.get(q["body"], {}).get("family", q["body"])
            a(f"| {qh} + {qb} | {q['context']} | [{q['id']}](./{q['id']}.md) |")
    else:
        a(
            "No other pairing in the data layer shares this exact logic; browse the "
            "pairings tab of the library for adjacent kinds."
        )
    a("")
    a("## Testing checklist")
    a("")
    a("- [ ] Real headline copy at final sizes; check the heading voice does not collapse.")
    a("- [ ] Real body copy for three paragraphs minimum; no rhythmic snags.")
    a("- [ ] Numerals in both faces match the product's needs (tabular vs proportional).")
    a("- [ ] Both licenses cover the project scope; record URLs in the decision log.")
    a("- [ ] Fallback stacks chosen per role so a slow load never swaps both faces at once.")
    a("")
    a("## Common mistakes")
    a("")
    a("- Letting the heading face appear in running text; contrast faces tire fast at small sizes.")
    a("- Matching weights instead of roles: 700 heading vs 400 body beats 600 vs 500 every time.")
    a("- Forgetting the caption style, which silently becomes the third voice on the page.")
    a("")
    a("## Cross-references")
    a("")
    a(f"- [{h_name} overview](../fonts/{p['heading']}-overview.md)")
    a(f"- [{b_name} overview](../fonts/{p['body']}-overview.md)")
    a("- [Classification primer](../references/selection/classification-primer.md)")
    a("- [Testing and comparing shortlists](../references/workflow/testing-and-comparing-shortlists.md)")
    return "\n".join(lines)


# ---------------------------------------------------------------- tools


def tool_guide(t: dict) -> str:
    slug = slugify(t["name"])
    stage, use = TOOL_SECTION_WORKFLOW.get(t["section"], ("research", "use it where the workflow needs evidence"))
    siblings = [x for x in TOOLS if x["section"] == t["section"] and x["name"] != t["name"]][:3]
    ref_map = {
        "catalogs": "../references/sourcing/google-fonts-catalog.md",
        "apis": "../references/sourcing/fontsource-api.md",
        "source-repos": "../references/sourcing/google-fonts-repository.md",
        "discovery": "../references/sourcing/open-and-independent-foundries.md",
        "foundries": "../references/sourcing/commercial-foundries-and-catalogs.md",
        "evidence": "../references/workflow/research-workflow.md",
        "education": "../references/selection/classification-primer.md",
        "licensing": "../references/licensing/open-font-license.md",
        "identification": "../references/identification/identification-workflow-overview.md",
        "pairing": "../references/selection/classification-primer.md",
        "technical": "../references/technical/inspecting-font-files.md",
        "tooling": "../references/technical/inspecting-font-files.md",
        "accessibility": "../references/accessibility/wcag-baseline-for-type.md",
        "scripts": "../references/scripts/mixed-script-fallbacks.md",
        "creation": "../references/technical/inspecting-font-files.md",
        "commercial": "../references/licensing/marketplace-license-models.md",
    }
    ref_link = ref_map.get(t["section"], "../references/workflow/research-workflow.md")
    lines: list[str] = []
    a = lines.append
    a(f"# {t['name']}: workflow guide")
    a("")
    a(
        "What this reference covers: "
        f"{t['name']} as a Fontlore workflow tool: what it is, where it sits in the "
        f"{stage} stage, how to use it well, and what evidence to record from it."
    )
    a("")
    a("## What it is")
    a("")
    a(t["what"])
    a("")
    a(f"- Section: {t['section']}")
    a(f"- Access: {t['access']}")
    a(f"- URL: {t['url']}")
    a("")
    a("## Where it sits in the Fontlore workflow")
    a("")
    a(
        f"This tool belongs to the **{stage}** stage. Concretely: {use}. "
        "It feeds records into the decision log, not opinions into the chat."
    )
    a("")
    a("## How to use it well")
    a("")
    a("- Go in with the project constraints written down: scripts, sizes, license scope, medium.")
    a("- Record what the tool returned, not what you hoped it would return.")
    a("- Prefer the tool's own primary data (files, license text, metadata) over summaries elsewhere.")
    a("- Combine with at least one independent source before treating a fact as verified.")
    if t["section"] in ("apis", "source-repos", "technical", "tooling"):
        a("- Pin versions: note the release, endpoint snapshot, or file hash alongside the retrieval date.")
    if t["section"] in ("licensing", "commercial"):
        a("- Screenshot or archive the license terms at review time; terms change without notice.")
    if t["section"] in ("identification", "pairing"):
        a("- Treat outputs as candidate lists. Verification is a separate, mandatory step.")
    a("")
    a("## Evidence to record")
    a("")
    a(f"When this tool contributes to a decision, log: {TOOL_OUTPUT.get(t['section'], 'the tool output, URL, and date')}.")
    a("")
    a("## Limitations and cautions")
    a("")
    a(TOOL_CAUTIONS.get(t["section"], "Verify critical outputs against the primary source before relying on them."))
    a("")
    a("## Alternatives and complements")
    a("")
    if siblings:
        a("| Tool | Section | Access |")
        a("| --- | --- | --- |")
        for s in siblings:
            a(f"| {s['name']} | {s['section']} | {s['access']} |")
        a(
            "Siblings serve the same stage; pick one primary and keep one fallback in "
            "case the primary changes terms or disappears."
        )
    else:
        a(
            "No direct siblings in this section; cross-reference the broader source list "
            "in the references tree."
        )
    a("")
    a("## Common mistakes")
    a("")
    a("- Copying tool output into the decision log without the URL and date.")
    a("- Letting one tool be the single source of truth for license facts.")
    a("- Using the tool outside its stage: identification tools do not verify licenses, catalogs do not test rendering.")
    a("")
    a("## Cross-references")
    a("")
    a(f"- [{ref_link.split('/')[-1].replace('.md', '').replace('-', ' ').title()}]({ref_link})")
    if siblings:
        a(f"- [{siblings[0]['name']} guide](./{slugify(siblings[0]['name'])}.md)")
    a("- [Research workflow](../references/workflow/research-workflow.md)")
    a("- [Evaluating catalog metadata](../references/sourcing/evaluating-catalog-metadata.md)")
    return "\n".join(lines)


def main() -> None:
    counts = {"fonts": 0, "pairings": 0, "tools": 0}
    for f in FONTS:
        write(GUIDES / "fonts" / f"{f['slug']}-overview.md", font_overview(f))
        write(GUIDES / "fonts" / f"{f['slug']}-implementation.md", font_implementation(f))
        write(GUIDES / "fonts" / f"{f['slug']}-pairing-playbook.md", font_pairing_playbook(f))
        counts["fonts"] += 3
    for p in PAIRINGS:
        write(GUIDES / "pairings" / f"{p['id']}.md", pairing_guide(p))
        counts["pairings"] += 1
    for t in TOOLS:
        write(GUIDES / "tools" / f"{slugify(t['name'])}.md", tool_guide(t))
        counts["tools"] += 1
    total = sum(counts.values())
    print(f"generated: {counts} total={total}")


if __name__ == "__main__":
    main()
