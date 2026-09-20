---
name: agent-evaluation-and-benchmarking
id: 20260727T110435Z
tier: library-topic
domain: coding-agentic-ai
author: Researcher-1
tags: [agent-evaluation, benchmarking, swe-bench, gaia, webarena, eval-harness, pass-at-k, production-readiness]
links: [library/coding-agentic-ai/agent-skill-systems.md, library/coding-agentic-ai/multi-agent-orchestration.md, library/coding-agentic-ai/context-window-management.md]
reviewed: 2026-09-20
---

# Agent Evaluation and Benchmarking -- Reliable Measurement Requires More Than a Leaderboard Score

Agent evaluation measures whether a model, harness, tools, and environment jointly complete multi-step work under stated constraints. Public benchmarks are useful comparison instruments, but production readiness requires a broader evaluation system that measures outcomes, trajectories, consistency, cost, safety, and failures on the deployment's own task distribution [1, 6, 11, 12].

## Background

Language-model evaluation began mainly with fixed datasets and short interactions. A model received a prompt, produced one answer, and was scored against a reference answer or a deterministic rule. This design made experiments reproducible and model comparisons inexpensive, but it assumed that the evaluated object was the model response. Tool-using agents invalidate that assumption: their outputs depend on prompts, tool definitions, execution permissions, state transitions, retry policies, context handling, and stopping rules. Anthropic therefore defines an agent evaluation as a test of the model and harness together, not the model in isolation [11].

Code evaluation introduced an important intermediate step. HumanEval contains hand-written function-completion problems with unit tests and evaluates functional correctness rather than textual similarity. Chen et al. also introduced the pass@k estimator, which asks whether at least one among k generated programs passes the tests [2]. This was a methodological improvement because many distinct programs can satisfy a specification, while a reference-string metric could reject valid alternatives. HumanEval nevertheless remains a short-horizon generation benchmark: it does not require repository navigation, iterative tool use, environment repair, or sustained decision-making across a long trajectory [2].

SWE-bench moved the unit of evaluation from a function to a software repository. Its 2,294 tasks were derived from resolved GitHub issues and pull requests in 12 Python repositories. A system receives an issue description and a repository state, then generates a patch; the benchmark applies the patch and runs tests to determine whether the issue is resolved without breaking prior behavior [1]. This design made localization, editing, and test feedback part of the evaluated workflow. It also exposed a new dependency: a reported score describes a model-scaffold pair under a specific tool interface and budget, not a context-free model capability [1, 8, 11].

Other benchmarks expanded the task surface. GAIA introduced 466 questions requiring combinations of reasoning, web browsing, multimodal processing, file handling, and tool use; its original study reported 92% for human respondents and 15% for GPT-4 with plugins [3]. WebArena created self-hosted, functional web applications and tasks whose evaluators inspect URLs, page content, or backend state rather than merely judge a natural-language answer [4]. AgentBench evaluated agents across eight heterogeneous environments, including operating-system, database, knowledge-graph, card-game, and web tasks, in order to test generality across interaction regimes [5]. These benchmarks do not form a single ladder from easy to hard. Each samples a different capability distribution and uses a different environment and grader [3, 4, 5].

The next expansion addressed interaction reliability and computer use. Tau-bench places an agent between a language-model-simulated user, domain policies, and database-backed API tools. Its grader compares the final database state and required outputs with an annotated goal, and its pass^k metric asks whether all k independent trials succeed [6]. OSWorld supplies virtualized desktop environments, raw mouse and keyboard control, and task-specific execution-based evaluators. The original OSWorld benchmark contained 369 Ubuntu tasks spanning web and desktop applications, file operations, and multi-application workflows [7]. These designs test dimensions that static question answering cannot represent: state mutation, policy compliance, partial observability, and recovery from unexpected interface state [6, 7].

