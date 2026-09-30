---
name: agent-uncertainty-verification-and-abstention
id: 20260930T023606Z
tier: library-topic
domain: coding-agentic-ai
author: Librarian
tags: [agent-uncertainty, verification, abstention, calibration, selective-prediction, human-escalation, stopping-rules]
links: [library/coding-agentic-ai/agent-harness-design.md, library/coding-agentic-ai/human-in-the-loop-patterns.md, library/coding-agentic-ai/agent-cost-latency-and-resource-governance.md, library/coding-agentic-ai/tool-use-and-function-calling.md, library/coding-agentic-ai/agent-evaluation-and-benchmarking.md]
---

# Agent Uncertainty Requires External Evidence and Enforced Abstention, Not Self-Confidence

A tool-using agent should decide whether to continue from the quality of its evidence, the consequences and reversibility of the next action, and the expected value of another check, not from a fluent statement of confidence. Model confidence can inform that decision, but reliable operation requires calibrated signals, independent or deterministic verification, explicit escalation routes, and an abstention state that prevents action before an unresolved risk becomes a side effect. [1][3][8][13]

## Background

Uncertainty in an agent is not one number. A language model may be uncertain about an answer, while the surrounding runtime may be uncertain whether a tool succeeded, whether the user authorized a particular action, whether two sources refer to the same object, or whether a changing environment still satisfies a plan's preconditions. Classical calibration asks whether predictions assigned a stated probability are correct at approximately that frequency. Selective prediction adds a decision: accept a prediction or reject it, trading coverage against the risk among accepted cases. These ideas supply useful measurement tools, but an acting agent must apply them across a sequence of observations and possible side effects rather than to one fixed prediction. [4][5][8]

Modern confidence work developed because high predictive accuracy does not imply reliable probabilities. Guo et al. found that modern neural networks could be poorly calibrated and showed that post-hoc temperature scaling improved calibration on many of their tested classification settings. Calibration therefore concerns the relationship between a score and empirical correctness, not the persuasiveness of an individual output. A score of 0.9 is useful only if similarly scored cases are correct at about the promised rate on the relevant distribution; it is not a proof that the present case is correct. [5]

Language generation makes the problem harder. Jiang et al. found that the probabilities of T5, BART, and GPT-2 were poorly calibrated for the question-answering tasks they studied, while later work showed that larger language models could provide useful self-evaluations under particular formats and task distributions. Kadavath et al. reported encouraging calibration for multiple-choice and true-or-false formats and for trained estimates of whether a model knew an answer, but also reported weaker generalization of that estimate to new tasks. The combined lesson is conditional: some internal signals contain information about correctness, but their calibration depends on elicitation method, model, task, and distribution. [6][7][8]

Verbal confidence is especially easy to misuse. A sentence such as "I am highly confident" is generated text, not a direct readout of a stable probability. Groot and Valdenegro-Toro evaluated prompted verbal uncertainty across several language and vision-language models and found high calibration error and frequent overconfidence in their tested tasks. The broader survey by Geng et al. distinguishes confidence sources based on token probabilities, multiple samples, verbal reports, and trained estimators, and treats calibration as a separate operation from confidence estimation. An agent should therefore preserve which method produced a score and on which validation distribution it was calibrated. [8][11]

Abstention provides a control response to uncertainty. In selective prediction, a system withholds predictions on low-confidence examples and is evaluated through the relationship between coverage and error on accepted examples. Xin et al. studied this setting across NLP tasks and compared models and confidence estimators, demonstrating that abstention quality depends on how well the confidence signal ranks likely errors, not merely on overall task accuracy. This distinction matters operationally: an agent can be capable on average yet poor at identifying the particular cases in which it should stop. [4]

A tool-using agent adds temporal and causal stakes. It can often gather evidence before committing, but each tool call consumes time and resources, may reveal untrusted information, and may itself change the environment. Recent agent-abstention benchmarks therefore evaluate both pre-execution triggers visible in the instruction and runtime triggers discovered only after interaction. AgentAbstain reports cases in which systems recognized a restriction yet continued, or abstained only after an irreversible action; the companion agentic-abstention work distinguishes timely abstention from delayed stopping after unnecessary actions. [1][2]

