---
name: library-auditor
description: "Audit written library topics: review quality, redundancy, anchor compliance, and source verification across 4 dimensions. Regenerate master index from filesystem. Use when new topics have been written since last audit cycle."
user-invocable: false
disable-model-invocation: false
---

# Library Auditor (v2)

## What This Skill Does

Guides the audit process of the library pipeline. Reviews recently
written topic files across 4 dimensions: quality, redundancy, anchor
compliance, and source verification. Regenerates the master index from
the live filesystem after each cycle. Decorrelated from the writing
process (different model or different system prompt emphasis). For the
full pipeline architecture and weight rules, read
`library/guide-library.md` and
`research/insights/library-system.md`.
For the topic format specification the auditor verifies against, read
`governance/template-library.md`.

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

- [ ] Procedure completed (clone, find unaudited, read, score all 4 dimensions, verdict, regenerate index, verify, commit, push, discard) (PASS / HALT)
- [ ] Audit Scoring verification: all 4 dimensions scored, weighted sum calculated (PASS / HALT)
- [ ] Source Verification: spot-check completed on 2-3 claims per topic (PASS / HALT)
- [ ] Index verification: regenerated from filesystem, no hardcoded counts (PASS / HALT)
- [ ] File Output verification: all items confirmed PASS (PASS / HALT)
- [ ] Logbook entry written to library.log (PASS / HALT)

## Procedure

### 1. Clone the agentic-brain

