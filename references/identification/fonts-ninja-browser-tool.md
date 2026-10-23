# Fonts Ninja Browser Tool

What this reference covers: How to use the Fonts Ninja browser extension to inspect typography on live web pages, what it can and cannot tell you, and how to fold its output into identification and audit workflows. It reads the DOM, and knowing that changes how you trust it.

Fonts Ninja answers a different question than image-based identifiers: instead of "what is this shape?", it asks "what did the website declare?". Both questions matter, and confusing them produces confident errors.

## What the extension does

- Hovering text with the extension active shows the font family in use, the rendered weight, font size, line height, and letter spacing, plus color values for text and background.
- Clicking through exposes the full font stack and, for many fonts, links to the foundry or marketplace page where the family can be licensed.
- It aggregates page-level views: you can sweep a site and collect which families, weights, and sizes are used where, which makes it a fast reconnaissance tool.
- A color picker and style summary make it useful beyond type, but the font inspection is the reason typographers keep it installed.

## The critical limitation: it reads declarations

- The extension reports CSS-computed values, not glyph shapes. If the site declares "Futura" but the visitor's machine lacks Futura, the rendered face is a fallback, and Ninja may still report Futura.
- Webfonts served under renamed files or obfuscated family names can be misreported or reported as generic families.
- Custom lettering rendered as SVG, images, or canvas is invisible to it; wordmarks and logo lockups will not show up at all.
- Variable fonts may report the axis defaults rather than the animated or clamped values in play.
- The lesson: Ninja is a read of intent (what the CSS asks for), while identification tools read of fact (what the pixels show). Verify anything load-bearing against rendered specimens.

## Using it for reconnaissance

- On a competitor or reference site, sweep the homepage and two or three interior pages; record family, weights, and sizes per role (headings, body, buttons).
- Note the pattern of a real system: consistent weight usage, sensible size scale, and a mono or serif accent where the brand needs one.
- Compare declared stacks across breakpoints; switching families on mobile is a common smell.
- Where the site serves actual webfonts, the declared family is usually genuine; where it relies on system stacks, what renders locally may differ from what renders for you.
- Screenshot the panel output alongside the page; the pairing is useful evidence in research notes.

## Using it for identification leads

- When a site uses a webfont, Ninja's family name plus weight is usually the correct identification; verify at the foundry and match a specimen against the page visually.
- When the family name is a renamed webfont (some CDNs rename), fall back to image-based identification on a screenshot of the rendered text.
- Ninja's marketplace links speed up the license and purchase path once identity is confirmed.
- For fonts behind authentication or apps, browser inspection does not apply; return to screenshot workflows.

## Auditing your own site

- Run Ninja over your own product pages to verify that the fonts you think are shipping are the fonts actually declared.
- Catch stack mistakes: a forgotten fallback causing system font rendering, or a condensed weight applied where the design expected regular.
- Check that declared weights match the design tokens; drift here is invisible in code review and obvious in Ninja's panel.
- Combine with performance thinking: Ninja shows which weights are in use, and unused declared weights are wasted bytes.

## Workflow

1. Install the extension in a dedicated browser profile for research work.
2. Sweep the target pages; record family, weight, size, and line-height per role.
3. Distinguish declared families from system-font fallbacks; treat the latter as unknowns.
4. Verify webfont identities against foundry specimens.
5. For anything commercial, follow the foundry link to pricing and license scope.
6. Log findings in the research record with page URLs and dates.

## Common mistakes

- Trusting a declared family name when the rendered glyphs are clearly a fallback.
- Assuming Ninja can identify lettering inside images, logos, or SVG.
- Copying a competitor's font sizes and spacing wholesale instead of understanding the system behind them.
- Reporting "the site uses X" without checking whether X is a webfont or an aspirational stack entry.
- Using it as the sole identification step for anything that will be purchased or embedded.

## Decision rules

