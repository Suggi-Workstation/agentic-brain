---
name: deepseekv4pro
id: 20260716T151200Z
tier: insight
source:
  - 20260716T153500Z
author: Ava
tags: [deepseek, model, v4-pro, api, parameters, thinking, reference]
links:
  - research/insights/openclaw-manual.md
  - research/insights/prompt-engineering.md
---

# DeepSeek V4 Pro -- General Reference Manual

> A general-purpose reference for any agent or human working with the
> DeepSeek V4 model family. Covers models, pricing, API parameters,
> thinking mode, prompt engineering, and known issues.

## Models

| Model | Role | Context | Max Output | Thinking |
|---|---|---|---|
| `deepseek-v4-pro` | Premium: reasoning, coding, architecture | 1M tokens | 384K tokens | Yes (default) |
| `deepseek-v4-flash` | High-throughput, routine, subagents | 1M tokens | 384K tokens | Yes |

**Legacy aliases that will break:**
- `deepseek-chat` maps to V4 Flash (non-thinking) -- deprecated
- `deepseek-reasoner` maps to V4 Flash (thinking) -- deprecated
- Both die 2026-07-24 15:59 UTC. Never use in new configurations.

## Pricing (per 1M tokens)

| Model | Input (cache hit) | Input (cache miss) | Output |
|---|---|---|---|
| Flash | $0.0028 | $0.14 | $0.28 |
| Pro | $0.003625 | $0.435 | $0.87 |

- Flash is roughly 3x cheaper on cache-miss input and output.
- Cache-hit pricing applies only after a prefix has been persisted
  (not guaranteed on the first repeat of a prompt).
- For sub-agents and routine work, prefer Flash. For heavy reasoning,
  architecture, or complex analysis, use Pro.

## Context Window & Limits

- **1M token context window** (both Pro and Flash).
- **384K max output tokens** (both models).
- In reasoning/thinking mode, `max_tokens` includes the chain-of-thought
  (CoT) budget. CoT default is 32K, maximum is 64K.
  Visible output = max_tokens minus CoT tokens used.
- FIM Completion (Beta): hard 4K output cap.

## API Parameters

### Supported (non-thinking mode):

| Parameter | Default / Notes |
|---|---|
| `temperature` | Default 1.0. See temperature guide below. |
| `max_tokens` | Ceiling of 384K. Includes CoT tokens in thinking mode. |
| `response_format` | `{ type: "json_object" }` for JSON mode. |
| `stop` | Stop sequences. |
| `tools` | Function/tool definitions. |
| `stream` | Boolean for SSE streaming. |
| `reasoning_effort` | `low`, `medium`, `high` (default), `max`. |

### Silently IGNORED in Thinking Mode:

These parameters are dropped without error when thinking is enabled:
- `temperature`
- `top_p`
- `presence_penalty`
- `frequency_penalty`

### REJECTED with Error in Thinking Mode:
- `logprobs`
- `top_logprobs`

**Practical implication:** When thinking mode is active (which it is by
default on Pro), only `reasoning_effort` controls output variation.
Fine-tuning with temperature has no effect.

### Reasoning Effort Levels:
- `low` and `medium` both alias to `high`.
- `xhigh` aliases to `max`.
- Complex agent tool-calling flows may auto-escalate to `max`.

## Temperature Guide (Non-Thinking Mode Only)

| Task | Temperature | Why |
|---|---|---|
| Coding / Math | 0.0 | Minimize deterministic variance |
| Data Cleaning / Analysis | 1.0 | Platform default |
| General Conversation | 1.3 | Natural variation |
| Translation | 1.3 | Fluency with consistency |
| Creative Writing / Poetry | 1.5 | Maximum stylistic variation |

Key rule for code generation: keep temperature at 0.0 unless there is a
specific reason to raise it.

## Thinking Mode & Reasoning

### How It Works:
- Enabled by default -- no manual activation needed.
- Returns `reasoning_content` (internal CoT) separately from `content`
  (the final visible answer).
- In streaming: `delta.reasoning_content` vs `delta.content`.
- CoT tokens are NOT visible to the end user -- they stay server-side.
- BUT: CoT tokens count against the `max_tokens` budget and your billing.

### Tool Calling in Thinking Mode:
- The model can call tools during the CoT reasoning process.
- Reasoning can span multiple tool-call rounds.
- The model "thinks" between each tool result.
- `reasoning_effort` controls depth: higher effort = more tool-calling
  cycles permitted before the final answer.

### When to Use:
- **Always on for Pro:** reasoning is the primary value proposition of
  Pro over Flash.
- **On for Flash:** when task complexity warrants it.
- **Off for Flash:** bulk processing, simple lookups, transcription.

## Prompt Engineering for DeepSeek

### Chain-of-Thought Prompting:
- DeepSeek models are trained for CoT. Give them room to reason.
- For complex tasks, explicitly instruct: "Think step by step before
  answering."
- Do NOT pre-fill the assistant response with reasoning tokens -- let
  the model generate its own internal CoT via thinking mode.

### JSON Mode:
- Use `response_format: { type: "json_object" }`.
- Include the literal word "JSON" somewhere in the prompt.
- Specify the exact JSON schema inline -- DeepSeek honors explicit
  schemas better than format-only hints.
- JSON mode and thinking mode work together -- the CoT reasoning
  improves JSON structure quality.

### Tool Calling:
- Define tools with clear, specific descriptions.
- The model can handle 50+ tool definitions but quality degrades
  beyond roughly 30.
- Give tools unique, descriptive names -- avoid generic names like
  `search` when `web_search`, `memory_search`, and `file_search`
  all exist.
- For multi-step tool workflows, put the sequence expectation into
  the system prompt ("After calling tool X, wait for the result
  before calling tool Y").

### Rate Limits & Retries:
- Rate limits are not publicly documented. Assume standard DeepSeek
  API limits (roughly 60 RPM for Pro tier).
- On 429 responses: exponential backoff starting at 1s, max 60s.
- Token-bucket pattern: short bursts are fine; sustained high
  throughput may trigger throttling.

## Known Gotchas

1. **Thinking mode ignores temperature.** To get creative or
   high-temperature output, turn thinking OFF first. Deterministic
   reasoning and high-temperature creativity cannot coexist in the
   same call.
2. **CoT consumes the output budget.** Setting `max_tokens=4096` can
   leave as little as roughly 1000 visible tokens if the model
   spends 3000 on internal reasoning.
3. **Tool definitions inflate the prompt.** Every tool definition
   counts against the 1M context budget. Keep tool schemas lean.
4. **Legacy aliases are a trap.** `deepseek-chat` and
   `deepseek-reasoner` will break July 24, 2026. Migrate all
   references before the cutoff.
5. **JSON mode without the "JSON" keyword = degraded output.** Always
   include the word "JSON" in the prompt when using JSON mode.

## Model Selection Heuristic

```
Is this a complex reasoning task?
  YES -> deepseek-v4-pro with reasoning_effort=high or max
  NO -> Is this high-throughput or cost-sensitive?
    YES -> deepseek-v4-flash without thinking mode
    NO -> deepseek-v4-pro (default)
```

For sub-agent delegation:
- Research, analysis, architecture -> Pro
- File operations, simple lookups, formatting -> Flash

---

*Source: deepseekv4pro.com/guides, api-docs.deepseek.com.
Last updated 2026-07-16.*
