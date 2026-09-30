---
name: agent-planning-and-task-decomposition
id: 20260929T230339Z
tier: library-topic
domain: coding-agentic-ai
author: Librarian
tags: [agent-planning, task-decomposition, plan-and-execute, dependency-graphs, replanning, completion-criteria, agent-reliability]
links: [library/coding-agentic-ai/agent-harness-design.md, library/coding-agentic-ai/multi-agent-orchestration.md, library/coding-agentic-ai/agent-cost-latency-and-resource-governance.md, library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md, library/coding-agentic-ai/agent-evaluation-and-benchmarking.md]
reviewed: 2026-09-30
---

# Agent Planning and Task Decomposition -- Reliable Autonomy Requires Executable Work Units and Replanning

Agent planning converts an open-ended goal into bounded work units whose dependencies, inputs, outputs, and completion conditions can be inspected before the system claims success. Research distinguishes reactive action selection, plan-first execution, search over alternative plans, external-planner assistance, and adaptive decomposition; no one pattern is reliable for every task or environment. [1][2][5][7] The author's synthesis is that a natural-language plan should be treated as a revisable hypothesis about how to reach a verified state, not as evidence that the state has been reached.

## Background

Planning has a narrower engineering meaning than producing a plausible list of steps. An agent starts with a goal expressed at one level of abstraction, observes only part of the relevant state, and has a set of actions whose availability, cost, and consequences may not be known until execution. Planning links those elements by selecting intermediate objectives, ordering or relating them through dependencies, assigning executable actions, and defining what evidence would show that each objective is complete. The survey by Huang et al. organizes LLM-agent planning work into task decomposition, selection among multiple plans, external planner-aided planning, reflection, and memory, which shows that generating one sequence is only one part of the field. [1]

Early prompting work established a basic decomposition pattern. Plan-and-Solve asks a model first to divide a problem into smaller subtasks and then to carry out those subtasks, addressing missing reasoning steps observed in zero-shot chain-of-thought prompting. Its experiments concerned reasoning datasets rather than long-lived tool environments, but the method made a useful distinction explicit: deciding the structure of work and performing the work are different operations. [3] HuggingGPT applied a similar distinction to tool orchestration by separating task planning, model selection, task execution, and response generation. Its planner represents execution order and resource dependencies before expert models execute the assigned subtasks. [4]

A reactive alternative appeared in ReAct. Rather than committing to a complete plan before contact with the environment, ReAct interleaves reasoning, an action, and the resulting observation. The observation can correct the next decision, so the system can update an implicit plan as facts arrive. ReAct improved results in the paper's knowledge and interactive decision tasks, but its one-step-at-a-time structure can require repeated model calls and can obscure global dependencies when a task contains many independent or conditionally related branches. [2][8] The distinction is therefore not planning versus no planning. It is advance commitment to a larger structure versus repeated local planning from fresh observations.

Long-horizon work exposed the limits of both extremes. A fixed plan can contain a subtask that is too broad, impossible, or inconsistent with the current environment. A purely reactive loop can spend context and calls rediscovering the global objective, repeat equivalent actions, or choose locally sensible steps that do not close the task. ADaPT directly compares iterative executors with plan-and-execute systems and responds by decomposing a subtask further only when the executor cannot complete it. [7] Plan-and-Act instead separates a high-level planner from a low-level executor and trains the planner with plans derived from successful trajectories, preserving a global roadmap while allowing the executor to translate it into environment-specific actions. [11]

Dependency representation became important once agents could call several tools or workers. HuggingGPT records ordering and resource dependencies among subtasks, while LLMCompiler generates a directed acyclic graph of function calls, dispatches tasks when their dependencies are satisfied, and permits independent calls to run concurrently. [4][8] This structure separates logical order from textual order. Two tasks may appear next to each other in a written plan yet be independent, while a later task may require artifacts from several earlier branches. A dependency graph can make those facts explicit and can identify the critical path without requiring every task to run serially.

Classical planning research also supplied a warning about fluent plans. Valmeekam et al. evaluated models on planning domains derived from International Planning Competition settings. The best tested model averaged about 12 percent success in autonomously producing executable plans, while performance was more promising when model outputs guided sound planners or were checked by external verifiers that returned corrective feedback. [5] Tree of Thoughts showed a complementary result: deliberate search over multiple intermediate reasoning paths can greatly improve selected bounded problems compared with a single chain, but it does so by adding generation, evaluation, and search work. [6] Together these studies support external state checks and search where the task warrants them; they do not support treating model-generated text as a sound planner by default.

