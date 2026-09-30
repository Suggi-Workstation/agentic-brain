---
name: durable-agent-execution-checkpointing-idempotency-and-recovery-across-failures
id: 20260930T053418Z
tier: library-topic
domain: coding-agentic-ai
author: Librarian
tags: [durable-execution, agent-reliability, checkpointing, deterministic-replay, idempotency, failure-recovery, workflow-orchestration]
links: [library/coding-agentic-ai/agent-harness-design.md, library/coding-agentic-ai/agent-memory-and-persistence.md, library/coding-agentic-ai/agent-observability-and-debugging.md, library/coding-agentic-ai/human-in-the-loop-patterns.md, library/coding-agentic-ai/tool-use-and-function-calling.md, library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md]
---

# Durable Agent Execution -- Safety Depends on Replayable State and Explicit Side-Effect Semantics

Durable agent execution lets a long-running agent survive process failure, deployment, timeout, and human delay without losing accepted progress or blindly repeating external effects. The central engineering claim is that durability does not come from a longer conversation, a trace, or an unrestricted retry loop; it comes from an authoritative execution record, replay-safe control flow, and declared semantics for every model call and tool side effect. [1][2][15]

## Background

A simple agent loop holds its immediate state in process memory: assemble a prompt, call a model, execute a proposed tool, append the result, and repeat. That design can work for a short interaction, but a crash can occur between any two of those operations or during an operation whose outcome is no longer knowable from the failed process. Microsoft describes production agents as workflows that may run for hours, invoke external tools, and encounter restarts, deployments, scale-in events, or transient service failures. Its Durable Task model checkpoints LLM responses, tool results, and control-flow decisions so execution can resume on another worker instead of beginning again. [1]

Distributed workflow systems developed the underlying mechanisms before current language-model agents. Temporal records a complete ordered Event History and rebuilds workflow state by replaying the workflow definition against that history. AWS Lambda durable functions likewise rerun a handler from the beginning and substitute checkpointed results for completed durable operations. Azure Durable Task uses event sourcing to reconstruct local orchestration state and therefore requires replayed orchestrator logic to be deterministic. These implementations differ, but all separate an execution's durable record from the lifetime of the worker that happens to run it. [2][3][6]

That separation changes the unit of reliability. A process is disposable; the execution identity, input, accepted transitions, operation results, pending waits, and terminal status are not. Anthropic's Managed Agents architecture makes this boundary explicit by separating an append-only session log, a replaceable harness, and a replaceable sandbox. A failed harness can reload the session and resume from the last event, while a failed sandbox is handled as a tool failure and can be reprovisioned. The report also states that the durable session is not the model's context window: the context is a selected view, while the session remains outside it. [15]

Conversational memory addresses a different problem. Memory stores facts, summaries, preferences, or prior messages that may help a later inference. Durable execution stores which operation was authorized, whether it started, whether it completed, which exact result was accepted, and what transition may legally happen next. A summary saying that an email was probably sent cannot safely replace a receipt or an idempotency record. The author's synthesis is that memory supports cognition, while execution state supports causality and authority; using one as the other turns an uncertain side effect into an invented fact. [2][5][15]

Observability is also distinct. A trace can explain model calls, tool calls, timing, and errors, but a trace is not automatically the state machine that controls resumption. A durable history must be sufficiently authoritative for runtime decisions: it determines whether replay returns a recorded result, schedules new work, waits, compensates, cancels, or terminates. A useful implementation can derive traces and status views from the same events, but diagnostic completeness and recovery correctness remain separate requirements. This distinction is the author's synthesis of event-history replay and Anthropic's external session design. [2][15]

Failures create an unavoidable ambiguity window. A worker may send a side-effecting request, the remote service may commit it, and the acknowledgement may be lost before the workflow records completion. From the worker's perspective the operation failed; from the external system's perspective it succeeded. Retrying without a stable identity can duplicate the effect. Stripe's API resolves this class for supported requests by storing the first result under a client-supplied idempotency key and returning that result for later requests with the same key and parameters. AWS durable-execution guidance likewise distinguishes replay and retry semantics and instructs callers to match those semantics to the side effect. [4][5]

Checkpointing alone therefore does not establish safety. A checkpoint before a payment or message protects earlier progress, but a crash after the side effect and before the next checkpoint still leaves an unknown outcome. Safe recovery needs either an atomic transaction that includes both effect and record, a remote idempotency contract, a stable natural key, a status query, or a compensating action. The transactional outbox pattern handles one important dual-write case by committing a domain change and an outbox record in the same database transaction, then relaying the record separately; AWS notes that consumers must still tolerate duplicate delivery. [12]

