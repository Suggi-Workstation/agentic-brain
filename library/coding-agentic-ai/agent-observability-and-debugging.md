---
name: agent-observability-and-debugging
id: 20260827T200233Z
tier: library-topic
domain: coding-agentic-ai
author: Library Runner
tags: [agent-observability, agent-debugging, tracing, spans, opentelemetry, replay-debugging, failure-taxonomy, langsmith]
links: [library/coding-agentic-ai/agent-evaluation-and-benchmarking.md, library/coding-agentic-ai/multi-agent-orchestration.md, library/coding-agentic-ai/tool-use-and-function-calling.md, library/coding-agentic-ai/context-window-management.md]
---

# Agent Observability and Debugging -- Why You Cannot Fix What You Cannot See Inside an Agent Run

Agent observability is the engineering discipline of capturing, storing, and
inspecting the complete execution record of an AI agent -- every model call,
tool invocation, retrieval step, guardrail check, and intermediate output --
so that a failed run can be understood, reproduced, and fixed. Traditional
software observability assumes deterministic control flow, but agents are
non-deterministic reasoning chains: the same input can take different paths,
which makes the execution trace the primary debugging artifact rather than a
supplementary one. Observability is therefore not an operational afterthought
for agent systems; it is the precondition for every other engineering
discipline in this domain, because evaluation, prompt iteration, and
orchestration all begin from what a trace reveals.

## Background

Software observability evolved in three waves, and each wave was driven by
systems whose behavior the previous wave could not explain. The first wave
was logging: application code emits lines of text, and operators read them
after something breaks. Logs work when control flow is simple and the state
space is small, but they do not scale to thousands of services. The second
wave was distributed tracing, popularized by Google's Dapper infrastructure
(Sigelman et al., 2010), which instrumented every request with a trace ID and
a tree of spans, one per downstream call, so that a single slow or failed
request could be followed across process boundaries. The third wave is the
standardization and productization of that model in OpenTelemetry, the CNCF
observability standard that defines the span as the universal unit of
instrumentation and ships collectors that can route spans to multiple
backends at once (OpenTelemetry, gen-ai semantic conventions repository,
2025). This lineage matters because agent observability borrows the entire
trace-and-span vocabulary while being forced to solve a problem none of its
predecessors had: the unit being traced is not a function call but a
reasoning process.

The reason classic observability breaks for LLM agents is structural, not
incidental. First, agent behavior is non-deterministic. A request handler
with a bug fails the same way every time, but an agent that writes a bad
patch, calls the wrong tool, or loops on a hallucinated fact may do none of
those things on the next run with the same input. The trace of the specific
failed run is therefore the only complete record of what actually happened,
and without it the failure may be unreproducible. Second, the reasoning that
produces the agent's decisions is hidden inside opaque model calls. In a
traditional service you can read the code to understand behavior; in an agent
the deciding "code" is the accumulated prompt -- system instructions, message
history, tool outputs, and retrieval results all concatenated and sent to a
model -- and the prompt that was actually sent on the failed run is rarely
what the developer believes was sent (LangChain, AI Agent Observability
resource, 2025). Third, agent structure is emergent rather than static. A
microservice call graph is fixed at deploy time, but an agent's span tree is
generated at runtime by the model's own decisions: loops, retries, handoffs
to sub-agents, and abandoned branches all appear as nested spans that no
static architecture diagram predicted (OpenAI, Agents SDK tracing
documentation, 2025). Fourth, the economics are different: every step of the
tree consumes tokens, latency, and money, so the trace is simultaneously a
debugging tool and a cost-accounting ledger.

The tooling response began with platform-native tracing. LangChain launched
LangSmith in 2023 as a debugging and evaluation platform for LLM
applications, and it has since expanded into a framework-agnostic
observability platform whose traces capture "the full execution tree: every
LLM call, tool invocation, retrieval step, and the reasoning that connected
them" (LangChain, AI Agent Observability resource, 2025). Independent
platforms followed the same shape -- Braintrust, Arize Phoenix, and others --
as did framework SDKs: the OpenAI Agents SDK ships with tracing enabled by
default, wrapping every runner invocation, model generation, function call,
guardrail, and handoff in a typed span without any user instrumentation
(OpenAI, Agents SDK tracing documentation, 2025). The direction of travel is
clear: tracing stopped being a feature that developers must bolt on and
became table stakes of any agent framework.

