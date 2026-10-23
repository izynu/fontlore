# Free Font Risks

What this reference covers: The specific hazards of free fonts from aggregator sites: pirated uploads, fake licenses, missing or wrong metadata, and version rot. It ends with a verify-before-use checklist and a map of free sources that do not carry these risks.

Free is a price, not a license. The fonts that cause real legal incidents are almost never the ones from careful sources; they are the ones grabbed from the first search result.

## How aggregator sites fail you

- Sites in the DaFont and 1001Fonts tradition aggregate uploads from anyone; the uploader is rarely the rights holder, and piracy is documented repeatedly across the industry.
- License labels on aggregators range from accurate to invented; "free for commercial use" is frequently pasted onto fonts that are trials, demos, or outright pirated retail fonts.
- Metadata rots: versions are old, charsets are incomplete, and the original foundry's fixes never arrive; you inherit bugs as features.
- Files are repackaged: renamed zips, stripped license files, and converted formats that break feature support.
- Malware risk is low but nonzero; font files have been used as infection vectors historically, and random re-packaging increases it.
- The "latest version" on an aggregator can be years behind the source; every rendering bug you debug in that gap is work the source already fixed.
- Aggregator pages often strip the sample text and feature lists that foundries provide, so you evaluate the font with less information than the license assumes.
- Charset integrity matters: some aggregator uploads are trimmed demos of larger families, and the missing glyphs surface only in production strings.

## The classic failure pattern

- A designer grabs a nice font from an aggregator for a client project.
- The font is actually a commercial family's trial or a pirated cut.
- The project ships, the foundry's monitoring (they do monitor) or a designer's eagle eye finds it.
- The client receives a cease-and-desist years later, retroactive licensing is negotiated at painful rates, and the agency's reputation takes the real damage.
- Every step was preventable at minute one with a source check.
- The audit trail was the second failure: nobody could say where the file came from, because the download predated the team's records. Provenance questions have a shelf life.
- The remediation chose replacement over retroactive licensing for a second reason beyond cost: the stripped file's version was so old that the licensed original would have changed the layout anyway.
- The team's intake rule now names the two artifacts required before any font enters the repo: the license document and the source URL, both checked by someone other than the downloader.

## Fake and misleading "free" categories

- Trial and demo fonts labeled as free: they are marketing samples with restricted rights; see the trial fonts guide.
- Personal-use-only fonts uploaded to aggregators with the personal-use notice stripped.
- Clone fonts: near-copies of retail designs released under new names; using them is legally murkier and reputationally worse than licensing the original.
- "Free" versions of retail families that are actually limited charset demos.
- Abandoned freeware whose author cannot be traced: the license may say free, but provenance cannot be verified, which fails due diligence for serious projects.
- fonts that are free but only in one weight, marketed under the full family's name; the missing weights are the upsell.
- Look-alike fonts that borrow a famous name with one letter changed; the game is SEO, and the license is whatever the mimic wrote.

## Verify-before-use checklist

1. Find the origin: search the font name plus "foundry" or "designer". If the origin is a foundry page, read the actual license there.
2. Read the license text, not the badge: the license name (OFL, FFL, custom), the rights granted, and the conditions.
3. Check the version: compare the aggregator's file against the source's current release; old versions are a quality and legal signal.
4. Check the file: inspect the font's name table and embedded license/copyright strings; they should match the source's claims.
5. Prefer canonical sources outright: Google Fonts, Fontsource, the foundry's own site, the designer's repository, or Fontshare for ITF work.
6. Record the source URL and date in the manifest; unverifiable provenance fails audits even when the font is lovely.
7. Cross-check the name table against the source's claims with a tool like FontDrop; two minutes that catch stripped files instantly.
8. Re-run the check when the font moves between projects, and when a new version appears at the source; yesterday's verification does not transfer.

## Safe free sources, recapped

- Google Fonts: open licenses (OFL, Apache, UFL), curated, versioned through the google/fonts repository.
- Fontsource: npm-packaged open fonts with version pinning; provenance is clean.
- Fontshare: ITF's own platform; free-use under ITF FFL with honest labeling.
- SIL: the OFL's author, with literacy-grade fonts and meticulous licensing.
- Independent open foundries (Velvetyne, The League of Moveable Type, and similar): OFL with upstream repos.
- The pattern: a source that identifies the rights holder and ships the license text is safe; a source that ships only the file is not.
- Variable-font-focused repositories and open foundry collectives (Velvetyne, OSP, and peers) publish source files and licenses together, which is the gold standard for verifiability.
- University and government releases (Public Sans from the US Web Design System, for example) carry institutional licensing discipline worth copying.

## Workflow

1. Before any free font enters the project, run the checklist above; five minutes maximum.
2. If the origin is an aggregator but the font traces to a clean source, re-download from the source.
3. If the origin cannot be traced, treat the font as unusable for commercial work; find a documented alternative.
4. Record license, version, source, and checker in the manifest.
5. Re-verify when the font moves between projects; yesterday's verification does not transfer automatically.
6. When a font fails the checklist mid-project, log the replacement decision with the date; the record is what turns an incident into a policy.

## Common mistakes

