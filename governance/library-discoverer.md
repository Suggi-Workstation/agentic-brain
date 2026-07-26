---
name: library-discoverer
description: "Discover knowledge gaps in the library: scan domain anchors, identify uncovered topics, score across 4 dimensions including domain balance. Propose candidates for the writing process. Use when the discovery cron cycle fires."
user-invocable: false
disable-model-invocation: false
---

# Library Discoverer (v2)

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

- [ ] Procedure completed (clone, select domains, scan anchors, identify gaps, score all 4 dimensions, check capacity, propose, check duplicates, verify, commit, push, discard) (PASS / HALT)
- [ ] Discovery Scoring verification: all 4 dimensions scored, weighted sum calculated (PASS / HALT)
- [ ] Domain Balance: underrepresented domains prioritized (PASS / HALT)
- [ ] Queue verification: candidates appended, no duplicates created (PASS / HALT)
- [ ] Queue capacity: total proposed entries in queue does not exceed 25 after cycle (PASS / HALT)
- [ ] File Output verification: all items confirmed PASS (PASS / HALT)
- [ ] Logbook entry written to library.log (PASS / HALT)

## Procedure

### 1. Clone the agentic-brain

```bash
cd /tmp && rm -rf brain-discover && git clone --depth 1 \
  "https://${OPENCLAW_GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-discover
```

### 2. Survey domain coverage

Count topics per domain to identify underrepresented domains:

```bash
cd /tmp/brain-discover
for domain in library/*/; do
  name=$(basename "$domain")
  count=$(ls "$domain"*.md 2>/dev/null | grep -v anchor | grep -v quarantine | wc -l)
  echo "$name: $count"
done
```

The domain balance dimension uses this survey. Domains with fewer
topics receive higher balance scores, which increases their
candidates' chance of being proposed. This prevents the library
from skewing toward a few well-covered domains while others stay
empty.

### 3. Select domains for this cycle

Select a subset of domains (recommended: 4-6 per cycle). Prioritize:
1. Domains with the fewest topics (balance-driven).
2. Domains not visited in the last 3 cycles (coverage-driven).
3. At least one domain from each major category (investing, science,
   human/social, global, thinking) for breadth.

### 4. Read each selected domain anchor

For each selected domain, read
`/tmp/brain-discover/library/<domain>/anchor-<domain>.md`. Note:
- The anchor paragraph (what the domain IS).
- Scope: In list (what belongs) and Out list (what does not).
- Adjacent domains and their boundary rules.
- Topic discovery guidance if present.

### 5. Scan existing topics in each domain

```bash
ls /tmp/brain-discover/library/<domain>/*.md | grep -v anchor | grep -v quarantine
```

Build a mental map of what is already covered. Check the master index
at `library/index-library.md` for cross-domain awareness.

### 6. Identify knowledge gaps

For each domain, identify 1-3 knowledge gaps: topics that SHOULD exist
in this domain based on the anchor but do NOT yet have a topic file.
A good gap topic:
- Is clearly within the domain's In scope.
- Does not overlap an existing topic (> 30% semantic overlap = skip).
- Has not been proposed before (check candidate queue).
- Has not been rejected by the auditor (check library.log).

### 7. Score each candidate (discovery weight, v2: 4 dimensions)

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

No minimum threshold for discovery -- score all candidates. The
writer applies its own >= 7.0 threshold. The queue itself is capped
at 25 proposed entries (see step 8).

### 8. Check queue capacity

Read `/tmp/brain-discover/library/candidate-queue.md`. Count every
entry with `Status: proposed`. Calculate available slots:
`available = 25 - proposed_count`.

- If available <= 0: log to library.log "Queue at capacity (25)."
  Note the candidates that would have been proposed (titles and
  scores) in the logbook entry. Skip to step 11 (logbook).
- If available < number of scored candidates: sort by discovery
  score descending, take only the top `available`. The rest are
  dropped -- they may re-surface in future cycles.
- If available >= number of scored candidates: proceed normally.

### 9. Propose candidates to the queue

Propose up to `available` top-scored candidates. Append each to
`/tmp/brain-discover/library/candidate-queue.md` using this format. If the queue already has entries, add a blank line
before the first `## Candidate:` block to separate the new candidates
from existing entries.

