---
name: pre-mortems-and-post-mortems
id: 20260921T173553Z
tier: library-topic
domain: probabilistic-thinking-forecasting
author: Librarian
tags: [pre-mortems, post-mortems, prospective-hindsight, decision-review, calibration, organizational-learning, uncertainty]
links: [library/probabilistic-thinking-forecasting/inside-outside-view.md, library/probabilistic-thinking-forecasting/scenario-planning-and-analysis.md, library/probabilistic-thinking-forecasting/calibration-and-overconfidence.md, library/self-improvement/decision-journals.md]
---

# Pre-Mortems and Post-Mortems Turn Uncertain Decisions Into Testable Learning Cycles

A pre-mortem imagines that a proposed decision has failed and searches backward for plausible causes before commitment, while a post-mortem reconstructs what happened after execution and converts the comparison into revised rules. Used together, they make assumptions, probabilities, warning signals, and causal claims explicit enough to test rather than allowing the observed outcome to rewrite the original forecast ([1] [2] [3]). Their value is not clairvoyance or retrospective certainty; it is a disciplined feedback loop that separates what was knowable at decision time from what became visible only afterward ([3] [4] [5]).

## Background

Learning from uncertain decisions is difficult because an outcome contains less information than it appears to contain. A project may succeed despite weak reasoning because favorable events intervened, or fail despite sound reasoning because a low-probability hazard occurred. Baron and Hershey demonstrated this problem experimentally: participants rated otherwise identical decisions and decision makers more favorably when outcomes were favorable, even when participants had the information available to the original decision maker and said outcomes should not affect the evaluation ([4]). This outcome bias turns a realized result into a false verdict on the quality of the preceding process.

Outcome knowledge also changes the reconstructed past. Fischhoff's three experiments found that people who learned how an event ended increased the event's perceived prior likelihood, altered which evidence seemed relevant, and underestimated the effect that outcome knowledge had on their judgments ([3]). Roese and Vohs later organized hindsight bias into three related forms: distorted memory of an earlier judgment, belief that the outcome was objectively inevitable, and belief that one personally could have foreseen it ([5]). Their review also found that hindsight encourages a single causal story and greater confidence in one's judgment, both of which obstruct learning from alternatives that did not occur ([5]). A post-mortem that begins only after the outcome and lacks a preserved ex ante record is therefore vulnerable at its foundation.

The pre-mortem developed as a structural response to a different but related problem: plans suppress consideration of failure while there is still time to change them. Mitchell, Russo, and Pennington defined prospective hindsight as explaining a future event as though it had already happened and experimentally varied temporal perspective and outcome certainty ([1]). Their findings showed that treating an outcome as certain changed the length and type of explanations more clearly than merely placing it in the past or future ([1]). Gary Klein translated this mechanism into the project pre-mortem: after a plan is prepared but before it is finalized, participants assume the plan has failed and independently generate reasons for that failure ([2]). The assumed failure licenses concrete causal explanation and gives dissenters a legitimate role in the planning process ([2]).

The post-mortem has parallel roots in military after-action review, organizational debriefing, and project retrospectives. U.S. Army doctrine defines an after-action review as guided analysis during or after an event with the objective of improving future performance; its agenda compares what was supposed to happen, what happened, what was right or wrong, and how to perform better next time ([8]). Army Research Institute work traces the after-action review as a feedback process for collective training and emphasizes experiential learning: observation and conceptualization create value only when they are followed by another opportunity to experiment ([9]). In project settings, Thomke and Sinofsky described a formal postmortem process used to help firms learn from completed projects, including software work ([13]). These traditions use different names and settings, but each treats review as a bridge from experience to the next decision rather than as a ceremonial report.

The paired method belongs in probabilistic thinking because both halves operate on distributions rather than deterministic stories. Kahneman and Lovallo showed that organizational forecasts become overly optimistic when decision makers adopt an inside view anchored on plans and scenarios while neglecting the statistics of comparable cases ([11]). A well-designed pre-mortem counteracts that tendency by forcing several failure paths into view, but imagination alone does not supply their frequencies. It must be paired with reference-class evidence. A well-designed post-mortem then asks whether the original probability assignments were reasonable given information available at the time, not whether the modal prediction happened. The author's synthesis is that the pair is strongest when a pre-mortem produces dated, testable forecasts and a post-mortem evaluates those forecasts against both the realized path and an outside-view baseline ([3] [4] [10] [11]).

