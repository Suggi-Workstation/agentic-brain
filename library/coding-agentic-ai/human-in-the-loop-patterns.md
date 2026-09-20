---
name: human-in-the-loop-patterns
id: 20260920T133428Z
tier: library-topic
domain: coding-agentic-ai
author: Librarian
tags: [human-in-the-loop, agent-oversight, approval-gates, escalation, human-ai-interaction, agent-governance]
links: [library/coding-agentic-ai/anchor-coding-agentic-ai.md, library/coding-agentic-ai/agent-sandboxing-and-security.md, library/coding-agentic-ai/tool-use-and-function-calling.md, library/coding-agentic-ai/multi-agent-orchestration.md, library/coding-agentic-ai/agent-observability-and-debugging.md, library/coding-agentic-ai/agent-evaluation-and-benchmarking.md]
---

# Human Oversight Improves Agent Workflows Only When It Is Risk-Triggered, Informed, and Enforceable

Human-in-the-loop design is not the practice of asking a person to approve every agent action. It is a control architecture that assigns routine, reversible work to automation while routing consequential, ambiguous, or out-of-policy actions to a qualified human through enforceable gates, review checkpoints, and escalation paths. Effective oversight therefore depends on gate placement, decision quality, durable state, and measured outcomes; a human click without time, context, authority, or attention is not a reliable safeguard. [1][2][3][4][5]

## Background

Human oversight of automation predates language-model agents by decades. Bainbridge's 1983 analysis of industrial automation identified an enduring design problem: automating normal operation often leaves people responsible for rare abnormal conditions while giving them fewer opportunities to practice the skills needed to handle those conditions. The operator is asked to monitor a reliable process, detect an uncommon failure, reconstruct what happened, and intervene correctly under time pressure. Automation therefore changes human work rather than simply removing it, and can make the remaining work more cognitively demanding. [7]

Parasuraman, Sheridan, and Wickens later formalized automation as a design space rather than a binary choice. Their model separates four functions - information acquisition, information analysis, decision and action selection, and action implementation - and permits different automation levels for each function. The model's key implication for agent engineering is that an agent need not receive one global autonomy setting. It can gather information automatically, summarize alternatives, recommend a decision, and still require a person to authorize execution. Reliability, human performance, and the cost of a wrong action are explicit criteria for choosing the level of automation. [6]

Research on trust added a second correction to the simple claim that more human review is always safer. Lee and See define the design objective as appropriate reliance: people should use automation when it is capable in the current context and reject it when it is not. Excessive trust produces misuse; insufficient trust produces disuse. Trust depends on observed performance, process understanding, purpose, context, and interface presentation, so merely showing a warning or an explanation does not guarantee calibrated review. A reviewer may defer to a fluent but wrong recommendation, or reject a useful one because the system's limits and evidence are unclear. [8]

Automation-bias research demonstrates why nominal human control can fail. Lyell and Coiera's systematic review examined experimental evidence on automation bias and verification complexity. Ten of eleven multitask studies in the review reported automation bias, while evidence also appeared in single-task diagnostic settings. The review connects overreliance to attentional demands and to the difficulty of independently verifying automated advice. The practical lesson is not that humans should be removed, but that review must be designed as a real task with sufficient evidence, time, and cognitive support. [11]

Modern agentic systems intensify these older problems because they can select tools, chain actions, modify external state, and continue for many steps. OpenAI's agent-governance paper treats limited direct supervision as a defining property of agentic systems and proposes practices such as constrained action spaces, monitoring, attribution, and interruptibility. NIST's AI Risk Management Framework similarly treats AI as a sociotechnical system and calls for defined human-AI roles, monitoring, intervention, appeal, override, and the ability to disengage or deactivate systems that depart from intended use. These are organizational and technical responsibilities, not properties that can be supplied by a prompt alone. [3][5][14]

Current agent implementations translate those responsibilities into concrete runtime patterns. Anthropic recommends simple, composable workflows and notes that agents can pause for human feedback at checkpoints or when blocked. Its safety framework argues that the balance between autonomy and oversight varies by use case, gives read-only versus state-changing permissions as an example, and emphasizes that people should retain control before high-stakes decisions. Microsoft describes human-in-the-loop review as a deterministic governance backstop: escalation conditions should be enforced by the application or orchestrator rather than left entirely to probabilistic model judgment. LangChain implements the same separation through middleware that inspects proposed tool calls, interrupts execution according to policy, and resumes from persisted state after an approve, reject, edit, or response decision. [1][2][4][15]