Production reports frame decomposition as an operating decision rather than a universal virtue. Anthropic distinguishes predefined workflows from agents that dynamically direct their own tool use, recommends prompt chaining for cleanly decomposable tasks, and describes orchestrator-worker systems for tasks whose subtasks cannot be known in advance. It also advises obtaining environmental ground truth during execution. [9] Its multi-agent research system reports that delegation quality depends on clear objectives, boundaries, source guidance, and output formats, while synchronous coordination simplifies state at the cost of information-flow bottlenecks and asynchronous coordination adds state-consistency and error-propagation problems. [10]

The domain boundary follows from these results. This topic concerns how an agent-engineering system represents, schedules, executes, checks, and revises work. It does not claim that language models possess general planning competence, prescribe one model architecture, or replace domain-specific planners, workflow engines, project management, or human judgment. The author's synthesis is that useful agent planning combines probabilistic proposal with deterministic control: the model can suggest decomposition and adaptation, while the harness owns current state, permissions, dependency release, budgets, action receipts, and terminal status. [5][8][9]

## Core Concepts

### A goal must become an acceptance contract

An open-ended instruction usually names an intended outcome without fully specifying observable completion. Before decomposition, the system needs a goal record containing the requested outcome, known constraints, non-goals, authorized resources, relevant environment, and evidence required for acceptance. Anthropic's workflow guidance places programmatic checks between prompt-chain stages, and its agent guidance says execution should obtain ground truth from tool results or code execution. [9] Valmeekam et al. similarly found that external verifiers could identify defects in generated plans and provide feedback for another attempt. [5]

The author's synthesis is to distinguish three statements. The goal says what state is wanted. The plan says which transitions are currently expected to produce it. The acceptance criteria say which observations will justify a completion claim. Conflating them creates a circular test in which the same model writes a plan, follows it, and declares it sufficient. A plan may be coherent while missing a user requirement; an action sequence may finish while the environment remains unchanged; and a valid intermediate artifact may still fail the final contract. [5][9]

Current state belongs in the contract because feasibility is state-dependent. A task such as updating a repository, booking an available resource, or collecting records depends on versions, permissions, inventory, prior side effects, and other facts that can change after planning. Reactive systems use observations after each action, while plan-and-execute systems need explicit refresh points before a step whose preconditions may have changed. [2][7][9] The authoritative state should come from the environment or durable system records, not from a remembered plan sentence.

### A work unit is an interface, not a sentence fragment

A useful work unit is small enough to assign and verify but large enough to produce a meaningful artifact or state transition. The author's synthesis is that it should record at least: an identifier; objective; parent goal; required inputs; preconditions; allowed actions and tools; dependencies; expected artifact or state change; completion check; budget; retry or escalation rule; and terminal status. HuggingGPT's structured tasks include arguments and resource dependencies, LLMCompiler records task dependencies for dispatch, and Anthropic's research system reports better delegation when workers receive objectives, output formats, source guidance, and clear boundaries. [4][8][10]

Granularity creates a trade-off. A unit that is too coarse pushes planning back into the executor, makes progress hard to measure, and lets one failure invalidate a large amount of work. A unit that is too fine increases coordination messages, model calls, context transfers, scheduling overhead, and opportunities for interface mismatch. ADaPT treats this as an adaptive problem: it decomposes further when the executor cannot perform a subtask, rather than forcing the same depth on every branch. Its analysis reports that decomposition depth changes with task complexity and executor capability. [7]

The completion check determines whether the unit is operational. "Research the topic" is not independently decidable; "produce a source table containing the required fields, with every URL fetched and every quotation linked to its source" is closer to a checkable unit. The first wording describes activity, while the second describes an artifact and tests. The author's synthesis is that an agent should prefer completion predicates based on observable state, schema validation, test results, counts, or human approval over predicates based on the model's confidence or narration. [5][9]

### Sequences, dependency graphs, and hierarchies encode different facts

A linear sequence is appropriate when each step consumes the previous step's output and the order is stable. Prompt chaining uses this form and can place a programmatic gate between calls. It improves tractability by giving each call an easier problem, but it adds serial latency and can propagate an early error through every later stage. [9] The plan should therefore identify which step results are authoritative inputs and which gate can stop downstream execution.

