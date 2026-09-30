---
name: agent-observability-and-debugging
id: 20260827T200233Z
tier: library-topic
domain: coding-agentic-ai
author: Librarian
tags: [agent-observability, agent-debugging, tracing, spans, opentelemetry, replay-debugging, failure-taxonomy, langsmith]
links: [library/coding-agentic-ai/agent-evaluation-and-benchmarking.md, library/coding-agentic-ai/multi-agent-orchestration.md, library/coding-agentic-ai/tool-use-and-function-calling.md, library/coding-agentic-ai/context-window-management.md]
reviewed: 2026-09-30
---

# Agent Observability and Debugging -- A Trace Makes Agent Failure Inspectable, Not Self-Explanatory

Agent observability records the observable execution of an agent -- model calls, tool calls, retrievals, handoffs, guardrails, timing, usage, errors, and selected inputs and outputs -- so operators can inspect how a run unfolded. A useful trace narrows the search for a failure, but it does not automatically expose hidden model reasoning, prove the root cause, reproduce a changing environment, or establish that the final answer was correct [2][4][8][9].

## Background

Modern agent tracing inherits its basic data model from distributed systems. Google's Dapper report described a trace as a set of causally related spans sharing a trace identifier; each span carried its own identifier, a parent identifier, a human-readable name, timing, and optional annotations. Dapper propagated trace context through common RPC and control-flow libraries, then sampled traces to keep overhead and storage manageable. The report is important because it established both the value and the limits of the model: a trace can reconstruct an observed request path, but instrumentation coverage and sampling determine which paths are available for inspection [1].

Agent systems reuse this model because one user request may cross a model provider, retriever, tool server, sandbox, database, guardrail, and one or more agents. The OpenAI Agents SDK, for example, represents a workflow as a trace and instruments runner tasks, model turns, agent invocations, generations, function calls, guardrails, handoffs, and audio operations as spans. LangSmith uses different names for a similar hierarchy: one unit of work is a run, the runs for one operation form a trace, and traces from a multi-turn session can be grouped into a thread [4][5]. These implementations make the execution path queryable without requiring each application to invent an unrelated log format.

The agent-specific difficulty is not that conventional software is always deterministic. Distributed systems already contain concurrency, retries, partial failure, and changing external state. Agent systems add model sampling, natural-language state, dynamically selected tools, variable retrieval results, and semantically wrong actions that may complete without a software exception. Two runs with the same nominal request can therefore differ in both path and result. The author's synthesis is that agent debugging needs two kinds of evidence together: operational telemetry that shows whether components ran, and semantic evidence that shows whether the selected action, arguments, evidence, and answer were appropriate [8][9][13].

This distinction corrects a common observability overclaim. A trace records what the instrumentation emitted. It is not necessarily a complete transcript. Dapper sampled whole traces; OpenAI permits tracing to be disabled per run and permits sensitive model and tool payloads to be omitted; LangSmith imposes a maximum of 25,000 runs per trace; OpenTelemetry warns that payload fields may contain personal or otherwise sensitive information [1][4][5][16]. A trace can also omit an uninstrumented custom step, lose spans during export, or retain metadata while deleting content. Completeness is therefore a testable property of a telemetry design, not a synonym for the word trace.

The vocabulary is also still evolving. OpenTelemetry moved its Generative AI semantic conventions into a dedicated repository. The current agent document defines conventions for agent creation, client and internal agent invocation, workflow invocation, planning, tool execution, skill loading, skill-resource access, and command execution, but the documented attributes and operation names remain at Development stability [2]. The associated reference project tests real Python libraries against deterministic local mock servers and reports coverage across frameworks for inference, retrieval, internal agent invocation, workflow invocation, planning, memory, and tool execution [3]. This is evidence of active convergence, not evidence that every backend or framework emits an identical stable schema.

Research has begun to use traces as data rather than only as user-interface artifacts. MAST analyzed multi-agent execution traces to build a 14-mode failure taxonomy spanning system design, inter-agent misalignment, and task verification [8]. Who&When treated failure attribution as a separate problem: given a failed execution log, identify the responsible agent and decisive step [9]. TraceElephant then compared partial logs with fuller traces containing inputs, outputs, metadata, tool and environment interactions, and agent configurations [10]. These studies support a narrow conclusion: richer execution records improve the material available for diagnosis. They also show that diagnosis remains difficult even when records are available.

