---
name: library-auditor
description: "Audit written library topics: review quality, redundancy, and anchor compliance. Regenerate master index from filesystem. Use when new topics have been written since last audit cycle."
user-invocable: false
disable-model-invocation: false
---

# Library Auditor

## What This Skill Does

Guides the audit process of the library pipeline. Reviews recently
written topic files for quality, redundancy, and anchor compliance.
Regenerates the master index from the live filesystem after each cycle.
Decorrelated from the writing process (different model or different
system prompt emphasis). For the full pipeline architecture and weight
rules, read `brain:library/guide-library.md` and
`brain:research/insights/library-system.md`.

## When to Invoke

Invoke when the cron scheduler triggers an audit cycle. The auditor
picks the most recently written (unaudited) topics and evaluates them.
Runs after the writing process has produced new files.

Skip for:
- No unaudited topics since the last audit cycle
- Topics already audited (check library.log for prior audit entries)
- Topics in quarantine directory

## Self-Check -- HARD GATE

Confirm ALL verification sections passed before committing.

- [ ] Procedure completed (clone, find unaudited, review, score, regenerate index, verify, commit, push, discard) (PASS / HALT)
- [ ] Audit Scoring verification: all items confirmed PASS (PASS / HALT)
- [ ] Index verification: regenerated from filesystem, no hardcoded counts (PASS / HALT)
- [ ] File Output verification: all items confirmed PASS (PASS / HALT)
- [ ] Logbook entry written to library.log (PASS / HALT)

## Procedure

### 1. Clone the agentic-brain

```bash
cd /tmp && rm -rf brain-audit && git clone --depth 1 \
  "https://${OPEN...KEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-audit
```

### 2. Find unaudited topics

Read `/tmp/brain-audit/logbook/library.log`. Identify topics written
since the last audit cycle (look for `category: library` entries from
the Writer). Cross-reference with the filesystem:
`ls /tmp/brain-audit/library/<domain>/*.md` to confirm files exist.

Select the most recent unaudited topics (up to 5 per audit cycle).

### 3. Read each topic and its domain anchor

For each topic:
- Read the topic file at `library/<domain>/<topic-slug>.md`.
- Read the domain anchor at `library/<domain>/anchor-<domain>.md`.
- Read adjacent domain anchors if boundary rules apply.

### 4. Score each topic (auditor weight)

Score each topic across three dimensions using a 0.0-10.0 scale:

| Dimension | Weight | What it measures |
|:--|:--|:--|
| Quality | 0.4 | Factual accuracy, completeness, source citations, ASCII compliance, structural correctness. |
| Redundancy | 0.3 | Semantic overlap with other topics in same or adjacent domains. |
| Anchor compliance | 0.3 | Does the topic stay within the anchor's scope? Would it fit better in an adjacent domain? |

Calculate weighted score: `(quality * 0.4) + (redundancy * 0.3) + (anchor * 0.3)`.

- >= 7.0: APPROVE. Add `audited: true` and `audit-score: X.X` to the
  topic file's frontmatter.
- 5.0-6.9: FLAG. Log specific change requests for the writer. Do not
  modify the topic file.
- < 5.0: REJECT. Move the topic file to
  `library/<domain>/quarantine/<topic-slug>.md` and log the reason.

### 5. Regenerate the master index

Regenerate `library/index-library.md` from the live filesystem. The
index MUST NOT contain hardcoded counts (R11). Derive everything from
`ls library/<domain>/*.md`.

```bash
cd /tmp/brain-audit
for domain in library/*/; do
  domain_name=$(basename "$domain")
  count=$(ls "$domain"*.md 2>/dev/null | grep -v anchor | grep -v quarantine | wc -l)
  echo "- **$domain_name**: $count topics"
done
```

Write the output to `library/index-library.md` with a timestamp header
and the audit cycle number.

### 6. Score the audit cycle itself (meta-audit)

Score the overall audit cycle quality for continuous improvement.
Log to library.log.

## Format Verification -- HARD GATE (before commit)

Verify every item below. Each maps to the library guide rules. HALT on
any failure; fix before committing.

### Audit Scoring

- [ ] Every unaudited topic scored across all three dimensions (PASS / HALT)
- [ ] Each dimension has a brief justification (1-2 sentences) (PASS / HALT)
- [ ] Weighted score calculated correctly (quality*0.4 + redundancy*0.3 + anchor*0.3) (PASS / HALT)
- [ ] Verdict applied correctly: APPROVE (>=7.0), FLAG (5.0-6.9), REJECT (<5.0) (PASS / HALT)
- [ ] APPROVE topics: frontmatter updated with audited=true and audit-score (PASS / HALT)
- [ ] FLAG topics: change requests logged with specific, actionable items (PASS / HALT)
- [ ] REJECT topics: moved to quarantine directory (PASS / HALT)

### Index

- [ ] Master index regenerated from live filesystem (not edited by hand) (PASS / HALT)
- [ ] Zero hardcoded counts (R11): all counts derived from `ls` output (PASS / HALT)
- [ ] Index includes timestamp header and audit cycle number (PASS / HALT)

### File Output

- [ ] Topic files modified only for APPROVE verdicts (frontmatter update) (PASS / HALT)
- [ ] No topic content modified (auditor reviews, does not rewrite) (PASS / HALT)
- [ ] Quarantine directory created if it did not exist (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in modified files (PASS / HALT)

### 7. Write logbook entry

Append to `/tmp/brain-audit/logbook/library.log` for each audited topic:

```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | <agent-name> | library | ref: library/<domain>/<topic-slug>.md | see: <writer-ent-id>
Audited topic <title>. Verdict: APPROVE/FLAG/REJECT. Weighted score: X.X/10.0
(quality=X.X, redundancy=X.X, anchor=X.X). <change requests if FLAG>.
<quarantine path if REJECT>.
```

Also append a summary entry for the index regeneration and meta-audit
score.

### 8. Commit and push

```bash
cd /tmp/brain-audit
git add -A
git diff --cached --stat
git -c user.name="<agent-name>" -c user.email="<agent-email>" \
  commit -m "library: audit cycle <N> -- <N> topics reviewed"
git push origin main
```

If the push fails, pull first, resolve, then push.

### 9. Discard the clone

```bash
cd /tmp && rm -rf brain-audit
```

## Related

- `brain:library/guide-library.md` -- pipeline architecture, weights, anchor format, index rules
- `brain:research/insights/library-system.md` -- full system blueprint, decorrelation rule
- `brain:governance/library-writer.md` -- writer skill (produces topics for audit)
- `brain:governance/library-discoverer.md` -- discoverer skill (proposes candidates)
- `brain:logbook/protocol.md` -- logbook entry format