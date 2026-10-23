#!/usr/bin/env python3
"""Fontlore repository quality gate.

Validates:
  1. Data layer (data/fonts.json, data/pairings.json, data/tools.json)
  2. Reference and generated guide house style
  3. Cross-reference links resolve
  4. Python scripts compile

Usage:
  python3 scripts/validate.py            # full check
  python3 scripts/validate.py --data     # data layer only
  python3 scripts/validate.py --docs     # markdown docs only

Exit code 0 = pass, 1 = failures found.
"""

from __future__ import annotations

import json
import py_compile
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS_DIRS = [ROOT / "references", ROOT / "guides"]
SCRIPTS = ROOT / "scripts"

ALLOWED_LICENSES = {
    "OFL-1.1",
    "Apache-2.0",
    "UFL-1.0",
    "ITF-FFL-1.0",
    "MIT",
    "Custom-OFL-based",
}

FONT_REQUIRED_FIELDS = {
    "slug", "family", "designer", "foundry", "license", "category",
    "classification", "scripts", "variable", "axes", "weights",
    "subsets", "source", "tags",
}

MIN_LINES = 140
MAX_LINES = 320

# Generated compendium guides (one per font / pairing / tool) are intentionally
# shorter, data-driven pages. They get their own bounds.
GENERATED_DIRS = ("fonts", "pairings", "tools")
GEN_MIN_LINES = 40
GEN_MAX_LINES = 120

FOOTER_LINE = "Compiled 2025 as part of the Fontlore project."

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def check_ascii(path: Path, text: str) -> None:
    try:
        text.encode("ascii")
    except UnicodeEncodeError as e:
        col = e.start
        line_no = text[:col].count("\n") + 1
        snippet = text[max(0, col - 20):col + 20].replace("\n", "\\n")
        err(f"{path}: non-ASCII character near line {line_no}: ...{snippet}...")


def validate_fonts(raw: dict) -> dict[str, dict]:
    fonts = raw.get("fonts")
    if not isinstance(fonts, list) or not fonts:
        err("fonts.json: missing non-empty 'fonts' array")
        return {}
    slugs = {}
    for i, f in enumerate(fonts):
        where = f"fonts.json[{i}]"
        if not isinstance(f, dict):
            err(f"{where}: not an object")
            continue
        missing = FONT_REQUIRED_FIELDS - set(f)
        if missing:
            err(f"{where} ({f.get('slug', '?')}): missing fields {sorted(missing)}")
        slug = f.get("slug")
        if not slug or not re.fullmatch(r"[a-z0-9-]+", str(slug)):
            err(f"{where}: bad slug {slug!r}")
            continue
        if slug in slugs:
            err(f"{where}: duplicate slug {slug}")
        slugs[slug] = f
        lic = f.get("license")
        if lic not in ALLOWED_LICENSES:
            err(f"{where} ({slug}): license {lic!r} not in allowed set")
        for url_field in ("source", "specimen"):
            u = f.get(url_field)
            if u is not None and not str(u).startswith("https://"):
                err(f"{where} ({slug}): {url_field} must be https, got {u!r}")
        if f.get("variable") is False and f.get("axes"):
            err(f"{where} ({slug}): static font cannot declare axes")
    return slugs


def validate_pairings(raw: dict, slugs: dict[str, dict]) -> None:
    pairings = raw.get("pairings")
    if not isinstance(pairings, list) or not pairings:
        err("pairings.json: missing non-empty 'pairings' array")
        return
    seen_pairs = set()
    for i, p in enumerate(pairings):
        where = f"pairings.json[{i}]"
        if not isinstance(p, dict):
            err(f"{where}: not an object")
            continue
        for field in ("heading", "body", "context", "rationale"):
            if not p.get(field):
                err(f"{where}: missing {field}")
        h, b = p.get("heading"), p.get("body")
        if h not in slugs:
            err(f"{where}: heading slug {h!r} not found in fonts.json")
        if b not in slugs:
            err(f"{where}: body slug {b!r} not found in fonts.json")
        if h and h == b:
            err(f"{where}: self-pairing {h}")
        if h and b:
            key = frozenset((h, b))
            if key in seen_pairs:
                err(f"{where}: duplicate direction-agnostic pair {h} + {b}")
            seen_pairs.add(key)