Long-lived work also changes deployment. Replay executes current workflow code against old history, so adding, removing, or reordering commands can make an in-flight execution diverge from the events already recorded. Microsoft documents nondeterminism errors when updated orchestration logic no longer matches prior steps. Temporal uses worker versioning or history markers for compatible transitions, allowing old executions to retain old paths while new executions use new code. A durable system that cannot evolve its workflow definition safely trades crash recovery for deployment fragility. [7][9]

Human review is another form of long wait rather than an exceptional break in the design. Azure Durable Task external events let an orchestration suspend until a named, typed signal such as an approval or webhook arrives. The run can release compute while the durable store retains the pending state. The approval must refer to the saved action and state version; regenerating the proposed action after resumption would convert one approval into authority for different work. [8]

The domain boundary is narrow. This topic concerns execution semantics around agent loops: checkpoints, histories, replay, side effects, ownership, waits, cancellation, versioning, and recovery tests. It does not replace conversational-memory design, generic distributed-systems theory, observability, tool-schema design, or human-oversight policy. It connects those subjects by asking one operational question: after any interruption, what durable evidence permits the next agent action without losing work, repeating harm, or claiming completion prematurely?

## Core Concepts

### The execution record is the source of truth

A durable run needs a stable execution identifier and a record whose lifetime exceeds every worker, model context, and sandbox used to complete it. At minimum, the record should contain the original request, workflow definition or compatible version, current status, ordered transition history, completed operation results, pending operation identities, retry counts, timers, external-event subscriptions, cancellation state, and terminal result. Temporal calls its ordered record Event History; Anthropic calls the corresponding managed-agent structure an append-only session log. Both support replacement of the component performing the current computation. [2][15]

The current-state row shown to operators is normally a projection, not the whole record. A projection can say that a run is waiting for approval, owns lease generation 17, and has completed four steps. The history explains how it reached that state and permits reconstruction after corruption or process loss. The author's synthesis is that an implementation should make the history append-oriented and the projection replaceable: a projection can be rebuilt, while silently rewriting causal history destroys the evidence needed for replay and audit. [2][14][15]

Checkpoint granularity determines both recovery cost and consistency risk. Checkpointing after every token would create excessive storage and coordination overhead without defining meaningful effects. Checkpointing only at final completion forces expensive model and tool work to repeat. Microsoft checkpoints agent state transitions such as model responses, tool results, and control decisions; AWS durable operations checkpoint step returns and waits. The practical boundary is a transition whose accepted result will influence later behavior or whose repetition has material cost or consequence. [1][3]

A checkpoint must be committed before downstream work relies on it. If a tool result enters the next prompt but has not reached durable storage, a crash can produce a later history that has no authoritative explanation for the model's decision. The author's synthesis is to treat each transition as prepare, execute, and commit: persist intent and identity, perform the nondeterministic operation, then atomically accept its result and release dependent work. Systems may optimize these phases, but they must preserve the causal order. [2][3][12]

### Replay reconstructs decisions, not external effects

Deterministic replay runs orchestration code again while substituting recorded outcomes for already completed durable operations. Temporal replays Event History; AWS reruns the handler and returns checkpointed step values; Azure reconstructs orchestrator tasks from history events. Code outside the designated durable-operation boundary must make the same decisions from the same inputs and recorded results. Calls to clocks, random generators, files, databases, networks, or model APIs belong behind a recorded activity or step because their outputs can change. [2][3][6]

An LLM call is nondeterministic external work for replay purposes even when the model name and prompt are unchanged. Provider updates, sampling, routing, rate limits, and hidden service state can change the response. The safe default is to record the accepted model response or structured decision as an activity result and reuse it during replay. Reissuing the call is a new attempt that needs an explicit policy; it is not reconstruction of the old attempt. Temporal explicitly lists LLM invocations among work placed in Activities, and Microsoft's agent guidance says completed LLM calls should not repeat during recovery. [1][2]

The same rule applies to tool results. A read from a changing repository, database, or web API must either be recorded as the value used by the run or deliberately refreshed through a new versioned step. Replaying orchestration code against the current external world mixes two times and can choose a branch that the original run never chose. The author's synthesis is that replay answers, "What decision follows from the history this run actually saw?" Re-evaluation answers, "What decision follows from current evidence?" Both can be useful, but they are different state transitions and should not share an identity. [2][3][9]

Replay does not mean that every activity executes exactly once. A worker can fail while an activity is running or after its effect but before its result is durably acknowledged. Workflow engines commonly provide at-least-once or selectable execution semantics around activities. Exactly-once business effect requires cooperation from the target system through transactions, conditional writes, deduplication, stable object names, or idempotency keys. AWS's durable-execution documentation makes this distinction explicit by asking developers to match step semantics to side effects. [4]

