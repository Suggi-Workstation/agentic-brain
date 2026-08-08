---
name: template-reports
id: 20260808T151846Z
tier: core-template
lock: approval-required
approved_by: pending
author: Link
links: []
---

# Report Template -- How We Write Reports

A report is a finished piece of cross-examined research. Unlike a library
topic (single-agent, single-pass), a report has been through at least one
independent evaluation pass. It represents the system's best answer to a
research question at the time of writing.

## Relationship to the write-report Skill

This file is the format specification AND the compliance validator. The
production procedure (clone, Feynman loop, write, commit, push, discard)
lives in `governance/skills/write-report.md`; that skill references
this file's Report Checklist as its format gate (R8: reference, never
duplicate). Keep the division: spec + checklist here, procedure there.

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

## The Report Checklist -- HARD GATE

Pre-commit gate: every item below MUST be confirmed. The file
MUST NOT be committed with any item unconfirmed. Do not include
this checklist in the published file.

- [ ] Frontmatter: all 6 fields present (name, id, tier, author, tags, links)  (PASS / HALT)
- [ ] name: lowercase kebab-case, matches filename slug  (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly; does not end in 000000Z (human-rounded = reject); never manually typed  (PASS / HALT)
- [ ] tier: "report"  (PASS / HALT)
- [ ] author: capitalized (e.g. Ava, Link, Researcher-1, Investor)  (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited, prefer existing brain tags  (PASS / HALT)
- [ ] links: relative paths from brain root; `brain:` prefix only for cross-repo references, omit for same-repo  (PASS / HALT)
- [ ] Executive Summary: research question + answer + key evidence + confidence; stands alone  (PASS / HALT)
- [ ] Research Question: falsifiable, scoped (in/out clearly stated)  (PASS / HALT)
- [ ] Methodology: reproducible, sources have retrieval dates, tools and parameters named, limitations stated  (PASS / HALT)
- [ ] Findings: each with claim + evidence + confidence  (PASS / HALT)
- [ ] Negative results: what was searched for and NOT found is documented  (PASS / HALT)
- [ ] Discussion: synthesizes findings, addresses contradictions and surprises  (PASS / HALT)
- [ ] Conclusion: restates question + answer + one recommendation + open questions  (PASS / HALT)
- [ ] Evaluation History: at least one independent evaluation linked (APPROVE or APPROVE WITH CHANGES resolved)  (PASS / HALT)
- [ ] Feynman pass completed BEFORE writing: blank page first  (PASS / HALT)
- [ ] Cross-links: evaluations + related reports + referenced library topics  (PASS / HALT)
- [ ] Version-history table: present (date + author + change rows) if file has version updates; omitted for single-version files; located at top of file, immediately after title, before content  (PASS / HALT)
- [ ] Filename: lowercase, kebab-case slug  (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file  (PASS / HALT)

## Frontmatter Schema

```yaml
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>           # ISO 8601 UTC, permanent, never reused. MUST generate with: date -u +'%Y%m%dT%H%M%SZ' at creation. Estimating or rounding = GATE FAILURE.
tier: report                     # always report
author: <name>  # who wrote this (e.g. Link, Ava, Zelda, Suggi, Luffy)
tags: [<tag>, <tag>]             # lowercase, hyphens for spaces
links: [<brain:path/to/file.md>]   # paths relative to agentic-brain root. Use `brain:` prefix for cross-repo references; omit for same-repo links.
---
```

## Frontmatter Rules

- `name` is a short lowercase kebab-case slug, unique. Example:
  `inter-agent-cooperation-findings`.
- `id` is ISO 8601 UTC (`YYYYMMDDTHHMMSSZ`). Never reuse. Never change after publishing. MUST generate with: `date -u +'%Y%m%dT%H%M%SZ'` at creation. Estimating or rounding = GATE FAILURE.
- `tier` is always `report`.
- `author` is who wrote the report (e.g. Link, Ava, Zelda, Suggi, Luffy).
- `tags` use lowercase, hyphens for spaces. Prefer existing tags from
  the brain's tag registry.
- `links` are paths relative to the agentic-brain root. Use `brain:`
  prefix (e.g. `brain:governance/system-constitution.md`) for
  cross-repo references. No prefix = same-repo link. Include links to
  the evaluations that reviewed this report. Do not use absolute
  paths or file:// URIs.

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

## Version History
*Has this report evolved?*

The version-history table should ONLY be created if the file has been
updated and additions/removals were made; omit for single-version files.

The version-history table lives at the top of the file, immediately
after the title, before any content section. See "## Example" section.

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | YYYY-MM-DD | <Agent> | Initial report. |
| 2 | YYYY-MM-DD | <Agent> | Updated findings. |

HALT - Add the version-history table ONLY if the file has been updated.

## Cross-Links

Link to:
- The evaluations that reviewed this report.
- Related reports, proposals, or insights.
- Library topics referenced in the findings.
- The IORs that triggered this research.

## Example -- Minimal Valid Report

```markdown
---
name: inter-agent-cooperation-findings
id: 20260614T120000Z
tier: report
author: Link
tags: [multi-agent, cooperation, verification, architecture]
links:
  - research/evaluations/ava-review-cooperation-findings.md
  - library/coding-agentic-ai/agent-memory-context-persistence.md
---

# Inter-Agent Cooperation -- Research Findings

## Version History (only when file has version updates)

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-06-14 | Suggi | Initial Research from WO-1 through WO-8 findings. |
| 2 | 2026-06-17 | Ava | Added extra explanations. |

## Executive Summary
Question: Can two agents on different model families cooperate
effectively on shared research tasks? Answer: Yes, with a structural
protocol. The key finding is that decorrelated review (different model
family reviews the output) catches errors the producing model cannot
see. The protocol requires: (1) independent passes, (2) a shared
artifact format, (3) explicit dissent requirements. Confidence: high
(85%), based on 8 work orders across 2 model families over 2 weeks.

## Research Question
Can OpenClaw and Claude Cowork agents on the same GitHub repo cooperate
on shared research tasks without a human coordinator for every handoff?

Scope: in. File-based artifact sharing, independent evaluation,
dissent protocol. Scope: out. Real-time coordination, shared memory
spaces, model weight sharing.

## Methodology
Approach: 8 work orders (WO-1 through WO-8) executed over 14 days.
Each WO: Link (Claude) produces -> Ava (DeepSeek) reviews -> Link
settles. Evaluation criteria: error catch rate, convergence time,
protocol breakage incidents. Sources: internal session logs, the
agentic-brain GitHub repo commit history, OpenClaw docs on sub-agents.

Limitations: 2 model families, 1 domain (system architecture). Results
may not generalize to other domains or model pairs.

## Findings

### Finding 1: Decorrelated Review Catches Invisible Errors
Ava caught 9 errors across 8 WOs that Link's self-review missed.
Error types: overclaims (4), stale references (3), missing edge
cases (2). The producing model is systematically blind to its own
overclaims -- it needs a different mind to see them.

### Finding 2: Protocol Adherence Is the Bottleneck
The 8 WOs succeeded when both agents followed the protocol. The 2
protocol violations (WO-4 self-close, WO-7 skipped evaluation)
produced the only uncaught errors. The protocol, not the models,
is the active ingredient.

### Finding 3: Negative Result -- Real-Time Coordination
We tested whether agents could coordinate through a shared live
document. Result: not viable without a locking mechanism. Both agents
wrote conflicting updates. File-based artifacts with explicit
handoff timestamps are the minimum viable coordination mechanism.

## Discussion
The decorrelation effect is real and measurable. A different model
family sees what the producing model cannot. This is not about model
quality (both are strong) -- it is about perspective. The protocol
formalizes this: produce -> independent review -> settle. Skipping
the independent review step (self-close) is the single largest source
of uncaught errors.

## Conclusion
Two agents on different model families can cooperate effectively using
file-based artifacts, independent evaluation, and an explicit handoff
protocol. The decorrelation effect (different model family review)
is the active ingredient. The protocol must be structural, not
volitional -- self-close must be impossible by design.

## Evaluation History
| Evaluator | Date | Verdict | Changes Made |
|:--|:--|:--|:--|
| ava | 2026-06-14 | APPROVE WITH CHANGES | Corrected precision error in Finding 2 |

## Cross-Links
- `research/evaluations/ava-review-cooperation-findings.md`
- `library/coding-agentic-ai/agent-memory-context-persistence.md`
- `governance/template-reports.md`
```

---

*Last updated: 2026-08-08 by Suggi. Rules are scar tissue -- each one should trace to a failure that proved it necessary.*