def validate_tools(raw: dict) -> None:
    tools = raw.get("tools")
    if not isinstance(tools, list) or not tools:
        err("tools.json: missing non-empty 'tools' array")
        return
    names = set()
    for i, t in enumerate(tools):
        where = f"tools.json[{i}]"
        if not isinstance(t, dict):
            err(f"{where}: not an object")
            continue
        for field in ("name", "url", "section", "what"):
            if not t.get(field):
                err(f"{where}: missing {field}")
        u = t.get("url", "")
        if u and not u.startswith("https://"):
            err(f"{where}: url must be https, got {u!r}")
        n = t.get("name")
        if n:
            key = n.lower()
            if key in names:
                err(f"{where}: duplicate tool name {n!r}")
            names.add(key)


def validate_data() -> dict[str, dict]:
    slugs: dict[str, dict] = {}
    fonts_path = DATA / "fonts.json"
    if fonts_path.exists():
        try:
            slugs = validate_fonts(json.loads(fonts_path.read_text(encoding="utf-8")))
        except json.JSONDecodeError as e:
            err(f"fonts.json: invalid JSON: {e}")
    else:
        err("data/fonts.json missing")
    pairings_path = DATA / "pairings.json"
    if pairings_path.exists():
        try:
            validate_pairings(json.loads(pairings_path.read_text(encoding="utf-8")), slugs)
        except json.JSONDecodeError as e:
            err(f"pairings.json: invalid JSON: {e}")
    else:
        err("data/pairings.json missing")
    tools_path = DATA / "tools.json"
    if tools_path.exists():
        try:
            validate_tools(json.loads(tools_path.read_text(encoding="utf-8")))
        except json.JSONDecodeError as e:
            err(f"tools.json: invalid JSON: {e}")
    else:
        err("data/tools.json missing")
    return slugs


INTRO_RE = re.compile(r"^What this reference covers:")


def validate_doc(path: Path) -> None:
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8", errors="replace")
    check_ascii(path, text)
    lines = text.splitlines()
    is_generated = (
        path.parent.parent.name == "guides" and path.parent.name in GENERATED_DIRS
    )
    lo, hi = (GEN_MIN_LINES, GEN_MAX_LINES) if is_generated else (MIN_LINES, MAX_LINES)
    if not (lo <= len(lines) <= hi):
        err(f"{rel}: has {len(lines)} lines, expected {lo}-{hi}")
    h1s = [l for l in lines if re.match(r"^# [^#]", l)]
    if len(h1s) != 1:
        err(f"{rel}: expected exactly one H1, found {len(h1s)}")
    body = lines[lines.index(h1s[0]) + 1:] if h1s else lines
    first_nonempty = next((l for l in body if l.strip()), "")
    if not INTRO_RE.match(first_nonempty.strip()):
        err(f"{rel}: intro paragraph must start with 'What this reference covers:'")
    if "## Cross-references" not in text:
        err(f"{rel}: missing '## Cross-references' section")
        return
    tail = text.split("## Cross-references", 1)[1]
    links = re.findall(r"\]\(([^)]+)\)", tail)
    links = [l for l in links if not l.startswith(("http", "mailto:"))]
    if not (2 <= len(links) <= 5):
        err(f"{rel}: expected 2-5 relative cross-reference links, found {len(links)}")
    for link in links:
        target = (path.parent / link).resolve()
        if not target.exists():
            err(f"{rel}: broken cross-reference link {link}")
    last = next((l for l in reversed(lines) if l.strip()), "")
    if last != FOOTER_LINE:
        err(f"{rel}: final line must be exactly '{FOOTER_LINE}' (got '{last[:60]}')")


def validate_docs() -> None:
    count = 0
    for d in DOCS_DIRS:
        if not d.exists():
            continue
        for path in sorted(d.rglob("*.md")):
            if path.name == "README.md":
                continue
            validate_doc(path)
            count += 1
    print(f"Checked {count} guide/reference files.")


def validate_scripts() -> None:
    if not SCRIPTS.exists():
        return
    for path in sorted(SCRIPTS.glob("*.py")):
        try:
            py_compile.compile(str(path), doraise=True)
        except py_compile.PyCompileError as e:
            err(f"scripts/{path.name}: does not compile: {e}")


def main() -> int:
    args = set(sys.argv[1:])
    do_all = not ({"--data", "--docs"} & args)
    if do_all or "--data" in args:
        validate_data()
    if do_all or "--docs" in args:
        validate_docs()
    if do_all:
        validate_scripts()
    if errors:
        print(f"FAIL: {len(errors)} error(s)")
        for e in errors:
            print(f"  - {e}")
        if warnings:
            print(f"{len(warnings)} warning(s)")
        return 1
    print("PASS: Fontlore repository validation clean.")
    for w in warnings:
        print(f"  warning: {w}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
