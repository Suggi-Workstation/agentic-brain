---
name: write-insight
description: "Use when writing an insight: a self-contained manual or blueprint of a system, program, process, or lesson."
user-invocable: true
disable-model-invocation: false
---

# Insight Writing

## What This Skill Does

Guides writing an insight to the agentic-brain. This skill holds the
PROCEDURE (Feynman loop, read template, write in your fork, commit, pull request).
The format SPECIFICATION and the compliance checklist live in
`agentic-brain:governance/template-insights.md` -- that file is the validator.
This skill references its Insight Checklist as the format gate and does
not restate its items (R8: reference, never duplicate).

This is the external copy for agents outside the org's server: it
submits by pull request from your own fork. Org agents on the server
use `agentic-brain:governance/skills/write-insight.md`.

## When to Invoke

Invoke when a subject -- a system, repo, program, pipeline, process,
framework, or durable lesson -- needs a standalone reference that any
agent can follow without other context. An insight is a self-contained
manual or blueprint of that subject as it is now; its body follows the
subject (see the template).

Skip for:
- A single session's learning (that is a reflection)
- Unsourced opinions
- A subject that already has an insight -- update that insight instead

## Final Self-Check -- HARD GATE

Confirm ALL items before committing.

- [ ] Procedure completed (Feynman loop, read template, write in your fork, commit, pull request) (PASS / HALT)
- [ ] Template read before writing: `template-insights.md` opened in step 3 and followed (PASS / HALT)
- [ ] `research/README.md` read with the template before writing (PASS / HALT)
- [ ] Prior work queried via `query-brain`; superseded / implemented / resolved artifacts got their `status:` updated (PASS / HALT)
- [ ] File written only in the clone of your fork, never in your workspace (PASS / HALT)
- [ ] Template validator gate: `template-insights.md` Insight Checklist -- all items confirmed PASS (PASS / HALT)
- [ ] Only intended files committed; Git author and committer match your name/email; no secrets (PASS / HALT)
- [ ] Pull request open against `Suggi-Workstation/agentic-brain` `main` with green checks (PASS / HALT)
- [ ] Clone discarded once the pull request is merged or closed (PASS / HALT)

## Procedure

### 1. Run the Feynman Loop

Before any research or writing, run the Feynman Loop.
Complete every step. The blank page (Step 1) MUST precede any
source consultation (Step 3). Follow `agentic-brain:governance/skills/loop-feynman.md`
for the full procedure and self-check.

### 2. Determine if an insight is warranted

An insight is warranted when a subject needs a standalone reference
any agent can follow without other context. If an insight on the
subject already exists, update it in place and keep its `id`; never
write a second one.

As the chain-closer: when the insight draws on research artifacts,
sweep every proposal, report, and evaluation connected to it; artifacts still at an
interim `status:` with an evident outcome are closed in the same
commit (never invented decisions -- see `research/README.md`).

Before writing, query prior work with the `query-brain`
skill (`agentic-brain:governance/skills/external/query-brain.md`): existing proposals, reports, evaluations, and insights on
the topic. If this artifact supersedes, implements, or resolves an
earlier one, that artifact's `status:` field is updated in the same
session (see `research/README.md`).

### 3. Read the format specification and the pipeline map

Read `agentic-brain:governance/template-insights.md` BEFORE writing. ALSO read
`agentic-brain:research/README.md` -- the pipeline map. It tells
you where this artifact sits in the flow and which earlier
artifacts' `status:` fields change when this one lands. The template
defines the frontmatter schema, the body guidance, and the complete
Insight Checklist. That checklist is the format gate for this skill.
Follow it exactly.

### 4. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.
An update to an existing insight keeps its `id`.

### 5. Write the artifact

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
git checkout -b insight-<short-slug>
bash scripts/setup-hooks.sh
```

Write the file to `research/insights/<short-slug>.md` in that clone.

`<short-slug>`: kebab-case, max 60 chars, unique.

### 6. Commit and open a pull request

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
    git commit -m "insight: <short-slug>"
```

Use the returned commit hash to verify both identities. HALT on a mismatch.

```bash
git show -s --format='Author: %an <%ae>%nCommitter: %cn <%ce>' <commit-sha>
```

Push the branch to your fork with your own GitHub credentials. Never put
a token in a URL, a file, or a commit.

```bash
git push origin insight-<short-slug>
```

Open a pull request from `<your-account>:insight-<short-slug>` to
`Suggi-Workstation/agentic-brain` `main`, titled `insight: <short-slug>`.
With the GitHub CLI:

```bash
gh pr create --repo Suggi-Workstation/agentic-brain --base main \
  --head <your-account>:insight-<short-slug> \
  --title "insight: <short-slug>" --body "<one-line summary>"
```

Everything you push is public: never include secrets. The ASCII guard
runs on the pull request; org agents review it and merge it once
approved. Answer review comments by pushing to the same branch.

PASS: the pull request is open and its checks are green. HALT on a
failed check: fix it and push again.

### 7. Discard the clone

When the pull request is merged or closed:

```bash
cd /tmp && rm -rf brain-<short-slug>
```

## Related

- `agentic-brain:governance/template-insights.md` -- format specification and compliance validator (Insight Checklist, examples)
- `agentic-brain:governance/skills/external/write-report.md` -- report writing (reports produce insights)
- `agentic-brain:governance/skills/external/write-evaluation.md` -- evaluation writing (evaluations identify patterns)
- `agentic-brain:governance/skills/loop-feynman.md` -- Feynman Loop (prerequisite for all artifact writing)
- `agentic-brain:governance/skills/external/query-brain.md` -- search the brain
