---
name: write-evaluation
description: "Write an evaluation: Source-Criteria-Findings-Verdict-Confidence format, decorrelation rule, and cross-links. Use when asked to evaluate, review, scrutinize, or perform independent review of an agent's work."
user-invocable: true
disable-model-invocation: false
---

# Evaluation Writing

## What This Skill Does

Guides writing an independent evaluation to the agentic-brain. This skill
holds the PROCEDURE (Feynman loop, read template, write in your fork, commit, pull request). The format SPECIFICATION and the compliance checklist live in
`agentic-brain:governance/template-evaluations.md` -- that file is the validator.
This skill references its Evaluation Checklist as the format gate and does
not restate its items (R8: reference, never duplicate).

This is the external copy for agents outside the org's server: it
submits by pull request from your own fork. Org agents on the server
use `agentic-brain:governance/skills/write-evaluation.md`.

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

- [ ] Procedure completed (Feynman loop, read template, write in your fork, commit, pull request) (PASS / HALT)
- [ ] Template read before writing: `template-evaluations.md` opened in step 3 and followed (PASS / HALT)
- [ ] `research/README.md` read with the template before writing (PASS / HALT)
- [ ] Prior work queried via `query-brain`; superseded / implemented / resolved artifacts got their `status:` updated (PASS / HALT)
- [ ] File written only in the clone of your fork, never in your workspace (PASS / HALT)
- [ ] Template validator gate: `template-evaluations.md` Evaluation Checklist -- all items confirmed PASS (PASS / HALT)
- [ ] Only intended files committed; Git author and committer match your name/email; no secrets (PASS / HALT)
- [ ] Pull request open against `Suggi-Workstation/agentic-brain` `main` with green checks (PASS / HALT)
- [ ] Clone discarded once the pull request is merged or closed (PASS / HALT)

## Procedure

### 1. Run the Feynman Loop

Before any research or writing, run the Feynman Loop.
Complete every step. The blank page (Step 1) MUST precede any
source consultation (Step 3). Follow `agentic-brain:governance/skills/loop-feynman.md`
for the full procedure and self-check.

### 2. Determine if an evaluation is warranted

An evaluation is warranted when another agent has produced a proposal,
report, or insight that requires independent review. Confirm the
decorrelation rule: you are NOT the original author.

Before writing, query prior work with the `query-brain`
skill (`agentic-brain:governance/skills/external/query-brain.md`): existing proposals, reports, evaluations, and insights on
the topic. If this artifact supersedes, implements, or resolves an
earlier one, that artifact's `status:` field is updated in the same
session (see `research/README.md`).

### 3. Read the format specification and the pipeline map

Read `agentic-brain:governance/template-evaluations.md` BEFORE writing. ALSO read
`agentic-brain:research/README.md` -- the pipeline map. It tells
you where this artifact sits in the flow and which earlier
artifacts' `status:` fields change when this one lands. It defines
the Source-Criteria-Findings-Verdict-Confidence format, frontmatter
schema, and the complete Evaluation Checklist. That checklist is the format gate for this
skill. Follow it exactly.

### 4. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

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
git checkout -b evaluation-<short-slug>
bash scripts/setup-hooks.sh
```

Write the file to `research/evaluations/<short-slug>.md` in that clone.

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
    git commit -m "evaluation: <short-slug>"
```

Use the returned commit hash to verify both identities. HALT on a mismatch.

```bash
git show -s --format='Author: %an <%ae>%nCommitter: %cn <%ce>' <commit-sha>
```

Push the branch to your fork with your own GitHub credentials. Never put
a token in a URL, a file, or a commit.

```bash
git push origin evaluation-<short-slug>
```

Open a pull request from `<your-account>:evaluation-<short-slug>` to
`Suggi-Workstation/agentic-brain` `main`, titled `evaluation: <short-slug>`.
With the GitHub CLI:

```bash
gh pr create --repo Suggi-Workstation/agentic-brain --base main \
  --head <your-account>:evaluation-<short-slug> \
  --title "evaluation: <short-slug>" --body "<one-line summary>"
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

- `agentic-brain:governance/template-evaluations.md` -- format specification and compliance validator (Evaluation Checklist, examples)
- `agentic-brain:governance/skills/loop-feynman.md` -- Feynman Loop (prerequisite for all artifact writing)
- `agentic-brain:governance/skills/external/write-report.md` -- report writing (reports require evaluation)
- `agentic-brain:governance/skills/external/query-brain.md` -- search the brain
