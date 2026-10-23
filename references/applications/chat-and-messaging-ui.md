# Chat and Messaging UI

What this reference covers: Typography for chat and messaging interfaces: small-size legibility in bubbles, metadata and timestamps, emoji handling in font stacks, the case for system fonts, and the mixed-script and RTL realities of real conversations. Chat is the most intimate text surface in software: users read it constantly and notice everything.

## Bubble typography

- Message body: 14 to 15 px (16 px is comfortable, 13 px is the floor for dense products); weight 400, line-height 1.35 to 1.45. Chat text is read in volume at arm's length; do not shrink it below your product's floor.
- Bubbles size to content with padding, not fixed heights; long messages wrap within a max-width (roughly 60 to 70 percent of the viewport) and the measure rules from long-form reading apply loosely at small sizes.
- Links inside messages: underlined and colored with full contrast; link previews reflow around them.
- Code, paths, and technical strings in chat: monospace with a background chip; this is where a mono face earns its place in a messaging product.
- Grouped messages: consecutive messages from one sender tighten spacing; a new sender block gets a gap. The rhythm is typographic even when the model is temporal.

## Metadata, senders, and system lines

- Timestamps and read receipts: 11 to 12 px, tabular figures, secondary contrast passing 4.5 to 1 (metadata at 3:1 is the most common contrast miss in chat UIs).
- Sender names in groups: 12 to 13 px, weight 500 or 600, colored per participant only as reinforcement, never as the sole identity signal.
- System and event lines ("Today", "Alice joined"): 11 to 12 px, centered or left, distinct style; tracked uppercase works for very short system words but check contrast and length.
- Unread indicators, typing indicators: pair any color with a label or icon; color alone fails the basic accessibility rule and confuses new users.

## The system font argument

Chat is the strongest case for system fonts:

- Zero font payload on the surface users spend the most time in; chat apps are performance-sensitive and battery-sensitive.
- Native feel: SF Pro on Apple platforms, Roboto on Android, Segoe UI on Windows; users perceive the chat as part of the OS.
- Emoji, multilingual input, and system text features (dynamic type, magnification) integrate for free.
- The stack: -apple-system, "Segoe UI", Roboto, system-ui, plus per-script fallbacks the OS provides automatically.

The counter-case: brand differentiation and cross-platform consistency, which a webfont buys. Many chat products accept the system look for body messages and use a brand face only for headings, empty states, and onboarding.

## Emoji and special characters

- Emoji come from platform fonts (Apple Color Emoji, Segoe UI Emoji, Noto Color Emoji); never force your own emoji font for user content, and ensure the stack lets them resolve (put text fonts first; emoji codepoints fall through automatically).
- Emoji presentation selectors (the variation selector that forces text versus emoji presentation of symbols like the heart) exist; test symbol-plus-emoji sequences rather than assuming.
- Cross-platform differences are a fact: the same emoji renders differently per OS; do not promise pixel parity, and do not render skin-tone or ZWJ sequences (family, flag compositions) without testing; ZWJ sequences are the classic partial-support failure.
- Reactions, stickers, and GIF overlays sit outside text flow; keep them from resizing bubbles.

## Mixed script and RTL conversations

- Real conversations mix scripts, names, and directions: a message in Arabic next to one in English in the same thread. Per-message dir="auto" (first strong character decides) is the standard behavior; bubble alignment follows the direction, which means Arabic bubbles hug the right edge with mirrored tails.
- User names in Latin script inside RTL metadata lines: wrap in bdi to stop bidi leaks.
- The system font stack handles most scripts via OS fallback; if the product self-hosts fonts, the mixed-script fallback planning applies in full.
- Input fields: 16 px on iOS to prevent zoom-on-focus; the compose field is the most-used input in the product.

## Common mistakes

- 11 px timestamps at gray 3:1 contrast, unreadable for anyone over 40.
- A custom display face for message bodies: personality where legibility was the job.
- Forcing a bundled emoji font and shipping broken or outdated emoji where the OS had perfect ones.
- Fixed bubble widths chopping long words and URLs; use overflow-wrap and let bubbles grow.
- No dir handling, so Arabic messages align left with Latin punctuation floating wrongly.
- Notification text rendered in a different type than the chat, or in a face the OS cannot render, so notifications show tofu.

