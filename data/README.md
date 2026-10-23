# Data layer

What this reference covers: the three machine-readable data files at the core of Fontlore, their schemas, and the rules that keep them verifiable.

| File | Contents | Count |
| --- | --- | --- |
| `fonts.json` | Font records: identity, classification, scripts, license, source URLs | 165 |
| `pairings.json` | Curated heading-plus-body pairings with context and rationale | 66 |
| `tools.json` | Tools: catalogs, APIs, inspectors, identification services | 71 |

Rules enforced by scripts/validate.py: slugs are lowercase-kebab and unique; every font record carries a https source URL; pairings reference existing font slugs with no self-pairing and no direction-agnostic duplicates; licenses come from the accepted set (OFL-1.1, Apache-2.0, UFL-1.0, ITF-FFL-1.0, MIT, Custom-OFL-based); unverifiable values are null, never guessed.

## Cross-references

- [Fonts JSON](fonts.json)
- [Pairings JSON](pairings.json)
- [Tools JSON](tools.json)

Compiled 2025 as part of the Fontlore project.
