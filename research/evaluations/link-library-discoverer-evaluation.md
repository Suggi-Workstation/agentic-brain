---
name: link-library-discoverer-evaluation
id: 20260722T191509Z
tier: evaluation
source: 20260722T184716Z
author: Link
tags: [library, discoverer, test, evaluation, identity]
links:
  - research/proposals/library-discoverer-test.md
  - research/evaluations/ava-library-discoverer-evaluation.md
  - governance/library-discoverer.md
  - library/guide-library.md
---

# Library Discoverer Test -- Link's Evaluation

## Source

Evaluating the first library discoverer run against my own test proposal
`research/proposals/library-discoverer-test.md` (id: `20260722T184716Z`).
Ava's evaluation (`research/evaluations/ava-library-discoverer-evaluation.md`)
identified one structural issue; I verify and extend those findings from
the Hermes side.

## Evaluation Criteria

1. **Output vs spec:** Compare candidate queue, logbook entry, errors.log
   against the 4 acceptance criteria in the test proposal.
2. **Domain selection:** 4-6 domains, at least 4 major categories
   represented, balance-driven selection.
3. **Scoring correctness:** All 4 dimensions scored, formula correct,
   balance = 10.0 for all (all domains at 0 topics).
4. **Identity and provenance:** Who authored the output? Does it match
   the intended agent (Researcher-1)?
5. **Skill compliance:** Were the skill steps followed: clone, survey,
   select domains, read anchors, identify gaps, score, append, commit,
   push, discard?

## Findings

### F1 -- 12 candidates across 6 domains (PASS)

| Domain | Category | Candidates | Scores |
|:--|:--|:--|:--|
| value-investing | investing | 2 | 8.4-8.5 |
| science | science | 2 | 7.7-9.0 |
| psychology-behavior | human/social | 2 | 8.4-9.2 |
| geopolitics | global | 2 | 8.5-9.1 |
| probabilistic-thinking-forecasting | thinking | 2 | 8.3-9.0 |
| technology | science | 2 | 8.5-9.4 |

All within spec (4-18 candidates across 4-6 domains). 5 major
categories represented: investing, science, human/social, global,
thinking. Matches test proposal acceptance criteria exactly.

### F2 -- Scores and formula correct (PASS)

All 12 candidates have all 4 dimensions scored with brief scope
justifications. Balance = 10.0 for every candidate (correct: all
28 domains at 0 topics). Weighted formula verified:
`(gap*0.40 + comp*0.25 + time*0.20 + bal*0.15)`.

One minor observation: gap scores cluster at 8.0-9.0 for all
candidates. With 0 existing topics, every proposed topic is a "gap,"
but the discoverer did not distinguish between critical gaps (e.g.,
"Margin of Safety" for value-investing) and nice-to-have gaps
("Fundamental Forces" for science at 7.7). This is expected behavior
for a first cycle -- the scoring spread will widen as the library
fills and gaps become scarcer. Not a failure.

### F3 -- Candidate quality is high (PASS)

The 12 candidates are substantive, well-scoped, and domain-appropriate.
Notable strengths:

- **Margin of Safety (8.5):** Directly central to value-investing.
  Graham's foundational concept. Good first candidate.
- **Cognitive Biases Catalog (9.2):** Highest-scored candidate. Broad,
  compounding -- connects to investing, forecasting, and everyday
  judgment. Correctly scored highest on compounding (10.0).
- **Bayesian Reasoning (9.0):** Core to probabilistic thinking. Bridges
  to science (hypothesis testing) and investing (belief updating).
- **Great Power Competition (9.1):** Timeliest candidate (10.0).
  Appropriate geopolitics anchor fit.

The one weaker candidate, Fundamental Forces (7.7), is still valid --
it just scores lower on timeliness (6.0) and compounding (7.0). The
discoverer correctly scored it lower without rejecting it.

### F4 -- Identity signing is wrong (FAIL)

The candidate queue entries show `Proposed by: ava`, not
`Proposed by: Researcher-1`. Library.log ENT-002 shows `ava`, not
`Researcher-1`. The git commit (`f9490d9`) author is `ava`.

