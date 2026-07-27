---
name: prompt-engineering-for-agents
id: 20260727T101558Z
tier: library-topic
domain: coding-agentic-ai
author: Researcher-1
tags: [prompt-engineering, agent-design, progressive-disclosure, instruction-hierarchy, system-prompts, context-engineering]
links: [library/coding-agentic-ai/context-window-management.md, library/coding-agentic-ai/agent-skill-systems.md, library/coding-agentic-ai/multi-agent-orchestration.md]
---

# Prompt Engineering for Agents -- Why Writing Instructions That Survive a Thousand Tool Calls Is the Central Unsolved Challenge of Agent Engineering

Prompt engineering for AI agents is a fundamentally different discipline
from prompt engineering for chatbots. Where a chatbot prompt runs once
and produces text, an agent prompt must guide behavior across dozens or
hundreds of tool-calling loops -- persisting through accumulating
context, surviving tool failures and error states, and producing
consistent behavior even when the agent encounters situations the prompt
author never anticipated. The field has converged on a set of core
patterns -- progressive disclosure, instruction hierarchy, conditional
system prompt assembly, and structured output enforcement -- that
collectively represent the shift from prompt engineering to context
engineering, where the central question is not "what words to use" but
"what configuration of context maximizes the likelihood of desired
behavior across an entire agent session."

## Background

The history of prompt engineering for agents tracks the evolution of
LLM applications from single-turn chatbots to multi-turn autonomous
systems. In the GPT-3 era (2020-2021), prompt engineering meant crafting
a single message to elicit a desired completion -- classification
labels, text generation, or simple Q&A. The prompt was consumed once,
the model responded, and the interaction ended.

The release of ChatGPT (November 2022) introduced multi-turn
conversation, but the pattern remained fundamentally chatbot-oriented:
each user message triggered one model response, with conversation
history appended as context. System prompts emerged as a way to set
persistent behavioral framing -- "You are a helpful assistant" -- but
the engineering challenge was still about single-turn output quality.

The agent era began in earnest with the widespread availability of
function-calling APIs (OpenAI, June 2023) and the rise of agent
frameworks like LangChain, AutoGPT, and later Claude Code, Cursor, and
Devin. Suddenly, prompts had to survive not one turn but dozens or
hundreds. A single ambiguity in the system prompt, harmless at turn 1,
could compound into dangerous behavior by turn 47 after the agent had
accumulated context from 12 tool calls, 3 error states, and multiple
sources of external data.

By 2025, Anthropic formally articulated the shift from prompt
engineering to context engineering -- the recognition that the
engineering problem was no longer about finding the right words but
about curating the optimal set of tokens across the entire context
state: system instructions, tool definitions, retrieved documents,
conversation history, and dynamically loaded skills. As Anthropic's
engineering team wrote in September 2025: "Building with language
models is becoming less about finding the right words and phrases for
your prompts, and more about answering the broader question of what
configuration of context is most likely to generate our model's desired
behavior."

Claude Code's system prompt exemplifies this evolution: it is not a
monolithic document but over 110 separate instruction strings totaling
16,000-25,000 tokens, conditionally assembled at runtime based on
active tools, current mode, project configuration, and skill
invocations. This represents the state of the art: system prompts as
software, not prose.

## Core Concepts

### The Five-Layer System Prompt Anatomy

Production agent systems have converged on a common five-layer
structure for system prompts. This architecture appears across Claude
Code, Cursor, Devin, and other major agents, suggesting it captures
fundamental requirements rather than implementation accidents.

**Layer 1: Identity framing** (~100 tokens). The agent's role, builder,
and capability scope. "You are X, built by Y." This layer sets the
agent's self-model and determines what kinds of tasks it considers
within its remit. An agent that believes it is a "helpful coding
assistant" will behave differently from one that believes it is "an
autonomous software engineer responsible for end-to-end feature
delivery."

