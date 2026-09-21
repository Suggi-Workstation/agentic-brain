---
name: agent-harness-design
id: 20260920T143640Z
tier: library-topic
domain: coding-agentic-ai
author: Librarian
tags: [agent-harness, agent-runtime, control-loop, context-assembly, tool-dispatch, state-management, error-recovery]
links: [library/coding-agentic-ai/anchor-coding-agentic-ai.md, library/coding-agentic-ai/tool-use-and-function-calling.md, library/coding-agentic-ai/context-window-management.md, library/coding-agentic-ai/agent-memory-and-persistence.md, library/coding-agentic-ai/agent-observability-and-debugging.md, library/coding-agentic-ai/agent-sandboxing-and-security.md, library/coding-agentic-ai/agent-evaluation-and-benchmarking.md]
reviewed: 2026-09-21
---

# Agent Harness Design -- Reliability Comes From the Runtime Around the Model

An agent harness is the runtime layer that repeatedly assembles context, invokes a language model, dispatches requested actions, records state, and decides whether work should continue, pause, recover, or stop. A capable model becomes a dependable agent only when this surrounding system supplies explicit interfaces, bounded execution, durable evidence, and recovery paths; the model and harness therefore form the real unit of behavior. [1][2][3][9]

## Background

A language model call is a bounded transformation from an input context to an output. It does not, by itself, preserve a task across calls, execute a tool, decide which result should enter the next prompt, enforce permissions, or recover a workflow after a process crash. Agent systems add those functions around the model. Microsoft defines an agent harness as runtime scaffolding that drives model and tool calls, manages conversation state and context, applies approval policies, and keeps multi-step work progressing. Anthropic describes agents in their simplest form as language models using tools in a loop based on environmental feedback. OpenAI's Agents SDK documentation makes the loop concrete: prepare input, call the model, inspect the output, execute tool calls or switch specialists, and continue until a final answer or another stopping condition occurs. [1][2][3]

This runtime perspective developed from earlier work on reasoning-and-acting loops. ReAct interleaved language reasoning with actions and observations instead of requiring a model to reason entirely from its parameters. Its experiments used external environments such as a Wikipedia API, ALFWorld, and WebShop, so each observation could alter the next decision. The important architectural result was not a particular prompt format. It was the closed-loop relationship among model output, environmental action, returned evidence, and revised reasoning. Modern function-calling agents retain that shape even when hidden reasoning is unavailable: a model proposes a structured call, deterministic application code executes it, and the returned observation becomes part of a later model input. [2][7]

As agent tasks became longer, the loop acquired more responsibilities. A production runtime must distinguish transient model context from persistent task state; select tools without exposing every capability on every turn; validate arguments before side effects; preserve a resumable event history; enforce budgets and approval boundaries; and emit traces that explain what happened. Microsoft's current Agent Framework harness composes a chat client, a function-invoking pipeline, context providers, middleware, observability, approval handling, optional compaction, and bounded looping. LangChain's documentation similarly separates model context, tool context, and lifecycle context, showing that information visible to one model call is not the same object as state that persists across turns. [1][4]

Long-running work exposed why a larger context window is not sufficient. Anthropic reported that agents operating across fresh context windows could attempt too much at once, leave half-finished work undocumented, or declare completion because they saw some existing progress. Its long-running harness used an initializer session, a structured feature list, a progress file, git history, incremental work, and end-to-end tests so a later session could reconstruct the state of the project. Compaction remained useful, but it did not replace explicit artifacts or clean checkpoints. The case demonstrates that continuity is a property of the runtime's state protocol, not an automatic consequence of passing more conversation text. [6]

Infrastructure failures exposed the same principle at a lower layer. Anthropic's Managed Agents architecture separates the session, harness, and sandbox. The session is an append-only event log; the harness runs the model loop and routes tool calls; the sandbox supplies an execution environment. A failed sandbox can be reprovisioned and treated as a tool failure, while a failed harness can be restarted and resume from the durable session log. Anthropic reports that making sandbox provisioning demand-driven also reduced median time to first token by roughly 60 percent and the 95th percentile by more than 90 percent in that system. These are vendor-reported production results, not a controlled comparison across independent platforms, but they illustrate the value of stable interfaces and externalized state. [5]