Alongside the platforms, two standardization pushes are reshaping the field.
The first is OpenTelemetry's Generative AI semantic conventions, which define
gen_ai spans for model calls and gen_ai.agent spans for agent operations so
that traces from any framework can be exported over OTLP and analyzed by any
backend, including correlation with the rest of an organization's
observability stack (OpenTelemetry, gen-ai semantic conventions repository,
2025). The second push is academic: researchers have begun treating agent
traces as a dataset. AIOS (Mei et al., 2024) proposed an operating-system
layer for LLM agents that manages scheduling, context, memory, and tool
access, with observability of agent execution built in as a kernel service
rather than an add-on. And the MAST project (Cemri et al., 2025) built the
first empirically grounded failure taxonomy for multi-agent systems from
annotated execution traces, demonstrating that trace analysis is becoming a
research discipline in its own right. The remainder of this topic develops
the concepts, evidence, and practical consequences of this emerging
discipline.

## Core Concepts

### The Trace as the Run Tree

The central abstraction of agent observability is the trace: the complete
record of a single end-to-end workflow execution, composed of spans, each
span being one unit of work with a start time, an end time, a parent, and
typed payload data. LangSmith calls these units runs and binds them to a
trace by a trace ID; the OpenAI Agents SDK calls them spans and gives each a
trace_id and parent_id (LangChain, observability concepts documentation,
2025; OpenAI, Agents SDK tracing documentation, 2025). The tree shape is the
artifact of the agent's decision process: a root agent span, under it a
sequence of generation spans (one per model turn), under each generation the
tool spans it triggered, under a handoff span an entire nested sub-agent
tree. Reading the tree top to bottom reconstructs the agent's trajectory --
what it decided, in what order, based on what evidence -- and the shape of
the tree itself is diagnostic. A wide, shallow tree means the agent
parallelized; a deep, repetitive subtree means a loop; a missing branch means
a step that never happened.

Trace metadata extends the schema outward: workflow_name labels the logical
application, group_id links all traces from one conversation, and custom
metadata carries deployment identifiers such as version or release, so that
a production failure can be correlated to the exact agent build that
produced it (OpenAI, Agents SDK tracing documentation, 2025).

### The Span Taxonomy: What a Complete Agent Record Contains

A useful span is not a log line; it is a typed record with a schema. The
OpenAI Agents SDK's default instrumentation enumerates the industry consensus
on what must be captured: generation spans holding the model parameters and
messages actually sent, function spans holding the tool name and JSON
arguments, guardrail spans holding input and output validation, handoff spans
recording delegation between agents, plus transcription and speech spans for
audio (OpenAI, Agents SDK tracing documentation, 2025). Two fields deserve
emphasis. The first is the prompt as sent: because an agent's behavior is a
function of its entire assembled context, debugging requires seeing exactly
which instructions, messages, and tool outputs the model received on the
failed run -- visibility that connects directly to context-window-management
discipline. The second is token and cost accounting per span, which turns the
trace into a ledger that answers not only "what went wrong" but "what did
that mistake cost" (LangChain, AI Agent Observability resource, 2025).

### Failure Taxonomies: Turning Trace-Reading into Classification

Reading traces one failure at a time does not scale, so the field is
developing taxonomies that classify spans into known failure modes. The MAST
taxonomy (Cemri et al., 2025) is the strongest example: built from expert
annotation of over 150 multi-agent traces and validated at kappa 0.88
inter-annotator agreement, it defines 14 failure modes in three categories --
system design issues (for example step repetition and loss of conversation
history), inter-agent misalignment (for example information withholding,
ignored input, and reasoning-action mismatch), and task verification failures
(for example premature termination and incorrect verification). The value of
a taxonomy is that it converts the open-ended question "why did the agent
fail" into a classification task with named categories, which can then be
counted, trended, and -- as the MAST authors demonstrate by shipping the
taxonomy as an installable Python package for trace analysis -- partially
automated.

MAST also locates each failure mode within the execution timeline --
pre-execution, execution, or post-execution -- and its dataset spans seven
frameworks including ChatDev, where annotators observed an agent disobeying
its role specification by terminating a conversation without the designated
consensus step (Cemri et al., 2025). The practical payoff: a team that tags
its own traces with taxonomy labels can aggregate failure modes over time
and see which category dominates its system, converting anecdotal debugging
into a measured distribution.

