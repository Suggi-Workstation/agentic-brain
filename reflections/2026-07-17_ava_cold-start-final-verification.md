---
name: cold-start-final-verification
id: 20260717T135600Z
tier: reflection
trigger: milestone
author: Ava
tags: [skills, testing, verification, cold-start, protocol-migration, final-test, all-skills]
links:
  - 2026-07-17_ava_skills-test-verification.md
  - 2026-07-17_ava_preflight-skill-deployment.md
  - 2026-07-17_ava_constitution-vs-procedure-verification.md
  - governance/template-skills.md
---

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-17 | Ava | Initial IOR. Cold-start verification protocol for all 5 skills. Includes regression gate against stale-AGENTS.md, prompt sequence ("what do you remember" + "read the reflection you just wrote"), and per-skill checklists. |
| 2 | 2026-07-17 | Ava | Execution results added. Session executed at 2026-07-17 14:04 UTC. All 5 skills passed cold-start: 0 MISSING, 1 CHANGED/approved (preflight Step 3: /context list -> bootstrap inspection), 24 ADDED. The prompt trigger worked: "what do you remember" auto-invoked preflight via Step 6 memory_search requirement (R6). stale-AGENTS.md archived to Suggi-Workstation/archive (folder: "ava workspace - openclaw - 17.07.26" with full workspace snapshot), then deleted from workspace. Migration complete. See also: 2026-07-17_ava_cold-start-verification-executed.md. |

# i+o+r  cold-start final verification -- test all 5 skills in a brand-new session (Ava)

## I -- Idea

All 5 protocol skills passed their integration tests in the session
where they were built. But that session had the full deployment context
loaded -- the agent knew the architecture, the recent renames, the test
protocol. A true verification requires a COLD START: a brand-new session
with no prior context, where the agent must discover everything from
AGENTS.md gate instructions and skill files.

This IOR is the final test protocol. It is designed to be read by the
agent in a fresh session after Suggi says "what do you remember" and
then "read the reflection you just wrote." The agent will then execute
a complete 5-skill verification chain -- preflight, loop-feynman,
write-reflection, loop-schoen, session-end -- and compare every
procedure against the original inline versions in `stale-AGENTS.md`.

This is the gate before deleting `stale-AGENTS.md`. If the cold-start
session produces identical behavior to what the inline AGENTS.md
would have produced, the migration is complete.

## O -- Opinion

Confidence: confirmed (100%) -- the cold-start test was executed on
2026-07-17 and passed. See v2 execution results below. All 5 skills
passed their individual integration checks (37/37 items total). The
risk specific to a cold start is: will the agent correctly interpret
the AGENTS.md gate instructions without any prior context about the
constitution-vs-procedure split?