## Decision rules

- Default to the system stack for message bodies; add a brand face only for non-conversational surfaces.
- Metadata: 11 to 12 px, tabular figures, full contrast; metadata is information, not decoration.
- Every bubble: content-sized, max-width capped, dir="auto", overflow-wrap safe.
- Emoji: platform fonts, tested ZWJ sequences for your markets, no bundled emoji for user content.
- Any new language launch: re-run the chat-specific checks (bubble alignment, compose input, notifications) with real conversations, not sample strings.

## Comparison table: font strategies for a chat surface

The font decision for chat is a strategy decision first and a family decision second:

| Strategy | Payload | Where it shines | Main risk |
| --- | --- | --- | --- |
| System stack (SF Pro, Segoe UI, Roboto) | zero | consumer chat, performance-sensitive surfaces | no cross-platform parity; the brand is invisible |
| One webfont, two weights (Inter, Source Sans 3) | one subsetted file | branded support widgets, in-app chat in a SaaS product | payload policing; host-page CSP can block the font |
| Hybrid: system body, brand face for chrome | one small subset | products needing brand presence without chat payload | two voices need rules or they read as drift |
| Self-hosted per-script families | highest | markets where OS fallback fails the script | fallback chains, shaping tests, RTL verification |

- The big three system faces all support tabular figures, so timestamps align even on the zero-payload path.
- A webfont for chat is subsetted to the scripts actually served; a bundle with eleven scripts is a maintenance burden, not a feature.
  - Two weights (400 body, 600 names) cover almost every chat UI; add 500 only if the design system already uses it.
- Support widgets live inside other people's pages: design so a blocked font load degrades to the system stack with zero layout breakage.
  - The document.fonts API gives a load signal; a one-line fallback check beats discovering the fallback from a screenshot.
- Emoji always resolve from platform fonts; the custom text font must never sit before the emoji fonts in the stack.
- One mono face (JetBrains Mono or IBM Plex Mono) covers code and error chips in technical chat; 12 to 13 px on a tinted background.
- RTL planning belongs to the font decision: per-message dir="auto" is behavior, but a self-hosted family must still shape Arabic or Hebrew correctly.
- Chat notification text renders with OS styling no matter what the app ships; do not spend brand budget there.
- One-time-code and password fields linked from chat flows read better in mono input styling; six digits at 16 px mono parse in one glance.

## Worked example: an embeddable support chat widget

Scenario: a B2B SaaS ships an embeddable support widget that runs inside customer pages, where its script is third-party, every kilobyte is argued over, and content security policies vary by host.

- Message body: the system stack at 14 px, line-height 1.4, weight 400; the widget renders hundreds of short messages per session and the native face keeps it fast and familiar.
- Sender names: 12 px at weight 600; agent names carry a team label word, never color alone.
- Timestamps: 11 px, secondary color at 4.5 to 1 contrast, tabular figures via font-variant-numeric so stacked timestamps align.
  - Read receipts share the line; their state words ("Sent", "Seen") are fixed strings with reserved room, so the bubble edge does not breathe.
- Code and error strings: JetBrains Mono at 12 px on a tinted chip with a copy affordance; the one bundled font, and it earned its bytes.
- Brand presence: Inter carries only the header, greeting, and CTA, loaded as one Latin subset covering two weights (400 and 600).
  - CSP defense: the widget listens for the font load promise and silently stays on the system stack when a host blocks the file.