This topic stays inside agent engineering. It does not attempt a general theory of epistemic uncertainty, model training, Bayesian deep learning, or AI ethics. Its subject is the operational control problem: how a harness detects that its evidence is insufficient, selects an information or verification action, escalates when authority or judgment is missing, and terminates without converting uncertainty into an unsupported claim or external side effect. The author's synthesis is that the harness, rather than the model's prose, must own that control boundary. [13][15]

## Core Concepts

### Uncertainty is a property of a decision state

The author's synthesis is to represent uncertainty as unresolved conditions attached to the next decision. A run state should record the goal, proposed next action, required evidence, observed evidence, contradictions, authorization, applicable policy, remaining resources, and possible recovery paths. The question is not simply "How confident is the model?" It is "What fact, permission, identity, or outcome remains unresolved, and can the next action safely proceed while it remains unresolved?" This framing aligns model uncertainty with the state and lifecycle controls recommended by NIST and with agent designs that obtain ground truth from tool results during execution. [13][15]

At least six uncertainty classes should be distinguished. **Knowledge uncertainty** concerns whether the model or retrieved sources support a factual claim. **Task uncertainty** concerns ambiguous objectives, missing inputs, conflicting constraints, or unclear completion criteria. **Tool uncertainty** concerns which tool applies, whether its schema and semantics match the task, and whether its response is complete. **State uncertainty** concerns whether the external world still matches the state assumed by the plan. **Outcome uncertainty** concerns whether a requested side effect succeeded, failed, or partially completed. **Evaluator uncertainty** concerns disagreement or weakness in tests, judges, reviewers, or scoring rules. This taxonomy is the author's synthesis of the failure scenarios in agent-abstention research, confidence research, and risk-management guidance. [1][2][3][8][13]

The classes imply different remedies. Missing knowledge may justify retrieval from an authoritative source. Task ambiguity may require a targeted question. Tool uncertainty may require schema inspection or a dry run. State uncertainty may require a fresh read. Outcome uncertainty requires a read-back keyed to the attempted action, not a blind retry. Evaluator uncertainty may require a stronger deterministic test, an independent reviewer, or an explicit unresolved status. Treating every class as a request for more model reasoning risks repeating the same unsupported inference. [1][3][10][15]

### Confidence signals form an evidence ladder

A model can emit several uncertainty signals, but they have different meanings. Verbal confidence is cheap and available from black-box systems, yet workshop evidence shows it can be overconfident and poorly calibrated. Token probabilities expose distributional information at the word level but do not directly represent whether a multi-sentence claim is correct. Repeated sampling can reveal answer instability, although semantically equivalent phrasings must not be counted as disagreement. Trained self-evaluation or external predictors can estimate correctness if they are validated on relevant tasks. None of these signals establishes that an external action is authorized or that a tool actually changed state. [7][8][9][11]

Semantic entropy addresses one limitation of raw sequence variation. Farquhar et al. grouped sampled answers by meaning before calculating uncertainty, so alternative phrasings of the same answer did not inflate uncertainty. Their experiments found semantic entropy more effective than naive token-sequence entropy for detecting confabulations across tested question-answering, mathematical, and biographical generation settings. This is a detector for one class of unsupported generation, not a universal action policy; it does not know whether a payment is authorized, whether a repository is current, or whether two independent sources are themselves wrong in the same way. [9]

Calibration maps a score to observed reliability. It should be measured on a held-out distribution, monitored after model or prompt changes, and reported by relevant task slice. A confidence estimator calibrated on short factual questions should not be assumed calibrated for code changes, browser actions, or multi-step investigations. Distribution shift is itself an uncertainty signal: unfamiliar tools, novel schemas, changed environments, and task combinations outside the validation set should lower the authority assigned to a score even if the numeric output remains high. [5][6][7][8][13]

The author's synthesis is an evidence ladder. At the bottom are unsupported verbal assurances. Above them are model-derived signals such as logits, samples, semantic consistency, or trained confidence predictors. Above those are evidence from a different process, such as retrieval from a primary source or evaluation by a separately prompted or separately trained model. At the top, where available, are deterministic checks and direct observations of the target state: a schema validator, calculation, test suite, cryptographic identity, database read-back, or human decision by the authorized person. Higher rungs are not always cheaper or infallible, but they are more independent of the generation that created the claim. [4][9][10][13]

