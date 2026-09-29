---
name: agent-cost-latency-and-resource-governance
id: 20260929T193356Z
tier: library-topic
domain: coding-agentic-ai
author: Librarian
tags: [agent-cost, latency, resource-governance, token-budgets, model-routing, prompt-caching, service-level-objectives, circuit-breakers]
links: [library/coding-agentic-ai/agent-evaluation-and-benchmarking.md, library/coding-agentic-ai/agent-harness-design.md, library/coding-agentic-ai/agent-observability-and-debugging.md, library/coding-agentic-ai/context-window-management.md, library/coding-agentic-ai/multi-agent-orchestration.md, library/coding-agentic-ai/tool-use-and-function-calling.md]
---

# Agent Resource Governance -- Reliability Requires Budgets for Cost, Latency, and Work

A tool-using agent is reliable only when it can achieve a defined task outcome inside an explicit resource envelope. Tokens, model calls, tool calls, wall time, memory, network traffic, concurrency, and money therefore need enforceable budgets, trace-level attribution, and degradation rules; unconstrained search or arbitrary truncation does not establish efficient performance. [1][2]

## Background

Early language-model applications made one request and returned one response, so operational accounting could often be reduced to input tokens, output tokens, and end-to-end request time. An agent changes that unit of work. One user request can create a sequence of model calls, tool invocations, retries, retrievals, context rewrites, delegated subtasks, and verification steps. The sequence may be selected dynamically from intermediate results, so the system cannot know its exact resource consumption from the initial prompt alone. Anthropic describes agentic systems as trading latency and cost for better task performance, while its production research system reports that ordinary agents used about four times as many tokens as chat interactions and its multi-agent system about fifteen times as many. Those figures describe one vendor's workload, not a universal multiplier, but they demonstrate why per-call pricing is not a sufficient control model for a multi-step run. [10][11]

Benchmark practice created a related problem. Kapoor and colleagues compared agent designs on coding tasks and found that systems with substantially similar accuracy could differ in inference cost by almost two orders of magnitude. Their simple retry baselines could outperform more elaborate agents while costing less, and their analysis showed that repeated sampling can improve accuracy merely by spending more. They therefore argued that agent evaluation must be cost-controlled and that accuracy and inference cost should be shown together as a Pareto frontier. A leaderboard that permits one entrant ten or fifty times the search budget of another may measure willingness to spend rather than architectural efficiency. [2]

Resource governance is broader than monetary cost. AgentSLABench, a 2026 academic preprint, proposes evaluating correctness together with wall-clock latency, API cost, token count, CPU, memory, HTTP calls, network bytes, and safety violations under declared limits. Its profiling protocol runs each agent-task pair in a constrained container, measures the resulting resource profile, applies a task judge, and writes an auditable record. The preprint is an early proposal rather than a settled standard, but its measurement boundary is useful: an agent run is a resource-consuming process, not merely a final answer. [1]

Latency also differs from one scalar duration. A service with acceptable median latency can still produce intolerable slow requests. Dean and Barroso showed that temporary slowdowns become dominant at scale because a user request often waits on many components; they argued for measuring and engineering the tail of the distribution rather than relying on averages. Tool-using agents amplify this effect. A run that waits sequentially for several model and tool calls accumulates round trips, while parallel fan-out can make completion depend on the slowest branch. The resulting service should therefore track percentiles such as p50, p95, and p99 by task class and stage, not only a fleet-wide mean. [4]

Site reliability engineering supplies the control vocabulary. Google defines a service-level objective as a target for a measured service-level indicator over a stated window. An error budget records how much noncompliance the service can tolerate, and the operational loop is to measure the indicator, compare it with the objective, decide whether action is needed, and act. Google also recommends defining SLOs from the user's perspective, using graceful load shedding and dynamic timeouts under overload, and damping retry amplification with exponential backoff and jitter. These ideas apply to agents when task success, latency, cost, and policy compliance are treated as service outcomes instead of disconnected dashboards. [5][6]

The economic vocabulary comes from unit economics and cost allocation. The FinOps Foundation recommends allocating resource costs before calculating a business unit metric, then dividing attributable cost by a value-bearing unit such as a transaction. For agents, useful units include cost per attempted task, cost per verified success, cost per customer resolution, and cost per accepted code change. A single average can conceal failed runs, retries, or cross-subsidized tenants, so the allocation keys must identify the run, agent version, model, tool, tenant or product, task class, and outcome. [14]