This scope differs from adjacent practices. Scenario planning constructs several internally consistent external futures and tests strategies across them; a pre-mortem begins with a specific decision and an assumed failure, then searches for causal routes to that failure. A personal decision journal preserves one decision maker's beliefs and emotions across time; an organizational post-mortem reconstructs a shared event, tests system assumptions, and assigns changes. Conventional risk registers list hazards before action, but a pre-mortem uses prospective certainty and independent explanation to reveal risks that a normal critique may suppress. Retrospective blame assignment asks who erred; a learning post-mortem asks which conditions, signals, controls, and decision rules made the observed path possible ([2] [8] [12]).

## Core Concepts

### The Pre-Mortem Creates Falsifiable Expectations Before Commitment

A useful pre-mortem starts after a concrete plan exists but before commitment becomes difficult to reverse. The facilitator states a precise future failure such as, "It is twelve months from now; the launch missed its adoption target and exceeded its loss limit." Participants first work independently and write plausible causes before group discussion. Klein's method uses the assumed failure to make reservations discussable and to reduce the pressure created by a team already invested in its plan ([2]). Independent generation matters because immediate discussion can anchor the group on the first explanation, allow hierarchy to suppress weak signals, and convert the exercise into defense of the existing plan. Those mechanisms are the author's synthesis from the method's stated purpose of legitimizing dissent, not a claim that independence eliminates group bias ([2]).

The author's synthesis is that the output should not stop at a list of worries. Each material failure mode needs an observable mechanism: initiating condition, transmission path, consequence, and an early indicator. "Customers may dislike it" is not testable. "If onboarding takes more than ten minutes, trial completion may fall below the base-rate range for comparable launches; weekly completion data will reveal the divergence" contains a mechanism, comparison, threshold, and monitoring signal. The distinction converts imagination into a provisional causal model. It also prevents risk workshops from ending with broad categories that sound comprehensive but cannot change a decision.

Reference classes should enter before the group revises probabilities. Kahneman and Lovallo found that decision makers naturally privilege details of the focal case and neglect distributions from comparable cases, producing bold forecasts ([11]). The pre-mortem should therefore record the relevant class, its outcome distribution, the reason for selecting it, and any adjustment from its base rate. The failure narrative then identifies case-specific evidence that could justify an adjustment rather than replacing the base rate. This sequence preserves the outside view as an anchor while allowing genuine differences in the focal case to matter ([11]).

A pre-mortem is not complete until failure modes affect the plan. The team can classify each mechanism by estimated probability, consequence, detectability, and controllability; choose prevention or mitigation; assign an owner; and define a trigger that forces reconsideration. These quantities are judgments, not measured facts, so false precision should be avoided. Ranges and conditional statements are often more honest than single-point estimates. The author's synthesis is that a failure mode deserves immediate action when it could cross a ruin boundary, when an inexpensive control can materially reduce exposure, or when the decision is hard to reverse. Low-impact or uncontrollable risks may instead be monitored. This converts the exercise from pessimistic brainstorming into decision design.

The author's synthesis is that the pre-mortem record should preserve at least six objects: the decision and success criterion; the horizon; a distribution over material outcomes; the selected reference class; the assumptions and failure modes that could move the distribution; and the controls, indicators, owners, and update rules. These objects establish what the team believed while uncertainty was still live. They also define the evidence a later post-mortem will need. Without the initial distribution and assumptions, retrospective review can describe events but cannot evaluate forecast quality.

### The Post-Mortem Reconstructs Evidence Before Explaining It

The first task after execution is factual reconstruction, not causal storytelling. Army doctrine begins by comparing what was supposed to happen with what actually happened and bases discussion on performance standards ([8]). Google's site reliability practice similarly defines a postmortem as a written record of an incident, its impact, mitigation or resolution, contributing causes, and follow-up actions ([12]). A decision post-mortem should therefore assemble the preserved plan, dated forecasts and updates, event timeline, decisions made during execution, indicators observed, controls activated, and final outcomes. Facts, estimates, and interpretations should remain visibly separate.

