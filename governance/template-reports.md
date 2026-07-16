---
name: template-reports
id: 20260618T120018Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: link
links: []
---

# Report Template -- How We Write Reports

A report is a finished piece of cross-examined research. Unlike a library
topic (single-agent, single-pass), a report has been through at least one
independent evaluation pass. It represents the system's best answer to a
research question at the time of writing.

## Global Formatting Rules

The entire GitHub org is plain 7-bit ASCII, lowercase, hyphen-delimited.
These rules are non-negotiable. CI enforces them.

- **ASCII-only:** Every character in every file is 7-bit ASCII (U+0000
  through U+007F). No emoji, no smart quotes, no Unicode dashes or
  arrows, no accented letters. The `ascii-guard.yml` CI gate fails the
  build on any violation.
- **Lowercase only:** All filenames, slugs, tags, domains, and folder
  names use lowercase exclusively. No CamelCase, no UPPERCASE, no
  mixed case.
- **Hyphens, not underscores:** Use hyphens (`-`) to separate words in
  filenames, slugs, and tags. Never use underscores (`_`).

## Frontmatter

```yaml
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>           # ISO 8601 UTC, permanent, never reused
tier: core-report                 # always core-report
lock: approval-required
approved_by: pending
author: <link|ava|zelda|suggi|luffy>
evaluated_by: [<agent>, <agent>]  # agents who independently evaluated
status: <draft|evaluated|complete>
tags: [<tag>, <tag>]
links: [<relative-brain-path>]
---
```

## Naming Convention

Files are named: `<short-slug>.md`

- `short-slug` -- kebab-case, max 60 chars, unique.

Example: `inter-agent-cooperation-research-2026-06.md`

## Body Structure

### Executive Summary
*What is the answer in one paragraph?*

- State the research question and the answer.
- Summarize the key evidence (one to two sentences per major finding).
- State the confidence level.
- This section must stand alone. A busy reader should get the full
  picture from this section only.

### Research Question
*What exactly were we trying to find out?*

- State the question as a falsifiable claim or an open question.
- Define scope: what is in, what is out.
- State why this question matters.

### Methodology
*How did we investigate this?*

- Describe the approach: literature review, data analysis, model
  comparison, experiment, expert consultation.
- List sources consulted (with retrieval dates).
- State limitations: what this methodology cannot tell us.

### Findings
*What did we discover?*

- Structure findings by theme or by evidence source.
- Each finding: claim, evidence, confidence.
- Include negative results (what we looked for and did not find).
- Use tables, charts (ASCII art), or structured lists for quantitative
  findings.

### Discussion
*What does it mean?*

- Synthesize findings into a coherent narrative.
- Address contradictions or surprises.
- Compare against prior knowledge in the brain.

### Conclusion
*What is the final answer?*

- Restate the research question and the answer.
- One actionable recommendation.
- Open questions for future research.

### Evaluation History
*Who reviewed this and what did they find?*

- List each evaluation pass: evaluator, date, verdict, key changes made.
- Link to the evaluation files.

## Cross-Links

Link to:
- The evaluations that reviewed this report.
- Related reports, proposals, or insights.
- Library topics referenced in the findings.
- The IORs that triggered this research.

## Quality Gates

Before marking `status: complete`:

- **Evaluated:** At least one independent evaluation pass (PASS or
  APPROVE WITH CHANGES resolved).
- **Executive summary stands alone:** A reader can get the answer from
  the summary alone.
- **Methodology is explicit:** Another agent could reproduce the
  approach.
- **Negative results included:** What was NOT found is as important as
  what was.
- **Cross-linked:** Links to evaluations, related reports, and library
  topics.
- **ASCII-only:** Zero non-ASCII characters.
- **Lowercase + hyphens:** Filename follows the convention.

---

*Last updated: 2026-07-16 by link + ava.*