These lineages converge on one engineering principle. A budget is not an estimate written in a planning document. It is a machine-enforced constraint attached to a run, observed at each resource-consuming boundary, and paired with a defined response when remaining resources are insufficient. The author's synthesis is that resource governance should make two failures impossible to confuse: an agent that correctly determines that it cannot finish within its envelope, and an agent that silently consumes unbounded resources until infrastructure stops it. The former is controlled abstention or degradation; the latter is an operational defect. [1][5][15]

## Core Concepts

### The Resource Envelope Is Part of the Task Contract

A resource envelope names the dimensions a run may consume and the maximum or target for each one. A practical envelope can include input, output, reasoning, cache-read, and cache-write tokens; model calls by model class; tool calls by tool and side-effect class; wall-clock deadline; per-stage timeout; CPU time; peak memory; disk use; bytes transferred; concurrent branches; retries; and monetary cost. AgentSLABench measures many of these dimensions directly, while the Microsoft Agent SRE specification defines task success, response latency, and cost per task as distinct service indicators. [1][15]

The envelope should distinguish hard limits from objectives. A hard limit is an execution boundary: for example, no more than 20 model calls, 200 tool calls, 15 minutes, or a fixed monetary amount. Reaching it must trigger a deterministic stop, pause, or permitted fallback. An objective is a distributional target: for example, 95 percent of support tasks complete within 10 seconds and 99 percent cost less than a declared amount. Individual runs may exceed an objective while the service remains within its window, whereas a hard limit cannot be exceeded without a separately authorized change. Google SRE's separation between measured indicators, objectives, and error budgets provides the general model. [5][6]

Budgets should be hierarchical. A fleet budget constrains total spend or shared capacity. Product, tenant, agent, task-class, and individual-run budgets subdivide it. A parent run that creates subagents should reserve or allocate child budgets rather than letting every child inherit the full parent allowance. The author's synthesis is to enforce conservation: resources granted to live children plus resources already consumed plus the parent's retained reserve must not exceed the parent's hard budget. This prevents fan-out from multiplying authority merely because work was decomposed. Anthropic's report that multi-agent research can use far more tokens than chat interactions shows the practical exposure, while its prompting guidance to scale subagent and tool counts to query complexity illustrates the need for explicit allocation. [11]

Different dimensions need different enforcement points. Token and model-call limits belong at the model gateway. Tool-call and network limits belong at the dispatcher or proxy. CPU, memory, process, disk, and wall-time limits belong in the execution environment. Monetary limits require a ledger that combines provider usage, tool charges, and allocated infrastructure cost. A model prompt may inform the agent about these limits so it can plan, but the prompt cannot be the enforcement boundary because the same model is deciding how to spend them. [1][12][15]

### Cost Attribution Requires a Run Ledger

Cost control begins with attribution. Every model call should record the run and span identifiers, model and provider, input and output tokens, cache-read and cache-write tokens, price version, request time, and computed charge. Every paid tool call should record its direct fee or billable unit. Self-hosted inference and shared tools should be allocated under a documented rule, such as GPU-seconds, CPU-seconds, bytes, or requests. The FinOps Foundation treats allocation as a prerequisite to unit economics, and OpenTelemetry standardizes model, token, and duration fields that can populate the technical side of this ledger. [12][14]

A simple per-run accounting identity is the author's synthesis:

`run cost = model charges + paid tool charges + allocated compute + allocated storage and network + allocated shared overhead`.

The identity is useful only when the components are not double-counted. Provider bills remain the source for actual external charges; telemetry estimates explain which run caused them. Shared overhead rules should be versioned because changing the allocator changes historical unit cost without changing execution. A report should therefore preserve raw quantities such as tokens, calls, bytes, and duration alongside dollars. Kapoor and colleagues recommend reporting token counts as well as monetary cost because provider prices can change while the underlying consumption remains comparable. [2]

The most decision-relevant derived metric is often cost per verified success rather than average cost per attempt. If `C` is total attributable cost, `N` is attempted tasks, and `S` is independently verified successes, then `C/N` measures cost per attempt and `C/S` measures cost per success. The latter rises when retries or failure consume resources without producing accepted outcomes. It should not be used alone: a system can lower cost per success by refusing difficult cases or narrowing the evaluated distribution. Pair it with success rate, task mix, failure severity, and latency. This is an author's synthesis from the joint cost-accuracy method in AI Agents That Matter and the unit-cost method in FinOps guidance. [2][14]

