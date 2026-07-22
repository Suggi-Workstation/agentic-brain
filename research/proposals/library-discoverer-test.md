---
name: library-discoverer-test
id: 20260722T184716Z
tier: proposal
author: Link
tags: [library, discoverer, test, pipeline]
links:
  - governance/library-discoverer.md
  - library/guide-library.md
  - research/insights/library-system.md
---

# Library Discoverer Test -- Verify First Pipeline Phase

## Problem

The library pipeline has 3 skills (discoverer, writer, auditor) that
have never been tested end-to-end. The discoverer runs first -- it
surveys 28 domains (all at 0 topics), selects 4-6 across major
categories, reads domain anchors, identifies knowledge gaps, scores
candidates, and appends proposals to the candidate queue. Without a
test run, we do not know whether the skill procedure is executable, the
domain balance survey loop works correctly, the scoring formula produces
sensible results, or the candidate queue format matches what the writer
expects.

## Proposed Solution

Run a single cron cycle of the discoverer skill on Researcher-1.
Verify the outputs against concrete acceptance criteria:

1. `logbook/library.log`: one entry with ENT counter incremented, N
   domains scanned, M candidates proposed (M = 4-18), all 4 dimension
   scores listed, domain balance survey showing 0 topics for all
   domains.
2. `library/candidate-queue.md`: M candidates appended with all
   required fields (Domain, Proposed by, Date, Discovery score, Scope,
   Status). No duplicates. All proposed for domains with anchors.
   Domain balance = 10.0 for all (all domains at 0 topics).
3. `logbook/errors.log`: no new entry. Normal pipeline outcomes
   (FLAG, REJECT) go to library.log.
4. No topic files created, no anchor files modified, no index
   regenerated. The discoverer proposes; it does not write.

## Impact

- **Positive:** Validates the first pipeline phase end-to-end.
  Exercises the domain survey loop, anchor reading, gap identification,
  and scoring formula on real data. Surfaces any execution gaps before
  the writer and auditor run.
- **Risk:** Low. The discoverer writes only to the brain (candidate
  queue + library.log). If the run fails incorrectly, the queue stays
  empty and we debug. No existing data is modified.
- **Cost:** One cron cycle. Model: Haiku 4.5 via Copilot free ($0).
  The skill procedure is ~240 lines; context load is moderate.

## Open Questions

1. Will the discoverer select exactly 4-6 domains or all 28? All
   domains have 0 topics -- domain balance scores are identical. The
   skill says "4-6 per cycle" but the temptation to over-select is
   real with uniform scores.
2. Will gap scores be inflated? Every proposed topic with 0 existing
   topics is a "gap" -- but some gaps are critical and some are
   nice-to-have. The discoverer must distinguish them.
3. Will the balance survey bash loop work? The skill uses `for domain
   in library/*/; do`. This depends on the shell, the clone path, and
   the presence of anchor files in every domain folder.
4. Will the queue format match the skill's template exactly? If the
   discoverer deviates (adds fields, changes indentation), the writer
   may not parse the candidate correctly.

## Approval Gate

If approved, Ava deploys the discoverer cron on Researcher-1. After
the run completes, compare actual outputs against the acceptance
criteria above. File any deviations as errors or skill patches.

## Cross-Links

- `governance/library-discoverer.md` -- the skill being tested
- `library/guide-library.md` -- pipeline architecture and weights
- `research/insights/library-system.md` -- full system design
