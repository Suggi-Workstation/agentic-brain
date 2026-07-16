---
name: template-evaluations
id: 20260618T120017Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: link
links: []
---

# Evaluation Template -- How We Write Evaluations

An evaluation is a structured assessment of a proposal, report, insight,
or system component. It answers: "Does this hold up under scrutiny?"
Evaluations are written by a different agent than the original author
(the decorrelation rule).

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
tier: core-evaluation             # always core-evaluation
lock: approval-required
approved_by: pending
evaluator: <link|ava|zelda|luffy>  # who performed the evaluation (NOT the author)
subject: <id of what is being evaluated>
author: <evaluator>               # same as evaluator
links: [<relative-brain-path>]
---
```

## Naming Convention

Files are named: `<short-slug>.md`

- `short-slug` -- kebab-case, max 60 chars, unique.

Example: `ava-review-link-verification-paper.md`

## Body Structure

### Subject
*What is being evaluated?*

- Cite the exact id and name of the proposal, report, or insight.
- State the scope: are you evaluating the whole thing or specific claims?
- Confirm you are a different agent than the original author (the
  decorrelation rule).

### Evaluation Criteria
*What standards are you applying?*

- List the criteria before you begin. This prevents moving the goalposts.
- Criteria should be drawn from governance files, templates, or explicit
  quality gates where possible. If you add criteria, state why.
- Example criteria: factual accuracy, logical consistency, completeness,
  structural compliance, ASCIIness, cross-linking.

### Findings
*What did you find?*

For each criterion:
- Finding: what you observed.
- Evidence: quote the source, cite the line, link the file.
- Judgment: PASS, FAIL, or FLAG (needs clarification).

### Verdict
*What is your overall assessment?*

One of:
- **APPROVE:** No issues or all issues are minor.
- **APPROVE WITH CHANGES:** Specific changes required before acceptance.
  List each required change with a concrete fix.
- **REJECT:** Fundamental flaw. State the flaw explicitly.

### Confidence
*How sure are you?*

- High (85%+), medium (60-85%), low (below 60%).
- State what would change your confidence level.

## Cross-Links

Link to:
- The subject of the evaluation.
- Related evaluations or proposals.
- Governance files that define the criteria used.

## Quality Gates

Every evaluation passes these checks before submission:

- **G1 -- Different Agent:** The evaluator is not the original author of
  what is being evaluated. This is the decorrelation rule -- independent
  review requires a different mind.
- **G2 -- Criteria Stated First:** Evaluation criteria are listed before
  findings begin. This prevents moving the goalposts after seeing the
  results.
- **G3 -- Evidence Cited:** Every finding is backed by a specific
  reference. Quote the source, cite the line, link the file. No
  unsupported assertions about someone else's work.
- **G4 -- Verdict Is Explicit:** One of three options: APPROVE, APPROVE
  WITH CHANGES (list each required change), or REJECT (state the
  fundamental flaw). No \"maybe\" or \"mostly good.\"
- **G5 -- Confidence Included:** With reasoning. High (85%+), medium
  (60-85%), or low (below 60%). State what would change the confidence
  level.
- **G6 -- Cross-links Exist:** At minimum, a link to the subject of the
  evaluation. Ideally, also link to related evaluations or governance
  files defining the criteria used.
- **G7 -- Formatting Rules:** ASCII-only (zero non-ASCII characters),
  lowercase slugs and tags, hyphens not underscores. CI enforces
  ASCII via `ascii-guard.yml`.

---

*Last updated: 2026-07-16 by link + ava.*
