# Desktop and App Licensing

What this reference covers: How desktop licenses differ from app embedding licenses, what iOS and Android bundling requires, and how ePub and game/console cases change the picture. Desktop rights do not imply app rights; this guide draws the line precisely.

The desktop-app boundary is the most common place teams discover their license is too small. Designers install fonts freely, an app ships with the same files inside, and the audit finds an unlicensed embedding.

The pattern generalizes: every font quietly collects use contexts over time, and each context has its own license category. The cure is a one-page map of contexts to grants, reviewed whenever a new surface ships.

## Desktop licenses

- A desktop license grants installation on machines and use in design tools to create artwork: mockups, print files, PDFs, images rendered from the design.
- Scope dimensions: number of users, number of machines (often more permissive than users), and sometimes company size or revenue tiers.
- Desktop rights cover outputs where the font is rendered into a static form (PDF, PNG, print). They do not cover shipping the font file itself to end users.
- Team distribution rules vary: some licenses let one designer install on multiple machines; enterprise licenses cover whole organizations. Read the user and machine clauses, not the marketing.
- Contractors count as users in most licenses; plan their access explicitly instead of "just sharing the files".

## What desktop does NOT cover

- Bundling the font file into any distributed software: apps, games, firmware, kiosks, themes for other products.
- Serving the font to browsers: that is the webfont license's job.
- Server-side rendering: PDF/image generation on servers is server use, usually a separate grant.
- These three boundaries (bundled, served, rendered-server-side) are the whole map; most confusion is one of them mislabeled.
- A quick self-test for any new feature: "does the user's device end up with the font file?" If yes, embedding. "Does the font render only inside our own process?" If yes, desktop or server. "Does the visitor's browser fetch it?" If yes, webfont.
- Writing the three answers into the feature's spec makes licensing review a lookup instead of a meeting.

## App embedding

- Embedding means the font file ships inside the application package (IPA, APK, desktop installer, game build) and renders text at runtime.
- Open fonts (OFL, Apache) permit this freely with license retention; keep the license file in the bundle's legal notices.
- Commercial fonts require an app or extended license: foundries price app embedding separately, often by app tier (free app vs paid app vs enterprise internal app).
- iOS specifics: fonts bundled in the app binary or shipped via custom font APIs count as embedding; platform system fonts (San Francisco) are covered by the OS and need no license.
- Android specifics: bundled TTF/OTF in APK or downloaded font resources both count; downloadable fonts through provider mechanisms still need the underlying license to permit distribution.
- Count the app's distribution model: free, paid, or internal-only enterprise distribution all price differently; internal tools sometimes qualify for lighter terms but only when the license says so.

## Games, consoles, and devices

- Games embed fonts like apps; console platforms add certification requirements that make clean font licensing part of submission paperwork.
- Digital signage, kiosks, and embedded devices are "bundled use" in perpetuity across hardware units; per-device or per-unit terms exist in enterprise foundry contracts.
- eReaders and ePubs: embedding subsets in publications is usually permitted under specific ePub terms; open fonts make this trivial, commercial fonts need the ePub clause.
- Hardware keyboards and firmwares rarely ship fonts, but smart TVs and set-top boxes do; those are OEM negotiations, not marketplace purchases.

## ePub and document embedding

- Document embedding (PDFs with embedded subsets) is normally covered by ordinary desktop licenses because the document is a rendered output.
- ePub is different: the file can install fonts on the reader's device, which crosses toward distribution; check the license's ePub or "electronic publication" clause.
- The distinction worth internalizing: a PDF embeds glyphs into a document, while an ePub often carries font files as assets; a document with outlines is an image of type, an ePub with fonts is a package containing software.
- Retailer platforms (the major ebook stores) may impose their own embedding requirements on top of the license; verify both layers when publishing through a store.
- OFL fonts: embed freely, keep the license accessible per the license terms when distributing the font itself; typical ePub subsetting is fine.
- Commercial ePub licenses usually tier by title sales or are sold per title; budget for the clause, not the hope.

## Workflow

1. Classify every font use: design-time (desktop), served (web), bundled (app/device), rendered server-side.
2. Buy desktop licenses for the design team's actual user count, including contractors.
3. For each shipped app or device, buy or verify an embedding license before feature freeze, not after submission.
4. Keep license documents and entitlements with the build system's legal folder.
5. Re-audit when the distribution model changes (new platform, public release of an internal tool).
6. Re-verify the seat count after organizational changes; seats drift upward quietly.
7. Keep the foundry's written answers about scope with the entitlements; they settle future questions without reopening negotiation.
8. Budget review: embedding licenses and seat counts grow with the product; treat them like infrastructure costs, not design incidentals.

## Quick reference: the three-question classifier

1. Does the user's device receive the font file? Yes means embedding or webfont, by channel.
2. Does the font render only inside our own process? Yes means desktop or server, by location.
3. Does a server or device render text at volume, or ship inside hardware? Yes means a negotiated category, priced by scale.

Run the three questions per surface, per product, at every platform launch; the answers are the license map, and the map is the audit's starting point.

## Common mistakes

- Shipping the design team's desktop-licensed fonts inside the production app because "we already own them".
- Forgetting contractor machines in the desktop user count.
- Using marketplace app license tiers meant for indie apps on an enterprise internal tool, or the reverse mismatch.
- Embedding commercial fonts in game builds during a game jam and never cleaning it up before release.
- Assuming ePub embedding is the same as PDF embedding; one is output, the other is distribution.
- Treating the app tier as a one-time decision; app pricing tiers often track revenue bands, so a successful app can outgrow its tier.

## Decision rules

