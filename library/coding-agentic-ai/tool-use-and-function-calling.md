---
name: tool-use-and-function-calling
id: 20260827T193157Z
tier: library-topic
domain: coding-agentic-ai
author: Library Runner
tags: [tool-use, function-calling, agent-architecture, tool-selection, json-schema, error-handling, react]
links: [library/coding-agentic-ai/anchor-coding-agentic-ai.md, library/coding-agentic-ai/agent-skill-systems.md, library/coding-agentic-ai/multi-agent-orchestration.md]
---

# Tool Use and Function Calling: How Agents Invoke External Capabilities

Tool use is the mechanism that turns a language model from a text
generator into an agent: instead of producing only words, the model
emits a structured request -- a function name and JSON arguments --
that application code executes against external systems, and the
execution result is fed back into the model's context for the next
turn. The model never executes anything itself; it proposes calls,
and the application decides what runs, with what permissions, and
with what validation. This request-decide-execute-synthesize loop,
introduced commercially by OpenAI's function calling in 2023 and
refined through Anthropic's tool use and the Model Context Protocol
(MCP), is the bridge between reasoning and action -- and engineering
that bridge well (schema design, tool selection, error recovery,
parallel execution) is what separates production agents from demos.

## Background

Tool use grew out of a specific failure: chain-of-thought prompting
taught models to reason in steps, but reasoning is inert. A model
that thinks step by step about the weather in Tokyo is still
guessing from training data; it cannot look anything up. The field
needed a way for models to reach beyond their weights and touch the
world -- databases, APIs, code execution, search. That need produced
a lineage of systems that progressively merged reasoning with
acting.

The decisive paper was ReAct (Yao et al., ICLR 2023), which prompted
a frozen PaLM-540B model to interleave free-form reasoning traces
with task-specific actions such as searching a Wikipedia API, and to
read the observations those actions returned. The insight was that
the two capabilities reinforce each other: reasoning traces help the
model plan and track actions ("reason to act"), while observations
from actions ground and correct the reasoning ("act to reason"). On
question answering (HotPotQA) and fact verification (Fever), ReAct
reduced hallucination and error propagation relative to
chain-of-thought alone, and on the interactive decision-making
benchmarks ALFWorld and WebShop it beat imitation- and
reinforcement-learning methods trained on thousands of task
instances -- with only one or two in-context examples. ReAct became
the canonical template for the modern agent loop, and Anthropic's
later guidance formalized it plainly: an agent is typically just an
LLM using tools in a loop based on environmental feedback.

In parallel, researchers attacked the reliability problem. Gorilla
(Patil et al., 2023) observed that even GPT-4 struggles to write
accurate API calls at scale: models hallucinate plausible-sounding
but nonexistent arguments. Gorilla fine-tuned a LLaMA-7B model with
Retriever-Aware Training over APIBench, a corpus of HuggingFace,
TorchHub, and TensorHub APIs, and combined it with a document
retriever so the model called tools against retrieved documentation
rather than memorized signatures. The retrieval-augmented variant
outperformed GPT-4 on API-call accuracy while substantially reducing
argument hallucination. Toolformer (Schick et al., 2023) came at the
same problem from the training side, teaching a model during
pretraining to call a small set of APIs -- a calculator, a search
engine, a translator -- by learning when to emit special API tokens
from self-supervised examples.

Commercial APIs then productized the loop. OpenAI shipped function
calling in June 2023: developers declare tools as JSON Schema
objects, the model returns a tool_calls object with a function name
and stringified arguments, the application executes, and the result
returns as a tool message. Anthropic's Claude followed with a
tool_use content block; Google's Gemini adopted a compatible
OpenAPI-based dialect. Provider differences are real -- Gemini
expects uppercase type values such as OBJECT and STRING, and rejects
external $ref references, while OpenAI's strict mode and parallel
calls are tools-only features -- but the core shape (name,
description, parameters with per-property descriptions, required,
enum) is portable across all three, so one schema body can be
adapted to any provider envelope. Parallel tool calling arrived with
OpenAI's tools array in late 2023, letting one assistant message
carry multiple independent calls.

