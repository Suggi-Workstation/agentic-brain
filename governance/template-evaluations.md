---
name: template-evaluations
id: 20260808T151324Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: Link
links: []
---

# Evaluation Template -- How We Write Evaluations

An evaluation is a structured assessment of a proposal, report, insight,
or system component. It answers: "Does this hold up under scrutiny?"
Evaluations are written by a different agent than the original author
(the decorrelation rule).

## Relationship to the write-evaluation Skill

This file is the format specification AND the compliance validator. The
production procedure (Feynman loop, read template and research README, write, transfer, commit)
lives in `governance/skills/write-evaluation.md`; that skill references
this file's Evaluation Checklist as its format gate (R8: reference, never
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

## The Evaluation Checklist -- HARD GATE

Pre-commit gate: every item below MUST be confirmed. The file
MUST NOT be committed with any item unconfirmed. Do not include
this checklist in the published file.

- [ ] Frontmatter: all 7 fields present (name, id, tier, source, author, tags, links)  (PASS / HALT)
- [ ] name: lowercase kebab-case, matches filename slug  (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly; does not end in 000000Z (human-rounded = reject); never manually typed  (PASS / HALT)
- [ ] tier: "evaluation"  (PASS / HALT)
- [ ] source: exact id of the work being evaluated  (PASS / HALT)
- [ ] author: capitalized (e.g. Ava, Link, Researcher-1, Investor); must differ from source author (decorrelation rule)  (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited, prefer existing brain tags  (PASS / HALT)
- [ ] links: relative paths from repo root; `repo:` prefix only for cross-repo references, omit for same-repo  (PASS / HALT)
- [ ] Source cited by exact id; scope stated  (PASS / HALT)
- [ ] Evaluation criteria listed before findings begin  (PASS / HALT)
- [ ] Every finding backed by a specific reference (quote/cite/link)  (PASS / HALT)
- [ ] Verdict: one of APPROVE / APPROVE WITH CHANGES / REJECT  (PASS / HALT)
- [ ] Required changes listed concretely (if APPROVE WITH CHANGES)  (PASS / HALT)
- [ ] Confidence: stated with reasoning, high 85%+ / medium 60-85% / low below 60%  (PASS / HALT)
- [ ] Evaluated artifact's `status:` updated in the same commit (evaluated / final / revision loop)  (PASS / HALT)
- [ ] Body word counts: Source >= 150, Evaluation Criteria >= 250, Findings >= 250, Verdict >= 200, Confidence >= 200  (PASS / HALT)
- [ ] Feynman pass completed BEFORE writing: blank page first  (PASS / HALT)
- [ ] Cross-links: source + related evaluations/governance files  (PASS / HALT)
- [ ] Filename: lowercase, kebab-case slug  (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file  (PASS / HALT)

## Frontmatter Schema

```yaml
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>           # ISO 8601 UTC, permanent, never reused. MUST generate with: date -u +'%Y%m%dT%H%M%SZ' at creation. Estimating or rounding = GATE FAILURE.
tier: evaluation                  # always evaluation
source: <id>                      # id of what is being evaluated
author: <name>  # the evaluating agent (e.g. Link, Ava, Zelda, Luffy). Not the source author.
tags: [<tag>, <tag>]             # lowercase, hyphens for spaces
links: [<path/to/file.md>]   # paths relative to repo root. Cross-repo references use the `repo:` prefix; omit for same-repo links.
---
```

## Frontmatter Rules

- `name` is a short lowercase kebab-case slug, unique. Example:
  `review-link-verification-paper`.
- `id` is ISO 8601 UTC (`YYYYMMDDTHHMMSSZ`). Never reuse. Never change after publishing. MUST generate with: `date -u +'%Y%m%dT%H%M%SZ'` at creation. Estimating or rounding = GATE FAILURE.
- `tier` is always `evaluation`.
- `source` is the id of the proposal, report, or insight being
  evaluated. Never evaluate your own work (the decorrelation rule).
- `author` is who performed the evaluation (e.g. Link, Ava, Zelda, Luffy). Must differ from the source's author.
- `tags` use lowercase, hyphens for spaces. Prefer existing tags from
  the brain's tag registry.
- `links` are paths relative to the repo root. Cross-repo references use the `repo:` prefix -- the token before `:` is
the exact GitHub repo name (see the Cross-Repo Link Convention in
`governance/system-blueprint.md`). Same-repo links carry no prefix. Do not use
  absolute paths or file:// URIs.

## Naming Convention

Files are named: `<short-slug>.md`

- `short-slug` -- kebab-case, max 60 chars, unique.

Example: `ava-review-link-verification-paper.md`

## Body Structure

The sections must have the following minimal word counts. Source >= 150 words, 
Evaluation Criteria >= 250 words, Findings >= 250 words, Verdict >= 200 words,
Confidence >= 200 words.

### Source
*What is being evaluated, and under what authority? The bullets below
are suggestions -- use what fits.*

- Cite the exact artifact by id and title, with its current status.
- State the scope: whole artifact, specific claims, or specific
  sections.
- Confirm the decorrelation rule: who you are, who authored the source,
  why you are entitled to evaluate it -- or disclose the waiver
  explicitly if Suggi suspended the rule for this run.
- Note anything that could bias the read: prior involvement with the
  work, agreement or disagreement with its conclusion before starting.
- Say what standard of proof you are applying: what would count as a
  failure regardless of overall quality.
- If evaluating a test-run or mechanics exercise rather than production
  work, say so here.

### Evaluation Criteria
*What standards are you applying? The bullets below are suggestions --
use what fits.*

- List the criteria before examining the evidence -- fixing them in
  advance prevents moving goalposts after seeing answers.
- Draw criteria from governance where possible: templates, checklists,
  gate rules, constitution.
- Give each criterion a one-line rationale for why it matters for this
  artifact.
- Order them by importance so a partial evaluation still covers what
  matters most.
- Add custom criteria only with a stated reason; do not pad the list.
- Number them -- findings will reference these numbers.

### Findings
*What did the scrutiny surface? The bullets below are suggestions --
use what fits.*

- Work through the criteria in order; one finding block per criterion.
- Each finding carries three parts: observation, evidence (quote, cite,
  or link), judgment (PASS / FAIL / FLAG).
- Quote precisely when disputing wording -- paraphrase hides the defect
  being flagged.
- Re-execute checks where possible instead of trusting the artifact's
  own claims about itself.
- Distinguish severity: cosmetic imprecision vs misleading error vs
  load-bearing falsehood.
- Note explicitly which checks came back clean -- silence reads as not
  examined.

### Verdict
*What is your overall assessment? The bullets below are suggestions --
use what fits.*

- Choose one: APPROVE / APPROVE WITH CHANGES / REJECT.
- Justify the choice in one paragraph: why this verdict and not the
  adjacent one.
- For APPROVE WITH CHANGES: list each required change as a concrete,
  executable instruction -- text to replace, number to correct, link
  to fix.
- For REJECT: state the fundamental flaw explicitly and whether
  revision is possible at all.
- In the SAME commit, set the evaluated artifact's `status:` per your
  verdict (`evaluated`, or the revision loop on REJECT).
- Keep the verdict proportional: verdict follows from the findings,
  not from overall impression.

### Confidence
*How sure are you, and where does that waver? The bullets below are
suggestions -- use what fits.*

- State high (85%+), medium (60-85%), or low (below 60%).
- Ground the level: what was verified directly vs taken on trust.
- Name the residual gaps: what this evaluation could not check, and
  why.
- Say what would raise or lower the confidence: which discovery would
  change the verdict.
- Under a waived decorrelation rule, acknowledge what self-review
  structurally cannot see.
- End concrete: confidence is a claim about evidence coverage, not a
  feeling.

## Version History

None. Git history is the version record. Do not add version-history tables to these files.

## Cross-Links

Link to:
- The source of the evaluation.
- Related evaluations or proposals.
- Governance files that define the criteria used.

## Example -- Minimal Valid Evaluation

```markdown
---
name: ava-review-link-verification-paper
id: 20260716T150000Z
tier: evaluation
source: 20260614T120000Z
author: Ava
tags: [verification, multi-agent, formatting]
links:
  - research/reports/link-verification-gates-multi-agent.md
  - governance/system-constitution.md
---

# Independent Review: Link's Verification Gates Paper

## Source
Evaluating `20260614T120000Z` -- "Verification Gates for Multi-Agent
Systems" by Link. Full-scope evaluation. I am Ava (DeepSeek V4 Pro), a different model family from Link (Claude).
The decorrelation rule is satisfied.

## Evaluation Criteria
1. Factual accuracy: are all 8 cited sources correctly represented?
2. Logical consistency: do the conclusions follow from the evidence?
3. Structural compliance: does the report follow template-reports.md?
4. ASCIIness: any non-ASCII characters?

## Findings

### Criterion 1: Factual Accuracy -- PASS
Verified 7 of 8 sources (one locked behind paywall). All 7 correctly
represented. The eighth source is flagged below.

### Criterion 2: Logical Consistency -- FLAG
The conclusion states "verification gates reduce errors by 40%." This
figure appears in the body as 35-45% from Source 5. The conclusion
should use the range, not the midpoint, since Source 5 explicitly
states the range depends on task complexity.

### Criterion 3: Structural Compliance -- PASS
Report follows template-reports.md structure. All sections present.

### Criterion 4: ASCIIness -- PASS
No non-ASCII characters found via grep.

## Verdict
APPROVE WITH CHANGES:
1. Change conclusion from "40%" to "35-45% depending on task complexity"
   per Source 5, paragraph 3.

## Confidence
High (90%). Seven of eight sources verified. The one flagged issue is
a precision error, not a factual error.

## Cross-Links
- `research/reports/link-verification-gates-multi-agent.md`
- `governance/template-reports.md`
```

---

*Last updated: 2026-08-08 by Suggi. Rules are scar tissue -- each one should trace to a failure that proved it necessary.*