### Stable identities make retries distinguishable from new intent

Every run, step, attempt, and external effect needs a stable identity. A run identifier groups the lifecycle. A logical step identifier names one intended operation within that run. Attempt numbers identify retries of that operation. An idempotency key identifies the intended external effect and must remain stable across attempts that mean "try the same effect again." Generating a new key during recovery converts a retry into a second request. [4][5]

A good key is unique to the business intent and bound to material parameters. Stripe compares retry parameters with the original request and rejects reuse when they differ, preventing one key from authorizing different work. Its retention window also shows that idempotency is scoped in time: if the server prunes the key, a much later reuse can create a new operation. The workflow must therefore retain enough metadata to know the provider's deduplication scope and must not imply permanent exactly-once protection from a temporary key store. [5]

Idempotency has several implementations. A remote API can cache the first result under a key. A database can use a uniqueness constraint and upsert. Object storage can use a deterministic object name and compare version or content. A consumer can record processed event identifiers in the same transaction as its local effect. A read can be naturally idempotent yet still return a different value over time, which matters for replay even though it does not mutate state. The author's synthesis is that "safe to repeat" and "same observation" are independent properties. [3][5][12]

Unknown outcomes need a query path. If a network timeout follows a request, the runtime should first query by operation identity when the target supports it. A response of completed permits the result to be recorded; not found may permit a retry; pending calls for waiting; and contradictory or unqueryable state may require human reconciliation. Representing every timeout as failure hides the possibility that the side effect succeeded and is the root cause of duplicate actions. [5]

### Atomicity, outboxes, and compensation close different gaps

A local transaction can atomically update workflow state and a local domain record when both live in one transactional store. It cannot normally atomically commit an unrelated remote API call. The transactional outbox narrows that gap for event publication: write the domain change and an outbound event record in one transaction, then let a relay publish committed records. If publication repeats, the event identifier and an idempotent consumer prevent duplicate local effects. AWS identifies duplicate messages and order preservation as explicit considerations rather than claiming magical exactly-once delivery. [12]

The inbox is the receiving analogue. Before applying a delivered event, the consumer checks or atomically claims its identifier. If it has already committed the effect, the duplicate becomes a no-op. If processing failed before commit, the claim must not suppress a legitimate retry. The author's synthesis is that outbox and inbox records form a durable handoff receipt on each side of an asynchronous boundary; neither makes the transport itself exactly once. [12]

Some multi-step effects cannot be rolled back mechanically because each service commits independently. Garcia-Molina and Salem introduced sagas as sequences of shorter transactions with compensating transactions for partial execution. A compensation is semantic repair, not time travel: refunding a charge does not erase the original charge from statements, and deleting a sent message may not remove copies already read. Durable agent workflows should record both forward and compensating actions, execute compensation in a defined order, and make compensation itself retry-safe. [13]

Forward recovery and compensation are policy choices. A transient provider outage may justify a bounded retry from the same step. An invalid business input should not be retried unchanged. A downstream rejection after earlier success may require compensation. An irreversible effect may require a terminal partial-failure state and human resolution. The author's synthesis is to declare these outcomes per operation instead of letting the model improvise after an exception. [11][13]

### Leases coordinate workers but do not make stale workers harmless

A durable queue needs to prevent two workers from treating the same runnable step as exclusively theirs. One common design grants a renewable lease with an expiration and heartbeat. If the owner stops renewing, another worker may claim the step. Chubby's production lock service uses sessions, leases, keep-alives, and lock generation numbers in a fault-tolerant service, illustrating both the utility and complexity of ownership under uncertain communication. [14]

Lease expiry does not instantly stop the old worker. A paused or partitioned worker can resume after a new worker has acquired ownership. If both can write, duplicate or stale effects remain possible. Chubby increments a lock generation number when a lock moves from free to held. The author's synthesis is to pass a monotonically increasing ownership generation to mutable resources and reject writes from older generations; this is a fencing rule, not merely a timeout. Where the target cannot enforce fencing, idempotency and conditional updates still have to protect the effect. [14]

Heartbeats serve two separate purposes. They show that a worker is making progress and they carry resumable progress for long operations. Temporal's cancellation guidance requires non-immediate activities to heartbeat so cancellation can reach them, demonstrating that liveness signals can also be a control channel. A heartbeat should not be mistaken for completion, and losing one should not by itself prove that no external effect occurred. [10]

### Retries require classification, budgets, and backoff