The sequence matters because hindsight makes the realized path feel more inevitable and more foreseeable than it was ([3] [5]). A timeline reconstructed from contemporaneous records is less vulnerable than one rebuilt from memory. The review should compare each decision with the information set available at that moment, not with later evidence. A missed warning signal is different from a signal that did not yet exist. A control that failed is different from a control no reasonable decision maker could have specified. This temporal discipline protects the review from imposing ex post knowledge on ex ante choices.

Causal analysis should preserve alternatives. A single event rarely identifies a single cause, because many conditions co-occur and the counterfactual world without one condition is unobserved. The review can distinguish proximate triggers, enabling conditions, latent system weaknesses, and external shocks, then state confidence in each causal link. Roese and Vohs found that hindsight narrows attention toward one causal understanding, whereas considering alternative explanations can reduce the bias ([5]). The author's synthesis is that every major causal claim should therefore be paired with at least one plausible rival explanation and a statement of what evidence would discriminate between them. A post-mortem is an inference document, not an autopsy that mechanically reveals certainty.

A blameless posture is an epistemic control, not an exemption from accountability. Google's guidance says a blameless review assumes people acted with good intentions and with the information available, then identifies contributing causes and concrete improvements; it warns that shaming discourages people from exposing issues ([12]). Army doctrine likewise emphasizes candid discussion focused on standards and future performance rather than judging success or failure ([8]). Blamelessness should not erase deliberate misconduct, repeated refusal to follow known controls, or ownership of corrective actions. It should prevent the review from substituting a person's name for an explanation of incentives, interfaces, workload, information, and safeguards.

### Process Error, Forecast Error, and Outcome Noise Must Be Separated

A post-mortem can classify discrepancies into three analytically different categories. A process error occurred when the decision procedure failed its own standard: a relevant base rate was ignored, an assumption was not tested, a trigger was observed but not acted on, or an available control was omitted. A forecast error occurred when stated probabilities were poorly aligned with repeated outcomes or when a model systematically missed a class of events. Outcome noise is residual variation that can produce a surprising result even when process and probabilities were reasonable. Baron and Hershey's experiments show why the categories matter: favorable outcomes can inflate evaluations of weak decisions, while unfavorable outcomes can depress evaluations of sound ones ([4]).

One realized event cannot by itself establish calibration. If a team assigns a 20 percent probability to failure and failure occurs, the forecast is not thereby wrong; events assigned 20 percent should occur about one time in five over a suitable reference set. Brier's probability score evaluates binary forecasts from the squared distance between the probability and the realized outcome and is designed for repeated probability forecasts ([10]). Across comparable forecasts, average scores can measure overall probability error, while calibration tables stratified by forecast probability can test whether events forecast at 20 percent occur at approximately that rate. A post-mortem may score an individual forecast, but it should not infer forecaster skill from one score.

The same rule applies to success. Ellis and Davidi found that soldiers reviewing both successful and failed navigation experiences improved more than those reviewing failed events alone ([7]). A success review can ask which expected mechanisms worked, which controls were unnecessary, which risks were avoided by design, and which benefits came from luck. Reviewing only failures enriches the causal model of failure while leaving the causes of success underspecified; reviewing both allows decision rules to preserve strengths as well as repair weaknesses ([7]).

The author's synthesis is a four-cell audit. Sound process plus favorable outcome supports cautious replication. Sound process plus unfavorable outcome calls for checking whether the event lay within the stated distribution before changing the rule. Weak process plus favorable outcome is dangerous because luck may reinforce a defective method. Weak process plus unfavorable outcome requires correction, but the correction should target the process defect rather than merely avoiding the exact observed result. This classification operationalizes the distinction between decision quality and outcome quality demonstrated by outcome-bias research ([4]).

### The Pair Forms a Closed Learning Loop