- Compose field: 16 px on iOS to prevent zoom-on-focus; the placeholder matches the message size so nothing jumps.
- Bubbles: content-sized with a max-width of 70 percent of the panel; overflow-wrap: anywhere keeps long URLs inside their bubbles.
- Grouping: consecutive messages from one sender tighten to 2 px; a new sender block gets 12 px. The rhythm is typographic even though the model is temporal.
- Unread badge: a count in tabular figures at 11 px on the accent color, contrast checked against the accent, not against white.
- Typing indicator: three dots plus the name at 12 px; the name renders in the sender style so attribution stays consistent.
- RTL: dir="auto" per message; Arabic canned replies tested with Latin product names wrapped in bdi elements.
- Rejected: a brand display face for message bodies (personality where legibility was the job) and a bundled emoji font (the OS already had newer, better ones).
- Result: one small font file, clean CSP audits across hosts, and a chat that reads native on every platform.

## Field notes

- Timestamps are the most-read text in chat and the most under-designed; align them, contrast them, stop treating them as decoration.
- Metadata at 3 to 1 gray is the most common contrast miss in chat; it fails for anyone over 40 and for every low-vision user.
- Grouping rhythm does more for scannability than any typeface change; tighten within a sender, space between senders.
- Long URLs are the stress test: overflow-wrap plus max-width keeps bubbles intact, and default word-break rules chop words mid-syllable.
- Emoji-only messages render at implicit larger sizes on some platforms; test reaction rows and reply quotes around them instead of fighting it.
- Dark mode flips chat surfaces fast; the timestamp gray that passed on white usually fails on near-black, so verify both.
- Edited and ephemeral states append words to metadata lines; reserve the room instead of reflowing the timestamp.
- Link previews pull titles at 13 to 14 px and descriptions at 12 to 13 px; cap each at two lines or the preview outweighs the message.
- Multi-tenant embeds inherit host fonts by accident; set font-family explicitly on every text node in widgets.
- Search results render message snippets at metadata sizes; the same tabular and truncation rules apply there.
- The compose field is the most-typed-into box in the product; the iOS 16 px rule is not negotiable, and the zoom it prevents looks like a bug.
- Dynamic type and OS font scaling resize bubbles live; test at maximum accessibility sizes before shipping.
- Voice notes and attachment captions follow metadata styling; invent no new style for them.
- Mobile keyboards produce smart quotes; never run a replace-all that mangles user content to keep a specimen look.
- Notifications inherit the OS, so a face the OS cannot render shows tofu on the lock screen; system fonts there are a correctness choice.
- Reaction chips and sticker rows sit outside text flow; keep them from resizing bubbles or shifting baselines.
- Unread counts, badges, and drafts all want tabular figures; counters that change width on every update read as jitter.
- The strongest chat type systems are boring: one body style, one metadata style, one mono chip; personality lives in chrome, not conversations.

## Quick reference: chat numbers that hold up

- Message body: 14 to 15 px, weight 400, line-height 1.35 to 1.45.
- Sender names: 12 to 13 px, weight 500 to 600.
- Timestamps and receipts: 11 to 12 px, tabular figures, 4.5 to 1 contrast.
- System lines: 11 to 12 px, short strings, distinct style.
- Code chips: 12 to 13 px mono on a tinted background with copy.
- Bubble max-width: 60 to 70 percent of the viewport.
- Grouping: tight within a sender, a clear gap between senders.
- Compose input: 16 px on iOS to prevent zoom-on-focus.
- dir="auto" on every message; bdi around user names in mixed-direction lines.
- Emoji from platform fonts; test ZWJ sequences for your markets.
- Weight budget: 400 body, 500 or 600 names; stop there.
- Timestamps absolute when precision matters; relative strings only where width changes are harmless.
- Metadata contrast checked in light and dark themes.
- No bundled emoji font for user content, ever.
- Fallback rule: if the webfont fails, the system stack must look intentional, not broken.
- New-language launches re-run the bubble, compose, and notification checks with real conversations.

## Cross-references

- [Web and SaaS interfaces](web-and-saas-interfaces.md)
- [Mixed script fallbacks](../scripts/mixed-script-fallbacks.md)
- [Dynamic type and preferences](../accessibility/dynamic-type-and-preferences.md)
- [Localization and RTL accessibility](../accessibility/localization-and-rtl-accessibility.md)

Compiled 2025 as part of the Fontlore project.