### Latency Is a Budget Across a Critical Path

End-to-end latency is the time from accepted request to terminal result, but optimization requires a stage decomposition. Record queue time, context assembly, routing, model time to first token, model generation time, tool execution, retry backoff, verification, persistence, and user or approval wait separately. OpenTelemetry's GenAI conventions expose model-operation duration and token usage, and its trace tree can relate model and tool spans to the parent agent invocation. The trace should preserve parallel relationships so summed span duration is not mistaken for wall time. [12]

A deadline should flow downward. If the run has 30 seconds remaining, a child operation should not receive a 60-second timeout. The author's synthesis is to calculate each call's deadline from the parent's remaining wall time, a reserve for verification and finalization, and the expected tail of later stages. This is more reliable than assigning independent static timeouts that can sum beyond the user-facing deadline. At fan-out, the critical path is the longest dependency chain, not the sum of all branch durations, but concurrency may increase queueing and contention. [4][7]

Percentiles are essential because averages hide the worst user-visible behavior. Measure p50, p95, and p99 by task class, model, tool, and outcome. Avoid averaging percentiles across services or combining interactive requests with overnight jobs. Dean and Barroso show why a small probability of component slowness can dominate a request that touches many components. Google SRE accordingly recommends defining latency SLOs in terms that reflect the user experience. [4][6]

### Iteration Caps and Early Stopping Must Use Evidence

Iteration caps prevent open-ended planning, retry, reflection, search, and delegation loops. Useful counters include maximum model turns, maximum equivalent actions, maximum failed validations, maximum retries per failure class, maximum subagents, and maximum depth. A terminal status should distinguish verified success, budget exhaustion, deadline, policy denial, dependency failure, user cancellation, and internal error. Collapsing these into `failed` prevents diagnosis and encourages blind retry. [1][15]

A cap alone is arbitrary truncation. Early stopping should instead use observable progress. The agent may continue while the expected value of another step exceeds its marginal cost and remaining constraints permit it. Practical signals include discovery of new evidence, reduction in unresolved acceptance criteria, successful verification, changed tool results, or a new recovery strategy. Repeating an equivalent call with unchanged inputs and preconditions is evidence of a loop, not progress. Anthropic reports finding agents that continued after sufficient results or searched endlessly for nonexistent sources; its response was to add effort-scaling heuristics and observe decision patterns. [11]

The author's synthesis is a three-part stop rule. Stop successfully when external checks satisfy the task contract. Stop with a bounded partial result when the remaining work cannot fit the envelope but the partial artifact is safe and useful. Stop without acting when the run lacks evidence or authority for a consequential operation. This distinguishes efficient planning from merely consuming the full budget and distinguishes graceful abstention from a crash at the limit.

### Concurrency Trades Wall Time for Capacity, Cost, and Tail Risk

Parallel execution can reduce wall time when branches are independent. OpenAI's latency guidance recommends parallelizing independent operations and making fewer serial requests. Anthropic reports that running three to five research subagents in parallel and allowing parallel tool calls cut research time by up to 90 percent for its complex queries. This is a vendor case on a specific system, not a general guarantee. The same case reports substantially higher token use, so elapsed-time improvement did not imply lower total work. [7][11]

Concurrency must therefore have a budget of its own. Bound live branches per run, per tenant, per model, and per external tool. Apply queue limits, fair scheduling, rate limits, and backpressure before launching work. Preserve dependency information so only independent branches run concurrently. Duplicate searches, competing writes, and parallel retries can increase cost or corrupt state without reducing the critical path. The worst case is amplification: a slowdown triggers retries, retries increase load, and load deepens the slowdown. Google recommends exponential backoff with jitter and graceful load shedding to dampen such feedback. [6]

Concurrency should be evaluated with both work and time metrics: total model calls, total tokens, tool calls, compute-seconds, monetary cost, wall time, queue time, and success. A design that is twice as fast but fifteen times as expensive may be correct for a rare high-value investigation and incorrect for routine support. The resource envelope makes that trade explicit rather than embedding it in an orchestration pattern. [2][11]

### Caching Saves Repeated Work Only When Reuse Is Real