A retry repeats an operation because the same intended result may still be obtainable. Transport interruption, rate limiting, temporary unavailability, or worker loss may be retryable. Invalid arguments, denied permission, violated policy, incompatible workflow history, exhausted budget, or a known permanent business rejection usually require correction, version rollback, escalation, compensation, or failure. Temporal's testing guidance specifically warns against infinite retries and calls for bounded timeouts, backoff, idempotent activities, and observation of retry storms. [11]

Each retry policy should declare maximum attempts or elapsed time, backoff and jitter, per-attempt timeout, total deadline, retryable error classes, and terminal disposition. Model calls also need cost and token limits because a technically recoverable loop can become economically failed. A retry that changes the prompt, tool arguments, model, or intended effect may be a repair or a new step and should receive a new identity rather than corrupting the history of the original operation. This classification is the author's synthesis of durable-step and agent-run constraints. [1][4][11]

Blind retry loops erase information. If the same deterministic validation error returns repeatedly, another attempt does not change the precondition. If a side-effect outcome is unknown, retrying without a key increases risk. If a workflow replay diverges after deployment, repeated task execution can remain stuck until compatible code returns. A durable runtime should surface these as typed states with finite recovery routes, not as one generic exception passed back to the model. [5][7][9][11]

### Human waits and cancellation are durable states

An agent that waits for approval, missing data, a callback, or a scheduled time should stop consuming worker resources while retaining its full execution state. Azure external events associate a named, typed event with a particular orchestration instance and wake the instance when the event arrives. The durable state should also retain the exact proposed action, policy version, expiration, and reviewer scope so resumption cannot silently authorize altered work. [8]

External events can arrive more than once or before the workflow reaches the wait, depending on the platform's delivery contract. The receiving transition therefore needs an event identity and deduplication rule. A timeout should race through a durable timer and produce an explicit expired, escalated, or canceled state. The author's synthesis is that a human wait is a message-processing problem with authority attached, not a suspended chat turn. [8][12]

Cancellation is not the same as process death. Temporal distinguishes graceful cancellation, which records a request and lets workflow code run cleanup, from termination, which stops the execution without giving code that opportunity. Activity cancellation can require heartbeats to become observable. A durable agent should define propagation to child tasks, treatment of queued side effects, non-cancellable cleanup, and the final status reported to the requester. [10]

Cancellation cannot retract an already committed external effect. Cleanup may compensate it, and pending requests may be revoked if the provider supports revocation, but the execution record must preserve what happened. The author's synthesis is that stop semantics require three questions: what new work must not start, what running work can receive cancellation, and what completed work needs compensation or disclosure. [10][13]

### Workflow code is part of durable state

A long-running execution can outlive several software releases. Replaying old history through incompatible code can reorder tool calls, change parameters, add branches, or omit an expected transition. Microsoft and Temporal both document version-aware execution because replay determinism links a run to the control-flow definition that produced its history. [7][9]

Compatible deployment strategies include pinning workers by version, retaining old workflow types, adding history-recorded patch markers, and routing new executions to a new definition while old executions drain. Data schemas, serialized model decisions, tool contracts, prompt templates, and policy versions may also need migration or retention. The author's synthesis is that versioning only orchestration source code is insufficient when a later step cannot deserialize or interpret the recorded artifacts on which that code depends. [7][9]

### Recovery is a behavior that must be tested

A happy-path test shows that the workflow can complete when dependencies and workers remain available. It does not establish durability. Temporal's pre-production guidance recommends killing and restarting workers, breaking downstream dependencies, removing network connectivity, introducing nondeterministic workflow changes, testing versioned deployment, and observing duplicates, backlog recovery, replay latency, retry behavior, and consistency. [11]

Failure injection should target boundaries: before an intent record, after intent but before dispatch, during the remote operation, after the external effect but before result commit, after result commit, during a human wait, during cancellation, and across a version deployment. The acceptance oracle should verify both positive progress and negative invariants: no duplicate charge or message, no lost committed result, no stale owner write, no unbounded retry, no execution of a canceled pending action, and no unsupported completion claim. This test matrix is the author's synthesis of the failure mechanisms above. [4][5][7][10][11][12][14]

## Evidence

### Independent workflow systems converge on history and replay

Temporal, AWS, and Microsoft document independently implemented durable runtimes with a common mechanism: persist operation history, rerun orchestration code after interruption, and substitute recorded results for completed work. Temporal describes an ordered Event History and deterministic replay. AWS states that completed steps return checkpointed values while non-durable code runs again. Microsoft states that event-sourced orchestrators replay and must produce the same result. This convergence is architectural evidence that durable execution requires an external record and a controlled nondeterministic-operation boundary rather than an in-memory agent transcript. [2][3][6]

