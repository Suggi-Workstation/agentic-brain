---
name: write-reflection
description: "Write a reflection (IOR): Idea-Opinion-Reflection format with quality gates G1-G9, one actionable change, and cross-links. Use when asked to write a reflection, reflect on a topic, or capture a durable insight."
user-invocable: true
disable-model-invocation: false
---

# Reflection Writing

## What This Skill Does

Guides writing a reflection (IOR) to the agentic-brain. This skill holds
the PROCEDURE (Feynman loop, read template, write, transfer, commit; the watcher pushes).
The format SPECIFICATION and the compliance checklist live in
`agentic-brain:governance/template-reflections.md` -- that file is the validator.
This skill references its Reflection Checklist as the format gate and does
not restate its items (R8: reference, never duplicate).

## When to Invoke

Invoke when the task involves writing or updating a reflection. A reflection is
warranted when a session produces a durable insight:

- The Feynman Loop revealed a gap you did not know you had.
- An error revealed a failure class not yet gated against.
- Research produced a conclusion that contradicts or extends existing
  brain knowledge.
- A structural change was made that other agents should know about.

Skip when the session produced only logs (memory/YYYY-MM-DD.md), status
updates, or insights already captured in an existing reflection (update the
existing one instead -- see template versioning rules).

## Final Self-Check -- HARD GATE

Confirm ALL items before committing.

- [ ] Procedure completed (read template, write, transfer, commit) (PASS / HALT)
- [ ] Template read before writing: `template-reflections.md` opened in step 4 and followed (PASS / HALT)
- [ ] File written to the agentic-brain clone (`reflections/`): directly by VPS agents, via SSH transfer by VPS-connected agents (PASS / HALT)
- [ ] Template validator gate: `template-reflections.md` Reflection Checklist -- all items confirmed PASS (PASS / HALT)
- [ ] Only intended files committed; Git author and committer match your name/email; natural watcher publication verified (PASS / HALT)

## Procedure

### 1. Run the Feynman Loop

Before any research or writing, invoke the `loop-feynman` skill.
Complete all 6 steps. The blank page (Step 1) MUST precede any
source consultation (Step 3). See `skills/loop-feynman/SKILL.md`
for the full procedure and self-check.

### 2. Determine if a reflection is warranted

See "When to Invoke" above. If no durable insight emerged, skip reflection
writing entirely. Do not write a forced reflection to check a box.

### 3. Read the format specification -- the validator

Read `agentic-brain:governance/template-reflections.md` BEFORE writing. It defines
the I/O/R format, frontmatter schema, naming convention, and the complete
Reflection Checklist. That checklist is the format gate for this skill.
Follow it exactly.

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
`/srv/brain/agentic-brain/reflections/<short-slug>.md` (your filesystem).

VPS-connected agents (remote machines, e.g. PC or laptop agents): write
locally (scratch), then transfer via the key door:

```bash
cat "<local-scratch>" | ssh -i "$VPS_SSH_KEY" -p 22 root@100.99.142.120 \
  'cat > /srv/brain/agentic-brain/reflections/<short-slug>.md'
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
    git commit -m "reflection: <short-slug>"
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

- `agentic-brain:governance/template-reflections.md` -- format specification and compliance validator (Reflection Checklist, examples, anti-patterns)
- `skills/loop-feynman/SKILL.md` -- Feynman Loop (produces material for reflections)
- `skills/session-end/SKILL.md` -- session-end calls reflection writing when insight emerged