Caching can operate at several layers. Prompt-prefix caching reuses processed model context. Response caching reuses a completed deterministic or sufficiently stable result. Retrieval and tool caches reuse external observations under a freshness policy. Artifact caches reuse builds, embeddings, or parsed documents. Each cache needs a key, scope, validity rule, privacy boundary, maximum age, invalidation method, and measurement of hits, misses, writes, and avoided work.

Provider prompt caches illustrate why economics must be measured rather than assumed. Anthropic documents cache writes priced above ordinary input tokens and cache reads at a fraction of the base rate; OpenAI likewise documents separate cache-write and cache-read usage and recommends measuring cached tokens, write tokens, latency, and realized cost. The break-even point depends on prefix length, write price, read price, reuse count, and time-to-live. A cache that is continually written and rarely read can increase cost. [8][9]

Prompt layout affects reuse because stable prefixes must remain stable. Tool definitions, policies, and shared instructions should precede dynamic data when the provider's caching contract uses prefix matching. But cache preservation must not keep stale facts or excessive history merely to improve the hit rate. The author's synthesis is that cache-hit rate is an operational metric, not a product objective: accept a lower hit rate when freshness, authorization, or context quality requires new data. [7][8][9]

### Model Routing Is a Policy With a Quality Floor

Model routing sends different tasks or stages to different models. A simple policy maps known task classes to fixed tiers. A learned router predicts whether a smaller model is sufficient. A cascade tries a cheaper model and escalates when an independent criterion rejects the result. Routing should optimize an explicit objective under constraints, such as minimizing expected cost subject to a task-success floor and latency SLO.

RouteLLM trained routers on preference data to choose between stronger and weaker models. Its ICLR 2025 paper reports more than a twofold cost reduction on public benchmarks without loss of the measured response quality, and its detailed experiments show that the trade-off varies by dataset and target quality. The result supports routing as a cost-quality tool under evaluated conditions; it does not justify assuming that a router transfers to every agent task, policy regime, or tool trajectory. [3]

The router itself needs evaluation and fallback. Measure quality by route, false-cheap assignments, unnecessary escalation, routing latency, and distribution drift. High-consequence actions may require a stronger model or independent verifier regardless of predicted difficulty. A failed cheap-model chain should not consume the entire budget before escalation, and forwarding erroneous intermediate content can contaminate later reasoning. The author's synthesis is to reserve budget for verification and one fresh escalation path rather than assigning the full envelope to the first route.

### Graceful Degradation and Circuit Breakers Bound Failure Amplification

Graceful degradation preserves the most valuable safe function when the preferred path cannot meet its envelope. An agent may return a cached read, use a smaller context, disable optional enrichment, reduce fan-out, switch to a qualified cheaper model, produce a draft without publishing, or ask for later asynchronous completion. The fallback must be declared in the task contract and labeled to the user. A silent reduction in verification or safety is not graceful degradation; it is an undisclosed change in service semantics. [6][13]

A circuit breaker protects a dependency or agent path that is persistently failing. Microsoft's architecture pattern defines closed, open, and half-open states: ordinary calls pass while closed, repeated failure opens the circuit and fails fast, and a limited probe in half-open determines whether normal traffic may resume. The pattern differs from retry. Retry expects a transient fault to clear; the circuit breaker prevents repeated work against a dependency likely to fail. Microsoft's example combines the breaker with cached or default responses and telemetry. [13]

Agents need breakers around model providers, tools, tenants, task classes, and sometimes the whole agent version. Trip signals can include sustained timeouts, rate-limit responses, policy violations, cost-budget overruns, invalid tool calls, or error-budget burn. Opening the breaker should cancel or prevent new work, not erase durable task state. Half-open probes need small, explicit budgets. This is the author's adaptation of the distributed-systems pattern to agent runtimes; the exact thresholds must be derived from observed failure and recovery distributions. [5][13][15]

### Resource SLOs Join Reliability and Efficiency

A resource SLO states the proportion of valid tasks that should satisfy both an outcome criterion and a resource criterion over a window. Examples include: 95 percent of verified support resolutions complete within 12 seconds; 99 percent of successful routine tasks cost no more than a stated amount; and 99.9 percent of runs terminate before their hard wall-time limit. Task classes should have separate targets because interactive support, repository maintenance, and long-running research have different value and latency constraints. [5][15]

