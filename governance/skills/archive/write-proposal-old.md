---
name: write-proposal
description: "Write a proposal: Problem-Solution-Impact format with quality gates G1-G7, frontmatter schema, and cross-links. Use when asked to write a proposal, propose a change, suggest a fix, or design a solution."
user-invocable: true
disable-model-invocation: false
---

# Proposal Writing

## What This Skill Does

Guides writing a proposal to the agentic-brain. Procedure steps cover
the mechanics (clone, write, commit, discard). Format verification
checkboxes cover correctness (frontmatter, body structure, quality
gates, output). For the full format specification with examples, read
`governance/template-proposals.md`.

## When to Invoke

Invoke when the task involves proposing a structural change: a gate,
process, architecture, or policy that needs approval before implementation.
Proposals require a specific problem statement, concrete solution,
estimated impact, and surfaced uncertainties.

Skip for:
- Minor edits that don't need approval
- Ideas without evidence
- Work that can be done without a formal proposal

## Final Self-Check -- HARD GATE

Confirm ALL verification sections passed before committing.

- [ ] Procedure completed (clone, write, verify, commit, push, discard) (PASS / HALT)
- [ ] Frontmatter Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Body Structure Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Quality Gates Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Version History Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] File Output Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] `template-proposals.md` Checklist: all items confirmed PASS (PASS / HALT)
- [ ] Committed and pushed: changes pushed to origin main (PASS / HALT)
- [ ] Discarded clone: temporary directory removed from /tmp/ (PASS / HALT)

## Procedure

### 1. Run the Feynman Loop

Before any research or writing, invoke the `loop-feynman` skill.
Complete all 6 steps. The blank page (Step 1) MUST precede any
source consultation (Step 3). See `skills/loop-feynman/SKILL.md`
for the full procedure and self-check.

### 2. Determine if a proposal is warranted

A proposal is warranted when a structural change needs approval before
implementation: new gates, architecture changes, policy updates,
process additions. The problem must be specific and evidence-backed.

### 3. Clone the agentic-brain

```bash
cd /tmp && rm -rf brain-prop && git clone --depth 1 \
  "https://${OPENCLAW_GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-prop
```

### 4. Read the format specification

Read `governance/template-proposals.md`. It defines the
Problem-Solution-Impact format with Approval Gate, frontmatter schema
(6 fields), quality gates (G1-G7), and examples. Follow it exactly.

### 4b. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 5. Write the proposal file

Write ONLY to the agentic-brain. NEVER write proposals to the workspace.

Path: `/tmp/brain-prop/research/proposals/<short-slug>.md`

`<short-slug>`: kebab-case, max 60 chars, unique.

## Sub-Checklists -- HARD GATE (before commit)

Verify every Sub-Checklist item below. Each maps to the template. HALT on any failure;
fix before committing.

### Frontmatter Sub-Checklist

- [ ] name: lowercase kebab-case, matches filename slug (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly. Does not end in 000000Z (human-rounded = reject). Never manually typed. (PASS / HALT)
- [ ] tier: "proposal" (PASS / HALT)
- [ ] author: capitalized (e.g. Ava, Link, Researcher-1, Investor) (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited (PASS / HALT)
- [ ] links: relative paths from brain root (PASS / HALT)

### Body Structure Sub-Checklist

- [ ] Problem: specific, evidence-backed, one to three sentences (G1). Reader understands what is wrong and why it matters (PASS / HALT)
- [ ] Proposed Solution: concrete steps, another agent could implement from description alone (G2) (PASS / HALT)
- [ ] Impact: positive impact + risk assessment + cost estimate, at least one sentence each (G3) (PASS / HALT)
- [ ] Open Questions: all uncertainties written down, nothing implied. Approval questions explicit (G4) (PASS / HALT)
- [ ] Approval Gate: explicit approval condition stated (PASS / HALT)

### Quality Gates Sub-Checklist

- [ ] Feynman Loop completed: blank page before research, all 6 steps confirmed (PASS / HALT)
- [ ] G1 (Problem Is Specific): specific problem cited, so that a reader understand what is wrong and why it matters (PASS / HALT)
- [ ] G2 (Solution Is Concrete): another agent could implement it from the description alone, no hand-waving (PASS / HALT)
- [ ] G3 (Impact Is Estimated): positive impact, risk assessment, and cost estimate are all addressed. At minimum: one sentence each (PASS / HALT)
- [ ] G4 (Open Questions Surfaced): every uncertainty is written down, nothing is buried or implied (PASS / HALT)
- [ ] G5 (Cross-links Exist): at least 1 link to triggering IOR/evaluation/governance file (PASS / HALT)
- [ ] G6 (Frontmatter Complete): all 6 fields present (name, id, tier, author, tags, links) (PASS / HALT)
- [ ] G7 (Formatting Rules): ASCII-only, lowercase slugs/tags, hyphens not underscores (PASS / HALT)

### Version History Sub-Checklist (ONLY if version-history table was added)

- [ ] Version-history table: present and correct (date + author + change rows) if file has version updates; omitted for single-version files (PASS / HALT)

### File Output Sub-Checklist

- [ ] File named: lowercase kebab-case slug (PASS / HALT)
- [ ] Written ONLY to /tmp/brain-prop/research/proposals/ (NOT workspace) (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (G7) (PASS / HALT)

### 6. Commit and push

```bash
cd /tmp/brain-prop
git add -A
git diff --cached --stat
git -c user.name="Ava" -c user.email="ava@suggi-workspace.dev" \
  commit -m "proposal: <short-slug>"
git push origin main

If the push fails, pull first, resolve, then push.
```

### 7. Discard the clone

```bash
cd /tmp && rm -rf brain-prop
```

## Related

- `governance/template-proposals.md` -- full format, examples, quality gates
- `skills/write-evaluation/SKILL.md` -- evaluation writing (proposals get evaluated)
- `skills/loop-feynman/SKILL.md` -- Feynman Loop (prerequisite for all artifact writing)
- AGENTS.md approval flow -- proposals require Suggi approval
