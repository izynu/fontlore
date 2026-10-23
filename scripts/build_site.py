#!/usr/bin/env python3
"""Build the Fontlore static website into site/ (GitHub Pages ready).

Stdlib only, no dependencies. Run after any data change:
    python3 scripts/build_site.py

Outputs:
  site/index.html                 landing page
  site/browse.html                tabbed library (References / Fonts / Pairings / Tools)
  site/references/<cat>/*.html    all curated references (95)
  site/guides/<kind>/*.html       all generated guides (632)
  site/privacy.html, terms.html, 404.html
  site/assets/                    style.css, app.js, favicon.svg, inline data
  site/robots.txt, sitemap.xml
"""

from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"

REPO_URL = "https://github.com/izynu/fontlore"
LIVE_URL = "https://izynu.github.io/fontlore/"

CATEGORY_BLURBS = {
    "sourcing": "Where to find fonts and how to read catalogs",
    "selection": "Choosing between candidates with a rubric",
    "identification": "Naming a font from an image or specimen",
    "licensing": "Reading and auditing font licenses",
    "scripts": "Per-script typography: Latin, CJK, Arabic, Devanagari, and more",
    "technical": "Formats, loading, performance, variable fonts",
    "accessibility": "Legibility, contrast, WCAG, dynamic type",
    "applications": "Typography per medium: web, print, email, UI, and more",
    "workflow": "End-to-end process: brief to handoff",
}

GUIDE_KIND_BLURBS = {
    "fonts": "Per-font guides: classification, scripts, weights, sources, cautions",
    "pairings": "Per-pairing guides: why the combination works and where to use it",
    "tools": "Per-tool guides: what it is, where it sits in the workflow, evidence to record",
}


# ---------------------------------------------------------------------------
# Minimal markdown renderer (Fontlore house subset: headings, paragraphs,
# bullet and numbered lists, tables, fenced code, bold, italic, code, links).
# ---------------------------------------------------------------------------

def esc(text: str) -> str:
    return html.escape(text, quote=True)


def _link_sub(m: re.Match) -> str:
    return '<a href="' + m.group(2) + '">' + m.group(1) + "</a>"


INLINE_RULES = [
    (re.compile(r"`([^`]+)`"), lambda m: "<code>" + m.group(1) + "</code>"),
    (re.compile(r"\*\*([^*]+)\*\*"), lambda m: "<strong>" + m.group(1) + "</strong>"),
    (re.compile(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])"), lambda m: "<em>" + m.group(1) + "</em>"),
    (re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)"), _link_sub),
]

H1_RE = re.compile(r"^#\s+(.*)$")
HEADING_RE = re.compile(r"^(#{1,4})\s+(.*)$")
UL_RE = re.compile(r"^[-*]\s+(.*)$")
OL_RE = re.compile(r"^(\d+)[.)]\s+(.*)$")
TABLE_SEP_RE = re.compile(r"^\|[\s:|-]+\|$")


def inline(text: str) -> str:
    out = esc(text)
    for rx, fn in INLINE_RULES:
        out = rx.sub(fn, out)
    out = re.sub(r'(href="[^"]*?)\.md(")', r"\1.html\2", out)
    out = re.sub(
        r'<a href="(https?://[^"]+)"',
        r'<a href="\1" target="_blank" rel="noopener noreferrer nofollow"',
        out,
    )
    return out


def render_blocks(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i, n = 0, len(lines)
    while i < n:
        stripped = lines[i].strip()
        if not stripped:
            i += 1
            continue
        if stripped.startswith("```"):
            lang = stripped[3:].strip()
            i += 1
            buf: list[str] = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            cls = ' class="language-' + esc(lang) + '"' if lang else ""
            out.append("<pre><code" + cls + ">" + esc("\n".join(buf)) + "</code></pre>")
            continue
        if stripped.startswith("|") and i + 1 < n and TABLE_SEP_RE.match(lines[i + 1].strip()):
            header = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            rows: list[list[str]] = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            parts = ["<table>", "<thead>", "<tr>"]
            parts += ["<th>" + inline(c) + "</th>" for c in header]
            parts += ["</tr>", "</thead>", "<tbody>"]
            for row in rows:
                parts.append("<tr>")
                parts += ["<td>" + inline(c) + "</td>" for c in row]
                parts.append("</tr>")
            parts += ["</tbody>", "</table>"]
            out.append("".join(parts))
            continue
        m = HEADING_RE.match(stripped)
        if m:
            level = len(m.group(1))
            out.append(f"<h{level}>" + inline(m.group(2)) + f"</h{level}>")
            i += 1
            continue
        if UL_RE.match(stripped):
            items = []
            while i < n and UL_RE.match(lines[i].strip()):
                items.append(UL_RE.match(lines[i].strip()).group(1))
                i += 1
            out.append("<ul>" + "".join("<li>" + inline(t) + "</li>" for t in items) + "</ul>")
            continue
        m = OL_RE.match(stripped)
        if m:
            start = int(m.group(1))
            items = [m.group(2)]
            i += 1
            while i < n and OL_RE.match(lines[i].strip()):
                items.append(OL_RE.match(lines[i].strip()).group(2))
                i += 1
            attr = f' start="{start}"' if start != 1 else ""
            out.append(f"<ol{attr}>" + "".join("<li>" + inline(t) + "</li>" for t in items) + "</ol>")
            continue
        if stripped == "---":
            out.append("<hr>")
            i += 1
            continue
        para = [stripped]
        i += 1
        while i < n:
            nxt = lines[i].strip()
            if (not nxt or nxt == "---" or nxt.startswith(("#", "```", "|"))
                    or UL_RE.match(nxt) or OL_RE.match(nxt)):
                break
            para.append(nxt)
            i += 1
        out.append("<p>" + inline(" ".join(para)) + "</p>")
    return "\n".join(out)


def render_document(raw: str) -> tuple[str, str, str]:
    """Return (title, description, body_html) for a house-style markdown file."""
    m = H1_RE.match(raw.lstrip().splitlines()[0].strip()) if raw.strip() else None
    title = m.group(1).strip() if m else "Fontlore"
    body = render_blocks(raw)
    desc = ""
    for line in raw.splitlines()[1:]:
        if line.strip():
            desc = line.strip()
            break
    if desc.lower().startswith("what this reference covers:"):
        desc = desc[len("What this reference covers:"):]
    desc = re.sub(r"\s+", " ", desc).strip()
    if len(desc) > 160:
        desc = desc[:157].rstrip() + "..."
    return title, desc, body


# ---------------------------------------------------------------------------
# Page shell
# ---------------------------------------------------------------------------

def page(title: str, desc: str, body: str, prefix: str = "", crumb: list | None = None) -> str:
    nav = f"""
    <a class="brand" href="{prefix}index.html"><span>Font</span><span class="brand-accent">lore</span></a>
    <nav class="nav" aria-label="Primary">
      <a href="{prefix}index.html">Home</a>
      <a href="{prefix}browse.html">Browse</a>
      <a href="{prefix}browse.html#references">References</a>
      <a href="{REPO_URL}" target="_blank" rel="noopener noreferrer">GitHub</a>
    </nav>"""
    crumbs = ""
    if crumb:
        bits = ['<nav class="crumbs" aria-label="Breadcrumb">']
        for label, href in crumb:
            if href:
                bits.append(f'<a href="{prefix}{href}">{esc(label)}</a>')
            else:
                bits.append(f"<span aria-current=\"page\">{esc(label)}</span>")
            bits.append('<span class="crumb-sep">/</span>')
        bits.pop()
        bits.append("</nav>")
        crumbs = "".join(bits)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<meta name="theme-color" content="#F7F1E8">
<title>{esc(title)} - Fontlore</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(title)} - Fontlore">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<link rel="icon" type="image/svg+xml" href="{prefix}assets/favicon.svg">
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
<header class="site-header">
  <div class="container header-inner">{nav}</div>
