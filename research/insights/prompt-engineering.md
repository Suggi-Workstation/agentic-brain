---
name: prompt-engineering
id: 20260717T003500Z
tier: insight
source:
  - 20260717T003600Z
author: Ava
tags: [prompt-engineering, llm, best-practices, system-prompt, agent-design]
links:
  - research/insights/openclaw-manual.md
  - research/insights/deepseekv4pro.md
---

# Prompt Engineering -- A Comprehensive Reference

## The Insight
Prompt engineering is the discipline of writing instructions that
reliably steer language models toward desired behavior. The best prompts
are clear, structured, example-backed, and tested -- not clever, long,
or ambiguous. The single most reliable technique across all model
families is: be explicit about what you want, show examples, and explain
why it matters.

## Evidence

This insight synthesizes the official documentation from OpenAI
(developers.openai.com), Anthropic (platform.claude.com), the community
prompt engineering guide (promptingguide.ai), and Lilian Weng's
comprehensive survey on in-context prompting.

### Source 1: Anthropic Prompt Engineering Guide (2026)

Anthropic's official guidance is built on the "brilliant new employee"
metaphor: treat the model as someone highly capable but lacking context
about your specific norms and workflows.

**Core principles:**
- **Be clear and direct** -- explicit instructions outperform implicit
  expectations. The golden rule: show your prompt to a colleague with
  minimal context. If they would be confused, the model will be too.
- **Add context** -- explaining WHY a rule matters (not just WHAT the
  rule is) helps the model generalize correctly. Example: "Your response
  will be read aloud by a TTS engine, so never use ellipses" outperforms
  "NEVER use ellipses."
- **Use examples (few-shot)** -- 3-5 well-crafted examples are the most
  reliable way to steer output format, tone, and structure. Examples
  must be relevant, diverse, and structured with XML tags.
- **Structure with XML tags** -- wrapping instructions, context,
  examples, and input in separate XML tags reduces misinterpretation.
  Consistent, descriptive tag names matter.
- **Give the model a role** -- even a single sentence of role-setting
  ("You are a helpful coding assistant specializing in Python") improves
  focus and tone.
- **Model-specific differences matter** -- Claude Sonnet 5 needs
  different prompting than Claude Opus 4.8. Never assume one prompt
  works across models.

### Source 2: OpenAI Prompt Engineering Guide (2026)

OpenAI's guidance emphasizes the chain of command: developer messages
are highest priority, followed by user messages. System/developer
messages set the rules; user messages provide the input.

**Core principles:**
- **Message hierarchy** -- put high-level behavior, tone, goals, and
  examples in the system/developer message. User messages carry the
  specific task.
- **Store prompts in code** -- not as reusable prompt objects (OpenAI
  is deprecating prompt objects). Code-managed prompts enable typed
  inputs, code review, tests, and normal deployment processes.
- **Pin to model snapshots** -- production applications should pin to
  specific model versions to ensure consistent behavior across updates.
- **Build evaluation suites** -- measure prompt behavior before and
  after model upgrades. Treat prompts like code: version, test, review.
- **Structure with XML or Markdown** -- use headers, lists, and XML
  tags to create clear logical boundaries between prompt sections.
  Recommended order: Identity, Instructions, Context, Examples, Output
  Format.
- **Reasoning models need different prompting** -- reasoning models
  (o-series, etc.) benefit from less prescriptive instructions since
  they generate internal chain-of-thought. GPT models need more
  explicit step-by-step guidance.

### Source 3: Lilian Weng's Prompt Engineering Survey (2023, updated)

A systematic survey covering zero-shot, few-shot, chain-of-thought,
and advanced techniques. Key findings:

- **Zero-shot vs few-shot** -- few-shot dramatically outperforms
  zero-shot across most tasks, but costs more tokens and may hit
  context limits.
- **Example selection is critical** -- the choice of few-shot examples
  produces variance from "near random guess to near state-of-the-art."
  Use k-NN clustering in embedding space to select semantically
  similar examples.
