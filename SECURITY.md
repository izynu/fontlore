# Security Policy

## What counts as a security issue here

Fontlore contains no runnable application surface: the code is stdlib-only Python you are expected to read before running. The attack surface is therefore the data and the documents, which AI agents are expected to load and act on. Report privately if you find:

- Wrong or falsified license information: a font marked OFL-1.1 that is proprietary, a license URL pointing somewhere other than the rights holder, or a license field edited to bypass the accepted set.
- Pirated or infringing links: any source, specimen, or tool URL that distributes cracked, ripped, or otherwise unlicensed font files.
- Malicious URLs in the data: links in fonts.json, pairings.json, or tools.json that lead to malware, phishing, drive-by downloads, or lookalike domains impersonating foundries or catalogs.
- Injection through data: crafted strings in the JSON that could execute in a consumer's pipeline, or content in generated guides intended to manipulate AI agents (prompt injection, fake instructions, hidden directives).
- Validator bypasses: a way to make scripts/validate.py pass on data or documents that violate the enforced rules, including unicode tricks that survive the ASCII check.
- Supply chain issues in the GitHub workflows: script injection through untrusted input, unpinned third-party actions, or credential exposure.

## How to report

Use GitHub's private vulnerability reporting on this repository (Security tab, "Report a vulnerability"). This opens a private advisory thread between you and the maintainers. Please include:

- The file and record affected (slug, field, exact value).
- Why it is a problem and, where relevant, what a consumer or agent would be misled into doing.
- Evidence: the correct license text or the legitimate URL.

Do not open a public issue for anything in the list above; a public issue about a malicious URL or a falsified license warns the wrong people and not the right ones.

## What is not a security issue

- Factual typography disagreements or data corrections: use the data-correction issue form.
- Broken links: use the data-correction issue form or a pull request.
- Bugs in decide.py or validate.py that produce wrong rankings without falsified data: use the bug report form.

## Maintainer response procedure

On triage, maintainers remove or correct the offending record first and push the fix to main before any public discussion, so downstream consumers of the default branch get the safe data immediately. CI re-runs the validator on the fix. If the issue affects published releases or the site, the correction is followed by a release note naming the records that changed. Advisories are published through GitHub with the reporter credited, and the corrected values are re-verified at their source URLs before the advisory closes.

## Response expectations

- First response within 5 days of the private report.
- Triage decision (accepted, needs more info, declined) within 10 days.
- For accepted issues: the offending record or URL is removed or corrected within 7 days of triage, before any wider fix or disclosure; the advisory is published once the data is safe.
- We credit reporters in the advisory by default and keep them anonymous on request.

## Safe harbor

Good-faith research against this repository's published code and data, reported privately as above, is welcome and will not be met with legal action from the maintainers.