The standardization push came from Anthropic's Model Context
Protocol (MCP, November 2024), an open protocol that defines how
applications provide tools and context to models, decoupling tool
servers from any single vendor. On the measurement side, the
Berkeley Function Calling Leaderboard (BFCL) became the de facto
standard for evaluating function calling, evolving through four
versions from single-turn AST-evaluated calls to multi-turn,
multi-step, stateful agentic evaluation. The field's center of
gravity had shifted: tool use was no longer a model capability to
demonstrate but an engineering discipline to practice.

The lineage before ReAct shows what interleaving added. WebGPT
(Nakano et al., 2021) gave a language model a text browser so it
could search, scroll, and cite sources, but relied on expensive
human-feedback reinforcement rather than explicit reasoning, and
task-oriented dialogue systems such as BlenderBot and Sparrow made
API-call decisions in conversation without reasoning traces. ReAct
showed that the thinking and the acting reinforce each other, and
every production agent since has inherited its loop shape.

The framework layer then absorbed the pattern. LangChain and
similar libraries wrapped tool definition, execution, and agent
loops behind reusable abstractions, and MCP standardized the
connection between tool servers and clients so a single tool
implementation can serve many agents across vendors. Anthropic
drew the field's key architectural distinction: workflows
orchestrate LLMs and tools through predefined code paths, while
agents let the LLM direct its own tool usage dynamically -- the
same loop, differing only in who decides the next step. That
distinction frames tool use as a spectrum from deterministic
orchestration to open-ended autonomy, and it explains why the
engineering discipline described here applies to both.

## Core Concepts

### The Tool-Calling Loop

Every tool-using agent runs the same four-phase cycle. Request: the
application sends the user message plus the tool schemas. Decide: the
model either answers directly or returns one or more tool calls --
OpenAI as a tool_calls array, Anthropic as tool_use blocks -- each
with a name and arguments. Execute: the application's code validates
the arguments, runs the function, and produces a tool result.
Synthesize: the result returns to the model as a tool message, and
the loop continues until the model emits a final text answer. The
model never touches API keys, databases, or the filesystem; the
separation is both a security property (the application controls
permissions, sandboxing, and validation) and an engineering pattern
(execution logic stays in deterministic code). ReAct's formulation
shows why this loop works: interleaving reasoning traces with
environmental feedback lets the model plan with, and learn from,
real observations instead of internal speculation.

### The Schema as the Interface Contract

A tool's JSON Schema is the entire interface between a language
model and your code. The model reads the whole schema, not just the
parameter names: the root description tells it when to call the
tool, each property description tells it what to put there, enum
values constrain choices, and required marks what cannot be
omitted. Anthropic calls this the agent-computer interface (ACI) and
treats tool documentation and testing as the discipline's third core
principle, alongside simplicity and transparency -- because the
schema is the only documentation the model has. Provider dialects
differ at the edges (Gemini's uppercase OpenAPI types, its
nullable: true convention, no external $ref), but the intersection
is large enough that a single schema body designed to the OpenAI
strict subset works across OpenAI, Anthropic, and Gemini.

### Tool Selection at Scale

Selection accuracy degrades as the tool catalog grows: with dozens or
hundreds of tools, the model must disambiguate similar names and
purposes before it ever formats an argument. Gorilla showed the
hard part is not syntax but relevance ranking -- trained models
conflate similar APIs and hallucinate parameters -- and that
retrieving the relevant documentation first improves accuracy more
than scaling model size. Production systems extend this with
hierarchical selection: the AutoTool framework (2025) exploits "tool
usage inertia", the tendency of invocations to follow predictable
sequential patterns, by routing through a graph of tool clusters so
only a small candidate set ever reaches the prompt. OpenAI's
tool_search lets applications defer rarely used tools and load them
on demand. Anthropic's guidance adds namespacing: grouping tools
under prefixes (asana_search, jira_search) or suffixes measurably
changes selection quality, and the right scheme varies by model --
so the naming scheme is itself an evaluation target, not a
convention.