The domain boundary is important. This topic concerns how to engineer and operate human oversight inside agent workflows: where gates sit, what triggers them, how a reviewer receives context, how execution pauses and resumes, and how outcomes are measured. It does not claim that oversight resolves general AI ethics, legal accountability, or model alignment. Those questions affect the policy supplied to the workflow, but the coding-agentic-ai problem is narrower: converting that policy into reliable control flow around tools, state, and side effects. [2][3][4][5]

## Core Concepts

### 1. Separate Proposal From Authorization

A model output is a proposal to act, not proof that the action is authorized. The reasoning layer may choose a tool and generate arguments, but a separate execution layer should validate the request, evaluate policy, obtain any required approval, and only then invoke the tool. This separation preserves a deterministic control point even when model behavior is probabilistic. Microsoft explicitly warns against letting the model decide whether review is required, because the same ambiguity or adversarial input that creates risk could also suppress escalation. LangChain's middleware expresses this pattern operationally by comparing each tool call with configured policy before execution. [4][15]

For example, a coding agent may propose `delete_branch(name)` after concluding that a branch is obsolete. The model can explain its reasoning, but application code should decide whether branch deletion belongs to an approval-required action class. The reviewer sees the repository, branch, protection status, recent commits, and recovery options; approval is bound to that specific call. A natural-language instruction such as "ask before dangerous actions" is weaker because both the meaning of dangerous and the decision to ask remain inside the model. [4][15]

### 2. Place Gates at Consequence Boundaries

A useful approval gate sits immediately before an action whose consequences justify delay and human attention. Candidate boundaries include irreversible changes, externally visible communication, financial transfer, security-sensitive permission changes, production deployment, disclosure of protected data, and decisions that materially affect a person. Read-only retrieval, local drafting, reversible branch edits, or deterministic tests usually need different controls, such as logging, sandboxing, or automated validation, rather than synchronous approval. This is the topic author's synthesis of the risk, reliability, and consequence criteria in the automation-level model and current agent safety guidance. [2][4][6]

Gate placement should be based on the action's semantics rather than on the number of agent steps. A workflow that asks for approval after every tool call creates repeated delay without distinguishing a file read from a production write. A workflow that asks once at the beginning for permission to "complete the task" may conceal later actions that were not foreseeable when consent was given. The stronger design groups low-risk steps inside a bounded operating envelope and requires fresh authorization when the proposed action crosses a declared boundary. [2][4][5]

### 3. Use More Than One Oversight Pattern

Human-in-the-loop is one member of a broader family. In a synchronous approval gate, execution pauses before a defined action and resumes only after approval. In a review checkpoint, the agent completes a reversible artifact - such as a draft, patch, plan, or analysis - and a person reviews it before publication or merge. In exception escalation, the agent hands off because required information is missing, policy is ambiguous, a tool failed, or an invariant was violated. In sampled audit, the workflow completes without blocking but a risk-weighted subset of outputs is reviewed later to estimate residual error and detect drift. These four patterns address different timing and throughput needs; treating them as interchangeable obscures their distinct control functions. This taxonomy is the author's synthesis of runtime approval, monitoring, audit, and override mechanisms described across the sources. [3][4][5][14][15]

A fifth mode, human-on-the-loop supervision, is appropriate when immediate blocking would destroy the workflow's utility but continuous telemetry and intervention remain possible. The agent proceeds inside a bounded envelope while operators monitor alerts, traces, budgets, and anomaly signals. Human-out-of-the-loop execution can be defensible for low-impact, well-tested, reversible operations with automated verification and rollback. These labels describe control modes, not moral rankings: the correct mode depends on consequence, detectability, time budget, reversibility, and evidence about performance. [5][6][14]

### 4. Define Escalation Triggers in Observable Terms

An escalation trigger should be testable by the orchestrator. Strong triggers include a requested tool or resource class, data sensitivity, monetary amount, permission scope, failed validation, repeated tool errors, missing required evidence, deviation from a plan, budget exhaustion, an out-of-distribution input indicator, or a policy rule. A model may additionally request help when uncertain, but model-reported confidence alone is not a complete safety boundary because language-model confidence can be uncalibrated and the model may not recognize its own failure. Deterministic triggers and model-initiated escalation are complementary. [4][5][15]

Trigger design benefits from separating hard and soft conditions. A hard trigger blocks execution until an authorized decision occurs: for example, any production database write or external payment. A soft trigger routes the case for review while permitting bounded progress: for example, the agent may continue gathering evidence but cannot publish. An advisory trigger records a warning for later audit. The author's synthesis is that this three-level structure prevents teams from forcing every anomaly into either full autonomy or a complete stop. [4][5][14]