The author's synthesis is that the pre-mortem and post-mortem become more valuable when they share the same data structure. Each pre-mortem assumption should have an identifier, prior probability or confidence range, leading indicator, threshold, control, owner, and review date. The post-mortem should report what evidence arrived for that assumption, whether the indicator fired, whether the control worked, and what posterior judgment or rule follows. This linkage prevents generic lessons such as "communicate better" because every change must point to a tested or newly discovered mechanism.

The loop closes only when a lesson changes a future artifact. Army research treats after-action review as one phase of experiential learning whose benefit appears when the learner actively experiments again ([9]). Google requires follow-up actions and broad sharing so that incident knowledge can alter systems beyond the originating team ([12]). The author's synthesis is that a post-mortem lesson should produce one or more of five outputs: a revised base rate, a changed forecast model, a new or modified control, a monitoring trigger, or a decision rule specifying when to stop, scale, hedge, or seek more information. A statement that produces none of these is an observation, not yet a learned rule.

The next pre-mortem should begin with prior post-mortems from the same reference class. This reverses the common pattern in which reviews are archived but not consulted. Repeated use gradually produces an organizational dataset linking forecast ranges, failure mechanisms, indicators, controls, and outcomes. Proper scoring can evaluate probabilities across comparable decisions, while qualitative comparison can reveal recurring mechanisms that are too rare for stable frequency estimates ([10]). The result is neither purely statistical nor purely narrative: base rates constrain stories, and causal records explain why a case may depart from the base rate.

### Boundaries With Scenario Planning and Decision Journals

The author's synthesis is that scenario planning and pre-mortems both imagine alternatives, but their unit of analysis differs. Scenario planning asks how a strategy performs across several plausible external worlds. A pre-mortem assumes one defined adverse outcome for one plan and asks which causal paths could have produced it. The techniques can be sequenced: scenarios define materially different environments, then a pre-mortem tests how the chosen strategy fails within each important environment. They should not be merged into an unbounded list of possible futures, because the pre-mortem gains force from a concrete failure criterion and horizon.

The author's synthesis is that decision journals and the paired method also complement rather than duplicate each other. A journal preserves the decision maker's ex ante belief and is especially useful for personal calibration. A pre-mortem is a prospective team intervention that diversifies failure hypotheses before commitment. A post-mortem is a shared causal and operational review that reconstructs execution and modifies organizational controls. The journal can provide evidence to the post-mortem, but a private record cannot replace timelines, system data, participant perspectives, or assigned corrective actions.

## Evidence

### Prospective Hindsight Changes the Search for Explanations

Mitchell, Russo, and Pennington conducted two experiments on prospective hindsight, manipulating whether subjects treated an event as future or past and whether its occurrence was certain or uncertain ([1]). Their abstract reports that temporal perspective had little effect in the first experiment, while outcome certainty changed explanations: explanations for sure events tended to be longer, contain more episodic reasons, and use past tense. The second experiment supported the interpretation that uncertainty influenced the type of explanation rather than merely time spent explaining ([1]). This is evidence that an assumed-certain outcome can restructure causal search, the mechanism used by a pre-mortem.

Klein reported that the earlier research increased the ability to identify reasons for future outcomes by 30 percent and used prospective hindsight to create the project pre-mortem ([2]). His HBR description supplies a practical protocol and field examples in which hidden constraints surfaced before commitment ([2]). However, the 30 percent figure should not be interpreted as a measured 30 percent increase in project success. Mitchell and colleagues studied explanation generation, not completed projects, and their abstract emphasizes outcome certainty more than temporal direction ([1]). Direct controlled evidence that project pre-mortems reduce failure rates remains limited. The defensible claim is narrower: the technique changes and often broadens the search for plausible causes before an outcome occurs.

Kahneman and Lovallo provide convergent theory rather than a direct pre-mortem trial. Their analysis attributes overly optimistic forecasts to inside-view reasoning anchored on the focal plan and recommends a broader statistical perspective on comparable cases ([11]). A pre-mortem can expose case-specific failure mechanisms, while the outside view supplies frequencies that imagination cannot provide. The combined procedure has a stronger theoretical basis than either tool alone, but its combined effect should still be tested rather than assumed.