Benchmark construction also became an object of research. OpenAI's review of SWE-bench found underspecified issues and tests that could reject valid solutions; the resulting SWE-bench Verified subset contains 500 human-validated samples, after 68.3% of reviewed samples were filtered for underspecification, unfair tests, or other problems [9]. A separate SWE-bench+ study examined 251 SWE-Agent plus GPT-4 patches that passed the original tests and classified 32.67% as solution leakage and 12.75% as incorrect fixes that still passed weak tests [10]. The two studies identify opposite validity risks: a benchmark can underestimate capability by rejecting valid work, or overestimate capability by accepting invalid work or exposing solution details [9, 10].

The historical lesson is that an agent score is meaningful only with its evaluation contract. That contract includes the task set and version, model and scaffold, prompts and tools, environment image, allowed budget, sampling settings, grader, number of trials, and aggregation rule [1, 6, 11]. Omitting these details turns a reproducible measurement into an ambiguous headline. Public leaderboards remain valuable, but they answer bounded comparative questions; they do not by themselves establish reliability on a different organization's workflows [11, 12].

## Core Concepts

### The Evaluated System, Not Just the Model

An agent evaluation has at least five coupled components: the task, the agent system, the environment, the grader, and the run protocol. The agent system includes the model, system prompt, context-management policy, tool schemas, orchestration code, memory, and stopping logic. The environment includes software versions, credentials or fixtures, network state, and reset behavior. The run protocol specifies budgets, sampling parameters, retries, and what information the agent may observe. Anthropic's formulation that the harness and model are evaluated together follows directly from this coupling [11].

This system boundary prevents a common attribution error. If one model-scaffold pair outperforms another, the experiment demonstrates a difference between the pairs. It does not identify how much of the difference came from model weights, prompt design, tool affordances, search strategy, or budget. A model comparison requires holding the harness and protocol constant; a product comparison may instead compare complete systems because the integrated product is the object of interest. The question determines the appropriate boundary [8, 11].

### Capability, Regression, and Production Evaluations

A useful evaluation portfolio serves three different purposes. Capability evaluations test whether a system can perform a target class of work under controlled conditions. Regression evaluations detect whether a new model, prompt, tool, or harness change breaks behavior that previously worked. Production evaluation monitors deployed traffic for distribution shift, newly observed failures, latency, cost, and harm. Anthropic describes evaluations as one signal to combine with production monitoring, A/B tests, user research, and other evidence; OpenAI similarly recommends continuous evaluation and expansion of the dataset as new nondeterministic cases appear [11, 12].

The three purposes should not be collapsed into one score. A difficult public benchmark can discriminate among frontier systems but contain few examples of an organization's routine tasks. A regression suite should be stable enough to compare releases, while a capability suite may need regular refresh as systems improve. Production monitoring observes real traffic but usually lacks complete ground truth and may expose users to failures before those failures become test cases. The portfolio works as a loop: controlled evaluations gate changes, production evidence discovers new cases, and curated cases enter future regression runs [11, 12].

### Task Validity and Representative Sampling

Evaluation validity has several layers. Construct validity asks whether the task and grader measure the claimed capability. Content validity asks whether the dataset covers the important parts of that capability. Ecological validity asks whether the environment and task distribution resemble deployment. Grader validity asks whether a passing result is actually acceptable and a failing result actually unacceptable. The SWE-bench Verified and SWE-bench+ analyses show why both false negatives and false positives matter: ambiguous specifications can reject valid patches, while leaked solutions or weak tests can accept work that does not demonstrate the intended competence [9, 10].

A deployment evaluation should therefore begin with a task taxonomy rather than a convenient pile of examples. Relevant slices may include difficulty, tool family, number of steps, statefulness, ambiguity, policy sensitivity, data freshness, and consequence of failure. Sampling should represent common work and rare but high-cost cases. Aggregate success can hide a catastrophic slice: a system may perform well overall while failing nearly every task that requires authorization, numerical accuracy, or recovery after a tool error. Reporting per-slice results preserves this information [6, 7, 12].

### Outcome, State, and Trajectory Grading

