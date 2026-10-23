#!/usr/bin/env python3
"""Fontlore decision engine: rank fonts for a project from the data layer.

Hard-filters data/fonts.json by required script and license, scores the
survivors against the rubric documented in MASTER-SKILL.md, prints a ranked
shortlist with per-font reasons, and lists curated pairings from
data/pairings.json that touch the shortlist. Reads only the JSON files next
to it; no network, no dependencies outside the standard library.

Scoring (weights sum to 100):
  30  category fit      primary role categories for the project type score
                        full, secondary roles 0.6, everything else 0.2
  25  tone match        classifications preferred for the tone score full,
                        adjacent classifications 0.5, the rest 0.1
  15  variable build    variable fonts score full
  15  script coverage   number of script ranges in the scripts field,
                        capped at full marks from 6 ranges up
  15  open license      licenses in the open set score full

Usage:
  python3 scripts/decide.py --project dashboard --script latin --tone neutral
  python3 scripts/decide.py --project dashboard --script devanagari --open-only --top 8
  python3 scripts/decide.py --project webapp --script latin --tone technical --json

Exit codes: 0 on success (including an empty result set), 2 on bad
arguments or unreadable data files.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / "data"

OPEN_LICENSES = {"OFL-1.1", "Apache-2.0", "UFL-1.0", "ITF-FFL-1.0", "MIT"}

PROJECTS = ("webapp", "dashboard", "marketing", "editorial", "ecommerce", "brand", "docs")
REQUIRED_SCRIPTS = (
    "latin", "devanagari", "arabic", "hebrew", "thai",
    "japanese", "korean", "chinese-simplified",
)
TONES = ("neutral", "friendly", "editorial", "technical", "playful")

# Primary role categories score 1.0, secondary 0.6, the rest 0.2.
CATEGORY_FIT = {
    "webapp": {"primary": {"sans-serif"}, "secondary": {"serif", "monospace"}},
    "dashboard": {"primary": {"sans-serif", "monospace"}, "secondary": {"serif"}},
    "marketing": {"primary": {"sans-serif", "display"}, "secondary": {"serif"}},
    "editorial": {"primary": {"serif"}, "secondary": {"sans-serif", "display"}},
    "ecommerce": {"primary": {"sans-serif", "display"}, "secondary": {"serif"}},
    "brand": {"primary": {"display"}, "secondary": {"sans-serif", "serif", "handwriting"}},
    "docs": {"primary": {"sans-serif", "monospace"}, "secondary": {"serif"}},
}

# Classifications that read as the requested tone score 1.0, adjacent ones 0.5.
TONE_MATCH = {
    "neutral": {
        "full": {"grotesque", "humanist", "geometric"},
        "adjacent": {"mono", "condensed", "wide", "squared", "gothic", "techno",
                     "slab", "mincho", "naskh", "kufi", "inscriptional"},
    },
    "friendly": {
        "full": {"geometric", "humanist", "rounded"},
        "adjacent": {"casual", "script", "marker", "brush", "slab", "gothic"},
    },
    "editorial": {
        "full": {"old-style", "transitional", "didone", "mincho"},
        "adjacent": {"slab", "naskh", "inscriptional", "script", "humanist"},
    },
    "technical": {
        "full": {"mono", "grotesque", "techno", "squared"},
        "adjacent": {"condensed", "wide", "geometric", "gothic"},
    },
    "playful": {
        "full": {"rounded", "casual", "script", "marker", "brush"},
        "adjacent": {"geometric", "techno", "wide", "gothic"},
    },
}

WEIGHT_CATEGORY = 30
WEIGHT_TONE = 25
WEIGHT_VARIABLE = 15
WEIGHT_COVERAGE = 15
WEIGHT_OPEN = 15

COVERAGE_CAP_SCRIPTS = 6  # this many script ranges already earn full coverage marks


def load_data():
    """Load fonts.json and pairings.json from the data directory beside the script."""
    fonts_path = DATA_DIR / "fonts.json"
    pairings_path = DATA_DIR / "pairings.json"
    try:
        fonts_raw = json.loads(fonts_path.read_text(encoding="utf-8"))
    except OSError as e:
        print(f"error: cannot read {fonts_path}: {e}", file=sys.stderr)
        raise SystemExit(2)
    except json.JSONDecodeError as e:
        print(f"error: {fonts_path} is not valid JSON: {e}", file=sys.stderr)
        raise SystemExit(2)
    try:
        pairings_raw = json.loads(pairings_path.read_text(encoding="utf-8"))
    except OSError as e:
        print(f"error: cannot read {pairings_path}: {e}", file=sys.stderr)
        raise SystemExit(2)
    except json.JSONDecodeError as e:
        print(f"error: {pairings_path} is not valid JSON: {e}", file=sys.stderr)
        raise SystemExit(2)
    return fonts_raw.get("fonts", []), pairings_raw.get("pairings", [])


def category_component(project: str, category: str) -> float:
    fit = CATEGORY_FIT[project]
    if category in fit["primary"]:
        return 1.0
    if category in fit["secondary"]:
        return 0.6
    return 0.2


def category_reason(project: str, category: str) -> str:
    fit = CATEGORY_FIT[project]
    if category in fit["primary"]:
        return f"category fit: {category} is a primary role for {project}"
    if category in fit["secondary"]:
        return f"category fit: {category} is a secondary role for {project}"
    return f"category fit: {category} is off-brief for {project}"


def tone_component(tone: str, classification: str) -> float:
    match = TONE_MATCH[tone]
    if classification in match["full"]:
        return 1.0
    if classification in match["adjacent"]:
        return 0.5
    return 0.1


def tone_reason(tone: str, classification: str) -> str:
    match = TONE_MATCH[tone]
    if classification in match["full"]:
        return f"tone match: {classification} reads {tone}"
    if classification in match["adjacent"]:
        return f"tone partial: {classification} leans away from {tone}"
    return f"tone mismatch: {classification} fights {tone}"


def score_font(font: dict, project: str, tone: str) -> tuple[int, list[str]]:
    """Score one font against the rubric. Returns (score 0-100, reasons)."""
    reasons = []

    category = font.get("category", "")
    c = category_component(project, category)
    reasons.append(category_reason(project, category))

    classification = font.get("classification", "")
    t = tone_component(tone, classification)
    reasons.append(tone_reason(tone, classification))

    v = 1.0 if font.get("variable") else 0.0
    if v:
        axes = font.get("axes") or []
        axes_text = ", ".join(axes) if axes else "axes unlisted"
        reasons.append(f"variable build: {axes_text}")

    scripts = font.get("scripts") or []
    coverage = min(len(scripts) / COVERAGE_CAP_SCRIPTS, 1.0)
    reasons.append(f"script coverage: {len(scripts)} script ranges listed")

    license_name = font.get("license", "")
    o = 1.0 if license_name in OPEN_LICENSES else 0.0
    if o:
        reasons.append(f"open license: {license_name}")
    else:
        reasons.append(f"license caution: {license_name} needs review before use")

    score = round(
        c * WEIGHT_CATEGORY + t * WEIGHT_TONE + v * WEIGHT_VARIABLE
        + coverage * WEIGHT_COVERAGE + o * WEIGHT_OPEN
    )
    return score, reasons


def hard_filter(fonts: list[dict], script: str, open_only: bool) -> tuple[list[dict], dict]:
    """Apply the non-negotiable filters. Returns (survivors, rejection counts)."""
    survivors = []
    stats = {"wrong script": 0, "license": 0}
    for font in fonts:
        if script not in (font.get("scripts") or []):
            stats["wrong script"] += 1
            continue
        if open_only and font.get("license") not in OPEN_LICENSES:
            # Custom-OFL-based and any future restricted licenses need a manual read.
            stats["license"] += 1
            continue
        survivors.append(font)
    return survivors, stats


def suggested_pairings(pairings: list[dict], fonts_by_slug: dict, top_slugs: set[str],
                       limit: int = 3) -> list[str]:
    """Curated pairings whose heading or body is in the ranked shortlist."""
    found = []
    for p in pairings:
        h, b = p.get("heading"), p.get("body")
        if h in top_slugs or b in top_slugs:
            hf = fonts_by_slug.get(h, {}).get("family", h)
            bf = fonts_by_slug.get(b, {}).get("family", b)
            found.append(f"{hf} + {bf} - {p.get('context', 'unspecified context')}")
        if len(found) >= limit:
            break
    return found


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="decide.py",
        description="Rank Fontlore fonts for a project brief (see MASTER-SKILL.md).",
    )
    parser.add_argument("--project", required=True, choices=PROJECTS,
                        help="project type: " + ", ".join(PROJECTS))
    parser.add_argument("--script", required=True, choices=REQUIRED_SCRIPTS,
                        help="script that must be covered: " + ", ".join(REQUIRED_SCRIPTS))
    parser.add_argument("--tone", default="neutral", choices=TONES,
                        help="target tone (default: neutral)")
    parser.add_argument("--open-only", action=argparse.BooleanOptionalAction, default=True,
                        help="keep only open licenses: OFL-1.1, Apache-2.0, UFL-1.0, "
                             "ITF-FFL-1.0, MIT (default: on; disable with --no-open-only)")
    parser.add_argument("--top", type=int, default=5, metavar="N",
                        help="length of the ranked shortlist (default: 5)")
    parser.add_argument("--json", action="store_true",
                        help="machine-readable output instead of a table")
    args = parser.parse_args(argv)

    if args.top < 1:
        parser.error("--top must be a positive integer")

    fonts, pairings = load_data()
    survivors, stats = hard_filter(fonts, args.script, args.open_only)

    scored = []
    for font in survivors:
        score, reasons = score_font(font, args.project, args.tone)
        scored.append((score, font, reasons))
    scored.sort(key=lambda item: (-item[0], item[1].get("family", "")))
    ranked = scored[: args.top]

    fonts_by_slug = {f.get("slug"): f for f in fonts}
    query = {
        "project": args.project,
        "script": args.script,
        "tone": args.tone,
        "open_only": args.open_only,
        "top": args.top,
    }

    if args.json:
        print(json.dumps({
            "query": query,
            "results": [
                {"slug": f.get("slug"), "family": f.get("family"), "score": s, "reasons": reasons}
                for s, f, reasons in ranked
            ],
        }, indent=2))
        return 0

    print(f"Fontlore decision engine - project: {args.project} | script: {args.script} "
          f"| tone: {args.tone} | open-only: {str(args.open_only).lower()} | shortlist: {args.top}")
    note = f"Hard filter: {len(survivors)} of {len(fonts)} fonts cover the {args.script} script."
    if stats["license"]:
        note += f" {stats['license']} removed by the open-license filter."
    print(note)
    if not ranked:
        print("No fonts matched the hard filters. Widen the script, license, or data layer.")
        return 0

    print()
    header = f"{'rank':<5}{'family':<26}{'score':<6}{'class':<15}{'license':<13}reasons"
    print(header)
    print("-" * len(header))
    for i, (score, font, reasons) in enumerate(ranked, start=1):
        line = (
            f"{i:<5}{font.get('family', '?'):<26}{score:<6}"
            f"{font.get('classification', '?'):<15}{font.get('license', '?'):<13}"
            + "; ".join(reasons)
        )
        print(line)

    print()
    print("Suggested pairings:")
    top_slugs = {f.get("slug") for _, f, _ in ranked}
    pairings_found = suggested_pairings(pairings, fonts_by_slug, top_slugs)
    if pairings_found:
        for entry in pairings_found:
            print(f"  - {entry}")
    else:
        print("  none of the 66 curated pairings involve this shortlist; "
              "pair manually per MASTER-SKILL.md Stage 3.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        # Downstream closed the pipe (for example piping into head); exit quietly.
        import os
        os._exit(0)
