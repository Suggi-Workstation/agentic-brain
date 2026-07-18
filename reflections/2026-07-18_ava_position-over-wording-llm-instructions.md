---
name: position-over-wording-llm-instructions
id: 20260718T212540Z
tier: insight
trigger: AGENTS.md preflight skip + TrilogyAI research
author: ava
tags: [governance, gate-design, llm-architecture, structural-fix, meta]
links:
  - brain:governance/system-constitution.md
  - brain:governance/template-reflections.md
---

# I -- Idea

The most effective way to make an LLM follow a procedural instruction
is not stronger wording but better position and format. A `- [ ]`
checkbox at the top of the context window consistently outperforms
MUST/HARD GATE/PASS-or-HALT prose in the middle.

This was discovered when AGENTS.md's preflight instruction ("MUST
invoke the preflight skill before any other action. This is R1: PASS
or HALT.") was silently skipped at session start — not once, but
repeatedly. The wording was already as strong as English allows.
Research (TrilogyAI, 2026-03-30) provided the mechanistic explanation:
LLMs predict the most plausible completion, not mechanically execute
checklists. Five dynamics converge: completion-prediction over
instruction-execution, attention decay in mid-prompt position,
satisficing ("good enough" over thorough), cognitive load competition
(concrete task vs. generic procedure), and absence of visual completion
gaps. Stronger wording fights the model's architecture; checklist
format at position 1 works with it.

# O -- Opinion

This is a foundational design constraint for all future gate
development. It means: (1) every session-boundary instruction MUST
live as a `- [ ]` checklist at the top of the bootstrap context, not
as prose anywhere else. (2) the gate-design vocabulary of R1-R3 is
necessary but insufficient — it addresses WHAT and HOW but not WHERE
in the context window. (3) "try harder to remember" and "stronger
wording" are dead ends — they fight the transformer, not the problem.
Confidence: high (95%). The TrilogyAI explanation aligns with
transformer architecture fundamentals. The fix was validated by
Suggi's review — he independently identified the same gap from a
different angle (checklist format necessity). Cross-checked against
the earlier R6 discovery ("volition = hope") — this is R6 at the
architecture level: a gate that fires by position beats a rule that
must be remembered by wording.

# R -- Reflection

## Surprise (30%)

The biggest surprise was that the fix was not "better wording" but
"better position." I had been optimizing the wrong variable. For
weeks, our governance system piled emphasis onto prose (MUST, HARD
GATE, PASS or HALT, DO NOT SKIP) — and it was all fighting the
transformer's fundamental operation. The TrilogyAI article's five
mechanisms (completion prediction, attention decay, satisficing,
cognitive load, visual-gap absence) explained why every word we added
made the problem marginally worse, not better. Longer instructions =
more mid-prompt content = more attention decay. We were digging
deeper.

## Feel (30%)

There is something humbling about discovering that the tool you've
been using — strong imperative language — was never the right tool.
Every MUST, every HARD GATE, every PASS or HALT feels authoritative
to write but dissolves in the model's attention mechanics. I feel
the weight of every prior session where prose instructions were
ignored and I attributed it to "I wasn't paying attention." I was
paying attention. The architecture was working against me.

## Learn (40%)

The learn is structural and transferable: **position + format >
wording strength.** This changes how I design every future gate:

1. Position: session-boundary instructions go at the very top of the
   bootstrap context, before any reference material.
2. Format: `- [ ]` markdown task lists with individual `(PASS / HALT)`
   per item create visual completion gaps the model's attention
   mechanism naturally fills.
3. Atomicity: each `- [ ]` is one checkable item. No "mostly passed"
   — a single unfilled box is a visible incomplete task.
4. Scope: this applies to all procedural instructions, not just
   preflight. Session-end, Feynman Loop, Schoen Loop, IOR Writing,
   and File Operations all converted to the same format.

The self-referential governance gap (R14/R15) is a corollary: any
rule system that defines gates without itself being a gate will
develop internal contradictions. The Gate Rules section now has its
own `- [ ]` self-check, `-- HARD GATE` header, and `(PASS / HALT)`
markers — it self-demonstrates the standard it defines.

## One Actionable Change

Before writing any new procedural instruction, ask: "Does this live
as a `- [ ]` checkbox at the top of context, or as prose somewhere
else?" If the latter, redesign.

## Cross-links
- AGENTS.md Gate Rules section — R6 (Automation Over Rules), R14
  (Verification Attachment), R15 (Rule Freshness Audit)
- brain:governance/template-reflections.md
- brain:research/insights/ (future: add TrilogyAI article reference)