The evidence is documentary, not a comparative benchmark. The vendors use different APIs, storage layers, limits, and failure contracts, and their documentation does not prove equal behavior under every fault. The supported conclusion is narrower: three production-oriented platforms impose the same replay invariant because a replacement worker must reconstruct decisions without repeating completed external work. [2][3][6]

Microsoft applies the model directly to agents. Its Durable Task guidance identifies infrastructure interruption, expensive repeated LLM calls, transient dependency failure, and long-running coordination as production problems. The runtime checkpoints LLM responses, tool-call results, and control decisions, resumes on another machine, and supplies bounded retry policies. It explicitly supports both code-directed workflows and agent-directed loops, which shows that dynamic model choice does not remove the need for durable transition records. [1]

### Anthropic's Managed Agents case separates failure domains

Anthropic reports a production architecture that decomposes a managed agent into session, harness, and sandbox interfaces. The session is an append-only event log outside the harness; the harness calls the model and dispatches tools; the sandbox performs computation. When a sandbox fails, the harness handles a tool error and can provision a replacement. When the harness fails, a new harness reloads the session and resumes from the last event. [15]

This is a primary vendor engineering case rather than an independent experiment, and the public report does not provide a controlled duplicate-side-effect rate. Its evidentiary value is the concrete recovery boundary: neither the reasoning process nor the execution container owns the only copy of the session. It also distinguishes session history from the model context, supporting the claim that prompt continuity and process continuity are separate engineering problems. [15]

Anthropic's earlier long-running coding-agent work used a simpler method: an initializer prepared the environment and durable artifacts, and later sessions made incremental changes while leaving feature state, progress notes, git history, setup instructions, and end-to-end test evidence. The reported failure modes before those controls included over-broad one-shot work, undocumented partial progress, and premature completion. The intervention was not a general workflow engine, but it provides a second implementation case in which explicit artifacts let fresh contexts reconstruct project state. [16]

The two Anthropic cases also define the new topic's boundary from existing coding-workflow knowledge. File and git checkpoints are effective durable artifacts for repository work; a service-backed event history generalizes the principle across model calls, tools, callbacks, and infrastructure. Neither case by itself closes the ambiguous external-side-effect window, which is why idempotency, outbox, compensation, and ownership semantics remain necessary additions. [15][16]

### Idempotency documentation exposes the uncertain-outcome problem

Stripe's API reference describes a concrete server-side method. A client supplies an idempotency key for a state-changing request; Stripe stores the first result and returns it for later requests with the same key, including a stored error response. It compares parameters to prevent the same key from being reused for different operations and documents retention behavior. This mechanism turns a lost response from a potential duplicate creation into a query-by-repeat of the same logical request, within the documented scope. [5]

AWS durable-execution guidance separates retry semantics from side-effect semantics and provides idempotency-token patterns. The significance is not one provider-specific API. Together, the sources show that a durable workflow engine cannot infer from a network exception whether a remote effect committed. Safety comes from a contract shared by caller and callee: a stable operation identity, deduplication or conditional application, and a reproducible result. [4][5]

These sources do not justify a blanket claim of exactly-once execution. The key can expire, the target may not support it, and a crash can still occur around local recording. The supported operational claim is that idempotency makes at-least-once request attempts compatible with one intended effect when the target honors the key and parameters. Other targets need transactions, natural keys, status queries, deduplicating consumers, or explicit reconciliation. [4][5][12]

### Outbox and saga research covers cross-system partial failure

AWS's transactional-outbox guidance starts from a dual write: update a database and publish a message. Either order can fail between operations and leave inconsistent state. Its implementation writes the domain change and outbox row in one transaction, then lets another component relay committed rows. The guidance explicitly warns that duplicate messages remain possible and recommends idempotent consumers. This is a documented architecture pattern rather than evidence that one AWS service combination is mandatory. [12]

Garcia-Molina and Salem's 1987 saga paper addresses a broader long-lived transaction problem. Its method decomposes a long transaction into a sequence of shorter transactions and associates completed work with compensating transactions if the saga cannot finish. The model relaxes global atomicity while preserving a structured recovery route for partial execution. For agents, the bounded application is to multi-tool workflows whose external services cannot share one database transaction. [13]

The original saga model also limits what compensation means. Other work can observe intermediate commits, and a compensating action restores an acceptable business state rather than erasing history. This supports explicit partial-failure and compensation records in an agent runtime. It does not support pretending that every real-world action has an inverse; disclosure, physical actions, and messages can be irreversible. [13]