A dependency graph is appropriate when some work can proceed independently and other work joins multiple branches. LLMCompiler's planner generates tasks and dependencies, its fetching unit releases tasks when inputs are ready, and its executor runs independent functions in parallel. [8] HuggingGPT likewise represents resource dependencies so an output from one expert can become an argument to another. [4] A graph makes parallelism an effect of satisfied dependencies rather than a guess based on list position.

A hierarchy is appropriate when high-level objectives must remain stable while low-level methods vary. A parent node states an outcome; child nodes refine it into smaller outcomes or actions. Plan-and-Act formalizes a high-level planner and environment-specific executor, while ADaPT recursively expands a difficult subtask as needed. [7][11] The hierarchy should preserve a path from every leaf action to a parent acceptance criterion. Otherwise decomposition can generate locally executable work that no longer contributes to the original goal.

These forms can coexist. The author's synthesis is to represent the overall goal as a hierarchy, sibling dependencies as a graph, and each worker's immediate interaction as a short sequence. The important constraint is acyclicity or an explicit iteration rule. A hidden cycle such as "review until good" has no bound; an explicit evaluator-optimizer loop has a criterion, a revision budget, and a terminal status. Anthropic recommends evaluator-optimizer patterns when criteria are clear and feedback measurably improves the output. [9]

### Reactive, plan-first, and hybrid control allocate uncertainty differently

Reactive action selection commits only to the next step. ReAct interleaves reasoning and action so each observation can alter the next move. This is useful when the environment is uncertain, actions reveal information, or a complete plan would become stale quickly. [2] Its costs include repeated model inference, weak visibility into the global dependency structure, and the possibility of cycling through locally plausible actions.

Plan-first execution commits to a larger structure before acting. Plan-and-Solve demonstrates the cognitive version: divide the problem, then solve each part. HuggingGPT and Plan-and-Act apply explicit planner-executor separation to tool and web environments. [3][4][11] Advance planning can expose missing branches, preserve long-range constraints, and enable scheduling, but the plan may encode false assumptions before the agent has observed the state needed to validate them.

Hybrid control preserves a high-level roadmap while replanning lower levels from evidence. ADaPT expands a failed subtask recursively, and LLMCompiler supports replanning when intermediate results make a static graph insufficient. [7][8] The author's synthesis is that the replanning boundary should follow uncertainty: keep stable requirements and verified completed artifacts, refresh steps whose preconditions changed, and discard only the dependent portion of the plan. Rebuilding the entire plan after every observation wastes valid work; preserving every original step despite contradictory evidence turns the plan into a liability.

### Preconditions, postconditions, and artifacts make plans auditable

A precondition is a fact that must hold before execution, such as a file version, authenticated role, available input, or completed dependency. A postcondition is the observable state expected after the action. An artifact is a durable output that can be inspected or consumed later. LLMCompiler uses dependency placeholders that are replaced with preceding task outputs, and HuggingGPT transfers generated resources between tasks. [4][8] These mechanisms are narrow examples of a broader interface contract: do not release a unit until its required inputs exist and match the expected identity.

Preconditions should be checked at execution time, not merely when the plan is drafted. The environment may change while another branch runs, and a prior action may have partially succeeded. The author's synthesis is that the dispatcher should record the state version used for the decision, apply the action through an authorized tool, and read back the result before releasing dependent work. This design treats tool observations as evidence and aligns with Anthropic's requirement for environmental ground truth during agent execution. [9]

Artifacts reduce context loss by moving important state out of model conversation. Anthropic's multi-agent research system reports persisting the lead agent's plan to memory and using explicit handoffs when fresh contexts are needed. [10] A durable artifact can carry provenance, version, producer, checks, and dependency identity. A prose summary without those fields may help a reader, but it cannot safely substitute for the artifact when exact state matters.

### Replanning needs failure semantics and invalidation rules

Replanning begins with a classified mismatch, not with generic dissatisfaction. Useful classes include failed precondition, unavailable dependency, invalid action, tool error, partial side effect, failed verification, exhausted budget, changed requirement, and evidence that the causal plan was wrong. ADaPT replans through additional decomposition after execution failure; LLMCompiler regenerates plans for dynamic dependency graphs; ReAct updates behavior from each observation. [2][7][8]