- Trusting the aggregator's "100% free" tag over the absence of any license document.
- Using a pirated retail font unknowingly and defending it with "it was on a free fonts site".
- Keeping unverified fonts in shared asset libraries where they silently propagate into every new project.
- Ignoring version rot: fixing rendering bugs caused by ancient files instead of updating from the source.
- Assuming malware is the only risk and skipping the license check.
- Reusing a verified font's license notes for a different file from the same site; verification is per file, not per site.
- Treating the manifest entry as done when the URL is recorded but the license document is not stored; links rot, documents persist.

## Decision rules

- No traceable rights holder: do not use, regardless of how good the font is.
- Traces to a clean source: re-source from the clean origin and verify there.
- Only available via aggregator with no origin: find an open alternative; the substitution cost is lower than the incident cost.
- When in doubt, the open-source ecosystem now covers enough ground that "we could not find a legit version" is rarely true.
- For heritage freeware that matters to a project, the honest paths are contacting the author or replacing the font; hope is not a license path.
- Anything that will ship to users under your brand gets the full checklist; internal-only experimentation can be lighter, but the files must be marked as unverified so they never migrate outward silently.
- Free does not mean anonymous: the free fonts with the cleanest histories are the ones whose authors stayed findable for a decade.
- When aggregators are the only mirror of a legitimately free font, cite the original author's page as the source in the manifest, not the mirror.

## Quick reference: the two-minute triage

1. Does the file have a license document with it? No: stop.
2. Does the name table name a real designer or foundry? No: stop.
3. Does the source resolve to a canonical origin (foundry, google/fonts, Fontsource, designer repo)? No: stop.
4. Does the license class match the use (commercial product, client work)? No: find an alternative.
5. Record license, version, source URL, date, checker: done.

Most rejected fonts fail at step 1 or 2, which is why the triage is fast; the expensive failures are the ones that skip the triage entirely.

## Signals to trust

- A license file with the font, naming a rights holder that exists and matches the name table.
- A canonical source: the foundry's own site, the google/fonts repository, Fontsource, Fontshare, or the designer's own repository, with the license text visible.
- Version history: releases with changelogs and dates suggest a living project rather than an abandoned upload.
- A name table whose family, designer, and license fields agree with the source's claims.
- An issue tracker or contact path where someone actually answers.

## Signals to distrust

- "100% free" badges on sites that ship no license document; badges are content, not grants.
- File names that differ from the family's real name, or zips renamed to dodge detection of pirated retail fonts.
- A font that is clearly a retail design (a well-known grotesk, a famous serif) offered free by a third party; famous designs are almost never free.
- Metadata stripped out: a font with an empty or generic name table has had its provenance deliberately removed.
- "Free for personal use" text pasted into a description while the download ships a full commercial charset.
- Wrong or impossible dates in metadata (a 2019 release of a font designed in 2021), which reveals sloppy repackaging.

## Worked example: the aggregator audit

A product team inherited a landing page using a display font downloaded years ago from an aggregator site. The audit walk:

- The font's name was a near-match to a retail serif by a known foundry; the file's name table was largely blank except for the family name.
- Searching the real family name plus "foundry" found the original: a commercial family with a paid license and a free trial cut. The aggregator file was the trial, stripped.
- The team's options were retroactive licensing or replacement; the font was used for one headline only, so replacement won.
- The replacement (an OFL display face with a similar voice) went through the normal intake: provenance check, license file, version record.
- The audit record now shows the incident, the substitution, and the rule adopted: no font enters the repo without a license document and a canonical source URL.
- Total cost: half a day. The same discovery by the foundry's monitoring would have started with a letter, not a task ticket.
- The substituted face was chosen from the open catalog in an hour; the scarcity that made the aggregator download feel necessary was never real.
- The team also scanned the rest of the asset library with the same checklist and found two more stripped files; audits of this kind always find siblings.
- The policy that stuck: the manifest row is created before the file is added, not after; reverse order is how unverified files hide.

## Field notes

- Aggregators are not uniformly malicious; many hosts genuinely free fonts. The problem is that the site's business model (traffic) has no stake in the license being right, so verification is always the user's job.
- Clone fonts deserve their own caution: a near-copy under a new name may be legal where it was made, but using it in place of the original is a design-quality decision as much as a legal one.
- The safest habit is boring: download from the source, record the URL, record the date, move on. Every shortcut in this chain is where the risk enters.
- Old freeware with a vanished author is a dead end for commercial work no matter how lovely; the license may say free, but unverifiable provenance fails due diligence.
- When a client supplies fonts, apply the same checklist to their files; clients inherit their vendors' risks.
- Font identification communities and reverse image search are legitimate first steps for tracing a font's origin; use them before adopting anything anonymous.
- Keep a substitution list: for the roles unverified free fonts were playing, name the documented open alternatives in advance, so the swap is a lookup instead of a project.
- When an aggregator site is the only place a font exists, treat the font as unusable for commercial work even if the license text looks generous; provenance failure is disqualifying on its own.
- Track which sites your team's downloads historically came from; the pattern tells you where your process leaks.

## Cross-references

- [Open-source due diligence](open-source-due-diligence.md)
- [License audit checklist](license-audit-checklist.md)
- [Trial and early access fonts](trial-and-early-access-fonts.md)
- [Google Fonts Catalog](../sourcing/google-fonts-catalog.md)

Compiled 2025 as part of the Fontlore project.