Do not combine every dimension into one opaque score for operations. A composite score can rank experiments, but production gates should preserve success, cost, latency, policy violations, and failure severity as separate indicators. Otherwise improvement in a cheap dimension can conceal deterioration in a critical one. AgentSLABench's efficiency-adjusted success rate is one proposed research metric; its own resource profile remains valuable because it exposes each dimension and budget utilization separately. [1]

An error budget can then govern change. When latency or task-success error budgets burn too quickly, pause risky releases and investigate. When cost per success breaches its objective, reduce optional work, inspect loops and routing, or revise the unit-economics assumption. A monetary limit should not be called an error budget when it is simply a monthly cap; reliability error budgets describe tolerated SLO misses, while spending budgets describe allowed resource consumption. Keeping the terms separate makes both controls auditable. [5][6][14]

## Evidence

### Cost-Controlled Agent Evaluation Changes Which Designs Look Efficient

Kapoor, Stroebl, Siegel, Nadgir, and Narayanan re-evaluated coding agents and simple baselines rather than accepting leaderboard accuracy alone. Their method measured accuracy, dollar inference cost, and running time, repeated stochastic evaluations, and plotted designs on an accuracy-cost plane. They also modified DSPy optimization on HotPotQA so the search objective included cost as well as accuracy. The study found almost two orders of magnitude of cost variation among agents with substantially similar accuracy; Reflexion and LDB cost more than 50 percent above one simple warming baseline, while LATS cost more than fifty times as much. Joint optimization reduced cost while maintaining measured HotPotQA accuracy. [2]

The result supports two operational conclusions. First, budgets belong in the evaluation protocol, because repeated calls and search can buy benchmark accuracy. Second, efficiency is a frontier rather than one scalar: a more expensive system can be rational when its incremental quality is worth the expense. The study does not establish one universal price threshold, because provider prices and application value differ. It instead supplies a method: record raw consumption, use current dollar cost for deployment decisions, compare systems under common constraints, and expose dominated designs. [2]

### AgentSLABench Profiles Multiple Resources Under Declared Limits

AgentSLABench proposes a sealed, containerized benchmark for six agentic task types. Its profiling protocol launches a task environment with CPU, memory, and network constraints; runs the agent episode; measures resources; judges correctness; and writes a JSONL profile. Reported dimensions include success and task metrics, wall time and latency percentiles, API cost and tokens, peak memory and CPU, HTTP calls and network bytes, and safety or policy violations. Its efficiency-adjusted success rate multiplies task success by penalties when actual latency, cost, or memory exceeds the declared budget. [1]

This method makes resource violations visible even when an agent completes the task. The paper reports distinct resource profiles across tasks: a code-generation workload was highest in API cost in the reported setup and operated near its latency budget, while browsing workloads produced more network calls. Those findings are limited by the paper's selected agents, tasks, models, prices, and container environments. More importantly, EASR's multiplicative penalties encode a normative choice about how dimensions should trade off. Production teams should retain the underlying profile and hard constraints rather than adopting one composite formula without validating it. [1]

### RouteLLM Demonstrates Measured Model-Tier Routing

Ong and colleagues trained several binary routers using preference data to choose between a stronger and a weaker model. Their method included matrix-factorization, similarity-weighted, BERT-classifier, and causal-model routers; evaluation measured quality-cost trade-offs on public datasets and examined transfer to model pairs not used for training. The ICLR 2025 paper reports that routing reduced cost by more than twofold without sacrificing its measured response quality and generalized to unseen strong-weak pairs. Detailed results vary across tasks, confirming that no one threshold dominates every quality target. [3]

The evidence supports routing only when the router is evaluated on the deployment's task distribution and quality criteria. The router adds its own inference, latency, and failure mode, although the paper reports small routing overhead relative to expensive model generation in its setup. Agent workflows create a further complication: the cost of a route includes later retries, tools, and verification, not merely the first model call. Resource governance should therefore learn or measure whole-run cost by route and reserve a fallback when a cheap assignment fails. This extension is the author's synthesis beyond the paper's binary-response evaluation. [3]

### Tail-Latency Research Explains Why Means Are Insufficient

Dean and Barroso analyzed latency variability in large online services and described techniques for building a predictable whole from variable components. Their evidence included production and benchmark cases involving fan-out. In one reported BigTable experiment, hedging requests after a delay reduced the 99.9th-percentile latency for reading 1,000 keys from 1,800 milliseconds to 74 milliseconds while increasing requests by about 2 percent. The method does not imply that every agent should duplicate expensive calls; it demonstrates that tail mitigation has a measurable load cost and must be applied selectively. [4]

