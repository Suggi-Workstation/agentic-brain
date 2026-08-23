---
name: template-reports
id: 20260808T151846Z
tier: core-template
lock: approval-required
approved_by: Suggi
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
production procedure (Feynman loop, read template and research README, write, transfer, commit)
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
- [ ] status: `draft` -> `evaluated` -> `final`, kept current by the evaluator's same-commit duty  (PASS / HALT)
- [ ] author: capitalized (e.g. Ava, Link, Researcher-1, Investor)  (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited, prefer existing brain tags  (PASS / HALT)
- [ ] links: relative paths from repo root; `repo:` prefix only for cross-repo references, omit for same-repo  (PASS / HALT)
- [ ] Executive Summary: research question + answer + key evidence + confidence; stands alone  (PASS / HALT)
- [ ] Research Question: falsifiable, scoped (in/out clearly stated)  (PASS / HALT)
- [ ] Methodology: reproducible, sources have retrieval dates, tools and parameters named, limitations stated  (PASS / HALT)
- [ ] Findings: each with claim + evidence + confidence  (PASS / HALT)
- [ ] Negative results: what was searched for and NOT found is documented  (PASS / HALT)
- [ ] Discussion: synthesizes findings, addresses contradictions and surprises  (PASS / HALT)
- [ ] Conclusion: restates question + answer + one recommendation + open questions  (PASS / HALT)
- [ ] Body word counts: Executive Summary >= 250, Research Question >= 300, Methodology >= 300, Findings >= 300, Discussion >= 300, Conclusion >= 250  (PASS / HALT)
- [ ] Feynman pass completed BEFORE writing: blank page first  (PASS / HALT)
- [ ] Cross-links: evaluations + related reports + referenced library topics  (PASS / HALT)
- [ ] Filename: lowercase, kebab-case slug  (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file  (PASS / HALT)

## Frontmatter Schema

```yaml
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>           # ISO 8601 UTC, permanent, never reused. MUST generate with: date -u +'%Y%m%dT%H%M%SZ' at creation. Estimating or rounding = GATE FAILURE.
tier: report                     # always report
status: draft                    # draft | evaluated | final
author: <name>  # who wrote this (e.g. Link, Ava, Zelda, Suggi, Luffy)
tags: [<tag>, <tag>]             # lowercase, hyphens for spaces
links: [<path/to/file.md>]   # paths relative to repo root. Cross-repo references use the `repo:` prefix; omit for same-repo links.
---
```

## Frontmatter Rules

- `name` is a short lowercase kebab-case slug, unique. Example:
  `inter-agent-cooperation-findings`.
- `id` is ISO 8601 UTC (`YYYYMMDDTHHMMSSZ`). Never reuse. Never change after publishing. MUST generate with: `date -u +'%Y%m%dT%H%M%SZ'` at creation. Estimating or rounding = GATE FAILURE.
- `tier` is always `report`.
- `status` tracks evaluation progress (see `research/README.md`):
  `draft` until an independent evaluation is linked, `evaluated`
  once a verdict exists, `final` when APPROVE-class verdicts are
  resolved into the text.
- `author` is who wrote the report (e.g. Link, Ava, Zelda, Suggi, Luffy).
- `tags` use lowercase, hyphens for spaces. Prefer existing tags from
  the brain's tag registry.
- `links` are paths relative to the repo root. Cross-repo references use the `repo:` prefix -- the token before `:` is
the exact GitHub repo name (see the Cross-Repo Link Convention in
`governance/system-blueprint.md`). Same-repo links carry no prefix. Include links to
  the evaluations that reviewed this report. Do not use absolute
  paths or file:// URIs.

## Naming Convention

Files are named: `<short-slug>.md`

- `short-slug` -- kebab-case, max 60 chars, unique.

Example: `inter-agent-cooperation-research-2026-06.md`

## Body Structure

The sections must have the following minimal word counts. Executive Summary >= 250 words, 
Research Question >= 300 words, Methodology >= 300 words, Findings >= 300 words,
Discussion >= 300 words, Conclusion >= 250 words.

### Executive Summary
*What is the answer, in one paragraph? The bullets below are suggestions
-- use what fits.*

- State the question and the answer back to back -- no buildup.
- Summarize the key evidence in one to two sentences per major finding.
- State overall confidence, and what bounds it.
- Name the single most decision-relevant takeaway for a reader who
  stops here.
- Note where the subject sits in the pipeline if relevant: which
  proposal this investigates, which artifact triggered it, what status
  that work carries.
- This section must stand alone: a busy reader should get the full
  picture from these lines only.

### Research Question
*What exactly were we trying to find out? The bullets below are
suggestions -- use what fits.*

- State the question as a falsifiable claim or an open question.
- Define scope: what is in, and just as important, what is out.
- State why the question matters now -- what decision or work hangs on
  the answer.
- If this investigates prior artifacts, name them by id and say what
  remained open about them.
- Say what a satisfying answer looks like: what evidence would settle
  it.

### Methodology
*How did we investigate? The bullets below are suggestions -- use what
fits.*

- Describe the approach in reproducible terms: searches run, tools
  used, commands executed, parameters chosen.
- List sources consulted, each with a retrieval date.
- Prefer primary sources; note wherever only secondary sources were
  available.
- Record the search's own negative results: queries that returned
  nothing useful.
- State limitations plainly: what this methodology cannot tell us.
- Note verification steps: what was re-checked against a second source
  or re-derived independently.

### Findings
*What did we discover? The bullets below are suggestions -- use what
fits.*

- Organize findings by theme, by source, or by criterion -- whichever
  maps cleanest onto the evidence.
- Each finding carries three parts: the claim, the supporting evidence,
  and a confidence level.
- Include negative results: what was searched for and genuinely not
  found.
- Use tables, ASCII charts, or structured lists for quantitative
  material.
- Flag any finding that rests on a single uncorroborated source.
- Keep observation separate from interpretation -- interpretation
  belongs in the Discussion.

### Discussion
*What does it mean? The bullets below are suggestions -- use what
fits.*

- Synthesize the findings into one coherent narrative, not a restated
  list.
- Address contradictions between findings, and surprises against
  expectation.
- Compare against prior knowledge in the brain: confirmations,
  extensions, contradictions -- cite by id.
- Acknowledge alternative interpretations where the evidence admits
  them.
- Trace implications forward: what follows if the findings hold, and
  what changes if they do not.
- Close the loop back to the motivation stated in the Research
  Question.

### Conclusion
*What is the final answer? The bullets below are suggestions -- use
what fits.*

- Restate the question and the answer in plain language.
- Give one actionable recommendation, not a menu.
- List open questions for future work, each concrete enough to act on.
- Name the next pipeline step if one exists: evaluation pending,
  insight candidate, decision awaited, implementation ready.
- End clean: everything above already carries the detail.

## Version History

None. Git history is the version record. Do not add version-history tables to these files.

## Cross-Links

Link to:
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

## Cross-Links
- `research/evaluations/ava-review-cooperation-findings.md`
- `library/coding-agentic-ai/agent-memory-context-persistence.md`
- `governance/template-reports.md`
```

---

*Last updated: 2026-08-08 by Suggi. Rules are scar tissue -- each one should trace to a failure that proved it necessary.*