### OpenTelemetry and the Standardization Push

The OpenTelemetry GenAI semantic conventions define gen_ai spans (for model
calls, with attributes covering the model, request, and token usage) and
gen_ai.agent spans (for agent operations such as agent creation and
execution), with the goal that any framework emits the same shape of data
(OpenTelemetry, gen-ai semantic conventions repository, 2025). LangSmith's
end-to-end OpenTelemetry support shows the interop pattern: an OTLP exporter
sends spans to a collector that fans them out to multiple backends
simultaneously, with langsmith-specific attributes such as the dotted order
field encoding each span's position in the trace tree (LangChain, Trace with
OpenTelemetry documentation, 2025). The strategic consequence is
decoupling: organizations can adopt a framework SDK's native tracing for
development depth and still export to their existing observability
infrastructure for correlation with databases, queues, and services --
agent spans sit next to database spans in one queryable graph.

### Replay and Time-Travel Debugging

Because agents are non-deterministic, a trace that merely records outcomes is
not enough; the trace must record the inputs and outputs of every step so
that the run can be replayed for inspection. The open-source agent-replay
tool illustrates the pattern: it stores every thought, tool call, retrieval,
and output of each run in a local SQLite database and lets a developer replay
the execution step by step "like rewinding a tape," diff behavior across
agent versions, and fork a recorded run to test whether a candidate fix would
have changed the outcome (agent-replay, GitHub repository, 2025). The
limitation is honest and inherent: replay of recorded steps is deterministic,
but re-execution is not, because the model may sample differently. Time-travel
debugging therefore means inspecting the recorded trajectory and testing
changes against it -- the trace as a fixed experimental substrate, not a
script to be rerun.

Industry guidance converges on the same discipline: Braintrust's production
debugging guide treats the trace, not the chat log, as the unit of analysis,
and recommends auto-instrumentation of agent SDKs so that recording is a
property of the runtime rather than something developers must remember to
add (Braintrust, 2025).

### The Trace-to-Eval Loop

The most consequential use of traces is as the input to evaluation. Arize's
engineering guidance states the principle directly: start evaluations from
traces, not from a blank page, because traces show what actually fails
(Arize AI, harness article, 2025). The loop runs: trace runs in production,
select failing spans, ask whether the agent or the evaluator was wrong,
update the prompt, tool, context, or rubric, then re-run -- with each cycle
producing a regression eval so the same failure cannot silently return.
LangSmith operationalizes the same loop at platform scale, converting traces
into datasets, offline and online evals, and annotation queues, with
clustering of recurring failure patterns across production traces (LangChain,
AI Agent Observability resource, 2025). The loop is where observability and
evaluation meet, and it is the mechanism by which a debugging tool becomes an
improvement engine.

The design principle underneath is that a failure you cannot see is a
failure you will repeat; only a failure visible in the trace can be
converted into a regression test that survives refactors (Arize AI, 2025;
LangChain, AI Agent Observability resource, 2025).

### Cost, Latency, and Privacy in the Trace Layer

Traces are sensitive by construction: they contain the full prompts and
tool payloads of real user traffic, so observability is also a data-governance
problem. The OpenAI Agents SDK documents the sharp edge: tracing is disabled
for organizations under Zero Data Retention policies, and per-run disabling
flags exist for handling sensitive requests (OpenAI, Agents SDK tracing
documentation, 2025). Platforms impose retention windows -- LangSmith's SaaS
retains trace data for 180 days, after which traces are deleted while
datasets persist indefinitely (LangChain, observability concepts
documentation, 2025) -- and the cost side is equally structural: capturing
every span of every run at production volume has real storage and export
costs, which is why sampling, tagging, and selective instrumentation are
first-class concerns rather than afterthoughts.

## Evidence

The strongest empirical foundation for agent observability comes from the
MAST project, which treats traces as a scientific dataset. Cemri et al.
(2025) collected 1,642 annotated execution traces from seven popular
multi-agent frameworks running GPT-4 and Claude model families on coding,
math, and general agent tasks, built the taxonomy from 150 expert-annotated
traces with inter-annotator agreement of kappa 0.88, and then scaled the
annotation across the full dataset. The findings are directly actionable:
failures concentrate in the handoffs between agents and in verification
behavior, with system-design modes like step repetition and loss of
conversation history among the most prevalent. The methodological claim is
as important as the empirical one -- that failure dynamics of agent systems
can only be understood from execution traces, not from final-answer scores,
because the same final answer can be reached through many trajectories and
only some of them are sound.