### Debriefs and After-Event Reviews Improve Later Performance

The evidence for structured retrospective review is broader. Tannenbaum and Cerasoli conducted a quantitative meta-analysis of 46 samples involving 2,136 participants across team and individual debriefs ([6]). They reported an average effect of d = 0.67, approximately a 25 percent improvement over control conditions, with similar average effects across teams and individuals, simulated and real settings, and medical and nonmedical samples ([6]). They also found indications that alignment among participants, review focus, intended outcome, and the level of performance measurement strengthens results; facilitation and structure may matter as well ([6]). This supports debriefing as a performance intervention, not merely a documentation habit.

Ellis and Davidi supplied more specific quasi-field evidence with soldiers performing successive navigation exercises ([7]). Participants who reviewed both successful and failed events after each training day improved significantly more than participants who reviewed failures only. Before the intervention, mental models for failed events contained more constructs and links than mental models for successful events; the difference narrowed as balanced review continued ([7]). The study supports two design rules for post-mortems: examine successful performance as well as breakdowns, and use review to enrich causal models rather than merely record errors.

Army adoption provides primary evidence about implementation but should not be confused with a randomized estimate of effect. Current doctrine specifies a guided, candid review based on standards, facts, self-discovery, and concrete improvement for future training ([8]). Army Research Institute analysis documents the institutional and research foundations of the after-action review and situates it in a cycle of experience, observation, conceptualization, and renewed action ([9]). The evidence establishes that a large organization can routinize frequent review and connect findings to subsequent practice. It does not prove that every meeting labeled an after-action review is effective; quality depends on preparation, evidence, facilitation, candor, and follow-through ([8] [9]).

### Hindsight and Outcome Bias Explain Why Records and Process Criteria Matter

Fischhoff's 1975 experiments included 479 college students and tested judgments with and without outcome knowledge ([3]). Knowing the reported outcome increased its judged prior likelihood and changed the perceived relevance of facts. Participants remained largely unaware of the distortion and overestimated what they or others could have known without the outcome ([3]). The result directly supports preserving forecasts and reasons before execution. A post-mortem cannot reliably recreate the ex ante state from unaided memory.

Baron and Hershey tested outcome bias in five studies using medical decisions and monetary gambles ([4]). Participants judged the quality of reasoning, competence of the decision maker, or willingness to delegate more favorably after good outcomes than after bad ones, despite knowing that the decision maker faced uncertainty and despite recognizing that outcome should not determine process quality ([4]). Roese and Vohs's later review explained how memory, perceived inevitability, perceived foreseeability, and motivated sensemaking reinforce the effect; it also identified consideration of alternative causal explanations as one partial corrective ([5]). Together, these studies justify separate process and outcome ledgers, rival causal hypotheses, and contemporaneous records.

### Evidence Does Not Eliminate the Identification Problem

The post-mortem evidence has boundaries. Tannenbaum and Cerasoli synthesized debriefs across training and work settings, not only high-stakes strategic decisions or project post-mortems ([6]). Ellis and Davidi studied repeated navigation tasks with relatively fast feedback, a setting more learnable than a unique acquisition, policy reform, or multi-year investment ([7]). Google's postmortem system and the HBS project note offer rich practice models, but their published descriptions do not isolate the causal effect of the review from organizational selection, expertise, or concurrent engineering changes ([12] [13]).

Rare events pose a second limitation. A single post-mortem cannot estimate a stable base rate, prove a counterfactual, or distinguish an improbable draw from a misspecified probability model. Brier scoring becomes informative across a set of comparable probability forecasts, not through narrative inspection of one surprise ([10]). For unique events, the review should preserve uncertainty, compare multiple reference classes, and mark causal conclusions by confidence. The method improves the quality of learning; it does not turn one history into a controlled experiment.

The evidence therefore supports a graded conclusion. Structured retrospective debriefs have substantial average evidence of performance benefit, especially when aligned and connected to later practice ([6] [7]). Hindsight and outcome-bias research strongly supports contemporaneous records and process-based evaluation ([3] [4] [5]). Prospective hindsight has experimental support as a way of changing explanation generation, but claims that pre-mortems directly prevent project failure exceed the available evidence ([1] [2]). The strongest implementation pairs the two methods, measures forecasts across repeated decisions, and treats causal lessons as testable updates rather than final truths.