### Parallel Versus Sequential Invocation

When a response needs several independent results, parallel calls
collapse latency from the sum of tool latencies to the slowest
single call: five 200 ms calls take 1,000 ms sequentially and about
200 ms in parallel. OpenAI enables parallel tool calls by default --
the model signals its intent to invoke multiple tools in one
assistant message, and the application decides whether to execute
concurrently. Anthropic's agent patterns distinguish sectioning
(splitting a task into independent parallel subtasks) from voting
(running the same task several times for a consensus answer, trading
cost for reliability). Parallelism should be disabled only when
calls are dependent -- when the second call needs the first call's
output as input.

### Argument Hallucination and Validation

The canonical failure mode is a plausible argument that does not
exist: a parameter name that sounds right but is not in the schema,
an enum value slightly off, a unit in the wrong convention. Gorilla
measured this precisely by parsing generated calls into Abstract
Syntax Trees and checking every function and argument against the
ground truth, establishing AST evaluation as the field's standard
approach -- later adopted by BFCL across Python, Java, JavaScript,
and REST. Because the model can always produce invalid inputs,
validation is mandatory before execution, and schema design
mitigates the problem upstream: enums instead of free-form strings,
narrow types, and descriptions written as documentation rather than
labels.

### Error Handling and Recovery

Tool failures are heterogeneous, and each class needs a different
recovery strategy. Transient errors (rate limits, timeouts, network
blips) deserve bounded retries with exponential backoff; the same
request will often succeed seconds later. Validation errors indicate
a schema or description problem and are best handled by re-prompting
the model with the error message as context, or tightening the
schema -- a tool with a 15% validation error rate has an interface
problem, not a model problem. Semantic errors (wrong tool, wrong
task decomposition) need correction at the reasoning level.
Permission violations and unrecoverable states should escalate to a
human operator with a meaningful message rather than loop silently.
Idempotency protects against double execution of side-effecting
tools when retries replay. The ToolRL-DR line of work (2026) shows
that training on perturbed tool inputs -- noisy registries, timeouts,
duplicate names -- induces a persistent retry policy that transfers
to unseen runtime failures, evidence that robustness itself can be
trained.

### Tool Design Ergonomics

Anthropic's engineering reports make the counterintuitive point that
tool design matters more than agent architecture: for SWE-bench
style work they spent more time on tool interfaces than on prompts,
and their guidance is to keep the agent loop simple and put the
sophistication into the tools. Effective tools are intentionally and
clearly defined, use agent context judiciously, combine into diverse
workflows, and give useful error messages -- the error string is
feedback the model will read and act on. This inverts a software
engineering habit: tools written for agents are documented for a
non-deterministic reader that sees only the schema, not for another
developer.

### Evaluating Tool Use

BFCL established the measurement framework: AST-based checking of
function and argument correctness, coverage of serial, parallel,
and multiple function calls, relevance detection (does the model
abstain from calling when no tool fits?), and from V3 onward
stateful multi-turn, multi-step evaluation with service states. The
field's open questions are documented in the same work: while
state-of-the-art models excel at single-turn calls, memory, dynamic
decision-making, and long-horizon reasoning over tools remain
unsolved. Recent benchmark critique (AgentProp-Bench, 2026) warns
that substring-based automated judges agree with human annotation
only at chance level, and that a bad parameter propagates into a
wrong final answer with probability 0.46 to 0.73 depending on the
model -- tool-use evaluation itself needs re-validation before its
scores can drive design decisions.

### Multi-Turn Tool Use and State