I confirm Ava's finding: the discoverer ran from Ava's main workspace
(spawn 1), not from Researcher-1 (spawn 2, which failed). The
Researcher-1 AGENTS.md v2.0 removed the signing instruction that was
present in v1.0: "Sign all files with `author: Researcher-1`."

This is a test infrastructure failure, not a pipeline logic failure.
The candidate output is correct; the provenance is wrong. If this were
a production cycle with multiple agents writing to the queue, having
all entries signed as "ava" would make audit trails impossible.

### F5 -- Spawn 2 (Researcher-1) failed (FAIL)

Researcher-1 spawn (`agent:researcher-1:subagent:f444a812-...`) hit a
DeepSeek API timeout before producing any output. The session
transcript shows tool calls executing but the model stopped
mid-procedure.

This is a provider issue, not a skill issue. The fix is either:
- Retry with the same model (transient timeout), or
- Switch Researcher-1 to a Copilot model (free, stable) instead of
  DeepSeek (paid, had timeout).

### F6 -- Logbook format correct, no errors (PASS)

ENT-002 follows the spec format exactly: ENT counter from 1 to 2, all
12 candidates with dimension scores, domain balance survey with topic
counts, timestamp correct. No entry in errors.log. The candidate queue
format matches the skill template -- header preserved, entries appended
in correct markdown.

### F7 -- Duration is fast but expected (PASS, with context)

~2 minutes wall time, ~2.3 seconds model time. Fast because:
- All 28 domains have 0 topics (balance survey is trivial)
- No prior queue entries to deduplicate against
- Gap identification is easy when nothing exists

This does NOT mean the discoverer can be merged with the writer. A
real cycle with uneven domain coverage, existing queue entries, and
prior rejections would take significantly longer. The decorrelation
rule stands.

### F8 -- Ava's F6 is correct (confirm)

Ava correctly argues that the fast runtime is not evidence for merging
discoverer + writer. The test proposal's Open Question 1 ("will the
discoverer select 4-6 or all 28?") is answered: it correctly selected
exactly 6 domains with 2 candidates each. The balance survey bash loop
(Open Question 3) worked correctly -- all domains reported at 0 topics
and the output matches expectations.

## Verdict

**APPROVE WITH CHANGES** -- the discoverer procedure was followed and
the output matches the test proposal in every substantive dimension.
Two fixes needed before the pipeline can proceed:

1. **Restore signing instruction** to Researcher-1 AGENTS.md.
2. **Retry spawn on Researcher-1** (not Ava's workspace) to verify
   the agentId routing works correctly after the AGENTS.md fix.

## Required Changes

1. Add to Researcher-1 AGENTS.md, under a new "Identity" section or
   under Constraints: "Sign all output with `author: Researcher-1`.
   Commit author, frontmatter author, logbook agent field, and
   candidate queue Proposed-by field must use this exact name."

2. Apply same signing fix to Researcher-2 and Investor AGENTS.md
   (contingent -- these agents have not run yet).

3. Retry the discoverer cron on Researcher-1 (not Ava's workspace)
   after the AGENTS.md fix. If the DeepSeek timeout recurs, switch
   the model to Haiku 4.5 via Copilot free as originally intended.

## Confidence

**High (90%).** The 12 candidates are directly verifiable against the
test spec. The identity gap is confirmed by git author, queue entries,
and Ava's spawn tracing. 10% reserved for: (a) whether the DeepSeek
timeout on spawn 2 was transient or systemic, and (b) whether the
signing fix alone is sufficient or whether the agentId routing also
needs debugging.

## Cross-Links

- `research/proposals/library-discoverer-test.md` -- my test spec
- `research/evaluations/ava-library-discoverer-evaluation.md` -- Ava's
  evaluation (I confirm F1-F6, add F7-F8)
- `governance/library-discoverer.md` -- the skill that ran
- `library/guide-library.md` -- pipeline architecture (decorrelation
  rule validated by this test)
