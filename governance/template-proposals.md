---
name: template-proposals
id: 20260808T151716Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: Link
links: []
---

# Proposal Template -- How We Write Proposals

A proposal is a structured request for approval. It describes a problem,
proposes a solution, estimates impact, and surfaces open questions.
Proposals are reviewed by Suggi (or a delegated reviewer) and either
approved, rejected, or sent back for revision.

## Relationship to the write-proposal Skill

This file is the format specification AND the compliance validator. The
production procedure (Feynman loop, read template and research README, write, transfer, commit)
lives in `governance/skills/write-proposal.md`; that skill references
this file's Proposal Checklist as its format gate (R8: reference, never
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
  Correct: `ava-core-files-v1.md`. Wrong: `ava_core_files_v1.md`.

## The Proposal Checklist -- HARD GATE

Pre-commit gate: every item below MUST be confirmed. The file
MUST NOT be committed with any item unconfirmed. Do not include
this checklist in the published file.

- [ ] Frontmatter: all 6 fields present (name, id, tier, author, tags, links)  (PASS / HALT)
- [ ] name: lowercase kebab-case, matches filename slug  (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly; does not end in 000000Z (human-rounded = reject); never manually typed  (PASS / HALT)
- [ ] tier: "proposal"  (PASS / HALT)
- [ ] status: `open` at birth; outcome recorded when it lands (approved / implemented / rejected / superseded)  (PASS / HALT)
- [ ] author: capitalized (e.g. Ava, Link, Researcher-1, Investor)  (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited, prefer existing brain tags  (PASS / HALT)
- [ ] links: relative paths from repo root; `repo:` prefix only for cross-repo references, omit for same-repo  (PASS / HALT)
- [ ] Problem: specific, evidence-backed (evidence cited by id or path), one to three sentences  (PASS / HALT)
- [ ] Proposed Solution: concrete steps, another agent could implement from the description alone  (PASS / HALT)
- [ ] Impact: positive contribution + risk assessment + cost estimate, at least one sentence each  (PASS / HALT)
- [ ] Open Questions: all uncertainties written down, nothing implied  (PASS / HALT)
- [ ] Approval Gate: explicit approval condition stated ("If approved, I will [specific action]")  (PASS / HALT)
- [ ] Body word counts: Problem >= 150, Proposed Solution >= 250, Impact >= 250, Open Questions >= 250, Approval Gate >= 150  (PASS / HALT)
- [ ] Feynman pass completed BEFORE writing: blank page first  (PASS / HALT)
- [ ] Cross-links: at least 1 link to triggering IOR/evaluation/governance file  (PASS / HALT)
- [ ] Filename: lowercase, kebab-case slug  (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file  (PASS / HALT)

## Frontmatter Schema

```yaml
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>           # ISO 8601 UTC, permanent, never reused. MUST generate with: date -u +'%Y%m%dT%H%M%SZ' at creation. Estimating or rounding = GATE FAILURE.
tier: proposal               # always proposal
status: open                 # open | approved | implemented | rejected | superseded
author: <name>  # who wrote this (e.g. Link, Ava, Zelda, Suggi, Luffy)
tags: [<tag>, <tag>]             # lowercase, hyphens for spaces
links: [<path/to/file.md>]   # related governance, proposals, or IORs. Cross-repo references use the `repo:` prefix; omit for same-repo links.
---
```

## Frontmatter Rules

- `name` is a short lowercase kebab-case slug, unique. Example:
  `ava-core-files-v1`.
- `id` is ISO 8601 UTC (`YYYYMMDDTHHMMSSZ`). Never reuse. Never change after publishing. MUST generate with: `date -u +'%Y%m%dT%H%M%SZ'` at creation. Estimating or rounding = GATE FAILURE.
- `tier` is always `proposal`.
- `status` moves the proposal through the pipeline (see
  `research/README.md`): `open` at birth, then `approved`,
  `implemented`, `rejected`, or `superseded by <id>`.
  When this proposal supersedes or implements an earlier artifact,
  update that artifact's `status` in the same commit and link both
  directions.
- `author` is who wrote the proposal (e.g. Link, Ava, Zelda, Suggi, Luffy).
- `tags` use lowercase, hyphens for spaces. Prefer existing tags from
  the brain's tag registry.
- `links` are paths relative to the repo root. Cross-repo references use the `repo:` prefix -- the token before `:` is
the exact GitHub repo name (see the Cross-Repo Link Convention in
`governance/system-blueprint.md`). Same-repo links carry no prefix. Link to related
  governance files, IORs, or prior proposals. Do not use absolute
  paths or file:// URIs.

## Naming Convention

Files are named: `<short-slug>.md`

- `short-slug` -- kebab-case, max 60 chars, unique.
  Example: `ava-core-files-v1.md`

## Body Structure

The sections must have the following minimal word counts. Problem >= 150 words, 
Proposed Solution >= 250 words, Impact >= 250 words, Open Questions >= 250 words,
Approval Gate >= 150 words.

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

## Version History

None. Git history is the version record. Do not add version-history tables to these files.

## Cross-Links

Link to:
- The IOR, evaluation, or insight that triggered this proposal.
- Related governance files that would be affected.
- Any prior proposals this supersedes or extends.

## Example -- Minimal Valid Proposal

```markdown
---
name: add-core-heartbeat-file
id: 20260716T140000Z
tier: proposal
author: Ava
tags: [heartbeat, bootstrap, core-files, token-budget]
links:
  - governance/system-blueprint.md
  - governance/template-reflections.md
  - research/proposals/ava-core-files-v1.md
---

# Add HEARTBEAT.md to Ava Core File Set

## Problem
The proposed core file set for Ava (v1.1) includes 7 files but omits
HEARTBEAT.md. The official OpenClaw workspace file map lists HEARTBEAT.md
as a standard bootstrap file. A missing HEARTBEAT.md injects a "missing
file" marker into every session prompt, wasting tokens on every turn.

## Proposed Solution
Add `ava-core-heartbeat.md` to the proposal set in
`research/proposals/`. The file follows the comment-only template
pattern already used in our current workspace. Content: a comment-only
heartbeat template that skips API calls until tasks are explicitly added.

## Impact
- Positive: eliminates the "missing file" warning from every session
  prompt. Saves roughly 50 tokens per session start.
- Risk: negligible. Comment-only file has zero behavioral effect.
- Cost: less than 5 minutes to write and commit.

## Open Questions
1. Should the heartbeat file use a comment-only template or include a
   minimal "check inbox" task by default?

## Approval Gate
If approved, I will add `ava-core-heartbeat.md` to the proposals folder,
update the core-files proposal index, and notify Suggi.

## Cross-Links
- `governance/system-blueprint.md`
- `governance/template-reflections.md`
- `research/proposals/ava-core-files-v1.md`
```

---

*Last updated: 2026-08-08 by Suggi. Rules are scar tissue -- each one should trace to a failure that proved it necessary.*