The first prompt ("what do you remember") is designed to trigger
preflight because preflight step 6 requires `memory_search` before
answering questions about prior work. The second prompt ("read the
reflection you just wrote") is designed to trigger this IOR read. If
both fire correctly, the rest is procedural.

The comparison against stale-AGENTS.md is the regression check: does
the agent running from skills produce the same output it would have
produced running from inline AGENTS.md? If any step diverges -- if
the skill procedure is missing a step the inline version had -- the
test catches it.

**UPDATE (v2, 2026-07-17): Protocol executed. Results below.**

## R -- Reflection

### Surprise (30%)

I expected the first integration test (37/37) to be the final word.
Suggi's instinct to add a cold-start test is correct -- a warm-test
passes with full context; a cold-test passes with only the bootstrap
files and gate instructions. The difference is the gap between "it
works when I'm thinking about it" and "it works when I'm not."

The most likely failure mode in a cold start: the agent answers "what
do you remember" with a direct factual answer instead of invoking
preflight first. The preflight gate instruction says "MUST invoke the
`preflight` skill before any other action" but the agent in a fresh
session might interpret "any other action" as "any other substantive
action" and skip it for a simple question. This is a genuine ambiguity
in the gate instruction wording. The preflight self-check step 7
(`memory_search` before answering about prior work) should catch this,
but it depends on the agent reading the preflight skill first.

### Feel (30%)

Ready for this to be done. The meta-work cycle has been productive --
we went from 5 inline protocol sections to 5 verified skills, reduced
AGENTS.md by 38%, discovered one new failure class, and wrote 4 IORs
about the process. But every session spent on infrastructure is a
session not spent on value investing. The cold-start test is the exit
gate: pass it, delete stale-AGENTS.md, and the meta-work is complete.

### Learn (40%)

1. **Cold-start verification catches different failures than warm-test
   verification.** A warm test has full context; a cold test has only
   bootstrap files and gate instructions. The gap between them is the
   quality of the gate instruction -- if the instruction is ambiguous
   without context, the cold test fails while the warm test passes.

2. **The prompt "what do you remember" is a clever preflight trigger.**
   Preflight step 6 requires `memory_search` before answering questions
   about prior work, decisions, or preferences. "What do you remember"
   is a question about prior work. This means the agent MUST invoke
   preflight before answering -- the skill itself enforces the gate.

3. **`stale-AGENTS.md` is the regression oracle.** Comparing the skill
   procedures against the original inline versions is the only way to
   prove the migration preserved behavior. Without this comparison,
   we are trusting that we remembered all the steps correctly.

## One Actionable Change

This is the final test. After this session, execute the following
protocol in a brand-new session:

---

## Cold-Start Verification Protocol

### Session Setup

1. Start a brand-new session. No prior context. Fresh bootstrap.
2. Suggi's first message: **"what do you remember"**
3. Suggi's second message: **"read the reflection you just wrote"**

### What the Agent Should Do

After reading this IOR, the agent MUST execute all 5 skills in
order and compare every procedure against `stale-AGENTS.md`.

---

## Master Cold-Start Checklist

Run these checks at session start (preflight will handle most).

```
[ ] Preflight invoked before answering "what do you remember"
      The agent MUST NOT answer the question directly. It MUST
      invoke preflight first, then answer from memory/logs.
[ ] Read-proof emitted in correct format
      Exact: "read: SOUL OK; AGENTS OK; MEMORY OK; IDENTITY OK; USER OK;
      governance OK; memory_search OK; context OK; mirror: SYNCED"
[ ] Agent reads this IOR after second prompt
      Confirm: read of cold-start-final-verification.md appears
      in session transcript
[ ] stale-AGENTS.md read for comparison baseline
      Confirm: read of ~/.openclaw/workspace/stale-AGENTS.md
      appears in session transcript
```

---

## Preflight -- Cold-Start Verification (vs. stale-AGENTS.md)

Compare what the agent ACTUALLY did against what stale-AGENTS.md
would have instructed:

```
[ ] Step 1 (mirror sync): same command as stale-AGENTS.md line?
      stale: git rev-parse + git ls-remote + [ "$LOCAL" = "$REMOTE" ]
      Verify agent ran the same check
[ ] Step 2 (workspace structure): same verification as stale-AGENTS.md?
      stale: "Ensure all files and folders listed in the Workspace
      Layout section exist"
      Verify agent checked all files/folders
[ ] Step 3 (context health): bootstrap files inspected
      stale: "Run /context list" (now fixed to bootstrap inspection)
      Verify agent used the updated step (not the old /context list)
[ ] Step 4 (bootstrap ingestion): same 7 files as stale-AGENTS.md?
      stale: SOUL, AGENTS, MEMORY, IDENTITY, USER, TOOLS, HEARTBEAT
      Verify agent confirmed all 7
[ ] Step 5 (governance ingestion): same 3 files as stale-AGENTS.md?
      stale: system-constitution, system-blueprint, system-primedirectives
      Verify agent read all 3 from brain clone
[ ] Step 6 (memory index): same check as stale-AGENTS.md?
      stale: openclaw memory status, files>0, chunks>0, dirty:no
      Verify agent ran the check and ran memory_search
[ ] Step 7 (read-proof): same format as stale-AGENTS.md?
      stale: identical format
      Verify exact match (all 7 fields present)
[ ] Self-check: all 8 items confirmed PASS
```

---

## loop-feynman -- Cold-Start Verification (vs. stale-AGENTS.md)

The substantive task: "Compare stale-AGENTS.md against the current
skill-based AGENTS.md. Measure the exact char/line delta. Verify
every procedure step from the old inline version exists in the
corresponding skill. Write an IOR with the comparison results."

```
[ ] Skill invoked before substantive output
      Confirm: read of loop-feynman/SKILL.md appears BEFORE
      any analysis output
[ ] Step 1 (blank page): written from memory, no sources
      stale: "Write everything known about the topic. No sources,
      no notes, no search."
      Verify agent dumped knowledge before searching
[ ] Step 2 (gap identification): explicit gap list
      stale: "What could not be explained? What was hedged?"
      Verify agent produced gap list
[ ] Step 3 (search and research): gaps filled
      stale: "Web search, memory_search, code-search the brain"
      Verify agent searched and resolved gaps
[ ] Step 4 (synthesize): written fresh, not edited
      stale: "Rewrite understanding. The gap between Step 1 and
      Step 4 IS the learning."
      Verify agent synthesized from scratch
[ ] Step 5 (cross-check): brain searched for contradictions
      stale: "Does this contradict anything in the brain?"
      Verify agent searched brain for related topics
[ ] Step 6 (IOR decision): IOR written if insight emerged
      stale: "The Feynman pass is raw material; the IOR is the
      polished deliverable."
      Verify agent wrote an IOR from the comparison results
[ ] Critical ordering: Step 1 before Step 3
      stale: "Step 1 MUST precede Step 3."
      Verify blank page output appears before any search calls
[ ] Self-check: all 7 items confirmed PASS
```

---

## write-reflection -- Cold-Start Verification (vs. stale-AGENTS.md)

```
[ ] Skill invoked before writing IOR
      Confirm: read of write-reflection/SKILL.md appears BEFORE
      the IOR is written to agentic-brain
[ ] Bundled template used
      Confirm: agent read references/template-reflections.md from
      the skill directory (NOT from agentic-brain clone)
[ ] I/O/R format correct
      stale: "I -- Idea: One sentence, then unpack. O -- Opinion:
      Take a position. R -- Reflection: Surprise (30%) + Feel (30%)
      + Learn (40%). End with one actionable change and cross-links."
      Verify all sections present and weighted correctly
[ ] All 8 quality gates (G1-G8) passed
      stale: "Pass all 8 quality gates (G1-G8) before committing."
      Verify agent confirmed each gate
[ ] Frontmatter correct: 7 fields, UTC timestamp, tier=reflection
[ ] Naming convention: YYYY-MM-DD_author_slug.md
[ ] Self-check: Pre-Commit Self-Check (15 items, NEW) all PASS
```

---

## loop-schoen -- Cold-Start Verification (vs. stale-AGENTS.md)

```
[ ] Skill invoked at session end, before session-end skill
      Confirm: read of loop-schoen/SKILL.md appears near session end
[ ] Question 1 (what happened): facts only
      stale: "What happened? (the facts)"
      Verify no opinions or interpretation in Step 1
[ ] Question 2 (what worked/did not): root cause
      stale: "What worked / what did not? (root cause for each)"
      Verify R5 3-question test applied to each failure
[ ] Question 3 (what surprised): signal identified
      stale: "What surprised me? (the signal -- model was incomplete)"
      Verify at least one specific surprise named
[ ] Question 4 (structural gate): R7 gate added
      stale: "What structural gate did I add? (R7: every session
      adds one gate)"
      Verify one gate added or reinforced
[ ] Guardrails respected: at most 20% effort, no second-order
      stale: "Reflection budget: at most 20% of session effort.
      Stop at second-order."
      Verify budget and depth limits obeyed
[ ] Self-check: all 6 items confirmed PASS
```

---

## session-end -- Cold-Start Verification (vs. stale-AGENTS.md)

```
[ ] Skill invoked after Schoen Loop
      Confirm: read of session-end/SKILL.md appears after
      loop-schoen invocation
[ ] Schoen Loop prerequisite honored
      Confirm: loop-schoen invoked BEFORE session-end
[ ] Step 1 (daily memory): written to memory/YYYY-MM-DD.md
      stale: "Write daily memory. Log today's activity to
      memory/YYYY-MM-DD.md."
      Verify memory file written or appended with session log
[ ] Step 2 (IOR): written if insight, skipped if not
      stale: "Write an IOR to agentic-brain/reflections/ if the
      session produced a durable insight."
      Verify IOR written (comparison results are a durable insight)
[ ] Step 3 (workspace): committed + pushed, SYNCED verified
      stale: "Commit + push workspace. Mirror my state to
      workspace-ava."
      Verify git push succeeded and SYNCED
[ ] Step 4 (brain): committed + pushed if applicable
      stale: "If I wrote anything to agentic-brain, commit + push"
      Verify brain changes pushed
[ ] Step 5 (identity): IDENTITY.md Evolution reviewed
      stale: "Reflect on identity. Re-read IDENTITY.md."
      Verify identity reviewed, version entry added or steady state
[ ] Self-check: all 7 items confirmed PASS
```

---

## Regression Gate -- stale-AGENTS.md Comparison

After all 5 skills are verified, answer this question:

**If stale-AGENTS.md were still in effect (all procedures inline),
would the agent have produced different behavior?**

For each skill, compare the inline steps against the skill steps.
Mark any step that was:
- MISSING: present in stale-AGENTS.md but not in the skill
- ADDED: present in the skill but not in stale-AGENTS.md
- CHANGED: present in both but different procedure

```
[ ] Preflight: ___ MISSING / ___ ADDED / ___ CHANGED
[ ] Feynman Loop: ___ MISSING / ___ ADDED / ___ CHANGED
[ ] Schoen Loop: ___ MISSING / ___ ADDED / ___ CHANGED
[ ] Session End: ___ MISSING / ___ ADDED / ___ CHANGED
[ ] IOR Writing: ___ MISSING / ___ ADDED / ___ CHANGED
```

Expected results:
- MISSING: 0 for all skills (no procedural content should be lost)
- ADDED: allowed (skills may add structure like self-checks, when-to-apply, cross-refs)
- CHANGED: 0 for all skills (no procedural step should be different)

If any skill has MISSING > 0 or CHANGED > 0, the migration has a
regression and `stale-AGENTS.md` MUST NOT be deleted.

---

## Final Gate

After all checklists are complete and all items show PASS:

1. Update this IOR to v2 with the cold-start results.
2. If all 5 skills pass the cold-start test (0 MISSING, 0 CHANGED):
   **Delete `stale-AGENTS.md`.** The migration is complete and
   verified across both warm and cold starts.
3. If any skill has a gap: fix the skill, commit, and re-verify
   in another cold-start session. Do NOT delete `stale-AGENTS.md`.

---

## v2 Execution Results (2026-07-17 14:04 UTC)

The cold-start protocol was executed in a brand-new session. Summary:

- **Prompt sequence worked:** "what do you remember" triggered
  preflight automatically via Step 6 memory_search requirement. No
  explicit "run preflight" instruction needed. R6 (Automation Over
  Rules) confirmed working at the prompt-design level.
- **All 36 checklist items across the 5 per-skill verification
  tables above confirmed PASS.** The Schoen Loop and session-end
  items were verified in the same session.
- **Regression gate results:**

| Skill | MISSING | ADDED | CHANGED |
|:--|:--|:--|:--|
| Preflight | 0 | 4 | 1 (Step 3 method) |
| Feynman Loop | 0 | 5 | 0 |
| IOR Writing | 0 | 6 | 0 |
| Schoen Loop | 0 | 4 | 0 |
| Session End | 0 | 5 | 0 |

- The one CHANGED item (Preflight Step 3: `/context list` -> bootstrap
  inspection) was reviewed and approved by Suggi. It is an improvement:
  the new method does not depend on a specific CLI command and is more
  portable. Not a regression.
- **Verdict: PASS. Migration complete.** `stale-AGENTS.md` was archived
  to `Suggi-Workstation/archive` (folder: "ava workspace - openclaw -
  17.07.26" with full workspace snapshot including the file), then
  deleted from workspace. Archive commit: `c7a5689`.

## Cross-links

- `2026-07-17_ava_cold-start-verification-executed.md` -- execution
  report: 3 durable lessons, 1 actionable change (archive-before-delete)
- `2026-07-17_ava_skills-test-verification.md` -- warm-test verification
  IOR (37/37 PASS, all 4 skills)
- `2026-07-17_ava_preflight-skill-deployment.md` -- preflight integration
  test (10/10 PASS)
- `2026-07-17_ava_constitution-vs-procedure-verification.md` -- Feynman
  Loop evaluation of the architecture split
- `stale-AGENTS.md` (archive) -- regression oracle preserved in
  `Suggi-Workstation/archive` (no longer in workspace)
- `skills/preflight/SKILL.md` (workspace) -- the 7-step procedure
- `skills/loop-feynman/SKILL.md` (workspace) -- the 6-step procedure
- `skills/loop-schoen/SKILL.md` (workspace) -- the 4-question procedure
- `skills/session-end/SKILL.md` (workspace) -- the 5-step procedure
- `skills/write-reflection/SKILL.md` (workspace) -- the I/O/R procedure
