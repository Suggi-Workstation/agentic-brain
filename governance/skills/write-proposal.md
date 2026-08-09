---
name: write-proposal
description: "Write a proposal: Problem-Solution-Impact format with quality gates G1-G7, frontmatter schema, and cross-links. Use when asked to write a proposal, propose a change, suggest a fix, or design a solution."
user-invocable: true
disable-model-invocation: false
---

# Proposal Writing

## What This Skill Does

Guides writing a proposal to the agentic-brain. This skill holds the
PROCEDURE (clone, Feynman loop, write, verify, commit, push, discard).
The format SPECIFICATION and the compliance checklist live in
`brain:governance/template-proposals.md` -- that file is the validator.
This skill references its Proposal Checklist as the format gate and does
not restate its items (R8: reference, never duplicate).

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

Confirm ALL items before committing.

- [ ] Procedure completed (clone, read template, write, verify, commit, push, discard) (PASS / HALT)
- [ ] Template read before writing: `template-proposals.md` opened in step 4 and followed (PASS / HALT)
- [ ] File written ONLY to /tmp/brain-prop/research/proposals/ (NOT the workspace) (PASS / HALT)
- [ ] Template validator gate: `template-proposals.md` Proposal Checklist -- all items confirmed PASS (PASS / HALT)
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
  "https://${GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-prop
```

### 4. Read the format specification -- the validator

Read `brain:governance/template-proposals.md` BEFORE writing. It defines
the Problem-Solution-Impact format with Approval Gate, frontmatter schema,
and the complete Proposal Checklist. That checklist is the format gate for
this skill. Follow it exactly.

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

### 6. Commit and push

```bash
cd /tmp/brain-prop
git add -A
git diff --cached --stat
git -c user.name="<AGENT>" -c user.email="<AGENT>@suggi-workspace.dev" \
  commit -m "proposal: <short-slug>"
git push origin main
```

Replace `<AGENT>` with your agent name (e.g. Link, Ava). If the push
fails, pull first, resolve, then push.

### 7. Discard the clone

```bash
cd /tmp && rm -rf brain-prop
```

## Related

- `brain:governance/template-proposals.md` -- format specification and compliance validator (Proposal Checklist, examples)
- `skills/write-evaluation/SKILL.md` -- evaluation writing (proposals get evaluated)
- `skills/loop-feynman/SKILL.md` -- Feynman Loop (prerequisite for all artifact writing)
- AGENTS.md approval flow -- proposals require Suggi approval
