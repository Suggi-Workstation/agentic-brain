---
name: library-writer
description: "Use when asked to write a library topic. Research, validate, and publish one queued candidate through the VPS library pipeline."
user-invocable: false
disable-model-invocation: false
---

# Library Writer

## What This Skill Does

Guides the writing process of the library pipeline. This skill holds
the PROCEDURE (locate brain, pick candidate, research, score, write,
log, commit; the watcher pushes). The format SPECIFICATION and the
compliance checklist live in
`governance/template-library.md` -- that file is the
validator. This skill references its Library Topic Checklist as the
format gate and does not restate its items (R8: reference, never
duplicate). The writer receives a candidate topic title + domain
anchor from the discovery queue, performs web search, synthesizes
knowledge, and writes a markdown topic file to the domain folder.

## When to Invoke

Invoke when asked to write a library topic. The writer processes
one candidate topic per cycle.

Skip for:
- Topics already covered by an existing file (>= 80% semantic overlap)
- Topics whose weighted score falls below 7.0 (log FLAG or REJECT)
- Domains without an anchor file
- Topics whose sources are too weak to proceed (authority < 3.0 AND
  core match would still not reach 7.0 after accounting for it)
- An empty candidate queue (log to library.log and exit)

## Path Convention -- Dual Platform

The brain working copy lives at `/srv/brain/agentic-brain` on the
fleet VPS. The watcher keeps it in two-way sync with GitHub and
pushes commits. There is NO clone step and NO push step in this
skill.

- **VPS agents** (running on the server, no SSH): every path below is
  a literal filesystem path under `/srv/brain/agentic-brain/`. Prepare
  drafts in OS temporary storage; publish through `scripts/library-publish.py`
  as yourself (agents group, no su).
- **VPS-connected agents** (remote machines, e.g. PC or laptop
  agents): read and write through the key door, commit via su:

```bash
# read a brain file
ssh -i "$VPS_SSH_KEY" -p 22 root@100.99.142.120 \
  'cat /srv/brain/agentic-brain/<path>'

# transfer a prepared draft to VPS temporary storage
cat "<local-scratch>" | ssh -i "$VPS_SSH_KEY" -p 22 root@100.99.142.120 \
  'cat > /tmp/<cycle>/<draft>'

# publish the prepared request as the clone owner
ssh -i "$VPS_SSH_KEY" -p 22 root@100.99.142.120 \
  'su - hermes -c "python3 /srv/brain/agentic-brain/scripts/library-publish.py publish /tmp/<cycle>/request.json"'
```

Quoting rule: the remote command sits in double quotes; inner quotes
sit in single quotes. A broken quote fails the whole command.

## Final Self-Check -- HARD GATE

Confirm each item at its corresponding step; commit and push checks follow
publication. HALT on failure.

