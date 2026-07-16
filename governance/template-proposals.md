---
name: template-proposals
id: 20260618T120016Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: link
links: []
---

# Proposal Template -- How We Write Proposals

A proposal is a structured request for approval. It describes a problem,
proposes a solution, estimates impact, and surfaces open questions.
Proposals are reviewed by Suggi (or a delegated reviewer) and either
approved, rejected, or sent back for revision.

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
  Correct: `ava-core-files-v1.md`. Wrong: `ava_core_files_v1.md`.

## Frontmatter

```yaml
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>           # ISO 8601 UTC, permanent, never reused
tier: core-proposal               # always core-proposal
lock: approval-required           # proposals always require approval
approved_by: pending              # pending | Suggi | <reviewer>
author: <link|ava|zelda|suggi|luffy>
links: [<relative-brain-path>]    # related governance, proposals, or IORs
---
```

## Naming Convention

Files are named: `<short-slug>.md`

- `short-slug` -- kebab-case, max 60 chars, unique.
  Example: `ava-core-files-v1.md`

## Body Structure

### Problem
*What is broken, missing, or could be improved?*

- State the problem in one to three sentences.
- Provide evidence: what was observed, what failure occurred, what
  constraint is being hit.
- If this proposal is a response to an IOR or evaluation, cite it by id.

### Proposed Solution
*What should we do about it?*

- Describe the solution in concrete terms. What files change? What new
  files are created? What processes are added or removed?
- If the solution has multiple components, list them.
- If there are alternatives considered and rejected, mention them briefly
  with the rejection reason.

### Impact
*What changes if this is approved?*

- Positive: what improves, what failure class is prevented, what new
  capability is enabled.
- Risk: what could go wrong, what is the blast radius, what is the
  rollback plan.
- Cost: estimated effort (hours/days), token budget impact, maintenance
  burden.

### Open Questions
*What is still uncertain?*

- List questions that need Suggi's judgment before approval.
- If any part of the solution is speculative, label it clearly.

### Approval Gate
*What does approval mean?*

- Explicitly state: "If approved, I will [specific action]."
- Do not assume approval implies anything beyond what is written.

## Cross-Links

Link to:
- The IOR, evaluation, or insight that triggered this proposal.
- Related governance files that would be affected.
- Any prior proposals this supersedes or extends.

## Quality Gates

Every proposal passes these checks before submission:

- **G1 -- Problem Is Specific:** "X broke on Y date because Z" or "Y is
  missing and causes Z," not "things could be better." A reader
  understands what is wrong and why it matters.
- **G2 -- Solution Is Concrete:** Another agent could implement it from
  the description alone. What files change? What is created? What
  processes are added or removed? No hand-waving.
- **G3 -- Impact Is Estimated:** Positive impact, risk assessment, and
  cost estimate are all addressed. At minimum: one sentence each.
- **G4 -- Open Questions Surfaced:** Every uncertainty is written down.
  Nothing is buried or implied. If Suggi needs to decide something,
  the question is explicit.
- **G5 -- Cross-links Exist:** At least one link to the IOR, evaluation,
  or governance file that triggered this proposal. Zero links =
  untethered from the system's learning.
- **G6 -- Frontmatter Complete:** All fields present. `approved_by:
  pending` until reviewed by Suggi.
- **G7 -- Formatting Rules:** ASCII-only (zero non-ASCII characters),
  lowercase slugs and tags, hyphens not underscores. CI enforces
  ASCII via `ascii-guard.yml`.

---

*Last updated: 2026-07-16 by link + ava.*