Observability also serves governance. NIST AI 600-1 recommends retention policies that preserve history for testing, evaluation, validation, and verification, together with monitoring, incident review, version history, and documentation practices. Those recommendations do not prescribe a particular tracing vendor or schema. They establish why an organization needs evidence that survives a single debugging session: incident response, change analysis, and risk management depend on records whose origin, access, and retention are controlled [11].

The author's synthesis is that the resulting discipline is broader than opening a trace viewer after a failure. It includes deciding what events must be observable, assigning stable identities, preserving causal relationships, protecting sensitive content, measuring coverage and loss, retaining representative failures, and connecting diagnosis to a verified correction. The core engineering question is not "Do we have traces?" It is "Can the available records support the specific conclusion we need to reach?"

## Core Concepts

### Trace, Span, Thread, and Trajectory

A trace is the bounded record for one logical operation. A span is one timed operation inside that trace. Parent-child identifiers organize nested work: a workflow span can contain an agent span, which contains a model-generation span, which is followed by a tool-execution span. Attributes add operation-specific evidence such as model name, token usage, tool name, arguments, result status, error type, and deployment version [1][2][4]. The hierarchy answers temporal and structural questions: which operations ran, in what order, under which parent, for how long, and with what recorded metadata.

A thread groups traces from one multi-turn session. A trajectory is the ordered sequence of observable messages, actions, tool results, and environment observations produced during execution. LangSmith explicitly distinguishes a nested trace from a flattened trajectory view over a thread [5]. Research papers often use trajectory where product documentation uses trace or execution log. The terms overlap but should not be collapsed. A trace emphasizes telemetry structure; a trajectory emphasizes the sequence evaluated as agent behavior.

The run boundary must be defined before instrumentation. One trace may represent one user turn, one job, one workflow, or one scheduled task. If the boundary is inconsistent, latency, token, and success metrics become incomparable. Stable correlation fields should identify the application, agent or workflow version, environment, tenant or test cohort where permitted, model configuration, and evaluation or release identifier. These fields make it possible to separate a prompt regression from a provider incident or a deployment change. This paragraph is the author's operational synthesis of the trace metadata exposed by OpenAI, LangSmith, and OpenTelemetry [2][4][5].

### The Minimum Observable Event Model

A useful agent trace normally needs more than model spans. The current OpenTelemetry GenAI conventions include agent and workflow invocations, plans when an instrumentation can reliably distinguish planning, tool execution, skills, and command execution. OpenInference separately defines span kinds for LLM calls, embeddings, chains, retrievers, rerankers, tools, agents, guardrails, evaluators, and prompts [2][14]. These schemas differ, but both recognize that an agent run is a graph of heterogeneous operations rather than one completion request.

At minimum, a production event model should represent the root workflow; every model request and response that policy permits recording; tool selection, arguments, result status, and errors; retrieval query and document identifiers; handoffs or delegated work; guardrail verdicts; approvals; state transitions; and the final externally visible outcome. It should also record timing and usage at a granularity that permits a slow or expensive branch to be isolated. The OpenAI Agents SDK's default spans and the Microsoft Agent Framework's workflow, executor, edge, and message spans provide concrete implementations of this model [4][15].

Instrumentation must cover application-owned code as well as framework-owned calls. Auto-instrumentation can capture supported model and framework operations, but custom routing, caching, transformation, policy checks, sandbox work, and state mutation may remain invisible unless the application emits custom spans. LangSmith exposes decorators, context managers, and a lower-level run-tree API for this purpose; OpenAI exposes custom spans and custom trace processors [4][5]. A trace with excellent model-call detail but no record of the application decision that selected those calls can still miss the decisive step.

### Causality Is More Than a Timestamp

Chronological order shows what happened first, not necessarily what caused what. Parent-child spans express nested execution, and Dapper's trace, span, and parent identifiers reconstruct the causal structure of RPC trees [1]. Agent workflows can also be asynchronous or many-to-one. Microsoft Agent Framework documents a case in which a target executor span is linked to a source message span rather than made its child, because message delivery establishes causality without a nested call relationship [15]. A practical schema therefore needs parentage for nested work and links or explicit artifact identifiers for non-nested dependencies.

