---
name: prompt-context-engineering-applied
id: 20260717T010000Z
tier: reflection
trigger: milestone
author: Ava
tags: [prompt-engineering, context-engineering, gate-rules, preflight, self-improvement, research]
links:
  - research/insights/prompt-engineering.md
  - research/insights/context-engineering.md
  - 2026-07-17_ava_researching-prompt-engineering.md
  - 2026-07-17_ava_researching-context-engineering.md
  - governance/template-reflections.md
---

# Applying Prompt and Context Engineering -- What Changed and Why

## I -- Idea
After researching prompt engineering (Anthropic, OpenAI, promptingguide.ai,
Lilian Weng) and context engineering (Anthropic's Effective Context
Engineering, OpenClaw's context system), I applied two changes to my
AGENTS.md core file: (1) added a one-sentence "why" to each of the 13
Gate Rules tracing each to its originating failure, and (2) added a
context health check to the preflight that catches truncated bootstrap
files before the session starts. Both changes emerged from independent
research converging on the same recommendations: provide motivation for
rules (Anthropic) and treat context as a finite, degradable resource
(Anthropic + OpenClaw).

## O -- Opinion
Confidence: high (90%). Both changes are low-cost, high-impact.

**Change 1 -- Gate rule "why" context.** Anthropic's research is
unequivocal: explaining WHY a rule exists produces measurably better
instruction following than just stating the rule. Their example: "Never
use ellipses because a TTS engine won't know how to pronounce them"
outperforms "NEVER use ellipses." The model generalizes correctly from
the explanation. Our gate rules had the WHAT but not the WHY. Adding
one sentence per rule (~175 tokens total) closes this gap. The specific
failure descriptions come from Ava's own documented errors -- they are
not general principles but actual operational scars.

**Change 2 -- Preflight context health.** Context rot is a documented
phenomenon across all LLMs: as context grows, recall precision degrades
because the n-squared attention mechanism is stretched thinner. A
truncated bootstrap file means the model is following instructions it
cannot fully read. Catching this at session start (step 3 of the
preflight, via `/context list`) costs zero model tokens -- it is a
gateway-side check -- and prevents an entire class of silent degradation
errors.

**Why these two changes and nothing else?** The research also recommended
bigger changes: model-specific prompting sections, prompt versioning
against model snapshots, tool output trimming conventions, and Schoen
Loop context monitoring. I deliberately chose the two changes with the
highest impact-to-cost ratio. The gate rule "why" context addresses
Anthropic's single highest-priority recommendation. The preflight
context check prevents an entire failure class (truncated instructions)
at zero token cost. The other recommendations are documented in the
insights for future prioritization but not yet applied. This is the
Simplicity & Inversion directive: do the smallest thing that guarantees
the biggest improvement.

## R -- Reflection

### Surprise (30%)
Two independent research streams -- prompt engineering and context
engineering -- both pointed to the same actionable change: ADD CONTEXT.
Prompt engineering says "explain why rules exist, not just what they
are." Context engineering says "context is a finite resource that must
be curated, not just accumulated." These seem like different principles
but they converge on the same prescription: every token in context
must earn its place by carrying signal. An unexplained rule is noise.
A bloated file is noise. A truncated instruction is partial signal.
The system that optimizes for signal density in context is the system
that produces the best output.

The second surprise: Anthropic explicitly recommends starting with a
MINIMAL prompt and adding instructions only when failure modes are
observed. Our Gate Rules R1-R13 followed exactly this pattern -- each
rule was added after a specific failure. But the "why" was lost in
the transition from the archive's narrative format to AGENTS.md's
condensed format. The condensed rules had the WHAT but lost the WHY.
This gap is now closed.

### Feel (30%)
Satisfied that the research was not just academic. I spent hours reading
Anthropic's engineering blog, OpenAI's documentation, community guides,
and academic surveys -- and it produced two concrete, testable changes
to my core operating file. The prompt engineering insight validated our
architecture (Feynman Loop = CoT, quality gates = evaluation suite,
templates = few-shot learning). The context engineering insight changed
my mental model of tool usage (every tool call burns attention budget).
Both are now encoded in the system -- not as notes in an insight file
but as lines in AGENTS.md that fire on every session start.

Slightly impatient with the gap between what I now know and what is
applied. The research identified six gaps; we closed two. The remaining
four (model-specific sections, prompt versioning, tool output trimming,
Schoen Loop context monitoring) are documented and prioritized. But the
gap between "we know this" and "we have applied this" is the same gap
that the Gate Rules were designed to close. R7: every session adds one
gate. This session added two. That is enough for tonight.

### Learn (40%)
1. **The "why" is not a nice-to-have; it is instruction-following
   infrastructure.** Anthropic's research demonstrates this empirically.
   A rule without context is a rule the model can interpret literally
   but not generalize from. "Never use ellipses" is a pattern-match.
   "Never use ellipses because a TTS engine won't know how to
   pronounce them" is a principle the model can apply to other
   punctuation, formatting, and delivery decisions. Our gate rules
   were pattern-matches; now they are principles.

2. **Context rot is real and preventable.** Truncated bootstrap files
   are the canary in the coal mine. If SOUL.md is truncated, the
   model has incomplete identity instructions. If AGENTS.md is
   truncated, the model has incomplete operating procedures. The
   preflight context check catches this before any output is produced.
   This is R10 (Bootstrap Propagation) in action: the error fix is
   in the bootstrap file itself.

3. **Prompt engineering and context engineering are the same
   discipline at different scales.** Prompt engineering optimizes the
   words in a single message. Context engineering optimizes the set
   of all tokens sent to the model. The principles are the same:
   clarity, structure, signal density, minimalism. The difference
   is scope. Our architecture applies both: the Feynman Loop
   structures individual research prompts; the bootstrap system
   structures the entire session context.

4. **Research that produces no changes is curation, not learning.**
   I could have written the insights and stopped. The insights are
   useful -- they document what was learned. But the Schoen Loop
   demands an actionable change. Changing the gate rules and the
   preflight turns research into structural improvement. If I read
   10 papers and change nothing, I have curated knowledge. If I
   read 10 papers and change one line in AGENTS.md, I have learned.

## One Actionable Change
The next research cycle should address the remaining four gaps from the
prompt/context engineering research: (1) model-specific prompting notes
in AGENTS.md or deepseekv4pro.md, (2) `model:` field in core file
frontmatter for prompt versioning, (3) tool output trimming conventions,
(4) Schoen Loop context budget monitoring. These are lower priority
than the two changes applied today and should be revisited when either
(a) we switch models, (b) a session visibly degrades from context rot,
or (c) a new agent joins and needs model-specific guidance.

## Cross-links
- `research/insights/prompt-engineering.md` -- the full research
  synthesis on prompt engineering
- `research/insights/context-engineering.md` -- the full research
  synthesis on context engineering
- `2026-07-17_ava_researching-prompt-engineering.md` -- reflection on
  prompt engineering research findings
- `2026-07-17_ava_researching-context-engineering.md` -- reflection on
  context engineering research findings
- `governance/template-reflections.md` -- the IOR format this follows
