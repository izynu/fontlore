# Marketplace License Models

What this reference covers: How the major font marketplaces and platforms structure their licensing: Fontspring's perpetual model, MyFonts and Monotype's marketplace and subscription approaches, Adobe Fonts' streaming subscription, and Fontstand's rental model. It maps each to the situations where it is the right buy.

The same family can be bought four different ways with four different sets of obligations. Choosing the model is as consequential as choosing the font.

## Fontspring: perpetual first

- Fontspring built its marketplace on perpetual licenses with no subscription or leasing pressure, and its license documents are unusually readable, with explicit scope tables.
- Licenses are one-time purchases covering defined scope: desktop user counts, web pageview tiers, app tiers, and combinations.
- Free trial fonts are available for most catalog entries, letting teams test before buying; trial terms still restrict production use.
- The model suits teams that want permanence and predictable cost: buy once, deploy, audit simply.
- Its Matcherator tool also makes Fontspring an identification destination, which shortens the path from "what is this font" to "license it".

## MyFonts and Monotype

- MyFonts is the largest font marketplace, selling perpetual desktop licenses and pageview-tiered webfont licenses across hundreds of foundries.
- Monotype, which owns MyFonts (and Fonts.com, Linotype, ITC), operates the Monotype Fonts subscription platform: broad library access for a recurring fee, aimed at enterprises.
- The marketplace path is best for specific identified fonts; the subscription path is best when many teams need many fonts with administrative support.
- Subscription fonts are usable while the subscription is active; budget continuity becomes a design-system dependency, and lapse means deactivation.
- MyFonts is also where WhatTheFont identifications land, which funnels a lot of purchases; verify that the identified font's foundry listing matches what the marketplace sells.

## Adobe Fonts

- Adobe Fonts bundles a large library into Creative Cloud subscriptions: fonts stream to desktop via the Creative Cloud app and serve on the web through Adobe-hosted kits.
- You never possess files in the traditional sense; activation is account-tied, and fonts deactivate when the subscription lapses.
- Web use goes through Adobe's hosting; self-hosting the font files is not permitted, which constrains some architectures.
- Contractors without seats cannot activate fonts, which complicates mixed teams.
- The model suits organizations already inside Creative Cloud that need breadth and zero procurement friction; it fits poorly for permanent, self-hosted, or contractor-heavy scenarios.
- Adobe Fonts includes both classic foundries and its own commissions; license scope is uniform inside the subscription and disappears outside it.
- Because activation is account-tied, shared accounts are a terms problem and a security problem at once; the fix is seats, not shared logins.

## Fontstand

- Fontstand rents desktop fonts month to month, with free trials of full fonts, across many independent foundries.
- Rental desktop rights mean files installed on rented terms: the font must be removed when the rental ends, which is an operational task, not a formality.
- Fontstand's trial month is full-quality and free, which makes it the honest way to test a retail font in real work before buying it anywhere.
- Rental fits pitches, campaigns, and experimental brand directions: full retail quality without a large upfront buy.
- Costs accumulate; a font rented forever costs more than a perpetual purchase, so convert to purchase when a font becomes permanent.
- Rental is desktop-focused; web and app needs route to the foundries' own licenses.
- The free trial month is genuinely useful for decision-making, but trial access still is not production licensing.

## Comparing the models

- Permanence: perpetual (Fontspring, MyFonts desktop, foundry-direct) wins; subscriptions and rentals require continued payment.
- Breadth: subscriptions win (Adobe Fonts, Monotype Fonts); nobody buys 500 perpetual families casually.
- Audit simplicity: perpetual with clear scope tables wins; streaming licenses complicate contractor and CI stories.
- Budget shape: perpetual is capex-like (lumpy, one-time), subscription and rental are opex-like (smooth, recurring); finance teams have opinions about this.
- Risk: subscription lapse deactivates fonts; perpetual lapses nothing; rental lapses when you stop paying.
- Contractor access: perpetual seats are purchased per person; subscriptions cover seats while active; rentals are per account. Mixed teams should price the contractor overhead before choosing.
- Evidence for audits: perpetual purchases produce entitlement documents; subscriptions produce account states; rentals produce account states. Only the first is proof that survives a vendor relationship ending.