## Implications

### For Strategic and Capital-Allocation Decisions

Executives can use the paired method as a gate around consequential, difficult-to-reverse commitments. Before approval, the pre-mortem should state the success criterion, horizon, reference-class distribution, key probabilities, ruin boundaries, failure mechanisms, indicators, and controls. Approval should record which residual risks are accepted and what evidence would trigger delay, scaling, hedging, or abandonment. After the evidence horizon, the post-mortem should compare the original record with the realized path, score probability forecasts where possible, and classify differences as process error, forecast error, or outcome noise. The author's synthesis is that this design protects capital allocation from both plan-based optimism and outcome-based rewriting ([4] [10] [11]).

The method is especially useful when a favorable early outcome could reinforce a fragile process. An acquisition may close smoothly because financing conditions remain benign even though integration assumptions were never tested. A product may exceed its first-quarter target because of a temporary channel effect rather than durable demand. The post-mortem should ask whether the mechanism that management forecast actually produced the outcome and whether the result would survive under the original reference class. This prevents a lucky success from becoming an unjustified increase in confidence, the favorable-outcome form of the bias observed by Baron and Hershey ([4]).

For repeated investments, forecasts should be stored in comparable form. Probabilities assigned to revenue ranges, schedule completion, covenant breach, or permanent capital loss can be evaluated over a portfolio of decisions with a Brier score or calibration table ([10]). A review should not reward a manager merely because a 60 percent thesis worked, nor punish one solely because a 20 percent hazard occurred. It should ask whether the probabilities, evidence, sizing, and safeguards were reasonable before the draw. This is the probabilistic standard that turns post-mortems from performance theater into forecast learning.

### For Forecasting and Research Teams

Forecasting teams can treat each pre-mortem mechanism as a candidate model misspecification. Before publishing a forecast, the team assumes the forecast fails materially and generates omitted variables, regime changes, data defects, incentives, and reference-class errors. Each mechanism is linked to an indicator and a possible update. The exercise should follow, not replace, an outside-view baseline; otherwise vivid failure stories may receive more weight than their frequencies justify ([1] [11]).

After resolution, the team should review calibration, resolution, and reasoning separately. The Brier score supplies a proper evaluation for binary probabilities, but an aggregate score cannot explain why the forecast missed ([10]). The post-mortem supplies the causal audit: Was the prior wrong? Did evidence arrive but receive too little weight? Did the event definition drift? Was the outcome correctly forecast but poorly acted upon? The author's synthesis is that statistical scoring tells the team whether performance changed, while causal review proposes why and specifies the next test. Neither should substitute for the other.

The author's synthesis is that research programs with slow or sparse feedback should aggregate by mechanism rather than waiting for many identical decisions. For example, several projects may share an assumption about adoption friction even if their products differ. Reviews can track whether that assumption repeatedly fails, while remaining explicit that heterogeneous cases weaken frequency estimates. This approach preserves learning without inventing a false sample size. It also makes the next pre-mortem sharper because prior lessons enter as named hypotheses instead of generic organizational memory.

### For Project, Engineering, and Reliability Work

Project teams can integrate the pre-mortem with planning and the post-mortem with delivery. The pre-mortem should occur when design is concrete enough to expose interfaces but before contracts, budgets, or public commitments eliminate options. The post-mortem should occur soon enough that records and participants remain available, while allowing sufficient evidence to distinguish temporary noise from final performance. Army doctrine and Google's SRE practice both emphasize structured evidence, candid participation, and changes aimed at future performance ([8] [12]).

For incidents, the pair creates a direct control loop. A launch pre-mortem might identify overload, dependency failure, alert blindness, and rollback friction, then assign thresholds and mitigations. If an incident occurs, the post-mortem compares those expectations with telemetry and the event timeline. An anticipated failure with an ignored trigger is a process problem. An anticipated failure with a control that proved inadequate is a design-learning problem. An unanticipated mechanism expands the failure library. A control that worked should also be preserved, consistent with evidence that reviewing successes and failures improves learning more than reviewing failures alone ([7]).

