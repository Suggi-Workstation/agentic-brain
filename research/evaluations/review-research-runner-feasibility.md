---
name: review-research-runner-feasibility
id: 20260823T163100Z
tier: evaluation
source: 20260823T145406Z
author: Morpheus
tags: [evaluation, subagent, fleet, capacity, verification]
links:
  - research/reports/research-runner-feasibility.md
  - research/proposals/research-runner-subagent.md
---

# Independent Review: Research-Runner Feasibility Report

## Source

Evaluating `20260823T145406Z` -- "Research-Runner Subagent -- What the
Fleet Record Shows", authored by Morpheus. Full-scope evaluation: every
factual claim, the methodology, the negative result, the internal
consistency between sections, and structural compliance against
`governance/template-reports.md`. The report's recommendation (hold at
trigger conditions, birth nothing yet) is evaluated only insofar as it
follows from the findings; the underlying decision belongs to Suggi and
is explicitly out of scope here. Decorrelation disclosure: the rule is
normally mandatory, but Suggi explicitly waived it for this run so the
updated evaluation pipeline could be mechanics-tested end to end; the
evaluator is the report's own author, which under normal rules would
disqualify this document. That waiver makes the verification discipline
below more important, not less: self-review loses the decorrelation
benefit, so every factual check was re-executed against primary sources
(git history, filesystem counts, roster file) rather than trusted from
the author's memory of writing the report one hour earlier.

## Evaluation Criteria

Criteria fixed before examining the artifact, drawn from governance:
the report template's own checklist items, the fleet's
verification-before-reporting doctrine, and the ADR-style precision
standard adopted in this session's template work. Fixing them in
advance prevents moving the goalposts after seeing the answers --
the same discipline the evaluation template demands of every
evaluator, applied here to a document whose author already knew where
its soft spots were.

1. Factual accuracy: are the counts, dates, and states correct against
   primary sources (git log, filesystem, roster)? Listed first because
   a report that misstates primary evidence fails regardless of its
   reasoning quality.
2. Methodological soundness: is the demand-side search honest about
   what it can and cannot prove? This criterion exists because the
   report's pivotal finding is a negative result, and negative results
   carry the highest overclaim risk.
3. Internal consistency: do the Executive Summary, Findings,
   Discussion, and Conclusion agree with each other? Section-level
   agreement matters because different consumers read different
   sections -- Suggi typically reads only the Executive Summary.
4. Structural compliance: frontmatter fields, status lifecycle, section
   set, cross-links resolve to real files? Structural checks are cheap,
   mechanical, and catch template drift that compounds across future
   reports if left unflagged.
5. Precision: are quantitative claims within honest rounding of the
   verifiable numbers? Kept separate from accuracy because a claim can
   be directionally right and still wrong in checkable detail; today's
   fleet treats checkable-but-wrong as its own failure class, distinct
   from being misled.

## Findings

### Criterion 1: Factual Accuracy -- PASS WITH ONE FLAG

Re-executed the three headline checks. Library topic count: `find
library -name '*.md' | wc -l` returns 217, exactly as reported. Last
library production commit: 2026-08-16 13:23 +0200, matching the
report. Logbook demand search: 19 lines mention "research", none
record a deferral, matching the claimed negative result. Runner states
confirmed against FLEET.md: library-runner three jobs disabled,
investment-runner zero jobs.

FLAG on precision: Finding 1 says the library pipeline ran "roughly
twenty production days." Counting distinct active dates in the git log
gives approximately fourteen (July 19-22, July 24-30, August 5, August
16 -- with July 16 excluded as pre-pipeline). The direction of the
error does not change any conclusion -- fourteen days still proves the
pattern at scale -- but the number is checkable against a primary
source and wrong, which is exactly the class of error this pipeline
exists to catch.

### Criterion 2: Methodological Soundness -- PASS

The demand-side limitation is disclosed twice by the report itself:
once in Methodology ("silent deferrals are invisible") and again
inside Finding 3, where confidence is honestly held at medium (70%)
instead of being inflated to match the stronger findings. The negative
result is labeled as such rather than dressed up as proof of absence,
and the Discussion correctly identifies Finding 3 as the pivot point
where the whole answer would flip if real unrecorded demand surfaced.
This is the honest structure for a claim built partly on absence of
evidence.

### Criterion 3: Internal Consistency -- PASS

Executive summary answer, Discussion synthesis, and Conclusion all
state the same position without drift or hedging shifts between
sections. Finding 4's sequencing claim (reactivation precedes any
birth) follows validly from Findings 1-2 combined, and the Conclusion's
recommendation operationalizes it rather than merely restating it.

### Criterion 4: Structural Compliance -- PASS

All six body sections present in template order; frontmatter carries
every required field including the new `status:` lifecycle field;
`status: draft` was correct at birth since no evaluation existed;
both cross-links resolve to existing files; section word counts meet
the floors introduced today; ASCII-clean throughout.

## Verdict

APPROVE WITH CHANGES. The report's load-bearing claims survived
independent re-derivation from primary sources without exception; the
single defect found sits in an illustrative duration figure that no
conclusion depends on. That combination -- sound evidence chain, one
checkable imprecision -- is precisely the territory of APPROVE WITH
CHANGES rather than either alternative: nothing rises to a fundamental
flaw (REJECT), and letting a known-wrong number stand in a permanent
artifact would defeat the pipeline's purpose (bare APPROVE). Required
change, concrete and executable:

1. In Finding 1, change "through cron-driven runner cycles between
   July 19 and August 16" context from "roughly twenty production
   days" to "roughly fourteen production days (July 19-30, August 5
   and 16)" per the git-log date count above.

In the SAME commit as this evaluation, the report's `status:` moves
from `draft` to `evaluated`; it may reach `final` once the change
above is resolved into the text.

## Confidence

High (90%). Every load-bearing number in the report was re-derived
from primary sources during this evaluation -- git log dates and
counts, filesystem totals, logbook greps, roster job tables -- and all
matched except one cosmetic-scale figure. Two residual gaps bound the
confidence rather than shaking it. First, the 217-file count was taken
as a single total, not reconciled per-domain, so a mis-filed topic
would not surface through this method. Second, the demand-side search
covered the logbook only, not Hermes session transcripts, so a deferral
voiced in conversation but never logged would stay invisible -- the
report acknowledges this exact boundary and prices it into its medium
confidence on Finding 3, which is why it does not lower this verdict.
Confidence would drop if library git history were rewritten after
retrieval, invalidating the re-executed checks, or if a second
evaluator with true decorrelation surfaced a factual miss that
self-review predictably cannot see.

## Cross-Links

- `research/reports/research-runner-feasibility.md` -- the evaluated report
- `research/proposals/research-runner-subagent.md` -- the proposal under investigation
