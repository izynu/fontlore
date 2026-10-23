# Webfont Embedding Rights

What this reference covers: What webfont embedding rights actually grant, how pageview and domain limits work, and the trade-offs between self-hosting and hosted services. It also covers the gray areas: webviews, SaaS dashboards, and staging environments.

Webfont licensing is where most accidental violations happen, because the web is where usage quietly grows. The rules are simple once stated; the discipline is measuring and documenting them.

## What web embedding rights mean

- A webfont license grants the right to serve the font files from your web properties so visitors' browsers download and render them.
- The grant is scoped by the license: which domains, how many pageviews per month, sometimes which subdomains and staging hosts.
- Serving means the file reaches the visitor: CDN delivery, self-hosting, and build-pipeline inlining all count as serving.
- Rendering on a server (PDF generation, image rasterization) is usually NOT webfont use; it is server or desktop use with different rules.
- What is always forbidden without extra rights: letting third parties download and reuse the font files as fonts (the file must be used to render your content, not redistributed).
- The forbidden case is rarer than teams fear and easier to trigger than teams think: a font-face rule on a public stylesheet makes the woff2 URL public, and anything public gets hotlinked eventually. Some teams block cross-origin font requests at the CDN for exactly this reason, which is a technical control aligned with the license's intent.
- The distinction that survives every architecture debate: who consumes the file as a font. If only your pages do, it is serving. If a visitor could take the file and use it, the license conversation changes.

## Pageview limits

- Marketplace webfont licenses historically tier by monthly pageviews: a quota (for example 250k, 1M, 10M) with higher tiers costing more.
- Exceeding the tier does not break rendering; it breaks the license. Monitoring is therefore a compliance task, not just a performance task.
- Measure honestly: pageviews counted at the CDN or analytics level should match the license definition (some count sessions, some count raw requests; read the definition).
- Record the definition itself in the register: "pageviews per vendor means served HTML documents at covered domains" is a sentence that prevents a future argument.
- When measurement systems change (a new analytics vendor, a CDN migration), re-derive the numbers against the license definition before assuming continuity.
- Growth curves beat point-in-time numbers: a chart of monthly pageviews against tier makes the upgrade conversation a formality rather than a negotiation.
- Plan growth: pick the tier that covers twelve months of projected traffic, and set an alert at 70 to 80 percent of the limit.
- Campaign spikes (launches, press) are the classic violation moment; pre-upgrade before a known spike.

## Domain and subdomain scope

- Licenses specify covered domains; www vs apex, staging hosts, and preview deployments are where scope mismatches hide.
- List every host that will serve the font: production domains, marketing microsites, docs sites, and staging.
- Wildcard coverage exists in some licenses; when absent, each additional domain is an additional cost line.
- Preview and CI environments that render real traffic-facing pages should be treated as in-scope until the license says otherwise.
- Keep the domain list in the font manifest and re-verify when new properties launch.

## Self-hosting versus hosted services

- Self-hosting (Fontsource packages, vendored files, foundry kits): you control files, versions, caching, and privacy; you own the compliance duty for scope and pageviews.
- Self-hosting also moves verification upstream: the files you vendored should be checked against the foundry's published versions at intake, because a webfont bought from a marketplace can still arrive stale.
- A hybrid exists: self-host with a license that includes free minor-version updates, which splits the difference between control and freshness; ask for it in negotiation.
- Google Fonts CDN: free and easy, but the served version is unpinned and requests leak visitor data to a third-party origin, which some privacy regimes care about.
- Adobe Fonts web serving: covered by the subscription through Adobe's hosted kits only; self-hosting the files is not permitted.
- Foundry-hosted kits: convenient, but check what happens to availability and billing if the subscription lapses.
- The compliance story is clearest with self-hosting under a written scope; the operational story is easiest with a hosted service. Decide which risk you prefer to manage.

## Gray areas