The harness should not be confused with the model, a fixed workflow, or an evaluation harness. The model supplies learned inference. A fixed workflow specifies a predetermined sequence of steps. An agent harness supplies the conditions under which the model may choose and execute a sequence while remaining inside lifecycle, state, tool, policy, and budget constraints. An evaluation harness runs tasks and grades outcomes; an agent harness runs the agent being evaluated. Anthropic's evaluation guidance and the scaffold-effect literature both treat the model-harness pair as the evaluated system because changes in context, tools, stop rules, and execution policy can change cost, failure mode, and success even when the model is held constant. [9][10][11]

The boundary is also a domain boundary. General model architecture and training belong to AI and machine-learning research. Harness design concerns the engineering system that surrounds inference: context assembly, tool mediation, execution environments, persistent state, verification, observability, and control. The author's synthesis is that a robust harness does not try to make a stochastic model deterministic. It makes every transition around that model explicit enough to validate, record, bound, and recover. That distinction keeps model capability available while assigning authority and reliability to code that can be inspected and tested. [1][3][4][5]

## Core Concepts

### 1. The Harness Owns the Agent Loop

The loop is the harness's central state machine, not a prompt convention. At the start of a step, the harness reads the current task state and assembles the next model request. It then invokes the selected model, parses the response, and classifies the result as a final answer, one or more tool calls, a handoff, a request for human input, an invalid response, or a failure. Each classification maps to an explicit transition. OpenAI's runner loops over model calls, tool execution, and specialist handoffs until it reaches a final answer; Microsoft adds configurable iteration limits and optional evaluator- or predicate-driven re-invocation. [1][3]

A sound loop declares its stop conditions before execution. Final output, verified goal completion, user cancellation, approval pause, maximum turns, token or cost budget, timeout, repeated equivalent action, and unrecoverable error are different terminal states. They should not collapse into one generic exit because the caller needs to know whether the task succeeded, paused, exhausted a budget, or failed. OpenAI explicitly distinguishes runtime failures such as max-turn limits, guardrail exceptions, and tool errors from expected approval pauses that should resume from the same state. [3]

The author's synthesis is that every iteration should be represented as a transaction with four phases: assemble, decide, execute, and commit. Assembly creates a versioned model input. Decision produces a typed proposal. Execution applies validation and policy before interacting with the environment. Commit records the observation and state transition only after the outcome is known. This structure prevents an ambiguous half-step in which a side effect occurred but the durable record still claims the tool call is pending. [3][5][10]

### 2. Context Assembly Is a Policy, Not Conversation Concatenation

The model sees only the request assembled for the current call. The harness decides which instructions, messages, tool schemas, retrieved memories, current files, summaries, and runtime facts enter that request and in what order. LangChain distinguishes model context from persistent tool and lifecycle context: changing the model request for one call need not rewrite stored state, while lifecycle middleware can persist a summary or state update for future turns. This separation lets the harness experiment with context strategy without corrupting the authoritative task record. [4]

Context assembly needs explicit provenance and precedence. Stable system rules, task instructions, trusted configuration, user input, retrieved records, and tool outputs do not carry equal authority. The harness should preserve their source and render them in a format that does not silently turn untrusted content into control instructions. It should also select only tools relevant to the present state. LangChain notes that too many tools can overload context and increase selection errors, while too few block capability; its dynamic-selection examples filter tools by authentication, permissions, feature flags, and conversation stage. [4]

Compaction is one context policy, not the state system itself. Summarization reduces prompt size but can omit a fact later turns need. Anthropic therefore separates a durable event log from the context-window view in Managed Agents: the session retains events while the harness selects, slices, transforms, or compacts them for a particular model call. The author's synthesis is that the durable record should be lossless enough for recovery and audit, while the prompt view may be lossy for efficiency. Conflating them makes a compression decision irreversible. [5]

### 3. Tool Dispatch Separates Proposal From Authority

A model proposes a tool name and arguments; the harness decides what executes. Dispatch begins with name resolution and schema validation, then applies authorization, rate, budget, target, and approval policy before calling the implementation. The result is normalized into a typed observation containing status, output, error class, timing, and side-effect metadata. This separation is necessary because a syntactically valid model output is neither proof that the action is permitted nor proof that its arguments are semantically safe. [1][2][4]