- [ ] Procedure completed (locate brain, read template, pick candidate, read anchor, research, score all 4 dimensions, check similarity, write, verify cross-references, log, commit) (PASS / HALT)
- [ ] Template read before writing: `template-library.md` opened in step 2 and followed (PASS / HALT)
- [ ] Template validator gate: `template-library.md` Library Topic Checklist -- all items confirmed PASS (PASS / HALT)
- [ ] Candidate selected FIFO: first `proposed` entry from top of queue in order, not score-sorted (PASS / HALT)
- [ ] Candidate removed from candidate-queue.md (PASS / HALT)
- [ ] Domain fidelity: written topic's domain matches the candidate's Domain field exactly (PASS / HALT)
- [ ] Logbook entry written to the agentic-brain clone's logbook/library.log (PASS / HALT)
- [ ] Logbook entry format: each data field (score, similarity, sources, cross-references) on its own line, matching the step 10 example exactly (PASS / HALT)
- [ ] Logbook entry properly separated: exactly one blank line between this entry and the previous. Verify: the line before the new `## [ENT-` header is blank, and the line before that is NOT blank (it is the previous entry's last content line). No double gaps, no merged entries. (PASS / HALT)
- [ ] Every outcome, including ERROR, recorded in library.log when safe publication was available; otherwise failure surfaced to the caller (PASS / HALT)
- [ ] Shared publication used the Library Guide's Publication procedure and returned PASS; topic, candidate disposition, and log form one commit (PASS / HALT)
- [ ] Failed or incomplete research did not remove the candidate or publish a partial topic (PASS / HALT)
- [ ] Exact committed work verified on the remote mirror; a fresh unrelated watcher log line alone is insufficient (PASS / HALT)

## Procedure

### 1. Locate the brain working copy

VPS agents: `cd /srv/brain/agentic-brain`. The watcher keeps the
clone synchronized with GitHub. Read the Publication section of
`agentic-brain:library/guide-library.md`. Use the helper's snapshot command
to capture the queue and research inputs before drafting; read captured
files in full. Capture the prospective topic path as absent before writing.
Do not modify the live clone while researching or preparing drafts.

VPS-connected agents: no local clone. Every read and write below goes
through the Path Convention commands above.

### 2. Read the format specification -- the validator

Read `governance/template-library.md` BEFORE writing. It
defines the body structure (mandatory sections in order), frontmatter
schema (7 required creation fields plus optional `reviewed` metadata
added later by the Reviewer), quality gates (G1-G12),
anti-patterns, the complete example, and the Library Topic Checklist.
That checklist is the format gate for this skill. Follow the template
exactly. Do not substitute your own section order or naming -- the
template is the single source of format truth.

### 3. Pick a candidate topic from the discovery queue

Read the captured `library/candidate-queue.md`. Select the
FIRST candidate with status `proposed` (reading top-to-bottom,
FIFO order). Do NOT skip older candidates to pick higher-scored
ones further down -- the queue is ordered, respect it. Note the
candidate title, domain, and proposed scope.

The candidate's domain and scope are binding. You MUST write to the
exact domain specified in the candidate entry. You MUST NOT change
the domain, redirect to a different domain, or substantially alter
the scope. If you believe the candidate is filed under the wrong
domain, HALT and record ERROR in library.log with your reasoning. Leave
the candidate in the queue; do not silently redirect.

### 3a. Prepare the candidate disposition

Prepare a temporary queue draft with only the selected candidate removed.
Do not remove it from the live queue yet. Publish the disposition together
with a completed topic, or a deliberate FLAG, REJECT, or DUPLICATE outcome.
Unexpected failures leave the candidate pending.

If the queue is empty, log to `logbook/library.log` and exit.

### 4. Read the domain anchor

Read `library/<domain>/anchor-<domain>.md`. This is
the eternal reference against which all topics are measured. The
anchor paragraph, scope (In/Out), and adjacent domain boundary rules
are non-negotiable.

### 5. Research the topic

Perform web search using the domain name + topic title as query terms.
Collect 8+ sources (at least 6 high authority, per template G4). Evaluate source quality:
- **High authority (8-10):** academic papers, reputable publications,
  primary sources, official data.
- **Medium authority (4-7):** reputable blogs, industry publications,
  secondary sources with attribution.
- **Low authority (1-3):** personal blogs, forums, unattributed content.

Synthesize into a coherent topic file following the body structure
defined in `governance/template-library.md`.

### 6. Score the candidate (4 dimensions; writing weights)

Before writing, score the candidate topic across four dimensions
using a 0.0-10.0 scale:

| Dimension | Weight | What it measures |
|:--|:--|:--|
| Core match | 0.35 | How central is this topic to the domain anchor? |
| Scope fit | 0.35 | Does it fit In scope? Avoid Out scope and adjacent overlap? |
| Knowledge value | 0.20 | Would this compound with existing brain knowledge? |
| Source authority | 0.10 | Are the web sources credible? Rated by the high/medium/low scale above. |

Calculate weighted score: `(core * 0.35) + (scope * 0.35) + (value * 0.20) + (authority * 0.10)`.

- >= 7.0: proceed to write.
- 5.0-6.9: log to library.log with FLAG and the scores. Skip.
- < 5.0: log to library.log with REJECT and suggested redirect domain. Skip.

### 7. Check topic similarity

Scan existing topic files in `library/<domain>/` for semantic overlap
with the candidate topic. Estimate overlap percentage:

- >= 80% overlap: skip. Log DUPLICATE to library.log.
- 50-80% overlap: proceed but cross-reference the existing topic and
  focus on the uncovered portion.
- < 50% overlap: proceed normally.

### 7b. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 8. Write the topic file

Prepare the topic draft in OS temporary storage, not the workspace or live
clone. Its final destination is ONLY the agentic-brain library. Follow
the body structure and section order specified in
`governance/template-library.md` exactly.

Path (relative to the brain root): `library/<domain>/<topic-slug>.md`

Publish the validated draft through `scripts/library-publish.py` in step 11.
VPS-connected agents transfer drafts and the request to VPS temporary storage
before invoking the same helper as the clone owner.

`<topic-slug>`: lowercase kebab-case, max 80 chars, unique within the
domain. Derive from the topic title.

### 9. Verify cross-references

Before writing the logbook entry, verify every cross-referenced file
actually exists in the brain clone. Hallucinated references to deleted
or assumed files produce broken links that fail G5.

```bash
# Extract paths from the topic's links: frontmatter and See Also,
# then verify each exists
for f in <path1> <path2>; do
  ls /srv/brain/agentic-brain/$f || { echo "MISSING: $f -- remove from topic"; exit 1; }
done
```

If any path fails, remove it from both `links:` frontmatter and
`## See Also` before committing.

### 10. Write logbook entry

Prepare a body for the agentic-brain clone's `logbook/library.log`.
The helper generates the ENT number, UTC timestamp, actor, and `library`
category under its lock. Do not append directly or include the header in
the request's log body. The resulting entry MUST follow this format.
Each data field MUST be on its own line.
Do NOT pack multiple fields onto a single line. The archiving system
counts lines, not bytes -- single-line entries defeat line-based
archiving.

```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | <agent-name> | library | ref: library/<domain>/<topic-slug>.md | see: <topic-id>
Wrote topic <title> to <domain>. Weighted score: X.X/10.0
(core=X.X, scope=X.X, value=X.X, authority=X.X).
Similarity overlap: X%.
Sources: N (N high, N medium, N low).
Cross-references: N topics.
```

For deliberate dispositions, begin the log body with FLAG, REJECT, or
DUPLICATE and record the candidate title, domain, and reason. For unexpected
failures, use a log-only body beginning `ERROR:` and leave the queue unchanged.
If the helper cannot publish safely, surface its HALT result to the caller;
never bypass the lock to write a failure entry.

### 11. Commit on the agentic-brain clone -- NO push

Follow `agentic-brain:library/guide-library.md#publication`.
Use `kind: write` with the topic and queue drafts, captured expected hashes,
catalog fingerprint, and log body. The helper rechecks the first proposed
candidate, destination absence, and current files, then saves all outputs in
one commit. Another writer completing the same candidate invalidates this
request; do not overwrite its topic or substitute a different candidate.

Use `kind: dispose` for FLAG, REJECT, or DUPLICATE, with only the queue draft
and log body. Use `kind: log` with no writes for empty-queue or ERROR outcomes.
On changed inputs, read fresh state and repeat the affected selection,
similarity, and validation checks before redrafting. Do not blindly retry
a stale request.

No direct append, `git add`, commit, pull, or rebase belongs in this cycle.
The existing `repo-pull.sh` watcher owns synchronization; its Brain log is
`/srv/brain/logs/brain-pull.log`. Verify the specific publication reached
GitHub after releasing the helper's lock.

## Related

- `agentic-brain:governance/template-library.md` -- format specification and compliance validator (Library Topic Checklist, quality gates G1-G12, anti-patterns, examples)
- `agentic-brain:governance/skills/library-reviewer.md` -- reviewer skill (refreshes existing topics)
- `agentic-brain:governance/skills/library-discoverer.md` -- discoverer skill (proposes candidates)
- `agentic-brain:library/guide-library.md` -- pipeline architecture, v2 weights, anchor format
- `agentic-brain:research/insights/library-system.md` -- full system blueprint, scoring rationale
- `agentic-brain:logbook/protocol.md` -- logbook entry format
