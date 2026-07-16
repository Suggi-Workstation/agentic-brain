---
name: deepseekv4pro
id: 20260716T151200Z
tier: core-insight
lock: approval-required
approved_by: Suggi
author: link
links:
---

> Self-reference manual. Written 2026-07-16 based on deepseekv4pro.com/guides
> and api-docs.deepseek.com. Update when model behavior changes.

## Models

| Model | Role | Context | Max Output | Thinking |
|---|---|---|---|---|
| `deepseek-v4-pro` | Premium: reasoning, coding, architecture | 1M tokens | 384K tokens | Yes (default) |
| `deepseek-v4-flash` | High-throughput, routine, subagents | 1M tokens | 384K tokens | Yes |

**Legacy aliases that will break:**
- `deepseek-chat` maps to V4 Flash (non-thinking) -- deprecated
- `deepseek-reasoner` maps to V4 Flash (thinking) -- deprecated
- Both die 2026-07-24 15:59 UTC. Never use in new flows.

## Pricing (per 1M tokens)

| Model | Input (cache hit) | Input (cache miss) | Output |
|---|---|---|---|
| Flash | $0.0028 | $0.14 | $0.28 |
| Pro | $0.003625 | $0.435 | $0.87 |

- Flash is ~3x cheaper on cache-miss input and output.
- Cache-hit pricing only applies after prefix persistence (not on first repeat).
- For sub-agents and routine work, prefer Flash. For heavy reasoning, use Pro.

## Context Window & Limits

- **1M token context window** (both models).
- **384K max output tokens** (both models).
- In reasoning/thinking mode, `max_tokens` includes the CoT budget.
  CoT default is 32K, max is 64K. Output = max_tokens - CoT used.
- FIM Completion (Beta): hard 4K output cap.

## API Parameters

### Supported (non-thinking mode):
| Parameter | Default / Notes |
|---|---|
| `temperature` | Default 1.0. See temperature guide below. |
| `max_tokens` | 384K ceiling. Includes CoT in thinking mode. |
| `response_format` | `{ type: "json_object" }` for JSON mode. |
| `stop` | Stop sequences. |
| `tools` | Function/tool definitions. |
| `stream` | Boolean for SSE streaming. |
| `reasoning_effort` | `low`, `medium`, `high` (default), `max`. |

### IGNORED in Thinking Mode (no error, just silently dropped):
- `temperature` -- ignored
- `top_p` -- ignored
- `presence_penalty` -- ignored
- `frequency_penalty` -- ignored
- `logprobs` -- REJECTED with error (not ignored)
- `top_logprobs` -- REJECTED with error

**Implication:** If we're running in thinking mode (which OpenClaw's `/reasoning on` enables), fine-tuning with temperature/top_p has zero effect. Only `reasoning_effort` matters.

### Reasoning Effort Mapping:
- `low` and `medium` both map to `high` (aliases only)
- `xhigh` maps to `max`
- Complex agent requests auto-escalate to `max`

## Temperature Guide (Non-Thinking Mode Only)

| Task | Temperature | Why |
|---|---|---|
| Coding / Math | 0.0 | Minimize variance |
| Data Cleaning / Analysis | 1.0 | Platform default |
| General Conversation | 1.3 | Natural variation |
| Translation | 1.3 | Fluency + consistency |
| Creative Writing / Poetry | 1.5 | Max stylistic variation |

**Key rule:** coding at 0.0 until you have a specific reason to raise it.

## Thinking Mode & Reasoning

### How it works:
- Enabled by default -- you don't manually activate it.
- Returns `reasoning_content` (CoT) separately from `content` (final answer).
- In streaming: `delta.reasoning_content` vs `delta.content`.
- CoT tokens are NOT visible to the user -- they're server-side only.
- BUT: CoT tokens count against `max_tokens` and your billing.

### Tool Calling in Thinking Mode:
- Model can call tools DURING CoT reasoning.
- Reasoning can span multiple tool-call rounds.
- The model "thinks" between tool results.
- `reasoning_effort` controls depth: higher = more tool-calling cycles possible.

### When to Use:
- **Always on for Pro:** reasoning is the primary value of Pro over Flash.
- **On for Flash:** when task complexity justifies it.
- **Off for Flash:** bulk processing, simple lookups, transcription.

## Prompt Engineering for DeepSeek

### Chain-of-Thought Prompting:
- DeepSeek models are trained for CoT. Give them room to reason.
- For complex tasks, explicitly say: "Think step by step before answering."
- Do NOT pre-fill the assistant response with reasoning -- let the model
  generate its own internal CoT via the thinking mode mechanism.

### JSON Mode Tips:
- Use `response_format: { type: "json_object" }`.
- Include the word "JSON" in the system prompt or user message.
- Specify the exact JSON schema in the prompt (DeepSeek honors it better
  with explicit schemas than with format-only hints).
- JSON mode + thinking mode work together -- CoT reasoning improves JSON
  structure quality.

### Tool Calling Best Practices:
- Define tools with clear, specific descriptions.
- DeepSeek can handle 50+ tool definitions but gets confused beyond ~30.
- Give tools unique, descriptive names -- avoid generic names like `search`
  when you have `web_search`, `memory_search`, `file_search`.
- For multi-step tool workflows, put the sequence expectation in the
  system prompt ("After calling tool X, wait for the result before
  calling tool Y").

### Rate Limits & Retries:
- Rate limits are NOT publicly documented. Assume standard DeepSeek API
  limits (~60 RPM for Pro tier).
- 429 responses: exponential backoff starting at 1s, max 60s.
- Token-bucket style: short bursts OK, sustained high throughput may
  throttle.

### Known Gotchas:
1. **Thinking mode ignores temperature** -- if you need creative output,
   turn thinking OFF first. You can't have both deterministic reasoning
   AND high-temperature creativity simultaneously.
2. **CoT consumes output budget** -- if you set `max_tokens=4096` and
   the model uses 3000 tokens for reasoning, you only get ~1000 tokens
   of visible output.
3. **Tool definitions inflate prompt** -- every tool definition counts
   against the 1M context. Keep tool schemas lean.
4. **Legacy aliases are a trap** -- `deepseek-chat` and `deepseek-reasoner`
   will break on July 24, 2026. Migrate all references before then.
5. **JSON mode + no "JSON" keyword = degraded output** -- always include
   the word "JSON" in your prompt when using JSON mode.

## Model Selection Heuristic

```
Is this a complex reasoning task?
  YES -> deepseek-v4-pro with reasoning_effort=high or max
  NO -> Is this high-throughput or cost-sensitive?
    YES -> deepseek-v4-flash without thinking mode
    NO -> deepseek-v4-pro (default)
```

For sub-agents spawned via sessions_spawn:
- Research/heavy analysis -> Pro
- File operations, simple lookups, formatting -> Flash

---

*Source: deepseekv4pro.com/guides, api-docs.deepseek.com. Last updated 2026-07-16.*