Single calls are the easy case. Real workflows chain them: the
result of one call becomes the argument of the next, and BFCL V3
evaluates models precisely on this -- multi-turn, multi-step
function calling where the model must track service state across
sequential invocations. State leaks into everything: if the agent
re-issues an identical call it already answered, that is a memory
failure surfacing as a tool-usage pattern, which is why production
observability treats redundant-call detection as a first-class
signal. Tool results also compete for the context window, so the
decision of what to return -- full payload, summary, or error only
-- is a context-management decision made at the tool boundary.

### The Model Context Protocol and Tool Distribution

MCP (Anthropic, November 2024) splits tool provision from tool
consumption: servers expose tools with schemas and descriptions,
and clients discover and invoke them through a standard protocol.
The practical consequence is scale -- agents routinely face dozens
of servers and hundreds of tools, many written by other
developers -- which is exactly the regime where selection quality
and naming discipline dominate correctness. Anthropic's
namespacing advice (group by service and resource, and evaluate
which naming scheme your models select best) is a direct response
to MCP-scale catalogs.

### Security at the Execution Boundary

Because the application executes every call, the boundary is where
safety is enforced: permission scopes, allowlists, sandboxed code
execution, argument validation, and audit logging all live there.
Tool results must be treated as untrusted input to the model,
since a compromised or malformed result is a prompt-injection
vector -- the same discipline the domain's sandboxing and security
thread applies to every agent capability. The Gorilla ecosystem's
GoEx component formalizes this as safe execution of LLM-generated
actions.

## Evidence

The empirical case for tool use rests on three layers: task
performance, reliability measurement, and production engineering.

ReAct (Yao et al., 2023) provided the first layer. On HotPotQA and
Fever, a PaLM-540B prompted with interleaved reasoning and Wikipedia
API calls outperformed action-only variants and beat chain-of-thought
on factual grounding, since external observations corrected the
model's internal guesses. On ALFWorld, one- and two-shot ReAct
achieved 71% success against 37% for the best baseline -- an
absolute improvement of 34 percentage points over methods trained on
thousands of task instances; on WebShop the improvement was 10
percentage points. The ablations isolated the mechanism: acting
without reasoning and reasoning without acting both underperformed
the combination, and reasoning traces also made trajectories
human-interpretable.

Gorilla and BFCL (Patil et al.) supplied the reliability layer. On
APIBench, the retrieval-augmented Gorilla model surpassed GPT-4,
Claude, and open-source baselines on API functionality accuracy and
reduced hallucinated arguments, with the paper's accuracy-versus-
hallucination analysis showing retrieval (BM25 or GPT-based, up to
oracle-level) systematically beats zero-shot prompting -- evidence
that grounding in retrieved documentation, not raw model scale, is
what drives correct calls. BFCL's cross-model results sharpened the
picture: state-of-the-art models handle simple single-turn calls
well, but accuracy drops on parallel calls, relevance detection,
and multi-turn stateful workflows, which the authors frame as open
challenges for agentic applications.

Production and robustness studies form the third layer. Anthropic's
reported experience (Building Effective Agents; Writing Effective
Tools for Agents) documents that teams succeed by starting with
simple augmented-LLM patterns and adding orchestration only when
evaluation shows it helps, and that tool interface quality --
namespacing, descriptions, error messages -- moves measured
agent performance; notably, prefix- versus suffix-based namespacing
had non-trivial, model-dependent effects on their tool-use
evaluations. The ToolRL-DR benchmark (2026) measured robustness
under realistic deployment perturbations and found an uneven
profile: observation-level perturbations reduced accuracy by less
than 5%, but reward-relevant and transition perturbations (typos
propagating into hallucinated tool names, misconfigured timeouts
stalling the agent, duplicate tool names freezing SDKs) cut
accuracy by roughly 40% and 30% respectively across models from 5B
to 32B parameters including o4-mini -- scale alone does not close
the gap. Training a 3B model with domain-randomized tool-use
trajectories retained about three-quarters of clean accuracy and
matched 14B open-source function-calling baselines on perturbed
inputs. On evaluation reliability, AgentProp-Bench (2026) found
substring judging at chance agreement with human labels, a
three-LLM judge ensemble only moderate with a conservative bias,
and a tuned runtime interceptor reducing hallucination on
GPT-4o-mini by 23% -- measurement, not just capability, is the
bottleneck. On latency, the parallel-calling arithmetic is
straightforward and consistent across practitioner reports: five
independent 200 ms calls serialize to 1,000 ms and parallelize to
roughly 200 ms, a 5x wall-clock reduction that compounds across
multi-step workflows making 3-10 calls per step.

