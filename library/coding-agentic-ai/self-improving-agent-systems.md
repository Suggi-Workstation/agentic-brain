---
name: self-improving-agent-systems
id: 20260908T073357Z
tier: library-topic
domain: coding-agentic-ai
author: Librarian
tags: [self-improving-agents, execution-feedback, agent-evaluation, prompt-optimization, skill-synthesis, agent-memory]
links: [library/coding-agentic-ai/agent-evaluation-and-benchmarking.md, library/coding-agentic-ai/agent-observability-and-debugging.md, library/coding-agentic-ai/agent-memory-and-persistence.md, library/coding-agentic-ai/agent-skill-systems.md, library/coding-agentic-ai/prompt-engineering-for-agents.md]
---

# Self-Improving Agent Systems -- Execution Feedback Becomes Capability Only When It Is Measured, Validated, and Persisted

A self-improving agent system changes a durable part of its operating scaffold from execution evidence rather than merely producing a better answer in one retry. The operative loop is observe, evaluate, diagnose, propose, validate, and promote: a run produces a trace, an evaluator produces a bounded signal, and only a verified change to a prompt, memory, tool policy, skill, or control flow becomes available to future runs. This topic concerns scaffold-level improvement for agents, not training a foundation model from scratch; the distinction matters because a system can compound capability without changing model weights. [1][3][6]

## Background

Before language-model agents, continual improvement was usually framed as a model-training problem. A system collected labeled examples or reinforcement signals, updated parameters, and evaluated a new model version. That framing remains important, but it has high data, compute, and deployment costs. Huang et al. showed one parameter-updating route: a pre-trained model generated high-confidence rationale-augmented answers from unlabeled questions and was then fine-tuned on those self-generated outputs. Their EMNLP study reported gains on GSM8K, OpenBookQA, and ANLI-A3 without ground-truth labels for the generated answers. [7] This is self-improvement at the model layer: the durable target is the model's parameters.

Language agents introduced a second route: leave the underlying model fixed and change the surrounding scaffold. The scaffold includes the task instructions, examples, tools, memory, retrieval policy, execution loop, evaluator, and release rules. Reflexion made this distinction explicit. Rather than fine-tuning weights after a failed attempt, its agent turns task feedback into verbal reflection, stores that reflection in episodic memory, and conditions a later trial on it. [1] Self-Refine similarly uses one model to generate an output, critique it, and revise it iteratively, without supervised training, reinforcement learning, or an additional model. [2] These systems demonstrate that a language model can improve behavior at inference time, but a retry alone is not durable learning unless the resulting lesson is selected and stored for later use.

The distinction between local correction and persistent improvement is central. A local correction changes the next attempt within a task: a code agent reads a compiler error, revises the patch, and passes a test. A persistent improvement changes a reusable artifact: for example, a recurring compiler error is converted into a tool-selection rule, a validated coding skill, or a regression test. The first may solve the current task. The second may reduce the recurrence rate across a future task distribution. The second claim requires an evaluation that measures future behavior; it cannot be inferred from a single successful retry. This is the author's synthesis from the evaluation and trace-based engineering patterns described in the cited work. [1][2][9]

Voyager supplied an early system-level example of scaffold-level accumulation. In Minecraft, it paired an automatic curriculum with an executable skill library and an iterative prompting mechanism that incorporated environment feedback, execution errors, and self-verification. Its skills were stored as reusable code, allowing later tasks to retrieve and compose behavior learned earlier. [3] The demonstration is not direct evidence that the same architecture transfers unchanged to coding, research, or business workflows. It is evidence for a narrower proposition: when execution outputs are converted into retrievable, composable artifacts, an agent can retain useful behavior across tasks without parameter fine-tuning. [3]

Prompt optimization extended the idea from individual retries to systematic search over instructions. OPRO places previously generated solutions and their measured values in the optimizer prompt, then generates and evaluates new candidates for subsequent rounds. In the prompt-optimization experiments reported by Yang et al., the best instructions exceeded human-designed prompts on selected GSM8K and Big-Bench Hard tasks. [4] ProTeGi uses natural-language critiques as textual gradients, then uses beam search and bandit selection to turn those critiques into prompt edits. [5] DSPy treats language-model pipelines as declarative transformation graphs and supplies a programming model intended to optimize them rather than hand-maintain prompt strings. [6] These approaches share a structure: a candidate change is judged by an explicit objective instead of being accepted solely because it sounds persuasive.