For agents, the relevant inference is structural. Serial calls accumulate round trips, fan-out waits on stragglers, and retries can improve the tail while consuming additional model or tool capacity. The correct experiment records the full latency distribution and total work under a fixed success criterion. A policy that lowers p99 by issuing speculative model calls may be worth its cost for an interactive high-value task and unacceptable for a cheap background workflow. [4]

### Production Cases Show Both the Value and Cost of Parallelism and Caching

Anthropic's research-agent engineering report provides a production case rather than a controlled independent study. It reports that parallel lead-agent fan-out and parallel tool calls reduced complex-query research time by up to 90 percent. It also reports that its agents and multi-agent system consumed substantially more tokens than chat interactions, and that token use explained much of the variance in one research evaluation. The case therefore demonstrates both sides of the resource trade: parallel work can improve coverage and wall time, but a success gain partly purchased by additional tokens must be reported as such. [11]

Provider caching documentation provides another measurable case. Anthropic and OpenAI publish separate prices for cache writes and reads and expose usage fields for cached and written tokens. Both recommend measuring actual cache behavior. These contracts make a break-even calculation possible, but the result depends on provider, model, prefix stability, time-to-live, and reuse. The evidence supports an experiment that compares realized cost and latency before and after caching, not a general claim that caching is always cheaper. [8][9]

### Observability and SLO Practice Supply the Operational Control Loop

OpenTelemetry's GenAI semantic conventions standardize model identity, operation duration, token usage, and agent or tool spans. Its official example uses latency histograms and token-usage histograms to compare models, detect regressions, and estimate per-request cost, while omitting prompt and tool content by default because those fields can contain sensitive data. This supplies a portable telemetry substrate, not a complete budget engine: enforcement and price attribution still belong to the application or gateway. [12]

Google's SRE guidance supplies the operational loop around those measurements. Service-level indicators are compared with objectives; error-budget consumption informs action; user-visible latency should be measured from the user perspective; overload should produce controlled degradation and load shedding; and retry behavior should avoid amplification. Microsoft's circuit-breaker pattern supplies a state machine for failing fast around a persistently unhealthy dependency. Together these sources support a governed run loop in which telemetry is not merely retained for postmortem analysis but drives throttling, degradation, release controls, and recovery. [5][6][13]

## Implications

### For Agent Architects

Design the resource envelope before selecting the orchestration pattern. List the task's value, required evidence, unacceptable failures, interactive or asynchronous deadline, maximum affordable cost, and resources that can cause shared harm. Then assign budgets to the root run and every child. A planning loop, verifier, or subagent should not exist outside this accounting tree. This reverses the common sequence in which an elaborate agent is built first and constrained only after a cost or latency incident. [1][2][11]

Make every terminal state explicit. `success` should require external evidence. `degraded` should identify which optional capability was omitted. `budget-exhausted` should identify the limiting dimension and consumed amount. `blocked` should identify the missing dependency or authority. `failed` should identify an error class. These statuses let callers decide whether to accept a partial result, retry with a new budget, route to a person, or stop. An unlabeled partial answer encourages the next layer to treat resource exhaustion as correctness.

Reserve resources for verification and finalization. If the planner can spend the entire token, call, and wall-time envelope, the system may reach a plausible result with no capacity left to test, read back, or communicate it. The author's recommendation is to partition each hard budget into planning and execution, recovery, verification, and closeout reserves, then release unused reserves only through a declared policy. This is an architectural synthesis from cost-controlled evaluation and harness control principles. [1][2][15]

### For Platform and Infrastructure Teams

Provide one governed gateway for models and one governed dispatcher for tools. The gateway should count token classes, model calls, cached usage, prices, rate limits, and remaining budget before accepting a request. The dispatcher should count calls, enforce timeouts and concurrency, attach idempotency keys where side effects are possible, and propagate deadlines. The execution environment should enforce CPU, memory, disk, process, network, and wall-time limits independently of the model. [1][12][15]

