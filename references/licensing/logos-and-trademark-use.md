# Logos and Trademark Use

What this reference covers: Using fonts in logo artwork: what licenses say about logo use, how trademark law differs from copyright in this area, why converting text to outlines does not escape the license, and the Reserved Font Name traps that catch teams modifying fonts for marks.

Logo use is the most feared and least understood font licensing topic. The fear is mostly misplaced for open fonts and entirely justified for some commercial licenses. Here is the actual map.

Two questions hide inside every logo conversation: what the font license permits, and what trademark law protects. They have different owners, different documents, and different failure modes; this file keeps them separated on purpose.

## What licenses say about logo use

- The OFL explicitly permits using the font in logo artwork, along with every other use; no special logo clause exists because none is needed.
- Many commercial licenses also permit logo use, but some restrict it, require an upgrade, or exclude trademark registration scenarios; the license's scope table is the only authority.
- Watch for licenses that distinguish "logo use" from "trademark use": the second can involve registration, which some foundries want to discuss before you file.
- Trial and personal-use licenses never cover logo use for a business; if the mark ships, so does a real license.
- The scope table in a commercial EULA is where the answer lives; marketing pages saying "used by brands" is not a grant.
- If the license is silent on logos, silence is not permission; it is a question to send to the foundry in writing, with the launch date in the first sentence.

## The outline conversion question

- Converting text to outlines produces vector artwork, but the artwork's provenance is still the font software; licenses bind the use of the font, not the file format of the output.
- Foundries' positions agree on the principle: rendering a font into a logo (whether by outline conversion or by printing) is a permitted use under licenses that allow logo use.
- What conversion does change: distribution. Sending outlined logo files to vendors or the public does not distribute the font software, so redistribution clauses are not triggered.
- The trap is modifying the letterforms: once you alter outlines and redistribute the modified artwork, you are in derivative territory for OFL fonts with Reserved Font Names if you redistribute font files, though outlined artwork alone is not font distribution.
- Practical rule: the license question is asked at the moment of use (rendering the font into the mark), and the answer lives in the license's use scope, not in the export menu.
- The moment-of-use rule has a practical corollary: photograph the license and the specimen into the brand archive when the mark is finalized; three years later, nobody remembers which license was in force.
- Outlining also destroys hinting and text re-flow, which is why packaging art is outlined and document text is not.

## Trademark law is a separate layer

- Copyright in the font software and trademark rights in the mark are different legal regimes; licensing the font does not create or transfer trademark rights.
- Your trademark protects the mark as a source identifier; you do not need any font license to enforce the trademark.
- Conversely, licensing a font does not clear you of trademark conflicts: if your mark is confusingly similar to another's, no font license helps.
- Distinctiveness matters in font choice for marks: highly distinctive lettering strengthens a mark; a common typeface contributes little distinctiveness, which is one reason brands commission custom lettering.
- Search clearance and trademark counsel live outside this guide; the font team's job is to document what was licensed and used.
- One practical bridge between the layers: trademark examiners sometimes cite the font used in a specimen as evidence of how a mark appears, so consistent licensed use also produces a cleaner filing record.
- Typeface names are often trademarked by their foundries as well; referring to "Inter" in marketing copy about your product is nominative use, but branding your own font product with a similar name is a different conversation.

## Reserved Font Name traps in logo work

- If a designer modifies an OFL font to build the mark and the design system later redistributes that modified font internally or publicly, RFN rules apply to the font files.
- The mark itself is unaffected by RFNs; the trap only springs when modified font files get distributed.
- Agencies that "tweak" a client's font for the logo should either keep the modification internal or renegotiate the font's naming before delivery.
- Document the base font, the modifications made, and the RFN status in the brand guidelines; future teams will otherwise re-derive this painfully.

## Custom lettering as the escape hatch

- When a license forbids logo use, the standard solution is commissioning custom lettering: the resulting artwork is yours by contract, with no font license attached.
- Custom lettering also solves the distinctiveness problem and reads as intentional brand investment.
- The middle path: license a font that permits logo use and adjust nothing; many strong marks are straight type settings.
- Keep artwork sources and license records together; audits ask "what made this mark?" and the answer should be written down.
- Commissioned lettering should state in the contract that the letterform artwork is assigned or exclusively licensed; otherwise you have paid for a drawing whose ownership is ambiguous.
- A hybrid is common and legitimate: a retail font for body text and brand surfaces, custom lettering for the mark only. The two records just must not blur.

## Workflow

1. Before finalizing the mark, read the candidate font's license scope table for logo and trademark clauses.
2. If terms are unclear or restrictive, decide: change font, upgrade license, or commission lettering.
3. Record the font, version, license, and any modifications in the brand documentation.
4. If outlines were converted, note that the use right came from the license in force at creation time.
5. Hand off to legal for trademark clearance; do not conflate the two processes.
6. Archive the license document, the font version, and the specimen into the brand repo on the day the mark is approved.
7. Re-run steps 1 and 2 whenever the mark's letterforms are substantially redesigned; a new cut is a new use.

## Common mistakes

- Assuming outline conversion removes licensing obligations; it does not.
- Using a trial font for the logo pitch and shipping the winning mark without a real license.
- Modifying an OFL font for the mark and later publishing the modified font under the reserved name.
- Treating "the foundry's FAQ says logos are fine" as the license; the license document is the contract.
- Conflating trademark clearance with font licensing and delaying both.
- Distributing a modified logo font inside a brand kit to every agency on the roster, multiplying the RFN problem by the number of recipients.
- Asking the foundry for permission verbally on a call and treating the memory as the grant; get the email.

## Decision rules