Outcome grading asks whether the final objective was achieved. Exact match is appropriate when only one normalized answer is valid. Unit tests are appropriate when multiple implementations can satisfy a functional specification. State-based graders inspect a database, filesystem, application configuration, or browser backend after execution. WebArena, tau-bench, and OSWorld all use state inspection because an agent's final message can claim success without creating the required external effect [4, 6, 7].

Outcome grading is necessary but can be insufficient. A support agent could produce the desired database state while violating a policy or acting without user confirmation. Tau-bench explicitly notes that its rule-based reward may be necessary but not sufficient when unobserved policy violations occur [6]. A coding patch can pass incomplete tests while remaining incorrect outside the tested cases [10]. For consequential work, the grader should combine independent checks: final state, invariant preservation, policy compliance, and any required communication to the user.

Trajectory grading inspects how the result was produced. It can test tool selection, argument accuracy, authorization, handoffs, loops, unsafe intermediate actions, or whether the agent used prohibited information. OpenAI recommends trace grading when debugging questions such as whether the agent selected the right tool, handed off correctly, or violated an instruction or safety policy [12]. Trajectory criteria should be used selectively: requiring one canonical sequence can reject valid alternative strategies. Grade process when the process itself affects safety, cost, auditability, or learning value; otherwise prefer robust outcome and state checks [11, 12].

### Reliability Metrics: pass@k Is Not pass^k

A single run does not characterize a stochastic agent. Chen et al.'s pass@k measures the probability that at least one of k attempts succeeds; its unbiased estimator is `1 - C(n-c, k) / C(n, k)` for n sampled outputs with c successes [2]. It fits workflows where multiple independent candidates can be generated and an external selector can identify a correct one. The score must be reported with k, the number of generated samples, and the selection procedure, because allowing more attempts changes the operational system [2].

Tau-bench's pass^k measures a different property: the probability that all k trials for a task succeed. It decreases as k grows and exposes inconsistency that an average or best-of-k result can conceal [6]. In the original tau-bench experiments, the GPT-4o function-calling agent achieved pass^1 of about 61% in retail and 35% in airline, while retail pass^8 fell below 25% [6]. This is directly relevant to deployment: a workflow serving many users needs repeatable success, not merely one successful sample among retries.

Neither metric should be substituted for first-attempt success. pass@k answers whether retry plus selection can recover at least one success. pass^k answers whether repeated runs remain successful. pass@1 describes one-run task success. A complete report may include all three, along with confidence intervals, per-task trial counts, and the actual retry policy. Correlated failures, changing environments, and an imperfect selector can make production behavior worse than an idealized independent-trial calculation suggests [2, 6].

### Efficiency, Latency, and Failure Severity

Success without resource constraints can reward systems that search excessively. The evaluation contract should record tokens, model calls, wall-clock time, tool calls, retries, and monetary cost where available. Budgets should reflect the intended use: an overnight repository-maintenance agent and an interactive support agent have different latency constraints. Agentless is an instructive controlled alternative in software engineering because its fixed localization, repair, and validation pipeline achieved 96 correct fixes, or 32.00%, on SWE-bench Lite at a reported average cost of $0.70 per issue in the paper's setup [8]. The result shows that more autonomous steps are not automatically better; architecture, budget, and score must be considered together [8].

Failure severity also matters. A harmless refusal, an incorrect answer, an unauthorized state change, and silent data corruption should not receive the same operational treatment. Binary task success can remain the headline metric, but release decisions should separately track safety-critical violations and irreversible actions. This is an application of consequence-sensitive evaluation rather than a claim that every benchmark needs one universal weighted score [6, 11, 12].

### Contamination, Versioning, and Reproducibility

Public tasks can enter training corpora, issue discussions can reveal solutions, and benchmark infrastructure can change. The SWE-bench+ authors found solution details in some issue reports and emphasized the exposure risk for issues created before model training cutoffs [10]. Contamination cannot always be proven from dates alone, so it should be treated as a validity risk rather than inferred as certain memorization. Mitigations include private holdouts, post-cutoff tasks, canary data, versioned datasets, and evaluation on newly collected production cases [10, 12].

