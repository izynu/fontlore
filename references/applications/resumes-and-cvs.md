# Resumes and CVs

What this reference covers: Typography for resumes and CVs: what applicant tracking systems actually parse, why structure outranks font choice, safe families and sizes, single-file PDF embedding, and the print-versus-screen question. The audience is dual (software first, humans second), and typography serves both differently.

## The ATS reality

Applicant tracking systems parse the text layer of your document into structured fields. Implications for typography:

- The font itself almost never breaks parsing; structure does. Multi-column layouts, tables, text boxes, headers/footers carrying contact details, and icon-based headings scramble the reading order and lose information.
- Standard section headings ("Work Experience", "Education", "Skills") help parsers; clever headings ("Where I Have Made an Impact") do not.
- Dates, titles, and companies as plain text lines with consistent formatting beat designed layouts where those relationships are encoded visually.
- Single column, top-to-bottom, real text: that is the whole technical requirement. The typographic quality budget should therefore be spent on legibility and hierarchy, not on layout gymnastics.

## Font choices that work

- Proven, widely installed, sturdy at 10.5 to 12 pt: Calibri, Arial, Helvetica, Georgia, Verdana, Cambria, Garamond-lineage faces. For PDFs with embedded fonts, any well-hinted face works, including Inter, Source Sans 3, IBM Plex Sans, or a text serif like Source Serif 4 or PT Serif.
- Size: body 10.5 to 12 pt; name 20 to 28 pt; section headings 12 to 14 pt with weight or small caps. One page at 11 pt beats two pages of 14 pt air for early-career candidates; seniority justifies length, not size.
- Hierarchy via weight and size only: 400 body, 600 headings, name at 700. Color, if any, one accent at full contrast; most resumes should be black on white.
- Avoid: display faces, thin weights (300 and below) which print and scan poorly, condensed faces that look cramped, and anything the reader's machine will substitute if fonts are not embedded.
- Consistency rules: one family, two weights, one size scale; resumes are read in 30 seconds and inconsistency reads as carelessness.

## The PDF: single file, real text, embedded fonts