### Chubby demonstrates ownership under uncertain communication

Burrows reports Google's operational experience with Chubby, a replicated coarse-grained lock and low-volume metadata service. The paper describes sessions, leases, keep-alives, locks, and generation numbers and reports use by systems including the Google File System and Bigtable. The method is an engineering case study based on deployed service behavior rather than a formal proof of all lease-based algorithms. [14]

The relevant finding for durable agents is that worker ownership is not a local boolean. Communication can fail independently of processes, a lock holder can lose its session, and a new master or owner must reason conservatively about prior state. Chubby's generation counters provide evidence for versioned ownership. The fencing application to agent step writes is the author's synthesis: a target that rejects older generations prevents a delayed worker from overwriting work accepted from its successor. [14]

### Recovery guidance tests the property instead of the path

Temporal's pre-production testing guide treats recovery as an object of testing. It calls for worker shutdown and restart, downstream breakage, network removal, failover, replay-safety checks, and versioning failures, with observations that include duplicate results, retry storms, backlog growth and drain, replay latency, consistency, and human recovery steps. [11]

The guide is operational guidance rather than peer-reviewed causal evidence, but its method is falsifiable: inject a named failure, observe state and invariants, and verify recovery. That is stronger than asserting durability because a checkpoint table exists. A checkpoint implementation passes only when the original run can resume without lost accepted work, duplicate prohibited effects, stale ownership, or incorrect terminal status under the tested failure schedule. [11]

Across the sources, the evidence supports a layered conclusion. History and replay preserve control-flow progress; idempotency and transactions protect effects; compensation repairs partial business completion; leases and generations coordinate workers; external events preserve waits; versioning preserves replay across deployments; and failure injection verifies that the composition works. No single mechanism substitutes for the others. [1][2][4][5][7][8][11][12][13][14][15]

## Implications

### For agent-runtime builders

Design the execution model before optimizing the prompt loop. Define durable states such as pending, runnable, running, waiting, compensating, canceled, failed, and completed. Define legal transitions, the event recorded for each transition, and the evidence required to enter a terminal success state. A model can propose an action or next state, but deterministic runtime code should own transition validation and durable commit. This recommendation is the author's synthesis of the replay systems and managed-agent case. [1][2][15]

Separate the authoritative record from all derived views. The prompt contains a bounded context assembled for one inference. Operator status is a projection. Observability is an indexed diagnostic view. Long-term memory is selected reusable knowledge. None should silently overwrite the execution history. If compaction drops detail from a model context, the result receipt and causal event should remain available for recovery. [2][15]

Choose checkpoint boundaries by semantics. Persist accepted LLM outputs before dispatching dependent tools. Persist tool intent and stable identity before a side effect, then persist the accepted result before releasing downstream work. Use a local transaction when state and outbox share a store. Where the target is remote, require idempotency, status lookup, conditional mutation, or compensation. The runtime should refuse automatic retry for an unknown consequential effect that has none of these protections. [4][5][12][13]

Classify every tool contract with fields that ordinary function schemas omit: side-effect class, replay behavior, idempotency-key support, natural key, query-by-operation support, retryable errors, timeout, compensation, cancellation support, and required ownership generation. This metadata lets the dispatcher choose a recovery path without asking a stochastic model to invent one after failure. The model can still help diagnose or select among authorized routes; it should not define execution semantics ad hoc. [4][5][10][12][14]

### For tool and API designers

Expose stable operation identifiers and state queries. A caller that receives a timeout should be able to ask whether the operation is absent, pending, completed, failed, or canceled. Return the same result for a repeated idempotent request with the same parameters, and reject key reuse with materially different parameters. Publish retention limits and concurrency behavior so workflow designers know the actual guarantee. Stripe's documented contract is a concrete example of this interface shape. [5]

Make conditional writes and version checks available. A tool that mutates a file, record, deployment, or queue should accept an expected version or ownership generation where stale writers are possible. This protects against both concurrent work and a worker that resumes after losing its lease. If the resource cannot enforce a condition, the agent runtime should narrow concurrency or route through a serializing owner rather than treating a lease in its own database as global exclusion. [14]

Design compensations as first-class operations where business reversal is meaningful. Name the original operation they compensate, make them idempotent, record their own results, and state what they cannot undo. A refund, revocation, deletion, or rollback may leave externally visible history, so the final state should say compensated rather than pretend the original action never happened. [13]

### For platform and reliability teams

