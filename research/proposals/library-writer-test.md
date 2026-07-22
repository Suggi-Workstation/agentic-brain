---
name: library-writer-test
id: 20260722T184716Z
tier: proposal
author: Link
tags: [library, writer, test, pipeline]
links:
  - governance/library-writer.md
  - governance/template-library.md
  - library/guide-library.md
  - research/proposals/library-discoverer-test.md
---

# Library Writer Test -- Verify Topic Creation

## Problem

After the discoverer populates the candidate queue, the writer must
pick the highest-scored candidate, read the domain anchor, research the
topic via web search, score across 4 dimensions, and write a topic file
following `governance/template-library.md` format. This has never been
tested with real candidates. Without a test run, we do not know whether
web search finds high-authority sources for the proposed topics, whether
the 4-dimension scoring formula produces scores >= 7.0, or whether the
output matches all 10 quality gates from the template.

## Proposed Solution

Run one writer cron cycle on Researcher-1 after the discoverer has
populated the queue. Verify outputs against acceptance criteria:

1. **Topic file** at `library/<domain>/<topic-slug>.md` (if score
   >= 7.0): frontmatter with all 7 required fields (name, id, tier,
   domain, author, tags, links); id from `date -u +'%Y%m%dT%H%M%SZ'`
   not human-rounded; body with claim title, opening paragraph,
   structured sections, 3+ cited sources with authority ratings, at
   least 1 cross-reference; ASCII-only; passes G1-G10 quality gates.
2. **Scoring recorded:** all 4 dimensions (core match 0.35, scope fit
   0.35, knowledge value 0.20, source authority 0.10) scored with
   justifications; weighted sum calculated correctly; similarity
   overlap estimated.
3. `logbook/library.log`: one entry with ENT counter incremented,
   weighted score, source counts, overlap estimate.
4. Queue updated: processed candidate removed or marked as written.
5. `logbook/errors.log`: no new entry.

If score < 7.0: logged as FLAG (5.0-6.9) or REJECT (<5.0) in
library.log. The candidate stays in queue with updated status.

## Impact

- **Positive:** Validates the second pipeline phase. Exercises web
  search synthesis, template compliance, and the full G1-G10 quality
  gate checklist on real output. Produces the first actual topic file
  in the library.
- **Risk:** Low. The writer writes only to the cloned brain, not to
  any workspace. If the run fails, we get a library.log entry
  explaining why and the queue retains the candidate.
- **Cost:** One cron cycle. Model: Sonnet 4.6 via Copilot free ($0).
  Web search may use free tier API calls. The skill + template +
  anchor + candidate context is ~500 lines -- moderate.

## Open Questions

1. With 0 existing topics, similarity overlap is always < 50%. Is the
   overlap check meaningful on the first topic, or does it produce a
   meaningless "0%" every time?
2. Will web search find high-authority sources for discoverer-chosen
   gaps? Some proposed topics may be niche -- source authority may drop
   below the >= 3.0 threshold, causing automatic rejection regardless
   of other scores.
3. Will the writer read `governance/template-library.md` as instructed?
   The skill says "read it, follow it exactly" -- but if the writer
   skips this step, the output format will deviate from the template.
4. What happens if all candidates in the queue score < 7.0? The queue
   fills with FLAG entries and nothing gets written. We may need to
   adjust scoring thresholds or improve the discoverer's candidate
   selection.

## Approval Gate

If approved, Ava deploys the writer cron on Researcher-1 after the
discoverer run completes and the queue is populated. Compare actual
outputs against acceptance criteria. File deviations as errors or
skill patches.

## Cross-Links

- `governance/library-writer.md` -- the skill being tested
- `governance/template-library.md` -- format specification and G1-G10 gates
- `library/guide-library.md` -- pipeline architecture and weights
- `research/proposals/library-discoverer-test.md` -- prerequisite test
