---
name: library-health-monitor
description: "Weekly library health audit: staleness detection, domain balance, cross-domain redundancy, source rot, quality trendlines, and master index regeneration. Decorrelated from the Writer and Discoverer. Runs weekly, not per-topic."
user-invocable: false
disable-model-invocation: false
---

# Library Health Monitor

## What This Skill Does

Runs a weekly system-level health audit of the library. Unlike the Writer
(which produces individual topics and self-scores them) and the Discoverer
(which identifies knowledge gaps), the Health Monitor looks at the library
as a whole. It detects patterns that are invisible to per-topic processes:
staleness, domain imbalance, cross-domain redundancy, source rot, and
quality trends across cycles.

For the topic format specification, read `governance/template-library.md`.
For the full library architecture, read `library/guide-library.md`.

## When to Invoke

Invoke weekly via cron (suggested: `0 5 * * 0` -- Sunday 5 AM, after the
week's writing cycles have completed). Do NOT invoke per-topic or per-cycle.
This is a system-level audit, not a content-level review.

Skip for:
- No new topics written since the last health cycle
- Last health report is <5 days old

## Self-Check -- HARD GATE

Confirm ALL verification sections passed before committing.

- [ ] Procedure completed (clone, scan, analyze all 5 dimensions, regenerate index, write report, logbook, commit, push, discard) (PASS / HALT)
- [ ] Staleness scan complete: every topic checked for last-modification date, stale threshold applied (>90 days), results logged (PASS / HALT)
- [ ] Domain balance analyzed: topic count per domain derived from filesystem, imbalance ratios calculated, undercovered domains flagged (PASS / HALT)
- [ ] Cross-domain redundancy checked: semantic overlap flagged between adjacent domains, recommendations written (PASS / HALT)
- [ ] Source rot spot-checked: topics older than 6 months sampled, source URLs verified, findings logged (PASS / HALT)
- [ ] Quality trendline computed: average scores from the last 20 audited topics, dimension-level breakdown, trend direction stated (PASS / HALT)
- [ ] Index regenerated from live filesystem (R11: no hardcoded counts) (PASS / HALT)
- [ ] Health report written to `library/reports/health-<YYYY-MM-DD>.md` with all 5 sections + index summary (PASS / HALT)
- [ ] Logbook entry written to library.log (PASS / HALT)

## Procedure

### 1. Clone the agentic-brain

```bash
cd /tmp && rm -rf brain-monitor && git clone --depth 1 \
  "https://${OPENCLAW_GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-monitor
```

### 2. Read governance specs

Read the format specification and library guide to understand the
structure being audited:

```bash
cat /tmp/brain-monitor/governance/template-library.md
cat /tmp/brain-monitor/library/guide-library.md
```

### 3. Staleness scan

For every topic file under `library/<domain>/` (excluding anchors,
quarantine, and index files), check the file's modification date.

```bash
# List topics with their last-commit dates
cd /tmp/brain-monitor
git ls-files -- 'library/*/*.md' | grep -v 'anchor-' | grep -v 'index-' | \
  grep -v 'quarantine/' | while read f; do
    echo "$(git log -1 --format=%ai -- "$f") $f"
done
```

Stale threshold: >90 days since last modification. Flag all stale topics
with their domain and last-modified date. Group by domain.

For each stale topic, determine whether it needs refresh or retirement:
- Topics on stable domains (mathematics, physics fundamentals, history):
  lower urgency. Still flag for periodic review.
- Topics on evolving domains (technology, AI, current events, markets):
  high urgency. May contain outdated information.

### 4. Domain balance analysis

Derive topic counts per domain from the live filesystem:

```bash
cd /tmp/brain-monitor
for d in library/*/; do
  domain=$(basename "$d")
  count=$(find "$d" -maxdepth 1 -name '*.md' ! -name 'anchor-*' ! -name 'index-*' | wc -l)
  echo "$domain: $count"
done
```

Calculate imbalance ratios:
- Ratio of largest domain to smallest domain (non-zero).
- Mean topics per domain.
- Domains >2x above mean are OVERREPRESENTED.
- Domains <0.5x below mean are UNDERCOVERED.

Flag undercovered domains. The Discoverer should prioritize these in
future candidate proposals. Flag overrepresented domains -- the
Discoverer should de-prioritize or pause candidate generation for them
to allow other domains to catch up.

### 5. Cross-domain redundancy detection

Identify domain pairs with potential semantic overlap. This is a
qualitative assessment, not an automated computation:

- Read domain anchors for adjacent domains (e.g., `anchor-economics.md`
  and `anchor-investing.md`).
- Identify boundary topics: topics whose content spans both domains.
  Example: "Capital Cycle Analysis" in investing/ may overlap with
  "Business Cycles" in economics/.
- For each boundary topic found, read both the topic and the adjacent
  domain's topics.
- If overlap is significant (>50% shared concepts), flag for either:
  (a) cross-referencing between the two topics, or (b) merging into a
  single topic in the most appropriate domain, or (c) keeping separate
  with explicit scope boundaries.

Write recommendations. Never modify topic files -- only report.

### 6. Source rot detection

Sample topics older than 6 months. For each sampled topic:

- Pick 2-3 source URLs from the topic's citations/sources section.
- Attempt to fetch each URL via `web_fetch` or `curl -sI` (HEAD request).
- Classify:
  - **Healthy:** URL returns 200, content appears relevant.
  - **Redirected:** 301/302 -- note the new URL.
  - **Dead:** 404/410 -- source is gone.
  - **Inaccessible:** timeout, blocked, paywalled -- cannot verify.
- Sample size: min(5 topics, total eligible topics).

Report findings with a ROT RATE: dead sources / total sources checked.
If the rot rate is >20%, recommend a broader source audit.

### 7. Quality trendline

Read `logbook/library.log`. Extract the last 20 Writer logbook entries
(which include the self-assigned quality/core/scope/value scores).

Compute:
- Rolling average of quality scores across the last 20 topics.
- Dimension-level breakdown if available (core, scope, value, authority).
- Trend direction: improving (last 5 avg > first 5 avg), stable
  (within 0.5 points), or declining (last 5 avg < first 5 avg - 0.5).

Flag declining trends with specific dimension drill-down.

### 8. Regenerate master index

Use the index script to regenerate from filesystem:

```bash
cd /tmp/brain-monitor && python3 scripts/index-library.py
```

Verify R11 compliance: the script derives ALL counts from `ls` output.
No hardcoded numbers in the output.

### 9. Write health report

Create the report at `library/reports/health-<YYYY-MM-DD>.md`:

```markdown
---
name: library-health-report
id: <YYYYMMDDTHHMMSSZ>
tier: report
domain: library
author: <agent-name>
tags: [health, audit, library, staleness, balance, redundancy]
---

# Library Health Report -- YYYY-MM-DD

## Summary
<TBD -- populated from scan below>

## 1. Staleness
- Topics checked: N
- Stale topics (>90 days): M
- Stale topics per domain: <domain: count>
- High-urgency stale topics (evolving domains): X
- Recommendations: <specific actions>

## 2. Domain Balance
- Total domains: N
- Total topics: M
- Topics per domain: <domain: count>
- Overrepresented domains (>2x mean): <list>
- Undercovered domains (<0.5x mean): <list>
- Recommendations: <which domains to prioritize, which to pause>

## 3. Cross-Domain Redundancy
- Domain pairs checked: N
- Boundary topics identified: M
- Significant overlaps flagged: X
- Recommendations: <cross-reference, merge, or scope-boundary suggestions>

## 4. Source Rot
- Topics sampled: N
- Sources checked: M
- Dead sources: X
- Redirected sources: Y
- Rot rate: X/M (percentage)
- Recommendations: <specific actions>

## 5. Quality Trendline
- Topics in sample: 20
- Average quality score: X.X
- Trend: improving/stable/declining
- Dimension breakdown: core-X.X, scope-X.X, value-X.X, authority-X.X
- Recommendations: <specific actions>

## 6. Index Summary
- Total topics: N
- Audited topics: M (percentage)
- Domains: D
- Index regenerated at: <timestamp>
```

### 10. Write logbook entry

Append to `/tmp/brain-monitor/logbook/library.log`:

```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | <agent-name> | library | ref: library/reports/health-<YYYY-MM-DD>.md
Weekly health monitor cycle. N topics across D domains.
Staleness: M stale topics (>90 days).
Domain balance: imbalance ratio X:1. Undercovered: <domains>.
Cross-domain redundancy: X boundary overlaps flagged.
Source rot: X/Y sources dead (Z% rot rate).
Quality trendline: avg X.X/10.0, <direction>.
Index regenerated: N topics, D domains.
```

Increment ENT counter from the last entry in library.log.

### 11. Commit and push

```bash
cd /tmp/brain-monitor
git -c user.name="<agent-name>" -c user.email="<agent-email>" \
  add -A
git -c user.name="<agent-name>" -c user.email="<agent-email>" \
  commit -m "library: health monitor cycle -- <date> (N topics, D domains, M stale)"
git push origin main
```

### 12. Discard the clone

```bash
cd /tmp && rm -rf brain-monitor
```

## Related

- `governance/template-library.md` -- topic format specification
- `library/guide-library.md` -- full library architecture
- `governance/skills/library-writer.md` -- writer skill (produces topics)
- `governance/skills/library-discoverer.md` -- discoverer skill (proposes candidates)
- `governance/skills/library-auditor.md` -- per-topic auditor (content-level review, legacy)
- `logbook/protocol.md` -- logbook entry format
