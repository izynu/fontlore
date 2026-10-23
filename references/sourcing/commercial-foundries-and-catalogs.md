# Commercial Foundries and Catalogs

What this reference covers: The commercial side of font sourcing: the big catalogs (Adobe Fonts, MyFonts, Monotype, Fontspring, Fontstand) and a working map of notable independent foundries. It covers how each sales model differs, which foundries specialize in what, and how to choose a buying channel.

Commercial fonts buy you polish, support, and licensing clarity that free sources cannot always provide. The complexity is the business models: perpetual, subscription, streaming, and rental all behave differently in an audit, a budget cycle, and a client handoff.

## The big catalogs

- Adobe Fonts comes with Creative Cloud subscriptions: thousands of families stream to desktop via the Creative Cloud app and serve on the web through Adobe's hosted kits. You never own files; families deactivate if the subscription lapses, and self-hosting webfonts is not permitted.
- MyFonts is the largest marketplace, with deep inventory from hundreds of foundries, pageview-tiered webfont licensing, and the WhatTheFont identification tool. It is the default place to buy an identified font.
- Monotype operates a subscription platform (Monotype Fonts) and owns MyFonts, Fonts.com, and the Linotype and ITC libraries. Enterprise typographic needs usually route here eventually.
- Fontspring sells perpetual licenses with explicit, readable scope tables and no subscription pressure. Its Matcherator tool also makes it an identification destination.
- Fontstand rents desktop fonts monthly, with free trials of full fonts. It suits short-lived projects and lets teams use retail fonts without a large upfront purchase.

## Notable independent foundries

- Klim Type Foundry (New Zealand, Kris Sowersby): Untitled Sans, Tiempos, Calibre, Founders Grotesk, Domaine. Editorial and product work with meticulous text fitness.
- Grilli Type (Switzerland): GT America, GT Walsheim, GT Sectra, GT Flexa, GT Alpina. Contemporary grotesques and hybrids with strong variable builds.
- Commercial Type (New York, Paul Barnes and Christian Schwartz): Graphik, Publico, Austin, Dala Floda. Editorial heavyweights with deep style ranges.
- Displaay: Roobert and related contemporary sans designs popular in product and tech branding.
- OH no Type Company (James Edmondson): Degular, Swear, Ohno Blazeface. Personality-forward display and text work with variable builds.
- Sharp Type (New York): a respected independent publishing house for several designers' work; a reliable source for editorial voices.
- Dinamo (Basel and Berlin): ABC Diatype, ABC Favorit, ABC Whyte and a large ABC-series catalog with flexible licensing and custom variants.
- This list is a starting map, not an endorsement of completeness; dozens of excellent small foundries exist, and specialized briefs usually find them faster than generalist catalogs.

## How the models differ in practice

- Perpetual licenses (Fontspring, most foundry direct sales, MyFonts desktop): pay once, use within the documented scope forever. Simplest to audit; renewals only if scope grows.
- Subscription libraries (Monotype Fonts): broad access for a recurring fee; fonts are usable while the subscription is active, so budget continuity becomes a design-system dependency.
- Streaming (Adobe Fonts): no files in hand, activation tied to accounts, which complicates CI, contractors, and offboarding.
- Rental (Fontstand): low commitment, monthly cost; good for pitches and temporary brand systems, poor for permanent product foundations.
- Free open-source (elsewhere in this category): zero license cost, real integration and governance costs. Price comparisons should include total cost of governance, not just invoice totals.

## Choosing a buying channel

- Identified a font from a specimen or a Fonts In Use entry? MyFonts or the foundry's own site is usually the shortest path; foundry-direct often prices large families better.
- Need many fonts for a big org? Model the subscription math against perpetual purchases; subscriptions win on breadth, perpetuals win on permanence.
- Contractor-heavy teams: prefer perpetual or foundry-direct with clear installer distribution rules; account-tied streaming causes offboarding friction.
- Client work: buy only what the deliverable needs and pass the licensing requirement to the client in writing (see client handoff guidance).

## Workflow

1. Confirm the candidate exists commercially: check the foundry site first, then marketplaces.
2. Read the license scope table, not the marketing page: users, machines, web pageviews, app, logo, embedding.
3. Price the full needed scope (design team desktop + web + any app), not just the desktop tier.
4. Record the purchase: vendor, license type, invoice, scope, version, date. Store license documents with the font files.
5. Calendar review points: pageview tier thresholds, subscription renewals, and any project phases that change scope.

## Common mistakes

- Assuming an Adobe Fonts subscription covers a client's use or a deliverable handoff; it covers the subscriber's use under Adobe's terms.
- Buying a desktop license and later discovering the project needs web or app rights, forcing an upgrade mid-project.
- Treating marketplace license summaries as the license; the license document attached to the purchase is the contract.
- Forgetting that streaming fonts disappear for contractors without seats, then blaming the design for inconsistent rendering.
- Budgeting only desktop costs on projects that are, in reality, web products.

## Decision rules

- Permanent product or brand foundation: perpetual from foundry-direct or Fontspring.
- Short campaign or uncertain brand direction: Fontstand rental or Adobe Fonts until direction settles.
- Enterprise breadth with many teams: evaluate Monotype Fonts against a curated perpetual set; breadth rarely justifies itself for small teams.
- Any candidate that exists both free (OFL) and commercial: decide with governance, not habit, and document the decision either way.

## Comparison table: catalogs at a glance

