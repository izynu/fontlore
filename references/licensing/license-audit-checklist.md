# License Audit Checklist

What this reference covers: A printable, repeatable license audit: building the font inventory, collecting per-font license evidence, mapping usage scope, tracking renewals, and remediating findings. Run it quarterly or before launches, and keep the output where auditors and successors can find it.

A font audit is boring by design. Thirty minutes of checklist discipline prevents the expensive kind of excitement: cease-and-desist letters, emergency re-licensing, and launches blocked by legal.

## The audit cadence

- Quarterly for products with active development; before major launches regardless of schedule; immediately after team changes that affect license coverage (new contractor-heavy phase, new platform).
- Annually, run a deep audit that re-verifies license documents against sources, not just internal records.
- Trigger-based audits: any new market, new platform, new use context (a logo, an app, a device) starts a scoped audit.
- Assign a named owner; unowned audits silently stop happening.
- Timebox it: the checklist below runs in under an hour for a typical ten-font product.
- Keep the previous audit's output; deltas between audits are the fastest findings.
- Run the inventory sweep before reading any license; knowing what exists changes what questions you ask.
- For products with per-tenant fonts (white-label deployments), audit one tenant fully rather than all tenants shallowly.

## Step 1: Inventory

- List every font family in use, per product and per context: web (with domains), desktop (with team), app (with platforms), print templates, marketing, email, devices.
- Sources to sweep: CSS font stacks and asset folders, design files (a design tool plugin can extract used fonts), package manifests (npm font packages), and the brand guidelines.
- Include the forgotten corners: email templates, PDF generators, slide templates, error pages, and third-party embeds.
- Record versions and where files live; version drift between environments is an audit finding in itself.
- Keep the inventory in a governed location (design repo, design system docs), not in a spreadsheet on someone's laptop.
- Automate what repeats: a script that walks CSS font-family declarations and npm dependencies catches code-side fonts faster than memory does.
- Tag each entry with its owner and its last-verified date; unowned entries are how inventories rot.
- Record the file paths where each font lives, because version drift between environments is a finding in itself.

## Step 2: Per-font license evidence

For each family, record:

- License name, exact and unabbreviated: OFL-1.1, Apache-2.0, UFL-1.0, ITF-FFL-1.0, or the commercial license's document title.
- Where the license text lives: link to the file in the repo, the purchase email, or the stored PDF.
- Rights holder: foundry or designer, plus contact path.
- Version licensed and version deployed; mismatches are findings.
- Purchase reference for commercial fonts: invoice number, entitlement ID, order date.
- Reserved Font Name status for OFL fonts (matters before any fork).
- Date last verified and by whom.
- Subsets in production and the tooling that produced them; a subset without a recorded recipe is unrepeatable.
- For OFL fonts, the upstream repository or foundry page as the canonical source.
- For subscription fonts, the subscription terms version and the account that holds the entitlement.
- Notes field for written foundry answers; paste the answer, not a summary of it.

## Step 3: Scope mapping

- For each font, list every use context from the inventory and check it against the license grant: desktop seats covered? web domains and pageview tiers covered? app platforms covered? server rendering covered? ePub covered?
- Flag every context that the license does not explicitly cover; "probably fine" is a finding, not a pass.
- Check subscription coverage dates (Adobe Fonts seats, Monotype Fonts terms) against the audit date.
- For client or multi-entity situations, verify which entity holds which rights; agency licenses rarely cover client use.
- Output: a scope table per font, green for covered, amber for undocumented, red for out of scope.
- Attach evidence links in the scope table: the license document, the purchase email, the monitoring dashboard screenshot.
- Check tier headroom arithmetic on the spot: current traffic against licensed tier against the alert threshold.
- For multi-entity situations, name the entity per row; "the company" is not a licensee.

## Step 4: Renewals and expiration

- Subscription renewal dates and their failure modes (fonts deactivating, web serving stopping).
- Pageview tier headroom: current traffic versus licensed tier, with alert thresholds.
- Rental end dates (Fontstand-style) and conversion decisions pending.
- Trial and evaluation fonts still present anywhere in production: automatic findings.
- Contract end dates for enterprise foundry agreements, with renewal negotiation lead time noted.
- Trial-font sweep results: any hit is a finding regardless of context.
- Subscription seat counts against the current org chart; seats drift upward after every hiring wave.

## Step 5: Remediation paths

- Out of scope but liked: buy the upgrade before the next release, not after an incident.
- Unverifiable provenance (aggregator fonts): replace with a documented open alternative; the substitution list lives in the sourcing guides.
- Subscription dependencies in critical paths: migrate to perpetual or OFL alternatives where continuity matters.
- Scope mismatches in client situations: reopen the handoff memo and rebuy at the right entity.
- Every finding gets an owner and a date; unowned findings are how audits fail.
- Findings that need money go to procurement with a deadline, not to a backlog; licensing debt compounds like any other debt.
- Findings that need design work (a font replacement) get a scoped ticket with the substitution list attached.
- Close the loop: the next audit verifies that each prior finding is actually remediated, not merely assigned.