Tool outputs and retrieved documents should carry identifiers that later spans can reference. If an answer cites a retrieved document, the trace should make that dependency inspectable. If a tool result is summarized before reaching another agent, the record should distinguish the original result from the transformed message. The author's synthesis is that provenance edges are often more useful than raw chronology: they show which evidence, state, or message a later decision actually consumed.

### Observable Reasoning Is Not Hidden Reasoning

A trace may store the prompt sent to a model, the returned message, declared tool calls, tool results, and framework state. It does not thereby reveal every internal computation that produced the model output. Documentation that labels a user-interface panel as reasoning or trajectory should not be interpreted as access to an unobserved internal chain of thought. The defensible term is observable trajectory: the sequence of recorded inputs, outputs, actions, and state changes [4][5][12].

The author's synthesis is that this boundary matters during root-cause analysis. A model may emit a wrong tool argument because relevant context was absent, because conflicting instructions were present, because the model made an error despite adequate context, or because an earlier transformation corrupted a value. The trace can test the first two possibilities if it records the prompt-as-sent and transformation path. It usually cannot prove a private mental cause. Diagnosis should name the first observable divergence and the evidence supporting it, then distinguish that from speculation about hidden reasoning.

Content capture is also optional for good reasons. The OpenAI Agents SDK can omit generation and function inputs and outputs when sensitive-data capture is disabled. OpenTelemetry advises implementers to minimize collection and treat privacy compliance, consent, protection, and storage as their responsibility [4][16]. A system should never claim complete semantic observability if policy intentionally excludes the content needed for semantic review. It should instead state which classes of diagnosis remain possible from metadata alone.

### Outcome, Process, and State Must Be Evaluated Separately

A successful HTTP response or completed span does not show that the agent completed the task correctly. Agent evaluation can operate at three levels. Outcome evaluation checks the final answer or external state. Process evaluation checks tool selection, arguments, order, handoffs, policies, and evidence use. Operational evaluation checks latency, errors, tokens, cost, retries, and saturation. OpenAI's agent-evaluation guidance uses traces for workflow-level questions such as whether the right tool was selected, whether a handoff occurred, or whether a policy was violated, then uses datasets and evaluation runs for repeatable comparisons [13].

All three levels are necessary because they can disagree. A run may reach the right answer through a prohibited or fragile path. A run may follow the intended process but fail because an external service returned stale data. A run may be semantically correct but too slow or costly for its service objective. The trace should preserve the evidence for each verdict rather than compress them into one success flag. The author's synthesis is that a production dashboard should never allow operational success to masquerade as task correctness.

### Failure Taxonomy and Attribution

A failure taxonomy gives reviewers consistent labels for recurring patterns. MAST derived 14 failure modes from multi-agent traces and grouped them into system-design problems, inter-agent misalignment, and task-verification failures [8]. A taxonomy makes aggregate analysis possible: teams can count repetition, instruction noncompliance, information withholding, reasoning-action mismatch, or premature termination rather than treating every incident as unique.

Classification is not the same as attribution. Attribution asks which agent and which step made the decisive error. Who&When showed that this remains difficult: its best reported method identified the responsible agent much more accurately than the exact decisive step [9]. The practical implication is that a trace viewer should support evidence-linked hypotheses, not pretend that the deepest red span is automatically the root cause. An exception may be the symptom of an earlier malformed request; a wrong final answer may result from an early retrieval omission that never produced an exception.

The author's synthesis is that a disciplined debugging record should distinguish four fields: symptom, first observable divergence, attributed cause, and corrective action. The symptom is what failed. The first divergence is the earliest recorded step that conflicts with requirements or a known-good run. The attributed cause is the explanation supported by the available evidence. The corrective action is the change intended to prevent recurrence. These fields can be revised independently when new evidence appears.

### Sampling, Coverage, and Telemetry Quality

Sampling is not merely a cost control; it changes which conclusions the data can support. Dapper sampled whole traces by a decision based on the trace identifier, preserving internal trace structure while reducing volume [1]. The author's synthesis is that a modern policy may sample by rate, error, latency, tenant, cost, or policy. Head sampling decides before the outcome is known; tail sampling can retain traces after observing error or latency but requires buffering. Whatever the strategy, the system should record or document inclusion rules so an operator does not treat a biased sample as the full workload.