</header>
<main class="container">
{crumbs}
{body}
</main>
<footer class="site-footer">
  <div class="container footer-inner">
    <div class="footer-brand">
      <a class="brand" href="{prefix}index.html"><span>Font</span><span class="brand-accent">lore</span></a>
      <p>Typeface intelligence for AI agents.<br>MIT licensed. No tracking, no vibes.</p>
    </div>
    <div class="footer-col">
      <h3>Library</h3>
      <a href="{prefix}browse.html#references">References (95)</a>
      <a href="{prefix}browse.html#fonts">Fonts (165)</a>
      <a href="{prefix}browse.html#pairings">Pairings (66)</a>
      <a href="{prefix}browse.html#tools">Tools (71)</a>
    </div>
    <div class="footer-col">
      <h3>Project</h3>
      <a href="{REPO_URL}" target="_blank" rel="noopener noreferrer">GitHub repository</a>
      <a href="{REPO_URL}/blob/main/LICENSE" target="_blank" rel="noopener noreferrer">MIT License</a>
      <a href="{REPO_URL}/blob/main/CONTRIBUTING.md" target="_blank" rel="noopener noreferrer">Contributing</a>
      <a href="{prefix}privacy.html">Privacy</a>
      <a href="{prefix}terms.html">Terms</a>
    </div>
  </div>
  <div class="container footer-base">
    <span>Compiled 2025 as part of the Fontlore project.</span>
    <span>Created by Zynu (@izynu) &middot; Maintained by Shraddha (@xhraddha)</span>
  </div>
</footer>
</body>
</html>
"""


def breadcrumb(items: list) -> str:
    bits = ['<nav class="crumbs" aria-label="Breadcrumb">']
    for label, href in items:
        if href:
            bits.append(f'<a href="{href}">{esc(label)}</a>')
        else:
            bits.append(f'<span aria-current="page">{esc(label)}</span>')
        bits.append('<span class="crumb-sep">/</span>')
    bits.pop()
    bits.append("</nav>")
    return "".join(bits)


# ---------------------------------------------------------------------------
# Assets
# ---------------------------------------------------------------------------

STYLE_CSS = """:root{
  --paper:#F7F1E8;--panel:#F0E4D2;--card:#FFFDF8;
  --ink:#1C1917;--ink-soft:#4A4238;--muted:#6E6353;
  --line:#E3D7C5;--line-soft:#EDE3D3;--accent:#A63D2F;--accent-soft:#F3E0D8;
  --serif:'Iowan Old Style','Palatino Linotype',Palatino,Georgia,'Times New Roman',serif;
  --sans:system-ui,-apple-system,'Segoe UI','Helvetica Neue',Arial,sans-serif;
  --mono:ui-monospace,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:16px;line-height:1.65;display:flex;flex-direction:column;min-height:100vh}
.container{width:100%;max-width:1080px;margin:0 auto;padding:0 24px}
main.container{flex:1;padding-top:28px;padding-bottom:72px}
a{color:var(--accent)}
a:hover{color:var(--accent)}
h1,h2,h3{font-family:var(--serif);line-height:1.15;letter-spacing:-0.01em}
h1{font-size:clamp(2rem,4.6vw,3.2rem);margin:.4rem 0 1rem}
h2{font-size:1.7rem;margin:2.4rem 0 .8rem}
h3{font-size:1.15rem;margin:1.6rem 0 .5rem}
p{margin:.6rem 0}
code{font-family:var(--mono);font-size:.9em;background:var(--panel);border:1px solid var(--line);border-radius:5px;padding:.08em .35em}
pre{background:var(--ink);color:#F3EDE3;border-radius:10px;padding:18px 20px;overflow-x:auto}
pre code{background:none;border:none;color:inherit;padding:0;font-size:13.5px;line-height:1.6}
table{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.94rem;background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:hidden}
th{font-family:var(--mono);font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);text-align:left;padding:10px 14px;border-bottom:1px solid var(--line);background:var(--panel)}
td{padding:10px 14px;border-bottom:1px solid var(--line-soft);vertical-align:top}
tr:last-child td{border-bottom:none}
ul,ol{padding-left:1.4rem}
li{margin:.3rem 0}
hr{border:none;border-top:1px solid var(--line);margin:2.2rem 0}