Operate durable execution as a stateful service, not a library feature that can be forgotten after integration. Monitor stuck runs, lease age, heartbeat gaps, retry counts, unknown outcomes, compensation failures, event-history growth, replay latency, version mismatches, callback age, and backlog drain. Alert on terminal-state contradictions, such as a completed run with unresolved pending effects. Temporal's testing guide identifies many of these recovery and backlog signals. [11]

Set finite recovery budgets. A dependency can remain unavailable longer than the run's business deadline, and an agent can spend more on retries than the result is worth. Retry budgets should combine attempt count, elapsed time, cost, and operation consequence. When exhausted, the runtime should enter a named state such as needs-input, needs-reconciliation, compensated, or failed instead of continuing silently. [1][4][11]

Use failure injection before deployment and during controlled game days. Kill workers at each commit boundary, isolate the history store, delay acknowledgements, duplicate external events, expire leases, restore a stale worker, corrupt a nonauthoritative projection, cancel during an activity, deploy incompatible code, and break a compensation. Verify the durable record, external state, and user-visible status after each test. Recovery time matters, but correctness invariants come first. [7][10][11][14]

Plan retention and archival. Histories, idempotency records, outboxes, inboxes, and checkpoints can grow without bound. Retention must respect the longest possible retry, callback, dispute, audit, and compensation window. Deleting a deduplication key while a retry remains possible weakens the effect guarantee. Conversely, retaining prompts and tool payloads indefinitely can create privacy and security risk. The author's synthesis is to retain causal metadata and necessary receipts under explicit policy while minimizing sensitive content. [5][11][12]

### For product and human-oversight designers

Treat approval as a durable external event bound to exact work. Before waiting, persist the proposed action, target, arguments, evidence, policy version, reviewer authority, and expiration. After an approval arrives, deduplicate the event and revalidate current state before dispatch. If material inputs changed, request a new decision. Azure's external-event model supplies the durable wait primitive; the binding and revalidation rule is the author's synthesis for authority safety. [8]

Expose accurate lifecycle language. "Running" should not cover waiting three days for input; "failed" should not cover an unknown remote outcome; and "completed" should not mean that the model emitted a final sentence. Users need pending, waiting, cancel-requested, compensating, partially completed, and needs-reconciliation states when those are true. Cancellation should state whether queued work was stopped, running work acknowledged cancellation, and completed effects remain. [8][10][13]

Provide graceful and forceful stop controls with different consequences. Graceful cancellation permits cleanup and compensation; forceful termination stops workflow code and may leave external work to reconcile. The user interface should not represent them as equivalent buttons. Long activities must heartbeat or otherwise expose cancellation points if the platform is expected to interrupt them. [10]

### For security and governance teams

Durability preserves authority only if authorization travels with state. Store who or what authorized a step, the scope and expiration of that authority, and the policy version applied. A replay should not reacquire broader credentials merely because a new worker has them. A model response recorded before a policy change is evidence of a prior decision, not automatic permission to execute later under changed conditions. This is the author's synthesis of durable history, external-event approval, and versioned execution. [7][8][15]

Limit the blast radius of replay. Sandboxes, scoped credentials, target allowlists, spend limits, and approval gates must still apply when execution resumes on a replacement worker. Anthropic's separation of session, harness, and sandbox demonstrates that state durability does not require placing permanent credentials inside the execution environment. [15]

Preserve an audit chain without treating raw prompts as the only evidence. Record execution identity, step identity, tool contract version, model call receipt, policy decision, external operation identity, attempt, status, reviewer event, compensation, and terminal reason. Sensitive prompts and payloads can be stored behind narrower access or represented by governed references and hashes. The goal is to reconstruct causal authority and effect, not to retain every secret in every context view. [2][15]

### For evaluators

Evaluate recovery as a matrix, not one success rate. Cross failure point with operation class: deterministic control step, expensive LLM call, read, idempotent write, non-idempotent write, outbox relay, human wait, compensation, lease transfer, cancellation, and version deployment. For each cell, test whether progress is preserved, prohibited duplication is absent, final state is truthful, and recovery remains within budget. [4][7][10][11][12][14]

Measure at least recovery success, lost-progress rate, duplicate-effect rate, unknown-outcome rate, mean and tail recovery time, attempts per step, compensation success, stale-owner rejection, callback age, cancellation latency, replay mismatch rate, and cost added by recovery. Report which external systems supplied idempotency or transaction guarantees; otherwise an aggregate pass rate hides the boundary that actually protected the effect. This metric set is the author's synthesis of the cited failure models. [4][5][11][12][14]

Run differential recovery tests. Execute the same workflow once without injected failure and once with a failure at a chosen boundary, then compare durable results and permitted external effects. The histories need not be byte-identical because retries and recovery events differ, but the business outcome and invariants should match unless the specification permits a partial or compensated result. Replay tests should also feed historical event streams into new workflow code before deployment. [7][9][11]