### 5. Make the Review Packet Decision-Complete

A reviewer cannot exercise judgment if the interface exposes only an approve button and the agent's conclusion. A decision-complete packet should identify the task and requester, proposed action, exact target and arguments, evidence used, policy rule that caused escalation, known uncertainty, expected effect, alternatives considered, reversibility, and the result of automated checks. For code changes, this means a bounded diff and test results rather than a prose assurance. For a message, it means recipient, final content, attachments, and source context. For a payment, it means beneficiary, amount, account, source document, and duplicate checks. This is an engineering synthesis of the legibility, control, monitoring, and interface guidance in the sources. [2][3][4][5][9]

Amershi et al.'s 18 human-AI interaction guidelines support this design at the interface level. Their work synthesized more than 150 recommendations and validated the resulting guidelines through iterative evaluation. Relevant rules include making system capabilities clear, showing contextually relevant information, supporting efficient correction and dismissal, scoping behavior when in doubt, making consequences visible, remembering recent interactions, and allowing users to control what the system learns. A review surface is therefore part of the control system: poor information design can turn a valid gate into a blind approval ritual. [9]

### 6. Preserve State Across the Pause

An approval interrupt changes the workflow from a single execution into a durable process. The system must persist the task state, proposed action, policy decision, reviewer assignment, deadline, and resume token before waiting. On approval, it should resume from the captured state rather than regenerate the action from scratch; on rejection or edit, it should return structured feedback to the agent; on timeout, it should follow an explicit fail-closed, fail-open, or alternate-routing policy. LangChain's interrupt and checkpoint design illustrates this requirement: the pending action is persisted and the run resumes from the interruption after a human decision. [15]

Replay safety is essential. If an agent proposes a side-effecting call, pauses, and then the process retries after a network failure, the system must not execute the approved action twice. Stable action identifiers, idempotency keys, expiration times, and current-state revalidation address this risk. If the target changed while approval was pending, the prior approval may no longer apply. The author labels this as synthesis because the cited runtime documentation establishes pause-and-resume mechanics, while the exact transaction controls depend on the host application. [4][15]

### 7. Treat Approval as a Capability With Scope

Approval should bind a reviewer, action, target, arguments, task, and time. It should not silently expand the agent's standing permissions. A person approving one repository write has not approved all future writes, and a person approving a draft has not approved its publication. The execution layer should verify that the action presented to the reviewer is byte-for-byte or semantically equivalent to the action executed. If the agent edits material fields after approval, the gate should fire again. [3][4][5]

Reviewer authority also needs definition. A subject-matter expert may judge technical correctness but lack authority to release funds; a manager may authorize expenditure but lack the expertise to validate a security exception. Multi-stage approval is justified only where distinct decisions require distinct authority. Otherwise, added stages increase latency and diffuse responsibility. This is the author's synthesis from NIST's requirement to define human-AI roles and responsibilities and from the governance literature's insistence that accountability belongs to identifiable people and organizations. [5][13][14]

### 8. Engineer for Appropriate Reliance, Not Maximum Trust

The reviewer's task is not to trust the agent or distrust it. It is to distinguish when the recommendation is usable. Lee and See's framework makes context and observed performance central to appropriate reliance. Interfaces should therefore expose evidence about the current case and the system's relevant performance, not a generic confidence badge or persuasive explanation. A reviewer also needs feedback after the decision so that trust can be updated from outcomes rather than from style. [8]

Cognitive forcing functions can improve review quality by requiring independent thought before revealing or accepting the AI recommendation. Bucinca et al. tested three such interventions in an experiment with 199 participants and found that they significantly reduced overreliance compared with simple explainable-AI interfaces, although benefits varied with participants' need for cognition. A practical implementation might require the reviewer to record an initial judgment, identify the governing criterion, or answer one verification question before the approve control becomes available. The intervention should be reserved for decisions important enough to justify the added effort. [10]

### 9. Design for Rejection, Correction, and Handoff

A binary approve/reject interface is insufficient for many agent tasks. A reviewer may need to edit arguments, request more evidence, narrow scope, choose an alternative, or hand the case to another role. The workflow contract should represent these outcomes explicitly so the agent does not interpret a rejection as a generic failure and repeatedly propose the same action. LangChain's documented decision types - approve, reject, edit, and respond - provide one concrete implementation. [15]