- Font file crosses to a user's device inside software: that is embedding; verify that license.
- Font renders inside your own design tool only: desktop license; nothing else needed.
- Uncertain whether a platform feature (dynamic type, downloadable fonts) counts as embedding: ask the foundry in writing before launch.
- For multi-platform products, price embedding licenses as a platform matrix, and revisit at every new platform launch.
- When the same family must cover design-time and runtime, check whether the foundry offers a combined license; some do, and it is usually cheaper than two purchases and always cheaper than one audit finding.
- Prefer families with explicit app-embedding pages on their site; a foundry that prices embedding openly will answer scope questions faster when the inevitable edge case arrives.
- If budget forces a choice, license the surface with real users first and design-time last; desktop seats are the easiest and cheapest to true up after the fact.

## Comparison table: use context to license category

| Use context | License category it needs | Notes |
| --- | --- | --- |
| Designer installs font and produces mockups | Desktop | Count seats, including contractors |
| Print vendor receives outlined or PDF output | Desktop (output covered) | No separate vendor license in most cases |
| Marketing website serves woff2 | Webfont | Separate grant; pageview and domain scoped |
| Native app ships the font inside the binary | App embedding | Priced by app tier; per platform |
| Server generates PDFs or images with the font | Server / application | Usually negotiated, not cart-bought |
| ePub ships embedded subsets | ePub clause | Distribution to readers' devices |
| Kiosk or signage device ships the font | Embedded / device | Per-unit terms common |
| Internal admin tool renders documents | Server or app, per license | Some licenses have lighter internal terms |
| Slide templates shared across the company | Desktop seats for installers | Templates circulate files, not just output |
| Console game build | App embedding plus platform cert | Certification requires clean paperwork |

The map fits on one screen, which is the point: every real project is a handful of rows, and each row either matches a grant you hold or is a finding.

Fill the table once per product and revisit it at every platform launch; the rows that change are usually the ones nobody predicted, which is exactly why the map is written down rather than remembered.

## Worked example: one font, four surfaces

A fintech brand uses one commercial grotesk across four surfaces. The licensing walk:

- Design team of six, including two contractors: eight desktop seats, purchased up front; the agency's two seats are separate.
- Marketing site: a webfont license with pageview tier and the two production domains.
- iOS and Android apps: app embedding licenses for the shipping platforms, bought at the paid-app tier because the app is not free; the internal test builds ride the same grant.
- A nightly reporting service that renders PDF statements on a server: a server license negotiated with the foundry after the team asked, not assumed from the desktop purchase.
- The team wrote the surface-by-surface map into the license register before writing any checks, which is what surfaced the server case at all.
- Total cost was dominated by the app tiers, not the desktop seats, which surprised nobody once the matrix was visible.
- When the brand later considered an OFL replacement (Inter or Public Sans are common swaps), the matrix collapsed to a single row plus license retention, and that arithmetic became part of the decision.
- The switch estimate included reflow and redesign work, which is the honest cost OFL swaps trade for the licensing simplicity; both columns of that comparison went into the decision record.
- The reporting service also got a written answer from the foundry confirming server scope, filed with the entitlement; the answer cost one email and closed the risk permanently.
- App tiers were revisited when the apps went free with subscriptions; a tier change is a license event, and the register caught it because tier was a field.

## Questions to ask before purchase

- Does the desktop license count users, machines, or both, and which number do you want from us?
- Do contractors and agencies working on our behalf need their own seats or ride ours?
- Is an upgrade from one app tier to another priced as the difference or as a new purchase?
- Does adding a platform (a TV app, a console port) require a new grant or fall under the existing embedding license?
- What do you require as evidence of licensing for app store review or an audit: invoice, certificate, signed agreement?
- For internal-only distribution, are there lighter terms, and what documentation proves internal-only status?
- What happens to our rights if the foundry is acquired or the product line is discontinued?
- Do beta and TestFlight-style distribution builds count under the app tier, or is there a separate evaluation grant?
- If we ship localized builds where the font renders user content, does user-generated text change the embedding category?
- Can the embedding license be counted per title (game, app) or must it be company-wide?

## Field notes

- The most expensive mistake in this category is sequencing: buying desktop seats, then discovering app embedding later, then paying twice for the design phase that should have been licensed once.
- Platform system fonts (San Francisco on iOS, Roboto on Android) need no license and no bundling; a surprising amount of "font licensing" anxiety dissolves into using the platform's own stack where brand allows.
- App store review rarely checks font licenses, but enterprise procurement and platform certification do; do not calibrate your diligence to the lenient reviewer.
- Keep per-platform entitlements attached to the build system's documentation, because the people shipping builds are rarely the people who bought the license.
- Hardware bundles (kiosks, smart TVs) outlive software contracts; negotiate perpetuity in the embedding grant for devices, or every firmware refresh becomes a licensing event.
- If the app is white-labeled, the embedding question doubles: does the license cover your customer's deployment, and does it cover their branding of yours?
- When a design agency hands over app source with fonts bundled, the handoff memo should name the app embedding license and its holder; source code repositories rarely carry that context.
- Watch for OS-level features that blur lines: dynamic type downloads, font providers, and on-demand resources all still deliver the font to the device, which is embedding by any license's definition.
- The desktop seat count is a snapshot, not a truth: re-verify after reorgs, contractor waves, and acquisitions, because seats are the most commonly drifted number.

## Cross-references

- [Webfont embedding rights](webfont-embedding-rights.md)
- [SaaS, ebook, and embedded use](saas-ebook-and-embedded-use.md)
- [Open Font License in practice](open-font-license.md)
- [Marketplace license models](marketplace-license-models.md)

Compiled 2025 as part of the Fontlore project.