Coverage has several dimensions: span coverage, field coverage, delivery coverage, and population coverage. Span coverage asks whether every required operation type is instrumented. Field coverage asks whether a span contains the identifiers and values needed for diagnosis. Delivery coverage asks whether emitted spans reached durable storage. Population coverage asks which runs were sampled or excluded. The OpenTelemetry GenAI reference project is useful because it tests semantic-convention coverage across real libraries; its matrix also demonstrates that support differs by operation and framework [3].

Telemetry should itself have reliability indicators. Export failures, dropped-span counts, queue saturation, schema-version mismatches, redaction failures, and clock problems should be monitored. Otherwise, absence of evidence is easily misread as evidence that an operation did not occur. The author's synthesis is that an observability system needs observability of its own collection path before its records can be treated as complete.

### Replay, Re-execution, and Counterfactual Testing

Replay is an overloaded word. Microsoft Foundry's Trace Replay is a viewer that lets an operator navigate recorded spans, switch between user and trajectory views, inspect model and tool steps, filter by span type or token use, and play through the recorded interaction [12]. This is playback of recorded evidence. It is useful for orientation, but it is not proof that the original environment can be recreated.

The author's synthesis is that re-execution is different from playback because it runs code again. It may differ because the model samples differently, a retrieval index changed, an API returned new data, credentials or permissions changed, time advanced, or the original side effect cannot safely be repeated. Deterministic record/replay requires freezing or substituting every relevant external input and controlling side effects. A trace that stores inputs and outputs can support mocks or fixtures, but trace presence alone does not establish replay fidelity.

Counterfactual testing changes one input or component and observes the result. TraceElephant reports a dynamic setting in which static traces were supplemented by controlled re-execution and probing [10]. That method can strengthen an attribution, but it remains specific to the benchmark's replayable environments. Production systems should label whether a debugging tool is showing recorded playback, live re-execution, mocked replay, or a counterfactual experiment.

### Privacy, Security, and Retention

Agent traces may contain system instructions, user content, retrieved documents, credentials accidentally placed in prompts, tool arguments, tool results, and internal business data. OpenTelemetry explicitly places responsibility for sensitive-data decisions on the implementer and provides collector processors for attribute removal, filtering, redaction, and transformation [16]. OpenAI warns that generation and function spans can include sensitive inputs and outputs and provides configuration to omit them [4]. Microsoft similarly warns that enabling sensitive workflow telemetry includes raw messages and executor inputs and outputs [15].

Data minimization should precede redaction. If a field is unnecessary for a defined diagnostic purpose, do not collect it. If content is necessary, separate metadata-only telemetry from restricted payload storage, apply access control, encrypt transport and storage, set a retention period, audit reads, and test the redaction path. OpenAI's documentation further notes that when export must depend on successful redaction, redaction and delivery should be composed so a redaction failure discards the batch rather than leaking the unredacted payload [4].

Retention must match purpose and current platform behavior. As of the review date, LangSmith documents base trace retention of 14 days and extended retention of 180 days, with some evaluation and automation actions capable of upgrading a trace's tier; datasets persist independently of source-trace retention [7]. That example shows why a topic should not state one timeless vendor retention period. Teams need an explicit local policy aligned with legal obligations, incident needs, evaluation datasets, and deletion verification [7][11].

## Evidence

### Distributed Tracing Established the Structural Model

Dapper was a production experience report, not a controlled trial of agent debugging. Google instrumented common RPC, threading, and control-flow libraries, propagated trace context, represented requests as trees of spans, and sampled to manage overhead. The report describes more than two years of deployment experience and emphasizes low overhead, application transparency, and usefulness to development and operations teams [1]. Its direct contribution to agent observability is structural: trace identifiers, span identifiers, parent relationships, timing, annotations, and sampling remain the foundation of later agent telemetry.

The limits transfer as well. Dapper's instrumentation strategy worked because common libraries covered much of Google's request path; it did not imply that every arbitrary application action was visible. Its sampling design deliberately omitted many traces. Agent systems inherit the same dependency on coverage and add semantic payloads that can be larger and more sensitive [1][4][16]. Dapper therefore supports the trace model, not the claim that a trace is automatically complete or sufficient for diagnosis.