The taxonomy's own structure is evidence about where agentic failure
concentrates. MAST locates its failure modes across the pre-execution,
execution, and post-execution stages of the inter-agent conversation, which
means failures originate not only in what the model generates but in how
the system is designed and in how -- or whether -- its outputs are verified
(Cemri et al., 2025). The pedagogical value of this distribution is
immediate: a debugging engineer who can read which stage a span belongs to
knows where in the stack to look before examining a single token of model
output.

Industry evidence is vendor-reported but directionally consistent. LangChain
reports a Klarna case study in which trace-driven debugging of customer
support agents reduced customer resolution times by 80 percent, and states
that LangSmith has handled over one billion traces, which is evidence of
adoption volume more than of causal efficacy (Articsledge, LangSmith guide,
2025). The more rigorous form of industry evidence is design documentation
from primary sources. The OpenAI Agents SDK's tracing documentation
demonstrates the "trace by default" architecture: the runner wraps the
workflow in a trace, each model turn in a turn span, each agent invocation in
an agent span, and each generation, function call, guardrail, and handoff in
typed spans, with no instrumentation required from the application developer
(OpenAI, 2025). The fact that a mainstream SDK ships this by default, and
that its only escape hatch is an explicit environment-variable opt-out, is
primary-source evidence that the industry has converged on the position that
agents are undebugable without traces.

The standardization evidence points the same direction. OpenTelemetry moved
its GenAI semantic conventions into a dedicated repository covering both
gen_ai spans and gen_ai.agent spans, and LangSmith shipped end-to-end
OpenTelemetry support in March 2025, replacing its earlier ingest-only OTel
support with native SDK instrumentation -- a primary-source signal that the
open standard is winning the format question for agent traces
(OpenTelemetry, gen-ai semantic conventions repository, 2025; LangChain,
Trace with OpenTelemetry documentation, 2025).

The academic operating-systems literature provides a third line of evidence.
AIOS (Mei et al., 2024) argues that observability belongs at the platform
layer: the proposed LLM agent operating system manages agent lifecycles,
context, memory, and tool access through a kernel-like scheduler and exposes
agent execution telemetry as a built-in service for meeting production SLAs.
The relevance here is architectural: when execution visibility is a property
of the runtime rather than a responsibility of each application, the marginal
cost of observability collapses, and the failure mode of "we did not
instrument it" disappears.

Taken together with the SDK default-tracing design, AIOS represents the
second extreme of a spectrum whose first extreme is per-application
instrumentation: observability provided once by the infrastructure and
consumed by every agent above it, the way process accounting is provided by
an operating system (Mei et al., 2024).

Finally, the trace-to-eval loop has direct empirical demonstration in the
harness-building literature. Arize's worked example follows a product
manager agent that pulled 40 discussions, 60 issues, and 8 releases from a
repository, scored the feedback, and generated a report -- then used the
trace to locate the specific failure (systematically under-ranking a class
of high-impact bugs) and convert it into a targeted evaluation and a harness
change (Arize AI, 2025). The example's lesson is procedural: the team did not
guess what was wrong from the final report; they inspected the spans, found
the under-weighted input, and fixed the harness at the point where the trace
showed the decision being made.

The loop's heuristics deserve recording because they generalize: a healthy
evaluation pipeline produces a mix of passes and failures that can be
inspected, categorized, and acted on -- if everything passes, the evaluation
is too weak; if everything fails, it is misaligned (Arize AI, 2025).
LangChain's guidance adds the operational version: enable tracing on a
subset of production traffic first, and instrument with decorators that
require no architecture changes so that tracing can be toggled without
redeployment (LangChain, AI Agent Observability resource, 2025).

Industry tooling converged on the same abstractions independently, which is
weak-but-real evidence that the abstractions are right: Braintrust's tracing
documentation, the OpenAI Agents SDK, LangSmith, and OpenTelemetry all
express agent execution as typed spans with parent-child nesting, distinct
generation and tool spans, and per-span token and latency accounting
(Braintrust, 2025; OpenAI, 2025; LangChain, observability concepts
documentation, 2025; OpenTelemetry, 2025). The platform vendors' volume
claims, while self-reported, describe a data layer with the operational
weight of production logs: LangChain reports over one billion traces
processed by LangSmith and a Klarna deployment in which trace-driven
debugging cut customer resolution time by 80 percent (Articsledge, 2025).