The modern engineering problem is broader than prompt search. An agent run exposes possible changes at several layers: an instruction can be clarified, a memory item can be consolidated, a skill can be added or revised, a tool can be wrapped with validation, a retrieval query can be changed, or the orchestration can be redesigned. TextGrad formalizes the general direction by treating textual feedback as a signal that can optimize components in a compound AI computation graph. [9] Godel Agent explores a more expansive design in which an LLM can change its own logic and behavior from high-level objectives. [10] Such work expands the candidate-update space, but it also makes governance and attribution harder: a measured improvement may arise from an altered evaluator, a changed tool, a different prompt, or chance variation rather than the intended repair.

The engineering consequence is that self-improvement is not a property of reflection text, a memory store, or an optimization algorithm in isolation. It is a controlled feedback system. The system needs an observation record, a task-relevant measurement, a candidate-change mechanism, an isolation boundary, and a promotion criterion. Without those components, it can create the appearance of learning by accumulating untested advice, optimizing a narrow proxy, or carrying a plausible but incorrect reflection into future work. The author's synthesis is that the highest-risk failure is an unverified change becoming durable and degrading many later runs; the primary prevention is to make promotion conditional on independently measured improvement and reversibility. [1][4][5][9][10]

## Core Concepts

### 1. Define the Improvement Boundary Before Measuring It

A self-improving system must state what may change. There are at least two boundaries. The model boundary covers parameters, fine-tuning data, and reward-model updates. The scaffold boundary covers the operational system around a fixed model: prompts, memory, tools, skill files, retrieval, routing, evaluators, and stop conditions. Huang et al. operate across the model boundary by training on self-generated rationales. Reflexion, Self-Refine, Voyager, OPRO, ProTeGi, and DSPy primarily demonstrate methods at the inference or scaffold boundary. [1][2][3][4][5][6][7]

This distinction prevents a category error. A model that writes a useful critique has not necessarily learned a durable skill. Conversely, a system that changes a versioned skill specification after evaluation can improve future behavior even if its model weights are unchanged. The system designer should name the update target in each proposal: `prompt`, `retrieval-policy`, `memory-record`, `skill`, `tool-wrapper`, `planner`, `evaluator`, or `model`. The label makes later attribution possible. If a benchmark changes after a release, the team can ask which boundary moved rather than treating the system as an indivisible black box.

A narrow boundary is safer than a broad one. For example, a coding agent that repeatedly misuses one API might first propose a revised tool description and a test fixture. That is more reversible and easier to attribute than allowing it to rewrite all prompts, tool definitions, and evaluation criteria at once. This is an engineering recommendation derived from the controlled-search structures in OPRO, ProTeGi, and TextGrad, not a reported experimental result. [4][5][9]

### 2. The Feedback Signal Must Be Observable, Relevant, and Bounded

Execution feedback is any information produced during or after a run that can discriminate better from worse behavior. It can be an external test result, a compiler diagnostic, a task score, a verifier's pass/fail result, an environment state change, a human annotation, a cost measurement, or a structured critique. Reflexion accepts scalar or free-form feedback from external or internally simulated sources. [1] Voyager incorporates environment feedback, execution errors, and self-verification into program improvement. [3] Self-Refine uses a model-generated critique as the feedback channel. [2]

Not all feedback is equally trustworthy. A unit test can be precise about the behavior it covers while remaining silent about untested behavior. A language-model critique can identify a useful weakness while also inventing one. A customer preference signal may measure satisfaction but not safety or cost. Therefore, every feedback signal needs a declared scope: what it measures, what it does not measure, how it can be corrupted, and whether it can be used as a release gate. This is the author's synthesis from the methods' reliance on task-specific evaluators. [1][2][4][5][9]

A bounded feedback schema reduces ambiguity. A useful record contains at least: task identifier, initial state, action sequence or trace reference, observed outcome, evaluator version, score or verdict, failure category, and evidence link. A free-text reflection may be attached, but it should not replace the evidence record. This separation permits later review: the system can retain the critic's hypothesis while an operator verifies whether the cited failing test, tool error, or benchmark score actually supports it.

The correct optimization objective is multi-dimensional when the agent has competing requirements. A coding agent, for example, may need correctness, policy compliance, latency, token cost, and non-destructive behavior. Optimizing only completion rate can favor shortcuts that pass a narrow test suite. OPRO and ProTeGi demonstrate that explicit values or textual gradients can guide candidate search, but they do not eliminate the need to define an objective that represents the deployed task. [4][5] The author's assessment is that an improvement objective should include hard constraints for safety and correctness before soft objectives such as speed or stylistic preference.

### 3. Reflection Is Diagnosis, Not Evidence

Reflection converts a result into a hypothesis about why it occurred and what should change. In Reflexion, the agent turns task feedback into verbal reflections stored in an episodic buffer for later trials. [1] In Self-Refine, feedback and refinement form an iterative loop inside a single model. [2] These patterns are useful because natural language can express a failure mechanism that a scalar score cannot: for example, that an agent selected an obsolete tool because it confused read and write permissions.