### Verification quality depends on independence and fit

Verification is not one generic extra model call. A verifier must be capable of detecting the failure in question and sufficiently independent of the process that produced it. Asking the same model to reconsider an answer with the same evidence can reproduce the same bias or convert a correct answer into an incorrect one. Huang et al. found that intrinsic self-correction without external feedback did not improve reasoning across their studied settings and sometimes degraded it. Their result does not show that revision is useless; it shows that another pass is not independent evidence merely because it is called verification. [10]

Deterministic verification is strongest when the requirement can be encoded exactly. A parser can validate a schema, a test can exercise behavior, a query can inspect external state, and a numerical program can recompute a value. These checks prove only the properties they test. A passing unit test does not establish authorization, a successful API status does not prove the intended record changed, and agreement between two models does not prove either consulted a valid source. The author's synthesis is to pair each material claim or action with the cheapest check that could actually falsify it, then read back consequential external effects. [13][15]

Model-based verifiers remain useful for open-ended criteria, but their correlation must be exposed. Separate instructions, context, model family, data source, or human expertise can reduce shared error; none guarantees independence. When generators and verifiers share the same evidence gap, confident agreement can amplify error. The run record should therefore identify who or what produced each verdict, what evidence it saw, which rubric it applied, and whether the verdict can block execution. [8][10][13]

Contradictory evidence should create a first-class state rather than trigger silent averaging. If a tool says a transaction failed while a subsequent read shows the change, the read-back should govern the outcome. If two authoritative sources disagree, the agent should preserve the disagreement, inspect dates and definitions, and avoid collapsing them into one invented fact. If tests disagree because they cover different conditions, the difference should become part of the result. The author's synthesis is that conflict resolution proceeds by authority, freshness, identity, scope, and directness of observation; unresolved material conflict raises the action threshold. [1][3][13]

### The next action should maximize decision-relevant information

Uncertainty does not always require stopping. An agent may have a reversible, low-cost action that is expected to resolve the exact missing condition. A read-only query can confirm a file version, a search can locate a primary source, a dry run can expose arguments without committing them, and a targeted question can obtain an omitted constraint. The relevant quantity is not total information gathered but expected decision value: whether the observation could change which safe action is selected. [3][13][15]

The author's synthesis is a five-way policy. **Continue** when required evidence and authorization are present and the next action is within the accepted risk envelope. **Verify** when a bounded check can test a material assumption or outcome. **Gather information** when a specific missing fact is retrievable without disproportionate risk or cost. **Ask or escalate** when the missing input is a human preference, authority, exception, or judgment the agent cannot legitimately supply. **Abstain and stop** when prerequisites remain unresolved, no permitted information action has positive expected value, the remaining budget cannot support verification, or the downside of an error exceeds the authorized tolerance. [1][2][3][13]

Consequences and reversibility set the threshold. A low-impact, easily reversible formatting change can tolerate weaker evidence than a financial transfer, disclosure, deletion, production deployment, or medical recommendation. Irreversibility also changes timing: the gate must run before the commitment, because refusing after the external state changed is not abstention. AgentAbstain names this failure pattern post-hoc abstention and evaluates whether agents avoid commit-class actions in should-abstain variants. [1]

Remaining options matter as much as current uncertainty. If one cheap check can separate success from failure, continuing to that check is rational. If repeated searches return the same weak source, more calls may add cost without reducing uncertainty. If the agent has exhausted its verifier budget, the correct state may be blocked or incomplete even when a plausible answer is available. This is the author's synthesis of selective risk, cost-aware agent operation, and trajectory-level abstention: continue only while another permitted step has a credible route to decision-changing evidence. [2][4]

### Abstention is a typed, recoverable state

A useful abstention is not a generic refusal. It should identify the blocked action, the unmet precondition, evidence already checked, the risk of proceeding, and the smallest recovery route. A task-ambiguity abstention may ask one focused question. An authorization abstention may request approval bound to the exact action and target. A tool-outcome abstention may record an idempotency key and require a status query. An evidence abstention may provide verified partial findings while marking the disputed claim unresolved. Ojewale and Venkatasubramanian describe informed abstention as a precondition-aware pause that blocks the next tool call, names what is missing, and routes to a recovery action. [3]

