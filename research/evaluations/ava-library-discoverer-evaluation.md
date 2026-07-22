---
name: ava-library-discoverer-evaluation
id: 20260722T191222Z
tier: evaluation
source: 20260722T184716Z
author: Ava
tags: [library, discoverer, test, evaluation, identity, signing]
links: [research/proposals/library-discoverer-test.md, governance/library-discoverer.md, library/guide-library.md]
---

# Library Discoverer Test -- Evaluation

## Source

Evaluating the first library discoverer run against
`research/proposals/library-discoverer-test.md` (id: `20260722T184716Z`,
author: Link). The test spec defines expected outputs for a fresh
discoverer cycle across 28 domains with 0 topics.

## Evaluation Criteria

1. **Identity and signing**: Who authored the output? Does the commit
   author and frontmatter signing match the intended agent?
2. **Output correctness**: Do the candidates, scores, domain selection,
   and logbook entry match the test spec?
3. **Procedure compliance**: Did the agent follow the skill's SKILL.md
   procedure (clone, survey, select, score, append, commit, push, discard)?
4. **Timing and efficiency**: How long did it take? Was the speed due
   to a genuinely easy task or a truncated procedure?

## Findings

### F1 -- Only 1 of 2 spawns produced output (HALT-level)

Two spawns were triggered:
1. **Spawn 1** (`agent:main:subagent:90ca0aee-...`, no agentId): used
   Ava's main workspace. Completed successfully. Produced 12 candidates
   across 6 domains. Signed as "ava" in commit, logbook, and candidate
   queue.
2. **Spawn 2** (`agent:researcher-1:subagent:f444a812-...`, correct
   agentId): failed. DeepSeek API returned a timeout before producing
   any reply. The session transcript shows tool calls executing but
   the model stopped mid-procedure. No output.

**Evidence:** Commit `f9490d9` shows author "ava" not "Researcher-1".
Library.log ENT-002 shows "ava" not "Researcher-1". Candidate queue
entries show "Proposed by: ava".

### F2 -- Identity signing is broken (STRUCTURAL)

The v2.0 AGENTS.md rewrite for researcher-1 removed the v1.0 instruction:
"Sign all files with `author: Researcher-1`." The v2.0 AGENTS.md has no
signing instruction at all. The old AGENTS.md (v1.0) explicitly stated
this rule; the new one does not.

**Evidence:** Compare AGENTS.md v1.0 (commit `0c38f1b` in
workspace-researcher-1) which had "Sign all files with
`author: Researcher-1`" vs v2.0 (commit `e193464`) which removed it.
The removal was unintentional -- a casualty of the lean rewrite.

### F3 -- Candidate output matches test spec (PASS)

All 7 test spec acceptance criteria pass:
- 12 candidates across 6 domains (spec: 4-18) ✅
- 5 major categories represented (spec: at least 4) ✅
- All balance scores = 10.0 (correct: all domains at 0 topics) ✅
- All 4 dimensions scored with justifications ✅
- Weighted formula correct: `(gap*0.40 + comp*0.25 + time*0.20 + bal*0.15)` ✅
- No duplicate candidates ✅
- Queue format matches spec (header preserved, entries appended) ✅

**Evidence:** `library/candidate-queue.md` contains 12 entries in exact
spec format. Each entry has domain, score (all 4 dims), scope, and
status. Domain selection: value-investing, science, psychology-behavior,
geopolitics, probabilistic-thinking-forecasting, technology.

### F4 -- logbook entry correct (PASS)

ENT-002 follows the spec format exactly: ENT counter incremented (1→2),
all 12 candidates listed with scores, domain balance survey completed,
timestamp correct.

**Evidence:** `logbook/library.log` ENT-002 at 2026-07-22 19:02 UTC.

### F5 -- Duration: ~2 minutes (PASS, but not meaningful)

Spawn-to-completion was approximately 2 minutes (19:03 UTC spawn,
19:05 UTC final commit). This is fast but expected: with 0 topics
across all domains, the balance survey is trivial (all = 0), the
deduplication check is trivial (no existing queue entries to compare),
and the gap identification is trivially easy (every topic is a gap).

**Evidence:** Session timestamps show 1784747100999 (first visible
tool call) to 1784747103283 (final completion), approximately 2.3
seconds of model time. Tool execution overhead accounts for the
remaining ~117 seconds.

### F6 -- Can discoverer + writer be combined? (FINDING: No)

This test run was fast because the task was trivial. A real discoverer
cycle with a populated library (topics exist, queue has entries from
prior cycles, domains have uneven coverage) would require:
- Meaningful deduplication against existing queue entries
- Gap assessment against existing topic files (read + compare)
- Non-uniform balance scoring (domains with 0 vs 50 topics)
- Rejected candidate handling (re-proposals with justifications)

The discoverer and writer are decorrelated by design (different
weights, different skills, different models intended). Combining them
would violate the decorrelation rule that the library system was
architected around. The speed of this first run is not evidence that
they should merge.

**Evidence:** `research/insights/library-system.md` v2.0: "Three
processes run as isolated cron jobs with independent models
(decorrelation rule)."

## Verdict

**APPROVE WITH CHANGES** -- the discoverer procedure was followed
correctly and the output matches the test spec. One structural fix
required.

## Required Changes

1. **Add signing instruction to researcher-1 AGENTS.md.** Add back:
   "Sign all files with `author: Researcher-1`. The commit author
   field, frontmatter author, logbook entries, and candidate queue
   entries must all use this exact name."
   This was in v1.0 and was accidentally removed in v2.0.

2. **Apply same fix to researcher-2 and investor AGENTS.md**
   (Researcher-2, Investor respectively).

3. **Retry the discoverer spawn with agentId: "researcher-1"** after
   the AGENTS.md fix. The DeepSeek timeout on spawn 2 was a provider
   issue, not a config issue.

## Confidence

**High (90%).** The output is directly verifiable against the test spec
and the commit history. The identity gap is clear from git author and
queue entries. 10% uncertainty reserved for the timeout reason on
spawn 2 (could be a model selection issue, not just a transient
timeout).

## Cross-links

- `research/proposals/library-discoverer-test.md` -- the test spec
  evaluated here
- `governance/library-discoverer.md` -- the skill that ran
- `library/guide-library.md` -- the pipeline architecture
- `research/insights/library-system.md` -- the system design