However, an articulate diagnosis can be wrong. A model may blame an instruction when the actual failure arose from stale retrieval, a broken tool, a missing dependency, or an invalid evaluator. The reflection therefore has the status of a candidate explanation, not a verified causal claim. A reliable system retains the link between the reflection and the underlying trace, test output, or evaluator evidence. It asks: what was observed; what mechanism is proposed; what smallest change follows; and what future test would falsify that proposal? This is an engineering interpretation of the distinction between feedback incorporation and measured optimization in Reflexion, ProTeGi, and TextGrad. [1][5][9]

The smallest useful reflection is actionable and scoped. "Be more careful" is not a candidate change because no evaluator can distinguish whether it was applied. "When a database schema inspection reports a nullable field, run the migration validation before generating a write query" is testable: the behavior can be placed in a targeted evaluation, the instruction can be versioned, and the run trace can show whether the step occurred. The lesson is not that every reflection should become a permanent instruction. It is that only specific, testable reflections are eligible for promotion.

### 4. Persistence Creates Compounding but Also Carries Error Forward

A system becomes persistent when it records an accepted change in a form that later runs can retrieve or execute. The storage form should match the update target. A trace or episodic memory preserves what happened. A semantic memory record preserves a verified fact. A procedural artifact, such as a skill, prompt module, executable program, or tool wrapper, preserves how the system should act. Voyager's ever-growing code skill library is a procedural store: a newly developed capability can be retrieved and reused in a later task. [3] Generative Agents similarly stores natural-language experiences, synthesizes higher-level reflections over time, and retrieves them dynamically for planning. [8]

Persistence is not automatically beneficial. A lesson from one failure can overfit a narrow environment; a prompt edit that wins on a small sample can harm a broader distribution; a skill can become obsolete when a tool changes. The system needs a retention policy that distinguishes raw trace evidence from candidate lessons and accepted procedures. A practical three-state lifecycle is `candidate`, `validated`, and `retired`. Candidate artifacts can inform human or automated review but cannot alter high-stakes behavior. Validated artifacts can be retrieved under their declared scope. Retired artifacts remain auditable but are excluded from ordinary retrieval. This lifecycle is the author's synthesis, supported conceptually by the reusable-skill and reflective-memory mechanisms in Voyager and Generative Agents. [3][8]

A durable lesson also needs provenance. Its record should identify the source tasks, evaluator result, author or generator, version, applicability conditions, and expiration or review rule. Provenance makes the improvement reversible: if a later regression arises, the system can identify and disable the specific promoted artifact rather than guessing among years of accumulated instructions. The requirement follows from the engineering need to attribute changes; it is an author's recommendation rather than a finding reported by one source. [4][5][6][9]

### 5. Candidate Generation Must Be Separated From Candidate Selection

The generative mechanism proposes alternatives; the selection mechanism decides whether any alternative is better. OPRO exemplifies this separation: a language model generates new solutions from prior solutions and their values, then the solutions are evaluated and added to the optimization context for a later step. [4] ProTeGi similarly generates prompt edits from textual gradients but uses beam search and bandit selection to guide the search. [5] TextGrad generalizes the generator side by propagating textual feedback to components in a computation graph. [9]

The separation matters because language models are good at producing plausible variants but plausibility is not a performance metric. A proposed new skill might be concise, confident, and stylistically consistent while decreasing task accuracy. A system should preserve an unchanged control candidate, run candidate and control under the same evaluator version, and accept the new artifact only when the result meets a predeclared threshold. When task execution is stochastic, acceptance should be based on repeated trials or a held-out set rather than a single favorable output. This is a methodological recommendation derived from the explicit evaluation loops in OPRO and ProTeGi. [4][5]

Candidate generation should also be constrained by change budget. One proposal should address one diagnosed failure class where feasible. Bundling a prompt rewrite, a new tool, a memory migration, and an evaluator edit can make a score change impossible to attribute. The exception is a coupled interface repair where the components cannot be evaluated separately; then the proposal should declare the coupling and use an integration test. This is an author's engineering synthesis, not an empirical claim. [6][9][10]

### 6. Evaluation Is the Learning Gate, Not a Reporting Afterthought

An improvement system needs a task distribution that represents the behavior it intends to improve. The evaluation has two roles. First, it diagnoses a failure by making it observable. Second, it gates promotion by comparing the candidate against the prior state. Self-Refine reports improvement across seven evaluated tasks, while Reflexion reports benchmark gains across sequential decision making, coding, and language reasoning. [1][2] Those results are evidence that their specific methods can help under their evaluated conditions; they do not establish that any reflection loop improves every production workflow.

