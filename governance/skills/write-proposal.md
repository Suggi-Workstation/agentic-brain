---
name: write-proposal
description: "Write a proposal: Problem-Solution-Impact format with quality gates G1-G7, frontmatter schema, and cross-links. Use when asked to write a proposal, propose a change, suggest a fix, or design a solution."
user-invocable: true
disable-model-invocation: false
---

# Proposal Writing

## What This Skill Does

Guides writing a proposal to the agentic-brain. This skill holds the
PROCEDURE (Feynman loop, read template, write, transfer, commit; the watcher pushes).
The format SPECIFICATION and the compliance checklist live in
`governance/template-proposals.md` -- that file is the validator.
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

- [ ] Procedure completed (read template, write, transfer, commit) (PASS / HALT)
- [ ] Template read before writing: `template-proposals.md` opened in step 4 and followed (PASS / HALT)
- [ ] File written to the VPS clone (`research/proposals/`): directly by VPS agents, via SSH transfer by VPS-connected agents (PASS / HALT)
- [ ] Template validator gate: `template-proposals.md` Proposal Checklist -- all items confirmed PASS (PASS / HALT)
- [ ] Committed on VPS clone as hermes; watcher pushes within 1 min (AHEAD: 0 verified) (PASS / HALT)

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

### 3. Read the format specification -- the validator

Read `governance/template-proposals.md` BEFORE writing. It defines
the Problem-Solution-Impact format with Approval Gate, frontmatter schema,
and the complete Proposal Checklist. That checklist is the format gate for
this skill. Follow it exactly.

### 4. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 5. Write the artifact

Write ONLY to the agentic-brain. NEVER leave artifacts in the workspace.

VPS agents (running on the server, no SSH): write directly to
`/srv/brain/agentic-brain/research/proposals/<short-slug>.md` (your filesystem).

VPS-connected agents (remote machines, e.g. PC or laptop agents): write
locally (scratch), then transfer via the key door:

```bash
cat "<local-scratch>" | ssh -i "$VPS_SSH_KEY" -p 22 root@100.99.142.120 \
  'cat > /srv/brain/agentic-brain/research/proposals/<short-slug>.md'
```

`<short-slug>`: kebab-case, max 60 chars, unique.
### 6. Commit on the VPS clone -- NO push

The watcher pushes within 1 min and reindexes. Verify after ~1 min:
`AHEAD: 0`, or a fresh push line in /srv/brain/logs/brain-pull.log.

VPS agents:

```bash
cd /srv/brain/agentic-brain && git add research/proposals/<short-slug>.md && \
  git commit -m "proposal: <short-slug>" && echo COMMITTED
```

VPS-connected agents:

```bash
ssh -i "$VPS_SSH_KEY" -p 22 root@100.99.142.120 \
  'su - hermes -c "cd /srv/brain/agentic-brain && git add research/proposals/<short-slug>.md && git commit -m \"proposal: <short-slug>\" && echo COMMITTED"'
```
## Related

- `governance/template-proposals.md` -- format specification and compliance validator (Proposal Checklist, examples)
- `skills/write-evaluation/SKILL.md` -- evaluation writing (proposals get evaluated)
- `skills/loop-feynman/SKILL.md` -- Feynman Loop (prerequisite for all artifact writing)
- AGENTS.md approval flow -- proposals require Suggi approval
