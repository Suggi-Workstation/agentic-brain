---
name: library-auditor-test
id: 20260722T184716Z
tier: proposal
author: Link
tags: [library, auditor, test, pipeline, expected-results]
links: [governance/library-auditor.md, governance/template-library.md, library/guide-library.md, proposals/library-writer-test.md]
---

# Library Auditor Test -- Expected Results

## Purpose

This proposal defines the expected outputs when Researcher-1 runs the
`library-auditor` skill after the writer has produced topic files. The
auditor must find unaudited topics, read each topic and its domain
anchor, spot-check sources, score across 4 dimensions, issue a verdict,
and regenerate the master index.

This document is the acceptance criteria. Compare actual outputs against
these expectations after the test run.

## Prerequisites

- At least one topic file exists at `library/<domain>/<topic-slug>.md`
- The topic's `audited` field is either absent or `false`
- The domain anchor exists at `library/<domain>/anchor-<domain>.md`
- `library/index.py` exists and is runnable

## Expected Outputs

### 1. Audit verdict per topic

Each unaudited topic receives a verdict based on weighted score:

| Verdict | Score range | Action |
|:--|:--|:--|
| APPROVE | >= 7.0 | Add `audited: true` and `audit-score: X.X` to frontmatter |
| FLAG | 5.0-6.9 | Log change requests. Do NOT modify the topic file |
| REJECT | < 5.0 | Move to `library/<domain>/quarantine/<topic-slug>.md` |

Scoring dimensions:

| Dimension | Weight | What it measures |
|:--|:--|:--|
| Quality | 0.35 | Factual accuracy, completeness, citations, ASCII, structure, frontmatter |
| Redundancy | 0.25 | Semantic overlap with other topics in same/adjacent domains |
| Anchor compliance | 0.30 | Stays within anchor scope? Would it fit better in adjacent domain? |
| Source verification | 0.10 | Do cited sources support the claims? From spot-check |

Acceptance criteria:
- Every unaudited topic scored across all 4 dimensions
- Each dimension has a brief justification (1-2 sentences)
- Weighted score calculated correctly
- Verdict applied correctly based on score threshold

### 2. APPROVE verdict -- frontmatter update

Topic file frontmatter gains two fields:
```yaml
audited: true
audit-score: 8.4
```

Acceptance criteria:
- Only APPROVE topics modified (>= 7.0)
- No topic content modified (auditor reviews, does not rewrite)
- No other frontmatter fields changed
- ASCII-only after modification

### 3. FLAG verdict -- change requests logged

Acceptance criteria:
- Specific, actionable change requests written to library.log
- Topic file NOT modified
- Change requests identify what is wrong AND what would fix it

### 4. REJECT verdict -- quarantine

Acceptance criteria:
- Topic file moved to `library/<domain>/quarantine/<topic-slug>.md`
- Quarantine directory created if it did not exist
- Original location cleaned up (no orphan file)

### 5. Master index regenerated

The auditor runs `python library/index.py` which:
- Scans every domain folder via `ls`
- Counts topic files (excluding anchors and quarantine)
- Counts audited topics by checking for `audited: true` in frontmatter
- Writes `library/index-library.md` with a UTC timestamp header

Acceptance criteria:
- `index-library.md` is regenerated (timestamp updated)
- Zero hardcoded counts (R11): all derived from live filesystem
- Total topic count matches `ls library/*/*.md | grep -v anchor | grep -v quarantine | wc -l`
- Audited count matches topics with `audited: true` in frontmatter

### 6. Source verification spot-check

For each topic, 2-3 claims are verified against cited sources:
- Source URL accessed if possible
- Claim checked against source content
- Score: 8-10 (verified), 5-7 (minor issues), 1-4 (misrepresented), 0 (paywalled)

Acceptance criteria:
- Spot-check results recorded with justification
- Inaccessible sources noted as "unable to verify" (not assumed correct)
- If all sources are paywalled, source verification score is 0 but topic is not automatically rejected

### 7. library.log entry

For each audited topic:
```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | Researcher-1 | library | ref: library/<domain>/<topic-slug>.md | see: <writer-ent-id>
Audited topic <title>. Verdict: APPROVE/FLAG/REJECT. Weighted score: X.X/10.0
(quality=X.X, redundancy=X.X, anchor=X.X, source=X.X).
Source check: N/N claims verified. <change requests if FLAG>.
<quarantine path if REJECT>.
```

Plus a summary entry for index regeneration:
```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | Researcher-1 | library | ref: library/index-library.md
Index regenerated: N topics across M domains (P audited).
```

Acceptance criteria:
- One entry per audited topic + one summary entry for index
- ENT counters increment from last library.log entry

### 8. errors.log (expected: no entry)

Same as other tests. No error entry unless something genuinely failed.

## Edge Cases

| Scenario | Expected behavior |
|:--|:--|
| No unaudited topics | Log to library.log, exit |
| Topic with no anchor file | Flag it -- anchor compliance = 0 |
| Topic in quarantine directory | Skip (already rejected) |
| Source URLs unreachable | Source verification = 0, note "unable to verify" |
| Push conflict on index | Pull --rebase, resolve, push |
| index.py fails | Log to errors.log, do not hand-edit the index |

## Open Questions

1. With only 1-2 topics (from the writer test), will redundancy (0.25 weight) be meaningful? Redundancy in a near-empty library is hard to assess.
2. Will source verification work? The writer will cite academic papers (high authority) -- many are paywalled. If all sources are inaccessible, source verification = 0 for every topic. Is this fair?
3. Will the auditor identify the writer's ENT ID for the `see:` reference? The auditor reads library.log to find writer entries -- this cross-referencing requires format consistency.
4. With 0 topics audited, the index will show `0 audited` for every domain. The first audit cycle will always show this -- it's correct but looks incomplete.

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1.0 | 2026-07-22 | Link | Initial test specification |
