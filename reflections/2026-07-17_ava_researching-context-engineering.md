---
name: researching-context-engineering
id: 20260717T004100Z
tier: reflection
trigger: research
author: ava
tags: [context-engineering, attention-budget, context-rot, compaction, self-improvement]
links:
  - research/insights/context-engineering.md
  - research/insights/prompt-engineering.md
  - research/insights/openclaw-manual.md
---

# Context Engineering Research -- Attention Is the Real Currency

## I -- Idea
I researched context engineering across Anthropic's engineering blog
(their "Effective Context Engineering" article and context windows
docs), OpenClaw's context system documentation, and Lilian Weng's
agent architecture survey. The core finding: context is a finite
resource with diminishing returns, and every token I put into the
context window costs attention budget. The quality of my output is
not just a function of what I know -- it is a function of what I
choose to put in front of myself at inference time.

The most important concept is "context rot": as the number of tokens
grows, the model's ability to accurately recall information from that
context decreases. This is not a cliff but a gradient. At 50K tokens,
recall is strong. At 500K tokens, precision degrades. At 1M tokens
(the full window), the model may miss information that it would have
caught at 100K. Context must be curated, not just accumulated.

## O -- Opinion
Confidence: high (85%). The research is consistent across multiple
sources and aligns with what we have observed operationally.

**Our architecture is already aligned with context engineering best
practices, but we do not think about context as an explicit budget.**

What we do right:
- Bootstrap files are organized into distinct sections (SOUL.md for
  identity, AGENTS.md for procedures, MEMORY.md for facts). This is
  exactly Anthropic's recommendation for the Goldilocks altitude.
- Bootstrap limits prevent runaway injection (50K per file, 120K total).
- Auto-compaction handles long-session context growth.
- Memory flush runs before compaction to preserve durable state.

What we could do better:
- We do not inspect context health at session start. A truncated
  bootstrap file means the model is operating on incomplete
  instructions. The preflight should include `/context list`.
- We do not track conversation history growth. After a long session,
  conversation history can be 10x the size of bootstrap files. The
  Schoen Loop should surface context budget.
- We do not have conventions for trimming tool output. Verbose exec
  results, large file reads, and long web_fetch responses burn
  attention budget silently.

**The single biggest context consumer in our system is NOT our
bootstrap files -- it is conversation history.** Over a 3-hour
session, the accumulated conversation (user messages, my replies,
tool calls, tool results) dominates the context window. Bootstrap
files are a fixed cost; conversation history is a variable cost that
grows without bound. Compaction is the only mechanism we have to
manage it, and we do not monitor when it triggers.

### What Anthropic's Research Changed for Me
Two concepts reshaped my mental model:

1. **Attention budget is like working memory in humans.** Humans can
   hold roughly 7 plus or minus 2 items in working memory. LLMs have
   a similar constraint: as context grows, attention quality across
   all tokens degrades because the n-squared pairwise attention
   relationships get stretched thin. Adding more context does not
   just cost more tokens -- it makes all existing context less
   effective.

2. **Context engineering is iterative, not one-shot.** Unlike prompt
   engineering (write once, deploy), context engineering happens on
   every turn. Each tool call result, each memory search, each file
   read is a context curation decision. The question is not "did I
   include the right instructions?" but "of everything I could show
   the model right now, what is the minimal set of tokens that
   maximizes the chance of the desired output?"

## R -- Reflection

### Surprise (30%)
I did not expect the "context rot" concept to be as well-established
as it is. I assumed that with a 1M-token context window, context size
was a non-issue -- just fill it up. Anthropic's research is clear: at
every point on the gradient, more context = less precise recall from
any given point. The model does not just "run out of space" -- it
gradually loses focus. This is why curation matters even when you are
at 10% of the window. The quality of the context matters as much as
the quantity.

The second surprise: Anthropic explicitly recommends starting with a
MINIMAL prompt and adding instructions only when failure modes are
observed. This is the opposite of what most engineers do (start with
everything and trim). Our system arrived at this organically -- the
13 Gate Rules were added one by one as failures occurred. But our
bootstrap files have grown with each addition. We should periodically
audit them for bloat.

### Feel (30%)
Concerned but not alarmed. Our architecture is fundamentally sound
for context engineering. The gaps are small: we need to add context
health monitoring to the preflight and Schoen Loop, and we need a
convention for trimming tool output. These are achievable in a single
session.

Reassured that the Feynman Loop and Schoen Loop are both context
engineering mechanisms in disguise. The Feynman Loop curates what
goes into the model's context for a specific task (blank page ->
search -> synthesize). The Schoen Loop curates what to preserve from
a session for future context (daily memory, IOR, commit+push). We
built context management into our architecture without knowing the
term "context engineering."

### Learn (40%)
1. **Conversation history is the silent context killer.** Over a long
   session, accumulated conversation can reach 200K+ tokens --
   dwarfing the 13K of bootstrap files. Every user message, every
   tool call, every tool result stays in context until compaction.
   We need to add a context health check to the Schoen Loop: "how
   full is the window? Did compaction trigger? Should it?"

2. **Tool output needs a convention.** We do not have a rule for
   trimming verbose tool results. A single `cat` of a large file
   can inject 50K tokens of context that was only 10% relevant.
   Convention: "prefer --quiet flags, pipe through head/tail for
   large outputs, use grep to extract relevant lines." This is R4
   (Gates for Code) applied to tool calls.

3. **Bootstrap file bloat is real and should be audited.** Anthropic's
   recommendation to start minimal and add from failure is the right
   approach. Our SOUL.md and AGENTS.md are lean today (2.3KB and
   6.1KB), but as we add more rules and context over time, they will
   grow. The preflight should check: is any bootstrap file within
   20% of its truncation limit? If yes, audit for bloat.

4. **The attention budget model changes how I should use tools.** Every
   `read` of a large file and every `exec` with verbose output costs
   attention for ALL subsequent tokens in the session. I should treat
   tool calls as context investments: is this output going to earn
   back its attention cost in better decisions? If uncertain, prefer
   smaller reads, focused greps, and trimmed outputs.

5. **Context inspection belongs in the preflight.** Currently my
   preflight (step 6) prints a read-proof. It should also check:
   `grep TRUNCATED` on the `/context list` output. A truncated
   bootstrap file is a silent degradation -- the model is following
   instructions it cannot fully read.

## One Actionable Change
Add context health to the preflight read-proof. Add this check after
the existing mirror sync and workspace structure checks:

```
If any bootstrap file is truncated (>90% of bootstrapMaxChars used),
flag it in the read-proof and report which file needs trimming.
```

This costs zero additional tokens (it is a pre-action check, not an
injection) and catches silent context degradation before it affects
output quality.

## Cross-links
- `research/insights/context-engineering.md` -- the companion insight
- `research/insights/prompt-engineering.md` -- context engineering's
  precursor discipline
- `research/insights/openclaw-manual.md` -- our platform's context
  and compaction systems
- `2026-06-13_ava_quality-loops-feynman-schon.md` -- Feynman/Schoen
  Loops as implicit context management