The author's synthesis is that each failure class should name what remains valid. If one independent research branch fails, completed sibling artifacts need not be discarded. If a shared assumption is falsified, every descendant that relied on it must be invalidated. If an external action has uncertain status, the system should query its outcome before retrying. Replanning without invalidation rules can merge stale and current conclusions; retrying without outcome checks can duplicate side effects.

Budgets are part of replanning because every alternative consumes tokens, calls, time, and attention. Tree of Thoughts improves selected tasks by generating and evaluating multiple paths, while LLMCompiler gains efficiency by exposing parallelizable dependencies and reducing sequential calls. [6][8] Search breadth, decomposition depth, worker count, and retry count therefore need explicit limits. The system should reserve resources for verification and finalization rather than spend the full envelope generating more candidate plans.

### Planner, executor, and reviewer are roles with different evidence

The planner maps goals and current state into work units and dependencies. The executor performs one unit using allowed tools and returns observations or artifacts. The reviewer compares the resulting evidence with acceptance criteria and can accept, reject, or request a bounded revision. Plan-and-Act supplies empirical evidence for separating high-level planning from low-level action, while Anthropic describes evaluator-optimizer and orchestrator-worker workflows as distinct patterns. [9][11]

Separation does not require three different models or processes. It requires distinct inputs, authority, and outputs. The author's synthesis is that the planner should not mark an unexecuted task complete; the executor should not change the parent goal to fit an easier action; and the reviewer should not invent new requirements unrelated to the acceptance contract. A single runtime can enforce these role boundaries through typed stages, but high-consequence tasks may justify independent models, deterministic validators, or human review. [5][9]

Review closes a unit only when its evidence is sufficient. This prevents a common error chain: the planner emits a plausible step, the executor produces fluent output, and the synthesizer assumes success because no structured failure was reported. External verification improved the planning loop in Valmeekam et al., and Anthropic's production guidance places checks and environmental feedback inside workflows. [5][9] The general principle is that silence is not a passing result and an artifact is not accepted merely because it exists.

### A plan is a versioned hypothesis, not a guarantee

Natural language is useful for expressing intent, alternatives, and domain knowledge, but it does not by itself enforce action legality, state transitions, resource conservation, or goal satisfaction. The approximately 12 percent autonomous executable-plan result in the evaluated classical domains is direct evidence against treating fluent plans as generally sound. [5] Plan-and-Act also states that accurate plans remain difficult because LLMs are not inherently trained for the target planning task, even though targeted planning data improved its tested web agents. [11]

The author's synthesis is to version the plan with the goal, observed state, planner and policy versions, creation time, assumptions, and dependency graph. Execution receipts should identify which plan version authorized an action. A replan should preserve completed verified nodes, supersede invalid nodes, and record why the revision occurred. This makes a plan auditable without elevating it to an immutable script.

The final status should describe evidence rather than intention: verified success, verified partial completion, blocked dependency, budget exhaustion, policy denial, cancelled, or failed. A stopped loop is not necessarily a completed plan, and a completed plan is not necessarily a satisfied goal. The author's synthesis is that the acceptance contract, current-state read-back, and reviewer decision jointly determine completion; the plan only organizes the attempt. [5][9]

## Evidence

### Reactive action selection grounds decisions but can remain locally myopic

ReAct tested interleaved reasoning and action on question answering, fact verification, ALFWorld, and WebShop. The paper reports that environmental interaction reduced hallucination and error propagation on knowledge tasks and that ReAct exceeded the cited imitation- or reinforcement-learning baselines by 34 percentage points on ALFWorld and 10 percentage points on WebShop with one or two in-context examples. [2] These experiments support feeding observations back into decisions. They do not establish that one-step reactive control is best for every long-horizon dependency structure, model, or tool environment.

Plan-and-Solve provides evidence at the reasoning rather than environment-control level. Across ten datasets and three reasoning problem types, its plan-first prompts outperformed zero-shot chain-of-thought in the reported GPT-3 experiments and were comparable with eight-shot chain-of-thought on mathematical reasoning. [3] The result supports explicit decomposition as a way to reduce missing steps in bounded reasoning. It does not test permissions, side effects, state drift, or recovery in a production agent.

### Search over alternatives can recover from early commitment at added cost