## Implications

For agent engineers building harnesses, the practical consequence is a
workflow inversion. The final answer is no longer the first thing examined;
the trace is. The debugging sequence is: open the failed run's trace, walk
the span tree, compare the prompt-as-sent against the prompt-as-intended,
inspect tool inputs and outputs at the first divergent step, and localize the
failure to a span before changing anything. This is also the only reliable
way to debug prompts: because an agent prompt must survive dozens of tool
calls, the failure of a prompt is visible in the spans where the agent's
behavior diverges from the instruction, which is far more precise than
re-reading the prompt text.

A secondary habit follows: when a fix is applied, the failed trace is
retained as a regression fixture, and the new behavior is verified by
replaying the recorded run or re-running against it, so that debugging
becomes a closed loop rather than a sequence of unverifiable edits
(agent-replay, GitHub repository, 2025).

For evaluation teams, the implication is that evaluation datasets should be
born from traces, not written from imagination. A regression suite assembled
from real production failures, each failure anchored to its trace, catches
recurrences of the specific errors the system has actually made; a suite of
hypothetical scenarios catches the errors the authors could imagine. The
discipline in between -- for each failing span, deciding whether the agent
was wrong or the evaluator was wrong -- keeps the measurement system honest
and is itself a trace-driven activity.

This changes the shape of the evaluation artifact: the durable unit is no
longer the score but the span -- the recorded instance of correct or
incorrect behavior -- because scores aggregate what spans preserve
(LangChain, AI Agent Observability resource, 2025). A team that builds this
muscle finds a curious inversion: the most valuable evaluations are often
written for failures it did not anticipate, because the trace showed it the
failure first.

For multi-agent system builders, MAST's finding that failures concentrate in
handoffs and verification has a direct design consequence: the spans at
agent boundaries deserve the most scrutiny, and verification gates should be
observed entities in their own right, not buried inside a sub-agent's
private reasoning. A builder who cannot see, in the trace, which agent said
what to which other agent and whether any verification actually ran is
operating a system whose most failure-prone components are invisible.

Concretely, handoff spans should carry the full message passed between
agents, and verification steps should emit spans with their inputs, their
verdicts, and their evidence, so that a failed handoff can be adjudicated
from the trace alone without replaying the whole system (Cemri et al.,
2025).

For SRE and platform teams, agent observability converges with the
organization's existing stack through OpenTelemetry. The same collector that
receives service spans can receive gen_ai spans, which means agent latency,
error, and cost data becomes queryable alongside everything else, and
agent-specific thresholds (token cost per trace, generation latency
percentiles) can feed the same alerting pipelines. The constraints are real:
trace volume from token-heavy agents is large, retention windows apply, and
sampling strategies must be chosen before production load forces them.

Practically, most teams should start with their framework's baked-in tracing
for development depth and add OTel export when agent traffic becomes a
production concern, following the LangChain recommendation to instrument
incrementally rather than instrument everything on day one (LangChain, AI
Agent Observability resource, 2025).

For security and governance, the trace layer is a new category of sensitive
data. Traces contain user prompts, internal tool outputs, and system
instructions; they are subject to the same retention and access rules as the
data they mirror, and policies like Zero Data Retention can conflict with
default-on tracing. The engineering answer is selective instrumentation,
redaction, and per-run opt-outs -- which must themselves be observable, or
the privacy mechanism silently creates the very blind spot observability was
meant to eliminate.

Consequently, observability policy and data policy must be designed
together: what gets recorded, where it is stored, how long it lives, and
who can read it are one decision, not four (OpenAI, Agents SDK tracing
documentation, 2025).

For the individual operator of a small agent fleet -- the case this
library's own pipeline exemplifies -- the same discipline scales down. A
structured execution record that captures each step's intent, action, and
outcome is enough to turn "the agent failed" into "the agent failed at this
step, for this reason, and here is the patch." The difference between a
system whose failures are inspectable and one whose failures are mysteries
is not tooling budget; it is the decision to record the run before it is
needed. The tools cited in this topic -- from a small SQLite recorder to a
hosted platform -- differ in scale by orders of magnitude, but they share
one invariant: the trace is written before the question is asked, because it
cannot be written after (the author's synthesis, drawn from the tooling
patterns above).