Escalation must also terminate safely. A missing reviewer, expired request, conflicting decisions, or unresolvable ambiguity cannot leave the agent running indefinitely or silently convert the action to approved. The workflow should define ownership, service-level expectations, fallback reviewer, timeout behavior, cancellation, and the state reported to the requester. This is a synthesis from agent lifecycle, interruptibility, and role-definition guidance; no cited source establishes one universal timeout policy. [3][4][5][15]

### 10. Connect Oversight to Observability and Evaluation

Every gate should emit a structured event: trigger, proposed action, evidence packet, reviewer, decision, time to decision, edits, execution result, and later outcome where observable. These records support incident reconstruction and answer whether the gate changes behavior rather than merely whether it exists. NIST calls for monitoring, override, incident response, and documented human-AI responsibilities. Raji et al.'s internal-audit framework similarly treats accountability as an end-to-end organizational process supported by artifacts, risk assessment, testing, documentation, and independent review. [5][13][14]

Useful metrics include intervention rate, rejection rate, edit rate, decision latency, queue age, timeout rate, reviewer agreement, false-escalation rate, missed-escalation rate, post-approval incident rate, and performance with and without the gate on comparable cases. Approval count alone measures activity, not safety. A gate that is never rejected may be perfectly targeted, or it may be a rubber stamp; outcome and counterfactual evidence are needed to distinguish those cases. The metric set is the author's synthesis of the measurement, audit, and human-reliance literature. [5][8][11][13][14]

## Evidence

### Automation-Level Design: Parasuraman, Sheridan, and Wickens

Parasuraman, Sheridan, and Wickens developed their model by decomposing human-machine information processing into acquisition, analysis, decision selection, and action implementation, then describing a continuum of automation levels for each function. The paper's method is a conceptual framework supported by examples and prior human-factors evidence, not a controlled evaluation of LLM agents. Its finding is nevertheless directly applicable: automation choices change human activity and should be evaluated by human performance, system reliability, and the cost of decision or action consequences. This supports mixed-control agent workflows in which information work can be highly automated while consequential action remains human-authorized. [6]

The model also warns against assigning one autonomy level to an entire agent. A research agent may automatically search and summarize, offer several recommendations, require a person to select among them, and then automatically format the chosen output. A coding agent may implement inside a sandbox but require review before merge. These mappings are author applications of the four-function model, not experimental findings from the 2000 study. [6]

### The Irony of Rare Intervention: Bainbridge

Bainbridge's short paper analyzes industrial-process automation and the classic allocation in which automatic systems control routine conditions while operators retain responsibility for abnormalities. The paper argues that this allocation can leave people with boring monitoring work, limited practice, and a sudden need for high-level diagnosis when automation fails. Its evidence is analytical and grounded in process-control practice rather than a randomized experiment. [7]

For agent workflows, the bounded inference is that a reviewer who sees only rare, difficult exceptions needs better support than an occasional approve prompt. Training examples, visible system state, diagnostic evidence, simulations, and feedback on decisions help preserve the competence needed at escalation time. The paper does not prove that a particular agent review interface will work; it identifies the human-performance failure that the interface must address. [7]

### Trust Calibration: Lee and See

Lee and See reviewed research from human factors, psychology, sociology, and related fields to build a conceptual model of trust in automation. Their central finding is that trust influences reliance especially when systems are too complex for complete understanding, and that appropriate reliance depends on how trust corresponds to automation capability in context. Display characteristics, experience, purpose, process, and performance all influence that calibration. [8]

This evidence rejects two simplistic oversight goals: maximizing user trust and maximizing user skepticism. Either can reduce performance. An oversight system should instead help the reviewer identify the relevant evidence, understand known limits, observe outcomes, and update reliance over time. The implication for agent engineering is a calibrated review surface and outcome feedback, not a persuasive explanation designed to secure approval. [8]

### Automation Bias and Verification Complexity: Lyell and Coiera

Lyell and Coiera conducted a PRISMA-compliant systematic review using multiple bibliographic databases and dual-review screening. The review compared experimental tasks from human factors and health care, with particular attention to multitasking and the complexity of verifying automated advice. Ten of eleven multitask studies reported automation bias, while evidence also appeared in some single-task diagnostic studies. [11]

The review supports the claim that adding a person after the model does not automatically create independent verification. If checking requires reconstructing a long tool trajectory, reading a large diff, or reproducing an analysis under time pressure, the reviewer may use the recommendation as a heuristic. Agent systems should reduce verification cost by surfacing provenance, focused diffs, invariant checks, and the reason for escalation. This design implication is a synthesis from the review's findings, not a measured universal effect size for agent workflows. [11]