| Catalog | Model | Files in hand | Webfonts | Best fit |
| --- | --- | --- | --- | --- |
| Adobe Fonts | Included with Creative Cloud | Desktop streaming only | Adobe-hosted kits, no self-hosting | Teams already inside the Creative Cloud gravity well |
| MyFonts | Marketplace, perpetual purchases | Yes | Pageview-tiered licenses | Buying an identified font from hundreds of foundries |
| Monotype Fonts | Subscription platform | Per terms | Included per subscription | Enterprise breadth across many teams |
| Fontspring | Perpetual, direct | Yes | Perpetual with explicit scope | Permanent foundations with readable license tables |
| Fontstand | Monthly rental | While renting | Per rental terms | Pitches, campaigns, undecided brand directions |

The rows that matter for audits are "Files in hand" and the scope table behind the purchase; everything else is procurement preference.

## Questions to ask before buying

- Does the license scope cover every surface this project will touch: desktop seats, web pageviews, app embedding, logo use, broadcast or video?
- Is the license perpetual for the purchased version, and are minor updates included or sold separately?
- How are contractors handled: named seats, shared workstation rules, or a written exception?
- What happens to web serving at subscription lapse (for streaming and subscription models), and what is the fallback?
- Who signs, whose name is on the license, and where does the invoice and license document get stored?
- Can the license be transferred at client handoff or company acquisition, and what does that cost?

## Worked example: pricing a three-surface launch

Scenario: a product launch needs a retail family for marketing site, web app, and a native mobile app.

1. List the surfaces and the rights each needs: web (marketing pageviews plus app traffic), app embedding (iOS and Android builds), and desktop seats for the design team and the engineers who touch brand assets.
2. Ask foundry-direct first; large families are usually priced better at the source, and the foundry can confirm app-embedding clauses that marketplaces summarize loosely.
3. Price the same scope on a marketplace for comparison; identical licenses, different packaging and support story.
4. Model the ten-year cost against a rental path: perpetual wins on permanence, rental wins if the brand direction is genuinely unsettled.
5. Record the decision with the scope table, the invoice, and the version purchased; calendar the review points (pageview tier thresholds, renewal dates).
6. Pass the license requirements to any agency or contractor in writing before they touch the files.

The purchase is rarely the hard part; the scope math and the paper trail are. Teams that skip step 1 buy the wrong tier and discover it at the worst moment.

## Field notes

- Adobe Fonts simplifies access and complicates governance: CI servers, contractors without seats, and offboarding are the recurring friction points, and self-hosting webfonts is not permitted.
- MyFonts remains the shortest path from identification to purchase, since identification tools and the store live in the same place; its webfont tiers are pageview-based, so traffic growth is a licensing event.
- Fontspring's readable scope tables are a good template for your own license register: users, machines, web pageviews, app installs, logo, embedding, each on one line.
- Fontstand trials put full retail fonts in front of stakeholders cheaply, which is exactly the right tool before a five-figure brand commitment.
- Monotype's libraries (Linotype, ITC) are the default answer when a brief names a classic design; check whether the needed styles are in the subscription tier you are actually buying.

## Signals to distrust

- Marketplace license summaries and marketing copy; the license document attached to the purchase is the contract.
- "Unlimited" claims without the scope table that defines users, domains, and surfaces.
- Quotes that exclude app or video rights by default; sales flows optimize for the desktop-plus-web bundle that most buyers expect, not the scope you actually have.
- Renewal reminders that arrive as invoices; if nobody can name what the subscription covers today, that is a governance failure, not a procurement one.

## Signals to trust

- Scope tables that enumerate users, machines, pageviews, app installs, and logo rights as separate rows; foundries that spell these out tend to honor them.
- Foundry-direct answers in writing about unusual uses; independent foundries respond fast and their replies are audit evidence.
- Invoices and license documents that name the same licensee and version as your manifest records.

## Worked example: an agency with a freelance bench

Scenario: an agency buys a retail serif for a client brand; three freelancers and a print vendor will touch the files.

1. License in the client's name from the start; the brand outlives the agency relationship and the license should too.
2. Count seats honestly: staff designers plus every freelancer who installs the font. Seat-based licenses do not care who signs the paycheck.
3. Check the contractor clause; some licenses permit named contractors under the client's account, many require separate seats. Get the answer in writing before the first file transfer.
4. Send the print vendor a PDF, never live files with fonts; embedding in a print-ready PDF is usually covered, handing over the font file itself is not.
5. Deliver a handoff pack at project end: files where the license permits, license documents, invoice copy, and the scope table, so the client's next agency inherits evidence instead of risk.

The pattern: decide who owns the license before deciding who uses the font. Reversing those two decisions is how agencies end up personally liable for a client's wordmark.

## Tool notes

- Foundry sites usually carry the fullest version histories and the clearest scope tables; use marketplaces for comparison shopping, foundries for the actual contract.
- Keep a license register row per purchase: family, version, licensee, scope, invoice link, renewal or review date. The register template in the governance reference matches this file's needs.
- Marketplace wishlists are a reasonable research tool, but a wishlist entry is not a license decision; nothing in a cart has been read yet.
- For subscription platforms, screenshot the family list available under your tier on the day you standardize; catalogs add and remove families, and your fallback plan depends on what existed when you chose.

## Cross-references

- [Open and independent foundries](open-and-independent-foundries.md)
- [Evaluating catalog metadata](evaluating-catalog-metadata.md)
- [Marketplace license models](../licensing/marketplace-license-models.md)
- [Client handoff licensing](../licensing/client-handoff-licensing.md)

Compiled 2025 as part of the Fontlore project.