- Webfont confirmed (files load, glyphs match): Ninja's answer is reliable enough to act on.
- System stack declared: treat the identification as unresolved; screenshot and run image tools.
- Lettering lives in images or SVG: Ninja cannot help; switch to the image workflow.
- For audits, Ninja is the fastest first pass, but token and code review remain the source of truth.

## Comparison table

Where Fonts Ninja sits against the pixel-based identifiers and the font-file inspectors:

| Tool | Input | What it actually reads | Blind spot |
| --- | --- | --- | --- |
| Fonts Ninja | Live web page | CSS declarations and loaded font files | Images, SVG, canvas, and system-fallback situations |
| WhatTheFont | Image crop | Glyph shapes against MyFonts inventory | Lettering not sold there; drawn or distorted type |
| Matcherator | Image crop | Glyph shapes against Fontspring and free catalogs | Connected scripts; texture; foundry-only inventories |
| WhatFontIs | Image crop plus corrections | Shapes guided by human transcription | Result quality is capped by correction quality |
| Wakamai Fondue | A font file | Name table, axes, and features inside the file | Says nothing about where the file came from |
| Identifont | Memory or description | Question-tree pruning with no image needed | Answers are only as honest as your memory |
| Fonts In Use | Search terms | Documented real projects with typeface credits | Absence proves nothing for obscure work |

The pairing habit falls straight out of the table: Ninja tells you what the site asked for, the image tools tell you what the pixels show, and Fondue tells you what a downloaded file contains. A load-bearing identification wants at least two of those answers to agree.

Treat disagreements between declaration and pixels as findings, not noise. A page that declares Roboto but renders Arial is a bug in someone's stack, a failed webfont load, or an obfuscated file, and each of those is worth more in your notes than a clean read would have been.

One more entry for the kit: when a site serves a single bundled woff2 under a generic name, download it where the license permits and drop it into Wakamai Fondue. The name table inside usually ends the renaming debate in one screen.

## Worked example

Reconnaissance on a competitor's marketing site, twenty minutes with the extension active:

- Homepage hero: the panel reads one family at weight 700 with tight letter spacing; the network tab shows the matching woff2 files loading, so the declaration is real.
- Body copy: the declared stack ends in Georgia and generic families, but only system files render locally; the body face is an unresolved unknown, and the record says so.
- Blog templates: a second sans appears from the same stack on mobile breakpoints, a smell worth flagging in the research notes.
- Wordmark: an SVG logo shows nothing in the panel; it routes to the lettering workflow instead of wasting a tool run.
- Pricing page: weight 300 declared where the text renders visually regular; either a variable axis default or a broken declaration, noted for verification.
- Buttons and labels: the same family as body copy but with positive letter spacing; a real system pattern worth copying as a pattern, never as raw values.
- Footer legal text: a third family at a tiny size, which turns out to be the platform's default; distinguishing brand choices from platform defaults is half the value of the sweep.
- Data table: tabular numerals confirmed by aligning a column of prices; a small detail that says the family's feature set is being used well.
- Testimonial band: an italic serif appears that no other page uses; flagged as either a deliberate accent or a leftover template font, for verification either way.
- Mobile web: letter spacing tightens and line-height rises; responsive choices are part of the system map, not noise.
- Navigation labels: the same family as headings but wide-tracked at small size, and the pattern holds across pages; that is a system, not an accident.
- Output: a per-role table of family, weight, size, and line-height with URLs and dates, plus screenshots of the panel beside the page itself.

The deliverable is a map of intent, not an identification: every declared-but-unserved entry is marked unknown, every served webfont is queued for specimen verification, and the SVG wordmark is noted as artwork. The next agent inherits specific questions to verify rather than conclusions to trust, which is the difference between research and rumor.

The same extension pointed inward, as a quarterly self-audit:

- Sweep the production homepage and the app shell; confirm the declared families match the design tokens, name by name and weight by weight.
- A forgotten fallback shows up immediately as the system sans rendering one marketing page; the panel makes the drift visible without opening the code.
- Unused declared weights appear as bytes shipped for nothing; compare what the CSS requests against what the panel reports rendering.
- Animated variable font states read as their axis defaults; verify those with devtools and motion review rather than the panel alone.
- Findings go into the audit record with URLs and dates, exactly like competitor research; internal drift deserves the same paper trail.

Research outward, audit inward: same tool, opposite disciplines. Outward the panel generates leads to verify; inward it catches drift to fix. Both pay off only when their findings pass through the same verification and documentation workflows as any other identification.

## Signals to trust

- The panel shows a family and the network tab shows that family's woff2 or woff files actually loading; declared and served agree.
- The rendered glyphs match the family's official specimen on the details that matter: g form, R leg, terminal cuts.
- The same family and weights appear consistently across pages, breakpoints, and interactive states, which is what a real system looks like.
- The reported weight matches the visual weight on screen; a panel reading of 400 on clearly bold text means the declaration is broken, not that your eyes are.
- The extension's foundry or marketplace link resolves to a real listing for that exact family name at that weight.
- The site serves subsets and unicode-range splits consistent with a maintained webfont pipeline rather than a hand-uploaded file from 2009.
- A screenshot crop of the page run through WhatTheFont returns the same family the DOM declared; pixel evidence and metadata agree.
- The read is stable across a hard refresh, a second browser, and a return visit a week later; flaky reads mean fallbacks in play.
- Buttons and navigation render in the declared family even at extreme sizes, which fails fast when a fallback is secretly in use.
- The served weight set matches the design's visible range, with no phantom weights requested and no failed requests hiding in the network log.
- Hover and focus states swap weights coherently, which reads as deliberate typography rather than browser defaults.
- Trust compounds: one verified read that matched pixel evidence earns the next read the benefit of the doubt, never the first read itself.
- The family's variable axis values on an interactive page match what devtools shows when you force the same axis; two independent reads agree.
- The site's own style guide or design system page names the family, and the served files behave like it.

## Signals to distrust

- System stacks: Helvetica Neue, Arial, or Georgia in the panel may be nothing more than fallback entries in a font-family list, and what renders depends on the visitor's machine.
- Family names that exist at no foundry: renamed, subsetted, or obfuscated webfonts often carry service-specific names no catalog lists.
- A family that changes between desktop and mobile breakpoints without a design reason; at least one of the two reads is wrong.
- Anything inside images, SVG wordmarks, video, or canvas: the extension has no access to pixels CSS did not declare.
- Variable font readouts reporting axis defaults while the page animates or clamps weight, width, or optical size to other values.
- Text inside cross-origin iframes, embeds, and web components, which some inspectors do not traverse; absence of a read is not evidence of absence of a font.
- Self-hosted files under names like fonts/site-v2.woff2, where the file name says nothing and the family name may be renamed at the source.
- Your own browser state: developer overrides, reader modes, and font-blocking extensions change what renders and can make a healthy site look broken.
- Print stylesheets and email templates inherit nothing from the panel's read; what ships there is a different stack entirely.
- Cookie banners and embedded chat widgets render their own fonts and are not part of the site's system at all.
- A read taken while the page is still loading can catch the fallback before the webfont swaps in; wait for the network to settle.
- Screenshots of the panel are not evidence by themselves; pair every capture with the page itself and the date, or the note decays into rumor.
- A page rebuilt from a theme marketplace where the "family" is a theme preset with a marketing name, not a typeface name.
- An image proxy or optimization layer that serves pre-rendered text as images in some regions; the panel reads nothing because there is nothing to read.

## Cross-references

- [Identification workflow overview](identification-workflow-overview.md)
- [Verifying an identification](verifying-an-identification.md)
- [Logos and custom lettering](logos-and-custom-lettering.md)
- [Google Fonts Catalog](../sourcing/google-fonts-catalog.md)

Compiled 2025 as part of the Fontlore project.