### Cognitive Forcing: Bucinca et al.

Bucinca et al. studied overreliance in AI-assisted decision making with 199 participants. The experiment compared three cognitive-forcing designs against two simple explainable-AI approaches and a no-AI baseline. The reported result was that cognitive forcing significantly reduced overreliance relative to the simple explanation approaches, while participants with higher need for cognition benefited more on average. [10]

The study provides direct evidence that interface sequence can affect oversight quality. Requiring a person to form an initial view or engage analytically before seeing the recommendation can reduce passive acceptance. It also establishes a limit: the intervention's benefit is not uniform across reviewers. Teams should evaluate review-interface changes with their actual operators and task distribution rather than assuming that a deliberation step always improves outcomes. [10]

### Human-Algorithm Decisions Can Remain Unreliable or Biased: Green and Chen

Green and Chen used controlled experiments to examine algorithm-assisted decisions in pretrial and lending contexts. Their work articulated accuracy, reliability, and fairness as principles for responsible algorithm-in-the-loop decision making, then tested how participants used risk assessments under different presentation conditions. The reported results showed that algorithmic advice often improved accuracy, but human decisions could remain unreliable and racially biased. [12]

The agent-engineering implication is limited but important: a human final decision does not transfer all system properties to the human side or erase interaction effects. Evaluation must cover the complete sociotechnical workflow, including how recommendations are framed, which information is visible, who reviews, and whether outcomes differ across relevant groups. The study is not an evaluation of tool-using coding agents, so it should not be used to estimate a numerical error reduction for agent approvals. [12]

### Interface Guidance: Amershi et al.

Amershi et al. collected more than 150 recommendations from academic and industry sources, consolidated them into 18 human-AI interaction guidelines, and refined the set through modified heuristic evaluation, a user study, and expert evaluation. The guidelines cover initial expectation setting, interaction timing and relevance, correction when the system is wrong, user control, feedback, and cautious adaptation over time. [9]

This work supplies design evidence for the review packet and correction path. A gate should make system capability and current context clear, show the consequence of the pending action, support dismissal or correction, and behave predictably after feedback. The authors also caution that general guidelines may require specialization in high-risk domains. Consequently, the guidelines are a starting checklist for agent oversight interfaces, not proof that an implementation is safe. [9]

### Governance and Runtime Practice: NIST, OpenAI, Anthropic, and Microsoft

NIST AI RMF 1.0 was produced through a consensus-driven process with public drafts, workshops, and comments. It organizes risk management into Govern, Map, Measure, and Manage functions and identifies human-AI roles, ongoing monitoring, intervention, override, incident response, and deactivation as parts of trustworthy operation. Its Generative AI Profile adds actions concerning human-AI configurations, documented overrides, real-time monitoring, feedback, and alerts for human intervention. These documents are normative risk-management guidance, not controlled evidence that any single gate improves performance. [5][14]

OpenAI's agent-governance paper proposes an initial set of practices for system developers, deployers, and users, including evaluating suitability, constraining action space, setting defaults, making behavior legible, monitoring, attributing actions, and maintaining interruptibility. Anthropic's engineering guidance recommends simple workflows, environmental feedback, meaningful human oversight, and checkpoints or blocker-driven feedback. Microsoft's security guidance makes an especially specific implementation claim: required review should be triggered and enforced deterministically by the application layer or orchestrator. Together, these independent primary sources converge on layered oversight outside the model, although their guidance is partly based on provider experience rather than comparative peer-reviewed trials. [1][2][3][4]

### Audit Evidence: Raji et al.

Raji et al. propose an end-to-end internal algorithmic-audit framework spanning development and pre-launch review. Their method draws lessons from audit practices in other industries and specifies organizational roles, documentation artifacts, risk assessment, testing, and review activities. The paper emphasizes that accountability belongs to organizations and people because algorithms are not moral or legal agents, and that audit procedures are embedded in sociotechnical contexts rather than being neutral checklists. [13]

For agent workflows, the evidence supports connecting runtime decisions to lifecycle governance. Approval logs should feed incident review, regression tests, policy revision, and release decisions. Runtime HITL cannot compensate for a system that was never scoped, tested, documented, or assigned an owner. Conversely, a pre-launch audit cannot replace runtime interruption when the agent encounters a consequential case that testing did not cover. This combination is the author's synthesis of the audit and runtime sources. [3][5][13][14]

## Implications

### For Agent Architects: Allocate Control by Function and Risk