Reproducibility requires more than releasing prompts. A report should identify task version, environment image or dependency lock, model version, harness commit, tool permissions, seeds or sampling settings, budgets, grader code, and raw run artifacts. Environment failures should be separated from agent failures when possible, but exclusions and retries must be governed by a rule set before inspecting the result. Otherwise, selective reruns can bias the score. This evaluation manifest makes later comparisons interpretable even when hosted models or websites change [1, 4, 7].

### An Evaluation Is a Decision Instrument

The final design principle is to work backward from the decision. Model selection, release gating, debugging, safety assurance, and scientific comparison require different datasets and metrics. OpenAI's evaluation guidance starts with defining the objective and success criteria, then collecting data, choosing metrics, running comparisons, and evaluating continuously [12]. A benchmark that cannot change a decision is measurement without an operational purpose. A benchmark that changes a decision without valid tasks and graders is worse: it supplies false confidence.

## Evidence

### Case 1: SWE-bench Shows Both Understatement and Overstatement

The original SWE-bench study created repository-level tasks from GitHub issues and associated pull requests, then evaluated generated patches through project tests. The method improved ecological validity relative to function completion because systems had to work in real repositories and because functional tests admitted multiple patch texts [1]. It also made task specification and test quality part of the measuring instrument.

OpenAI audited this instrument by having human annotators assess whether problems were sufficiently specified and whether tests fairly accepted valid solutions. The review flagged 38.3% of samples for underspecified problem statements and 61.1% for tests that might unfairly reject valid solutions; 68.3% were filtered for these or other issues, leaving a 500-sample Verified subset [9]. Using the best tested open-source scaffold in that report, GPT-4o resolved 33.2% of Verified samples versus 16% on the original benchmark. The method and finding show that benchmark defects can make a capable system look worse, not only better [9].

Aleithan et al. tested the opposite failure direction. They manually compared successful SWE-Agent plus GPT-4 patches with issue reports, tests, and developer patches. Among 251 patches that passed all associated tests, they classified 32.67% as cases where solution details appeared in the issue or comments, 12.75% as incorrect fixes, 3.59% as changes to different files or functions, and 14.74% as incomplete fixes [10]. Their taxonomy is contestable in individual cases because a valid fix need not match the developer patch, but the study demonstrates the need to audit accepted outputs rather than equate test passage with complete correctness. Together, the two audits establish a bidirectional lesson: grader defects can create false failures or false successes [9, 10].

### Case 2: The Harness Changes What a Coding Score Means

SWE-bench evaluates an integrated system. The original task gives a repository and issue description, but each entrant decides how to localize code, present tools, allocate context, generate edits, and use test feedback [1]. Agentless tested whether a simpler, fixed pipeline could compete with autonomous tool-using agents. Its method decomposed work into hierarchical localization, candidate patch generation, reproduction-test generation, regression testing, and patch ranking without allowing a model to choose arbitrary next actions. It reported 96 correct fixes out of 300 SWE-bench Lite tasks, or 32.00%, with a reported average cost of $0.70 per issue in its experimental setup [8].

This result does not prove that fixed pipelines dominate agents generally. It shows that SWE-bench performance depends materially on how the model is embedded in a system and that autonomy is not itself the measured capability. The appropriate scientific object is therefore the model-harness pair, with ablations used when researchers want to attribute gains to a component [8, 11]. For buyers, the practical unit is the complete system they will deploy; for model researchers, a common harness is needed to isolate model differences.

### Case 3: Benchmark Diversity Reveals Capability Boundaries