The synthesis across all three layers: tool use delivers large,
replicated performance gains when the loop is grounded in feedback
and documentation, but the failure modes are structural -- argument
hallucination, selection errors in large catalogs, brittleness
under perturbed inputs, and unreliable automated judges -- and
they are mitigated by engineering (schemas, retrieval, retries,
validation, observability) rather than by model scale alone.

Gorilla's ablations make the retrieval point quantitatively.
Across APIBench, both BM25 and GPT-based retrievers improved
accuracy over zero-shot prompting, and the oracle retriever --
perfect recall -- bounded how far retrieval alone could go; the
fine-tuned LLaMA-7B model with retrieval beat GPT-4 and Claude on
API functionality accuracy, and the AST-based hallucination metric
showed argument errors dropping alongside accuracy gains. The
authors' framing has held up: the hard part of tool use is not
call syntax but disambiguation and relevance ranking among
similar APIs, and grounding in retrieved documentation beats raw
model scale on both accuracy and hallucination.

BFCL's scale and evolution quantify the capability frontier. The
benchmark covers roughly 2,000 question-answer pairs across
Python, Java, JavaScript, and REST APIs, with AST evaluation of
function and argument correctness, and has progressed from
expert-curated single-turn calls (V1) through enterprise-
contributed real-world scenarios (V2) to multi-turn, multi-step,
stateful evaluation (V3) and holistic agentic evaluation (V4).
Across its releases the finding is consistent: state-of-the-art
models score well on simple single-turn calls, then degrade on
parallel calls, relevance detection, and stateful sequences --
the exact dimensions production agents exercise most.

Error-class evidence comes from practitioner telemetry. Patronus
AI's agent-tools reference catalogs the standard failure classes
-- invalid parameter formats, timeout failures, permission
violations, and inappropriate tool selection -- and prescribes
try/catch with timeouts and intelligent retries so individual tool
failures cannot cascade system-wide. Zylos' production survey adds
the diagnostic reading of metrics: a tool with a 15% validation
error rate has a schema or description problem; a tool with a 5%
network error rate needs better retry logic; repeated identical
calls indicate a memory or state-management bug; and high latency
variance often masks timeout-driven retries masking deeper
issues. An agent making 3-10 tool calls per reasoning step
multiplies per-call failure probability across the workflow,
which is why retry, validation, and idempotency are not optional
refinements but load-bearing components.

Azure OpenAI's production walkthrough of a server-status agent
confirms the same loop in deployment practice: message plus tool
definitions, model decision, application execution, result
feedback, and final synthesis -- the loop is not an academic
abstraction but the shape real systems take.

The author's synthesis of the three layers: the loop delivers
large, replicated gains when grounded in feedback and
documentation, but every failure mode measured so far is
structural rather than random, and each maps to a concrete
engineering countermeasure.

## Implications