A useful evaluation suite has at least three partitions. The regression partition contains previously observed failures and prevents recurrence. The representative partition samples routine work so that a repair does not degrade ordinary performance. The adversarial or boundary partition tests known unsafe, expensive, or ambiguous conditions. The author recommends holding the evaluator and task set fixed during a candidate comparison. Changing the prompt and the scoring rubric together can make a worse behavior appear better by moving the goalposts.

Improvement should be measured as a vector, not a single number, when the system has hard constraints. A proposed tool policy might raise task completion while increasing invalid writes; it should be rejected if the invalid-write constraint is breached. A prompt might lower latency by eliminating verification; it should be rejected if correctness declines below the agreed floor. This recommendation follows from the fact that the cited optimization systems require an objective function; it adds the engineering requirement that objectives include constraints relevant to deployment. [4][5][9]

### 7. Promotion, Rollback, and Isolation Convert Search Into Safe Operations

Promotion makes a validated candidate available to future production runs. It must be a distinct action from candidate creation. The minimum promotion record includes the prior artifact version, the candidate version, the evaluation evidence, the expected benefit, the known scope, an owner, and a rollback path. The single worst outcome is propagation: an agent promotes an unverified or mis-scored update and causes a systematic failure across many future runs. Isolation prevents this by evaluating in a sandbox or shadow path before release, and rollback limits the blast radius if the comparison was misleading.

The Godel Agent work illustrates why this control layer becomes more important as the update target broadens. It presents a framework in which an LLM can dynamically modify its own logic and behavior, and reports gains on its studied reasoning and agent tasks. [10] The work demonstrates a possibility, not a universal operational safety case. If an agent is permitted to change its own evaluator, access policy, or tool implementation, then the system must separately protect those governing components. Otherwise, the agent can improve its reported score by weakening the measurement rather than improving the task behavior. The warning is an author's inference from the asymmetry between a mutable system and its measurement boundary. [4][5][9][10]

A practical release sequence is: generate candidate; run static checks; run targeted regression tests; run representative evaluations against an unchanged control; inspect constraint metrics; approve or reject; deploy with version tagging; monitor post-deployment outcomes; and automatically or manually roll back when the declared guardrail fails. The sequence is a proposed engineering pattern that combines the evaluate-and-select structure in prompt optimization with the reusable-artifact pattern in lifelong agents. [3][4][5][6]

### 8. Exploration Needs an Explicit Budget and Stop Rule

Improvement loops consume model calls, tool calls, time, and potentially external side effects. Self-Refine gains quality by iterating feedback and refinement, but each iteration adds inference cost. [2] OPRO evaluates multiple candidate solutions, and ProTeGi uses beam search and bandit selection to guide search efficiency. [4][5] An operational system must set maximum iterations, candidate count, spend, latency, and permitted side effects before it starts optimization.

A stop rule avoids turning the search loop into an uncontrolled retry loop. Common stop conditions are: a candidate satisfies the predefined acceptance threshold; no candidate improves the control after a fixed budget; the evaluator reports an unsafe state; the trace indicates repeated equivalent actions; or a human-review boundary is reached. The stop rule should be encoded outside the component being optimized where possible. This is an author's recommendation grounded in the evaluation-driven search structure of the cited systems. [4][5][9]

The result is a precise definition: a self-improving agent system is not a system that always modifies itself. It is a system that turns eligible execution evidence into narrowly scoped candidates, accepts only measured improvements under stable criteria, and retains the resulting artifact with provenance, review, and rollback. That definition places self-improvement within ordinary engineering control rather than treating it as autonomous mutation.

## Evidence

### Reflexion: Verbal Feedback Stored for Later Trials

Shinn et al. evaluated Reflexion as a language-agent framework that avoids parameter updates. Their method lets an agent receive feedback, produce a verbal reflection, retain the reflection in an episodic buffer, and use the stored text on a subsequent attempt. The paper tested the approach across sequential decision making, coding, and language reasoning. In its reported HumanEval experiment, Reflexion reached 91 percent pass@1, compared with the cited 80 percent previous GPT-4 result. [1] The method supports a specific design claim: feedback can be converted into a persistent textual state that changes later agent decisions without fine-tuning.

The study does not prove that every stored reflection is accurate, transferable, or beneficial over a long production history. Its ablations examine feedback signal types, incorporation methods, and agent types, which is useful evidence that the implementation choices affect outcomes. [1] For system design, the proper inference is conditional: use reflection as a candidate diagnostic mechanism, then validate its downstream effect in the target environment. A separate release gate remains necessary because the research benchmark and the production task distribution may differ.

### Self-Refine: Single-Model Generate, Critique, and Revise