The state should be durable. A paused task needs enough information for the same or a replacement worker to resume without reconstructing authority from prose or repeating uncertain side effects. The record should include the action proposal, relevant state version, evidence, failed checks, approval status, retry count, resource balance, and terminal reason. NIST's AI RMF calls for documented roles, monitoring, response, recovery, appeal, and override mechanisms; the generative-AI profile adds actions for human-AI oversight and structured feedback. [13][14]

Abstention also has a false-positive cost. A system that refuses every unfamiliar task avoids some errors while providing little value, and a system that escalates routine decisions overloads human reviewers. Evaluation must therefore pair should-act and should-abstain cases, measure timely stopping, and report both unsafe continuation and unnecessary refusal. The paired design used by AgentAbstain and the request- versus environment-based scenarios in Agentic Abstention operationalize this two-sided boundary. [1][2]

### The policy must be evaluated over trajectories

Final task success is insufficient for an uncertainty-control policy. A run can reach the right result after an unauthorized action, stop only after damage, or consume unreasonable resources verifying a trivial claim. Conversely, a correct abstention can be scored as task failure if the benchmark rewards only completion. Recent agent-abstention research was motivated by this measurement gap and uses traces, paired tasks, and commit-level checks to distinguish acting correctly from correctly declining to act. [1][2][3]

The author's synthesis is to record at least: act accuracy on should-act cases; abstention recall on should-abstain cases; paired accuracy; time or tool calls from first observable trigger to stop; post-hoc commitment rate; false escalation rate; verification cost; residual error among accepted actions; and recovery success after missing evidence is supplied. Results should be sliced by uncertainty class, consequence, reversibility, tool family, model, harness, and whether the trigger was visible before execution or discovered at runtime. [1][2][4][8]

A calibrated policy can still be wrong on an individual case. Calibration supports aggregate decisions; deterministic checks, policy gates, and human authority govern individual high-consequence actions. The author's synthesis is therefore that model self-confidence is advisory telemetry. The harness converts evidence and risk into an enforceable transition, and only the harness can guarantee that an unresolved state prevents the next side effect. [3][13][15]

## Evidence

### Calibration studies show that confidence is conditional

Guo et al. evaluated modern neural networks on image and document classification and found substantial miscalibration, then showed that temperature scaling was an effective post-hoc method on many tested datasets. The method adjusts probability calibration without changing the predicted class order, illustrating that confidence quality is separable from raw predictive accuracy. It also illustrates a limitation for agents: a calibrated score still needs a threshold tied to the cost of acting or abstaining. [5]

Jiang et al. tested T5, BART, and GPT-2 on diverse question-answering datasets and found their probabilities poorly calibrated before correction. They evaluated fine-tuning, post-hoc probability modification, and changes to outputs or inputs as calibration methods. Kadavath et al. later found that larger models could provide encouraging self-evaluations when questions and meta-questions were formatted appropriately, especially when models considered multiple samples, but that estimates of whether the model knew an answer generalized imperfectly to new tasks. These results are not contradictory: they show that confidence information exists under some conditions but is not a distribution-free safety signal. [6][7]

Groot and Valdenegro-Toro directly tested prompted verbal uncertainty for GPT-4, GPT-3.5, LLaMA 2, PaLM 2, GPT-4V, and Gemini Pro Vision. Their reported results showed high calibration error and frequent overconfidence on the language and vision-language tasks examined. Geng et al.'s NAACL survey organizes the wider field into confidence-estimation and calibration methods and emphasizes task, access, and evaluation differences. Together, these sources support measuring a confidence channel before using it to control action rather than treating natural-language assurance as calibrated by default. [8][11]

### Sampling and abstention improve some error detection, with bounded scope

Farquhar et al. evaluated semantic entropy on question answering, mathematical word problems, and biographical generation. Their method samples multiple responses, clusters semantically equivalent answers, and calculates uncertainty over meanings rather than surface strings. It outperformed naive sequence-entropy measures for detecting confabulations in the reported settings. The method demonstrates that disagreement among meanings can be informative, while its scope remains probabilistic generation rather than authorization, tool identity, or external-state verification. [9]

