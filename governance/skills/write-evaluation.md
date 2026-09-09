---
name: write-evaluation
description: "Write an evaluation: Source-Criteria-Findings-Verdict format with quality gates G1-G8, decorrelation rule, and cross-links. Use when asked to evaluate, review, scrutinize, or perform independent review of an agent's work."
user-invocable: true
disable-model-invocation: false
---

# Evaluation Writing

## What This Skill Does

Guides writing an independent evaluation to the agentic-brain. This skill
holds the PROCEDURE (Feynman loop, read template, write, transfer, commit; the watcher pushes). The format SPECIFICATION and the compliance checklist live in
`agentic-brain:governance/template-evaluations.md` -- that file is the validator.
This skill references its Evaluation Checklist as the format gate and does
not restate its items (R8: reference, never duplicate).

## When to Invoke

Invoke when the task involves evaluating another agent's work: a
proposal, report, or insight needs independent scrutiny. The
decorrelation rule requires a different agent (or model family) than
the original author.

Skip for:
- Your own work (violates decorrelation rule)
- Work already evaluated with APPROVE verdict
- Minor formatting fixes

## Final Self-Check -- HARD GATE

Confirm ALL items before committing.

- [ ] Procedure completed (read template, write, transfer, commit) (PASS / HALT)
- [ ] Template read before writing: `template-evaluations.md` opened in step 4 and followed (PASS / HALT)
- [ ] `research/README.md` read with the template before writing (PASS / HALT)
- [ ] Prior work queried via `query-brain-vps`; superseded / implemented / resolved artifacts got their `status:` updated (PASS / HALT)
- [ ] File written to the agentic-brain clone (`research/evaluations/`): directly by VPS agents, via SSH transfer by VPS-connected agents (PASS / HALT)
- [ ] Template validator gate: `template-evaluations.md` Evaluation Checklist -- all items confirmed PASS (PASS / HALT)
- [ ] Only intended files committed; Git author and committer match your name/email; natural watcher publication verified (PASS / HALT)

## Procedure

### 1. Run the Feynman Loop

Before any research or writing, invoke the `loop-feynman` skill.
Complete all 6 steps. The blank page (Step 1) MUST precede any
source consultation (Step 3). See `skills/loop-feynman/SKILL.md`
for the full procedure and self-check.

### 2. Determine if an evaluation is warranted

An evaluation is warranted when another agent has produced a proposal,
report, or insight that requires independent review. Confirm the
decorrelation rule: you are NOT the original author.

Before writing, query prior work with the `query-brain-vps`
skill: existing proposals, reports, evaluations, and insights on
the topic. If this artifact supersedes, implements, or resolves an
earlier one, that artifact's `status:` field is updated in the same
session (see `research/README.md`).

### 3. Read the format specification and the pipeline map

Read `agentic-brain:governance/template-evaluations.md` BEFORE writing. ALSO read
`agentic-brain:research/README.md` -- the pipeline map. It tells
you where this artifact sits in the flow and which earlier
artifacts' `status:` fields change when this one lands. It defines
the Source-Criteria-Findings-Verdict format, frontmatter schema, and the
complete Evaluation Checklist. That checklist is the format gate for this
skill. Follow it exactly.

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
`/srv/brain/agentic-brain/research/evaluations/<short-slug>.md` (your filesystem).

VPS-connected agents (remote machines, e.g. PC or laptop agents): write
locally (scratch), then transfer via the key door:

```bash
cat "<local-scratch>" | ssh -i "$VPS_SSH_KEY" -p 22 root@100.99.142.120 \
  'cat > /srv/brain/agentic-brain/research/evaluations/<short-slug>.md'
```

`<short-slug>`: kebab-case, max 60 chars, unique.
### 6. Commit on the agentic-brain clone -- NO push

Run on the VPS as the clone owner, directly or through your approved connection.
Stage only your artifact paths and check the staged diff before committing:

```bash
cd /srv/brain/agentic-brain
git add <artifact-paths>
git diff --cached --stat
```

Commit with your own Git name and email. Do not change repository or global settings.

```bash
AGENT_NAME="<your Git name>"
AGENT_EMAIL="<your Git email>"
env GIT_AUTHOR_NAME="$AGENT_NAME" GIT_AUTHOR_EMAIL="$AGENT_EMAIL" \
    GIT_COMMITTER_NAME="$AGENT_NAME" GIT_COMMITTER_EMAIL="$AGENT_EMAIL" \
    git commit -m "evaluation: <short-slug>"
```

Use the returned commit hash to verify both identities. HALT on a mismatch.

```bash
git show -s --format='Author: %an <%ae>%nCommitter: %cn <%ce>' <commit-sha>
```

Let the existing watcher push naturally. Do not push manually or force a watcher run.
Verify publication; if pending, wait for the next watcher tick and check again:

```bash
git fetch origin
git merge-base --is-ancestor <commit-sha> origin/main
```

PASS: the exact commit is on origin/main. HALT on a publication error.

## Related

- `agentic-brain:governance/template-evaluations.md` -- format specification and compliance validator (Evaluation Checklist, examples)
- `skills/loop-feynman/SKILL.md` -- Feynman Loop (prerequisite for all artifact writing)
- `skills/write-report/SKILL.md` -- report writing (reports require evaluation)