Blamelessness is operationally important because hidden information is the raw material of the review. Google's practice focuses on contributing causes, impact, mitigation, and owned follow-up rather than indicting individuals; the stated rationale is that fear suppresses reporting ([12]). The author's synthesis is that accountability should attach to completing actions and maintaining standards, while causal analysis should examine why the action seemed reasonable in context. This allows a team to be exacting about safeguards without treating punishment as explanation.

A post-mortem repository becomes useful only when retrieval is part of the next plan. Teams should index reviews by decision type, failure mechanism, signal, control, and outcome, then require relevant prior reviews in pre-mortem preparation. Thomke and Sinofsky's project-learning model and Google's sharing practice both treat the artifact as organizational knowledge rather than a private meeting record ([12] [13]). The repository should record superseded lessons and failed corrective actions so that institutional memory does not become a list of untested maxims.

### For Governance, Policy, and High-Stakes Institutions

Boards, regulators, and public agencies often evaluate rare decisions under intense hindsight. Outcome knowledge can make an adverse event appear obvious and a favorable result appear deserved, even when the ex ante evidence was ambiguous ([3] [4]). Governance can reduce this distortion by requiring a contemporaneous decision record, range forecasts, alternative explanations, and explicit review criteria before action. The post-mortem can then judge whether procedures, evidence standards, and risk limits were followed without pretending that one outcome proves the original probability wrong.

The author's synthesis is that this distinction supports fairer accountability. A sound process with an unlucky outcome may still reveal a control worth adding, but it should not automatically be treated as negligence. A weak process with a lucky outcome should not receive automatic validation. Deliberate misconduct and ignored mandatory controls remain accountable acts; the method does not excuse them. It prevents institutions from confusing punishment with causal learning and from teaching participants to hide uncertainty.

Public policy also requires attention to counterfactuals. A policy outcome reflects the chosen intervention, external conditions, implementation quality, and the unobserved path that would have occurred without the policy. A post-mortem cannot observe that missing world directly. It can compare the original causal model with outcome measures, relevant controls or reference classes, and rival explanations, then state what remains unidentified. The author's synthesis is that explicit uncertainty strengthens legitimacy: a review that labels inference limits is more useful than one that manufactures certainty after the fact.

### A Minimal Operating Protocol

The author's synthesis from the evidence is a twelve-step protocol. First, define the decision, horizon, success and failure criteria. Second, record the outside-view distribution and current probabilities. Third, assume a specific failure and generate causes independently. Fourth, map material causes to mechanisms, indicators, thresholds, controls, and owners. Fifth, revise the plan and probabilities, preserving the original record. Sixth, specify the review date and required evidence. Seventh, during execution, append dated updates without overwriting earlier beliefs. Eighth, reconstruct the factual timeline after the outcome. Ninth, compare expected and actual signals, actions, and outcomes. Tenth, separate process errors, forecast errors, and noise while considering rival causes. Eleventh, score comparable forecasts in aggregate and review successes as well as failures. Twelfth, convert supported lessons into revised base rates, controls, triggers, or decision rules and verify their use in the next pre-mortem ([6] [7] [8] [9] [10] [12]).

The author's synthesis is that the protocol should be proportionate. A reversible, low-cost decision may require a ten-minute pre-mortem and brief review. An irreversible capital commitment or safety-critical change requires a documented baseline, independent facilitation, objective evidence, and tracked actions. The governing question is not whether every decision deserves ceremony, but whether the expected learning and avoided downside exceed the cost of the review. The paired method is most valuable when uncertainty is material, feedback is otherwise easy to distort, and future decisions can still change.

The final implication is epistemic humility. Pre-mortems do not enumerate every future, and post-mortems do not reveal a single true cause. Their contribution is narrower and more durable: they preserve what was believed, expand the set of considered failure paths, compare claims with evidence, and carry qualified lessons into the next decision. Repetition turns isolated outcomes into a growing reference class, while explicit uncertainty prevents that reference class from becoming another deterministic story ([1] [3] [5] [10]).

