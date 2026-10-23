# Fontshare and ITF Free Fonts

What this reference covers: How to use Fontshare, the free-font platform from the Indian Type Foundry, and how its ITF FFL license differs from true open-source licenses. It covers the catalog's notable families, ITF's Google Fonts output, and the legal lines you should not cross with FFL fonts.

Fontshare publishes high-quality retail-grade families for free, which makes it one of the best free sources in typography. The catch is licensing: ITF FFL is a free-use license, not an open-source license, and teams that confuse the two eventually get burned in audits or handoffs.

## What Fontshare is

- Fontshare is operated by the Indian Type Foundry, a commercial foundry founded in 2014 and known for retail families and for contributions to Google Fonts.
- The catalog is curated rather than exhaustive: dozens of families, nearly all contemporary sans and serif designs with strong marketing presentation, full specimens, and downloadable variable or static builds.
- Families ship with clear style lists, glyph coverage, and language tags, and the site offers a hosted CSS API alongside direct downloads.
- Quality is unusually consistent for a free source because these are foundry retail designs being promoted, not abandonware.
- A hosted CSS endpoint in the general shape below serves requested weights; check the site for the current parameter format before scripting against it.

```
https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700&display=swap
```

## Notable families

- Satoshi and General Sans are the platform's flagship neo-grotesque sans faces, common choices for product and marketing work.
- Switzer is a Helvetica-adjacent grotesque with a wide weight range; Cabinet Grotesk is a friendlier display-leaning grotesque.
- Clash Display and Melodrama are display faces for headlines; Tanker is a single-style bold display face.
- Gambetta, Erode, and Boska cover serif and text-leaning needs; Author is a reading-oriented sans designed for long-form use.
- Chillax and Ranade offer distinctive personality when a project needs less neutral voice.
- Panchang pairs Latin with Devanagari, reflecting ITF's bilingual design practice.

## ITF on Google Fonts

- ITF designs also appear on Google Fonts under open licenses, which is a separate, genuinely open-source channel: Poppins, the Hind series, Teko, Rajdhani, and Khand are prominent examples.
- Poppins, credited to Jonny Pinhorn and Ninad Kale, became one of the most-used geometric sans faces on the platform and pairs Latin with Devanagari.
- The distinction matters for licensing: the same publisher operates both a free-use store (FFL) and an open-source channel (OFL). Check which one a given file came from.
- If a project requires modification or redistribution rights, prefer the ITF families that were released through Google Fonts under the OFL.

## ITF FFL license basics

- The ITF Free Font License grants use in personal and commercial projects at no cost. Attribution is not required for ordinary use.
- It is not an open-source license: you may not sell the font files, and redistributing the files themselves is restricted. Host your own copies per the license terms rather than re-uploading them to public repositories.
- Modification rights are limited compared to the OFL; do not assume you may derivate, subset-and-redistribute, or fork an FFL family the way you would an OFL family.
- Unusual uses, such as bundling in an application or redistributing inside a design system package, deserve a careful read of the current FFL text on fontshare.com before you ship.
- Record the license as ITF-FFL-1.0 in font inventories and keep a copy of the license text with the files so future maintainers do not have to guess.

## Workflow

1. Shortlist FFL families like any other source, using specimens and real copy at real sizes.
2. Before adoption, read the FFL text on Fontshare and map it against the project's usage contexts: web, app, print, logo, client handoff.
3. If any context is restricted (modification, redistribution, app embedding), either drop the candidate or route through an OFL alternative.
4. Download from Fontshare directly, keep the license file alongside the fonts, and log the source URL and date.
5. Never commit FFL font files into public open-source repositories; that is redistribution the license does not grant.

## Common mistakes

- Treating Fontshare fonts as OFL-equivalent and pushing them into open-source packages or forked builds.
- Re-hosting FFL files in public repos, package registries, or design-file templates shared with the world.
- Modifying letterforms and shipping the result, assuming a free font is a modifiable font.
- Forgetting the license during client handoff: FFL fonts can usually be used by the client, but the handoff should still document source and license terms.
- Assuming every ITF design is on Fontshare and every Fontshare font is by ITF; the platform also hosts collaborating designers, so check each family's credits.

## Decision rules

- Need modification, redistribution, or bundling rights? Choose the OFL channel (ITF families on Google Fonts) over FFL families.
- Need a distinctive retail-quality sans for a commercial project with no redistribution? Fontshare is one of the strongest free options available.
- When in doubt about a FFL clause, write to the foundry; their answers are usually quick and specific, and a written answer is audit evidence.

## Catalog tour: matching families to jobs

Fontshare families earn their reputation in specific roles. The common failure is using a display voice where a text voice was needed.