Implement backpressure before overload becomes collapse. Bound queues, reject or defer low-priority work, and prevent a single tenant or recursive fan-out from consuming every worker. Retries must have failure-class rules, backoff, jitter, and a total retry budget. Circuit breakers should fail fast around unhealthy model or tool dependencies and expose state changes to monitoring. Graceful fallbacks may serve cached information, remove optional enrichment, or convert synchronous work to asynchronous work, but they must not bypass policy or falsify completion. [6][13]

Keep telemetry and content governance separate. Token counts, durations, model names, call identities, and terminal reasons can often be retained broadly. Prompts, tool arguments, retrieved documents, and outputs may contain private data or secrets and need stricter capture, access, and retention rules. OpenTelemetry omits content by default in its GenAI example for this reason. Cost observability does not justify a permanent archive of every payload. [12]

### For Evaluation and Research Teams

Publish the complete resource contract with every agent result. At minimum include model and version, harness, task set, token and call limits, timeout, retry policy, concurrency, tool availability, cache state, prices or raw usage, number of trials, and the grader. Report success, latency percentiles, cost per attempt, cost per success, tool and model calls, and safety-critical failures. A headline accuracy without the search budget is not a reproducible agent result. [1][2]

Compare systems under more than one envelope. A tight interactive envelope may favor a small routed workflow; a longer high-value investigation may justify parallel subagents. Plot Pareto frontiers rather than selecting one universal winner. Audit whether a result improves because of architecture, model choice, extra sampling, or a wider budget. If an optimization changes both the agent and the evaluator, treat the result as unverified until an unchanged external judge tests it. [2][3]

Do not reward arbitrary truncation. A system that hits a cap and returns an unverified answer is not efficient merely because it spent less. Include abstention, partial completion, and verification status in the grader. Conversely, do not reward unconstrained search by allowing repeated trials without accounting. The objective is verified value per resource unit under a declared failure tolerance, not minimum spend or maximum success in isolation.

### For Product, Finance, and Governance Teams

Define unit economics around value-bearing outcomes. Cost per message may be convenient but can reward fragmentation or conceal task difficulty. Cost per verified resolution, accepted patch, completed report, or policy-compliant transaction connects consumption to value. Preserve task-class slices so easy work does not subsidize hard work invisibly, and document how shared infrastructure is allocated. [14]

Set policy for who can raise a budget. Automatic escalation can be allowed inside a narrow reserve for selected task classes. A larger increase should require a caller, operator, or business rule with authority to trade cost or latency for expected value. Log the old envelope, new envelope, reason, actor, and outcome. Otherwise a hard limit becomes a suggestion that the agent can negotiate with itself.

Budget breaches should trigger more than an invoice alert. Repeated breaches can freeze a release, reduce concurrency, disable an expensive route, open a circuit breaker, or require redesign. The response should depend on severity and reversibility. A one-off high-value research run may be approved; systematic cost growth without a corresponding outcome gain indicates a unit-economics or architecture failure. Google SRE's use of error budgets to change release behavior provides the governance analogy, while FinOps supplies the cost-allocation discipline. [5][6][14]

### For Operators

Operate from distributions and traces, not anecdotes. Watch task success, p50/p95/p99 latency, cost per attempt and success, budget-exhaustion rate, cache hit and write rates, routing decisions, queue age, concurrency, retry count, circuit state, and terminal reasons. Break these down by agent version, task class, model, tool, tenant, and deployment. A fleet-wide average can remain stable while one route develops a severe tail or one customer triggers runaway fan-out. [4][12]

When a budget alarm fires, locate the first divergent span. Determine whether the increase came from larger inputs, longer outputs, changed model routing, cache misses, duplicated tools, retries, queueing, or a new task mix. Do not reduce the cap first and call the incident solved; that can convert expensive successful runs into cheap silent failures. Change the underlying cause or explicitly change the service contract, then verify the original failure would have been prevented.

Test degradation and recovery deliberately. Inject tool timeouts, provider rate limits, slow model responses, cache misses, network denial, memory pressure, and partial child failure. Verify that deadlines propagate, retries remain bounded, circuit breakers open, optional work is shed, durable state remains recoverable, and user-visible status is accurate. A budget policy that has never been exercised under failure is configuration, not demonstrated control. [6][13][15]

### A Minimum Resource-Governance Record

The author's synthesis is that every agent run should leave a compact record with: run and parent identifiers; task and tenant class; agent, harness, model, tool, and policy versions; initial and amended budgets; input, output, reasoning, cache-read, and cache-write tokens; model and tool calls; wall time and stage percentiles; CPU, memory, disk, and network usage where relevant; direct and allocated cost; cache and routing decisions; retry and concurrency counts; terminal reason; verification evidence; and any degradation or budget override. [1][12][14][15]