- Open fonts (OFL): logo use is a non-issue; spend the worry budget elsewhere.
- Commercial fonts: check the scope table; when logo use costs extra, price it into the brand project before choosing the font.
- Any redistribution of modified font files: resolve RFN naming first.
- When the mark's distinctiveness is the brief, custom lettering beats any license gymnastics.
- If the font's logo terms are expensive, weigh them against a custom lettering commission before assuming the license is the only path; sometimes the commission is cheaper and always more distinctive.
- Anything ambiguous in the scope table: the cost of a written foundry answer is an email; the cost of guessing is a mark built on sand.

## Worked example: a rebrand under audit

A startup's wordmark is set in an OFL geometric sans (Space Grotesk is a common choice of this kind); the symbol is custom drawn. Three years later, an acquisition audit asks where every brand asset came from:

- The wordmark: the license is the OFL, the font is unmodified, logo use is explicitly permitted; the audit passes with a copy of OFL.txt and the specimen file archived with the brand assets.
- The designer had also "cleaned up" a few letterforms and kept the modified font in the brand kit folder. The mark itself is unaffected, but the modified font file in a kit distributed to agencies is a redistribution of a Modified Version named with a reserved string.
- The fix cost an afternoon: the modified file was removed from the kit, the mark's outlines were delivered instead, and the internal note records that any future redistribution of the modified font requires a rename under the RFN rules.
- The custom symbol had no font at all, so its documentation was a one-paragraph provenance note: who drew it, when, under what contract.
- The letterform cleanups were also the reason the mark looked distinctive; the lesson recorded was that modification is a design tool, and RFN discipline is the price of keeping it in the open.
- The audit interview took thirty minutes because every answer had a document behind it; the same questions at another company routinely take weeks.
- The audit's finding was zero, but the exercise documented the difference between "we think this is fine" and "here is the license, the provenance, and the reasoning", which is the difference acquirers actually price.
- The team's brand book now includes a two-page "type provenance" appendix; it takes one hour to update per rebrand and has already been requested twice in vendor onboarding.

## Comparison table: the two legal layers

| Question | Font license answers it | Trademark law answers it |
| --- | --- | --- |
| May I render this font into a logo? | Yes or no, per the grant | Not its question |
| May I register the resulting mark? | Not its question | Clearance, distinctiveness, filing |
| May I enforce the mark against copycats? | Not its question | Trademark rights do this |
| Must I credit the typeface publicly? | Usually no; keep license with files | Not its question |
| Do I own the letterforms I set? | No; the design stays with its author | The mark, as a whole, can be yours |
| Does outlining change the analysis? | No; use rights were fixed at creation | No effect on trademark either |
| Does modifying letters create risk? | RFN rules on redistributing modified font files | Only insofar as the mark changes |

Reading the table right to left and left to right is the whole skill: teams that mix the columns either over-pay for permissions they already have or assume clearance they never obtained.

## Field notes

- Many famous wordmarks are not retail fonts at all; they are custom lettering or heavily modified cuts, which is why "our brand font is fine for the logo" is a question, not an answer.
- The fsType embedding bits in the font's OS/2 table govern document embedding, not logo use; checking them for logo questions is a category error.
- When a foundry's site says "contact us for logo licensing", that is pricing, not prohibition; the written answer defines the grant.
- Portfolio sites and Dribbble shots are not license evidence; the license document in the brand repo is.
- If the mark was made by a freelancer, the freelancer's license (or its absence) is your problem the moment you ship; audit at intake, not at exit.
- Distinctive custom lettering has a second benefit the legal analysis ignores: it cannot be matched by a competitor buying the same retail font.
- Logotype licensing questions spike at two moments: rebrands and trademark filings. Budget the license review into both milestones.
- Keep a single owner for the mark's type provenance; committees produce records with gaps.
- When in doubt about what a "logo license" includes, ask for the clause by name; foundries answer "does section 4.2 cover packaging use" far better than "is this allowed".

## Questions to ask before the mark ships

- Which font, which version, which license document, and does that document mention logos or marks at all?
- Was the font modified to make the mark, and where do the modified files live?
- Will any modified font files be distributed (brand kits, agencies, contractors), or does only the outlined artwork travel?
- If the font is OFL with a Reserved Font Name, does anyone downstream plan to publish modified files?
- Has trademark counsel cleared the mark independently of the font licensing?
- Is the provenance of every letterform in the mark written down somewhere durable?
- Does the license cover the mark's uses beyond the screen: signage, merchandise, broadcast, packaging? Logo grants sometimes exclude surfaces the brand will reach within a year.
- If the foundry offers an extended logo license, what does it add beyond the standard grant, and is the price comparable to commissioning lettering?
- Does the brand kit ship font files or outlines, and does that match what the license allows?
- Who signs off that the font licensing and trademark clearance are both complete, and where is that recorded?

## Quick reference: the mark's paperwork stack

1. License document for the font, with logo use confirmed (or the OFL text).
2. Written foundry answer for any silent or ambiguous clause.
3. Modification record: what was changed, by whom, and where modified files live.
4. Provenance note for custom lettering: author, date, contract.
5. Trademark clearance result from counsel, kept separately.
6. Brand kit contents list, stating files versus outlines.

Six documents, one folder, updated at every rebrand. That folder is what turns a logo's type history from folklore into a record.

## Cross-references

- [Open Font License in practice](open-font-license.md)
- [OFL reserved font names](ofl-reserved-font-names.md)
- [Logos and custom lettering](../identification/logos-and-custom-lettering.md)
- [Client handoff licensing](client-handoff-licensing.md)

Compiled 2025 as part of the Fontlore project.