Tree of Thoughts represents partial solutions as nodes, generates multiple continuations, evaluates them, and permits lookahead or backtracking. On the paper's Game of 24 setup, GPT-4 with chain-of-thought solved 4 percent of tasks while Tree of Thoughts solved 74 percent; the paper also evaluates creative writing and mini crosswords. [6] The comparison shows that branching search can outperform one left-to-right chain on tasks with useful intermediate-state evaluation. The additional branches and evaluations also consume more inference work, so the evidence does not justify using search for a task whose next step is already cheap and externally checkable.

Valmeekam et al. provide a counterweight to demonstrations of fluent planning. Their benchmark used planning domains related to International Planning Competition problems and checked whether generated plans were executable. The best tested model averaged about 12 percent autonomous success, while LLM-generated guidance was more useful when combined with sound planners and external verifiers. [5] This supports a division of labor in which the model proposes heuristics or formalizations and a verifier checks state-transition validity.

### Structured decomposition supports specialized execution and data flow

HuggingGPT demonstrates a four-stage controller: task planning, model selection, task execution, and response generation. The planning stage decomposes a request, determines order and resource dependencies, and passes subtask outputs to later expert models. [4] Its contribution is architectural evidence that a planner can coordinate heterogeneous capabilities through structured interfaces. The paper's results are tied to the available expert models, descriptions, and benchmark tasks and therefore do not prove that the generated task graph is generally complete.

LLMCompiler tests dependency-aware scheduling more directly. Its function-calling planner forms tasks and dependencies, a fetching unit releases ready work, and an executor runs independent calls concurrently. The ICML paper reports up to 3.7 times latency speedup, up to 6.7 times cost savings, and about 9 percent accuracy improvement compared with ReAct across its evaluated workloads. [8] The system also includes replanning for tasks whose later graph depends on intermediate results. These results support explicit dependencies and parallel release when the workload contains real independent branches; they do not imply that parallelism helps stateful or side-effecting actions that require serialization.

### Adaptive granularity addresses executor failure

ADaPT evaluates recursive, as-needed decomposition against iterative and plan-and-execute baselines in ALFWorld, WebShop, and TextCraft. The paper reports improvements of up to 28.3 percentage points in ALFWorld, 27 points in WebShop, and 33 points in TextCraft and shows decomposition depth adapting to task complexity and executor capability. [7] The supported conclusion is that fixed granularity can be a failure source and that a planner can expand only the subtask an executor cannot handle. The exact gains are benchmark- and configuration-specific, and recursive decomposition still needs depth and interaction budgets.

Plan-and-Act tests a different intervention: training a planner to produce high-level plans inferred from successful trajectories while an executor maps those plans to actions. The ICML 2025 paper reports 57.58 percent success on WebArena-Lite and 81.36 percent for its text-only result on WebVoyager. [11] The separation supports maintaining long-horizon intent outside the executor's local action choice. The authors also identify accurate plan generation as difficult, so the result supports targeted training and structured execution rather than assuming any general model will produce a reliable plan from prompting alone.

### Production reports expose delegation and coordination costs

Anthropic's agent guidance reports recurring production patterns rather than controlled benchmark comparisons. It recommends prompt chaining for stable fixed decompositions, parallelization for independent work, orchestrator-workers when subtasks must be discovered dynamically, and evaluator-optimizer loops when clear criteria make revisions measurable. It also emphasizes simplicity, transparent planning, and tested tool interfaces. [9] This evidence is valuable for implementation pattern selection but remains vendor-authored experience rather than an independent estimate of effect size.

Anthropic's multi-agent research report states that its lead agent saves a plan, selects subagent count from query complexity, and gives workers explicit objectives, output formats, tool and source guidance, and boundaries. It also reports that synchronous execution creates bottlenecks while asynchronous execution complicates coordination, state consistency, and error propagation. [10] These observations support the claim that decomposition quality includes handoff design and concurrency control, not merely the number of subtasks.

### The combined evidence favors conditional architecture choices

The studies do not identify one dominant planner. Reactive execution gains fresh evidence but can pay serial cost. Plan-first separation preserves global structure but can encode false assumptions. Search can escape early commitment but multiplies inference. Recursive decomposition can match granularity to failure but can expand without bounds. Dependency graphs enable concurrency but require accurate edges and artifact interfaces. External planners and verifiers increase soundness when a formal state model exists but add translation and integration work. [2][5][6][7][8][11]