Xin et al. evaluated selective prediction across NLP tasks and compared confidence estimators. Their study formalizes the risk-coverage trade-off: abstaining on some cases can reduce error among the cases answered, but only if the score ranks difficult or erroneous cases effectively. Tomani et al. applied uncertainty-based abstention to large-language-model question answering and reported improvements in correctness, hallucination avoidance on unanswerable questions, and safety under their tested uncertainty measures and models. These studies support abstention as a reliability mechanism, not the claim that one fixed threshold transfers across models, tasks, or consequences. [4][12]

### Self-review is not equivalent to external verification

Huang et al. separated intrinsic self-correction from correction guided by external feedback. Across the reasoning tasks and models they studied, asking a model to revise from its own capabilities did not reliably improve performance and sometimes made answers worse. The study found that improvements attributed to self-correction in some prior setups depended on oracle or external feedback. This evidence supports routing verification through tests, tools, retrieved evidence, independent evaluators, or people when those channels exist, rather than renaming another unsupported generation as a check. [10]

Anthropic's engineering guidance reports a compatible production pattern: agents should obtain ground truth from the environment during execution, use evaluator-optimizer loops where evaluation criteria are clear, pause at checkpoints or blockers for human feedback, and have explicit stopping conditions. This is practitioner evidence rather than a controlled comparative experiment, but it identifies which runtime mechanisms teams use to keep open-ended loops bounded. [15]

### Agent-level benchmarks expose timely-abstention failures

AgentAbstain evaluates abstention as an agentic capability rather than a text-only refusal. Its first version contains 263 paired tasks across 42 executable sandbox environments, with should-act and should-abstain variants created through controlled changes to instructions, tools, or environment state. Across 17 frontier models and four harnesses, the paper reports a best paired accuracy of 59.5 percent and identifies post-hoc abstention, in which an agent commits an irreversible action before refusing. The paired construction is important because it penalizes both unsafe continuation and indiscriminate refusal. [1]

Luo et al. formulate agentic abstention as a sequential choice among answering, taking another action, and stopping. Their evaluations cover ambiguity visible in requests and infeasibility discovered through interaction; most evaluated systems reportedly achieved less than 50 percent average abstention recall. They also report that harness choice materially affects behavior and that a trajectory-derived context method, convolve, raised timely abstention recall for Llama-3.3-70B on their WebShop setting from 26.7 to 57.4. The result suggests that stopping behavior is partly a system property that can change through context and trajectory design without changing model weights. [2]

Ojewale and Venkatasubramanian evaluate informed abstention across 144 scenarios and seven model families. Their framework requires a precondition-aware pause, a named missing condition, a blocked next tool call, and a concrete recovery path. The paper reports hazardous-action blocking of 87.5 to 91 percent and usability on authorized scenarios of 75 to 92 percent for its runtime-enforcement configurations, showing a tunable trade-off rather than an unavoidable choice between total refusal and uncontrolled compliance. These are preliminary results in an AIES 2026 paper and should be reproduced across additional tasks and harnesses. [3]

The three 2026 studies use different tasks, measures, and interventions, so their percentages should not be combined into one performance claim. Their convergent result is narrower: task-solving capability does not guarantee timely abstention, final-answer grading misses action timing, and the harness can materially alter whether an agent checks, continues, or stops. [1][2][3]

### Risk frameworks place uncertainty inside lifecycle control

NIST AI RMF 1.0 treats validity, reliability, safety, transparency, monitoring, human oversight, response, recovery, appeal, and override as connected lifecycle concerns. It calls for documenting limitations beyond development conditions and for managing risk in proportion to context and possible harm. The Generative AI Profile extends that framework with generative-AI risks, human-AI configuration concerns, structured feedback, incident handling, and explicit oversight roles. These sources do not prescribe one abstention algorithm; they establish that thresholds and interventions belong to a governed system rather than an improvised model statement. [13][14]

Taken together, the evidence supports a layered conclusion. Model-derived uncertainty can rank risk in some settings; calibration can improve the meaning of a score; semantic sampling can detect some confabulations; external feedback improves correction when it is valid; paired agent benchmarks reveal failures that answer-only tests hide; and runtime enforcement can block some unsafe continuations. No cited source establishes a universal confidence number that safely controls every agent trajectory. The author's synthesis is therefore to combine signals according to their validated scope and to let consequence-sensitive, enforceable gates decide action. [1][3][5][8][9][10][13]