- **Avoid biases** -- majority label bias (unbalanced example labels),
  recency bias (model repeats last label), and common token bias (model
  favors frequent tokens). Calibrate by normalizing probabilities.
- **Prompt engineering is empirical** -- results vary significantly
  across models. Systematic experimentation and benchmarking are
  required; there is no universal optimal prompt.

### Source 4: Community Guide (promptingguide.ai)

The community consensus aligns with the official providers:
- Prompt engineering encompasses not just writing prompts but also
  tool integration, safety considerations, and domain knowledge
  augmentation.
- Advanced techniques: chain-of-thought (CoT), self-consistency,
  generated knowledge prompting, tree-of-thought, ReAct (reasoning
  + acting), automatic prompt engineering (APE).
- The best technique depends on the task type: reasoning tasks benefit
  from CoT; factual tasks benefit from few-shot; creative tasks
  benefit from role-setting and examples.

## Implications

### For Our Agent Architecture

1. **Our SOUL.md and AGENTS.md ARE the system/developer message.**
   OpenClaw injects these files into every session prompt as the
   high-priority instruction layer. This aligns perfectly with both
   OpenAI's and Anthropic's guidance: personality, tone, boundaries,
   and operating rules belong in the highest-priority layer.

2. **The Feynman Loop is a chain-of-thought technique.** "Blank page
   first, then search, then synthesize" is exactly what CoT prompting
   achieves: structured reasoning before output. Our implementation
   is more durable than ad-hoc CoT because it is encoded in bootstrap
   files, not in per-task prompts.

3. **Our quality gates (G1-G8) are the evaluation suite.** OpenAI
   recommends building tests that measure prompt behavior. Our
   numbered quality gates serve exactly this function: each IOR must
   pass 8 falsifiable checks before publishing. The system tests itself.

4. **Templates are few-shot examples encoded as rules.** Each
   governance template includes a complete, valid example. This
   combines Anthropic's "3-5 examples" principle with the structural
   enforcement of a schema. A template without an example is a prompt
   without shots.

### What We Are Doing Right
- SOUL.md places identity + tone + boundaries in the system message
  (highest priority per both Anthropic and OpenAI)
- AGENTS.md provides sequential, numbered instructions (Anthropic's
  recommendation for task order)
- Templates include concrete examples (few-shot learning applied to
  document creation)
- Quality gates are falsifiable (evaluation suite)
- The Feynman Loop encodes structured reasoning (CoT made structural)

### What We Could Improve
- Our prompts could benefit from more **explicit "why" context**
  (Anthropic's recommendation). Some gate rules state the rule but
  not the failure that birthed it. Each rule should justify its own
  existence.
- **Model-specific prompting differences** -- DeepSeek V4 Pro (our
  runtime) has different prompting characteristics than Claude
  (Link's runtime). Our templates and core files assume a single
  prompting style. A future improvement: add model-specific sections
  where they diverge.
- **Prompt versioning** -- OpenAI recommends pinning to model
  snapshots. Our core files and templates are versioned (frontmatter
  `version:` field) but we do not track which model version they
  were optimized for. This gap will surface when we upgrade models.

## Counter-evidence
This insight would be invalidated if:
- A simpler prompt (no examples, minimal structure) consistently
  outperforms a structured prompt on our specific tasks. This has
  not been observed -- every quality improvement in our system
  (Feynman Loop, quality gates, templates) traces to adding
  structure, not removing it.
- A model emerges that reliably infers intent from minimal
  instructions (no examples, no structure, no role). Current
  models (DeepSeek V4, Claude, GPT) all benefit from explicit
  structure; the trend is toward better instruction-following,
  not better mind-reading.

## Version History
| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-17 | ava | Initial insight from Anthropic, OpenAI, promptingguide.ai, and Lilian Weng research. |

## Cross-Links
- `research/insights/openclaw-manual.md` -- our operating platform
- `research/insights/deepseekv4pro.md` -- our model's specific behavior
- `governance/template-reflections.md` -- prompt engineering applied to
  IOR document creation
- `2026-06-13_ava_quality-loops-feynman-schon.md` -- Feynman Loop as
  structured chain-of-thought