## Workflow

1. Classify the need: one known family, broad team access, or temporary campaign.
2. For one known family: compare foundry-direct and marketplace perpetual prices for the full scope (desktop plus web plus app).
3. For broad access: model subscription cost against the 20 families the teams actually use.
4. For temporary work: rental or trial, with a written end date and a conversion plan.
5. Record model, vendor, entitlements, and renewal dates in the license inventory.
6. Put subscription and rental lapse dates in the same calendar as product launches, so nothing deactivates during a campaign.
7. Re-price annually: a subscription that exceeds the value of the faces actually used is a purchase decision waiting to happen.

## Common mistakes

- Buying a subscription for one font, or a perpetual license for a need that is really a 200-font enterprise problem.
- Building a brand on Adobe Fonts-activated fonts and discovering the deactivation risk when the org restructures.
- Renting a font for two years without noticing a perpetual license would have been cheaper after month eight.
- Assuming marketplace license summaries across vendors are equivalent; scope tables differ per foundry and per listing.
- Ignoring renewal and lapse dates until the design system breaks in production.
- Buying "desktop" from a marketplace and assuming webfonts are included; the licenses are separate products on every major platform.
- Treating Google Fonts as a vendor with support; it is a catalog with a license per family, and the support channel is the repository.
- Mixing models for one family across products (rental for the site, perpetual for the app) without recording which entitlement covers which surface.
- Choosing a subscription because the sticker looks smaller, then renewing for five years; total cost of ownership is the comparison, not the monthly price.
- Forgetting that marketplace discounts and bundles change the license tier you actually receive; the discounted scope is the scope.

## Decision rules

- Permanent brand or product foundation: perpetual, foundry-direct when possible.
- Need breadth across many teams with admin support: enterprise subscription, with exit planning.
- Short campaign or undecided direction: rental or trial with a scheduled decision point.
- Any model: the license document attached to the entitlement is the contract; summaries are marketing.
- When two models cost the same, prefer the one that leaves files and entitlement documents in your hands.
- Re-evaluate the model whenever usage outgrows it; the model that fit a three-person studio rarely fits a twenty-person team at the same price shape.
- For brand-critical families, prefer the model with the clearest continuity story: who holds the license if the vendor disappears?
- The vendor table is worth re-reading annually; marketplaces merge, subscriptions rebrand, and rental catalogs rotate, and your register should describe the vendor that exists today.
- When a stakeholder asks why the team does not just subscribe to everything, the answer is the audit column: entitlements you hold beat entitlements you rent whenever continuity matters.

## Quick reference: the model decision

1. Permanent and brand-critical: perpetual, foundry-direct, entitlement documents filed.
2. Broad team access to many faces: enterprise subscription with an exit clause, or open packages where licenses allow.
3. Temporary, exploratory, or campaign-bound: rental or trial with a written end date and a conversion decision date.
4. Anything open-licensed: self-host via packages or vendored files; no purchase at all.
5. Whatever the model: one register row per entitlement, with expiry, scope, and evidence.

The decision takes minutes when the use case is named honestly; it takes months when the use case is "we will figure it out later".

## Comparison table: the vendors