## Sources

1. Mitchell, D. J., Russo, J. E., & Pennington, N. (1989). "Back to the
   Future: Temporal Perspective in the Explanation of Events." Journal of
   Behavioral Decision Making, 2(1), 25-38.
   https://doi.org/10.1002/bdm.3960020103 [high]

2. Klein, G. (2007). "Performing a Project Premortem." Harvard Business
   Review, 85(9), 18-19.
   https://hbr.org/2007/09/performing-a-project-premortem [high]

3. Fischhoff, B. (1975). "Hindsight Is Not Equal to Foresight: The Effect
   of Outcome Knowledge on Judgment Under Uncertainty." Journal of
   Experimental Psychology: Human Perception and Performance, 1(3),
   288-299. https://doi.org/10.1037/0096-1523.1.3.288 [high]

4. Baron, J., & Hershey, J. C. (1988). "Outcome Bias in Decision
   Evaluation." Journal of Personality and Social Psychology, 54(4),
   569-579. https://doi.org/10.1037/0022-3514.54.4.569 [high]

5. Roese, N. J., & Vohs, K. D. (2012). "Hindsight Bias." Perspectives on
   Psychological Science, 7(5), 411-426.
   https://doi.org/10.1177/1745691612454303 [high]

6. Tannenbaum, S. I., & Cerasoli, C. P. (2013). "Do Team and Individual
   Debriefs Enhance Performance? A Meta-Analysis." Human Factors, 55(1),
   231-245. https://doi.org/10.1177/0018720812448394 [high]

7. Ellis, S., & Davidi, I. (2005). "After-Event Reviews: Drawing Lessons
   From Successful and Failed Experience." Journal of Applied Psychology,
   90(5), 857-871. https://doi.org/10.1037/0021-9010.90.5.857 [high]

8. Headquarters, Department of the Army. (2021). "After Action Reviews."
   Field Manual 7-0, Appendix K.
   https://www.first.army.mil/Portals/102/FM%207-0%20Appendix%20K.pdf [high]

9. Morrison, J. E., & Meliza, L. L. (1999). "Foundations of the After
   Action Review Process." U.S. Army Research Institute for the Behavioral
   and Social Sciences, Special Report 42.
   https://apps.dtic.mil/sti/tr/pdf/ADA368651.pdf [high]

10. Brier, G. W. (1950). "Verification of Forecasts Expressed in Terms of
    Probability." Monthly Weather Review, 78(1), 1-3.
    https://doi.org/10.1175/1520-0493(1950)078%3C0001:VOFEIT%3E2.0.CO;2
    [high]

11. Kahneman, D., & Lovallo, D. (1993). "Timid Choices and Bold Forecasts:
    A Cognitive Perspective on Risk Taking." Management Science, 39(1),
    17-31. https://doi.org/10.1287/mnsc.39.1.17 [high]

12. Beyer, B., Jones, C., Petoff, J., & Murphy, N. R. (eds.). (2016).
    "Postmortem Culture: Learning from Failure." Site Reliability
    Engineering. O'Reilly Media and Google.
    https://sre.google/sre-book/postmortem-culture/ [high]

13. Thomke, S. H., & Sinofsky, S. (1999). "Learning from Projects: Note on
    Conducting a Postmortem Analysis." Harvard Business School Background
    Note 600-021.
    https://www.hbs.edu/faculty/Pages/item.aspx?num=26475 [high]

## See Also

- `library/probabilistic-thinking-forecasting/inside-outside-view.md` --
  reference-class forecasting supplies the base rates that pre-mortem
  narratives cannot generate by imagination alone.
- `library/probabilistic-thinking-forecasting/scenario-planning-and-analysis.md` --
  scenario planning tests strategy across external futures, a distinct but
  complementary use of prospective simulation.
- `library/probabilistic-thinking-forecasting/calibration-and-overconfidence.md` --
  calibration provides the standard for evaluating repeated probability
  judgments without confusing confidence with accuracy.
- `library/self-improvement/decision-journals.md` -- decision journals
  preserve an individual's ex ante reasoning and can supply evidence to a
  later organizational post-mortem.