Dispatch also determines concurrency. Independent read operations can run in parallel, while a call that consumes another call's output must wait. Side-effecting calls may require serialization, idempotency keys, or a transaction boundary. A robust dispatcher records the exact call before execution and the exact result afterward, correlating both with the run, step, task, and actor. OpenAI's observability documentation treats model calls, tool calls, handoffs, and guardrails as traceable events, while Microsoft's harness makes approval and observability middleware part of the runtime composition. [1][10]

Tool results should be bounded before re-entering context. Large command output, duplicate records, or binary data can consume the next prompt without improving the decision. The dispatcher can store the full result outside the prompt, return a structured summary plus a retrieval handle, and preserve error details needed for recovery. The author's synthesis is that a tool interface has two contracts: an execution contract for deterministic code and an observation contract for the model. Treating one raw string as both contracts creates avoidable ambiguity. [4][8]

### 4. State Must Be Explicit, Durable, and Layered

Agent state includes more than message history. It can include the goal, current plan, completed and pending actions, tool observations, approvals, budgets, files, artifacts, checkpoints, and stop reason. OpenAI documents several continuation strategies, including application-managed history, SDK sessions, server-managed conversations, and response identifiers, and warns that mixing state strategies can duplicate context. A harness should select one authoritative continuation model for each conversation or task. [3]

Durability is what turns a transient loop into a resumable agent. Anthropic's Managed Agents case externalizes an append-only session log so a replacement harness can reload the event stream and continue after failure. Its long-running coding case uses simpler durable artifacts: a progress file, git commits, a feature ledger, and an initialization script. The implementations differ, but the invariant is the same: a new process can reconstruct what is true without relying on the previous model instance's hidden state. [5][6]

Layered state prevents one storage mechanism from serving incompatible purposes. The author's synthesis is to distinguish an authoritative event log, a current task projection, working files or artifacts, and long-term memory. The event log answers what happened; the projection answers what is currently believed to be true; artifacts contain the work product; long-term memory stores selected knowledge across tasks. Each layer needs versioning, ownership, and an update rule. [4][5][6]

### 5. Recovery Is a State Transition With a Budget

Retries are not a universal recovery mechanism. A transient network failure may justify bounded retry with backoff. Invalid tool arguments require correction from validation feedback. A context overflow requires trimming, retrieval, or compaction. A failed test should return evidence to the planning loop. An authorization denial should not be retried unchanged. Repeating the same action without a changed precondition is a loop defect, not recovery. [3][4][8]

The harness should classify failures by layer: model transport, response parsing, context assembly, tool validation, tool execution, environment, policy, verification, or control flow. Each class maps to permitted recovery actions and a finite budget. After that budget is exhausted, the harness should backtrack to a checkpoint, request human input, produce a partial result with explicit status, or fail closed. This is the author's synthesis from the failure surfaces described by OpenAI, the context lifecycle described by LangChain, and the empirical interface failures measured by SWE-agent. [3][4][8]

Recovery depends on idempotency and checkpoints. If an external action may already have succeeded before a timeout, blind retry can duplicate it. The harness needs a stable action identifier, a way to query outcome, and a policy for resume versus compensate. Checkpoints should be placed after validated state transitions, not at arbitrary token boundaries. A restart then resumes from the last committed state rather than replaying an unknown side effect. [3][5]

### 6. Verification Must Be Distinct From Generation

A model's declaration that work is complete is not a completion test. The harness should define outcome evidence outside the final answer: tests, state queries, schema checks, artifact existence, policy checks, or human review. Anthropic's long-running-agent case found that explicit browser-based end-to-end testing caught defects that source inspection, unit tests, or simple HTTP checks did not reveal. SWE-agent's evaluation likewise grades repository changes through the external SWE-bench test environment rather than accepting a persuasive explanation. [6][8]

Verification can run during the loop and at termination. During execution, validators reject malformed edits or failed tests and return actionable observations. At termination, a completion gate checks the task's acceptance criteria and records the evidence. If verification fails, the loop may re-enter planning within a bounded repair budget. The author's synthesis is that the stop rule should depend on verified environment state whenever such a state is available, not solely on a special phrase or model-produced confidence score. [6][8][10]

### 7. Observability Is Part of Execution Semantics

A trace should reconstruct the run: assembled model input or a governed reference to it, model output, tool proposal, policy decision, execution result, state update, cost, latency, and stop reason. OpenAI's Agents SDK tracing records model calls, tool calls, handoffs, guardrails, and custom spans. Microsoft enables OpenTelemetry in its harness composition. These records support debugging, evaluation, cost analysis, and incident review. [1][10]