GAIA's method uses questions that combine reasoning, browsing, files, multimodal input, and tools, while retaining objective final answers. Its original comparison found 92% human performance and 15% for GPT-4 with plugins across the benchmark [3]. WebArena instead runs agents against self-hosted websites and grades task completion from URLs, page content, or backend state. The benchmark contains 812 tasks represented by 241 templates across five functional sites, making navigation and state change central rather than incidental [4]. AgentBench broadens the comparison across eight environments, testing whether performance transfers among qualitatively different action and observation spaces [5].

OSWorld pushes this method to full desktop interaction. Its 369 Ubuntu tasks use real applications, configurable initial states, and 134 execution-based evaluation functions. In the original paper, human participants completed 72.36% of tasks while the best reported baseline achieved 12.24%; workflow tasks spanning applications were especially difficult [7]. These studies do not support one universal ranking because they use different task distributions and interfaces. They support a capability-map approach: repository editing, web navigation, general research, database interaction, and desktop control require distinct evidence [3, 4, 5, 7].

### Case 4: Average Success Conceals Inconsistency

Tau-bench directly measured repeated-trial reliability in simulated retail and airline support. Each task combined a hidden user goal, an LM-simulated user, domain policies, and API-backed database state. The evaluator compared final state and required outputs with an annotated target, and each task was rerun to estimate pass^1, pass@k, and pass^k [6]. In the original experiments, GPT-4o with function calling achieved about 61% pass^1 in retail and 35% in airline, but its retail pass^8 was below 25% [6].

The method matters as much as the numerical baseline. Repeated runs held the underlying task semantics constant while stochastic user and agent messages varied. The falling pass^k curve therefore measured fragility under conversational variation, not a switch to harder tasks [6]. For high-volume service, this is a more relevant warning than a best-of-many result: a system can have a respectable average and still fail to deliver consistent behavior across repeated instances of the same request.

### Case 5: Operational Guidance Converges on Layered Evaluation

Anthropic's engineering guidance reports that useful agent evaluation combines task suites with production monitoring, A/B tests, user research, and inspection of traces. It emphasizes that agents are difficult to evaluate because they act over many turns, modify state, and adapt to intermediate results [11]. OpenAI's guidance recommends defining an objective, collecting representative data, combining quantitative metrics with human judgment, and evaluating continuously. For agent workflows, it identifies tool selection, tool-argument precision, handoff accuracy, instruction following, and functional correctness as separate evaluation targets [12].

These are practitioner sources rather than neutral comparative experiments, so their evidence is strongest about the methods their organizations use and recommend. Their convergence with the benchmark studies is nevertheless informative: neither treats a public leaderboard score as sufficient for release. Both advocate layered evidence, repeatable datasets, trace inspection during debugging, and expansion of evaluation sets from observed failures [11, 12].

## Implications

### For Agent Engineers

Begin with a written evaluation objective tied to a decision. If the decision is model selection, run candidate models through the same harness, tools, prompts, environment, and budget. If the decision is product selection, compare the complete systems that would actually be deployed. If the decision is whether to release a change, use a stable regression suite and predeclared thresholds. This distinction prevents a product comparison from being presented as a model comparison and prevents a public capability score from being used as a release gate for unrelated tasks [11, 12].

Build the dataset from the deployment's task taxonomy. Include ordinary workflows, boundary cases, known incidents, ambiguous requests that should trigger clarification, tool failures that require recovery, and high-consequence actions that require authorization. Keep a protected holdout for final comparisons and a visible development set for iteration. Record provenance and collection dates so contamination risk can be assessed. When production reveals a new failure class, add a sanitized representative case to the regression suite rather than only patching the individual prompt [10, 12].

Use the cheapest valid grader for each criterion, not the cheapest grader overall. Deterministic checks are appropriate for schemas, calculations, tests, and external state. Human or model-based judgment may be needed for communication quality or open-ended synthesis, but such graders should be calibrated against expert labels and checked for consistency. Consequential actions should be read back from the target system: a success message is not evidence that the database, file, or account reached the intended state. WebArena, tau-bench, and OSWorld demonstrate practical forms of state-based verification [4, 6, 7].