The author's synthesis is that planning quality should be evaluated at three levels: plan validity before execution, trajectory quality during execution, and verified outcome after execution. Metrics should include task success, invalid or skipped preconditions, dependency errors, replans, repeated actions, tool and model calls, token and monetary cost, latency, reviewer rejection, and failure severity. The cited evidence shows that success rate alone cannot explain whether a system improved through better decomposition, more search, greater spend, or a stronger verifier. [5][6][7][8]

### Planning-specific diagnostics separate planning errors from execution outcomes

Sun et al.'s 2026 Agent Planning Benchmark (APB) provides planning-specific diagnostic evidence that complements end-to-end agent results. APB contains 4,209 multimodal cases across 22 domains and five settings. It evaluates complete long-horizon plans, feedback-conditioned step-wise plans, and robustness when the tool set contains irrelevant tools, broken tools, or tasks that cannot be solved from the available information. Across 12 multimodal language models, the authors report systematic weaknesses in long-horizon planning, tool-noise robustness, calibrated refusal, and inference-time refinement. [12]

The authors also tested whether the diagnostic signal transferred to execution. On 200 ToolSandbox tasks and 200 tau^2-bench tasks, APB-guided refinement improved plan correctness, plan grade, and downstream execution metrics across three representative models. [12] This supports evaluating planning separately before asking whether a full agent succeeded, but it does not make planning scores substitutes for deployment evidence. The paper states that its cases cannot exhaust real task diversity, that planning diagnostics should complement rather than replace end-to-end benchmarks, and that parts of the data and judging pipeline rely on proprietary foundation models despite human verification. [12]

## Implications

### For agent architects

Design backward from the terminal evidence. The author's synthesis is to write the acceptance contract first, identify the environment queries or tests that can establish it, and then decompose only enough work to produce those observations. This reverses the failure-prone pattern of generating an elaborate plan and searching afterward for a way to declare it complete. External verification results and production guidance both support making checks independent of the planner's prose. [5][9]

Choose a control pattern from task properties. Use a short reactive loop when observations arrive quickly and invalidate future actions. Use a fixed sequence when the stages and gates are stable. Use a dependency graph when independent branches and join points are known. Use a hierarchy when stable high-level goals need environment-specific refinement. Add alternative-plan search when early choices are consequential and intermediate states can be evaluated. Add an external planner or verifier when soundness matters and the domain can be represented formally. [1][2][5][6][8][9]

Keep the planner's authority narrow. It may propose tasks, dependencies, budgets, and alternatives, but the harness should validate schemas, permissions, preconditions, and resource availability before dispatch. The executor should return typed status and evidence rather than only narrative output. The reviewer should compare those results with the original acceptance contract and name any failed criterion. This role separation follows the planner-executor and evaluator patterns in the research and production sources. [5][9][11]

### For task and handoff designers

Define each unit by its boundary conditions. The author's synthesis is to require an objective, inputs, preconditions, dependencies, allowed actions, output schema, completion check, budget, and failure route. When assigning work to another agent, include the source and destination of every artifact and preserve the parent requirement. Anthropic reports that detailed worker descriptions reduce duplicate work and gaps, while HuggingGPT and LLMCompiler demonstrate machine-readable dependency transfer. [4][8][10]

Use adaptive granularity rather than one global step size. Start with the coarsest unit that has a credible executor and completion check. Expand it when the executor reports a classified inability, not merely because the planner can imagine more steps. Cap depth, total units, and replans. ADaPT supports as-needed expansion, but any recursive policy can exhaust its budget if failure produces unbounded child generation. [7]

Do not use decomposition to hide uncertainty. If a requirement is ambiguous, splitting it into ten precise-looking steps preserves the ambiguity beneath additional text. If a precondition is unknown, create an information-gathering unit whose output resolves it. If no observable completion test exists, route the decision to a qualified reviewer or label the result provisional. The author's synthesis is that every child should reduce uncertainty, produce an artifact, or move the environment toward a verified state; otherwise it is coordination overhead.

### For harness and workflow engineers

Store the plan outside the transient prompt and treat it as versioned state. The record should include plan version, goal version, current-state snapshot, assumptions, node statuses, dependencies, artifacts, budgets, and revision history. Anthropic's research system persists plans and uses explicit handoffs to survive context limits, while LLMCompiler and HuggingGPT rely on structured dependency records to pass results. [4][8][10]

Make dependency release deterministic. A scheduler should release a node only when required predecessors have accepted status, their named artifacts exist, and execution-time preconditions pass. Independent read-only units can run concurrently; writes that share a target or depend on current state may require serialization. LLMCompiler's results demonstrate the upside of accurate parallelism, while Anthropic's report identifies state consistency and error propagation as costs of asynchronous execution. [8][10]