### MAST Turned Execution Traces Into a Failure Dataset

Cemri and colleagues published MAST in the NeurIPS 2025 Datasets and Benchmarks Track. The final paper reports MAST-Data as 1,642 annotated execution traces from seven multi-agent frameworks over coding, mathematics, and general-agent tasks. The taxonomy-development stage used an initial 150 traces from five frameworks examined by six human experts with grounded-theory procedures. Inter-annotator agreement was iteratively checked by three experts on subsets of five traces per round, reaching Cohen's kappa of 0.88. The resulting taxonomy contains 14 modes in three categories: system design, inter-agent misalignment, and task verification [8].

These details correct two possible misreadings. First, the kappa statistic was not computed by independently relabeling all 1,642 traces. Second, the taxonomy-development sample and the final scaled dataset are different stages. The authors used an LLM annotator to scale labeling after the human taxonomy work [8]. MAST provides a disciplined vocabulary and a large corpus, but it does not show that a generic tracing platform can infer root causes automatically or that the reported failure frequencies transfer unchanged to every deployment.

### Who&When Measured the Difficulty of Exact Attribution

Zhang and colleagues presented Who&When at ICML 2025. The dataset contains 184 failure-annotation tasks drawn from 127 algorithm-generated and hand-crafted multi-agent systems. Human experts labeled the failure-responsible agent and decisive error step. The study evaluated all-at-once, step-by-step, and binary-search attribution methods under different information conditions and model choices [9].

The abstract's headline result is a best agent-level accuracy of 53.5 percent and a best exact step-level accuracy of 14.2 percent. In the GPT-4o experiments, methods also traded off context breadth and localization: all-at-once generally did better at identifying the responsible agent, while incremental processing often did better at locating a step. Performance declined as failure logs became longer, with step-level attribution more sensitive to length [9].

The evidence supports a bounded conclusion. Execution logs enable attribution research, but possessing a log does not make the decisive step obvious. Results depend on trace content, system type, context length, ground-truth availability, model, prompting method, and the benchmark's single decisive-error labeling. Operators should therefore treat automated attribution as a hypothesis generator unless a deterministic check or expert review confirms the causal claim [9].

### TraceElephant Tested Richer Observability and Replayable Environments

Chen and colleagues' TraceElephant was accepted by ACL 2026 and is available as arXiv:2604.22708. The benchmark collected 380 traces from Captain-Agent, Magentic-One, and SWE-Agent over GAIA, AssistantBench, and SWE-Bench tasks; 220 traces were failures. Each record included agent actions, natural-language inputs and outputs, tool and environment interactions, agent configuration, and an executable environment [10].

In the reported comparison, fuller static traces improved agent-level and step-level attribution over an output-only condition; the paper states a 76 percent relative improvement in step-level accuracy. Its dynamic condition, which added controlled re-execution and counterfactual probing, improved step-level attribution by a further 10 percent relative to its static setting. Absolute accuracy remained limited: the paper reports 65.9 percent agent-level and 30.3 percent step-level accuracy in the full-trace setting [10].

The study directly supports two design choices: preserve inputs as well as outputs, and keep a replayable environment when safe and feasible. It also reinforces the boundary between evidence and explanation. More complete traces improved attribution, but did not produce near-perfect localization. Because the systems, tasks, attribution labels, and probing budget are benchmark-specific, the percentages should not be generalized to unrelated production fleets [10].

### Current Implementations Show Both Coverage and Fragmentation

The OpenAI Agents SDK is a concrete case of framework-level auto-instrumentation. Its documented default hierarchy covers the overall runner, runner tasks, model turns, agent invocations, generations, function calls, guardrails, handoffs, and audio spans. The same documentation exposes custom processors, per-run disabling, sensitive-data controls, and alternative exporters [4]. This demonstrates that detailed tracing can be a runtime property rather than repeated application code.

OpenTelemetry provides a cross-framework direction rather than one vendor data store. Its GenAI agent conventions define shared operation names and attributes, and its reference project exercises libraries against mock services and reports which span types each library emits. The current matrix includes broad inference and tool coverage but narrower coverage for planning, memory, retrieval, and workflow spans [2][3]. That uneven matrix is evidence against claiming universal schema completeness.