```bash
cd /tmp && rm -rf brain-audit && git clone --depth 1 \
  "https://${OPENCLAW_GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-audit
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

### 4. Verify sources (spot-check)

For each topic, pick 2-3 claims that cite specific sources. Attempt
to verify that the source actually supports the claim:
- Read the source URL if accessible.
- Check that the cited claim is present in the source.
- Note any misrepresentations, fabrications, or loose paraphrasing.

Score source verification on a 0.0-10.0 scale:
- **8-10:** All spot-checked claims verified. Sources accurately cited.
- **5-7:** Most claims verified. Minor paraphrasing issues.
- **1-4:** Claims misrepresented or sources do not support them.
- **0:** Unable to verify (paywalled, inaccessible) -- note this.

### 5. Score each topic (auditor weight, v2: 4 dimensions)

Score each topic across four dimensions using a 0.0-10.0 scale:

| Dimension | Weight | What it measures |
|:--|:--|:--|
| Quality | 0.35 | Factual accuracy, completeness, source citations, ASCII compliance, structural correctness. Includes frontmatter verification: all required fields present (name, id, tier, domain, author, tags, links), id matches `date -u` format, no human-rounded timestamps. |
| Redundancy | 0.25 | Semantic overlap with other topics in same or adjacent domains. |
| Anchor compliance | 0.30 | Does the topic stay within the anchor's scope? Would it fit better in an adjacent domain? |
| Source verification | 0.10 | Do the cited sources actually support the claims? Based on the spot-check from step 4. |

Calculate weighted score: `(quality * 0.35) + (redundancy * 0.25) + (anchor * 0.30) + (source * 0.10)`.

- >= 7.0: APPROVE. Add `audited: true` and `audit-score: X.X` to the
  topic file's frontmatter.
- 5.0-6.9: FLAG. Log specific change requests for the writer. Do not
  modify the topic file.
- < 5.0: REJECT. Move the topic file to
  `library/<domain>/quarantine/<topic-slug>.md` and log the reason.

### 6. Regenerate the master index

Run the index regeneration script. This derives all counts from the
live filesystem (R11: never hardcode):

```bash
cd /tmp/brain-audit && python scripts/index-library.py
```

The script:
- Scans every domain folder via `ls`.
- Counts topic files (excluding anchors and quarantine).
- Counts audited topics by checking frontmatter for `audited: true`.
- Writes `library/index-library.md` with a UTC timestamp header (via `scripts/index-library.py`).
- Prints a summary with total topics, domains, and audited counts.

The script is the single source of truth for index generation. The
auditor MUST use this script, never regenerate the index by hand.

### 7. Write logbook entry

Append to `/tmp/brain-audit/logbook/library.log` for each audited
topic. The logbook entry MUST follow this exact format. Each data
field MUST be on its own line. Do NOT pack multiple fields onto a
single line.

```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | <agent-name> | library | ref: library/<domain>/<topic-slug>.md | see: <writer-ent-id>
Audited topic <title>.
Verdict: APPROVE/FLAG/REJECT. Weighted score: X.X/10.0
(quality=X.X, redundancy=X.X, anchor=X.X, source=X.X).
Source check: N/N claims verified.
```

If FLAG: add a line listing the required changes.
If REJECT: add a line with the quarantine path.

Increment ENT counter from the last entry in library.log.

### 7a. Log errors (if any)

If any step in this procedure failed or produced unexpected results,
append to `/tmp/brain-audit/logbook/errors.log`:

```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | <agent-name> | error | ref: library/<domain>/<topic-slug>.md | see: <related-ent-id>
<description of what went wrong, what was expected, and any partial results>
```

This allows other agents to identify and fix pipeline failures.
Only write to errors.log if something actually failed. Successful
operations go to library.log (step 7).

## Format Verification -- HARD GATE (before commit)

Verify every item below. Each maps to the library guide rules. HALT on
any failure; fix before committing.

### Audit Scoring

- [ ] Every unaudited topic scored across all four dimensions (PASS / HALT)
- [ ] Each dimension has a brief justification (1-2 sentences) (PASS / HALT)
- [ ] Weighted score calculated correctly: (quality*0.35 + redundancy*0.25 + anchor*0.30 + source*0.10) (PASS / HALT)
- [ ] Verdict applied correctly: APPROVE (>=7.0), FLAG (5.0-6.9), REJECT (<5.0) (PASS / HALT)
- [ ] APPROVE topics: frontmatter updated with audited=true and audit-score (PASS / HALT)
- [ ] FLAG topics: change requests logged with specific, actionable items (PASS / HALT)
- [ ] REJECT topics: moved to quarantine directory (PASS / HALT)

### Source Verification

- [ ] 2-3 claims spot-checked per topic against cited sources (PASS / HALT)
- [ ] Source verification score has justification (what was checked, what was found) (PASS / HALT)
- [ ] Inaccessible sources noted (paywalled, not "assumed correct") (PASS / HALT)

### Index

- [ ] Master index regenerated from live filesystem (not edited by hand) (PASS / HALT)
- [ ] Zero hardcoded counts (R11): all counts derived from `ls` output (PASS / HALT)
- [ ] Index includes timestamp header, audit cycle number, and audited/unadited breakdown (PASS / HALT)

### File Output

- [ ] Topic files modified only for APPROVE verdicts (frontmatter update) (PASS / HALT)
- [ ] No topic content modified (auditor reviews, does not rewrite) (PASS / HALT)
- [ ] Quarantine directory created if it did not exist (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in modified files (PASS / HALT)
- [ ] Logbook entry format: each data field on its own line, matching the step 7 example exactly (PASS / HALT)

### 8. Commit and push

```bash
cd /tmp/brain-audit
git add -A
git diff --cached --stat
git -c user.name="<agent-name>" -c user.email="<agent-email>" \
  commit -m "library: audit cycle -- N topics reviewed (M approved, P flagged, Q rejected)"
git push origin main
```

If the push fails, pull first, resolve, then push.

### 9. Discard the clone

```bash
cd /tmp && rm -rf brain-audit
```

## Related

- `governance/template-library.md` -- topic format specification the auditor verifies against
- `library/guide-library.md` -- pipeline architecture, v2 weights, anchor format, index rules
- `research/insights/library-system.md` -- full system blueprint, decorrelation rule
- `skills/library-writer.md` -- writer skill (produces topics for audit)
- `skills/library-discoverer.md` -- discoverer skill (proposes candidates)
- `logbook/protocol.md` -- logbook entry format