Implement invalidation as part of replanning. A changed assumption should identify all dependent nodes and artifacts; a local tool failure should not erase unrelated verified branches. Keep stable action identifiers for side effects and query uncertain outcomes before replay. Preserve the old plan for audit while marking superseded nodes. The author's synthesis is that a replan is a state migration with explicit validity rules, not an invitation to overwrite history.

### For resource and context governance

Attach budgets to the graph, not only the overall run. Each unit should have call, token, time, retry, and concurrency limits, while parent nodes reserve enough capacity for integration and verification. Tree search, recursive decomposition, and multi-agent fan-out can all improve coverage, but each expands work along a different dimension. [6][7][10] A parent planner should not grant every child the full root allowance because decomposition would multiply authority and cost.

Measure the critical path separately from total work. Parallel execution can lower wall time while increasing calls, tokens, and coordination. Serial reactive loops can minimize concurrent work while accumulating latency. LLMCompiler reports simultaneous gains in its tested workloads, but those gains depend on discovering true independence. [8] The author's synthesis is to report both elapsed time and total resource use, together with verified outcome and task class.

Protect context from plan sprawl. Store full artifacts and receipts durably, then give a worker only the parent objective, relevant inputs, constraints, and accepted upstream results. Anthropic's research report uses fresh subagents and handoffs as context grows. [10] A larger task graph does not require every worker to read the whole graph, but the coordinator must preserve global dependencies and acceptance criteria.

### For evaluators and reviewers

Evaluate the plan independently from the final answer. A plan-validity review asks whether steps are executable, dependencies are complete, preconditions are plausible, and terminal criteria cover the goal. A trajectory review asks whether the system followed authorized transitions, incorporated observations, avoided loops, and revised invalid assumptions. An outcome review asks whether the environment and artifacts satisfy acceptance criteria. Valmeekam et al. show why executable-plan checks matter, ReAct and ADaPT show why trajectory adaptation matters, and APB provides a planning-specific diagnostic layer that its authors validate against controlled execution tasks. [2][5][7][12]

Use adversarial state changes to test replanning. Remove a dependency, change an input after planning, make one branch fail, return a partial tool result, exhaust a child budget, and make an external side effect time out after uncertain completion. The expected result is not always success; it is a bounded, accurate terminal status with valid work preserved. The author's synthesis is that a planner is reliable when failure remains diagnosable and contained, not when a benchmark contains no surprises.

Compare architectures under common resource envelopes. A search method that samples many alternatives, a reactive method that makes many sequential calls, and a multi-agent method that fans out workers are not comparable from success rate alone. Record model and harness versions, prompts or planning policy, tool set, state representation, call and token budgets, parallelism, retries, verifier, number of trials, and failure categories. The cited papers report large gains under specific tasks and configurations, so generalization requires controlled replication. [5][6][7][8][11]

### For operators and governance teams

Expose plan status as evidence-backed state. Useful statuses include pending, ready, running, blocked, failed, superseded, accepted, and rejected, with a reason and artifact references. A dashboard or handoff should distinguish work that ran from work that passed. The author's synthesis is that the worst operational outcome is an agent that converts an uncertain partial trajectory into an unqualified success because the run ended without a structured failure.

Set escalation thresholds from consequence and reversibility. Low-risk information gathering can replan automatically within a small budget. A scope change, new external side effect, irreversible action, policy exception, or repeated verifier failure should require fresh authorization or human review. Production guidance supports environmental checks and carefully designed interfaces, while external-verifier research shows the value of authority outside plan generation. [5][9]

Retain plan versions, action receipts, artifacts, verifier results, and terminal reasons long enough to diagnose failures without storing unnecessary sensitive content. Review recurring invalid dependencies, coarse tasks, duplicate work, stale-state actions, and rejected completions, then adjust the decomposition policy or tool contract. The author's synthesis is that planning improves structurally only when trace evidence changes the system that produces future plans; adding more prose to the planner prompt without measuring the original failure does not establish improvement.

A dependable agent can still fail to complete a difficult goal. The engineering objective is narrower and testable: every action follows an authorized work unit, every dependency is represented, every plan revision responds to evidence, every budget is bounded, and every completion claim resolves to an independent observation. Research on reactive agents, explicit planners, tree search, adaptive decomposition, parallel task graphs, and external verification supports different parts of that objective but no single method supplies all of them. [2][5][6][7][8][11]