This record makes the central question answerable: did the system produce a verified outcome with an acceptable resource profile, or did it merely stop? Reliable tool-using systems require the first standard. Budgets are therefore not constraints opposed to capability. They are the mechanism that makes capability comparable, deployable, and governable.

## Sources

1. Madiraju, M. B., and Madiraju, M. S. P. (2026). "AgentSLABench:
   Evaluating and Benchmarking Agentic Systems Under Resource Constraints."
   arXiv:2608.00805v1. https://arxiv.org/html/2608.00805v1 [high]

2. Kapoor, S., Stroebl, B., Siegel, Z. S., Nadgir, N., and Narayanan, A.
   (2025). "AI Agents That Matter." Transactions on Machine Learning
   Research. https://arxiv.org/html/2407.01502v1 [high]

3. Ong, I., Almahairi, A., Wu, V., Chiang, W.-L., Wu, T., Gonzalez, J. E.,
   Kadous, M., and Stoica, I. (2025). "RouteLLM: Learning to Route LLMs
   from Preference Data." ICLR 2025.
   https://proceedings.iclr.cc/paper_files/paper/2025/hash/5503a7c69d48a2f86fc00b3dc09de686-Abstract-Conference.html [high]

4. Dean, J., and Barroso, L. A. (2013). "The Tail at Scale."
   Communications of the ACM, 56(2), 74-80.
   https://research.google/pubs/the-tail-at-scale/ [high]

5. Google. "Service Level Objectives." Site Reliability Engineering.
   https://sre.google/sre-book/service-level-objectives/ [high]

6. Google. "A Collection of Best Practices for Production Services."
   Site Reliability Engineering.
   https://sre.google/sre-book/service-best-practices/ [high]

7. OpenAI. "Latency Optimization." Official API documentation.
   https://developers.openai.com/api/docs/guides/latency-optimization [high]

8. OpenAI. "Prompt Caching." Official API documentation.
   https://developers.openai.com/api/docs/guides/prompt-caching [high]

9. Anthropic. "Prompt Caching." Official Claude Platform documentation.
   https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching [high]

10. Anthropic. (2024). "Building Effective Agents." Official engineering
    guidance. https://www.anthropic.com/engineering/building-effective-agents [high]

11. Anthropic. (2025). "How We Built Our Multi-Agent Research System."
    Official engineering case study.
    https://www.anthropic.com/engineering/multi-agent-research-system [high]

12. OpenTelemetry. (2026). "Inside the LLM Call: GenAI Observability with
    OpenTelemetry." Official project documentation and example.
    https://opentelemetry.io/blog/2026/genai-observability/index.md [high]

13. Microsoft. "Circuit Breaker Pattern." Azure Architecture Center.
    https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker [high]

14. FinOps Foundation. "Unit Economics Playbook: Calculate the Unit Cost."
    Practitioner guidance on allocation and value-based unit cost.
    https://www.finops.org/pro/unit-economics-playbook-calculate-the-unit-cost [medium]

15. Microsoft Agent Governance Toolkit. "Agent SRE Governance -- Version
    1.0." Open-source specification for agent SLOs, error budgets, traces,
    and bounded resource use.
    https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/specs/AGENT-SRE-GOVERNANCE-1.0.md [medium]

## See Also

- `library/coding-agentic-ai/agent-evaluation-and-benchmarking.md` -- explains why cost, latency, reliability, and the evaluation contract must accompany task success.
- `library/coding-agentic-ai/agent-harness-design.md` -- locates budgets, deadlines, stop rules, dispatch, and recovery in the runtime around the model.
- `library/coding-agentic-ai/agent-observability-and-debugging.md` -- develops the traces and span metrics needed for attribution and incident diagnosis.
- `library/coding-agentic-ai/context-window-management.md` -- covers selection and compression of the prompt resource consumed on each model call.
- `library/coding-agentic-ai/multi-agent-orchestration.md` -- shows how delegation and parallelism create child budgets and coordination overhead.
- `library/coding-agentic-ai/tool-use-and-function-calling.md` -- defines the execution boundary where call, timeout, retry, and side-effect budgets are enforced.