.site-header{position:sticky;top:0;z-index:50;background:rgba(247,241,232,.94);backdrop-filter:blur(6px);border-bottom:1px solid var(--line)}
.header-inner{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-top:14px;padding-bottom:14px;flex-wrap:wrap}
.brand{font-family:var(--serif);font-size:1.45rem;color:var(--ink);text-decoration:none;letter-spacing:-0.02em}
.brand span{color:var(--ink)}
.brand .brand-accent{color:var(--accent)}
.nav{display:flex;gap:22px;flex-wrap:wrap}
.nav a{color:var(--ink-soft);text-decoration:none;font-size:.95rem}
.nav a:hover{color:var(--accent)}

.crumbs{font-family:var(--mono);font-size:.78rem;color:var(--muted);margin-bottom:18px;letter-spacing:.02em}
.crumbs a{color:var(--muted);text-decoration:none}
.crumbs a:hover{color:var(--accent)}
.crumb-sep{margin:0 8px;color:var(--line)}

.btn{display:inline-flex;align-items:center;gap:8px;border-radius:8px;padding:12px 22px;font-size:.98rem;text-decoration:none;border:1px solid var(--ink);transition:transform .12s ease,box-shadow .12s ease;cursor:pointer}
.btn:hover{transform:translateY(-1px);box-shadow:0 3px 0 rgba(28,25,23,.18)}
.btn-primary{background:var(--ink);color:var(--paper)}
.btn-ghost{background:transparent;color:var(--ink)}
.btn-accent{background:var(--accent);border-color:var(--accent);color:#FFF6EE}

.lede{font-size:1.12rem;color:var(--ink-soft);max-width:640px}
.meta-line{font-family:var(--mono);font-size:.82rem;color:var(--muted);letter-spacing:.03em}

.stats-band{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:1px;background:var(--line);border:1px solid var(--line);border-radius:12px;overflow:hidden;margin:2.2rem 0}
.stat{background:var(--card);padding:20px 18px}
.stat b{display:block;font-family:var(--serif);font-size:2rem;font-weight:600;line-height:1.1}
.stat span{font-family:var(--mono);font-size:.72rem;letter-spacing:.09em;text-transform:uppercase;color:var(--muted)}

.card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:16px}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px 18px;transition:transform .12s ease,border-color .12s ease,box-shadow .12s ease}
.card:hover{transform:translateY(-2px);border-color:#CBBBA0;box-shadow:0 6px 16px rgba(28,25,23,.07)}
.card h3{margin:.1rem 0 .3rem;font-size:1.05rem}
.card p{margin:.2rem 0;font-size:.9rem;color:var(--muted)}
.card .card-link{font-size:.88rem;text-decoration:none;font-weight:600}
.chip{display:inline-block;font-family:var(--mono);font-size:.68rem;letter-spacing:.06em;text-transform:uppercase;border:1px solid var(--line);border-radius:999px;padding:2px 10px;color:var(--ink-soft);background:var(--paper);margin:0 6px 6px 0}
.chip-accent{border-color:var(--accent);color:var(--accent)}
.chip-mono{font-family:var(--mono)}

.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px;margin:1.4rem 0}
.step{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px}
.step .num{font-family:var(--mono);color:var(--accent);font-size:.8rem;letter-spacing:.08em}
.step h3{margin:.3rem 0 .2rem;font-size:1.02rem}
.step p{font-size:.86rem;color:var(--muted);margin:0}

.section-kicker{font-family:var(--mono);font-size:.76rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);margin:0 0 .3rem}

/* Browse page */
.tabbar{display:flex;gap:4px;border-bottom:2px solid var(--line);margin:1.2rem 0 1.6rem;flex-wrap:wrap}
.tab{appearance:none;background:none;border:none;font-family:var(--serif);font-size:1.08rem;color:var(--muted);padding:10px 18px;cursor:pointer;border-bottom:3px solid transparent;margin-bottom:-2px}
.tab:hover{color:var(--ink)}
.tab[aria-selected="true"]{color:var(--ink);border-bottom-color:var(--accent);font-weight:600}
.panel{display:none}
.panel.active{display:block}
.controls{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:18px}
.controls input[type="search"],.controls select{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 14px;font-family:var(--sans);font-size:.94rem;color:var(--ink)}
.controls input[type="search"]{min-width:230px;flex:1}
.controls select{cursor:pointer}
.count-note{font-family:var(--mono);font-size:.78rem;color:var(--muted);margin:0 0 14px}
details.cat{border:1px solid var(--line);border-radius:10px;background:var(--card);margin-bottom:12px}
details.cat summary{cursor:pointer;padding:14px 18px;font-family:var(--serif);font-size:1.08rem;list-style:none;display:flex;justify-content:space-between;align-items:center}
details.cat summary::-webkit-details-marker{display:none}
details.cat summary .cat-count{font-family:var(--mono);font-size:.78rem;color:var(--accent)}
details.cat .cat-body{padding:0 18px 16px}
details.cat .cat-blurb{color:var(--muted);font-size:.9rem;margin:0 0 10px}
.ref-list{columns:2;column-gap:28px;padding-left:1.2rem;margin:0}
.ref-list li{break-inside:avoid}
.pair-card .sample-head{font-family:var(--serif);font-size:1.5rem;line-height:1.2;margin:.2rem 0}
.pair-card .sample-body{font-family:var(--sans);font-size:.92rem;color:var(--ink-soft);margin:0 0 .6rem}
.tool-row{display:flex;justify-content:space-between;gap:14px;align-items:baseline;border-bottom:1px solid var(--line-soft);padding:12px 4px;flex-wrap:wrap}
.tool-row:last-child{border-bottom:none}
.tool-row h3{margin:0;font-size:1rem}
.tool-row p{margin:0;font-size:.88rem;color:var(--muted);flex:1;min-width:220px}
.tool-links a{font-size:.86rem;text-decoration:none;font-weight:600;white-space:nowrap;margin-left:14px}

.doc h1{margin-top:.2rem}
.doc .intro{font-size:1.08rem;color:var(--ink-soft)}
.doc-footer{margin-top:3rem;padding-top:1.2rem;border-top:1px solid var(--line);font-family:var(--mono);font-size:.8rem;color:var(--muted)}
.doc-nav{display:flex;justify-content:space-between;gap:16px;margin-top:1.4rem;flex-wrap:wrap}
.doc-nav a{font-size:.92rem;text-decoration:none;font-weight:600}