Madaan et al. evaluated Self-Refine using one LLM in the roles of initial generator, feedback provider, and refiner. The method iterates output, feedback, and revision without additional supervised data, model training, reinforcement learning, or a second model. Across seven tasks, the authors reported roughly 20 percent absolute average improvement in human preferences and automatic task metrics compared with conventional one-step generation using the same models. [2]

The evidence establishes that self-feedback can be useful at test time, including for strong base models. It also exposes a limitation relevant to durable agents: the paper's loop improves the current answer; it does not by itself specify a policy for promoting its feedback into future prompts, skills, or tool policies. An engineering system should therefore treat Self-Refine as an in-run quality-control pattern. To make it a self-improvement system in the durable sense defined here, it must add candidate storage, an evaluator that spans more than the current output, and a promotion rule. This distinction is the author's synthesis from the study design. [2]

### Voyager: Curriculum, Skill Library, and Execution Feedback

Wang et al. evaluated Voyager, an LLM-powered embodied lifelong-learning agent in Minecraft. Its architecture combined an automatic exploration curriculum, an ever-growing library of executable skills, and iterative prompting based on environment feedback, execution errors, and self-verification. [3] The paper reports that, relative to its stated prior baselines, Voyager obtained 3.3 times more unique items, traveled 2.3 times farther, and unlocked selected technology-tree milestones up to 15.3 times faster. It also reports that learned skills could be used in a new Minecraft world for novel tasks. [3]

This is direct evidence for the importance of the storage layer. The feedback loop did not merely rewrite the next action; it produced code artifacts that could be retrieved, interpreted, and composed later. The transfer setting is especially relevant because it tests whether a stored capability has value beyond the immediate trajectory that created it. The study's environment is a game, so it does not directly validate a coding-agent deployment. The transferable design principle is narrower: persistent, executable skills should have a retrieval rule and a new-task evaluation rather than being assumed to generalize. [3]

### OPRO: Measured Search Over Prompt Candidates

Yang et al. introduced OPRO as an optimization process in which an LLM receives previously generated solutions and their values, generates new candidates, and adds evaluated candidates back to the optimization prompt. [4] The reported studies included linear regression, traveling-salesperson problems, and prompt optimization. On selected prompt-optimization evaluations, the authors reported that optimized prompts outperformed human-designed prompts by up to 8 percent on GSM8K and up to 50 percent on Big-Bench Hard tasks. [4]

The useful evidence is methodological as much as numerical. OPRO separates candidate generation from candidate valuation and preserves prior scores in the search context. That supports a general operational rule: a self-improvement system should not promote a proposed prompt simply because an LLM generated a persuasive explanation. It should use a held evaluator to assign a value, compare the candidate with a control, and retain the result as evidence. The exact reported improvements are task-specific and should not be projected to unrelated workflows. [4]

### ProTeGi and TextGrad: Feedback as a Search Direction

Pryzant et al. introduced ProTeGi, which produces natural-language critiques of a prompt, treats them as textual gradients, and converts them into prompt edits using beam search and bandit selection. The paper reports improvements of up to 31 percent over initial prompt performance in its benchmark settings. [5] The mechanism supplies a concrete answer to a common agent-engineering question: how can a free-text failure explanation lead to a structured candidate search rather than an unbounded rewrite? The answer is to constrain the candidate set and score alternatives against a specified objective.

TextGrad extends the feedback concept to compound AI systems. Yuksekgonul et al. describe a framework that uses LLM-generated textual feedback to optimize components in computation graphs, with examples involving code and other variables. [9] The paper is evidence that natural-language feedback can be organized as an optimization interface across multiple components. It does not remove the attribution problem: when several components change together, a metric change may not identify which edit caused it. The recommended operational response is component-level evaluation where possible and explicit declaration of coupled changes where not. This latter recommendation is an author's engineering inference. [5][9]

### DSPy: Declarative Pipelines Rather Than Hand-Maintained Prompt Strings

Khattab et al. presented DSPy as a programming model that abstracts language-model pipelines as text-transformation graphs, motivated by the fragility of hard-coded prompt templates discovered by trial and error. [6] Its relevance to self-improving agents is architectural: optimization needs an addressable representation of what can change. A prompt embedded as an undocumented string inside control code is difficult to compare, version, test, or roll back. A declared pipeline with named modules and evaluators makes those operations more feasible.

The evidence here supports a design constraint rather than a universal performance estimate. Durable improvement requires the update target to be explicit. If the target cannot be named, versioned, and evaluated independently, then an apparent improvement will be difficult to reproduce or undo. This is an author's synthesis extending the declarative-pipeline rationale in DSPy to agent release operations. [6]

### Self-Generated Training Data and Recursive Logic Modification