## The printable checklist

1. Inventory complete? Every context listed, including the forgotten corners.
2. License named exactly, per font, with document location?
3. Rights holder and purchase reference recorded for commercial fonts?
4. Scope table built and every context checked against grants?
5. Renewals, tiers, and expiration dates logged with alerts?
6. Findings listed with owners and dates?
7. Audit output stored in the governed location and shared with the team?
8. Next audit scheduled?
9. Trial fonts: zero hits?
10. Seat counts and tier headroom: verified against live data?
11. Previous audit's findings: remediated and closed?

## The register, as a table

The audit's durable output is a register. One row per font entitlement, with these columns:

| Field | What goes in it | Why it matters |
| --- | --- | --- |
| Family and version | Exact name, version string | Answers "which Inter is this" |
| License | Exact identifier (OFL-1.1, Apache-2.0, document title) | The audit's join key |
| Rights holder | Foundry or author, with contact path | Renegotiation and verification |
| Scope | Seats, domains, tiers, platforms, contexts | The grant's actual shape |
| Evidence | Document location or entitlement ID | Proof, not memory |
| Renewal or expiry | Date, or "perpetual" | The failure calendar |
| Owner | One name | Unowned rows are findings |
| Last verified | Date and checker | Staleness detector |
| Notes | Written foundry answers, constraints | The reasoning that audits ask for |

A register with all nine columns answers almost every licensing question without a meeting; a register missing scope and evidence answers none of them.

## Worked example: a ten-font product audit

A mid-size product runs four open families, three commercial desktop licenses, two webfont entitlements, and one subscription face. The audit in practice:

- Inventory sweep (ten minutes): CSS and npm sweeps found the four open families plus one forgotten font in a PDF template; the design-tool plugin found the three commercial families; total eleven rows, one more than expected.
- Evidence check (fifteen minutes): the open families had license files in the repo; one commercial entitlement PDF was missing, re-downloaded from the vendor portal in two minutes; the subscription face had an account screenshot for evidence.
- Scope mapping (fifteen minutes): all green except the forgotten template font, which had no license at all; it was an aggregator download predating the register.
- Remediation (ten minutes): the template font was replaced with a documented OFL alternative, and the incident was logged with a date and an owner.
- The audit output: one red finding remediated on the spot, two ambers (a pageview tier at 74 percent, a rental approaching its decision date) assigned owners, and a dated clean record for everything else.
- Total time: fifty minutes, of which the forgotten font was twenty.

## Field notes

- The audit that finds nothing is not wasted; the dated clean record is what clients, acquirers, and enterprise procurement want to see.
- Automate the sweep, human-review the scopes; tools are good at finding fonts and bad at reading licenses.
- Keep audit outputs with the register, not in chat; the delta between audits is the most informative document you will produce.
- When an audit finding repeats across two audits, it is a process gap, not a font problem; fix the intake, not just the font.
- Small teams can run this checklist quarterly in an hour; the discipline is the same at any size, only the row count changes.
- Before a launch or a funding event, run the audit early enough to remediate; a clean record the week before diligence is worth exactly nothing.

## Common mistakes

- Auditing only the website and forgetting the PDF generator, email templates, and slide decks.
- Recording "free" as the license name; audits need exact license identities.
- Treating the inventory as complete when it came from one source; cross-check design files against code.
- Skipping the re-verification of license documents; internal records drift from reality.
- Letting findings linger without owners, converting the audit into a formality.
- Running the audit as a solo hero exercise; two reviewers catch what one misses, and the second set of eyes is cheap.
- Storing the register in a format nobody can edit casually; an unmaintained register is worse than none, because it looks like evidence.
- Treating ambers as fine; ambers are undocumented scope, which is the audit's middle danger zone.
- Forgetting to version the register; a register without dates cannot prove what you knew and when.

## Decision rules

- Any red finding blocks the next release until remediated; ambers get owners and dates.
- If the inventory cannot be built in an hour, the font governance itself needs fixing; audit the governance, not just the fonts.
- When two records disagree, the license document at the source wins; update the internal record.
- An audit that finds nothing still produces value: the dated, clean record is what auditors and clients want to see.
- Audit before procurement asks you to; an internal record outranks a scramble.
- When the register grows past a page, move from checklist to tooling; the discipline stays, the storage upgrades.
- Scope questions that cannot be answered from documents become written foundry questions; the audit generates the email, the owner sends it.

## Cross-references

- [Free font risks](free-font-risks.md)
- [Client handoff licensing](client-handoff-licensing.md)
- [Open-source due diligence](open-source-due-diligence.md)
- [Documenting identification results](../identification/documenting-identification-results.md)

Compiled 2025 as part of the Fontlore project.