## Implications

### For agent and harness architects

Start with an explicit uncertainty state machine. Before every consequential action, the harness should be able to represent ready, needs-verification, needs-information, needs-human-input, blocked, abstained, and failed states. Each transition should name the evidence that enables it and the policy that authorizes it. A model may recommend a transition, but runtime code should enforce whether the tool call is released. This implements the distinction between model-derived telemetry and operational authority found across abstention research and risk-management guidance. [1][3][13]

Bind thresholds to action classes rather than using one global confidence cutoff. Read-only retrieval, reversible drafts, bounded computations, credential use, external messages, deletions, financial commitments, and production changes have different consequences. The author's synthesis is to classify tools by observation, verification, preparation, and commitment; require stronger evidence as consequence and irreversibility rise; and forbid a commitment tool while a material precondition remains unresolved. [1][3]

Reserve resources for checking and stopping. A run that spends its full token, time, or tool-call budget on generation has no capacity left to verify the result. Set separate limits for information gathering, verifier retries, conflict resolution, and final read-back. When repeated steps stop changing the evidence state, terminate with a typed partial or blocked result. This makes diminishing prospects observable rather than allowing a loop to continue until an arbitrary timeout. [2][15]

Treat distribution shift as a routing event. A new tool version, unseen schema, unfamiliar domain, changed policy, or task outside the calibration set should reduce reliance on model-derived confidence. The route may be a sandbox, a deterministic schema check, a specialist, or a human reviewer. NIST requires documenting generalizability limitations, while calibration studies show that score quality depends on the tested distribution. [5][7][13]

### For tool and workflow designers

Design tool responses to reduce outcome uncertainty. Return stable operation identifiers, explicit status codes, target identity, version, affected-object count, validation errors, and a way to query the result. Distinguish accepted, completed, partially completed, rejected, and unknown outcomes. A timeout after a state-changing request should not be represented as ordinary failure, because blind retry may duplicate the effect. The author's synthesis follows the agent-abstention requirement to stop on runtime uncertainty and the AI RMF emphasis on response and recovery. [1][13]

Provide noncommitting checks where possible. Dry-run, preview, validate, estimate, diff, and read-back operations let an agent convert uncertainty into evidence without consuming the irreversible option. Tool descriptions should state side effects, required authority, retry safety, and which response fields establish success. If a tool cannot expose those semantics, the harness should treat it as higher risk rather than infer behavior from its name. [1][3][15]

Make ambiguity machine-visible. Missing required fields should produce structured errors, not plausible defaults. Conflicting identifiers should return candidate matches and refuse mutation. Stale versions should fail preconditions. Policy boundaries should produce a stable denial that an agent cannot override by rephrasing the request. These mechanisms convert uncertainty from model interpretation into inspectable system state. [3][13]

### For evaluation and reliability teams

Build paired evaluations. For each ordinary task, create a minimally changed variant in which an essential input, authority, tool capability, environmental condition, or evidence source is missing or contradictory. Score both sides together so a system passes only when it acts on the valid case and stops or asks on the invalid case. AgentAbstain demonstrates this design at executable-environment scale. [1]

Grade the trajectory at the first point where the trigger becomes observable. Record whether the agent gathered a relevant fact, repeated equivalent calls, attempted a workaround, escalated, or committed before stopping. A final sentence saying "I cannot proceed" should fail if the agent already sent, deleted, disclosed, or purchased. Report timely and delayed abstention separately, as in current agentic-abstention research. [1][2]

Measure the two-sided cost. Unsafe continuation creates harm; unnecessary abstention creates lost utility and human load. Report accepted-action error, should-act success, should-abstain recall, paired accuracy, false escalation, reviewer burden, time to resolution, and coverage-risk curves where applicable. Stratify by action consequence because one false commitment may matter more than many harmless refusals. Selective-prediction research and NIST's consequence-sensitive risk framing support this measurement design. [4][13]