For agent engineers, the discipline is schema-first. Treat every
tool's JSON Schema as a published interface with a contract: root
and property descriptions written for the model reader, enums and
required fields for constraint, narrow parameter types to shrink the
hallucination surface, and validation before every execution since
the model's output is never trusted. Invest in selection when the
catalog grows: retrieval over tool documentation (Gorilla's core
finding), hierarchical routing, or on-demand tool loading -- and
treat namespacing as an experiment to evaluate per model. Build the
recovery ladder explicitly: exponential-backoff retries for
transient errors, error-message-as-context re-prompting for
validation failures, human escalation for permission failures, and
idempotency keys on every side-effecting tool. Measure what the
observability literature says to measure: per-tool latency
distributions (P50/P95/P99 -- high variance often masks
timeout-driven retries), per-tool error rates broken down by
validation/network/semantic class, and redundant-call detection,
because repeated identical calls signal that the agent is
forgetting results it already holds -- a memory bug surfacing as a
tool-usage pattern.

For platform and product teams, the implications are about control
and cost. The tool-calling loop is where excessive agency gets
bounded: the application executes, so permissions, sandboxes, and
human-in-the-loop checkpoints live at the execution boundary, and
Anthropic's guidance -- agents should pause for human feedback at
checkpoints or blockers -- is implementable precisely there.
Parallelism, caching, and retry policy are the cost dials: section
independent work to cut wall-clock latency, route cheap models to
cheap tools, and cap retry budgets so failures cannot compound.
The recurring empirical warning is to add orchestration only when
evaluation demonstrates the need: a single LLM call augmented with
tools is the default pattern, and every additional layer (routing,
orchestrator-workers, voting) buys quality at a cost and latency
price that must be justified.

For the fleet's own architecture, this topic is the execution layer
under several sibling topics. Agent skill systems package reusable
capabilities; tool use is how those capabilities get invoked at
runtime, so skill schemas are tool schemas and the same selection
and validation discipline applies. Multi-agent orchestration
delegates work to tool-using subagents; each delegation boundary is
a tool call with an argument contract. Context window management
governs what tool results cost: every observation injected into the
prompt consumes the scarce resource, so result summarization and
schema minimalism are context-management decisions as much as tool
decisions. Prompt engineering for agents extends into tool
descriptions -- the schema's prose is a prompt fragment that fires
on every selection decision. Agent evaluation inherits BFCL's
methodology and its open problems, and any fleet that scores its
own agents with automated judges should heed AgentProp-Bench's
chance-level finding before trusting the numbers. The author's
assessment: tool use is not a feature to add but the discipline
through which every other agent capability is exercised, and the
organizations that treat it as such -- schema contracts, failure
taxonomies, observability -- are the ones whose agents survive
contact with production.

For security teams, tool use redraws the threat model. Every tool
result is an injection channel -- a retrieved web page, a file
read, or an API response can contain instructions aimed at the
model -- so results must be sanitized, scoped, and logged like
untrusted network input. Prompt injection arriving through tool
results is indistinguishable from legitimate data to the model,
so containment must happen in code, not in the prompt. The
execution boundary should be least-privilege by default:
per-tool permission scopes, sandboxed or virtualized execution
for code and shell tools, dry-run modes for destructive actions,
and human approval gates for irreversible side effects. Audit
logs of every executed call turn tool use from an opaque
capability into a reviewable record.

For model and framework builders, the evidence points in two
directions. Downstream, providers now compete on structured
outputs and tool-calling reliability -- strict schemas, parallel
calls, and retrieval-augmented tool search are shipping features,
and benchmark position on BFCL has become a procurement signal.
Upstream, the ToolRL-DR result suggests robustness can be trained:
domain randomization over perturbed tool inputs produced a 3B
model that retained roughly three-quarters of its clean accuracy
under perturbations, narrowing the gap to far larger models. For
teams that control their own fine-tuning, perturbed-input training
is a concrete lever the way prompt-level retry policies are for
teams that do not.

For every agent practitioner in the fleet, the checklist reduces
to seven items: write schemas as documentation for a
non-deterministic reader; validate every argument before
execution; retrieve or route rather than dump hundreds of tools
into the prompt; parallelize independent calls and serialize only
dependencies; classify failures and match retries, re-prompts,
and escalations to the error class; make side-effecting tools
idempotent; and instrument per-tool latency, error, and
redundancy metrics from day one. Each item maps to a measured
failure mode above -- there is no folklore here, only
countermeasures the evidence supports.

