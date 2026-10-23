# Support

## Where to ask what

- GitHub Discussions (Questions category): how to use the skill, how to read the data, how to interpret a decide.py result, and general typography questions. Start here for anything that is not a confirmed bug.
- GitHub Discussions (pairing and identification help): stuck pairing a shortlist, or trying to identify a font from a screenshot? Ask with your constraint sheet (scripts, license scope, context) or your specimen image details. Maintainers and contributors answer when they can; there are no guaranteed response times.
- GitHub Issues: confirmed bugs in the code (decide.py, validate.py, build_data.py, CI) and data problems. Use the provided forms:
  - Bug report: something in the scripts or templates does not work as documented.
  - Data correction: a wrong or stale value in the data layer, with an evidence URL.
  - New font / new tool: additions with verifiable metadata.

## Before opening an issue

- Run the validator: python3 scripts/validate.py. If it fails, the error message usually names the file and the rule.
- Check the counts: if a number in the docs disagrees with the data files, that is a data-correction issue with the JSON as evidence.
- For decide.py surprises, include the exact command and the full output. The tool is deterministic; your run is reproducible.
- For pairing questions, state the constraints you already applied (project type, script, tone, license) so answers can build on them instead of restating them.
- For identification help, include where the image came from and which tools from the identification references you already tried, so nobody repeats dead ends.

## Self-service reading order

Many questions are already answered in the repository, in this order:

1. SKILL.md: the 8-step agent workflow and the data schema.
2. MASTER-SKILL.md: the scoring rubric, the stages, the worked example, and the edge cases.
3. references/workflow/brief-to-constraints.md: how to turn a brief into constraints.
4. The category that matches your problem: licensing for rights questions, scripts for coverage questions, technical for loading and performance, identification for "what font is this".
5. The repository map in SKILL.md, if you are unsure which file holds the thing you are looking for.

## What this project is not

- Not a font foundry: we do not host, license, or modify font files.
- Not legal advice: the licensing references are operational summaries; verify at the foundry source before shipping.
- Not a paid support channel: everything here is community-maintained under MIT.
- Not a font identification oracle: identification help in Discussions expects the image details you already checked; the identification category references list the tools and the verification steps.
- Not a marketplace: tools in tools.json are listed for reference; access models and prices can change upstream, so check the tool's own page.

## Response expectations

Issues and pull requests are triaged by the maintainers (@izynu, @xhraddha) on a best-effort basis, typically within a week, without a formal SLA. Discussions may take longer. If a topic is stalled, a polite follow-up with new information is more effective than a bump. Security-sensitive reports never go through these channels; see SECURITY.md for the private reporting path.