LangSmith demonstrates a product-specific model of runs, traces, threads, and trajectories and accepts OpenTelemetry data through OTLP and collectors [5][6]. OpenInference defines a parallel AI-specific semantic convention on top of OpenTelemetry, including span kinds for LLMs, tools, agents, retrievers, guardrails, and evaluators [14]. These implementations agree on the need for structured operations and parent-child relationships, but their field names and coverage are not identical. Interoperability therefore requires tested mappings and versioned schemas, not merely the claim that two systems both use OpenTelemetry.

### Governance Sources Establish the Record-Keeping Obligation

NIST AI 600-1 recommends policies for monitoring, after-action review, incident response, and retaining history for testing, evaluation, validation, and verification. It also links documentation, logging, version history, and provenance to incident analysis and information sharing [11]. This is not empirical evidence that one trace design improves model quality. It is authoritative governance evidence that operational records need ownership, retention rules, and review procedures.

The combined evidence does not support the strongest version of the original thesis -- that a trace makes every failure understandable. It supports a more precise claim: structured, sufficiently complete, and protected traces make failures inspectable; richer records improve attribution; exact root-cause diagnosis remains a separate analytical task [8][9][10].

## Implications

### For Agent Engineers: Debug the First Observable Divergence

A practical debugging sequence begins with the user-visible symptom and works backward through the trace. Confirm the expected outcome and the actual external state. Identify the first span whose input, output, action, or missing action conflicts with the requirement. Compare the prompt-as-sent with the intended context, then inspect retrieval results, tool arguments, tool outputs, handoffs, guardrails, and transformations upstream of that point. This sequence uses the trace to localize evidence without claiming access to hidden reasoning [4][5][9].

The author's synthesis is that the first red or failed span is not necessarily the first divergence. A tool exception may result from an argument corrupted three steps earlier. A wrong answer may contain no exception. A timeout may be downstream of an unnecessary loop. Engineers should record both the symptom span and the earliest supported divergence, then state the causal inference and its uncertainty. Where possible, a deterministic assertion, unit test, sandbox replay, or controlled counterfactual should test the proposed cause.

Every fix should produce a regression artifact. For deterministic behavior, that may be a unit or integration test. For stochastic or semantic behavior, it may be a dataset case with an outcome grader, a trajectory constraint, and repeated runs across relevant configurations. OpenAI's evaluation guidance explicitly separates trace inspection for early debugging from datasets and evaluation runs for repeatable comparison [13]. A repaired example is not evidence that a distributional failure is solved unless the evaluation covers the affected distribution.

### For Harness Designers: Make Required Controls Visible

Critical controls should emit explicit spans or events. Approval requests, policy decisions, budget checks, verification gates, and handoffs should record their input identity, verdict, and outcome without exposing unnecessary sensitive content. If a gate is absent from the trace, an operator cannot distinguish "the gate passed" from "the gate never ran." OpenAI and Microsoft both model guardrail, handoff, executor, and message operations as observable units [4][15].

Record versioned identities for prompts, tools, schemas, policies, models, retrievers, indexes, and agent builds. Storing the entire prompt may help one incident but creates privacy and retention costs; a content hash plus a versioned artifact can often establish identity, while restricted payload capture can be enabled only for authorized cases. The author's synthesis is that an observability contract should list each required span type, mandatory metadata, optional payload, redaction rule, and retention tier before implementation.

Handoffs deserve special treatment. A handoff record should show the sender, receiver, declared task, transmitted context, expected return contract, and completion status. It should also preserve links to the source artifacts that informed the handoff. Multi-agent taxonomies and attribution studies show why: system-level failure can emerge from coordination and verification even when each component completes its local call [8][9].

### For Evaluation Teams: Use Traces as Cases, Not as Verdicts

Production and test traces reveal real paths, including unexpected tools, retries, missing checks, and costly loops. These traces can seed evaluation datasets and failure taxonomies. However, selection must be explicit. A dataset built only from reported failures overrepresents visible incidents; a dataset built only from sampled normal traffic may miss rare high-severity behavior. Sampling rules, cohort definitions, and label procedures should accompany the dataset [1][8][9].

Outcome and trajectory graders should remain separate. The outcome grader asks whether the task succeeded. A trajectory grader asks whether the process satisfied requirements such as tool restrictions, approval order, evidence use, or bounded work. A cost or latency check asks whether the service objective was met. A run can pass one and fail another. Keeping these labels separate makes regressions actionable and prevents a single aggregate score from hiding a dangerous path [13].