## Sources

1. Huang, X., Liu, W., Chen, X., Wang, X., Wang, H., Lian, D., Wang, Y., Tang, R., and Chen, E. (2024). "Understanding the Planning of LLM Agents: A Survey." arXiv:2402.02716.
   https://arxiv.org/abs/2402.02716 [high]

2. Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K. R., and Cao, Y. (2023). "ReAct: Synergizing Reasoning and Acting in Language Models." ICLR 2023.
   https://openreview.net/forum?id=WE_vluYUL-X [high]

3. Wang, L., Xu, W., Lan, Y., Hu, Z., Lan, Y., Lee, R. K.-W., and Lim, E.-P. (2023). "Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models." ACL 2023, pages 2609-2634.
   https://aclanthology.org/2023.acl-long.147/ [high]

4. Shen, Y., Song, K., Tan, X., Li, D., Lu, W., and Zhuang, Y. (2023). "HuggingGPT: Solving AI Tasks with ChatGPT and Its Friends in Hugging Face." NeurIPS 2023.
   https://proceedings.neurips.cc/paper/2023/hash/77c33e6a367922d003ff102ffb92b658-Abstract.html [high]

5. Valmeekam, K., Marquez, M., Sreedharan, S., and Kambhampati, S. (2023). "On the Planning Abilities of Large Language Models: A Critical Investigation." NeurIPS 2023.
   https://proceedings.neurips.cc/paper/2023/hash/efb2072a358cefb75886a315a6fcf880-Abstract-Conference.html [high]

6. Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T., Cao, Y., and Narasimhan, K. (2023). "Tree of Thoughts: Deliberate Problem Solving with Large Language Models." NeurIPS 2023.
   https://proceedings.neurips.cc/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract.html [high]

7. Prasad, A., Koller, A., Hartmann, M., Clark, P., Sabharwal, A., Bansal, M., and Khot, T. (2024). "ADaPT: As-Needed Decomposition and Planning with Language Models." Findings of NAACL 2024, pages 4226-4252.
   https://aclanthology.org/2024.findings-naacl.264 [high]

8. Kim, S., Moon, S., Tabrizi, R., Lee, N., Mahoney, M. W., Keutzer, K., and Gholami, A. (2024). "An LLM Compiler for Parallel Function Calling." ICML 2024, PMLR 235, pages 24370-24391.
   https://proceedings.mlr.press/v235/kim24y.html [high]

9. Anthropic. (2024). "Building Effective Agents." Official engineering guidance on workflows, agents, orchestration, evaluation, and agent-computer interfaces.
   https://www.anthropic.com/engineering/building-effective-agents [high]

10. Anthropic. (2025). "How We Built Our Multi-Agent Research System." Official engineering report on orchestrator-worker decomposition, delegation, context, evaluation, and production reliability.
    https://www.anthropic.com/engineering/multi-agent-research-system [high]

11. Erdogan, L. E., Lee, N., Kim, S., Moon, S., Furuta, H., Anumanchipalli, G., Keutzer, K., and Gholami, A. (2025). "Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks." ICML 2025, PMLR 267, pages 15419-15462.
    https://proceedings.mlr.press/v267/erdogan25a.html [high]

12. Sun, H., Wang, W., Song, M., He, J., Zhang, W., Liu, Y., Yang, Y., and Cheng, Y. (2026). "Agent Planning Benchmark: A Diagnostic Framework for Planning Capabilities in LLM Agents." arXiv:2606.04874v2.
    https://arxiv.org/abs/2606.04874v2 [high]

## See Also

- `library/coding-agentic-ai/agent-harness-design.md` -- runtime state, dispatch, recovery, verification, and stopping around the plan.
- `library/coding-agentic-ai/multi-agent-orchestration.md` -- worker topologies and coordination patterns used to execute decomposed work.
- `library/coding-agentic-ai/agent-cost-latency-and-resource-governance.md` -- budgets, concurrency, critical paths, and terminal states for planned runs.
- `library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md` -- a domain-specific evidence chain from task contract through planning, execution, and handoff.
- `library/coding-agentic-ai/agent-evaluation-and-benchmarking.md` -- outcome, trajectory, cost, and reliability evaluation for agent systems.