- Export to PDF, never submit .docx-only when the system accepts PDF (and vice versa: some parsers prefer .docx; when in doubt, follow the posting's instructions).
- Real text layer: no image-based resumes, no text baked into headers as graphics; if copy-paste from the PDF returns garbage, so will the parser.
- Font embedding: exports from Word, Pages, InDesign, and LaTeX embed (usually subset) fonts by default; verify in the PDF properties that fonts show as embedded-subset. This guarantees your typography survives every viewer.
- File hygiene: single file, sensible filename (Firstname-Lastname-Resume.pdf), no password, no oversized assets; a resume PDF should be well under 1 MB.
- Test the output: open the PDF on another machine, copy-paste the text into a plain editor, and check the order and completeness; this five-minute test predicts the parser's view.

## Screen versus print

- Most first reads are on screen: optimize for that. Print copies are for interviews and career fairs.
- Screen: 11 pt body, generous line length control (a one-column A4/Letter page is already near the right measure), real bold for scanning anchors.
- Print: the same file should print cleanly; black text, no reliance on color for structure, margins at least 15 mm so nothing clips.
- If a printed version matters (academic CVs, design roles), print one copy on the actual printer before the interview; home-printer scaling is a real failure mode.
- Academic CVs follow different conventions (long, list-heavy, serif traditional); the parsing advice still applies, the aesthetic constraints loosen.

## Design roles: the exception that proves the rule

- Designers and typographers are judged on their documents' craft; a tasteful, typographically excellent one-column resume demonstrates skill without breaking parsers.
- The demonstration budget: type scale, spacing, and hierarchy; not custom letterhead layouts that scramble text order. Portfolio links carry the visual ambition; the resume stays parseable.

## Common mistakes

- Two-column templates from resume builders whose reading order interleaves columns line by line; the parser produces word soup.
- Contact details in the document header or footer, which many parsers skip entirely.
- Thin display faces at 10 pt failing both on screen and in print.
- Icon fonts or image glyphs for phone/email markers, replacing the parseable text.
- Fonts not embedded in the PDF, so the reviewer's machine substitutes and the layout reflows.
- Fake small caps or letter-spaced headings that survive rendering but garble plain-text extraction.

## Decision rules

- Default recipe: one column, one family (embedded), 400 and 600 weights, 11 pt body, standard headings, real text throughout.
- Any template choice: run the copy-paste test before submitting; it is the ATS in miniature.
- If the posting asks for .docx: provide .docx with an installed-safe font (Calibri, Arial, Georgia) and no exotic formatting; embedding does not apply the same way.
- Design-role exception: typographic excellence within the one-column parseable frame; ambition lives in the portfolio.
- Every version of the resume ships as a single PDF with verified embedded-subset fonts and a clean text layer.

## Comparison table: safe families and their clones

| Face | Class | Where it is installed | Watch-outs |
| --- | --- | --- | --- |
| Calibri | humanist sans | every Office install since 2007 | the .docx default look; open metric-compatible clone is Carlito |
| Arial | grotesque | universal on Windows and Mac Office | generic but never wrong; clone is Liberation Sans |
| Georgia | screen serif | universal | old-style figures by default, so dates vary in height |
| Verdana | screen sans | universal | runs large; use about 10 pt where you would use 11 pt |
| Cambria | serif | Office installs | lining figures; stiffer than Georgia |
| Helvetica | grotesque | macOS and print shops | Windows silently substitutes Arial |

- Carlito and Liberation Sans are the open metric-compatible clones: documents built with them keep Calibri and Arial line breaks on any machine, which matters for Linux and LaTeX workflows.
- For PDF resumes with embedded fonts, the installed-base question disappears; Inter, Source Sans 3, IBM Plex Sans, or Source Serif 4 all work because the file carries them.
- Georgia's old-style figures are a taste decision: charming in prose, wobbly in a column of dates.
- One family, two weights (400 and 600), one size scale; every extra font is a chance for inconsistency to read as carelessness.
- Avoid thin weights (300 and below) and condensed cuts: they print poorly, scan poorly, and substitute badly.
- If the posting demands .docx, the font must be installed-safe; embedding does not transfer the same way.
- Academic CVs relax the aesthetic constraints but not the parsing ones; serif tradition (Georgia, Cambria, Garamond-lineage faces) is safe there.

## Worked example: a mid-career engineer's resume

Scenario: an engineer with nine years of experience applies through a portal that accepts PDF; an ATS parses it, a hiring manager reads it on a laptop, and a panel prints it.

- Structure: one column, real text, standard headings ("Experience", "Education", "Skills"), dates as plain text lines; everything beyond that is decoration budget.
- Type: Inter embedded-subset in the PDF; body 11 pt at 1.35 leading, name 24 pt at 700, headings 12 pt at 600, company lines at 11.5 pt with titles at 600.
- Dates right-aligned with tab stops and tabular figures, so the column reads as a column; month names spelled consistently.
- Bullets as real list items with parallel phrasing; measurable results carry numbers in tabular figures.
- Contact block in the body, never in a header or footer; email and phone as plain text, not icons.
- Skills section as a plain list with consistent separators; skill bars and star ratings encode information that parsers and humans both misread.
- One accent color maximum, full contrast, used for section rules only; the resume stays black on white in print.
- .docx twin for the one portal that demands it: Calibri 11 pt, no tables, no text boxes, standard headings; maintained alongside, not converted at the last minute.
- Tests before sending: copy-paste into a plain editor (order and completeness intact), open on a second machine, print one copy, file size well under 1 MB.
- Rejected: a two-column template with a skills sidebar (reading order interleaves), icon fonts for contact markers (they garble extraction), and a 300-weight name (prints faint).
- Aftermath: the parser extracted every field, the manager's laptop rendered the embedded Inter, and the panel's printout matched the screen.

## Field notes

- The ATS reads the text layer; typography's job is keeping that layer clean and giving the human stage hierarchy.
- Headers and footers are where contact details go to disappear; contact info lives in the body.
- Multi-column layouts are the biggest single parser risk; simulate a sidebar with spacing, not columns.
- Consistent date formats beat clever ones; parsers and humans both pattern-match dates.
- Standard headings are extraction anchors; a synonym costs accuracy for zero aesthetic gain.
- Icon fonts replace parseable text with nothing; a plain label always wins.
- Letter-spaced or fake small-caps headings can garble plain-text extraction; test extraction, not just rendering.
- Some systems store only extracted text, so typography serves the humans of the later stages.
- A clean text layer is also what recruiters copy into their notes; garbled copy-paste garbles your record in their system.
- File hygiene: sensible filename, no password, no oversized images, one file per application.
- Portfolios and code links carry ambition; the resume demonstrates typographic restraint.
- For design roles, a one-column frame with excellent spacing is the demonstration; a poster resume is a portfolio piece, not a resume.
- Career changers: a 12 pt summary line in full contrast beats a banner; hierarchy tells the story.
- Some portals re-render PDFs as previews; open your own submission in their preview when offered.
- Keep the master in a format you can regenerate in five minutes; the resume that cannot be edited does not get edited.
- References and "available upon request" lines are wasted vertical space; cut them and give the room to results.
- Dense keyword blocks in white or near-white text fail contrast and read as gaming; keywords belong in real sentences.
- The 30-second read is the design brief: name, title, three anchors, and dates must survive a skim.

## Quick reference: the resume recipe

- One column, real text, standard headings, plain dates.
- PDF with embedded-subset fonts; .docx twin in Calibri or Arial when demanded.
- Body 10.5 to 12 pt (11 pt is the sweet spot); name 20 to 28 pt; headings 12 to 14 pt.
- Weights: 400 body, 600 headings, 700 name; nothing thinner than 400.
- One family, two or three weights, one size scale.
- Black on white; at most one accent at full contrast.
- Bullets as real lists; dates tabular and consistent.
- Contact details in the body, never header or footer.
- Copy-paste test before every submission.
- Print test on a real printer when an interview looms.
- Under 1 MB, sensible filename, no password.
- Display faces, thin weights, multi-column templates: rejected on sight.
- Install-safe faces for .docx: Calibri, Arial, Georgia, Cambria, Verdana.
- Standard heading words ("Experience", "Education", "Skills"); no synonyms.
- Embedded fonts verified in the PDF properties (embedded-subset), not assumed.
- Section order: contact, summary (optional), experience, education, skills; parsers expect the standard flow.
- One page for early career; two pages justified by experience, not by 14 pt air.
- Margins at least 15 mm so nothing clips in print.
- Real bold (600) for scanning anchors; color never carries structure.
- One date style for the whole document, spelled or numeric consistently.
- No layout tables; a skills table is the classic word-soup generator.
- Text boxes are invisible to many parsers; plain paragraphs only.
- LaTeX users: check the template embeds fonts and the metric clones (Carlito, Liberation) map correctly.
- The filename carries name and document type, not "final_v3".
- Tests rerun after every edit; a passing resume can fail after one layout tweak.

## Cross-references

- [Webfont formats](../technical/webfont-formats.md)
- [Presentations and slides](presentations-and-slides.md)
- [Contrast and hierarchy](../accessibility/contrast-and-hierarchy.md)
- [Common mistakes](../workflow/common-mistakes.md)

Compiled 2025 as part of the Fontlore project.