**Layer 2: Behavioral rules.** The operational constitution --
task execution principles, reversibility guidelines ("prefer
non-destructive actions"), tone requirements, and output format
expectations. This is where the agent learns its constraints: what it
must do, should do, and must never do. The distinction between
mandatory rules (MUST, NEVER) and guidelines (should, prefer) is
critical. Overly prescriptive rules create fragility when the agent
encounters edge cases the author did not anticipate. Overly loose
guidelines produce unpredictable behavior.

**Layer 3: Typed tool APIs.** Beyond JSON schemas, production agents
include explicit per-tool instruction sections: how to use each tool,
when to prefer one over another, what side effects to expect, and
what errors mean. Vague tool descriptions are the primary driver of
tool selection errors. Tool definitions must be self-contained,
robust to error, and extremely clear about intended use. If a human
engineer cannot definitively say which tool to use in a given
situation, an AI agent cannot be expected to do better.

**Layer 4: Safety layers.** Embedded as operational rules woven
throughout the prompt rather than collected in a separate block.
Security is architectural, not appended. Safety-critical instructions
(git operations, destructive actions, data deletion) receive
especially precise treatment with explicit confirmation requirements.

**Layer 5: Conditional sections.** Mode-specific instructions (plan
mode, auto mode, minimal mode) assembled dynamically at runtime. This
is where progressive disclosure operates -- rather than loading all
instructions for all modes at initialization, the agent receives only
the instructions relevant to its current operating context.

### Progressive Disclosure: Load Only What You Need

Progressive disclosure is the dominant pattern for scaling agent
capability without proportionally scaling context bloat. The core
insight is simple: an agent performing a Meeting Scheduling task needs
calendar APIs and timezone rules; that same agent performing an
Invoice Processing task needs accounting logic and payment terms. Yet
most naive implementations load both sets of instructions into every
query, consuming context window budget before the user types a single
character.

The principle generalizes beyond skills to all context: tools,
instructions, examples, behavioral rules. At any given moment, the
agent's context should contain only the information needed for the
current decision, plus enough framing to know where to find more.

Four implementation patterns have emerged, ordered by increasing
sophistication:

**Pattern 1: Index-first loading.** The agent receives a compact index
of available capabilities (skill names with one-line descriptions) at
initialization. When it determines a specific capability is needed, it
fetches the full instructions. This reduces baseline context by 60-80%
for agents with many capabilities, and the per-query cost savings
compound significantly for high-volume agents.

**Pattern 2: Conditional system prompt construction.** Rather than a
static prompt string, the system prompt is a function that evaluates
the current query context -- user input, session state, previous tool
results -- and returns only the relevant instruction blocks. Pydantic
AI 2.0 implements this directly: the system prompt is a Python
function decorated with @agent.system_prompt that receives a
RunContext and returns a context-dependent prompt string. This means
prompt logic becomes code that can be tested, versioned, and extended
incrementally.

**Pattern 3: Dynamic retrieval of instructions.** Instructions are
stored in a searchable store (vector database or structured index),
and the agent retrieves the top 2-3 most relevant instruction chunks
at query time. This scales to hundreds of instruction variants without
any increase in per-query context size. It is particularly effective
for knowledge-heavy agents, large instruction libraries, or frequently
updated documentation.

**Pattern 4: Specialized sub-agents (multi-agent architecture).** The
highest-fidelity implementation: each workflow gets its own dedicated
agent with its own focused system prompt and tool set. An orchestrator
agent routes queries to the appropriate specialist. This is
progressive disclosure at the architectural level -- each agent sees
only its own narrow context, and the orchestrator's prompt describes
routing heuristics rather than domain logic.

### Instruction Hierarchy: System Over User Over Tools

Without explicit hierarchy, LLMs treat all inputs equally -- enabling
injection through any channel. A user message can override system
instructions; tool output from an untrusted web search can redirect
agent behavior. Instruction hierarchy addresses this by training
models to respect a priority ordering:

- Priority 0: System messages (application developer)
- Priority 10: User messages (end user)
- Priority 30: Tool output (web results, API responses, third-party content)

OpenAI trained this hierarchy into GPT-3.5 Turbo using two techniques:
Context Synthesis (training aligned responses to hierarchical inputs)
and Context Ignorance (teaching the model to answer "as if it never
saw" conflicting lower-priority instructions). The results were
substantial: +63% defense against system prompt extraction, +30%
jailbreak robustness, and generalization to unseen attack types.

However, instruction hierarchy trained into the model is necessary but
not sufficient. RL-based attacks (RL-Hammer) achieved approximately
98% success against GPT-4o's instruction hierarchy defenses.
Production systems layer runtime defenses on top: XML/delimiter
separation between instruction blocks and user data, input filtering
for known injection patterns, LLM guardrails (AWS Bedrock Guardrails,
Azure AI Content Safety), and structured queries that treat user input
as data structures rather than natural language.

### The Specificity-Flexibility Tension

Every agent prompt author faces a fundamental tension. Highly specific
instructions ("always format dates as YYYY-MM-DD") produce reliable
behavior but break when the agent encounters valid edge cases the
author did not anticipate. Flexible instructions ("format dates
appropriately for context") give the agent room to exercise judgment
but produce inconsistent behavior across sessions.

The field's resolution, visible in the evolution of Claude Code's
system prompt, is to use strong specificity for safety boundaries and
structural constraints, and looser heuristics for operational
decisions. Claude Code 2.0 (September 2025) shifted from "MUST" to
"should," from "NEVER" to "NEVER... unless explicitly instructed," and
removed entire code-convention blocks that the model had absorbed
through RLHF training. The exception was safety-critical instructions
(git operations, destructive actions), which got tighter, not looser.

The meta-principle is: as model capability increases, reduce prompt
verbosity. Find the smallest set of high-signal tokens that maximize
the likelihood of the desired outcome. The optimal system prompt
shrinks as the model improves -- but safety constraints should tighten,
not loosen.

### Prompt-Drift Across Long Sessions

A unique challenge of agent prompts is prompt-drift: the phenomenon
where the system prompt's influence weakens as the conversation
lengthens and accumulated context crowds it out. Early instructions
get buried under pages of tool output, conversation history, and
retrieved data. The agent does not forget its system prompt -- the
tokens are still in context -- but its effective attention to those
tokens degrades, a phenomenon related to the "lost in the middle"
effect documented in LLM attention research.

Mitigations include periodic goal re-injection (re-stating the
original task and constraints at checkpoints), bounded iteration loops
that reset context after major phases, and the "constitutional
document" pattern where core behavioral rules are kept compact and
re-injected as system-reminder blocks at regular intervals.

## Evidence and Research Foundation

The empirical case for agent-specific prompt engineering rests on
three pillars: production system analysis, academic research on
instruction hierarchy, and the documented failure modes of naive
approaches.

**Production system analysis.** Zylos Research (March 2026) conducted
a comprehensive analysis of system prompts across Claude Code, Cursor,
Devin, and Codex, finding convergence on the five-layer anatomy
described above. Claude Code's 110+ instruction strings represent the
most sophisticated known implementation, with conditional assembly
producing 16,000-25,000 tokens of context per query. The analysis
found that 31 tools add approximately 4,500 tokens per query in tool
descriptions alone, making tool description quality the highest-leverage
prompt engineering surface -- more impactful than pages of behavioral
instructions.

**Multi-turn degradation.** The same analysis documented that even
90%+ single-turn accuracy degrades to 10-15% success across full
multi-step conversations when prompts are not designed for persistence.
This is the central unsolved challenge: making prompts that survive
not one call but the full agent lifecycle. Bounded iteration loops,
verifiable checkpoints (tests), sub-agent isolation, and periodic goal
re-injection are the engineering patterns that address this, not
better prompt wording.

**Instruction hierarchy research.** OpenAI's instruction hierarchy
paper (arXiv:2404.13208, April 2024) demonstrated that models trained
with hierarchical privilege ordering achieved +63% defense against
prompt extraction and +30% jailbreak robustness, with generalization
to unseen attack types. However, subsequent RL-based attacks (RL-Hammer)
achieved approximately 98% bypass rates against these defenses,
establishing that training-level hierarchy is necessary but
insufficient. Prompt injection remains OWASP LLM Top 10 #1 as of 2025.

**Context rot and attention degradation.** Research on the "needle in
a haystack" problem demonstrated that as context length increases,
model recall accuracy for specific information decreases -- a
phenomenon the Chroma research team labeled "context rot." This
finding directly motivates progressive disclosure: every irrelevant
token in context not only wastes budget but actively degrades the
model's ability to attend to the relevant tokens. Models may have 128K
or 1M token windows, but effective attention is a scarcer resource
than context capacity.

**Anthropic's context engineering framework.** In September 2025,
Anthropic published "Effective Context Engineering for AI Agents,"
articulating the shift from prompt engineering to context engineering.
Their guidance emphasizes treating context as a finite resource with
diminishing marginal returns, curating the smallest set of
high-signal tokens, and the "just in time" pattern of loading context
at runtime rather than pre-loading all potentially relevant
information. The document established that the n-squared nature of
transformer attention creates a natural tension between context size
and attention focus, making context curation an engineering necessity
rather than an optimization.

## Implications

**For agent builders: invest in prompt architecture, not prompt prose.**
The highest-leverage engineering decision is how you structure and
assemble your system prompt, not which words you choose. Treat the
system prompt as conditionally assembled software: version-controlled,
tested, and gradually rolled out. Start with a minimal prompt and the
best available model; add instructions only in response to documented
failure modes.

**Tool descriptions are the most underinvested prompt surface.** Vague
tool descriptions are the primary driver of tool selection errors. A
well-written tool description -- specifying not just what the tool does
but when to prefer it over alternatives, what errors mean, and what
side effects to expect -- prevents more failures than pages of
behavioral instructions. Invest engineering time in tool descriptions
proportional to their impact on agent accuracy.

**Progressive disclosure is not optional at scale.** An agent with 10
capabilities can get away with loading everything. An agent with 100
capabilities cannot. Progressive disclosure is the architectural
pattern that decouples capability count from context size, and it must
be designed into the system from the start. The choice of
implementation pattern (index-first, conditional construction, dynamic
retrieval, or sub-agents) depends on complexity requirements, but the
principle of loading only what is needed when it is needed applies
universally.

**Instruction hierarchy requires defense in depth.** Training-level
hierarchy is a baseline, not a solution. Production agents need
layered defenses: delimiter-based separation, input filtering, output
validation, structured query interfaces, and guardrail models. The
adversarial nature of prompt injection means static defenses are
insufficient -- the arms race continues.

**The specificity-flexibility calibration evolves with model
capability.** As models improve, prompts should become shorter and
less prescriptive for operational behavior, but tighter for safety
boundaries. The Claude Code 2.0 migration from "MUST" to "should" for
operational rules, while strengthening safety constraints, represents
the direction of travel. The principle: let the model's training
handle conventions; use the prompt only for what training cannot
provide.

**Context engineering subsumes prompt engineering.** The field is
moving from "how do I write a good prompt?" to "how do I curate the
optimal context state across an entire agent session?" This is a
broader, harder problem that encompasses prompt writing but also
includes tool design, memory architecture, retrieval strategy, and
session management. Teams that continue to treat prompt engineering as
a text-crafting exercise will be outpaced by teams that treat it as a
systems engineering discipline. The engineers who win will be those
who think in terms of context architectures, not prompt paragraphs.

## Sources

1. Anthropic Engineering. (2025). "Effective Context Engineering for
   AI Agents." https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
   [high]

2. Zylos Research. (2026). "Prompt Engineering for AI Agent Systems:
   System Prompts, Tool Descriptions, and Instruction Hierarchies."
   https://zylos.ai/research/2026-03-30-prompt-engineering-ai-agent-systems-instruction-hierarchies/
   [high]

3. OpenAI. (2024). "The Instruction Hierarchy: Training LLMs to
   Prioritize Privileged Instructions." arXiv:2404.13208.
   https://arxiv.org/abs/2404.13208 [high]

4. Paxrel. (2026). "AI Agent Prompt Engineering: 10 Patterns That
   Actually Work." https://paxrel.com/blog-ai-agent-prompts [medium]

5. MindStudio. (2026). "How to Use Progressive Disclosure in AI Agent
   Design to Scale Capabilities."
   https://www.mindstudio.ai/blog/progressive-disclosure-ai-agent-design-scale-capabilities
   [medium]

6. Ardalis, Steve Smith. (2026). "Optimizing AI Agents with Progressive
   Disclosure." https://ardalis.com/optimizing-ai-agents-with-progressive-disclosure/
   [medium]

7. Chroma Research. (2024). "Context Rot: How Context Length Affects
   Model Recall." https://research.trychroma.com/context-rot [medium]

## See Also

- `library/coding-agentic-ai/context-window-management.md` -- the
  context window is the resource that prompt engineering optimizes;
  understanding its constraints is prerequisite knowledge.
- `library/coding-agentic-ai/agent-skill-systems.md` -- skills are
  the primary consumer of progressive disclosure: loaded on demand,
  kept out of context until needed.
- `library/coding-agentic-ai/multi-agent-orchestration.md` -- the
  orchestrator pattern is progressive disclosure at the architectural
  level, with each sub-agent receiving only its domain-specific prompt.