The author's synthesis is a final design test that is simple to state even when difficult to satisfy: after any worker, model, tool, network, or deployment failure, a replacement executor must be able to determine what is known, what is uncertain, what is authorized, and which next transition is safe from durable evidence alone. If it must guess from conversational prose, repeat an unidentifiable side effect, or trust that an expired worker stopped, the workflow is not yet durable.

## Sources

1. Microsoft. "Durable Task for AI Agents." Official Azure Durable Task documentation on agent checkpoints, recovery, retries, and workflow patterns.
   https://learn.microsoft.com/en-us/azure/durable-task/sdks/durable-task-for-ai-agents [high]

2. Temporal Technologies. "Temporal Workflow." Official documentation on Event History, deterministic replay, Activities, and recovery.
   https://docs.temporal.io/workflows [high]

3. Amazon Web Services. "Determinism During Replay." AWS Durable Execution SDK Developer Guide.
   https://docs.aws.amazon.com/durable-execution/patterns/best-practices/determinism/ [high]

4. Amazon Web Services. "Idempotency and Retries." AWS Durable Execution SDK Developer Guide.
   https://docs.aws.amazon.com/durable-execution/patterns/best-practices/idempotency/ [high]

5. Stripe. "Idempotent Requests." Official API reference for key scope, result reuse, parameter comparison, and retention.
   https://docs.stripe.com/api/idempotent_requests [high]

6. Microsoft. "Durable Orchestrator Code Constraints." Official Azure documentation on event sourcing and deterministic replay.
   https://learn.microsoft.com/en-us/azure/durable-task/common/durable-task-code-constraints [high]

7. Microsoft. (2026). "Orchestration Versioning: Safe Deployments for Durable Orchestrations." Official Azure documentation.
   https://learn.microsoft.com/en-us/azure/durable-task/common/durable-orchestration-versioning [high]

8. Microsoft. (2026). "Handle External Events in Durable Orchestrations." Official Azure documentation for durable human and system callbacks.
   https://learn.microsoft.com/en-us/azure/durable-task/common/durable-task-external-events [high]

9. Temporal Technologies. "Versioning - Python SDK." Official documentation on worker versioning, patch markers, and replay testing.
   https://docs.temporal.io/develop/python/workflows/versioning [high]

10. Temporal Technologies. "Interrupt a Workflow Execution - Python SDK." Official documentation on cancellation, termination, cleanup, and activity heartbeats.
    https://docs.temporal.io/develop/python/cancellation [high]

11. Temporal Technologies. "Pre-production Testing." Official failure-injection and recovery-testing guidance.
    https://docs.temporal.io/best-practices/pre-production-testing [high]

12. Amazon Web Services. "Transactional Outbox Pattern." AWS Prescriptive Guidance on dual writes, outbox relay, ordering, and duplicate handling.
    https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html [high]

13. Garcia-Molina, H., and Salem, K. (1987). "Sagas." Proceedings of the 1987 ACM SIGMOD International Conference on Management of Data, 249-259.
    https://doi.org/10.1145/38713.38742 [high]

14. Burrows, M. (2006). "The Chubby Lock Service for Loosely-Coupled Distributed Systems." OSDI 2006, 335-350.
    https://research.google.com/archive/chubby-osdi06.pdf [high]

15. Anthropic. (2026). "Scaling Managed Agents: Decoupling the Brain From the Hands." Primary engineering case on external session logs and replaceable harnesses and sandboxes.
    https://www.anthropic.com/engineering/managed-agents [high]

16. Anthropic. (2025). "Effective Harnesses for Long-Running Agents." Primary engineering case on progress artifacts, incremental execution, and recovery across context windows.
    https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents [high]

## See Also

- `library/coding-agentic-ai/agent-harness-design.md` -- broader runtime architecture for loop control, dispatch, state, policy, and verification; this topic develops its durability and failure semantics.
- `library/coding-agentic-ai/agent-memory-and-persistence.md` -- lifecycle design for retained knowledge, distinct from authoritative execution progress.
- `library/coding-agentic-ai/agent-observability-and-debugging.md` -- traces and diagnostic evidence derived from execution without replacing its control state.
- `library/coding-agentic-ai/human-in-the-loop-patterns.md` -- approval and escalation design for the durable wait boundary.
- `library/coding-agentic-ai/tool-use-and-function-calling.md` -- tool contracts and dispatch boundaries where retry and idempotency policies apply.
- `library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md` -- repository-specific checkpoints, verification, and handoff artifacts.