Attribution labels need review. Who&When and TraceElephant both show that exact step attribution is difficult and dependent on available evidence [9][10]. When experts disagree, retain the disagreement or multiple plausible causes rather than force a false single truth. An automated diagnosis should cite the spans and requirements on which it relies, so a reviewer can reproduce or reject the conclusion.

### For SRE and Platform Teams: Operate the Telemetry Pipeline as a System

Agent observability must join the rest of the service graph. OpenTelemetry and OTLP permit agent spans to travel through collectors and be routed to multiple backends; LangSmith documents this fan-out pattern [6]. Correlating model and tool spans with HTTP, database, queue, and sandbox telemetry helps distinguish model behavior from infrastructure failure. The mapping must be tested because GenAI conventions remain under development and product schemas differ [2][6][14].

Service-level indicators should include both agent and telemetry health. Useful measures include end-to-end latency, model and tool latency, token usage, retries, tool-error rates, guardrail outcomes, unfinished traces, dropped spans, exporter failures, and the share of sampled traffic. Alert thresholds should reflect user impact and budget rather than raw event volume. Dapper's experience shows why sampling and common instrumentation are structural design choices, not cleanup tasks added after volume becomes unmanageable [1].

Retain high-value evidence deliberately. Errors, policy violations, unusually expensive runs, and representative regression cases may need longer retention than routine traffic, subject to law and policy. Current LangSmith tiers illustrate how product defaults and feature-triggered upgrades can change retention and cost [7]. The system of record should therefore document local decisions instead of assuming a vendor default is permanent.

### For Security and Privacy Teams: Treat Trace Payloads as Production Data

The worst observability failure is turning a debugging system into a second ungoverned copy of sensitive data. Prompts and tool payloads can contain personal information, secrets, health or financial data, private documents, and privileged instructions. OpenTelemetry recommends minimization and makes the implementer responsible for consent, protection, and compliance; OpenAI and Microsoft expose controls because their spans can include raw model, tool, message, and executor data [4][15][16].

A defensible design starts metadata-only, then allowlists content needed for a documented purpose. Redaction should occur before export when possible and fail closed when export depends on it. Access should be role-based and audited. Retention should be finite, deletion should be verifiable, and datasets promoted for long-term evaluation should undergo a separate review because they may outlive source traces [4][7][16].

Security monitoring also needs provenance. An operator investigating an unintended action should be able to identify the authenticated agent, tool, policy version, approval state, and external side effect. A trace without stable identity can show a sequence but cannot support accountability. NIST's emphasis on incident records, version history, monitoring, and retained TEVV evidence provides the governance basis for these controls [11].

### For Multi-Agent Systems: Observe Boundaries and Shared State

Multi-agent traces should expose messages, delegated objectives, artifacts, shared-memory changes, verification steps, and termination decisions at agent boundaries. A flat transcript can hide which context each agent actually received. Parent-child and linked spans, together with artifact identifiers, make it possible to distinguish message order from data dependency [8][15].

Do not infer that a fuller trace guarantees exact blame. MAST provides reusable categories, while Who&When and TraceElephant show that agent-level and especially step-level attribution remain imperfect [8][9][10]. A safer operational use is to narrow the candidate set, identify missing evidence, and direct a human or deterministic test to the relevant boundary. The trace is an evidence map, not a moral assignment of fault.

### For Small Agent Fleets: Start With a Reconstructable Record

The author's synthesis is that a small fleet does not need a large observability platform to adopt the discipline. It needs a stable run identifier, timestamped structured events, model and tool identities, arguments and outcomes where policy permits, artifact versions, errors, completion checks, and a durable link from a failure to its corrective test. The format can be a local file or database if access control, retention, and integrity are adequate.

The author's synthesis is that the smallest useful design is one in which an operator can answer five questions from records rather than memory: What was requested? What observable steps ran? What data and tools did those steps use? What external state changed? What check justified the final success or failure? If any answer depends on reconstructing events after the fact, the record is incomplete for that purpose.

