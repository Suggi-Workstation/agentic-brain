---
name: template-evaluations
id: 20260618T120017Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: Suggi
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

## Frontmatter Schema

```yaml
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>           # ISO 8601 UTC, permanent, never reused. Use the exact second of creation -- run date -u +'%Y%m%dT%H%M%SZ'
tier: evaluation                  # always evaluation
source: <id>                      # id of what is being evaluated
author: <Link|Ava|Zelda|Luffy>    # the evaluating agent (NOT the author of the source)
tags: [<tag>, <tag>]             # lowercase, hyphens for spaces
links: [<relative-brain-path>]   # paths relative to agentic-brain root
---
```

## Frontmatter Rules

- `name` is a short lowercase kebab-case slug, unique. Example:
  `review-link-verification-paper`.
- `id` is ISO 8601 UTC (`YYYYMMDDTHHMMSSZ`). Never reuse. Never change after publishing. Use the exact second of creation -- run date -u +'%Y%m%dT%H%M%SZ'
- `tier` is always `evaluation`.
- `source` is the id of the proposal, report, or insight being
  evaluated. Never evaluate your own work (the decorrelation rule).
- `author` is who performed the evaluation. The author list is {link,
  ava, zelda, luffy}. A different agent than the source's author.
- `tags` use lowercase, hyphens for spaces. Prefer existing tags from
  the brain's tag registry.
- `links` are relative paths from the agentic-brain root. Do not use
  absolute paths or file:// URIs.

## Naming Convention

Files are named: `<short-slug>.md`

- `short-slug` -- kebab-case, max 60 chars, unique.

Example: `ava-review-link-verification-paper.md`

## Body Structure

### Source
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
- The source of the evaluation.
- Related evaluations or proposals.
- Governance files that define the criteria used.

## Quality Gates

Every evaluation passes these checks before submission:

- **G1 -- Different Agent:** The author is not the original author of
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
- **G6 -- Cross-links Exist:** At minimum, a link to the source of the
  evaluation. Ideally, also link to related evaluations or governance
  files defining the criteria used.
- **G7 -- Formatting Rules:** ASCII-only (zero non-ASCII characters),
  lowercase slugs and tags, hyphens not underscores. CI enforces
  ASCII via `ascii-guard.yml`.

## Example -- Minimal Valid Evaluation

```markdown
---
name: ava-review-link-verification-paper
id: 20260716T150000Z
tier: evaluation
source: 20260614T120000Z
author: Ava
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

## The Evaluation Checklist

Pre-commit gate: every item below MUST be confirmed. The file
MUST NOT be committed with any item unconfirmed. Do not include
this checklist in the published file.

```
[ ] Frontmatter Schema complete (7 fields: name, id, tier, source, author, tags, links)
[ ] Frontmatter Rules correctly applied (7 fields: name, id, tier, source, author, tags, links)
[ ] id is UTC timestamp with exact second, never used before
[ ] Source cited by exact id; scope stated
[ ] Criteria listed before findings begin
[ ] Every finding backed by a specific reference (quote/cite/link)
[ ] Verdict is one of: APPROVE / APPROVE WITH CHANGES / REJECT
[ ] Required changes are listed concretely (if APPROVE WITH CHANGES)
[ ] Confidence stated with reasoning (high/medium/low)
[ ] Cross-links: source + related evaluations/governance files
[ ] Filename: lowercase, kebab-case slug
[ ] ASCII-only: zero non-ASCII characters in the file
```

---

*Last updated: 2026-07-16 by Suggi. Rules are scar tissue -- each
one should trace to a failure that proved it necessary.*
