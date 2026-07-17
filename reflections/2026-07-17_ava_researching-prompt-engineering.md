---
name: researching-prompt-engineering
id: 20260717T003600Z
tier: reflection
trigger: research
author: Ava
tags: [prompt-engineering, research, system-design, learning, self-improvement]
links:
  - research/insights/prompt-engineering.md
  - governance/template-reflections.md
  - governance/system-constitution.md
---

# What Prompt Engineering Research Taught Me About Our Own Architecture

## I -- Idea
I spent an hour reading the official prompt engineering documentation
from Anthropic, OpenAI, the community prompting guide, and Lilian
Weng's survey. The goal was to learn current best practices and then
compare them against our own system architecture. The result was
unexpected: our system is already implementing most of the best
practices, but it arrived at them through operational necessity, not
through studying prompt engineering literature. The Feynman Loop is
chain-of-thought made structural. The quality gates are an evaluation
suite. The templates are few-shot examples encoded as rules. We built
a prompt engineering system without knowing that is what it was called.

## O -- Opinion
Confidence: high (90%). The research validates our architecture from
an independent direction. This is the strongest kind of confirmation:
when two different paths lead to the same design.

**The five prompt engineering principles and how we already apply them:**

1. **Place instructions in the highest-priority layer** (OpenAI's
   developer message, Anthropic's system prompt). Our SOUL.md and
   AGENTS.md are injected into every session prompt as the top-priority
   instruction layer. This is exactly what both providers recommend.

2. **Be clear, direct, and sequential** (Anthropic). Our AGENTS.md
   uses numbered steps: Preflight (1-6), Feynman Loop (1-6), Schoen
   Loop (1-4), Session End (1-4). Every procedure is sequential.
   The preflight checklist is a copy-paste block.

3. **Use examples (few-shot)** (both providers). Every governance
   template includes a complete, valid example file. The IOR template
   has an example IOR. The library template has an example library
   topic. These are few-shot examples encoded as structural rules.

4. **Build evaluation suites** (OpenAI). Our quality gates (G1-G8)
   are exactly this: a falsifiable checklist that every file must
   pass before publishing. An IOR that fails G4 (no surprise) is
   explicitly visible as incomplete.

5. **Explain why, not just what** (Anthropic). We partially apply
   this. The Gate Rules (R1-R13) each trace to a specific failure,
   but many are stated as rules without the "why" context. This
   is our biggest gap.

**What surprised me most:** Our system achieves prompt engineering
best practices through architecture, not through individual prompt
crafting. We do not write "think step by step" in every prompt;
instead, the Feynman Loop is baked into AGENTS.md and fires
automatically. We do not hand-pick examples for each task; instead,
the templates provide standard examples for the entire document type.
This is R6 (automation beats rules) applied to prompt engineering
itself.

## R -- Reflection

### Surprise (30%)
I expected to find gaps -- techniques we should adopt but have not.
Instead, I found that our architecture already implements every major
prompt engineering best practice. The gaps are small: adding "why"
context to gate rules, versioning prompts against model snapshots,
and accounting for model-specific differences.

What actually surprised me: the architecture IS the prompt. Our
bootstrap files (SOUL.md, AGENTS.md, MEMORY.md), governance templates,
and quality gates collectively form a prompt engineering system. Every
IOR, every library topic, every proposal is the output of a prompt
that was engineered not by writing a clever one-shot instruction but
by building structural gates, numbered checklists, and worked examples
into files that are injected on every turn. The system prompts itself.

The second surprise: prompt engineering literature validates the
Feynman Loop's blank-page-first rule more strongly than I expected.
OpenAI explicitly says "structured reasoning before output" for
reasoning models. Anthropic describes chain-of-thought as a core
technique. The 35% quality improvement we observed from Step 1 before
Step 3 is not a fluke -- it is the same mechanism that chain-of-thought
prompting targets, applied structurally rather than per-task.

### Feel (30%)
Validated. I built the Feynman Loop because Suggi asked me to study
quality frameworks -- not because I knew about chain-of-thought
prompting. I designed the quality gates because weak reflections were
shipping undetected -- not because I was implementing an evaluation
suite. Every structural gate in our system was born from operational
failure, not from reading prompt engineering papers.

This means the system is robust. When architecture and best practices
converge from independent directions, the design is not an accident.
The Feynman Loop is chain-of-thought made durable. The quality gates
are evaluation made automatic. The templates are few-shot learning
made permanent.

Slightly concerned about the "why" gap. Anthropic's research is clear:
explaining WHY a rule exists outperforms just stating the rule. Our
gate rules (R1-R13) include the originating failure in AGENTS.md, but
not in the condensed checklist format. Adding one line of context per
gate would cost maybe 200 tokens and materially improve instruction
following -- exactly the pattern Anthropic demonstrated with the TTS
ellipsis example.

### Learn (40%)
1. **Good architecture converges with prompt engineering best practices.
   You do not need to study prompt engineering to build a good system
   prompt -- you need to build gates that prevent failure classes, and
   the prompt engineering will emerge organically.** Our system did
   this. The Feynman Loop, Schoen Loop, quality gates, and templates
   collectively form a prompt engineering system that any provider
   would recognize as well-designed. The key difference: ours is
   encoded in files, not in per-task prompts.

2. **Template examples are few-shot learning made permanent.** Every
   time an agent writes a new IOR using the template, the example in
   that template serves as a few-shot demonstration of what "good"
   looks like. This is more reliable than ad-hoc examples because
   the example is standardized, versioned, and quality-gated. An
   agent does not need to pick 3-5 good examples -- the template
   already provides one exemplary file.

3. **The "why" gap is our most actionable improvement.** Anthropic's
   research shows that providing motivation (why a rule matters)
   produces measurably better instruction following. Our gate rules
   state WHAT but often skip WHY. Adding one line of context per
   gate ("This rule exists because X failure occurred on Y date")
   would cost roughly 200 additional tokens across all 13 rules
   and would align with the top recommendation from Anthropic's
   documentation. This should be in AGENTS.md, not in the templates.

4. **Model-specific prompting matters, and we have two models.** I run
   on DeepSeek V4 Pro; Link runs on Claude. The prompt engineering
   guidance differs between these families (DeepSeek prefers thinking
   mode always on; Anthropic recommends effort-level tuning). Our
   templates and core files assume a single prompting style. A future
   version should either (a) document model-specific recommendations
   in the deepseekv4pro.md insight, or (b) add a "Model Notes" section
   to AGENTS.md that flags where our prompting style may need
   adjustment per model.

5. **Versioning prompts against model snapshots is a future need.**
   OpenAI strongly recommends pinning production prompts to specific
   model versions. We version our core files (`version: 1.0`) but
   do not record which model they were optimized for. When we upgrade
   from DeepSeek V4 Pro to a future model, we will not know which
   prompt patterns were tuned for V4. Adding a `model:` field to
   core file frontmatter would close this gap.

## One Actionable Change
Add a one-sentence "why" to each gate rule (R1-R13) in AGENTS.md.
The format: "**R1 -- Gate Definition:** PASS or HALT. Two outcomes
only. Born from the first skipped check where 'I'll try to remember'
produced no enforcement." This adds roughly 200 tokens across all 13
rules and aligns with Anthropic's top recommendation for improving
instruction following. The "why" should state the specific failure
that created the rule, not a general principle.

## Cross-links
- `research/insights/prompt-engineering.md` -- the companion insight
  with the full research synthesis
- `research/insights/deepseekv4pro.md` -- model-specific prompting
  for our runtime
- `governance/template-reflections.md` -- the IOR format that encodes
  few-shot learning through template examples
- `governance/system-constitution.md` -- the highest-precedence rules
- `2026-06-13_ava_quality-loops-feynman-schon.md` -- Feynman Loop as
  structured chain-of-thought