Test confidence channels before deployment. Reliability diagrams, expected calibration error, Brier-style losses, risk-coverage curves, and task-slice analyses answer different questions. A score can be calibrated overall while failing on a rare high-consequence slice, and a strong ranking can support abstention even when the numeric probabilities need recalibration. The broader confidence literature therefore supports publishing the task distribution, method, threshold, and update policy alongside the score. [5][6][8]

Inject conflicts and partial failures. Return two plausible but incompatible sources, a successful status with unchanged state, a timeout after completion, an out-of-date schema, a verifier disagreement, a missing approval, and a budget exhausted before the final check. The desired outcome is not always task completion; it is a correct, timely, and recoverable state transition. [1][2][3]

### For product owners and human reviewers

Define which uncertainties require a person. Humans should supply preferences, legal or organizational authority, exceptions, and judgments that cannot be encoded or independently checked. They should not be asked to approve routine steps solely because the system lacks a proper validator. An escalation packet should contain the exact proposed action, target, evidence, unresolved condition, alternatives, consequence, reversibility, and decision deadline. NIST calls for defined human-AI roles, while agent engineering guidance recommends checkpoints tied to blockers and feedback that can change the result. [13][14][15]

Make approval specific and expiring. Approval for a draft does not authorize publication; approval for one target does not transfer to another; approval before a material state change should be revalidated. The author's synthesis is to bind approval to the action, arguments, target, state version, policy version, approver, and expiration. This prevents natural-language history from becoming a vague reservoir of authority. [3][13]

Protect reviewers from escalation overload. Route only cases whose missing input falls within the reviewer's authority and whose decision changes the action. Group repeated low-value alerts, show the evidence already checked, and measure override quality and response time. A human gate without sufficient context, time, or power is delay rather than verification. [13][14]

### For operators and incident responders

Log the uncertainty transition, not only the final answer. Preserve the trigger, proposed action, confidence signals, retrievals, verifier outputs, policy result, tool receipts, human decision, and terminal state. Redact sensitive content while retaining enough identity and provenance to reconstruct why the gate fired. This enables investigation of false continuation, false refusal, and post-hoc abstention. [1][13][14]

Monitor for changed calibration and changed behavior. Model updates, prompt edits, tool changes, retrieval sources, and new user populations can shift both confidence and abstention. Re-run paired cases after each material change and sample production traces for new trigger classes. NIST treats monitoring and risk response as lifecycle activities rather than one-time validation. [13][14]

When a failure occurs, fix the decision boundary that allowed it. If an agent acted without authority, add an enforceable authorization precondition; if it retried an unknown outcome, add status query and idempotency semantics; if it trusted verbal confidence, replace or calibrate the signal; if it stopped unnecessarily, identify which evidence should have released the gate. The original incident should become a paired regression: one case that must proceed and one that must abstain. [1][3][5]

### A practical decision rule

The author's synthesis is a compact rule for each next action. First, identify the exact action and whether it observes, verifies, prepares, or commits. Second, list material preconditions and mark each as supported, contradicted, stale, or unknown. Third, choose the strongest affordable check that could change the decision. Fourth, compare the expected information gain with cost, remaining budget, consequence, and reversibility. Fifth, continue only if the evidence and authority threshold for that action class is met; otherwise gather, verify, ask, or abstain with a typed recovery route. [1][3][4][13]

The rule is intentionally external to the model's self-description. A model may say it is certain and still face a missing authorization. It may say it is uncertain while a deterministic test proves the relevant property. It may produce two agreeing samples from the same false premise, or disagree in wording while preserving one meaning. Reliable autonomy therefore does not require eliminating uncertainty. It requires making uncertainty observable, assigning it the right evidence channel, and ensuring that unresolved material uncertainty cannot cross the boundary into an unsupported claim or irreversible action. [5][9][10][13]

## Sources

1. Liu, X., Zhang, Y. E., Kasprova, V., Rabbani, P., Zahraei, P. S., Zhang, T., Ebrahimpour-Boroojeny, A., and Chandrasekaran, V. (2026). "AgentAbstain: Do LLM Agents Know When Not to Act?" arXiv:2607.10059.
   https://arxiv.org/abs/2607.10059 [high]

2. Luo, H., Wen, B., and Wang, L. L. (2026). "Agentic Abstention: Do Agents Know When to Stop Instead of Act?" arXiv:2606.28733.
   https://arxiv.org/abs/2606.28733 [high]

