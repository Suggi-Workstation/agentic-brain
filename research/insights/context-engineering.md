---
name: context-engineering
id: 20260717T004000Z
tier: insight
source:
  - 20260717T004100Z
author: ava
tags: [context-engineering, context-window, attention-budget, context-rot, compaction, prompt-caching]
links:
  - research/insights/prompt-engineering.md
  - research/insights/openclaw-manual.md
  - research/insights/deepseekv4pro.md
---

# Context Engineering -- The Art of Curating What the Model Sees

## The Insight
Context engineering is the discipline of curating the set of tokens
sent to a language model at inference time. It is the natural
progression of prompt engineering: instead of optimizing individual
prompts, you optimize the entire configuration of context -- system
instructions, conversation history, tool results, retrieved documents,
and injected files -- to maximize output quality against a finite
attention budget. As context length increases, accuracy and recall
degrade (context rot), making curation just as important as capacity.

## Evidence

This insight synthesizes Anthropic's "Effective Context Engineering for
AI Agents" (2025), Anthropic's context windows documentation, OpenClaw's
context system documentation, and Lilian Weng's agent architecture
survey.

### Source 1: Anthropic -- Effective Context Engineering (2025)

Anthropic frames context engineering as the successor to prompt
engineering. Key findings:

- **Attention budget -- a finite resource.** LLMs have an attention
  budget that depletes as context grows. The transformer architecture
  creates n-squared pairwise relationships between tokens. As context
  length increases, the model's ability to capture these relationships
  gets stretched thin. Every new token depletes the budget by some
  amount.

- **Context rot -- accuracy degrades with length.** Across all models,
  as token count grows, recall accuracy decreases. This is not a
  cliff but a gradient: models remain capable at longer contexts but
  show reduced precision. The mechanism: models develop attention
  patterns from training data where shorter sequences are more common,
  giving them fewer specialized parameters for context-wide
  dependencies.

- **The Goldilocks zone for system prompts.** System prompts should
  strike a balance between two failure modes: (1) hardcoding complex,
  brittle logic that creates fragility, and (2) providing vague,
  high-level guidance that fails to give concrete signals. The
  optimal altitude: specific enough to guide behavior, flexible
  enough to provide strong heuristics.

- **Minimal viable tool set.** Bloated tool sets cause ambiguous
  decision points. If a human engineer cannot definitively say which
  tool to use, the agent cannot be expected to do better. Tools
  should be self-contained, robust to error, and have minimal
  functional overlap.

- **Few-shot examples: quality over quantity.** Adding examples is
  well-established best practice, but stuffing a "laundry list" of
  edge cases into prompts creates bloat without proportional benefit.
  Each example should earn its token cost.

- **Context is iterative.** Unlike prompt engineering (discrete task
  of writing a prompt), context engineering is iterative. Curation
  happens each time you decide what to pass to the model. This is
  especially critical for agent loops that generate more data each
  turn.

- **Organize prompts into distinct sections.** Use XML tags or
  Markdown headers to delineate sections. Start with a minimal
  prompt, test with the best model, add instructions and examples
  based on failure modes.

### Source 2: Anthropic -- Context Windows Documentation (2026)

- **Context window sizes:** Claude Opus/Sonnet 5 have 1M-token windows.
  DeepSeek V4 Pro also has 1M tokens. Large but finite.

- **Everything counts toward context:** system prompt, messages, tool
  results, images, documents, tool definitions. Extended thinking
  tokens count too and are billed as output.

- **Prompt caching:** input count is split across `input_tokens`,
  `cache_read_input_tokens`, and `cache_creation_input_tokens`.
  All three count toward the window.

- **Compaction/editing:** Claude supports server-side compaction.
  Previous thinking blocks can be cleared to preserve token capacity.

### Source 3: OpenClaw -- Context System (2026)

OpenClaw builds its own system prompt each run. The context includes:

- **System prompt:** rules, tools, skills list, time/runtime, injected
  workspace files (SOUL.md, AGENTS.md, etc.).
- **Conversation history:** user messages + assistant messages.
- **Tool calls/results + attachments:** command output, file reads,
  images/audio.
- **Skills:** only metadata is injected; full skill instructions are
  loaded on demand via `read`.

- **Bootstrap limits:** `bootstrapMaxChars` (default 20K per file,
  ours: 50K) and `bootstrapTotalMaxChars` (default 60K, ours: 120K)
  cap injected workspace content.

- **Compaction:** `/compact` summarizes older history. Auto-compaction
  fires when approaching the context limit. Memory flush runs before
  compaction. Tool-call/result pairs are preserved at the boundary.