| Vendor | Model | Perpetual files | Web serving | Expiry risk | Best fit |
| --- | --- | --- | --- | --- | --- |
| Fontspring | Marketplace, perpetual EULAs | Yes, you keep files | Via perpetual web tiers | None | Permanent deployments with clean scope tables |
| MyFonts | Marketplace (Monotype) | Yes, per purchase | Pageview tiers | None | One-off identified families |
| Monotype Fonts | Enterprise subscription | No | Per terms | Subscription lapse | Large orgs needing breadth and admin |
| Adobe Fonts | Creative Cloud streaming | No (activation) | Adobe-hosted kits only | Subscription lapse | Orgs already inside Creative Cloud |
| Fontstand | Desktop rental | No | Via foundries | Rental end | Pitches, campaigns, trials of retail quality |
| Foundry direct | Per foundry | Usually yes | Per foundry | Per contract | Brand-critical families, custom terms |
| Google Fonts | Open catalog | Yes (open licenses) | Free CDN or self-host | None | Defaults, multilingual coverage |

The table is a decision aid, not a ranking; the same family can appear in several rows, and the row you choose determines your audit obligations more than the design does.

## Worked example: a twenty-person team's year

A twenty-person product team runs a brand on one commercial grotesk, dozens of open faces, and a rotating cast of campaign fonts. The year in licensing decisions:

- The brand grotesk is bought foundry-direct as a perpetual bundle: desktop seats for the design team, a webfont tier, and an app tier, all in one negotiation that included a written answer about the upcoming TV app.
- Open faces (Inter, JetBrains Mono, Literata) are vendored via Fontsource packages; no purchase, version-pinned, license files in the packages.
- Two campaign microsites in Q4 rent display fonts on Fontstand with a written end date; both convert to perpetual purchases when one campaign becomes evergreen, at the month-eight mark where rental cost crosses purchase price.
- A designer proposes an Adobe Fonts-activated family for a side project; it is rejected for production precisely because the deactivation risk and the no-self-hosting rule do not fit the pipeline, and the rejection is recorded.
- One MyFonts purchase covers a specialty face the foundry sells only through marketplaces; the entitlement PDF is filed with the same rigor as the direct purchase.
- The year ends with three kinds of records in the register: perpetual entitlements, package versions, and one rental with a decision date; the audit took forty minutes.
- The lesson the team wrote down: the model follows the use. Permanence bought perpetual, breadth used open packages, and temporariness rented.
- The register stores one row per entitlement regardless of model, with a "dies when" field that forced the team to answer the expiry question at purchase time.

## Field notes

- Marketplace license summaries are written per listing, and foundry EULAs differ underneath them; the document attached to the entitlement is the contract, the marketplace page is merchandising.
- Subscription platforms change terms over time; keep dated copies of the subscription terms your usage relies on.
- Rental models are excellent for decision-making and terrible as defaults; the failure mode is the campaign that quietly becomes infrastructure.
- When a foundry sells both direct and through marketplaces, direct purchases usually get faster license support, because you are the customer rather than the marketplace's customer.
- Free trials from marketplaces are for evaluation; the trial-to-purchase moment belongs in the project plan, not in someone's memory.
- Enterprise subscription negotiations should include an exit clause: what you may keep using, in what form, if the subscription ends.
- Watch marketplace bundles: a "full family" bundle may exclude variable builds or future weights, and upgrades are priced separately.

## Questions to ask before choosing a model

- How long will this font be in production use? A year of rental equals a perpetual license in price, with none of the permanence.
- Who needs to touch the font: a design team only, or engineering, contractors, and CI as well?
- Does the license include the web and app scopes the product will need within twelve months, or only the scope it needs today?
- What happens to our rights if the vendor, the marketplace, or the subscription changes?
- Can we get the entitlement document now, in a form our audit can file, instead of a receipt?
- For subscriptions: what exactly deactivates at lapse, and what is the grace period?

## Cross-references

- [Webfont embedding rights](webfont-embedding-rights.md)
- [Desktop and app licensing](desktop-and-app-licensing.md)
- [Trial and early access fonts](trial-and-early-access-fonts.md)
- [Commercial foundries and catalogs](../sourcing/commercial-foundries-and-catalogs.md)

Compiled 2025 as part of the Fontlore project.