Observability must not leak every secret contained in the run. Credentials, private data, and sensitive tool output require redaction, access control, and retention rules. At the same time, redaction should preserve enough structure to locate the first divergent step. The author's synthesis is that a trace is a governed evidence artifact, not a complete prompt dump by default. [5][10]

### 8. Modularity Should Follow Failure Boundaries

A harness becomes easier to evolve when model access, session storage, tool execution, sandbox provisioning, policy, and user interface depend on explicit interfaces. Anthropic's Managed Agents design allows the harness, session, and sandbox to fail or be replaced independently. Microsoft's harness composes chat pipelines, context providers, middleware, and user experience rather than embedding every behavior in one monolithic loop. [1][5]

Modularity is valuable only when it aligns with operational boundaries. Splitting every function into a service adds latency and failure modes; coupling state, credentials, and generated code in one process increases blast radius and blocks independent recovery. The author's synthesis is to isolate components when they have different trust, durability, scaling, or restart requirements, and keep them together when a local call preserves a simple invariant. Stable interfaces matter more than the number of services. [5]

## Evidence

### ReAct: Environmental Feedback Improves the Basic Loop

Yao et al. evaluated ReAct by prompting language models to interleave reasoning traces with actions and observations. The study used knowledge-intensive tasks with a Wikipedia API and interactive decision environments including ALFWorld and WebShop. This method compared the combined reasoning-and-acting loop with approaches that reasoned without external action or acted without interleaved reasoning. [7]

The reported finding was that environmental observations reduced hallucination and error propagation on knowledge tasks and improved performance in interactive tasks. The broader harness inference is bounded: ReAct does not establish a complete production runtime, but it demonstrates why a useful agent loop must route real observations back into later decisions. A loop that calls the model repeatedly without grounded environmental feedback is iteration, not necessarily agency. [7]

### SWE-agent: Interface and Context Choices Change Outcomes

Yang et al. designed an agent-computer interface for repository work and evaluated it on SWE-bench. The interface supplied purpose-built file viewing, editing, search, and feedback rather than exposing an unstructured shell alone. The paper reports 12.47 percent resolution on the full 2,294-task SWE-bench test set and 18.00 percent on the 300-task Lite split for SWE-agent with GPT-4 Turbo. More important for harness design, its ablations changed individual interface and context choices while holding the general system fixed. [8]

The ablations found that a 100-line file view outperformed both a 30-line view and full-file display in the reported setting; keeping the last five observations outperformed full history for the default comparison; summarized search outperformed iterative search; and removing edit-time linting reduced the result. These findings show that more context and more general interfaces are not automatically better. The harness shapes what the model can perceive, how errors become feedback, and how much stale material competes for attention. [8]

### The Scaffold Effect: Harness Choice Changes Cost and Failure Shape

Vats and Golev evaluated two models across three open-source coding harnesses -- Goose, OpenCode, and OpenHands-SDK -- on a stratified 50-task subset of Terminal-Bench Pro. Their controlled comparison measured pass rate, token consumption, turns, idle behavior, and failure categories. The work appears in the ICML 2026 virtual program, while the cited arXiv record remains version 1. Its 50-task sample is deliberately small, and the authors report that most paired pass-rate differences are not statistically distinguishable from zero at that sample size; the results are therefore bounded evidence rather than a universal harness ranking. [9]

The authors report paired pass-rate differences of zero to eight percentage points within a model, but up to a 40-fold difference in tokens per solved task across harnesses. They also found harness-specific failure fingerprints that repeated across models: reasoning-dominated failures for Goose, verification or maximum-turn failures for OpenHands-SDK, and timeout or idle-loop behavior for OpenCode. This evidence supports evaluating the harness-model pair and recording resource and failure metrics alongside success rate. It does not prove that one harness is universally superior outside the sampled tasks. [9]

### Anthropic Managed Agents: Externalized State Enables Independent Recovery

Anthropic's production case began with the session, harness, and sandbox in one container. The reported operational problem was coupled failure: a stuck or failed container could make session recovery and diagnosis difficult, while the runtime assumed that all resources lived beside the harness. The redesign separated an append-only session log, stateless harness processes, and provisionable execution environments behind interfaces. [5]