Huang et al. reported a model-level improvement method using high-confidence, rationale-augmented answers generated from unlabeled questions. Their EMNLP results improved a 540B-parameter model from 74.4 to 82.1 percent on GSM8K, from 90.0 to 94.4 percent on OpenBookQA, and from 63.4 to 67.9 percent on ANLI-A3. [7] This study provides a contrast case: self-improvement can cross the model boundary, but then the proposed update is more expensive and less easily reversible than a versioned prompt or skill. The evidence supports evaluating model updates separately from scaffold updates rather than using one undifferentiated concept of learning.

Yin et al. reported Godel Agent, a self-referential framework that lets an LLM dynamically modify its logic and behavior under high-level objectives. The paper states that its experiments on mathematical reasoning and complex agent tasks showed continuing improvements over manually crafted agents on its evaluated dimensions. [10] This is evidence that a broad self-modification search space is technically investigable. It is not evidence that unrestricted self-modification is ready for every operational environment. The more mutable the system becomes, the more important it is to protect the evaluator, permission boundary, and release mechanism from the optimized component. That is the author's risk-control interpretation. [10]

### Generative Agents: Reflection as a Memory-Planning Architecture

Park et al. presented Generative Agents as an architecture that stores a complete natural-language record of experiences, synthesizes higher-level reflections over time, and retrieves relevant memories for planning. [8] Although the paper studies simulated human behavior rather than task-optimization agents, it provides evidence for the separation of episodic record, consolidated reflection, and retrieval. That separation is useful because it avoids treating all past text as equally authoritative. Raw events retain provenance; higher-level reflections are derived artifacts; and the planning loop retrieves only a subset.

The authors' architecture does not itself supply a production release protocol for changing skills or tool policies. It does support the memory design pattern used here: preserve raw execution evidence, derive a candidate lesson, and retrieve the accepted lesson under conditions that can be inspected later. The extension from simulation to production control is the author's synthesis and requires an independent evaluation gate. [8]

Taken together, these studies support four bounded conclusions. First, feedback can improve immediate behavior without weight updates. [1][2] Second, feedback can be transformed into reusable skills or persistent memory. [3][8] Third, language models can generate candidate edits while explicit values, search methods, and evaluators choose among them. [4][5][9] Fourth, broad self-modification and model-level learning are possible research directions but increase the need for isolated evaluation and rollback. [7][10] None of the studies establishes that self-improvement is monotonic, universal, or safe without a target-specific control system.

## Implications

### Build the Feedback Loop as a Versioned Product Surface

For agent builders, the practical unit of improvement should be a versioned change proposal, not an unstructured note saying that the agent learned something. Each proposal should identify: the observed failure, the trace or test evidence, the proposed update target, the expected behavior change, the evaluator, the result against a control, the permitted scope, and the rollback procedure. The proposal can originate from a model reflection, a human review, or a script; the acceptance standard should be the same. This recommendation follows from the feedback-storage and evaluation structures in Reflexion, Voyager, OPRO, and ProTeGi. [1][3][4][5]

A minimal implementation can start with ordinary software artifacts. Store traces or failure records separately from procedural instructions. Store candidate prompt or skill edits in reviewable files. Run a fixed regression suite before promotion. Attach evaluator scores and version identifiers to the commit or release record. This does not require a new foundation model or a fully autonomous optimizer. The author's assessment is that a small, auditable loop is preferable to a broad system that can write everywhere but cannot demonstrate which change improved which behavior.

### Treat Memory as a Promotion Layer, Not an Automatic Truth Store

For memory-system designers, the key question is not only what to remember, but what authority the remembered artifact has. Raw execution traces are evidence with context. Reflections are hypotheses. Validated skills and policies are procedures. Mixing all three in one retrieval channel risks injecting a failed experiment as a standing instruction. Generative Agents and Voyager support the value of retaining and retrieving accumulated information; neither result implies that every accumulated artifact deserves identical authority. [3][8]

A practical policy is to use different stores or metadata tiers. `Episodic` records preserve task-specific events and logs. `Candidate` records hold proposed diagnoses and changes. `Validated procedural` records hold reusable instructions or executable skills that have passed the declared gate. Retrieval should prefer validated procedures for action, while reviews may inspect candidates and episodes for diagnosis. This is an author's system-design proposal, grounded in the distinction between reflection, storage, and reusable skills in the cited architectures. [1][3][8]

### Use Evaluations to Prevent Proxy Optimization

For evaluation teams, self-improvement raises the risk that the agent learns the test rather than the task. OPRO, ProTeGi, and TextGrad depend on objectives or evaluators to guide search. [4][5][9] A narrow evaluator can reward a superficially effective candidate even when it creates an unmeasured failure. A code agent can increase a unit-test score by avoiding a required edge case; a research agent can increase citation count by selecting irrelevant sources; an operations agent can lower latency by skipping a verification step.

