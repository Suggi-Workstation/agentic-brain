---
name: library-discoverer
description: "Use when asked to discover library topics. Find and score uncovered topics for the candidate queue."
user-invocable: false
disable-model-invocation: false
---

# Library Discoverer

## What This Skill Does

Guides the discovery process of the library pipeline. Scans domain
anchors, identifies knowledge gaps, proposes new candidate topics
across 4 dimensions including domain balance to prevent library tilt.
Does NOT write topic files -- only proposes titles and brief scopes
for the writing process to pick up. Candidates are appended to
`library/candidate-queue.md`. For the full pipeline architecture and
weight rules, read `library/guide-library.md` and
`research/insights/library-system.md`.

## When to Invoke

Invoke when asked to discover candidate library topics. Each cycle picks
a subset of domains and proposes 1-3 candidate topics per domain.

Skip for:
- Domains with no anchor file
- Topics already in the candidate queue
- Topics already covered by existing files (check per-domain index files)
- Topics previously rejected (check library.log)

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
publication. One checklist -- no
sub-checklists, no section summaries. Each item maps to a procedure
step or a library guide rule. HALT on any failure; fix before
committing.

- [ ] Procedure completed: select domains, read full anchors, identify gaps, score all 4 dimensions, check duplicates/capacity, prepare drafts and log body, publish (PASS / HALT)
- [ ] Each candidate scored across all four dimensions (PASS / HALT)
- [ ] Each dimension has a brief justification (1-2 sentences) (PASS / HALT)
- [ ] Weighted score calculated correctly: (gap*0.40 + compounding*0.25 + timeliness*0.20 + balance*0.15) (PASS / HALT)
- [ ] Gap assessment verified against existing topics via per-domain index files (no false gaps)  (PASS / HALT)
- [ ] Domain balance score derived from topic count survey in step 2 (PASS / HALT)
- [ ] Scope brevity: every candidate scope is 3-4 sentences, max 100 words. No multi-paragraph scopes. (PASS / HALT)
- [ ] No candidate proposed for a domain without an anchor file (PASS / HALT)
- [ ] Topic count survey completed before selecting domains (from index-library.md)  (PASS / HALT)
- [ ] Underrepresented domains prioritized in domain selection (PASS / HALT)
- [ ] Balance dimension score reflects actual topic counts, not assumed (PASS / HALT)
- [ ] Candidate queue format matches the specification (PASS / HALT)
- [ ] No duplicate candidates in the queue (checked by title and scope) (PASS / HALT)
- [ ] Each candidate has domain, score (all 4 dims), scope, and status fields (PASS / HALT)
- [ ] Candidate queue created with header if it did not exist (PASS / HALT)
- [ ] Blank line separates new candidates from existing queue entries when appending (PASS / HALT)
- [ ] Queue capacity: total proposed entries in queue <= 25 after this cycle (PASS / HALT)
- [ ] Candidate appended ONLY to library/candidate-queue.md (PASS / HALT)
- [ ] No topic files created (discoverer proposes, does not write) (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (PASS / HALT)
- [ ] Logbook entry written to logbook/library.log (PASS / HALT)
- [ ] Logbook entry format: each data field on its own line, candidates listed one per bullet, matching the step 11 example exactly (PASS / HALT)
- [ ] Logbook entry properly separated: exactly one blank line between this entry and the previous. Verify: the line before the new `## [ENT-` header is blank, and the line before that is NOT blank (it is the previous entry's last content line). No double gaps, no merged entries. (PASS / HALT)
- [ ] Shared publication returned PASS; additions used queue.append with only new candidate blocks; no direct queue/log writes or Git staging outside the helper (PASS / HALT)
- [ ] Every outcome, including ERROR, recorded in library.log when safe publication was available; otherwise failure surfaced to the caller (PASS / HALT)
- [ ] Exact committed work verified on the remote mirror; a fresh unrelated watcher log line alone is insufficient (PASS / HALT)

## Procedure

### 1. Locate the brain working copy

VPS agents: `cd /srv/brain/agentic-brain`. The watcher keeps the
clone synchronized with GitHub. Read the Publication section of
`agentic-brain:library/guide-library.md` before preparing changes. Use the
helper's snapshot command to capture the queue and selected anchors/indexes
used for the decision. Read each captured file in full. Do not modify
the live clone while researching or preparing candidate drafts.

VPS-connected agents: no local clone. Every read and write below goes
through the Path Convention commands above.

### 2. Survey domain coverage

Read `library/index-library.md` -- the master index table lists every
domain with its live topic count and anchor description. Use the topic
counts to identify underrepresented domains.

The domain balance dimension uses this captured survey. Domains with fewer
topics receive higher balance scores, which increases their candidates'
chance of being proposed. Scores describe that research snapshot; do not
restart discovery because a queued topic becomes written or indexes refresh.

### 3. Select domains for this cycle

Select a subset of domains (recommended: 4-6 per cycle). Prioritize
domains with the fewest topics (balance-driven).

### 4. Read each selected domain anchor

For each selected domain, read
`library/<domain>/anchor-<domain>.md`. Note:
- The anchor paragraph (what the domain IS).
- Scope: In list (what belongs) and Out list (what does not).
- Adjacent domains and their boundary rules.
- Topic discovery guidance if present.

### 5. Scan existing topics in each domain

Read `library/<domain>/index-<domain>.md` for each selected domain.
This file lists every existing topic with its title, filename, and a
one-line teaser -- the full picture of what is already covered, in
one read per domain.

Build a mental map of what is already covered. Use the master index
at `library/index-library.md` for cross-domain awareness (topic
counts and descriptions across all current domains).

### 6. Identify knowledge gaps

For each domain, identify 1-3 knowledge gaps: topics that SHOULD exist
in this domain based on the anchor but do NOT yet have a topic file.
A good gap topic:
- Is clearly within the domain's In scope.
- Does not overlap an existing topic (> 30% semantic overlap = skip).
- Has not been proposed before (check candidate queue).
- Has not been rejected before (check library.log).

### 7. Score each candidate (4 dimensions; discovery weights)

Score each candidate across four dimensions using a 0.0-10.0 scale:

| Dimension | Weight | What it measures |
|:--|:--|:--|
| Gap score | 0.40 | How uncovered is this topic? Is this a known gap in domain coverage? |
| Knowledge compounding | 0.25 | Would this connect multiple existing topics? Fill a bridge between domains? |
| Timeliness | 0.20 | Currently relevant? Recent developments, new research, active debates? |
| Domain balance | 0.15 | Is this domain underrepresented vs others? Higher score for domains with fewer topics. |

Calculate weighted score: `(gap * 0.40) + (compounding * 0.25) + (timeliness * 0.20) + (balance * 0.15)`.

Domain balance scoring: assign 10 to the domain with the fewest topics
in this cycle, scale others proportionally. A domain with 0 topics =
balance 10. A domain with 50 topics next to one with 0 = balance 1-2.

No minimum threshold for discovery -- score all candidates. The queue
is capped at 25 proposed entries (see step 9).

### 8. Check for duplicates in queue

Read the captured `library/candidate-queue.md`. Before calculating capacity or
appending anything, compare every scored candidate against the
existing queue by title and scope.

If a candidate with a similar title or scope already exists and is
still `proposed`, skip it. If a prior candidate was `rejected`, note
the rejection reason and explain why this re-proposal is different.
Only non-duplicate candidates proceed to the capacity check.

### 9. Check queue capacity

Count every entry with `Status: proposed`. Calculate available slots:
`available = 25 - proposed_count`.

- If available <= 0: log to library.log "Queue at capacity (25)."
  Note the candidates that would have been proposed (titles and
  scores) in the logbook entry. Skip to step 11 (logbook).
- If available < number of non-duplicate scored candidates: sort by
  discovery score descending, take only the top `available`. The rest
  are dropped -- they may re-surface in future cycles.
- If available >= number of non-duplicate scored candidates: proceed
  normally.

### 10. Propose candidates to the queue

Propose up to `available` top-scored non-duplicate candidates. Prepare a
temporary file containing only the new candidate blocks in this format,
separated by blank lines. Do not copy the existing queue or include a header
or comments; the publisher appends these blocks to the current queue.

```markdown

## Candidate: <topic-title>
- **Domain:** <domain-slug>
- **Proposed by:** <agent-name>
- **Date:** YYYY-MM-DD
- **Discovery score:** X.X/10.0 (gap=X.X, compounding=X.X, timeliness=X.X, balance=X.X)
- **Scope:** <3-4 sentences, max 100 words total.>
- **Status:** proposed
```

If `candidate-queue.md` does not exist, the publisher creates its header.

### 11. Write logbook entry

Prepare the body for a `logbook/library.log` entry. The helper generates
the ENT number, UTC timestamp, actor, and `library` category under the lock;
do not append directly or include the header in the request's log body.
The resulting entry MUST follow this format. Each data field MUST be on its
own line. Candidates MUST be listed one per line using bullet points
(`-`). Do NOT pack multiple fields onto a single line. The archiving
system counts lines, not bytes -- single-line entries defeat
line-based archiving.

```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | <agent-name> | library | ref: library/candidate-queue.md
Discovery cycle: N domains scanned, M candidates proposed, K skipped (queue capped at 25).
Candidates:
- <title> (X.X): gap=X.X, compounding=X.X, timeliness=X.X, balance=X.X
- <title> (X.X): gap=X.X, compounding=X.X, timeliness=X.X, balance=X.X
Domain balance: <least-covered> (N topics) to <most-covered> (N topics).
```

Capacity/no-op outcomes use a log-only request. Unexpected failures use a
log-only body beginning `ERROR:` with the failed step and reason. If the
helper cannot publish safely, surface its HALT result to the caller; never
bypass the lock to write a failure entry. The helper preserves existing
entries and inserts exactly one separator line.

### 12. Commit on the VPS clone -- NO push

Follow `agentic-brain:library/guide-library.md#publication`.
Use `kind: discover`, empty `writes` and `expected`, `queue.append` pointing
to the new-candidates file, and the prepared log body. The helper checks the
current queue and appends the whole batch with its log in one commit. No
whole-queue, catalogue, or index freshness condition is required. If current
capacity or duplicate checks reject the batch, correct it and its log body;
never claim partial additions. Use `kind: log` without a queue operation for
capacity, no-op, or ERROR outcomes.

No direct append, `git add`, commit, pull, or rebase belongs in this cycle.
The existing `repo-pull.sh` watcher owns synchronization; its Brain log is
`/srv/brain/logs/brain-pull.log`. Verify the specific publication reached
GitHub after releasing the helper's lock.

## Related

- `agentic-brain:library/guide-library.md` -- pipeline architecture, v2 weights, anchor format
- `agentic-brain:research/insights/library-system.md` -- full system blueprint, anti-staleness design
- `agentic-brain:governance/skills/library-writer.md` -- writer skill (picks candidates from queue)
- `agentic-brain:governance/skills/library-reviewer.md` -- reviewer skill (refreshes existing topics)
- `agentic-brain:logbook/protocol.md` -- logbook entry format