In the resulting design, a sandbox failure becomes a tool-call error and a replacement environment can be provisioned. A harness failure can be recovered by starting another harness, loading the session event log, and resuming from the last event. Demand-driven sandbox provisioning produced the vendor-reported time-to-first-token reductions described earlier. The method is an implementation case rather than an independent experiment, but it supplies concrete evidence that durability and execution need not share a process lifetime. [5]

### Anthropic Long-Running Agents: Artifacts Bridge Context Windows

Anthropic tested a two-role harness for application development: an initializer configured the environment and durable task artifacts, while later coding sessions made incremental progress and left structured updates. The artifacts included a feature ledger, progress notes, git history, an initialization script, and end-to-end tests. The authors observed common failures before these controls, including one-shot attempts, undocumented partial work, premature completion, and features marked complete without adequate testing. [6]

Their reported finding was qualitative: incremental feature work, explicit progress artifacts, clean commits, and browser-based verification made fresh sessions better able to continue the project and detect broken state. The case does not provide a controlled benchmark or universal effect size. Its contribution is a testable architecture for continuity: every new session can inspect durable evidence, select unfinished work, verify the baseline, make one bounded change, and leave a recoverable checkpoint. [6]

### Convergent Runtime Decompositions

Independent framework documentation converges on similar responsibilities. Microsoft lists model connection, function invocation, history persistence, compaction, context providers, approvals, observability, and bounded looping. OpenAI documents the loop, state continuation, pauses, tool errors, and specialist handoffs. LangChain separates transient model context from persistent tool and lifecycle context. A 2026 source-code study of eleven production coding harnesses further reports recurring subsystems and design patterns across independently developed systems. [1][3][4][11]

This convergence is architectural evidence, not proof that one decomposition is complete. Framework vendors may describe systems in terms that fit their own products, and the source-code study reports a fast-moving ecosystem. The conservative conclusion is that loop control, context, tools, state, verification, safety, and evidence recur because long-running tool use repeatedly creates those responsibilities. Their recurrence across independently designed systems supports treating them as explicit engineering concerns rather than incidental prompt features. The exact interface boundaries should still be tested against the target task and failure model. [1][3][4][11]

## Implications

### For Agent Builders: Design the State Machine Before the Prompt

The first implementation artifact should be a lifecycle diagram or transition table, not a long system prompt. Define the run states, legal transitions, side effects, stop conditions, retry classes, approval pauses, and evidence required for success. Then decide which transitions the model may propose and which the runtime alone may authorize. This makes the worst failure visible: an ambiguous transition that performs an external action without a durable record or enforceable policy. The author's recommendation follows the explicit loop and pause semantics in Microsoft and OpenAI's runtimes. [1][3]

Keep the minimum viable loop small. A useful baseline can assemble a request, call one model, validate one tool schema, execute through a controlled dispatcher, append an event, and stop on a finite set of conditions. Add retrieval, multi-agent delegation, self-improvement, or dynamic routing only when an observed failure requires them. Anthropic's engineering guidance recommends simple designs, transparent planning, and carefully tested agent-computer interfaces, while Microsoft makes advanced features such as background agents and looping optional. [1][2]

### For Context Engineers: Preserve the Difference Between Record and View

Treat durable state as the source of truth and each prompt as a derived view. Store events, artifacts, approvals, and checkpoints in forms that survive process replacement. Build the model context from that state using a documented policy for selection, ordering, trimming, and compaction. If a summary replaces original messages in the authoritative store, state clearly that information has been discarded; if recovery and audit matter, retain the original outside the prompt view. [4][5]

Context quality should be evaluated empirically. SWE-agent's ablations show that a full file or full history can perform worse than a bounded view, while Anthropic's long-running case shows that compaction alone does not provide project continuity. Measure task success, retrieval misses, stale-context errors, token use, and recovery quality as the context policy changes. Do not infer quality from window utilization. [6][8]

### For Tool and Platform Teams: Make Dispatch a Governed Service Boundary

Each tool should have a typed request, typed result, declared side effects, authorization rule, timeout, retry policy, and idempotency behavior. The dispatcher should resolve tools by stable identity, validate arguments, obtain narrowly scoped credentials, enforce approvals, and record the execution result. Tool output should return enough evidence for the model to adapt without flooding context. These controls belong in runtime code because the same model that proposes an action cannot be the sole authority that permits it. [1][4][5]