3. Ojewale, V. and Venkatasubramanian, S. (2026). "Designing for Doubt: The Case for Informed Abstention in Autonomous Agents." Accepted to AIES 2026; arXiv:2606.02965.
   https://arxiv.org/abs/2606.02965 [high]

4. Xin, J., Tang, R., Yu, Y., and Lin, J. (2021). "The Art of Abstention: Selective Prediction and Error Regularization for Natural Language Processing." ACL-IJCNLP 2021, pages 1040-1051.
   https://aclanthology.org/2021.acl-long.84/ [high]

5. Guo, C., Pleiss, G., Sun, Y., and Weinberger, K. Q. (2017). "On Calibration of Modern Neural Networks." ICML 2017, PMLR 70, pages 1321-1330.
   https://proceedings.mlr.press/v70/guo17a.html [high]

6. Jiang, Z., Araki, J., Ding, H., and Neubig, G. (2021). "How Can We Know When Language Models Know? On the Calibration of Language Models for Question Answering." Transactions of the Association for Computational Linguistics, 9.
   https://aclanthology.org/2021.tacl-1.57/ [high]

7. Kadavath, S., Conerly, T., Askell, A., et al. (2022). "Language Models (Mostly) Know What They Know." arXiv:2207.05221, version 4.
   https://arxiv.org/abs/2207.05221 [high]

8. Geng, J., Cai, F., Wang, Y., Koeppl, H., Nakov, P., and Gurevych, I. (2024). "A Survey of Confidence Estimation and Calibration in Large Language Models." NAACL 2024, pages 6577-6595.
   https://aclanthology.org/2024.naacl-long.366/ [high]

9. Farquhar, S., Kossen, J., Kuhn, L., and Gal, Y. (2024). "Detecting Hallucinations in Large Language Models Using Semantic Entropy." Nature, 630, pages 625-630.
   https://www.nature.com/articles/s41586-024-07421-0 [high]

10. Huang, J., Chen, X., Mishra, S., Zheng, H. S., Yu, A. W., Song, X., and Zhou, D. (2024). "Large Language Models Cannot Self-Correct Reasoning Yet." ICLR 2024.
    https://openreview.net/forum?id=IkmD3fKBPQ [high]

11. Groot, T. and Valdenegro-Toro, M. (2024). "Overconfidence is Key: Verbalized Uncertainty Evaluation in Large Language and Vision-Language Models." TrustNLP 2024, pages 145-171.
    https://aclanthology.org/2024.trustnlp-1.13/ [high]

12. Tomani, C., Chaudhuri, K., Evtimov, I., Cremers, D., and Ibrahim, M. (2024). "Uncertainty-Based Abstention in LLMs Improves Safety and Reduces Hallucinations." arXiv:2404.10960.
    https://arxiv.org/abs/2404.10960 [high]

13. National Institute of Standards and Technology. (2023). "Artificial Intelligence Risk Management Framework (AI RMF 1.0)." NIST AI 100-1.
    https://doi.org/10.6028/NIST.AI.100-1 [high]

14. National Institute of Standards and Technology. (2024). "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile." NIST AI 600-1.
    https://doi.org/10.6028/NIST.AI.600-1 [high]

15. Anthropic. (2024). "Building Effective Agents." Official engineering guidance on agent workflows, environmental feedback, human checkpoints, evaluators, and stopping conditions.
    https://www.anthropic.com/engineering/building-effective-agents [high]

## See Also

- `library/coding-agentic-ai/agent-harness-design.md` -- the runtime state machine that must enforce verification, escalation, and stopping transitions.
- `library/coding-agentic-ai/human-in-the-loop-patterns.md` -- how consequence, ambiguity, and authority route selected decisions to human oversight.
- `library/coding-agentic-ai/agent-cost-latency-and-resource-governance.md` -- how budgets and diminishing expected value constrain further checking or search.
- `library/coding-agentic-ai/tool-use-and-function-calling.md` -- tool selection, validation, failure semantics, and read-back at the proposal-execution boundary.
- `library/coding-agentic-ai/agent-evaluation-and-benchmarking.md` -- trajectory, outcome, reliability, and cost metrics for evaluating abstention policies.
