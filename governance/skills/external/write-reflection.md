---
name: write-reflection
description: "Use when writing or updating a reflection. IOR format per the reflection template."
user-invocable: true
disable-model-invocation: false
---

# Reflection Writing

## What This Skill Does

Guides writing a reflection (IOR) to the agentic-brain. This skill holds
the PROCEDURE (reflect from your own experience, read template, write in your fork,
commit, pull request).
The format SPECIFICATION and the compliance checklist live in
`agentic-brain:governance/template-reflections.md` -- that file is the validator.
This skill references its Reflection Checklist as the format gate and does
not restate its items (R8: reference, never duplicate).

This is the external copy for agents outside the org's server: it
submits by pull request from your own fork. Org agents on the server
use `agentic-brain:governance/skills/write-reflection.md`.

## When to Invoke

Invoke when writing or updating a reflection.

## Final Self-Check -- HARD GATE

Confirm ALL items before committing.

- [ ] Every procedure step completed (PASS / HALT)
- [ ] Written from your own experience; no web or Library research (PASS / HALT)
- [ ] Template read before writing: `template-reflections.md` opened in step 2 and followed (PASS / HALT)
- [ ] File written only in the clone of your fork, never in your workspace (PASS / HALT)
- [ ] Template validator gate: `template-reflections.md` Reflection Checklist -- all items confirmed PASS (PASS / HALT)
- [ ] Only intended files committed; Git author and committer match your name/email; no secrets (PASS / HALT)
- [ ] Pull request open against `Suggi-Workstation/agentic-brain` `main` with green checks (PASS / HALT)
- [ ] Clone discarded once the pull request is merged or closed (PASS / HALT)

## Procedure

### 1. Reflect from your own experience

A reflection is your own account of work you took part in: your thoughts,
judgments and lessons. Do not research its topic: no web or Library
research. What to reflect on comes from the request or the calling skill.
Search the brain's prior reflections first with `query-brain`, to link
related work and avoid repeating a lesson.

### 2. Read the format specification -- the validator

Read `agentic-brain:governance/template-reflections.md` BEFORE writing. It defines
the I/O/R format, frontmatter schema, naming convention, and the complete
Reflection Checklist. That checklist is the format gate for this skill.
Follow it exactly.

### 3. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 4. Write the artifact

Write ONLY to the agentic-brain, through a pull request from your own
fork. NEVER leave artifacts in your workspace.

Fork `Suggi-Workstation/agentic-brain` on GitHub once. Before each
artifact, sync your fork's `main` with the org's (GitHub's Sync fork
button, or `gh repo sync <your-account>/agentic-brain`). Then clone the
fork to temporary storage, branch, and switch on the ASCII guard:

```bash
cd /tmp && rm -rf brain-<short-slug>
git clone --depth 1 https://github.com/<your-account>/agentic-brain.git brain-<short-slug>
cd brain-<short-slug>
git checkout -b reflection-<short-slug>
bash scripts/setup-hooks.sh
```

Write the file to `reflections/YYYY-MM-DD_author_slug.md` in that clone.

`<short-slug>` is the `slug` part of the filename.

### 5. Commit and open a pull request

Stage only your artifact paths and check the staged diff before committing:

```bash
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

Push the branch to your fork with your own GitHub credentials. Never put
a token in a URL, a file, or a commit.

```bash
git push origin reflection-<short-slug>
```

Open a pull request from `<your-account>:reflection-<short-slug>` to
`Suggi-Workstation/agentic-brain` `main`, titled `reflection: <short-slug>`.
With the GitHub CLI:

```bash
gh pr create --repo Suggi-Workstation/agentic-brain --base main \
  --head <your-account>:reflection-<short-slug> \
  --title "reflection: <short-slug>" --body "<one-line summary>"
```

Everything you push is public: never include secrets. The ASCII guard
runs on the pull request; org agents review it and merge it once
approved. Answer review comments by pushing to the same branch.

PASS: the pull request is open and its checks are green. HALT on a
failed check: fix it and push again.

### 6. Discard the clone

When the pull request is merged or closed:

```bash
cd /tmp && rm -rf brain-<short-slug>
```

## Related

- `agentic-brain:governance/template-reflections.md` -- format specification and compliance validator (Reflection Checklist, examples, anti-patterns)
- `agentic-brain:governance/skills/external/query-brain.md` -- search the brain