Run multiple trials when nondeterminism is material. Report pass@1 or pass^1 for one-attempt success, pass@k only when the product genuinely supports retry and selection, and pass^k when consistency across repeated instances matters. Preserve task-level results and confidence intervals rather than only an aggregate. A change that improves mean success while increasing policy violations or catastrophic failures should not pass a release gate merely because one number increased [2, 6].

Instrument traces before failures become mysterious. Store prompts, tool calls, arguments, observations, state changes, latency, token usage, termination reason, grader outputs, and environment errors. Trace grading can then localize whether a failure came from task interpretation, tool selection, argument extraction, recovery, handoff, or stopping behavior [12]. This complements outcome grading; it should not force a single canonical trajectory when multiple safe strategies can succeed.

### For Benchmark Authors and Researchers

Publish the evaluation contract with the score. At minimum, identify the dataset version, task exclusions, environment image, model version, scaffold commit, prompts, tools, permissions, sampling settings, trial count, token or action budget, grader code, retry rules, and aggregation method. Release raw per-task results and enough artifacts to distinguish environment failures from agent failures. Without this information, later researchers cannot determine whether a score change reflects capability, infrastructure, or protocol [1, 4, 7, 11].

Audit both rejected and accepted outputs. Reviewing only failures detects false negatives but misses weak graders; reviewing only passes detects false positives but misses unfair tasks. SWE-bench Verified and SWE-bench+ illustrate why the audit must be bidirectional [9, 10]. Sample manual audits should be stratified by task slice and outcome, and disagreements should be documented. When a task or grader is corrected, version the benchmark instead of silently changing the historical measuring instrument.

Separate leaderboard incentives from scientific attribution. A leaderboard may legitimately rank complete systems, but it should label model-scaffold pairs and include cost and budget. Claims about a model require a common scaffold or controlled ablations. Claims about an architectural component require changing that component while holding the rest constant. Agentless demonstrates why this discipline matters: a strong score can arise from a constrained pipeline rather than increasing autonomous decision-making [8].

Refresh saturated or contaminated suites without discarding longitudinal value. Frozen versions support reproducibility, while fresh hidden sets preserve discrimination. Report performance on both when possible. New tasks should be designed from a capability taxonomy, not merely made longer or more obscure. Difficulty that comes from broken infrastructure, ambiguous instructions, or unfair tests is measurement error, not useful headroom [9, 10].

### For Product, Risk, and Governance Teams

Translate aggregate performance into expected operational exposure. The important questions are not only how often the system fails, but where, how severely, whether the failure is detectable, and whether it is reversible. Maintain separate gates for unauthorized actions, privacy or security violations, financial errors, silent corruption, and inability to escalate. Rare high-severity failures may dominate a release decision even when average task success is high. Tau-bench's policy-constrained tasks show why satisfying the user's requested outcome is not always sufficient [6].

Define authority boundaries in the evaluation environment. Test which actions require confirmation, which data may be accessed, what happens when a tool returns malformed output, and whether the agent stops safely when prerequisites are missing. Include adversarial and conflicting instructions where those conditions can occur in deployment. The grader should inspect both final state and prohibited intermediate actions when an unsafe step cannot be undone [11, 12].

Treat monitoring as part of the evaluation system. Distribution shifts, tool updates, changed websites, new user behavior, and model-provider revisions can invalidate a predeployment result. Use canary releases, rollback criteria, sampled human review, and alerts on failure slices, cost, latency, and policy violations. Feed verified incidents into the regression suite. This creates the continuous loop recommended by both Anthropic and OpenAI: evaluation gates deployment, production supplies new evidence, and the suite evolves [11, 12].

### A Practical Evaluation Sequence

A defensible sequence is: define the decision and unacceptable failures; specify the task taxonomy and sampling plan; freeze the model-harness-environment protocol; choose independent outcome, state, and process graders; pilot the tasks and manually audit both passes and failures; set thresholds before the final run; execute enough trials to measure variability; report aggregate, slice, reliability, cost, and safety results; then preserve artifacts and add verified production failures to future regressions [4, 6, 9, 10, 11, 12].