Architects should design autonomy as a matrix rather than a switch. For each workflow step, identify whether the agent acquires information, analyzes it, selects an action, or implements that action; then assign the appropriate automation level. The same workflow may automate retrieval and analysis, use human selection for a consequential choice, and return to automation for a bounded implementation. Document the reliability assumptions, consequence of error, reversibility, detection mechanism, and maximum acceptable review latency for each step. [5][6]

The worst design is hidden authority: a tool appears to be a harmless helper but can indirectly cause an external side effect, or an agent can select a path that bypasses the approval node. Draw the execution graph from every model-call output to every side-effecting capability. Required gates must dominate the protected action in the control-flow graph, meaning every path to the action crosses the gate. This graph criterion is the author's synthesis of deterministic application-layer enforcement and tool-execution separation. [4][15]

Use automated controls before spending human attention. Schema validation, sandboxing, least privilege, test suites, policy checks, spending limits, destination allowlists, and invariant checks can reject many unsafe actions deterministically. Human judgment should handle cases where meaning, context, competing values, or exception authority matter. This allocation avoids using people as slow syntax validators while preserving their role where rules alone are insufficient. [2][4][5]

### For Reviewers and Operations Teams: Make Oversight a Staffed Function

A reviewer needs defined authority, expertise, workload, and service expectations. Assigning an approval queue to whoever happens to be available creates uncertain latency and inconsistent judgment. Operators should know which decisions they own, which evidence is required, when to ask another specialist, and how to cancel or contain the workflow. The organization should train reviewers on both common correct behavior and representative failures so that rare escalations are recognizable. Bainbridge's analysis makes clear why passive monitoring without practice is an unstable control strategy. [7][14]

Queue design affects safety. Track age, priority, consequence, and deadline; reserve interruptive channels for urgent high-impact cases; and batch lower-risk reviews where comparison improves consistency. If review demand exceeds capacity, do not hide the backlog by widening automatic approval. Reduce the action envelope, add deterministic controls, sample low-risk outputs, or increase qualified review capacity. This is an author's operational synthesis; the cited literature establishes the human-attention and verification problems, not one universal queueing policy. [7][10][11]

Give reviewers feedback. After an approved action executes, record whether automated checks passed, whether an incident occurred, and whether later reviewers agreed. Without outcome feedback, trust can drift according to interface fluency or isolated memorable events. Lee and See's model predicts that reliance depends on experience and context, while NIST requires ongoing measurement and monitoring. [5][8][14]

### For Security and Governance Teams: Keep Enforcement Outside the Model

Security policy should define action classes that always require review, classes that can execute inside a bounded sandbox, and classes that are prohibited. The orchestrator should enforce these classes before issuing credentials or invoking tools. A model may explain why it thinks an exception is warranted, but it should not be able to waive the gate, alter the policy, approve its own request, or choose the identity that reviews it. [3][4][5]

Approval records should be auditable without becoming secret dumps. Log the action identity, actor, policy version, reviewer, decision, relevant evidence references, timestamps, and execution result; redact credentials and minimize sensitive payloads. Link these records to incident response, post-deployment monitoring, internal audit, and policy revision. NIST and Raji et al. both place human oversight inside a broader governance process with assigned responsibility and lifecycle evidence. [5][13][14]

Interruptibility is a backstop, not a complete design. An operator must be able to stop a run, revoke credentials, freeze state, and prevent queued actions from executing after cancellation. But intervention may arrive too late for a fast or irreversible action. Preventive gating is therefore required where consequences exceed the time available for detection and response. This distinction follows from OpenAI's emphasis on interruptibility and the automation literature's attention to action consequence and time. [3][6]

### For Multi-Agent and Skill-System Designers: Put Gates at Authority Transfers

A subagent handoff can transfer information, capability, or both. The orchestrator should specify the delegated objective, tools, data scope, budget, and return contract, and should gate any transfer that expands authority. A reviewer agent is not equivalent to a human reviewer merely because it occupies a node named review; if policy requires human accountability, the human decision must be represented explicitly. Multi-agent patterns can improve specialization or independent checking, but they also add handoffs whose state and authority need observation. This is the author's synthesis across orchestration, audit, and deterministic-gate guidance. [1][4][13]

Skill systems should declare side effects and approval requirements in machine-readable metadata. A tool schema explains arguments; a policy profile should separately classify read/write behavior, external visibility, data sensitivity, reversibility, and required reviewer role. Dynamic tool discovery must not dynamically erase governance. If a new tool appears, the safe default is no side-effect authority until its policy is registered and tested. This is an author synthesis grounded in the separation of capability discovery from execution authorization. [4][15]