The mitigation is to define a scorecard before candidate generation. The scorecard should include the desired outcome, hard failure constraints, and costs. It should use held-out cases, repeat trials when behavior is stochastic, and preserve a no-change control. The evaluator itself should be versioned and protected from the component it judges. If a candidate changes an evaluator, it should be assessed through a higher-level review rather than evaluated by the modified evaluator alone. This is an author's control principle inferred from the optimization structure and broad-modification risks in the cited work. [4][5][9][10]

### Separate In-Run Repair From Cross-Run Learning

For operators, in-run correction and cross-run learning should be monitored separately. An in-run loop such as Self-Refine may increase the quality of a single answer but also increase cost and latency. [2] A cross-run lesson may reduce future failures but can create drift if it is retained without revalidation. The system should therefore record at least two metric families: per-run repair metrics, such as retry count and final task outcome; and release metrics, such as regression pass rate, held-out performance, adoption rate of a new skill, rollback count, and post-release constraint violations.

This separation makes a useful diagnostic possible. If in-run repair improves while cross-run performance does not, then reflections may be too task-specific or are not being promoted effectively. If cross-run performance initially improves and then degrades, then retained artifacts may be stale, overfitted, or interacting poorly. Those diagnoses are hypotheses to test, not conclusions that can be drawn from a single score. The recommendation is an author's synthesis of the local feedback loops and persistent skill or memory mechanisms in the literature. [1][2][3][8]

### Limit Autonomy by Reversibility and Blast Radius

For safety and reliability engineers, permissions should scale with reversibility. An agent may safely draft a candidate instruction, label it as unvalidated, and submit it to an isolated evaluation. It should receive stricter controls before changing a shared skill catalog, a tool implementation, a permission policy, or a production evaluator. The logic is simple: the cost of a wrong candidate rises sharply when the change affects many future runs or changes the measurement system itself.

Godel Agent shows why this rule remains relevant. Its research design explores recursive modification of logic and behavior. [10] A production system does not have to replicate that breadth to benefit from improvement loops. It can gain most of the engineering value from narrow updates to prompts, retrieval filters, and procedural skills, while reserving tool, permission, and evaluator changes for controlled review. The author's assessment is that a less autonomous but well-measured loop is more valuable than an unrestricted loop whose gains cannot be trusted or reversed.

### Design Skill Synthesis as Release Engineering

For teams that want agents to synthesize skills from task traces, the output should be treated like a software release. A skill candidate needs a name, declared inputs and outputs, scope, prerequisites, known failure modes, test cases, and version history. Voyager provides evidence that an accumulating executable skill library can compound capabilities when skills are reusable and retrievable. [3] It does not establish that a skill generated from one trace is safe to publish globally. The release process must test whether the skill handles the failure class rather than merely reproducing the exact successful trace.

A useful test is a counterfactual: would the proposed skill have prevented the original failure while preserving correct behavior on neighboring tasks? If the answer is not demonstrated, retain the candidate as an observation rather than promoting it as a procedure. This converts skill synthesis from free-form memory accumulation into a falsifiable artifact pipeline. The approach is an author's engineering recommendation informed by the reusable-skill evidence and evaluation-driven prompt optimization methods. [3][4][5]

### Optimize for Knowledge Value, Not Just Immediate Scores

For product and research leaders, the highest-value improvements often generate reusable understanding about the system. A trace that exposes a tool contract ambiguity can support a better tool wrapper, a targeted regression, and a clearer skill instruction. A trace that exposes evaluator weakness can improve the measurement system. A trace that only yields a one-off wording fix may still be useful, but it compounds less broadly. This is an author's prioritization framework rather than an empirical ranking.

The framework suggests selecting improvements by three questions: Does the evidence identify a repeatable failure class? Is the proposed change narrow enough to attribute? Does the evaluation cover the future context where the artifact will be reused? OPRO, ProTeGi, and TextGrad demonstrate candidate search driven by evaluation signals; Voyager and Generative Agents demonstrate persistence and retrieval of accumulated artifacts. [3][4][5][8][9] Combining those functions yields a disciplined compounding loop.

### Report Negative Results and Retire Stale Lessons

A mature self-improvement system must retain negative results. A candidate that failed evaluation tells future operators that a particular diagnosis or edit did not work under known conditions. Removing that evidence can cause the same unproductive search to recur. At the same time, active procedures should be reviewed and retired when their prerequisites, tools, or task distribution change. Persistent storage without review becomes instruction debt.

The author's proposed policy is to preserve failed candidates with evidence and an explicit rejection reason, while excluding them from normal action retrieval. Active artifacts should carry a review date or trigger based on tool version changes, repeated regression failures, or observed scope violations. This keeps the improvement history auditable without making every historical reflection operational. The policy extends the lifecycle problem implied by persistent skills and memories; it is not a direct result reported in a single cited study. [3][8]

