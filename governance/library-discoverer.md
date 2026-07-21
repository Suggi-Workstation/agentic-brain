---
name: library-discoverer
description: "Discover knowledge gaps in the library: scan domain anchors, identify uncovered topics, propose candidates for the writing process. Use when the discovery cron cycle fires."
user-invocable: false
disable-model-invocation: false
---

# Library Discoverer

## What This Skill Does

Guides the discovery process of the library pipeline. Scans all 24
domain anchors, identifies knowledge gaps, proposes new candidate
topics. Does NOT write topic files -- only proposes titles and brief
scopes for the writing process to pick up. Candidates are appended to
`library/candidate-queue.md`. For the full pipeline architecture and
weight rules, read `brain:library/guide-library.md` and
`brain:research/insights/library-system.md`.

## When to Invoke

Invoke when the cron scheduler triggers a discovery cycle. Runs before
the writing process to populate the candidate queue. Each cycle picks
a subset of domains and proposes 1-3 candidate topics per domain.

Skip for:
- Domains with no anchor file
- Topics already in the candidate queue
- Topics already covered by existing files (check filesystem)
- Topics previously rejected by the auditor (check library.log)

## Self-Check -- HARD GATE

Confirm ALL verification sections passed before committing.

- [ ] Procedure completed (clone, scan anchors, identify gaps, score, propose, verify, commit, push, discard) (PASS / HALT)
- [ ] Discovery Scoring verification: all items confirmed PASS (PASS / HALT)
- [ ] Queue verification: candidates appended, no duplicates created (PASS / HALT)
- [ ] File Output verification: all items confirmed PASS (PASS / HALT)
- [ ] Logbook entry written to library.log (PASS / HALT)

## Procedure

### 1. Clone the agentic-brain

```bash
cd /tmp && rm -rf brain-discover && git clone --depth 1 \
  "https://${OPEN...KEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-discover
```

### 2. Select domains for this cycle

List available domains:
```bash
ls -d /tmp/brain-discover/library/*/
```

Select a subset of domains for this cycle (recommended: 4-6 domains
per cycle to keep the queue manageable). Rotate domains across cycles
to ensure even coverage.

### 3. Read each selected domain anchor

For each selected domain, read
`/tmp/brain-discover/library/<domain>/anchor-<domain>.md`. Note:
- The anchor paragraph (what the domain IS).
- Scope: In list (what belongs) and Out list (what does not).
- Adjacent domains and their boundary rules.
- Topic discovery guidance if present.

### 4. Scan existing topics in each domain

```bash
ls /tmp/brain-discover/library/<domain>/*.md | grep -v anchor | grep -v quarantine
```

Build a mental map of what is already covered. Check the master index
at `library/index-library.md` for cross-domain awareness.

### 5. Identify knowledge gaps

For each domain, identify 1-3 knowledge gaps: topics that SHOULD exist
in this domain based on the anchor but do NOT yet have a topic file.
A good gap topic:
- Is clearly within the domain's In scope.
- Does not overlap an existing topic (> 30% semantic overlap = skip).
- Has not been proposed before (check candidate queue).
- Has not been rejected by the auditor (check library.log).

### 6. Score each candidate (discovery weight)

Score each candidate across three dimensions using a 0.0-10.0 scale:

| Dimension | Weight | What it measures |
|:--|:--|:--|
| Gap score | 0.5 | How uncovered is this topic? Is this a known gap in domain coverage? |
| Knowledge compounding | 0.3 | Would this connect multiple existing topics? Fill a bridge between domains? |
| Timeliness | 0.2 | Currently relevant? Recent developments, new research, active debates? |

Calculate weighted score: `(gap * 0.5) + (compounding * 0.3) + (timeliness * 0.2)`.

No minimum threshold for discovery -- all scored candidates are
proposed. The writer applies its own >= 7.0 threshold.

### 7. Propose candidates to the queue

Append each candidate to `/tmp/brain-discover/library/candidate-queue.md`
using this format:

```markdown
## Candidate: <topic-title>
- **Domain:** <domain-slug>
- **Proposed by:** <agent-name>
- **Date:** YYYY-MM-DD
- **Discovery score:** X.X/10.0 (gap=X.X, compounding=X.X, timeliness=X.X)
- **Scope:** <2-3 sentence scope description for the writer>
- **Status:** proposed
```

If `candidate-queue.md` does not exist, create it with a header:
`# Library Candidate Queue -- topics proposed for the writing process`.

### 8. Check for duplicates in queue

Before appending, scan existing queue entries. If a candidate with
similar title or scope already exists and is still `proposed`, skip it.
If a prior candidate was `rejected` by the auditor, note the rejection
reason and explain why this re-proposal is different.

## Format Verification -- HARD GATE (before commit)

Verify every item below. Each maps to the library guide rules. HALT on
any failure; fix before committing.

### Discovery Scoring

- [ ] Each candidate scored across all three dimensions (PASS / HALT)
- [ ] Each dimension has a brief justification (1-2 sentences) (PASS / HALT)
- [ ] Gap assessment verified against existing topics (no false gaps) (PASS / HALT)
- [ ] No candidate proposed for a domain without an anchor file (PASS / HALT)

### Queue

- [ ] Candidate queue format matches the specification (PASS / HALT)
- [ ] No duplicate candidates in the queue (checked by title and scope) (PASS / HALT)
- [ ] Each candidate has domain, score, scope, and status fields (PASS / HALT)
- [ ] Candidate queue created with header if it did not exist (PASS / HALT)

### File Output

- [ ] Candidate appended ONLY to library/candidate-queue.md (PASS / HALT)
- [ ] No topic files created (discoverer proposes, does not write) (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (PASS / HALT)

### 9. Write logbook entry

Append to `/tmp/brain-discover/logbook/library.log`:

```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | <agent-name> | library | ref: library/candidate-queue.md
Discovery cycle: <N> domains scanned, <N> candidates proposed.
Domains: <list>. Candidates: <list with scores>.
```

Include each candidate's title, domain, and discovery score in the
body.

### 10. Commit and push

```bash
cd /tmp/brain-discover
git add -A
git diff --cached --stat
git -c user.name="<agent-name>" -c user.email="<agent-email>" \
  commit -m "library: discovery cycle -- <N> candidates proposed"
git push origin main
```

If the push fails, pull first, resolve, then push.

### 11. Discard the clone

```bash
cd /tmp && rm -rf brain-discover
```

## Related

- `brain:library/guide-library.md` -- pipeline architecture, weights, anchor format
- `brain:research/insights/library-system.md` -- full system blueprint, anti-staleness design
- `brain:governance/library-writer.md` -- writer skill (picks candidates from queue)
- `brain:governance/library-auditor.md` -- auditor skill (reviews written topics)
- `brain:logbook/protocol.md` -- logbook entry format