### For Evaluation Teams: Measure the Combined Human-Agent System

Evaluate at least four baselines: human alone, agent alone, human with agent, and the deployed gated workflow. Human-plus-agent performance cannot be inferred from the better of the first two because interaction creates automation bias, verification cost, and possible complementary strengths. Report both beneficial reliance - accepting correct help - and harmful reliance - accepting incorrect help - rather than reporting agreement with the model as if agreement were accuracy. [8][10][11][12]

Gate evaluation should use scenario suites that contain ordinary cases, boundary cases, adversarial inputs, ambiguous policies, and known failures. Measure whether the trigger fired, whether the packet contained sufficient evidence, whether the reviewer made the correct decision under a defined rubric, how long the decision took, whether execution matched approval, and whether the system recovered correctly from rejection, timeout, or state change. This evaluation design is the author's synthesis of human-AI interaction, risk management, and audit principles. [5][9][13][14]

Review quality and throughput must be measured together. A gate that catches errors but creates an unbounded queue may cause workarounds or make the product unusable; a fast gate that is always approved may add latency without reducing risk. Teams should set a risk-based latency budget, monitor decision distributions, and test whether automated checks can safely narrow the review population. No source supplies a universal threshold because consequence and workflow economics are context-specific. [6][7][11]

### For Product Leaders: Spend Human Attention Where It Changes Outcomes

The autonomy-latency trade-off should be explicit. Synchronous review buys a chance to prevent an action before it happens, but costs waiting time and reviewer interruption. Post-hoc audit preserves throughput but can only detect and repair harm after execution. Reversible staged release lies between them: the agent acts in a sandbox, draft, branch, or preview, then a person controls promotion to the higher-impact environment. Product design should choose among these patterns based on consequence, reversibility, detectability, and response time rather than on a generic preference for autonomy or control. [5][6][14]

As evidence improves, oversight may change, but gates should not be removed merely because users have become comfortable. Use observed error rates, missed escalations, audit findings, and the effectiveness of automated controls. Changes to autonomy are themselves governed releases: version the policy, test it on historical cases, monitor after deployment, and retain rollback. Amershi et al. recommend cautious updating, while NIST and Raji et al. place ongoing review and documented change inside the lifecycle. [5][9][13][14]

The final product principle is narrow: human attention is scarce, fallible, and valuable. Good HITL architecture does not maximize the amount of human involvement. It makes a qualified person's judgment decisive at the small set of boundaries where automated evidence and rules are not sufficient, and it supplies enough context, time, authority, and feedback for that judgment to be real. This conclusion is the author's synthesis of the cited human-factors, HCI, governance, and agent-engineering evidence. [1][4][6][7][8][10][11]

## Practical Framework

The following framework is the author's synthesis and should be validated against the target workflow rather than treated as an empirical standard. [3][5][6][9][13]

1. **Map effects.** Inventory every tool and path that can change external state, disclose data, spend resources, affect a person, or expand permissions.
2. **Classify consequence.** For each action, record severity, reversibility, detectability, time to harm, policy sensitivity, and required authority.
3. **Choose the control mode.** Use automated enforcement for clear rules; synchronous approval for consequential pre-execution decisions; review checkpoints for reversible artifacts; exception escalation for ambiguity or failure; sampled audit for residual low-risk monitoring.
4. **Encode triggers.** Put mandatory triggers in deterministic application or orchestrator logic. Permit model-initiated requests for help as an additional path, not as the sole gate.
5. **Build the packet.** Present exact action, target, arguments, evidence, trigger reason, automated checks, uncertainty, expected effect, and recovery path.
6. **Persist before waiting.** Save workflow state, action identity, policy version, reviewer assignment, and expiration before emitting an interrupt.
7. **Support real decisions.** Represent approve, reject, edit, request-evidence, reroute, and cancel outcomes explicitly.
8. **Bind and revalidate.** Bind approval to the reviewed action and recheck target state, policy, and expiration immediately before execution.
9. **Observe the result.** Record decision latency, edits, execution outcome, later incidents, and feedback without logging unnecessary secrets.
10. **Evaluate and revise.** Test historical and adversarial cases, compare human-agent baselines, inspect missed and excessive escalations, and version every policy change.

A compact decision rule follows from the framework. Require preventive human approval when the action is consequential, difficult to reverse, and not fully governable by deterministic checks within the available response time. Prefer automated controls plus observation when the action is low-impact, reversible, and independently verifiable. Use staged execution when the work can be made reversible before promotion. This rule is an author synthesis of consequence-sensitive automation, runtime enforcement, and risk-management guidance. [4][5][6][14]