### A Practical Operating Pattern

A system can implement the topic's ideas with the following constrained pattern:

1. Record an execution trace and outcome for each eligible task.
2. Classify a verified failure or opportunity using evidence, not only a model's explanation.
3. Generate one or more narrowly scoped candidates for a declared target.
4. Run static checks and targeted regression tests in isolation.
5. Compare candidate and unchanged control on representative and boundary evaluations.
6. Reject candidates that violate a hard constraint, fail to improve by the declared threshold, or cannot be attributed.
7. Promote the accepted artifact with provenance, versioning, scope, and rollback.
8. Monitor post-promotion outcomes and retire or roll back on regression.

This is an author's engineering synthesis, not a claim that the exact sequence has been experimentally validated as a universal standard. Its components reflect the observed feedback loops, candidate searches, memory stores, and reusable skill libraries in the cited research. [1][2][3][4][5][8][9]

The central implication is therefore conservative. Self-improvement is valuable when it makes future behavior more reliable under evidence that survives review. It is not valuable merely because the system can generate self-criticism or rewrite itself. The durable asset is the tested feedback loop: observed execution, stable measurement, bounded candidate change, controlled promotion, and reversible persistence.

## Sources

1. Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K., and Yao, S. (2023). "Reflexion: Language Agents with Verbal Reinforcement Learning." NeurIPS 2023. Reports feedback-driven verbal reflection stored in episodic memory and evaluated across decision-making, coding, and reasoning tasks.
   https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html [high]

2. Madaan, A., Tandon, N., Gupta, P., et al. (2023). "Self-Refine: Iterative Refinement with Self-Feedback." NeurIPS 2023. Describes generate-feedback-refine loops using the same LLM without additional training or reinforcement learning.
   https://proceedings.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html [high]

3. Wang, G., Xie, Y., Jiang, Y., et al. (2023). "Voyager: An Open-Ended Embodied Agent with Large Language Models." Describes an automatic curriculum, executable skill library, and iterative prompting from environment feedback and self-verification.
   https://arxiv.org/abs/2305.16291 [high]

4. Yang, C., Wang, X., Lu, Y., et al. (2023). "Large Language Models as Optimizers." Introduces Optimization by PROmpting (OPRO), which uses evaluated candidate solutions to guide later generation.
   https://arxiv.org/abs/2309.03409 [high]

5. Pryzant, R., Iter, D., Li, J., Lee, Y. T., Zhu, C., and Zeng, M. (2023). "Automatic Prompt Optimization with Gradient Descent and Beam Search." Introduces ProTeGi and textual gradients for prompt editing.
   https://arxiv.org/abs/2305.03495 [high]

6. Khattab, O., Singhvi, A., et al. (2023). "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines." Presents a declarative programming model for language-model pipelines and optimization.
   https://arxiv.org/abs/2310.03714 [high]

7. Huang, J., Gu, S., Hou, L., et al. (2023). "Large Language Models Can Self-Improve." Proceedings of EMNLP 2023, pages 1051-1068. Studies self-generated rationale data for model fine-tuning from unlabeled questions.
   https://aclanthology.org/2023.emnlp-main.67/ [high]

8. Park, J. S., O'Brien, J. C., Cai, C. J., et al. (2023). "Generative Agents: Interactive Simulacra of Human Behavior." Describes experience records, reflection, retrieval, and planning in language-model agents.
   https://arxiv.org/abs/2304.03442 [high]

9. Yuksekgonul, M., Bianchi, F., Boen, J., et al. (2024). "TextGrad: Automatic Differentiation via Text." Describes textual feedback used to optimize components of compound AI systems.
   https://arxiv.org/abs/2406.07496 [high]

10. Yin, X., Wang, X., Pan, L., et al. (2025). "Godel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement." ACL 2025. Studies an LLM agent that dynamically modifies logic and behavior from high-level objectives.
    https://arxiv.org/abs/2410.04444 [high]

## See Also

- `library/coding-agentic-ai/agent-evaluation-and-benchmarking.md` -- evaluation is the release gate that distinguishes an improvement from an attractive but unmeasured change.
- `library/coding-agentic-ai/agent-observability-and-debugging.md` -- execution traces supply the evidence used to diagnose candidates and create regressions.
- `library/coding-agentic-ai/agent-memory-and-persistence.md` -- memory tiers and consolidation govern how validated lessons survive across agent sessions.
- `library/coding-agentic-ai/agent-skill-systems.md` -- skills are a practical storage form for reusable procedures produced by validated experience.
- `library/coding-agentic-ai/prompt-engineering-for-agents.md` -- prompt modules are a common but narrower target for evaluation-guided scaffold updates.