The author's assessment is that observability is the compounding substrate of
this domain. Every other discipline in coding-agentic-ai -- evaluation,
prompt engineering, context management, orchestration -- consumes traces as
its raw material, and the fleet's own library pipeline is a working instance
of the loop: a run fails or drifts, the failure is read from the execution
record, the correction is written back as a skill patch or a logbook entry,
and the next run is measurably better. Systems that close this loop improve
monotonically; systems that do not merely repeat their failures.

## Sources

1. Cemri, M., Pan, M. Z., Yang, S., Agrawal, L. A., et al. (2025). "Why Do
   Multi-Agent LLM Systems Fail?" arXiv:2503.13657. Introduces MAST, the
   first empirically grounded multi-agent failure taxonomy (14 modes, 3
   categories) and MAST-Data, 1,642 annotated traces across 7 frameworks.
   https://arxiv.org/abs/2503.13657 [high]

2. OpenAI. "Tracing -- OpenAI Agents SDK." Official SDK documentation of the
   trace and span model, default instrumentation, and tracing controls.
   https://openai.github.io/openai-agents-python/tracing/ [high]

3. OpenTelemetry. "Generative AI Semantic Conventions" repository (gen-ai
   spans and gen-ai agent spans).
   https://github.com/open-telemetry/semantic-conventions-genai [high]

4. LangChain. "Observability concepts -- LangSmith Docs." Definitions of
   traces, runs, instrumentation mechanisms, and 180-day retention policy.
   https://docs.langchain.com/langsmith/observability-concepts [high]

5. LangChain. "Trace with OpenTelemetry -- LangSmith Docs." OTLP export,
   collector fanout, and LangSmith span attribute mapping.
   https://docs.langchain.com/langsmith/trace-with-opentelemetry [high]

6. Mei, K., et al. (2024). "AIOS: LLM Agent Operating System."
   arXiv:2403.16971. Proposes an OS layer for LLM agents with kernel-level
   scheduling, context, memory, tool management, and built-in observability.
   https://arxiv.org/abs/2403.16971 [high]

7. Sigelman, B. H., Barroso, L. A., Burrows, M., et al. (2010). "Dapper, a
   Large-Scale Distributed Systems Tracing Infrastructure." Google Technical
   Report. The foundational distributed tracing system.
   https://research.google/pubs/pub36356/ [high]

8. LangChain. "AI Agent Observability: Tracing, Testing, and Improving."
   Platform resource on trace anatomy and the trace-to-eval loop.
   https://www.langchain.com/resources/agent-observability [medium]

9. Braintrust. "How to Trace and Debug AI Agents in Production." Industry
   guide to auto-instrumentation and trace-driven debugging.
   https://www.braintrust.dev/articles/agent-tracing-debug-ai-agents-production [medium]

10. Arize AI. "How to Build a Better Agent Harness with Traces and Evals."
    Worked example of the trace, eval, failed-span, harness-change loop.
    https://arize.com/blog/improve-ai-agents-traces-evals-harness/ [medium]

11. Articsledge. "What is LangSmith? Complete Guide to LLM Observability."
    Summary of LangSmith capabilities and reported platform statistics
    (Klarna case study, one billion traces).
    https://www.articsledge.com/post/langsmith [medium]

12. clay-good. "agent-replay." Open-source SQLite-backed CLI for recording,
    replaying, forking, and evaluating agent execution traces.
    https://github.com/clay-good/agent-replay [low]

## See Also

- `library/coding-agentic-ai/agent-evaluation-and-benchmarking.md` -- the
  measurement discipline whose datasets and regressions are built from the
  traces this topic describes.
- `library/coding-agentic-ai/multi-agent-orchestration.md` -- MAST shows that
  the majority of multi-agent failures live in the handoffs this topic
  argues must be observable.
- `library/coding-agentic-ai/tool-use-and-function-calling.md` -- tool spans
  are the richest nodes in the trace tree and the usual site of failure
  localization.
- `library/coding-agentic-ai/context-window-management.md` -- the
  prompt-as-sent visibility this topic requires is the managed artifact of
  context discipline.
- `library/coding-agentic-ai/anchor-coding-agentic-ai.md` -- the domain
  anchor that places observability and debugging inside this domain's scope.
