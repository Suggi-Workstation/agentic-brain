---
name: library-auditor-test
id: 20260722T184716Z
tier: proposal
author: Link
tags: [library, auditor, test, pipeline]
links:
  - governance/library-auditor.md
  - governance/template-library.md
  - library/guide-library.md
  - research/proposals/library-writer-test.md
---

# Library Auditor Test -- Verify Review and Index

## Problem

After the writer produces topic files, the auditor must find unaudited
topics, read each topic and its domain anchor, spot-check 2-3 claims
against cited sources, score across 4 dimensions, issue a verdict
(APPROVE/FLAG/REJECT), and regenerate the master index. This has never
been tested with real topics. Without a test run, we do not know whether
source verification works (many academic sources are paywalled),
whether the decorrelated model catches issues the writer missed, or
whether the index regeneration script produces correct counts.

## Proposed Solution

Run one auditor cron cycle on Researcher-1 after the writer has
produced at least one topic file. Verify outputs against acceptance
criteria:

1. **Per-topic verdict:** Every unaudited topic scored across 4
   dimensions (quality 0.35, redundancy 0.25, anchor compliance 0.30,
   source verification 0.10) with justifications; weighted score
   calculated correctly.
2. **APPROVE verdict (>= 7.0):** frontmatter updated with
   `audited: true` and `audit-score: X.X`. No other content modified.
3. **FLAG verdict (5.0-6.9):** change requests logged to library.log
   with specific actionable items. Topic file not modified.
4. **REJECT verdict (< 5.0):** topic moved to
   `library/<domain>/quarantine/<topic-slug>.md`. Quarantine directory
   created if needed.
5. **Source verification:** 2-3 claims spot-checked per topic.
   Results recorded with justification. Inaccessible sources noted
   as "unable to verify."
6. **Master index:** `library/index-library.md` regenerated via
   `python scripts/index-library.py`. Zero hardcoded counts (R11). Topic
   count matches `ls library/*/*.md | wc -l`. Audited count matches
   topics with `audited: true`.
7. `logbook/library.log`: one entry per audited topic + one summary
   entry for index regeneration. ENT counters incremented.
8. `logbook/errors.log`: no new entry.

## Impact

- **Positive:** Validates the final pipeline phase. Exercises source
  verification, decorrelated review, and index regeneration. Produces
  the first audited topic with an audit trail. The regenerated index
  provides the first real snapshot of library content.
- **Risk:** Low. The auditor modifies topic frontmatter only (APPROVE
  verdicts), moves files to quarantine (REJECT), or logs change
  requests (FLAG). No topic content is rewritten. Index regeneration
  is deterministic -- a failed run can be re-executed.
- **Cost:** One cron cycle. Model: GPT-5.4 via Copilot free ($0).
  Source verification may require web fetching (free tier). Context
  load moderate -- skill + topics + anchors + scripts/index-library.py.

## Open Questions

1. With only 1-2 topics in the library, is the redundancy dimension
   (0.25 weight) meaningful? Redundancy against what -- an empty
   library?
2. Will source verification work? Academic papers at paywalled URLs
   return "unable to verify" (score 0). If every topic's sources are
   paywalled, source verification = 0 for all topics. Is this fair,
   or should we adjust the weight?
3. Will the auditor identify the writer's ENT ID for the `see:`
   reference? The auditor reads library.log to find writer entries --
   if the format is inconsistent, cross-referencing breaks.
4. With 0 audited topics before this run, the index will show `0
   audited` for every domain. The first audit cycle always shows this.
   It is correct but looks incomplete.

## Approval Gate

If approved, Ava deploys the auditor cron on Researcher-1 after the
writer run completes and topic files exist. Compare actual outputs
against acceptance criteria. File deviations as errors or skill
patches.

## Cross-Links

- `governance/library-auditor.md` -- the skill being tested
- `governance/template-library.md` -- format the auditor verifies against
- `library/guide-library.md` -- pipeline architecture and weights
- `research/proposals/library-writer-test.md` -- prerequisite test
