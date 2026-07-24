---
name: context-window-management
id: 20260724T182104Z
tier: library-topic
domain: coding-agentic-ai
author: Ava
tags: [context-window, context-management, token-efficiency, agent-architecture, llm-compression, observation-masking]
links: [library/coding-agentic-ai/anchor-coding-agentic-ai.md]
---

# Context Window Management -- Why the Prompt Is the Scarce Resource in Agent Engineering

Context window management is the discipline of controlling what an AI
agent "remembers" during a session to maximize task performance while
minimizing token consumption, latency, and cost. Every turn an agent
takes adds reasoning traces, tool outputs, and observations to the
prompt; without management, context grows unbounded until it overflows
the model's window or degrades performance through attention dilution.
Effective context management is not a post-hoc optimization -- it is a
first-order design constraint that determines whether an agent can
complete long-horizon tasks at all.

## Background

The context window is the maximum number of tokens a language model can
process in a single forward pass. Early LLMs had windows measured in
thousands of tokens (GPT-3: 2,048; GPT-3.5: 4,096). Modern models
support dramatically larger windows -- Claude 3.5 Sonnet handles
200,000 tokens, GPT-4 Turbo supports 128,000, and Gemini 2.5 Pro
reaches 1 million. These numbers suggest abundance, but the operational
reality is different: every token in the context costs money (input
pricing), adds latency (quadratic attention complexity), and
contributes to the "lost-in-the-middle" phenomenon where model
attention degrades for information in the middle of long contexts
(Liu et al., 2024; Koshorek et al., 2025).

For AI coding agents -- which may run for dozens or hundreds of turns,
each generating reasoning traces, tool call results, file contents, and
error messages -- context grows rapidly. A single SWE-bench task can
generate 50,000+ tokens of trajectory. Without management, long-running
agents exhaust their context budget or become prohibitively expensive
before completing their work. JetBrains Research (2025) found that both
major context management approaches cut costs by over 50% compared to
unmanaged growth, without degrading task completion rates.

## Core Concepts

### The Unmanaged Baseline: Raw Agent Growth

In the simplest agent scaffolding (ReAct, CodeAct), the full trajectory
of reasoning, actions, and observations accumulates in the context
without bound. Each turn appends:

1. The model's reasoning trace (chain-of-thought).
2. The tool call or action specification.
3. The environment or tool output (observation).

This produces linear or super-linear context growth with turn count.
For an agent running 250 turns, the raw context may exceed 150,000
tokens -- approaching or exceeding practical limits even on large-window
models. The cost per turn also grows, since every turn reprocesses the
entire history. This is unsustainable for production agent systems.

### Observation Masking: Trimming Without Summarizing

Observation masking keeps the agent's reasoning and actions intact but
replaces older observations with placeholder messages once they fall
outside a fixed window. For example, SWE-agent implements a rolling
window: the last N turns of observations are preserved in full, while
older observations are replaced with "[Some details omitted for
brevity.]" The agent can still see what it did (actions, reasoning) but
not the full text of old tool outputs.

JetBrains Research (2025) found that observation masking not only cut
costs by over 50% but often matched or slightly beat LLM summarization
on benchmark tasks. The insight is counterintuitive: older tool outputs
are often irrelevant to current decisions, and their removal does not
impair performance. The rolling window size is the key hyperparameter
-- too small and the agent loses critical context; too large and costs
remain high. Tuning is agent- and task-specific.

### LLM Summarization: Compressing History into a Summary

An alternative approach uses a separate language model (or the agent
model itself in a dedicated step) to compress older trajectory segments
into structured summaries. OpenHands implements this pattern: a
summarizer model condenses past reasoning, actions, and observations
into compact text, which replaces the raw history in the context. The
most recent turns remain uncompressed to preserve detail for immediate
decisions.

Summarization produces more information-dense context than masking
because the summary captures the gist of what happened rather than
discarding it entirely. However, it introduces a new failure mode:
summarization errors. If the summarizer misrepresents a critical
observation -- a file path, an error message, a return code -- the
agent may make incorrect decisions based on corrupted history. It also
adds latency and cost from the summarization step itself.

### Hybrid Approaches

Production systems increasingly combine both techniques (JetBrains
Research, 2025): observation masking for the middle-distance history
(turns 5-30), LLM summarization for the deep history (turns 30+), and
full context for the most recent turns (1-5). This mirrors how human
developers work: detailed memory of what they just did, a rough summary
of the session so far, and only the highlights of work done hours ago.