Platform teams should expose failures in categories the agent can use. A timeout, invalid argument, permission denial, unavailable dependency, failed precondition, and partial success require different next actions. Error strings without stable codes force the model to infer operational meaning from prose. The author's synthesis is that structured failure is a capability: it lets the harness select a bounded recovery path and lets evaluation count which layer is failing. [3][8][9]

### For Reliability Engineers: Test Resume, Not Only Success

A robust agent should be tested under injected failures. Kill the harness after a recorded model decision, interrupt a tool after an uncertain side effect, expire an approval, return malformed tool output, overflow the context budget, and restart the execution environment. For each case, verify whether the task resumes from a committed checkpoint, repeats an action safely, or terminates with an explicit status. Anthropic's separation of session, harness, and sandbox supplies one concrete recovery model; OpenAI's paused-run semantics supply another. [3][5]

Recovery budgets should be observable and finite. Track retries by class, repeated equivalent actions, backtracks, time spent waiting for approval, tool error rates, and terminal reasons. A task that eventually succeeds after uncontrolled looping may be economically or operationally unacceptable. The scaffold-effect study shows that harnesses can produce similar pass rates with radically different token costs and characteristic failures, so reliability reporting should include efficiency and failure shape, not only completion. [9]

### For Security Engineers: Put Authority Outside Generated Text

The harness is where model proposals meet credentials, files, networks, and external systems. Security review should trace every path from model output to side effect and verify that it crosses schema validation, policy, credential scope, sandbox, and audit boundaries appropriate to the action. Anthropic's Managed Agents design keeps credentials outside the execution sandbox and uses proxies or resource-bound authentication so generated code need not access long-lived tokens. [5]

Approval is a state transition, not a chat message. Bind an approval to the exact task, action, target, arguments, policy version, reviewer, and expiration. Persist the pending state before waiting, and revalidate the world before execution. If the action changes, approval should not silently follow it. This design also permits a replacement harness to resume the same approved or pending action without reconstructing authority from natural-language history. [1][3][5]

### For Evaluators: Report the Harness as Part of the System

A benchmark result should identify the model, harness version, tool set, context policy, environment, stop limits, retry policy, and verification method. The scaffold-effect study shows that model-only labels can conceal major differences in resource use and failure behavior. SWE-agent shows that seemingly small interface choices alter performance. A result without the harness specification is therefore incomplete evidence about a deployed agent. [8][9]

Evaluation should include trajectory and system metrics: success, token and monetary cost, wall-clock latency, tool calls, invalid calls, idle turns, approval burden, recovery count, side-effect errors, and terminal reason. Use traces first to discover recurring failure classes, then convert those classes into repeatable evaluations. OpenAI's observability guidance explicitly connects tracing with later workflow evaluation. [10]

### For Product and Operations Teams: Expose Progress and Control

The user interface is part of the harness because it displays progress, requests approvals, accepts cancellation, and communicates whether a run completed, paused, or failed. Microsoft separates application UX from the underlying agent while still treating streaming, progress, and approval collection as harness responsibilities. A useful interface should show the current task state and evidence without requiring the user to parse raw model messages. [1]

Long-running work needs durable status that is meaningful after the original process disappears. A task ledger, progress file, event stream, or equivalent projection should answer what has been attempted, what passed verification, what remains, and what requires intervention. Anthropic's two long-running cases show both lightweight file-based and service-based forms of this principle. The author's assessment is that status should be generated from committed runtime state rather than from a model's narrative summary alone. [5][6]

### For Architecture Selection: Prefer Reversible Boundaries

The simplest deployable harness is usually better than a platform assembled from every available feature. Add a separate service when trust, durability, scale, or restart behavior requires it. Keep components local when splitting them would add failure modes without isolating anything important. Anthropic's managed design justifies separate session and sandbox interfaces because their persistence, security, and failure lifecycles differ; a small local agent may satisfy the same invariants with an append-only file and a child process. [5]

Choose boundaries that can evolve without rewriting the task model. Model providers, context strategies, tool implementations, and sandboxes will change. Stable request, event, tool, policy, and artifact contracts make those substitutions reversible. The author's synthesis is that the harness should be opinionated about invariants -- typed actions, durable state, bounded loops, enforceable authority, and verified completion -- while remaining flexible about the implementation behind each interface. [1][5]

### A Minimum Review Checklist

Before deploying a harness, answer these questions with executable evidence:

1. What are the loop states and every terminal condition?
2. Which store is authoritative after a crash or worker replacement?
3. How is each model context derived from durable state?
4. Where are tool names, arguments, permissions, and side effects validated?
5. Which actions are idempotent, compensating, approval-bound, or prohibited?
6. How are failures classified, budgeted, retried, backtracked, or escalated?
7. What independent evidence establishes completion?
8. Can a trace reconstruct the first divergent step without exposing secrets?
9. Can the harness, sandbox, or model provider be replaced without losing task state?
10. Do evaluations report cost, latency, failure shape, and the exact harness configuration?

This checklist is the author's synthesis of the runtime responsibilities and failure evidence in the cited sources. A harness that cannot answer one of these questions may still run a demonstration, but the unanswered question identifies where a production failure can become ambiguous, unrecoverable, or unsafe. [1][3][4][5][6][8][9][10]

## Sources

1. Microsoft. "Agent Harness." Microsoft Agent Framework documentation. Defines harness architecture, sessions, compaction, approvals, observability, and bounded looping.
   https://learn.microsoft.com/en-us/agent-framework/concepts/harness [high]

2. Anthropic. (2024). "Building Effective Agents." Official engineering guidance on agent loops, tool design, simplicity, and agent-computer interfaces.
   https://www.anthropic.com/engineering/building-effective-agents [high]

3. OpenAI. "Running Agents." Official Agents SDK documentation for the model-tool loop, continuation strategies, pauses, failures, and stop behavior.
   https://developers.openai.com/api/docs/guides/agents/running-agents [high]

4. LangChain. "Context Engineering in Agents." Official documentation on model context, tool context, lifecycle context, state, stores, middleware, and dynamic tool selection.
   https://docs.langchain.com/oss/javascript/langchain/context-engineering.md [high]

5. Anthropic. (2026). "Scaling Managed Agents: Decoupling the Brain From the Hands." Production architecture case separating session, harness, and sandbox interfaces.
   https://www.anthropic.com/engineering/managed-agents [high]

6. Anthropic. (2025). "Effective Harnesses for Long-Running Agents." Engineering case on initializer sessions, progress artifacts, incremental work, git checkpoints, and end-to-end verification.
   https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents [high]

7. Yao, S., Zhao, J., Yu, D., et al. (2023). "ReAct: Synergizing Reasoning and Acting in Language Models." ICLR 2023.
   https://arxiv.org/html/2210.03629 [high]

8. Yang, J., Jimenez, C. E., Wettig, A., et al. (2024). "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering." arXiv:2405.15793.
   https://arxiv.org/html/2405.15793 [high]

9. Vats, N., and Golev, O. (2026). "The Scaffold Effect in Coding Agents: Harness Choice as a Hidden Variable in Coding-Agent Evaluation." ICML 2026; arXiv:2607.22585, version 1.
   https://icml.cc/virtual/2026/82739
   https://arxiv.org/abs/2607.22585v1 [high]

10. OpenAI. "Integrations and Observability." Official Agents SDK documentation for MCP integration, runtime boundaries, and tracing of model calls, tools, handoffs, and guardrails.
    https://developers.openai.com/api/docs/guides/agents/integrations-observability [high]

11. Barbaste, P., Darrigol, T., Vu, G., and Wiltberger, T. (2026). "Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents -- A Source-Code Study of Eleven Systems." arXiv:2609.00006.
    https://arxiv.org/html/2609.00006 [high]

## See Also

- `library/coding-agentic-ai/tool-use-and-function-calling.md` -- the structured proposal-execution-observation boundary managed by the harness.
- `library/coding-agentic-ai/context-window-management.md` -- the context selection and compaction policies executed on each loop iteration.
- `library/coding-agentic-ai/agent-memory-and-persistence.md` -- state layers that preserve knowledge and task continuity beyond a model call.
- `library/coding-agentic-ai/agent-observability-and-debugging.md` -- traces and spans that make harness behavior inspectable.
- `library/coding-agentic-ai/agent-sandboxing-and-security.md` -- execution isolation and permission boundaries outside model control.
- `library/coding-agentic-ai/agent-evaluation-and-benchmarking.md` -- why models must be evaluated together with the harness that runs them.
- `library/coding-agentic-ai/anchor-coding-agentic-ai.md` -- the domain anchor placing harness design inside agent engineering.