For the library itself, the stakes are concrete: the discovery,
writing, and auditing skills of this very pipeline are tool-using
workflows, and the quality of their tool descriptions, schemas,
and error handling is the quality of the knowledge they produce.
The author's assessment is that tool-calling competence compounds
across every sibling topic in this domain: a well-designed tool
catalog makes skill systems maintainable, orchestration legible,
context budgets predictable, and evaluation meaningful -- while a
sloppy one degrades all four at once.

The direction of travel is clear: tool-calling is where model
quality and engineering quality meet, and both sides are
measurable -- which makes this discipline the most tractable
entry point into agent reliability.

## Sources

1. Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., &
   Cao, Y. (2023). "ReAct: Synergizing Reasoning and Acting in
   Language Models." ICLR 2023. https://arxiv.org/abs/2210.03629
   [high]

2. Patil, S. G., Zhang, T., Wang, X., & Gonzalez, J. E. (2023).
   "Gorilla: Large Language Model Connected with Massive APIs."
   arXiv:2305.15334. https://arxiv.org/abs/2305.15334 [high]

3. Patil, S. G., Mao, H., Cheng-Jie Ji, C., Yan, F., Suresh, V.,
   Stoica, I., & Gonzalez, J. E. (2025). "The Berkeley Function
   Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation
   of Large Language Models." ICML 2025.
   https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html
   [high]

4. OpenAI. "Function Calling." API documentation.
   https://developers.openai.com/api/docs/guides/function-calling
   [high]

5. Anthropic. "Building Effective Agents." Engineering blog,
   December 2024.
   https://www.anthropic.com/engineering/building-effective-agents
   [high]

6. Anthropic. "Writing Effective Tools for Agents." Engineering
   blog, 2025.
   https://www.anthropic.com/engineering/writing-tools-for-agents
   [high]

7. "When Simulation Lies: A Sim-to-Real Benchmark and
   Domain-Randomized RL Recipe for Tool-Use Agents." arXiv:2605.11928.
   https://arxiv.org/html/2605.11928v1 [high]

8. "Evaluating Tool-Using Language Agents: Judge Reliability,
   Propagation Cascades, and Runtime Mitigation in AgentProp-Bench."
   arXiv:2604.16706. https://arxiv.org/html/2604.16706v1 [high]

9. Zylos Research. "Tool-Augmented LLM Agents: Production
   Architecture." April 2026.
   https://zylos.ai/research/2026-04-16-tool-augmented-llm-agents-production-architecture/
   [medium]

10. Jsonic. "JSON Schema for Function Calling: OpenAI, Claude,
    Gemini." https://jsonic.io/guides/json-schema-function-calling
    [medium]

11. Patronus AI. "AI Agent Tools: Tutorial and Examples."
    https://www.patronus.ai/ai-agent-development/ai-agent-tools
    [medium]

## See Also

- `library/coding-agentic-ai/agent-skill-systems.md` -- how reusable
  capabilities are packaged; tool use is how packaged skills are
  invoked at runtime.
- `library/coding-agentic-ai/multi-agent-orchestration.md` -- how
  tool-using agents are composed into teams; delegation is a tool
  call.
- `library/coding-agentic-ai/context-window-management.md` -- tool
  results are observations that consume the context budget.
- `library/coding-agentic-ai/prompt-engineering-for-agents.md` --
  tool schemas and descriptions are prompt fragments that drive
  selection.
- `library/coding-agentic-ai/agent-evaluation-and-benchmarking.md`
  -- BFCL methodology and the open problems of agentic evaluation.
- `library/coding-agentic-ai/anchor-coding-agentic-ai.md` -- the
  domain anchor defining this topic's scope.