### Progressive Disclosure and Context Engineering

Beyond compression, context management includes progressive disclosure:
the deliberate ordering and structuring of prompt content so the most
critical information appears first and the least critical last. This
exploits the "lost-in-the-middle" finding -- models attend best to the
beginning and end of the context window. System instructions, critical
rules, and the immediate task go at the top; reference material and
historical summaries go in the middle; the most recent turns go at the
bottom. Context engineering is the craft of designing what goes where
in the prompt to maximize effective attention.

## Evidence

Liu et al. (2024) demonstrated the "lost-in-the-middle" effect: in
multi-document question answering, model performance degrades
significantly when relevant information is placed in the middle of a
long context, even when the model's nominal window size is large enough
to contain it. This finding directly motivates progressive disclosure
and selective context management -- a larger window does not guarantee
effective use of all tokens within it.

JetBrains Research (2025) conducted controlled experiments comparing
raw agent growth, observation masking, and LLM summarization on the
SWE-bench-Verified benchmark with up to 250-turn trajectories. Key
findings:

- Both masking and summarization reduced token consumption by >50%
  versus unmanaged growth.
- Observation masking matched or exceeded summarization performance on
  task completion, despite being simpler to implement.
- The optimal approach was task-dependent: summarization outperformed
  masking on tasks requiring long-range reasoning across distant turns;
  masking outperformed on tasks where only recent observations mattered.
- A hybrid approach (masking + summarization) achieved the best overall
  results, with window size and summarization frequency requiring
  per-agent tuning.

The practical implication is that context management is not a solved
problem with a universal solution -- it is a design space with
tradeoffs that must be evaluated per use case.

## Implications

For **agent builders**, context management should be treated as a
first-class architecture component, not an afterthought. Design
decisions include: what to keep, what to compress, what to discard, and
in what order to present it. The choice of strategy (masking,
summarization, hybrid) depends on the agent's task horizon,
observation verbosity, and reliability requirements.

For **cost management**, context is the dominant operational expense in
long-running agent systems. An agent running 100 turns with unmanaged
context might consume 500,000 input tokens at $2.50/M tokens (GPT-4o
pricing) -- $1.25 per session. With 50% compression, that drops to
$0.63. At production scale (thousands of sessions per day), this
difference is material. Context management is as much an economic
discipline as a technical one.

For **system design**, context management interfaces with other agent
subsystems: memory and persistence (what gets stored between sessions),
tool design (how verbose should tool outputs be?), and evaluation
(when does context degradation cause task failure?). The discipline
bridges prompt engineering, systems architecture, and cost engineering.

## Common Pitfalls

**Treating larger windows as a substitute for management.** A 1M-token
window does not eliminate the need for context management -- it just
raises the ceiling. Attention dilution, cost, and latency scale with
context size regardless of the window limit.

**Over-summarizing critical details.** If the summarizer collapses an
error message from "TypeError at line 247: 'NoneType' object has no
attribute 'split'" to "a type error occurred," the agent loses the
information needed to fix the bug. Summarization must preserve
actionable detail, not just gist.

**One-size-fits-all tuning.** A window size of 5 turns may work for a
code-fix agent but fail for a debugging agent that needs to trace
causality across 20 turns. Hyperparameters must be tuned per agent and
per task family.

## Sources

1. JetBrains Research (2025). "Cutting Through the Noise: Smarter
   Context Management for LLM Agents."
   https://blog.jetbrains.com/research/2025/12/efficient-context-management/ [high]

2. Liu, N. F. et al. (2024). "Lost in the Middle: How Language Models
   Use Long Contexts." Transactions of the Association for
   Computational Linguistics (TACL), 12, 157-173.
   https://aclanthology.org/2024.tacl-1.9/ [high]

3. Maxim AI. "Context Window Management: Strategies for Long-Context AI
   Agents and Chatbots."
   https://www.getmaxim.ai/articles/context-window-management-strategies-for-long-context-ai-agents-and-chatbots [medium]

4. Machine Learning Mastery (2026). "Context Window Management for
   Long-Running Agents: Strategies and Tradeoffs."
   https://machinelearningmastery.com/context-window-management-for-long-running-agents-strategies-and-tradeoffs [medium]

5. Koshorek, O. et al. (2025). "Long-Context Language Models and the
   Attention Degradation Problem."
   https://openreview.net/forum?id=0OshX1hiSa [high]

## See Also

- `library/coding-agentic-ai/anchor-coding-agentic-ai.md` -- domain anchor defining the full scope of coding agent engineering.
