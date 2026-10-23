# Identifont Decision Tree

What this reference covers: How to identify a typeface from memory or description using Identifont's question-based approach: when to use it, how its question paths work, how to answer letterform questions accurately, and how to convert its output into verified candidates.

When there is no image, only a memory of "that serif with the funny g", automated identifiers are useless. Question-based identification is the tool for that situation, and it is also excellent training for reading letterforms deliberately.

## When there is no image

- Someone describes a font from a remembered poster, book, or old website; the artifact is gone but the impression remains.
- A stakeholder asks for "something like the font in that banking ad" with only a screenshot from memory to offer.
- You can see the font in the real world but cannot capture it (signage behind glass, a bus going past): note the answers to the key questions on the spot.
- In all these cases the workflow inverts: instead of pixels feeding a matcher, your observations feed a question tree, and your honesty about uncertainty determines the outcome.

## How Identifont works

- Identifont offers several identification modes: the main decision tree of yes/no questions, identification by similarity to a named font, by designer or publisher, and by name partials.
- The main tree asks about structural features in a designed order: serif or sans first, then weight, width, and the shapes of specific letters.
- Each answer prunes the candidate space; the tree ends with a short list of families matching all answers.
- The question order is pedagogically useful: it teaches which features actually discriminate between families, in contrast to the vague adjectives most people use.

## Answering letterform questions well

- The g question is usually first or near first: single-story (like Futura) or double-story (like Times)? Answer from memory of the actual shape, not from genre assumption.
- The a question follows the same logic: double-story a is the norm in serifs; geometric sans faces often use single-story forms.
- Questions about R (straight or curved leg), Q (tail shape), G (spur or no spur), and terminals (ball, beak, sheared) require recalling details most people never consciously saw.
- When genuinely unsure, choose the "not sure" option if offered rather than guessing; a wrong answer prunes the correct font silently.
- If the memory is fuzzy on everything, identify by similarity instead: name a well-known font it resembles and let the similarity mode generate candidates.

## Converting output into candidates

- The result list is a candidate set, not an answer: pull specimens for each and compare against the remembered features.
- Search the candidates on Fonts In Use and in foundry catalogs; seeing the font used in context often triggers recognition that specimens alone do not.
- For shortlisted candidates, run the standard verification: diagnostic letters, metrics impression, era plausibility (a font released in 2015 cannot be the 1998 poster).
- Feed any surviving candidate into the normal identification documentation workflow with an honest confidence level; memory-based identification rarely rises above "probable".

## Training value

- Running the tree on fonts you know (test yourself on Helvetica, then on Garamond) calibrates your eye and reveals which features you misjudge.
- The question vocabulary (terminals, apertures, spur, tail, stress) transfers directly to manual letterform analysis; learn it once and use it everywhere.
- Teams that run the tree together converge on shared vocabulary, which shortens future reviews.

## Workflow

1. Write down every verifiable fact first: era, medium, brand context, serif or sans, weight impression.
2. Run the Identifont tree, answering honestly and using "not sure" freely.
3. Take the resulting shortlist to specimens; compare the remembered features one by one.
4. Search Fonts In Use for each plausible candidate to test recognition in context.
5. Verify the survivor at the foundry, then document with a confidence level appropriate to memory-based evidence.

## Common mistakes

- Guessing at letterform questions instead of admitting uncertainty; the tree punishes confident wrong answers.
- Assuming the first result is the answer without specimen comparison.
- Using the tree when an image exists; automated tools on pixels beat memory on pixels.
- Confusing designer memory with font memory ("it was a Frutiger-like thing" is a similarity answer, not a tree answer).
- Forgetting era constraints and shortlisting fonts that did not exist when the artifact was made.

## Decision rules

- Image available: use image tools; the tree is for memory and description only.
- More than half the answers are "not sure": switch to similarity mode or gather better observations.
- The tree's shortlist contains fewer than three families: verify each thoroughly before expanding the search manually.
- Memory-based identification never ships without an explicit "probable" or lower confidence marking in the record.

## Comparison table

Identifont's identification modes and when each applies:

| Mode | You provide | Best when | Watch out for |
| --- | --- | --- | --- |
| Main decision tree | Yes or no answers about letterform features | A real memory of shapes exists | Confident wrong answers prune the truth silently |
| By similarity | The name of a font it resembles | "Like Frutiger but warmer" is all you have | The anchor drives the whole list; choose it with care |
| By designer or publisher | A designer or foundry name | The attribution memory is strong | People remember shapes far better than credits |
| By name partials | A fragment of the name | A brand or file name survived | Partials bury the true candidate among near neighbors |

The modes stack: run the tree for structure, then similarity mode to widen the net when the shortlist feels wrong. No mode verifies anything; every output is a candidate list that owes you specimens, an era check, and a confidence tier.

Mode choice is itself evidence about your memory. A stakeholder who answers tree questions fluently has a real visual memory; one who can only produce adjectives ("clean", "modern", "friendly") should be routed to similarity mode immediately, because tree answers built from adjectives are genre guesses in disguise.

Era matters more here than anywhere else in identification: a candidate that did not exist when the artifact was made is not a candidate, no matter how well it fits the description. Collect the artifact's date, medium, and market before the first question.

Budget the questions too: every "not sure" spends one, and a tree run where half the answers are guesses is not a run at all. Ten honest answers beat thirty guessed ones every time.

## Worked example

A stakeholder remembers a 2003 annual report cover: "a friendly serif with big old-style numerals". No file survives. The tree, run honestly:

1. Serif or sans: serif, moderately heavy.
2. Contrast and serifs: moderate contrast, sturdy bracketed serifs; nothing hairline, nothing slab-like.
3. Width: normal, not condensed; the memory insists the cover "felt calm, not squeezed".
4. g question: double-story, remembered clearly because the lower loop looked generous.
5. Numerals: old-style by default; the 3 and the 5 descended below the baseline in the remembered image.
6. x-height: large, "almost sans-like" in the stakeholder's words.
7. Terminals and stress: not sure; answered honestly rather than guessed.

The shortlist comes back led by Georgia, with several book serifs behind it. The era check decides: Georgia shipped with core web fonts and Microsoft products from 1996, so a 2003 report could plausibly use it, and Georgia's signature default old-style numerals match the memory's strongest detail. Merriweather, whose large x-height also fits the profile, dies on era alone: it did not exist until 2011. Confidence lands at probable, the honest ceiling for memory-based identification, and the record names its own confirmation bar: finding the artifact itself.

What kept the case honest: the stakeholder used "not sure" once instead of performing confidence; the strongest memory detail outweighed the vaguest; and the era check eliminated a candidate that two glyph impressions would have waved through.

A second case, similarity mode, because the tree failed: a designer remembers a 2010s tech blog's body face as "Roboto but friendlier", and half the tree answers are "not sure". Roboto goes in as the similarity anchor, and the returned neighbors are all open humanist sans faces. The break comes from context instead of letterforms: an archived copy of the blog settles it, because the page CSS declared Source Sans Pro from Google's serving all along. Confidence: confirmed, and the record notes the lesson plainly, that a forced tree run is worth less than an honest similarity anchor plus a provenance check.

Both cases share the same ending: outputs converted into candidates, candidates verified against evidence that exists outside anyone's memory, and a confidence tier that admits what the method cannot prove.

The first case run carelessly, for contrast:

- Contrast guessed as "high, probably" because the stakeholder wanted to sound helpful; the shortlist fills with didones and loses Georgia.
- Numerals answered as lining because old-style "seems unlikely for a corporate report"; the single strongest memory detail gets discarded.
- Era skipped because the tree feels authoritative; Merriweather survives and steals the case on the strength of a large x-height.

## Field notes

Observations from running the tree on real memory-based cases:

- People remember the serif-versus-sans split and the g form best; terminals and stress are almost never consciously seen. Ask the g question early and let it anchor the rest.
- Numerals are underrated anchors: old-style versus lining, a flagged 1, an open 4. Anyone who noticed a numeral detail noticed something reliable.
- The tree punishes genre assumptions. Someone who "knows" it was a geometric sans will answer the a question from the genre, not the memory; have them sketch the letter from memory first.
- Similarity mode with a well-chosen anchor (Helvetica for grotesques, Frutiger for humanist sans, Garamond for old-style serifs) beats a half-guessed tree more often than not.
- Treat "bold-ish" as a range, not a value; false precision on weight prunes real candidates.
- Write down every answer with its certainty level; when the shortlist fails, the least-certain answer is the first one to flip.
- Run the tree on fonts the team knows (Helvetica, then Garamond, then Inter) as a calibration exercise; it trains the vocabulary and exposes which features everyone misjudges.
- Attribution memory is the least reliable input; "it was a Frutiger thing" is a similarity answer and should route there directly.
- When two tree runs disagree (same person, different day), believe neither; the honest conclusion is that the memory is not load-bearing.
- Regional and market context prune hard: a face sold only in one country's domestic market is unlikely on another country's poster.
- Timebox memory-based hunts; forty minutes of tree and similarity usually exhausts what memory can give, and beyond that only the artifact itself moves the case.
- Old samples favor old candidates: the longer ago the artifact, the more the shortlist skews toward classics, and a modern hit list is usually a sign of bad answers.
- Devices corrupt memories: what someone remembers from a low-resolution phone photo of a poster is the rendering, not the typeface; ask where and how they saw it.
- Composite memories are the hardest cases: two similar fonts remembered as one; when a description contradicts itself mid-sentence, suspect a blend and split it.

## Quick reference

The question sequence that matters, with anchor examples that keep answers honest:

1. Serif or sans: the first split; wrong here and everything downstream is noise.
2. Contrast: near-monoline, moderate, or extreme; Futura, Georgia, and Playfair Display span the range.
3. Weight and width: heavy or light; condensed, normal, or extended.
4. g: single-story like Futura or double-story like Georgia; the single most discriminating question.
5. a: single-story or double-story; finished with a tail or clean.
6. R: straight, kicked, or curved leg.
7. G: spur or no spur.
8. Q: tail inside, outside, straight, or curled.
9. Terminals: ball, beak, sheared, or flat cuts.
10. Numerals: lining or old-style; the 1 flagged or bare; the 0 narrower than the O or not.

Answer rules: answer from the remembered shape, never from the genre; use "not sure" freely and record where you used it; and treat every answer as a claim you will defend at specimen time. Run the sequence on paper before opening any reference site; the discipline is writing answers down, not knowing them.

When the shortlist comes back empty, do not answer harder: loosen the two least-certain answers and re-run, or switch to similarity mode. And when it comes back huge, tighten the answers you were most sure about; a list of forty families means the tree learned nothing.

## Cross-references

- [Manual letterform analysis](manual-letterform-analysis.md)
- [Identification workflow overview](identification-workflow-overview.md)
- [Verifying an identification](verifying-an-identification.md)
- [Documenting identification results](documenting-identification-results.md)

Compiled 2025 as part of the Fontlore project.