- App webviews and hybrid apps rendering your web content: usually fine under webfont scope, but in-app bundling of font files is app licensing; check which one your architecture does.
- SaaS dashboards behind login: webfont licenses generally cover them, but enterprise foundry contracts often negotiate this explicitly; confirm for large deals.
- Email embedding of fonts: mail clients largely strip webfonts anyway; do not spend license money here.
- PDF generation from web content: the server does the rendering, which is server-use territory; some webfont licenses explicitly exclude it.
- Open-source projects shipping webfont demos: redistribution rules apply; use OFL fonts to keep this simple.
- Password-protected shareholder or investor portals count as web serving; exclusivity is not a licensing category.
- Offline-capable web apps (PWAs) that cache fonts locally are still webfont use; the license cares about delivery to the visitor's browser, which is exactly what a service worker does.
- Embedded analytics dashboards rendered inside customer sites via iframe: the serving origin is yours, so your license scope applies; the iframe does not push the duty to the customer.
- Documentation sites on separate domains (docs.example.com, developers.example.com) are separate hosts in the license's eyes unless the grant is broad.

## Workflow

1. For each font in production, record the license type and the exact web scope it grants.
2. Inventory every host serving the font, including staging and previews.
3. Set pageview monitoring with alerts under the license limit.
4. Choose delivery architecture (self-host vs hosted) deliberately and record the privacy and availability rationale.
5. Review scope quarterly and before launches; update the manifest with changes.

## Common mistakes

- Buying a desktop license and self-hosting the webfonts anyway because "the files were right there".
- Letting a viral marketing page blow through a 250k pageview tier silently.
- Forgetting staging hosts in the license scope, then failing an audit over a test environment.
- Serving Adobe Fonts-subscribed fonts from your own origin, which the terms do not allow.
- Counting "pageviews" differently than the license does and discovering the gap during a renegotiation.

## Decision rules

- Traffic growth is predictable and versioning matters: self-host with a scoped license and monitoring.
- Privacy commitments forbid third-party font origins: self-host, including for Google Fonts families.
- Rapid experimentation across many microsites: a hosted service or a broad multi-domain license beats per-site purchases.
- Any architecture that renders fonts server-side: treat as server/desktop use and check that license, not the webfont one.

## Comparison table: delivery models

| Model | Files live on | Version control | Pageview handling | Dies with subscription | Watch for |
| --- | --- | --- | --- | --- | --- |
| Self-hosted commercial | Your origin | You pin versions | Your monitoring against the tier | No (perpetual license) | Tier headroom and domain scope |
| Google Fonts CSS API | Google's CDN | None (unpinned) | No caps | No | Privacy exposure; silent updates |
| Fontsource npm | Your build output | package.json + lockfile | Your monitoring | No | License travels in the package |
| Adobe Fonts web kits | Adobe's serving | Managed by Adobe | Project caps in Adobe terms | Yes | No self-hosting; kits required |
| Foundry-hosted kits | Foundry's serving | Managed by foundry | Per contract | Usually | Availability and lapse behavior |
| OFL self-hosted | Your origin | You pin versions | No caps | No | RFN rules on public redistribution |
| Google Fonts families self-hosted | Your origin | You pin versions | No caps | No | License and notices stay with files |
| CDN in front of self-hosted files | Your bucket, their edge | You pin versions | Your monitoring | No | Edge config must not strip CORS |

The table's quiet lesson: licensing risk concentrates where files and billing are controlled by someone else, while operational risk concentrates where you control everything. Pick the risk you would rather own.

Two patterns the table hides but audits surface constantly: teams on hosted services that assume perpetual rights, and teams on perpetual licenses that assume the foundry's newest versions are included. Both assumptions are wrong in most contracts; both are cheap to check.

## Worked example: the 250k tier launch

A product self-hosts a commercial webfont licensed for a 250,000 monthly pageview tier. The launch plan and the license math:

- Baseline traffic is 40,000 pageviews weekly, about 175,000 monthly; the tier holds until the launch campaign triples traffic for two weeks.
- The campaign would push the month to roughly 400,000, which breaches the tier for that month even if the average never sustains.
- The team upgrades to the 1M tier before launch instead of negotiating an overage after it; the upgrade is priced from the same vendor and takes a purchase order, not a renegotiation.
- The alert threshold was already set at 80 percent of tier in the monitoring dashboard, which is how the risk was visible weeks ahead.
- The domain list (production apex, www, and the campaign microsite) is checked against the license scope; the microsite was added to the license at purchase, not assumed.
- The audit trail now shows: tier upgrade dated before launch, monitoring screenshot, and the license document version that applies.
- Post-launch review records actual pageviews against the tier so the next campaign inherits real numbers instead of guesses.
- The count the vendor cares about is the license definition's count, not the analytics dashboard's; the team reconciled both once and documented the 4 percent gap between them.
- Had the launch slipped a quarter, the same math would have applied; tier decisions are calendar-independent, which is why monitoring exists.
- The negative pattern is equally documented: a competitor's launch blog went viral, doubled traffic for a month, and the breach was discovered in a renewal-year audit rather than in any dashboard.
- The team's register now stores tier, alert threshold, current month's count, and the vendor's count definition in one row per licensed font.
- Nothing in this example required negotiation skill; it required the numbers existing before the campaign did.

## Questions to ask the vendor

- How exactly are pageviews counted: raw requests, rendered pages, or sessions? Which measurement do you expect us to reconcile against?
- Are staging, preview, and QA hosts in scope, or must they be listed separately?
- What is the overage process: automatic billing, a grace period, or termination of serving?
- What is the price and turnaround for moving up one tier mid-contract?
- Is usage behind authentication (customer portals, apps with webviews) covered by the webfont grant?
- For hosted serving: what data protection terms apply to visitors whose browsers hit your origin?
- If we migrate to self-hosting later, what does the license say about the transition?
- Do you require notification when we add a domain, or is a wildcard grant in force?
- Are campaigns and A/B test domains (with their vanity hosts) covered by the same grant?
- What evidence will you accept from us during an audit: server logs, CDN reports, or your own measurement?
- Does the grant cover serving fonts from a different origin than the page origin (fonts.example-cdn.com), and does that count separately?

## Field notes

- The most common real-world gap is not a big breach; it is a forgotten microsite or a staging host that never left the license's blind spot for years.
- Google Fonts families can be self-hosted precisely because their licenses are open; the CSS API versus self-hosting choice for them is about privacy and control, not licensing.
- When an enterprise deal is negotiated, get the pageview definition written into the contract body, not an appendix; definitions drift between documents.
- Webfont licenses are usually perpetual but tied to a version; the right to serve the font does not automatically include future versions the foundry releases.
- If your architecture inlines fonts into a bundle or uses a service worker to serve them, you are still "serving" to visitors; the license category does not change with the delivery mechanism.
- Keep the purchase email with the entitlement; support portals get migrated and decommissioned far more often than mail archives.
- A pageview tier that survived three years of growth is not evidence of compliance forever; recheck at every analytics migration, because definitions change when measurement changes.
- When legal asks "what happens if we exceed the tier by 10 percent for one month", the honest answer is that the license says whatever it says; overage clauses are the place to look, and the place to ask.
- Teams that churn marketing sites should consider broad multi-domain licenses; five microsites on five separate grants is five audits.
- Browser caching reduces requests but not pageviews in most definitions; caching is not a compliance strategy.
- If the license prohibits modifying files (some do beyond subsetting), your optimization pipeline may be the breach; check the modification clause, not just the serving clause.
- Document who owns the vendor relationship; when the contact leaves, entitlements that lived in their account often vanish with them.

## Cross-references

- [Marketplace license models](marketplace-license-models.md)
- [SaaS, ebook, and embedded use](saas-ebook-and-embedded-use.md)
- [Open Font License in practice](open-font-license.md)
- [Fontsource REST API](../sourcing/fontsource-api.md)

Compiled 2025 as part of the Fontlore project.