```markdown

## Candidate: <topic-title>
- **Domain:** <domain-slug>
- **Proposed by:** <agent-name>
- **Date:** YYYY-MM-DD
- **Discovery score:** X.X/10.0 (gap=X.X, compounding=X.X, timeliness=X.X, balance=X.X)
- **Scope:** <2-3 sentence scope description for the writer>
- **Status:** proposed
```

If `candidate-queue.md` does not exist, create it with a header:
`# Library Candidate Queue -- topics proposed for the writing process`.

### 10. Check for duplicates in queue

Before appending, scan existing queue entries. If a candidate with
similar title or scope already exists and is still `proposed`, skip it.
If a prior candidate was `rejected` by the auditor, note the rejection
reason and explain why this re-proposal is different.

## Format Verification -- HARD GATE (before commit)

Verify every item below. Each maps to the library guide rules. HALT on
any failure; fix before committing.

### 11. Write logbook entry

Append to `/tmp/brain-discover/logbook/library.log`. The logbook
entry MUST follow this exact format. Each data field MUST be on its
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

Increment ENT counter from the last entry in library.log.

### 11a. Log errors (if any)

If any step failed or produced unexpected results (clone failed,
push rejected, file write error, or any crash), append to
`/tmp/brain-discover/logbook/errors.log`:

```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | <agent-name> | error | ref: library/candidate-queue.md | see: <related-ent-id>
<description of what went wrong, what was expected, and any partial results>
```

Only write to errors.log if something actually failed. Successful
discovery cycles go to library.log. Errors.log is for unexpected
failures only.

### Discovery Scoring

- [ ] Each candidate scored across all four dimensions (PASS / HALT)
- [ ] Each dimension has a brief justification (1-2 sentences) (PASS / HALT)
- [ ] Weighted score calculated correctly: (gap*0.40 + compounding*0.25 + timeliness*0.20 + balance*0.15) (PASS / HALT)
- [ ] Gap assessment verified against existing topics (no false gaps) (PASS / HALT)
- [ ] Domain balance score derived from topic count survey in step 2 (PASS / HALT)
- [ ] No candidate proposed for a domain without an anchor file (PASS / HALT)

### Domain Balance

- [ ] Topic count survey completed before selecting domains (PASS / HALT)
- [ ] Underrepresented domains prioritized in domain selection (PASS / HALT)
- [ ] At least one domain from each major category included (PASS / HALT)
- [ ] Balance dimension score reflects actual topic counts, not assumed (PASS / HALT)

### Queue

- [ ] Candidate queue format matches the specification (PASS / HALT)
- [ ] No duplicate candidates in the queue (checked by title and scope) (PASS / HALT)
- [ ] Each candidate has domain, score (all 4 dims), scope, and status fields (PASS / HALT)
- [ ] Candidate queue created with header if it did not exist (PASS / HALT)
- [ ] Blank line separates new candidates from existing queue entries when appending (PASS / HALT)
- [ ] Queue capacity: total proposed entries in queue <= 25 after this cycle (PASS / HALT)

### File Output

- [ ] Candidate appended ONLY to library/candidate-queue.md (PASS / HALT)
- [ ] No topic files created (discoverer proposes, does not write) (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (PASS / HALT)
- [ ] Logbook entry format: each data field on its own line, candidates listed one per bullet, matching the step 11 example exactly (PASS / HALT)
- [ ] Logbook entry properly separated: a blank line precedes this entry in library.log. Verify with: `tail -n +<last-ent-line> /tmp/brain-discover/logbook/library.log | head -2` -- the first line must be empty. No entries merged without spacing. (PASS / HALT)

### 12. Commit and push

```bash
cd /tmp/brain-discover
git add -A
git diff --cached --stat
git -c user.name="<agent-name>" -c user.email="<agent-email>" \
  commit -m "library: discovery cycle -- N candidates proposed across M domains"
git push origin main
```

If the push fails, pull first, resolve, then push.

### 13. Discard the clone

```bash
cd /tmp && rm -rf brain-discover
```

## Related

- `library/guide-library.md` -- pipeline architecture, v2 weights, anchor format
- `research/insights/library-system.md` -- full system blueprint, anti-staleness design
- `governance/library-writer.md` -- writer skill (picks candidates from queue)
- `governance/library-auditor.md` -- auditor skill (reviews written topics)
- `logbook/protocol.md` -- logbook entry format
