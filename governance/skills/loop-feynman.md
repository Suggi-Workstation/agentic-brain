---
name: loop-feynman
description: "Run the 6-step Feynman Loop for output quality before writing any artifact to the agentic-brain: blank page, identify gaps, search and research, synthesize, and cross-check."
user-invocable: false
disable-model-invocation: false
---

# Feynman Loop -- Output Quality

## Hard Gate (R4)

This skill is invoked by the AGENTS.md Feynman Loop instruction.
Every step MUST be followed before producing substantive output.
The critical ordering constraint (Step 1 before Step 3) prevents
existing-knowledge bias. Reversing them produces shallow thinking
(observed: 4x depth loss in v0.8-v4.0).

## When to Apply

Run the full loop before:
- Writing any artifact to the agentic-brain
- Answering a complex investing question
- Producing any analysis that requires sourcing and synthesis
- Writing anything where you have prior knowledge that could bias you

Skip the loop for:
- Simple factual answers (dates, names, references)
- Procedural actions (file edits, git commits, config changes)
- Conversational responses that do not require research

## Self-Check -- HARD GATE

Feynman gate: every item below MUST be confirmed before producing
substantive output. The output MUST NOT be delivered with any item
unconfirmed.

- [ ] Step 1 completed from memory (no sources, no search)  (PASS / HALT)
- [ ] Step 2 produced explicit gap list  (PASS / HALT)
- [ ] Step 3 searched and filled every gap  (PASS / HALT)
- [ ] Step 4 rewritten fresh (not edited Step 1)  (PASS / HALT)
- [ ] Step 5 cross-checked against agentic-brain  (PASS / HALT)
- [ ] Step 6 completed: artifact written if warranted  (PASS / HALT)
- [ ] Step 1 preceded Step 3 (critical ordering constraint)  (PASS / HALT)

## Steps

### 1. Blank Page

Write everything known about the topic. No sources, no notes, no search.
Open a blank canvas (or write in your thinking block) and dump raw knowledge.
This is the diagnostic -- it reveals what you actually know vs. what you
think you know.

**PASS:** A complete knowledge dump. Every claim, every connection, every
uncertainty -- written from memory alone.
**HALT:** If you are tempted to look something up mid-stream. Resist. The
gap between Step 1 and Step 4 IS the learning.

### 2. Identify Gaps

Review the Step 1 output and ask:
- What could not be explained?
- What was hedged or qualified with "I think" or "probably"?
- What connections are missing or incomplete?
- What numbers or dates are approximate?

List every gap explicitly. These are your search targets for Step 3.

### 3. Search and Research

Fill every gap identified in Step 2. Use:
- `web_search` for current information, market data, news
- `memory_search` for prior work, decisions, and context in memory
- Clone the agentic-brain and search for library topics, insights,
  and prior reflections that relate to this topic

Cross-reference sources. Resolve contradictions -- if two sources
disagree, investigate which one is correct and document why.

### 4. Synthesize

Rewrite your understanding from scratch. Do not edit Step 1. Write fresh.

- Start with what changed between Step 1 and now.
- Integrate the research results. Cite sources.
- State your confidence level for each major claim.
- The gap between Step 1 output and this output IS the learning.
  If nothing changed, you either skipped Step 1 honestly or the topic
  is so shallow the loop was unnecessary.

### 5. Cross-Check

Does this contradict anything in the agentic-brain? Search for related
topics and prior artifacts. If yes, resolve it explicitly:

- State the contradiction.
- Explain which source is more current or reliable.
- Cross-link the conflicting documents so future readers can trace the
  resolution.

### 6. Write the Artifact

The Feynman pass (Steps 1-5) is raw material. The artifact is the
polished deliverable. Follow the appropriate write-x skill for format
and quality gates. The blank page revealed what you actually knew;
knew; the research filled the gaps; the cross-check verified against
the brain.

Not every Feynman Loop produces an artifact. If the topic does not
produce a durable result worth preserving, skip artifact creation.
The loop itself is the quality gate -- the artifact is only written
when there is something worth preserving in the brain.

## Related

- AGENTS.md Feynman Loop section -- the gate instruction that triggers this skill
- `skills/session-end/SKILL.md` -- post-session quality review (step 1: Schoen Loop)
- `skills/write-reflection/SKILL.md` -- Reflection writing format and quality gates
- `governance/template-skills.md` -- skill construction rules