## Sources

1. Anthropic. (2024). "Building Effective Agents." Official engineering guidance on workflows, agents, checkpoints, environmental feedback, and human oversight.
   https://www.anthropic.com/engineering/building-effective-agents [high]

2. Anthropic. (2025). "Our Framework for Developing Safe and Trustworthy Agents." Official framework on keeping humans in control while enabling bounded autonomy.
   https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents [high]

3. Shavit, Y., Agarwal, S., Brundage, M., et al. (2023). "Practices for Governing Agentic AI Systems." OpenAI white paper on constrained action, monitoring, legibility, attribution, and interruptibility.
   https://cdn.openai.com/papers/practices-for-governing-agentic-ai-systems.pdf [high]

4. Microsoft Security. (2026). "Defense in Depth for Autonomous AI Agents." Official security guidance on application-layer enforcement, least permission, and deterministic human-in-the-loop triggers.
   https://www.microsoft.com/en-us/security/blog/2026/05/14/defense-in-depth-autonomous-ai-agents [high]

5. Tabassi, E. (2023). "Artificial Intelligence Risk Management Framework (AI RMF 1.0)." NIST AI 100-1.
   https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf [high]

6. Parasuraman, R., Sheridan, T. B., and Wickens, C. D. (2000). "A Model for Types and Levels of Human Interaction with Automation." IEEE Transactions on Systems, Man, and Cybernetics - Part A, 30(3), 286-297.
   https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=11760769&retmode=xml [high]

7. Bainbridge, L. (1983). "Ironies of Automation." Automatica, 19(6), 775-779. DOI: 10.1016/0005-1098(83)90046-8. [high]

8. Lee, J. D., and See, K. A. (2004). "Trust in Automation: Designing for Appropriate Reliance." Human Factors, 46(1), 50-80.
   https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=15151155&retmode=xml [high]

9. Amershi, S., Weld, D., Vorvoreanu, M., et al. (2019). "Guidelines for Human-AI Interaction." Proceedings of CHI 2019. DOI: 10.1145/3290605.3300233.
   https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf [high]

10. Bucinca, Z., Malaya, M. B., and Gajos, K. Z. (2021). "To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-Assisted Decision-Making." Proceedings of the ACM on Human-Computer Interaction, 5(CSCW1), Article 188.
    https://www.eecs.harvard.edu/~kgajos/papers/2021/bucinca21trust.pdf [high]

11. Lyell, D., and Coiera, E. (2017). "Automation Bias and Verification Complexity: A Systematic Review." Journal of the American Medical Informatics Association, 24(2), 423-431.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC7651899 [high]

12. Green, B., and Chen, Y. (2019). "The Principles and Limits of Algorithm-in-the-Loop Decision Making." Proceedings of the ACM on Human-Computer Interaction, 3(CSCW), Article 50.
    https://www.benzevgreen.com/wp-content/uploads/2019/09/19-cscw.pdf [high]

13. Raji, I. D., Smart, A., White, R. N., et al. (2020). "Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing." FAT* 2020, 33-44.
    https://www.nist.gov/system/files/documents/2021/08/23/ai-rmf-rfi-0038.pdf [high]

14. Autio, C., Schwartz, R., Dunietz, J., et al. (2024). "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile." NIST AI 600-1.
    https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=958388 [high]

15. LangChain. "Human-in-the-Loop." Official LangChain documentation for policy-based tool-call interrupts, checkpointing, and approval decisions.
    https://docs.langchain.com/oss/python/langchain/human-in-the-loop [medium]

## See Also

- `library/coding-agentic-ai/agent-sandboxing-and-security.md` -- explains why approval is one layer in a broader system of least privilege, policy enforcement, and execution isolation.
- `library/coding-agentic-ai/tool-use-and-function-calling.md` -- describes the proposal-execute boundary where approval middleware intercepts consequential tool calls.
- `library/coding-agentic-ai/multi-agent-orchestration.md` -- provides the handoff and coordination structures in which human review can become an explicit workflow node.
- `library/coding-agentic-ai/agent-observability-and-debugging.md` -- defines the traces and spans needed to audit triggers, decisions, and post-approval execution.
- `library/coding-agentic-ai/agent-evaluation-and-benchmarking.md` -- supplies the measurement discipline for testing the complete human-agent workflow.
- `library/coding-agentic-ai/anchor-coding-agentic-ai.md` -- places human-in-the-loop patterns within the engineering and operation of agentic systems.