This sequence does not produce a universal agent score. It produces evidence fit for a stated decision. That is the central implication of the benchmark literature: measurement improves when the evaluator stops asking whether an agent is simply "good" and instead specifies which system, on which tasks, under which constraints, with which failure tolerance [1, 3, 6, 7, 11].

## Sources

1. Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O.,
   and Narasimhan, K. (2024). "SWE-bench: Can Language Models Resolve
   Real-World GitHub Issues?" ICLR 2024.
   https://arxiv.org/abs/2310.06770 [high]

2. Chen, M., Tworek, J., Jun, H., Yuan, Q., et al. (2021). "Evaluating
   Large Language Models Trained on Code." arXiv:2107.03374.
   https://arxiv.org/abs/2107.03374 [high]

3. Mialon, G., Fourrier, C., Wolf, T., LeCun, Y., and Scialom, T.
   (2024). "GAIA: A Benchmark for General AI Assistants." ICLR 2024.
   https://proceedings.iclr.cc/paper_files/paper/2024/hash/25ae35b5b1738d80f1f03a8713e405ec-Abstract-Conference.html [high]

4. Zhou, S., Xu, F. F., Zhu, H., Zhou, X., et al. (2024). "WebArena: A
   Realistic Web Environment for Building Autonomous Agents." ICLR 2024.
   https://arxiv.org/abs/2307.13854 [high]

5. Liu, X., Yu, H., Zhang, H., Xu, Y., et al. (2024). "AgentBench:
   Evaluating LLMs as Agents." ICLR 2024.
   https://arxiv.org/abs/2308.03688 [high]

6. Yao, S., Shinn, N., Razavi, P., and Narasimhan, K. (2024).
   "Tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World
   Domains." arXiv:2406.12045.
   https://arxiv.org/abs/2406.12045 [high]

7. Xie, T., Zhang, D., Chen, J., Li, X., et al. (2024). "OSWorld:
   Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer
   Environments." NeurIPS 2024 Datasets and Benchmarks Track.
   https://proceedings.neurips.cc/paper_files/paper/2024/hash/5d413e48f84dc61244b6be550f1cd8f5-Abstract.html [high]

8. Xia, C. S., Deng, Y., Dunn, S., and Zhang, L. (2024). "Agentless:
   Demystifying LLM-based Software Engineering Agents."
   https://arxiv.org/abs/2407.01489 [high]

9. OpenAI (2024). "Introducing SWE-bench Verified." Human annotation
   methods, filtering results, and baseline evaluation.
   https://openai.com/index/introducing-swe-bench-verified [high]

10. Aleithan, R., Xue, H., Mohajer, M. M., Nnorom, E., Uddin, G., and
    Wang, S. (2024). "SWE-Bench+: Enhanced Coding Benchmark for LLMs."
    arXiv:2410.06992.
    https://arxiv.org/abs/2410.06992 [high]

11. Anthropic (2026). "Demystifying Evals for AI Agents." Engineering
    guidance on agent evaluation structure, graders, and deployment use.
    https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents [high]

12. OpenAI. "Evaluation Best Practices" and "Evaluate Agent Workflows."
    Official guidance on evaluation design, continuous evaluation, and
    trace grading.
    https://developers.openai.com/api/docs/guides/evaluation-best-practices
    https://developers.openai.com/api/docs/guides/agent-evals [high]

## See Also

- `library/coding-agentic-ai/agent-skill-systems.md` -- how reusable
  instructions and tools create behaviors that evaluation must measure.
- `library/coding-agentic-ai/multi-agent-orchestration.md` -- how
  handoffs and decomposition add evaluation boundaries.
- `library/coding-agentic-ai/context-window-management.md` -- how
  context selection and compression affect agent reliability.