- **Inspection tools:** `/context list` (injected files + sizes),
  `/context detail` (per-file, per-tool, per-skill breakdown),
  `/context map` (treemap visualization).

- **Truncation warnings:** `bootstrapPromptTruncationWarning` controls
  whether truncation warnings are injected into the prompt (`off`,
  `once`, `always`; default `always`).

### Source 4: Lilian Weng -- Agent Architecture (2023, updated)

Key distinctions for context in agent systems:

- **Short-term memory (working memory):** the in-context learning --
  what is in the current context window. Bounded by the model's
  token limit. This is "what the agent is thinking about right now."

- **Long-term memory:** external knowledge stores (vector databases,
  file systems, git repos) that persist across sessions. Retrieved
  on demand via tools. This is "what the agent has learned over time."

- **Planning:** task decomposition, self-reflection, and iterative
  refinement consume context budget. Each planning step adds tokens
  to the working memory.

- **ReAct pattern:** Thought -> Action -> Observation cycles. Each
  cycle generates more tokens for the next turn. Context management
  must prune or summarize older cycles.

## Implications

### For Our Agent Architecture

1. **Our bootstrap files ARE the system prompt at the Goldilocks
   altitude.** Anthropic recommends organization into distinct
   sections with XML or Markdown headers. Our SOUL.md (Identity +
   Prime Directives), AGENTS.md (Procedures + Gates), and MEMORY.md
   (Facts + Decisions) provide exactly this: specific enough to guide
   behavior, flexible enough to provide heuristics rather than
   if-else rules. We are in the Goldilocks zone.

2. **Bootstrap limits are our first line of defense against context
   rot.** Our 50K/120K bootstrap config is well above defaults but
   still a fraction of the 1M context window. The real risk is not
   bootstrap files -- it is conversation history accumulating over
   a long session. Auto-compaction is critical.

3. **Every tool call burns attention budget.** Each tool call adds
   its result to the context. Long exec outputs, large file reads,
   and verbose web_fetch results all consume tokens. This is why
   our templates specify lean, structured outputs -- every byte
   saved in tool output is budget preserved for reasoning.

4. **Memory_search is long-term memory retrieval into working memory.**
   When I run memory_search, the results are injected into the
   context. This is Lilian Weng's long-term -> working memory bridge.
   The key insight: over-retrieval (too many search results) burns
   attention budget without proportional benefit.

5. **The Feynman Loop is context curation in practice.** Step 1
   (blank page) puts existing knowledge into context. Step 3 (search)
   adds external knowledge. Step 4 (synthesize) produces the final
   curated set. The loop is literally: populate context with known +
   discovered -> produce output from curated context.

### What We Are Doing Right
- Bootstrap files organized into distinct sections at Goldilocks
  altitude (specific enough, not brittle)
- Bootstrap limits configured above defaults (50K/120K)
- Auto-compaction enabled for long sessions
- Memory flush before compaction
- Tools produce structured, lean outputs
- Templates enforce minimal, high-signal content

### What We Could Improve
- **Add context inspection to the preflight.** Currently I do not
  check `/context list` at session start to see which files are
  truncated. A file showing TRUNCATED in the context report means
  the model is operating on incomplete instructions.
- **Monitor context rot in long sessions.** After 200K+ tokens of
  conversation, attention quality degrades. Our Schoen Loop should
  include a context health check ("how full is the window?") at
  session end, not just at compaction time.
- **Tool output pruning.** Some of our exec commands return verbose
  output. We do not have a convention for trimming tool results.
  A simple rule ("prefer --quiet flags, pipe through tail -50 for
  long outputs") would save thousands of tokens per session.
- **Conversation turnaround cost.** Each user message + my reply
  accumulates in the context forever (until compaction). This is
  the single largest consumer of the 1M window. Over a long session,
  conversation history dominates over bootstrap files by 10:1 or
  more. The Schoen Loop should surface this.

## Counter-evidence
This insight would be invalidated if:
- Future models eliminate context rot (attention quality remains
  constant regardless of context length). No model has achieved
  this yet; the n-squared attention architecture makes it
  structurally unlikely.
- Context windows become so large and models so efficient that
  curation is unnecessary. At 1M tokens today with visible
  degradation at the high end, this threshold is still far away.

## Version History
| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-17 | ava | Initial insight from Anthropic, OpenClaw, and Lilian Weng. |

## Cross-Links
- `research/insights/prompt-engineering.md` -- the precursor discipline
  that context engineering builds upon
- `research/insights/openclaw-manual.md` -- our platform's context system
- `research/insights/deepseekv4pro.md` -- our model's 1M context window
- `governance/system-constitution.md` -- Simplicity & Inversion applies
  to context curation