The author's final assessment is deliberately limited. Agent observability is necessary for reliable debugging because unrecorded execution cannot be inspected later. It is not sufficient because instrumentation can omit evidence, telemetry can be sampled or redacted, semantic correctness needs evaluation, and causal attribution remains difficult. The engineering objective is therefore not maximal trace volume. It is sufficient, protected, and testable evidence for the decisions operators must make.

## Sources

1. Sigelman, B. H., Barroso, L. A., Burrows, M., et al. (2010). "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure." Google Technical Report. https://research.google.com/archive/papers/dapper-2010-1.pdf [high]

2. OpenTelemetry. "Semantic Conventions for GenAI Agent and Framework Spans." Current repository documentation; conventions marked Development. https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md [high]

3. OpenTelemetry. "Semantic Conventions GenAI Reference Implementations." Conformance scenarios and operation-coverage reports for Python libraries. https://github.com/open-telemetry/semantic-conventions-genai/blob/main/reference/README.md [high]

4. OpenAI. "Tracing -- OpenAI Agents SDK." Official SDK documentation for traces, default spans, sensitive-data controls, processors, and exporters. https://openai.github.io/openai-agents-python/tracing [high]

5. LangChain. "Observability Concepts -- LangSmith." Official definitions of runs, traces, threads, trajectories, instrumentation, and trace limits. https://docs.langchain.com/langsmith/observability-concepts [high]

6. LangChain. "Trace with OpenTelemetry -- LangSmith." Official OTLP ingestion, mapping, and collector fan-out documentation. https://docs.langchain.com/langsmith/trace-with-opentelemetry [high]

7. LangChain. "Usage and Billing -- LangSmith." Official current retention tiers, upgrades, datasets, and limits. https://docs.langchain.com/langsmith/usage-and-billing [high]

8. Cemri, M., Pan, M. Z., Yang, S., Agrawal, L. A., et al. (2025). "Why Do Multi-Agent LLM Systems Fail?" Advances in Neural Information Processing Systems 38, Datasets and Benchmarks Track. https://proceedings.neurips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html [high]

9. Zhang, S., Yin, M., Zhang, J., Liu, J., et al. (2025). "Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems." Proceedings of the 42nd International Conference on Machine Learning, PMLR 267, 76583-76599. https://proceedings.mlr.press/v267/zhang25cq.html [high]

10. Chen, M., Wang, J., Mu, F., Wang, Y., Liu, Z., Feng, H., and Wang, Q. (2026). "Seeing the Whole Elephant: A Benchmark for Failure Attribution in LLM-based Multi-Agent Systems." Accepted by ACL 2026; arXiv:2604.22708. https://arxiv.org/abs/2604.22708 [high]

11. National Institute of Standards and Technology. (2024). "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile." NIST AI 600-1. https://doi.org/10.6028/NIST.AI.600-1 [high]

12. Microsoft. "Review Agent Interactions with Trace Replay -- Microsoft Foundry." Official product documentation, preview. https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-replay [high]

13. OpenAI. "Evaluate Agent Workflows." Official documentation for trace grading, datasets, and repeatable evaluation runs. https://developers.openai.com/api/docs/guides/agent-evals [high]

14. OpenInference. "Semantic Conventions." Official specification for AI-oriented OpenTelemetry span kinds and attributes. https://arize-ai.github.io/openinference/spec/semantic_conventions.html [high]

15. Microsoft. "Agent Framework Workflows -- Observability." Official documentation for workflow spans, links, logs, metrics, and sensitive-data controls. https://learn.microsoft.com/en-us/agent-framework/workflows/observability [high]

16. OpenTelemetry. "Handling Sensitive Data." Official data-minimization and collector-processing guidance. https://opentelemetry.io/docs/security/handling-sensitive-data/ [high]

## See Also

- `library/coding-agentic-ai/agent-evaluation-and-benchmarking.md` -- explains how traces become outcome, process, and regression evaluations.
- `library/coding-agentic-ai/multi-agent-orchestration.md` -- provides the coordination context for observable handoffs and shared state.
- `library/coding-agentic-ai/tool-use-and-function-calling.md` -- covers the tool operations represented by execution spans.
- `library/coding-agentic-ai/context-window-management.md` -- explains the assembled model input that trace payloads may record.
- `library/coding-agentic-ai/anchor-coding-agentic-ai.md` -- defines observability and debugging as part of this domain's scope.