| Family | Voice and best role | Watch out for |
| --- | --- | --- |
| Satoshi | Geometric-leaning flagship sans for product and marketing | Ubiquity has dulled its distinctiveness |
| General Sans | Neutral, slightly warm UI sans | Modest personality; needs strong layout |
| Switzer | Helvetica-flavored grotesque, wide weight range | Neutral voice can read as generic |
| Cabinet Grotesk | Warm display grotesque | Limited fitness for small text |
| Clash Display | High-contrast display sans for headlines | Spacing tuned for display sizes only |
| Gambetta | Old-style-flavored text serif | Lean display range |
| Erode | Soft-edged serif with a bookish texture | Test numerals in data-heavy contexts |
| Zodiak | High-contrast serif for editorial headlines | Headlines only |
| Sentient | Old-style serif with a quiet voice | Narrow weight range |
| Author | Reading-oriented sans for long-form | Small style range |
| Panchang | Bilingual Devanagari and Latin sans | Verify Devanagari shaping at your sizes |

None of these are bad designs; the catalog is coherent. The job is picking the two or three whose voices match the brief instead of adopting the whole platform.

## FFL versus OFL at a glance

The two ITF channels differ in rights, and the differences are exactly the ones that surface during audits and open-source work.

| Right | ITF FFL (Fontshare) | OFL 1.1 (Google Fonts channel) |
| --- | --- | --- |
| Use in commercial client work | Yes | Yes |
| Modify letterforms and ship the result | Restricted; read the license text | Yes, with Reserved Font Name rules |
| Redistribute the font files | No | Yes, with the license attached |
| Commit files to a public repository | No | Yes, license file included |
| Sell the font file itself | No | No |
| Attribution paperwork | Not required for ordinary use | Keep copyright and license notices |

If the project plan includes an open-source design system package, a public repository, or any redistribution, the FFL column fails and the OFL column passes. That single row decides more Fontshare adoptions than any design debate.

## Worked example: Satoshi and the open-source fork problem

Scenario: a startup adopts Satoshi for its product; six months later the design system is scheduled to be open-sourced, fonts included.

1. Flag the conflict early: FFL files cannot be committed to the public repository, so "open-source everything" is now blocked by typography.
2. Re-read the FFL text on fontshare.com and confirm the restriction in the current wording; do not rely on anyone's memory, including this reference.
3. Decide the path: keep Satoshi and exclude fonts from the open-source release, or replace the family with an OFL equivalent.
4. OFL candidates with a comparable contemporary-sans voice: Hanken Grotesk, Instrument Sans, Schibsted Grotesk, Figtree. Test each against the existing Satoshi-set interfaces for metric and tone drift.
5. If replacement wins, re-approve headlines, labels, and numerals at real sizes; substitution is a design change, not a find-and-replace.
6. Record the decision and the rejected path in the manifest so the question does not reopen every quarter.

The lesson generalizes: the rights your roadmap will need are part of font selection, even when licensing feels like a launch-day formality.

## Signals to trust

- Family pages that state style lists, glyph coverage, and language tags plainly; the platform's presentation is unusually honest for a free source.
- Quality consistency across the catalog: these are retail designs being promoted, not abandonware scraped from forums.
- Written foundry answers to FFL questions, which are typically quick and specific.

## Signals to distrust

- "Free font" framing that implies open source; Fontshare is free-use, which is a different legal object.
- Any claim about FFL rights from memory, including from this reference; the current license text on the site is the only authority.
- Assumptions that the hosted CSS endpoint is a stable contract; the parameter format can change, so self-hosting is the durable choice for production.
- Credits remembered instead of checked; the platform hosts collaborating designers, so authorship varies family by family.

## Questions to ask before adopting

- Which planned uses (web, app bundling, print, client handoff, open-source release) does the FFL text actually cover, in writing?
- Do we need modification rights for a planned fork, condensed variant, or re-weighted build?
- Who owns keeping the license copy alongside the files we distribute internally?
- Is there an OFL sibling or equivalent that removes the license question entirely?
- If a foundry answer is needed, who writes to them, and where is the reply stored?

## Field notes

- Fontshare releases lean variable; many families ship variable builds, which makes weight-range-driven design systems comfortable without extra files.
- Keep the license file beside every FFL font you distribute internally; future maintainers should not have to rediscover what they inherited.
- ITF's Google Fonts channel and Fontshare are separate release tracks; versions and even some design details can differ between channels, so pin whichever you adopt.
- Poppins, the Hind series, Teko, Rajdhani, and Khand are the high-profile OFL names; if a brief needs ITF's craft with open rights, start there rather than stretching FFL terms.
- Never commit FFL files to npm, public Git repositories, or shared design-system packages; that is redistribution, and repository history preserves the evidence.

## Cross-references

- [Open and independent foundries](open-and-independent-foundries.md)
- [Regional and script catalogs](regional-and-script-catalogs.md)
- [License families compared](../licensing/license-families-compared.md)
- [Free font risks](../licensing/free-font-risks.md)

Compiled 2025 as part of the Fontlore project.