.site-footer{background:var(--ink);color:#EFE7DA;margin-top:auto}
.footer-inner{display:grid;grid-template-columns:2fr 1fr 1fr;gap:32px;padding-top:44px;padding-bottom:28px}
.footer-brand .brand{color:#F7F1E8}
.footer-brand .brand span{color:#F7F1E8}
.footer-brand .brand .brand-accent{color:#E08B76}
.footer-brand p{font-size:.88rem;color:#B9AC99;margin:.5rem 0 0}
.footer-col h3{font-family:var(--mono);font-size:.74rem;letter-spacing:.1em;text-transform:uppercase;color:#B9AC99;margin:0 0 10px}
.footer-col a{display:block;color:#EFE7DA;text-decoration:none;font-size:.92rem;padding:3px 0}
.footer-col a:hover{color:#E08B76}
.footer-base{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;border-top:1px solid rgba(239,231,218,.16);padding-top:16px;padding-bottom:28px;font-family:var(--mono);font-size:.76rem;color:#B9AC99}
.site-footer h2,.site-footer h3{color:#F7F1E8}

@media (max-width:720px){
  .footer-inner{grid-template-columns:1fr}
  .ref-list{columns:1}
  .header-inner{padding-top:12px}
  .nav{gap:14px}
}
"""

APP_JS = """(function(){
  var DATA = window.__FONTLORE__;
  function el(tag, cls, text){
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text !== undefined) e.textContent = text;
    return e;
  }
  function chip(text, accent){
    var c = el('span', 'chip' + (accent ? ' chip-accent' : ''), text);
    return c;
  }
  function cardLink(href, label){
    var a = el('a', 'card-link', label || 'Open guide');
    a.href = href;
    return a;
  }

  /* ---------- References panel ---------- */
  var refRoot = document.getElementById('references-root');
  var cats = {};
  DATA.references.forEach(function(r){ (cats[r.category] = cats[r.category] || []).push(r); });
  Object.keys(cats).sort().forEach(function(cat){
    var list = cats[cat];
    var d = el('details', 'cat');
    d.id = 'cat-' + cat;
    if (cat === 'sourcing') d.open = true;
    var s = el('summary');
    s.appendChild(el('span', null, cat.charAt(0).toUpperCase() + cat.slice(1)));
    s.appendChild(el('span', 'cat-count', list.length + ' guides'));
    d.appendChild(s);
    var body = el('div', 'cat-body');
    body.appendChild(el('p', 'cat-blurb', DATA.categoryBlurbs[cat] || ''));
    var ul = el('ul', 'ref-list');
    list.forEach(function(r){
      var li = el('li');
      var a = el('a', null, r.title);
      a.href = r.file;
      li.appendChild(a);
      ul.appendChild(li);
    });
    body.appendChild(ul);
    d.appendChild(body);
    refRoot.appendChild(d);
  });

  /* ---------- Fonts panel ---------- */
  var fontGrid = document.getElementById('fonts-grid');
  var fontNote = document.getElementById('fonts-count');
  function renderFonts(){
    var q = document.getElementById('font-search').value.trim().toLowerCase();
    var cat = document.getElementById('font-category').value;
    var lic = document.getElementById('font-license').value;
    var script = document.getElementById('font-script').value;
    var variable = document.getElementById('font-variable').value;
    fontGrid.innerHTML = '';
    var n = 0;
    var seen = {};
    DATA.fonts.forEach(function(f){
      if (seen[f.slug]) return; seen[f.slug] = 1;
      if (cat && f.category !== cat) return;
      if (lic && f.license !== lic) return;
      if (variable === 'variable' && !f.variable) return;
      if (variable === 'static' && f.variable) return;
      if (script && (f.scripts || []).indexOf(script) === -1) return;
      if (q && (f.family + ' ' + f.designer + ' ' + f.foundry + ' ' + (f.tags||[]).join(' ')).toLowerCase().indexOf(q) === -1) return;
      n++;
      var c = el('article', 'card');
      var h = el('h3');
      var a = el('a', null, f.family);
      a.href = 'guides/fonts/' + f.slug + '.html';
      a.style.color = 'inherit'; a.style.textDecoration = 'none';
      h.appendChild(a);
      c.appendChild(h);
      c.appendChild(el('p', null, f.designer + (f.foundry ? ' - ' + f.foundry : '')));
      var chips = el('div');
      chips.appendChild(chip(f.license, true));
      chips.appendChild(chip(f.category));
      if (f.variable) chips.appendChild(chip('variable'));
      (f.scripts || []).slice(0, 3).forEach(function(s){ chips.appendChild(chip(s)); });
      c.appendChild(chips);
      var lrow = el('div');
      lrow.style.marginTop = '8px';
      var a1 = cardLink('guides/fonts/' + f.slug + '-overview.html', 'Overview');
      var a2 = cardLink('guides/fonts/' + f.slug + '-implementation.html', 'Implementation');
      lrow.appendChild(a1);
      var sep = el('span', null, ' - ');
      sep.style.fontSize = '.86rem';
      lrow.appendChild(sep);
      lrow.appendChild(a2);
      c.appendChild(lrow);
      fontGrid.appendChild(c);
    });
    fontNote.textContent = n + ' of ' + DATA.counts.fonts + ' font records shown';
  }
  ['font-search','font-category','font-license','font-script','font-variable'].forEach(function(id){
    document.getElementById(id).addEventListener(id === 'font-search' ? 'input' : 'change', renderFonts);
  });

  /* ---------- Pairings panel ---------- */
  var pairGrid = document.getElementById('pairings-grid');
  var pairNote = document.getElementById('pairings-count');
  function renderPairs(){
    var q = document.getElementById('pair-search').value.trim().toLowerCase();
    var ctx = document.getElementById('pair-context').value;
    pairGrid.innerHTML = '';
    var n = 0;
    DATA.pairings.forEach(function(p){
      if (ctx && p.context !== ctx) return;
      if (q && ((p.headingFamily + ' ' + p.bodyFamily + ' ' + p.context + ' ' + p.rationale).toLowerCase().indexOf(q) === -1)) return;
      n++;
      var c = el('article', 'card pair-card');
      c.appendChild(chip(p.context, true));
      c.appendChild(el('p', 'sample-head', p.headingFamily));
      c.appendChild(el('p', 'sample-body', 'paired with ' + p.bodyFamily));
      c.appendChild(el('p', null, p.rationale));
      var links = el('div');
      links.style.marginTop = '8px';
      var a0 = cardLink('guides/pairings/' + p.file + '.html', 'Pairing guide');
      var a1 = cardLink('guides/fonts/' + p.heading + '-overview.html', p.headingFamily);
      var a2 = cardLink('guides/fonts/' + p.body + '-overview.html', p.bodyFamily);
      links.appendChild(a0);
      var sep = el('span', null, ' - ');
      sep.style.fontSize = '.86rem';
      links.appendChild(sep);
      links.appendChild(a1);
      var sep2 = el('span', null, ' + ');
      sep2.style.fontSize = '.86rem';
      links.appendChild(sep2);
      links.appendChild(a2);
      c.appendChild(links);
      pairGrid.appendChild(c);
    });
    pairNote.textContent = n + ' of ' + DATA.counts.pairings + ' curated pairings shown';
  }
  ['pair-search','pair-context'].forEach(function(id){
    document.getElementById(id).addEventListener(id === 'pair-search' ? 'input' : 'change', renderPairs);
  });

  /* ---------- Tools panel ---------- */
  var toolList = document.getElementById('tools-list');
  var toolNote = document.getElementById('tools-count');
  function renderTools(){
    var q = document.getElementById('tool-search').value.trim().toLowerCase();
    var section = document.getElementById('tool-section').value;
    toolList.innerHTML = '';
    var n = 0;
    DATA.tools.forEach(function(t){
      if (section && t.section !== section) return;
      if (q && ((t.name + ' ' + t.what).toLowerCase().indexOf(q) === -1)) return;
      n++;
      var row = el('div', 'tool-row');
      var left = el('div');
      left.style.minWidth = '160px';
      var h = el('h3');
      h.appendChild(el('span', null, t.name));
      h.style.color = 'inherit';
      left.appendChild(h);
      left.appendChild(chip(t.section));
      row.appendChild(left);
      row.appendChild(el('p', null, t.what));
      var links = el('div', 'tool-links');
      var visit = el('a', null, 'Visit site');
      visit.href = t.url;
      visit.target = '_blank';
      visit.rel = 'noopener noreferrer nofollow';
      links.appendChild(visit);
      var guide = el('a', null, 'Guide');
      guide.href = 'guides/tools/' + t.slug + '.html';
      links.appendChild(guide);
      row.appendChild(links);
      toolList.appendChild(row);
    });
    toolNote.textContent = n + ' of ' + DATA.counts.tools + ' tools shown';
  }
  ['tool-search','tool-section'].forEach(function(id){
    document.getElementById(id).addEventListener(id === 'tool-search' ? 'input' : 'change', renderTools);
  });

  renderFonts(); renderPairs(); renderTools();

  /* ---------- Tabs + deep links ---------- */
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.tab'));
  var panels = {
    'references': document.getElementById('panel-references'),
    'fonts': document.getElementById('panel-fonts'),
    'pairings': document.getElementById('panel-panel'),
    'tools': document.getElementById('panel-tools')
  };
  function selectTab(name, push){
    if (!panels[name]) name = 'references';
    tabs.forEach(function(t){ t.setAttribute('aria-selected', String(t.dataset.tab === name)); });
    Object.keys(panels).forEach(function(k){ panels[k].classList.toggle('active', k === name); });
    if (push && history.replaceState) history.replaceState(null, '', '#' + name);
  }
  tabs.forEach(function(t){ t.addEventListener('click', function(){ selectTab(t.dataset.tab, true); }); });
  var hash = (location.hash || '').replace('#','');
  var params = new URLSearchParams(location.search);
  var wanted = params.get('tab') || hash;
  if (hash === 'references' || params.get('category')) {
    selectTab('references', false);
    var cat = params.get('category');
    if (cat) {
      var target = document.getElementById('cat-' + cat);
      if (target) { target.open = true; setTimeout(function(){ target.scrollIntoView({behavior:'smooth', block:'start'}); }, 60); }
    }
  } else if (wanted) {
    selectTab(wanted, false);
  } else {
    selectTab('references', false);
  }
})();
"""

FAVICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="12" fill="#F7F1E8"/>
  <rect x="1.5" y="1.5" width="61" height="61" rx="10.5" fill="none" stroke="#E3D7C5" stroke-width="2"/>
  <text x="30" y="45" font-family="Georgia, 'Times New Roman', serif" font-size="38" fill="#1C1917" text-anchor="middle">F</text>
  <circle cx="46" cy="42" r="4" fill="#A63D2F"/>
</svg>
"""

# ---------------------------------------------------------------------------
# Landing page
# ---------------------------------------------------------------------------

def build_index(fonts: list, pairings: list, tools: list, ref_counts: dict) -> str:
    refs_total = sum(ref_counts.values())
    body = f"""
<section style="padding:34px 0 10px">
  <p class="section-kicker">Open-source skill - MIT licensed</p>
  <h1>Typeface intelligence<br>for AI agents.</h1>
  <p class="lede">Fontlore gives AI assistants a curated knowledge base to research, select, pair, license, and implement fonts with evidence. Real catalogs, real licenses, real tradeoffs. No vibes.</p>
  <p style="margin-top:22px;display:flex;gap:12px;flex-wrap:wrap">
    <a class="btn btn-primary" href="browse.html">Browse the library</a>
    <a class="btn btn-ghost" href="{REPO_URL}" target="_blank" rel="noopener noreferrer">View on GitHub</a>
  </p>
  <p class="meta-line">MIT &middot; {727} guides and references &middot; no cookies, no analytics</p>
</section>

<div class="stats-band">
  <div class="stat"><b>727</b><span>Guides and references</span></div>
  <div class="stat"><b>{len(fonts)}</b><span>Font records</span></div>
  <div class="stat"><b>{len(pairings)}</b><span>Vetted pairings</span></div>
  <div class="stat"><b>{len(tools)}</b><span>Tools and sources</span></div>
  <div class="stat"><b>{len(ref_counts)}</b><span>Reference categories</span></div>
</div>

<section>
  <p class="section-kicker">The library</p>
  <h2>Nine curated reference categories</h2>
  <p class="lede">Every category answers one operational question. Each guide follows one house style, cross-links its neighbors, and ends in a checkable artifact.</p>
  <div class="card-grid" style="margin-top:18px">"""
    for cat, n in sorted(ref_counts.items()):
        body += f"""
    <article class="card">
      <h3>{cat.capitalize()}</h3>
      <p>{CATEGORY_BLURBS[cat]}</p>
      <a class="card-link" href="browse.html?category={cat}">{n} guides &rarr;</a>
    </article>"""
    body += f"""
  </div>
</section>

<section>
  <p class="section-kicker">The engine</p>
  <h2>From brief to handoff, deterministically</h2>
  <div class="steps">
    <div class="step"><span class="num">01</span><h3>Brief</h3><p>Project type, audience, tone, medium.</p></div>
    <div class="step"><span class="num">02</span><h3>Constraints</h3><p>Scripts, license scope, sizes, delivery.</p></div>
    <div class="step"><span class="num">03</span><h3>Score</h3><p>Rubric ranking with printed reasons.</p></div>
    <div class="step"><span class="num">04</span><h3>Pair</h3><p>Curated heading plus body, with rationale.</p></div>
    <div class="step"><span class="num">05</span><h3>Handoff</h3><p>CSS, tokens, and evidence to re-check.</p></div>
  </div>
  <p><a href="{REPO_URL}/blob/main/MASTER-SKILL.md" target="_blank" rel="noopener noreferrer">Read the full pipeline in MASTER-SKILL.md &rarr;</a></p>
</section>

<section>
  <p class="section-kicker">Data integrity</p>
  <h2>Verified, or null</h2>
  <div class="card-grid" style="margin-top:18px">
    <article class="card"><h3>Source URLs on every record</h3><p>Each font points at its own foundry page or repository. Verified at the source, not at aggregators.</p></article>
    <article class="card"><h3>Null, never guessed</h3><p>Unverifiable values stay null. The schema makes missing data visible instead of plausible.</p></article>
    <article class="card"><h3>CI-gated on every commit</h3><p>validate.py checks JSON schemas, pairing integrity, house style, and every cross-link before merge.</p></article>
    <article class="card"><h3>Licenses as SPDX ids</h3><p>OFL-1.1, Apache-2.0, UFL-1.0, ITF-FFL-1.0, MIT. Anything else must be read in full, in the guide.</p></article>
  </div>
</section>

<section>
  <p class="section-kicker">Quick start</p>
  <h2>Run the decision engine</h2>
  <pre><code>git clone {REPO_URL}.git
cd fontlore
python3 scripts/decide.py --project dashboard --script latin --tone neutral
python3 scripts/decide.py --project marketing --script devanagari --tone editorial --json</code></pre>
  <p>Hard-filters by script and license, scores against the rubric, prints ranked reasons, and suggests curated pairings.</p>
</section>

<section style="margin-top:30px;background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:30px">
  <h2 style="margin-top:0">Build the site yourself</h2>
  <p class="lede">This entire site is generated from the data layer by a single stdlib-only script. After any data change:</p>
  <pre><code>python3 scripts/build_site.py</code></pre>
  <p>727 pages, no dependencies, no tracking. Deployed to GitHub Pages by the included workflow.</p>
</section>
"""
    return page("Typeface intelligence for AI agents",
                "Fontlore: an open-source typography skill with 727 guides and references, 165 verified font records, 66 curated pairings, and a deterministic decision engine.",
                body)


# ---------------------------------------------------------------------------
# Browse page
# ---------------------------------------------------------------------------

def build_browse(fonts: list, pairings: list, tools: list, refs: list) -> str:
    ref_counts: dict = {}
    for r in refs:
        ref_counts[r["category"]] = ref_counts.get(r["category"], 0) + 1
    categories = sorted(ref_counts)
    data_payload = {
        "counts": {"fonts": len(fonts), "pairings": len(pairings), "tools": len(tools)},
        "categoryBlurbs": CATEGORY_BLURBS,
        "references": refs,
        "fonts": [
            {k: f.get(k) for k in ("slug", "family", "designer", "foundry", "license",
                                    "category", "classification", "scripts", "variable", "tags")}
            for f in fonts
        ],
        "pairings": [
            {"file": f"pair-{i + 1:03d}", "heading": p["heading"], "body": p["body"],
             "context": p["context"], "rationale": p["rationale"],
             "headingFamily": p.get("headingFamily", p["heading"]),
             "bodyFamily": p.get("bodyFamily", p["body"])}
            for i, p in enumerate(pairings)
        ],
        "tools": [
            {k: t.get(k) for k in ("slug", "name", "url", "section", "what")}
            for t in tools
        ],
    }
    payload_json = json.dumps(data_payload, ensure_ascii=False).replace("</", "<\\/")
    cat_opts = "".join(f'<option value="{c}">{c.capitalize()}</option>' for c in categories)
    licenses = sorted({f.get("license") for f in fonts if f.get("license")})
    lic_opts = "".join(f'<option value="{l}">{l}</option>' for l in licenses)
    scripts = sorted({s for f in fonts for s in (f.get("scripts") or [])})
    script_opts = "".join(f'<option value="{s}">{s}</option>' for s in scripts)
    contexts = sorted({p.get("context") for p in pairings if p.get("context")})
    ctx_opts = "".join(f'<option value="{c}">{c}</option>' for c in contexts)
    sections = sorted({t.get("section") for t in tools if t.get("section")})
    sec_opts = "".join(f'<option value="{s}">{s}</option>' for s in sections)

    body = f"""
<p class="section-kicker">The full library</p>
<h1>Browse Fontlore</h1>
<p class="lede">Every guide in the repository, one click away. Four tabs: the nine reference categories, the font records, the curated pairings, and the tool catalog.</p>

<div class="tabbar" role="tablist" aria-label="Library sections">
  <button class="tab" role="tab" data-tab="references" aria-selected="true" id="tab-references">References (95)</button>
  <button class="tab" role="tab" data-tab="fonts" aria-selected="false" id="tab-fonts">Fonts (165)</button>
  <button class="tab" role="tab" data-tab="pairings" aria-selected="false" id="tab-pairings">Pairings (66)</button>
  <button class="tab" role="tab" data-tab="tools" aria-selected="false" id="tab-tools">Tools (71)</button>
</div>

<section id="panel-references" class="panel active" role="tabpanel" aria-labelledby="tab-references">
  <p class="lede">Curated, hand-written guides. Start with the category that matches your task.</p>
  <div id="references-root"></div>
</section>

<section id="panel-fonts" class="panel" role="tabpanel" aria-labelledby="tab-fonts">
  <div class="controls">
    <input type="search" id="font-search" placeholder="Search 165 fonts: family, designer, tag..." aria-label="Search fonts">
    <select id="font-category" aria-label="Filter by category"><option value="">All categories</option>{cat_opts}</select>
    <select id="font-license" aria-label="Filter by license"><option value="">All licenses</option>{lic_opts}</select>
    <select id="font-script" aria-label="Filter by script"><option value="">All scripts</option>{script_opts}</select>
    <select id="font-variable" aria-label="Filter by variability"><option value="">Variable and static</option><option value="variable">Variable only</option><option value="static">Static only</option></select>
  </div>
  <p class="count-note" id="fonts-count"></p>
  <div class="card-grid" id="fonts-grid"></div>
</section>

<section id="panel-panel" class="panel" role="tabpanel" aria-labelledby="tab-pairings">
  <div class="controls">
    <input type="search" id="pair-search" placeholder="Search 66 pairings: family, context, rationale..." aria-label="Search pairings">
    <select id="pair-context" aria-label="Filter by context"><option value="">All contexts</option>{ctx_opts}</select>
  </div>
  <p class="count-note" id="pairings-count"></p>
  <div class="card-grid" id="pairings-grid"></div>
</section>

<section id="panel-tools" class="panel" role="tabpanel" aria-labelledby="tab-tools">
  <div class="controls">
    <input type="search" id="tool-search" placeholder="Search 71 tools..." aria-label="Search tools">
    <select id="tool-section" aria-label="Filter by stage"><option value="">All stages</option>{sec_opts}</select>
  </div>
  <p class="count-note" id="tools-count"></p>
  <div class="card" id="tools-list" style="padding:6px 18px"></div>
</section>

<script>window.__FONTLORE__ = {payload_json};</script>
<script src="assets/app.js"></script>
"""
    return page("Browse the library",
                "Browse all Fontlore guides: 9 reference categories, 165 font records, 66 curated pairings, and 71 tools. Search and filter everything.",
                body, crumb=[("Home", "index.html"), ("Browse", None)])


# ---------------------------------------------------------------------------
# Legal pages
# ---------------------------------------------------------------------------

def build_privacy() -> str:
    body = """
<p class="section-kicker">Legal</p>
<h1>Privacy</h1>
<p class="doc intro">Fontlore collects nothing. This page states exactly what runs, what is stored, and who to contact.</p>

<h2>What this site does not do</h2>
<ul>
  <li>No cookies, no local-storage identifiers, no session storage.</li>
  <li>No analytics, no telemetry, no beacons, no fingerprinting.</li>
  <li>No accounts, no forms, no comment systems.</li>
  <li>No external requests: styles, scripts, and data are served from this site only.</li>
</ul>

<h2>What is processed</h2>
<p>Standard server access logs are kept by GitHub Pages (the hosting infrastructure), governed by <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" target="_blank" rel="noopener noreferrer">GitHub's Privacy Statement</a>. This project does not control those logs and does not receive individual visitor data from GitHub.</p>

<h2>Content licensing and attribution</h2>
<p>Font records link to each typeface project's own source page. Licenses are recorded as SPDX-style identifiers and must be verified at the source before commercial use. The typefaces referenced remain the property of their respective authors and foundries.</p>

<h2>Contact</h2>
<p>Privacy questions or corrections: open an issue at <a href="https://github.com/izynu/fontlore/issues" target="_blank" rel="noopener noreferrer">github.com/izynu/fontlore/issues</a>.</p>
<div class="doc-footer">Compiled 2025 as part of the Fontlore project.</div>
"""
    return page("Privacy", "Fontlore collects nothing: no cookies, no analytics, no tracking. Static pages only, hosted by GitHub Pages.", body, crumb=[("Home", "index.html"), ("Privacy", None)])


def build_terms() -> str:
    body = """
<p class="section-kicker">Legal</p>
<h1>Terms and conditions</h1>
<p class="doc intro">Plain-language terms for using the Fontlore repository and website.</p>

<h2>1. License</h2>
<p>The Fontlore repository (guides, data, scripts, and site) is released under the <a href="https://github.com/izynu/fontlore/blob/main/LICENSE" target="_blank" rel="noopener noreferrer">MIT License</a>. You may copy, modify, and redistribute it with attribution and the license notice.</p>

<h2>2. Typeface trademarks and licenses</h2>
<p>Font names, designs, and trademarks referenced in Fontlore remain the property of their respective authors and foundries. Fontlore records metadata and links to sources; it does not grant any rights to use the typefaces themselves. Each font's own license governs its use.</p>

<h2>3. Accuracy</h2>
<p>Data is verified against source URLs at the time it was written and marked null where unverifiable. Catalogs change; verify license terms and file metadata at the source before relying on any record, especially commercially.</p>

<h2>4. External links</h2>
<p>External links are provided for verification, not endorsement. We do not control third-party sites and are not responsible for their content or availability.</p>

<h2>5. No warranty</h2>
<p>The site and repository are provided "as is", without warranty of any kind, express or implied. Use at your own risk. Nothing here is legal advice; for high-stakes licensing, read the actual license text and consult counsel.</p>

<h2>6. Changes</h2>
<p>These terms may be updated as the project evolves. Material changes are announced in the repository's commit history and releases.</p>

<h2>7. Contact</h2>
<p>Questions: open an issue or discussion at <a href="https://github.com/izynu/fontlore" target="_blank" rel="noopener noreferrer">github.com/izynu/fontlore</a>.</p>
<div class="doc-footer">Compiled 2025 as part of the Fontlore project.</div>
"""
    return page("Terms and conditions", "Plain-language terms for the Fontlore repository and website: MIT license, trademark notice, accuracy disclaimer, no warranty.", body, crumb=[("Home", "index.html"), ("Terms", None)])


def build_404() -> str:
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found - Fontlore</title>
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
<style>
body{margin:0;background:#F7F1E8;color:#1C1917;font-family:Georgia,'Times New Roman',serif;display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center;padding:24px}
a{color:#A63D2F}
.mono{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.8rem;color:#6E6353;letter-spacing:.08em;text-transform:uppercase}
h1{font-size:clamp(2.4rem,7vw,4rem);margin:.4rem 0}
</style>
</head>
<body>
<div>
  <p class="mono">404 - glyph not found</p>
  <h1>This page fell off the baseline.</h1>
  <p><a href="index.html">Back to Fontlore</a> &middot; <a href="browse.html">Browse the library</a></p>
</div>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def main() -> None:
    fonts = json.loads((ROOT / "data" / "fonts.json").read_text(encoding="utf-8"))["fonts"]
    pairings_raw = json.loads((ROOT / "data" / "pairings.json").read_text(encoding="utf-8"))["pairings"]
    tools_raw = json.loads((ROOT / "data" / "tools.json").read_text(encoding="utf-8"))["tools"]

    family_by_slug = {f["slug"]: f["family"] for f in fonts}
    pairings = []
    for p in pairings_raw:
        q = dict(p)
        q["headingFamily"] = family_by_slug.get(p["heading"], p["heading"])
        q["bodyFamily"] = family_by_slug.get(p["body"], p["body"])
        pairings.append(q)

    tools = []
    for t in tools_raw:
        q = dict(t)
        q["slug"] = re.sub(r"[^a-z0-9]+", "-", t["name"].lower()).strip("-")
        tools.append(q)
    tool_slugs = {t["slug"] for t in tools}

    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "assets" / "data").mkdir(parents=True)

    # static assets
    (SITE / "assets" / "style.css").write_text(STYLE_CSS, encoding="utf-8")
    (SITE / "assets" / "app.js").write_text(APP_JS, encoding="utf-8")
    (SITE / "assets" / "favicon.svg").write_text(FAVICON_SVG, encoding="utf-8")

    # references pages + index entries
    refs_index: list[dict] = []
    ref_counts: dict[str, int] = {}
    for cat_dir in sorted((ROOT / "references").iterdir()):
        if not cat_dir.is_dir():
            continue
        cat = cat_dir.name
        (SITE / "references" / cat).mkdir(parents=True)
        for md_path in sorted(cat_dir.glob("*.md")):
            if md_path.name == "README.md":
                continue
            title, desc, body_md = render_document(md_path.read_text(encoding="utf-8"))
            crumb_html = breadcrumb([
                ("Home", "../../index.html"),
                ("References", "../../browse.html#references"),
                (cat.capitalize(), None),
            ])
            doc = f"""
{crumb_html}
<article class="doc">
{body_md}
<div class="doc-footer">Part of the Fontlore reference library. <a href="../../browse.html#references">Back to all references</a>.</div>
</article>"""
            out = page(title, desc, doc, prefix="../../")
            (SITE / "references" / cat / (md_path.stem + ".html")).write_text(out, encoding="utf-8")
            refs_index.append({"category": cat, "title": title,
                               "file": f"references/{cat}/{md_path.stem}.html"})
            ref_counts[cat] = ref_counts.get(cat, 0) + 1

    # guides pages
    generated = 0
    for kind in ("fonts", "pairings", "tools"):
        kdir = ROOT / "guides" / kind
        if not kdir.is_dir():
            continue
        (SITE / "guides" / kind).mkdir(parents=True)
        for md_path in sorted(kdir.glob("*.md")):
            if md_path.name == "README.md":
                continue
            title, desc, body_md = render_document(md_path.read_text(encoding="utf-8"))
            crumb_html = breadcrumb([
                ("Home", "../../index.html"),
                ("Browse", "../../browse.html#" + kind),
                (kind.capitalize(), None),
            ])
            doc = f"""
{crumb_html}
<article class="doc">
{body_md}
<div class="doc-footer">Generated from the Fontlore data layer. <a href="../../browse.html#{kind}">Back to all {kind}</a>.</div>
</article>"""
            out = page(title, desc, doc, prefix="../../")
            (SITE / "guides" / kind / (md_path.stem + ".html")).write_text(out, encoding="utf-8")
            generated += 1

    # landing, browse, legal, 404
    (SITE / "index.html").write_text(build_index(fonts, pairings, tools, ref_counts), encoding="utf-8")
    (SITE / "browse.html").write_text(build_browse(fonts, pairings, tools, refs_index), encoding="utf-8")
    (SITE / "privacy.html").write_text(build_privacy(), encoding="utf-8")
    (SITE / "terms.html").write_text(build_terms(), encoding="utf-8")
    (SITE / "404.html").write_text(build_404(), encoding="utf-8")

    # machine data (kept for API-ish consumers)
    for name, payload in (("fonts.json", {"count": len(fonts), "fonts": fonts}),
                          ("pairings.json", {"count": len(pairings), "pairings": pairings}),
                          ("tools.json", {"count": len(tools), "tools": tools})):
        (SITE / "assets" / "data" / name).write_text(
            json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    # sitemap + robots
    urls = ["", "browse.html", "privacy.html", "terms.html"]
    for r in refs_index:
        urls.append(r["file"])
    for kind in ("fonts", "pairings", "tools"):
        for md_path in sorted((ROOT / "guides" / kind).glob("*.md")):
            if md_path.name != "README.md":
                urls.append(f"guides/{kind}/{md_path.stem}.html")
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{LIVE_URL}{u}</loc></url>")
    sm.append("</urlset>")
    (SITE / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")
    (SITE / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {LIVE_URL}sitemap.xml\n", encoding="utf-8")

    html_count = sum(1 for _ in SITE.rglob("*.html"))
    print(f"Built site: {html_count} HTML pages "
          f"({len(refs_index)} references + {generated} generated guides + shell pages), "
          f"sitemap with {len(urls)} URLs.")


if __name__ == "__main__":
    main()
