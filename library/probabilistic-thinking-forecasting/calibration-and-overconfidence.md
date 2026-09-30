---
name: calibration-and-overconfidence
id: 20260730T113117Z
tier: library-topic
domain: probabilistic-thinking-forecasting
author: Researcher-1
tags: [calibration, overconfidence, dunning-kruger, tetlock, metacognition, confidence-intervals, brier-score]
links: [library/probabilistic-thinking-forecasting/superforecasting.md, library/probabilistic-thinking-forecasting/bayesian-reasoning.md, library/probabilistic-thinking-forecasting/inside-outside-view.md, library/psychology-behavior/cognitive-biases.md]
reviewed: 2026-09-30
---

# Calibration and Overconfidence -- Confidence Becomes Useful Only When It Is Scored Across Comparable Cases

Calibration asks whether stated probabilities match observed frequencies across a defined set of comparable forecasts. It is not the same as confidence, accuracy, discrimination, sharpness, or a low aggregate score, and a single outcome cannot establish it [1][5][13]. Overconfidence is likewise not one universal tendency: overestimation, overplacement, and overprecision are distinct and can move in different directions across tasks [7].

## Background

Probability language becomes testable only when a forecast is connected to a later observation. A claim that an event has a 70 percent chance cannot be judged from one resolution: occurrence and nonoccurrence are both compatible with the claim. Calibration instead concerns a series. Among sufficiently comparable cases assigned about 70 percent, a calibrated forecasting process should see the event occur about 70 percent of the time. Lichtenstein and Fischhoff formalized this frequency-matching definition for subjective judgments and separated it from resolution, the ability to assign meaningfully different probabilities to cases with different outcome frequencies [1]. Modern reliability-diagram research uses the same definition for probabilistic classifiers [13].

The formal scoring tradition came from weather forecasting. Brier proposed a quadratic probability score in 1950 for mutually exclusive and exhaustive weather outcomes [3]. Murphy later partitioned the probability score into terms associated with uncertainty, reliability, and resolution, making clear that one mean error can arise from different combinations of environment and forecast behavior [4]. Proper-scoring-rule theory generalized the incentive principle: a strictly proper rule makes an assessor's believed distribution the unique report that optimizes expected score, under the rule's assumptions [5]. Properness disciplines reporting; it does not prove that the underlying belief is well informed, that the question is useful, or that the resulting forecast has decision value [5].

The psychology of confidence developed beside this measurement work. Lichtenstein and Fischhoff's 1977 experiments examined confidence in answers to knowledge and recognition tasks. Their abstract reports moderate overall calibration, systematic biases that varied with item difficulty, and overconfidence as the most common bias in those tasks; it also distinguished calibration from resolution [1]. Their later training experiments used repeated probability assessments and comprehensive feedback. Performance improved substantially, much of the change followed the first feedback, and transfer was modest to some related tasks and absent on two others [2]. Those findings support the possibility of learned calibration under feedback, but not the stronger claim that one generic exercise transfers to every domain.

The word overconfidence accumulated several incompatible meanings. Moore and Healy separated three: overestimation of one's absolute performance, overplacement of oneself relative to others, and overprecision in the width or concentration of one's beliefs [7]. In their experiment, 82 participants completed repeated easy, medium, and hard trivia quizzes and reported probability distributions for their own and another participant's scores. Participants underestimated absolute performance on easy quizzes, overestimated it on hard quizzes, overplaced themselves on easy quizzes, and underplaced themselves on hard quizzes; their distributions nevertheless showed overprecision [7]. A statement that "people are overconfident" is therefore incomplete unless it names the target, comparator, elicitation method, task, and form of error.

Forecasting tournaments moved calibration from short laboratory tasks into repeated geopolitical questions. The Good Judgment Project used explicit probabilities, defined resolutions, repeated updating, and Brier scores. The original tournament analysis reported that probability training, team collaboration, and tracking high performers improved calibration and resolution [10]. A follow-up selected top performers into elite teams and found that their accuracy, calibration, and resolution advantages persisted over later tournament years, while also warning that selection, cognitive ability, motivation, updating effort, and enriched environments were entangled [11]. A later item-response reanalysis reported that controlling extraneous method variation substantially reduced, eliminated, or sometimes reversed estimated training and teaming effects on latent forecasting ability [12]. The responsible conclusion is narrower than the original topic: structured forecasting systems can produce measurable improvements, but causal attribution to any single ingredient remains contested.

The Dunning-Kruger literature provides a second warning against slogans. Kruger and Dunning's four studies found that bottom-quartile participants on humor, grammar, and logic tasks substantially overestimated their percentile standing; in one logical-reasoning study, participants at the 12th percentile estimated their test performance at the 62nd percentile [8]. The authors proposed a "dual burden" in which weak task skill also impaired recognition of error. A preregistered 2022 study used separate baseline and test blocks, trial-level confidence, signal-detection measures, and path analysis. It reproduced the familiar negative relation between skill and global estimation error, but found no lower metacognitive efficiency among poor performers, found that poor performers were less rather than more confident, and attributed the pattern mainly to performance and regression effects rather than to the proposed dual burden [9]. The classic result and its mechanism must therefore be reported separately.

Calibration is best understood as a measurement contract. The forecaster must state a probability before resolution; the event, horizon, information cutoff, and outcome rule must be fixed; and evaluation must preserve the full eligible set rather than memorable wins or losses. The evaluator then needs enough comparable cases to estimate conditional frequencies, a declared scoring convention, and uncertainty around the diagnostics. Without those elements, "well calibrated" is a reputation claim rather than an empirical result [5][13].

## Core Concepts

### Calibration is conditional frequency agreement

For binary events, let `p` be the issued probability and `o` the later outcome, coded 1 if the event occurs and 0 otherwise. Calibration asks whether the conditional event frequency agrees with the issued probability: cases assigned near `p` should resolve positively at a frequency near `p`. A reliability diagram displays observed event frequency against forecast probability; perfect calibration lies on the diagonal [1][13]. The claim belongs to a forecasting process on a case set, not to one isolated forecast.

Grouping matters. Forecasts may be discrete, such as a platform restricted to multiples of 5 percent, or nearly continuous, with most values unique. Classical reliability diagrams group values into bins, but the number and boundaries of those bins can change the apparent curve. Dimitriadis, Gneiting, and Jordan demonstrated that diagrams using 9, 10, and 11 equally spaced bins could look substantially different on the same forecast data. They developed the CORP method to automate monotone binning and add consistency or confidence bands [13]. The general lesson does not require adopting one estimator: publish the grouping method, sample sizes, and uncertainty, and do not treat an unstable visual deviation as a discovered psychological bias.

Calibration can also be assessed at different levels. Calibration-in-the-large asks whether the average forecast matches the overall event rate. Local or conditional calibration asks whether observed frequencies track issued probabilities across the scale or relevant subgroups. A forecaster may look calibrated in aggregate while failing within horizons, topics, or regimes. Conversely, a small subgroup can appear miscalibrated through sampling noise. The author's synthesis is that any calibration statement should name the forecast set, period, probability range, grouping or smoothing rule, and dependence assumptions [5][6][13].

### Calibration does not equal resolution, discrimination, or sharpness

A process that always predicts the unconditional base rate can be calibrated while contributing little case-specific information. Resolution asks whether the forecast sorts cases into groups with different outcome frequencies. Discrimination asks whether forecast values separate events from nonevents. Sharpness describes the concentration of predictive distributions without using outcomes and is desirable only subject to calibration [4][6]. These properties answer different questions.

Consider a balanced set in which half the events occur. A constant 50 percent forecast is calibrated at the aggregate level and has no resolution. A second forecaster may issue values near 20 and 80 percent that reliably separate cases; if the corresponding outcome frequencies match, that forecaster has both calibration and resolution. A third may issue the same sharp values without frequency agreement and be overconfident. Evaluating only the calibration diagonal rewards the first process for caution while ignoring that it does not distinguish cases. Evaluating only extremity rewards the third for unsupported confidence. Proper scores and decompositions help keep the properties separate [4][5][13].

For continuous outcomes, calibration also has multiple definitions. Gneiting, Balabdaoui, and Raftery distinguished probabilistic, exceedance, and marginal calibration and proposed the principle of maximizing sharpness subject to calibration [6]. A predictive interval can obtain high coverage by being extremely wide, just as a binary forecaster can remain near the base rate. Informative uncertainty requires both empirical consistency and useful concentration.

### The Brier score measures overall probability error

Under the common event-only convention for a binary forecast, the Brier loss is:

`BS = (p - o)^2`

A 70 percent forecast scores 0.09 if the event occurs and 0.49 if it does not; lower is better. Averaging across resolved forecasts produces a mean loss between 0 and 1 under this convention [3][5]. Brier's original multicategory form sums the squared errors for every mutually exclusive outcome. For a two-outcome event, that full-vector convention is twice the event-only value and ranges from 0 to 2. Published scores are not comparable until the outcome representation, scale, weighting, and orientation are stated [3][5].

A constant 50 percent binary forecast has event-only loss 0.25 on every case, but 0.25 is not a universal benchmark. If the event rate is 10 percent, a constant forecast equal to that base rate has expected loss 0.09. Skill must therefore be assessed against an appropriate reference forecast on the same cases, not against a context-free number. The reference may be an unconditional base rate, a conditional climatology, a simple model, or an existing operational forecast; the choice changes the claim [4][5].

The Brier score is strictly proper for the stated binary probability, but it combines several properties. In the lower-is-better convention, Murphy's familiar decomposition can be written conceptually as:

`Brier loss = uncertainty - resolution + reliability penalty`

Uncertainty reflects outcome variability in the evaluated set. Resolution rewards useful separation among cases. Reliability penalizes mismatch between forecast probabilities and observed frequencies [4]. Empirical estimates depend on grouping, weighting, and sample size; modern decompositions such as CORP address some instability, but do not remove the need to disclose the evaluation design [13][15]. A lower score can result from better calibration, better resolution, an easier question set, different participation, or different time weighting [10][15].

### Proper scoring does not make a forecast true

A strictly proper score makes honest reporting optimal in expectation for the forecaster's own belief [5]. That incentive property is narrower than epistemic quality. A person can report a sincere but poorly modeled probability, omit a live outcome, use a biased reference class, or forecast a badly defined event. The score can evaluate only the distribution and outcome supplied to it. It cannot repair a vague resolution rule or infer whether the research process was competent.

Scores also do not directly measure decision value. An action depends on probabilities plus consequences, costs, constraints, thresholds, and reversibility. Two forecast systems can have similar average Brier loss but differ near the probability threshold that triggers evacuation, investment, treatment, or inspection. Conversely, a statistically improved score may leave every action unchanged. The author's synthesis is to evaluate probability quality with a proper score and diagnostics, then evaluate decisions with an explicit consequence model; neither layer should substitute for the other [5].

### Overconfidence has three distinct targets

Overestimation concerns an absolute quantity: predicted performance minus actual performance. Overplacement concerns relative standing: believed rank minus actual rank. Overprecision concerns excessive concentration: intervals, probability distributions, or confidence judgments that are narrower or more extreme than the evidence warrants [7]. The distinction prevents several errors.

First, overestimation and overplacement can reverse with task difficulty. Moore and Healy found underestimation paired with overplacement on easy tasks and overestimation paired with underplacement on hard tasks [7]. Second, confidence in one selected answer can combine overestimation and overprecision, so the elicitation method may not distinguish mechanisms. Third, a majority can be above an arithmetic average in a skewed distribution, although a majority cannot be above the median; "better than average" claims must identify the comparator [7]. Fourth, justified high confidence is not overconfidence. The empirical question is whether confidence exceeds the accuracy or precision warranted by a defined benchmark.

### Calibration and metacognition are related but not identical

Calibration is an external relation between forecasts and outcomes. Metacognition concerns information about one's own cognitive processing. A person may have trial-level sensitivity to which answers are likely correct yet give poor global estimates of total performance; conversely, a lucky global estimate need not demonstrate trial-level insight [9]. This distinction matters when interpreting the Dunning-Kruger pattern.

Kruger and Dunning's original studies supplied evidence for large global self-estimation errors among low performers and for improvement after brief logic training [8]. McIntosh and colleagues later separated metacognitive sensitivity, metacognitive efficiency, and confidence bias. Their poor performers had lower metacognitive sensitivity because their first-order information was weaker, but not lower efficiency after accounting for available information. Their path models attributed the familiar relation between low skill and high estimation error mainly to performance scores and noisy global estimates [9]. This does not prove that low competence is never paired with unjustified confidence. It shows that quartile plots and global self-ratings do not, by themselves, identify a dual-burden mechanism.

### Training is a feedback system, not a motivational slogan

Calibration training requires resolvable questions, explicit probabilities, outcome feedback, and repeated comparison. Lichtenstein and Fischhoff's intensive experiments found substantial learning but limited transfer [2]. The Good Judgment Project combined probability training with teams, repeated updates, score feedback, selection, and aggregation; its original analysis found improvements in calibration and resolution [10]. Because these interventions and participant characteristics interacted, the later superforecaster study described high performers as partly discovered and partly created rather than as products of one drill [11]. The 2025 reanalysis further cautions that Brier-score improvements need not map cleanly to a latent ability effect once method variance is modeled [12].

The author's synthesis is that feedback can improve measured performance on structured tasks and that some forecasting systems have sustained high calibration and resolution. Transfer across domains, persistence without continued feedback, and the causal contribution of each component require separate evidence. A prediction log without resolution is an archive; score feedback without comparable cases can reward noise; and confident use of more decimal places is not training unless the distinctions improve out-of-sample forecasts [2][10][11].

## Evidence

### Early calibration experiments established the measurement problem

Lichtenstein and Fischhoff asked participants to answer tasks and attach probabilities to their judgments. Their 1977 paper defined perfect calibration as equality between an assigned probability and the true proportion among propositions receiving that probability. It separately defined resolution as successful discrimination among degrees of certainty. Across their experiments, participants were moderately calibrated, but the most common systematic direction was overconfidence, and calibration changed with item difficulty [1]. The method and findings reject two claims in the original topic: there is no source-supported universal ratio such as "90 percent confidence means 50 percent accuracy," and miscalibration is not invariant across tasks.

Their 1980 training paper tested whether feedback could improve probability assessment. One experiment used 11 sessions of 200 assessments followed by comprehensive feedback; a second reduced training to three sessions. Considerable learning occurred, much of it after the first feedback, but generalization was modest to some related tasks and absent on two others [2]. This is direct evidence that calibration behavior can change. It is also direct evidence against promising automatic, domain-general transfer from one training format.

### Overconfidence taxonomy explains apparently contradictory results

Moore and Healy reviewed the literature and then measured overestimation, overplacement, and overprecision within one repeated-task experiment. Eighty-two participants completed 18 ten-item trivia quizzes covering six topics, with easy, medium, and hard versions. Participants reported full probability distributions for their own score and for a randomly selected earlier participant's score [7]. This design allowed the three constructs to be observed separately rather than inferred from different studies.

Absolute estimates were regressive toward expected performance: participants underestimated easy-quiz scores by 0.22 points on average, were approximately accurate on medium quizzes, and overestimated hard-quiz scores by 0.79 points. Relative judgments moved oppositely: participants overplaced themselves on easy quizzes and underplaced themselves on hard quizzes. Their nominal 90.5 percent score intervals contained the realized score 73.1 percent of the time, showing overprecision under that elicitation [7]. The result supports a conditional claim: task difficulty and the information structure can reverse overestimation and overplacement even while overprecision remains.

### Forecasting tournaments show improvement and attribution limits

The Good Judgment Project evaluated geopolitical probabilities under defined resolutions and repeated updates. The 2014 tournament paper reports that probability training, collaborative teams, and tracking top performers improved both calibration and resolution [10]. The 2015 superforecaster study selected 60 top performers into elite teams after Year 1 and compared their later performance with high-performing regular-team members and other forecasters. The selected group retained better standardized Brier scores, calibration, resolution, and discrimination in Years 2 and 3 [11].

The same paper states important limits. Selection was based on earlier accuracy; superforecasters differed in cognitive measures, political knowledge, effort, update frequency, information use, and team environment; and the elite-team comparison was not a pure experimental estimate of team assignment [11]. Hauenstein and colleagues later reanalyzed the first two tournament years with item-response models. Their abstract reports that extraneous method variables substantially reduced, removed, or sometimes reversed estimated training and teaming effects on latent ability [12]. The combined evidence supports measured forecasting-system performance and persistent individual differences. It does not isolate a universal training effect or prove that ordinary forecasters become superforecasters through one component.

### Dunning-Kruger findings do not settle their own mechanism

Kruger and Dunning ran four studies involving humor, logic, and grammar. Bottom-quartile participants substantially overestimated their performance; the frequently cited 12th-versus-62nd percentile result came from one logical-reasoning study with 45 undergraduates, 11 in the bottom quartile [8]. A later experiment in the paper randomly gave 70 of 140 participants brief logic training. Among the initially lowest performers, training improved monitoring of correct and incorrect answers and reduced self-estimation error [8]. These studies established a pattern and supplied evidence consistent with a metacognitive explanation.

McIntosh and colleagues preregistered a more direct test with 151 valid participants. They used separate baseline trials to measure skill, test trials to measure performance, trial-level confidence ratings, signal-detection measures of metacognitive sensitivity and efficiency, and global relative and absolute self-estimates [9]. The familiar negative relation between skill and estimation error reappeared. However, poorer performers were less confident, not more; metacognitive efficiency was not lower; and performance-only path models fit better than models assigning the pattern to metacognitive variables. The authors concluded that their data refuted the dual-burden account for this task and were compatible with noisy, regressive self-estimates plus general optimism or pessimism [9]. The broader evidence is contested, so neither the original mechanism nor the later refutation should be generalized beyond their designs without qualification.

### Calibration diagrams require statistical discipline

Dimitriadis, Gneiting, and Jordan studied reliability diagrams for binary probability forecasts. They showed that traditional bin-and-count plots could change sharply under small changes in bin number, with associated calibration measures inheriting the instability. Their CORP method used isotonic regression to select bins automatically, supplied uncertainty bands, and yielded an exact score decomposition under stated conditions [13]. The paper's practical contribution is not that every evaluator must use CORP. It demonstrates that visual calibration judgments are estimates with design choices and sampling uncertainty, not direct pictures of a forecaster's internal honesty or skill.

Together these studies replace the original topic's dramatic generalizations with bounded findings. Miscalibration occurs, feedback can improve it, selected forecasters can sustain strong measured performance, and self-estimation can be seriously wrong. Yet magnitudes, directions, transfer, and mechanisms depend on the task, elicitation, case set, scoring convention, comparison group, and statistical method [1][2][7][9][10][11][12][13].

## Implications

### For an individual forecaster

The author's synthesis from the scoring, training, and reliability-diagram evidence is a prospective calibration protocol [2][5][10][13]:

1. Define the event before forecasting. State mutually exclusive outcomes, the resolution date, the authoritative outcome source, and rules for ambiguity or cancellation.
2. Record one probability distribution and timestamp. For a binary event, record `p` for the event and preserve the information cutoff.
3. Preserve every eligible forecast. Do not select only memorable successes, extreme calls, or cases that resolved quickly.
4. Resolve under the original rule. Keep pending, annulled, and disputed cases separate from scored cases.
5. Declare the score convention. For Brier loss, state whether the event-only or full-vector form is used, which forecast version is scored, and how cases and time are weighted.
6. Inspect more than one diagnostic. Report mean proper score, a baseline on the same cases, calibration with uncertainty, and resolution or discrimination.
7. Stratify only with enough data and predeclared reasons. Horizon, topic, and probability range may expose local failures, but small cells should be labeled uncertain rather than turned into reputations.
8. Change one practice at a time when possible. If question design, research access, team process, updating cadence, and aggregation all change together, the system may improve without revealing which component caused it.

A single failed 90 percent forecast is not proof of overconfidence; such events should occur about one time in ten under calibration. A single success at 10 percent is not proof of foresight. The learning unit is a defined series, and the review question is whether probability groups match frequencies while still separating cases. This discipline prevents outcome knowledge from converting every surprise into a story that the original forecast was irrational [1][13].

Calibration practice should also distinguish belief revision from score management. A forecaster should update when new evidence arrives, but preserve the earlier version and timestamp. Scoring only the final forecast measures near-resolution accuracy; scoring every day gives longer-lived questions more weight; scoring fixed horizons measures a different ability. None is automatically correct. The evaluation policy must follow the use case and be fixed before seeing outcomes [5][10][15].

### For organizations

Organizations should design a forecasting system rather than exhort employees to "be less confident." The system needs resolvable questions, protected dissent, independent initial estimates, a declared aggregation rule, feedback, and records that survive staff turnover. Training can teach probability language and reference-class use, but the evidence does not justify treating one workshop as permanent or domain-general calibration [2][10][12]. Periodic evaluation should test transfer on the organization's actual question types.

Incentives require care. A strictly proper scoring rule aligns expected score with honest belief when rewards follow the score, but surrounding promotion, winner-take-all prizes, or blame can create different objectives [5][14]. If managers punish every low-probability event that occurs, forecasters will avoid honest tail probabilities. If they reward only bold correct calls, participants can gain status through selective extremity. The author's synthesis is to reward complete records, clear resolution contracts, justified updates, and long-run scoring rather than rhetorical certainty or individual anecdotes [5][14].

Calibration reports should identify their unit of analysis. An individual forecast, team median, statistical aggregate, question-selection process, and complete research platform are different objects. The Good Judgment evidence shows that selection, motivation, updating, teamwork, and aggregation can coexist [10][11]; the later reanalysis shows why measured score improvements should not automatically be relabeled as latent individual ability [12]. Governance should attribute performance only to components tested by an appropriate comparison.

### For investors and capital allocators

The author's synthesis is to use calibration for bounded thesis variables rather than for the vague question "Was the investment right?" A purchase decision combines business quality, valuation, financing, downside, opportunity cost, portfolio construction, and time horizon. These can be separated into resolvable forecasts: revenue retention above a stated threshold, debt refinancing by a date, normalized margin within a range, or a named thesis break. Each forecast should preserve its source data, base rate, probability, update triggers, and resolution rule. Market price alone cannot identify which component of the original analysis was sound.

A calibration record is most informative when definitions are stable across cases. Ten heterogeneous investments do not support a precise personal 10 percent bin, and a manager can appear calibrated by staying near broad base rates without identifying exceptional businesses. Review should therefore pair frequency agreement with resolution: did higher-conviction cases actually resolve more favorably than lower-conviction cases under the same definitions? The Brier score can summarize probability error, but comparisons require the same horizons, case eligibility, and benchmark [4][5][13][15].

Decision value remains separate. The author's synthesis is that a 30 percent probability of permanent capital loss may dominate a 70 percent probability of gain if the loss is ruinous, while a 30 percent chance of a small reversible setback may be acceptable. Position size and margin of safety require payoffs and downside constraints, not calibration alone. Calibration improves one input to capital allocation; it does not replace valuation, incentives, balance-sheet analysis, or judgment about irreversibility.

### For education and professional expertise

Feedback should be tied to the exact skill being trained. The early calibration experiments found learning with limited transfer [2]. The original Dunning-Kruger training result improved recognition after participants learned relevant logical rules [8], while the later registered report challenged the general claim that poor performers possess inferior metacognitive efficiency [9]. A defensible educational design asks learners to predict performance before a test, records item-level confidence, returns outcome feedback, and checks whether gains persist on new material. It does not label low performers as constitutionally blind to their errors.

Experts also need bounded claims. High confidence may be warranted in stable environments with repeated, timely feedback; low confidence may reflect difficult questions rather than virtue. Credentials alone do not establish calibration, and calibration in one domain does not transfer automatically to another [1][2]. Professional evaluation should compare forecasts with outcomes inside a defined domain and should report both successful discrimination and failures.

### Common failure modes and stopping rule

The first failure is retrospective reconstruction: assigning a probability after learning the result. The second is an undefined event that can be reworded at resolution. The third is selective inclusion of dramatic cases. The fourth is comparing Brier scores computed under different conventions or case weights. The fifth is reading a smooth calibration curve from sparse bins without uncertainty. The sixth is treating calibration as the whole of forecast quality. The seventh is treating any self-estimation error as proof of a specific cognitive mechanism. Each failure breaks a different part of the measurement contract [5][9][13].

The author's stopping rule is that evaluation is adequate when an independent reviewer can reproduce the eligible cases, forecast versions, outcomes, formula, weights, baseline, calibration diagnostic, uncertainty, and resolution measure. If those elements are unavailable, another decimal place does not create evidence. The correct conclusion is "not yet measurable," not "well calibrated" or "overconfident."

## Sources

1. Lichtenstein, S., & Fischhoff, B. (1977). "Do Those Who Know More Also
   Know More About How Much They Know?" Organizational Behavior and
   Human Performance, 20(2), 159-183.
   https://doi.org/10.1016/0030-5073(77)90001-0 [high]

2. Lichtenstein, S., & Fischhoff, B. (1980). "Training for Calibration."
   Organizational Behavior and Human Performance, 26(2), 149-171.
   https://doi.org/10.1016/0030-5073(80)90052-5 [high]

3. Brier, G. W. (1950). "Verification of Forecasts Expressed in Terms of
   Probability." Monthly Weather Review, 78(1), 1-3.
   https://doi.org/10.1175/1520-0493(1950)078%3C0001:VOFEIT%3E2.0.CO;2
   [high]

4. Murphy, A. H. (1973). "A New Vector Partition of the Probability
   Score." Journal of Applied Meteorology, 12(4), 595-600.
   https://doi.org/10.1175/1520-0450(1973)012%3C0595:ANVPOT%3E2.0.CO;2
   [high]

5. Gneiting, T., & Raftery, A. E. (2007). "Strictly Proper Scoring Rules,
   Prediction, and Estimation." Journal of the American Statistical
   Association, 102(477), 359-378.
   https://doi.org/10.1198/016214506000001437 [high]

6. Gneiting, T., Balabdaoui, F., & Raftery, A. E. (2007).
   "Probabilistic Forecasts, Calibration and Sharpness." Journal of the
   Royal Statistical Society: Series B, 69(2), 243-268.
   https://doi.org/10.1111/j.1467-9868.2007.00587.x [high]

7. Moore, D. A., & Healy, P. J. (2008). "The Trouble With
   Overconfidence." Psychological Review, 115(2), 502-517.
   https://doi.org/10.1037/0033-295X.115.2.502 [high]

8. Kruger, J., & Dunning, D. (1999). "Unskilled and Unaware of It: How
   Difficulties in Recognizing One's Own Incompetence Lead to Inflated
   Self-Assessments." Journal of Personality and Social Psychology,
   77(6), 1121-1134. https://doi.org/10.1037/0022-3514.77.6.1121 [high]

9. McIntosh, R. D., Moore, A. B., Liu, Y., & Della Sala, S. (2022).
   "Skill and Self-Knowledge: Empirical Refutation of the Dual-Burden
   Account of the Dunning-Kruger Effect." Royal Society Open Science,
   9(12), 191727. https://doi.org/10.1098/rsos.191727 [high]

10. Mellers, B., Ungar, L., Baron, J., et al. (2014). "Psychological
    Strategies for Winning a Geopolitical Forecasting Tournament."
    Psychological Science, 25(5), 1106-1115.
    https://doi.org/10.1177/0956797614524255 [high]

11. Mellers, B., Stone, E., Murray, T., et al. (2015). "Identifying and
    Cultivating Superforecasters as a Method of Improving Probabilistic
    Predictions." Perspectives on Psychological Science, 10(3), 267-281.
    https://doi.org/10.1177/1745691615577794 [high]

12. Hauenstein, C. E., Thomas, R. P., Illingworth, D. A., & Dougherty,
    M. R. (2025). "Rethinking the Role of Teams and Training in
    Geopolitical Forecasting: The Effect of Uncontrolled Method Variance
    on Statistical Conclusions." Psychological Science, 36(1), 3-18.
    https://doi.org/10.1177/09567976241266481 [high]

13. Dimitriadis, T., Gneiting, T., & Jordan, A. I. (2021). "Stable
    Reliability Diagrams for Probabilistic Classifiers." Proceedings of
    the National Academy of Sciences, 118(8), e2016191118.
    https://doi.org/10.1073/pnas.2016191118 [high]

14. Witkowski, J., Freeman, R., Vaughan, J., Pennock, D., & Krause, A.
    (2018). "Incentive-Compatible Forecasting Competitions."
    Proceedings of the AAAI Conference on Artificial Intelligence, 32(1).
    https://doi.org/10.1609/aaai.v32i1.11471 [high]

15. Merkle, E. C., & Hartman, R. (2018). "Weighted Brier Score
    Decompositions for Topically Heterogenous Forecasting Tournaments."
    Judgment and Decision Making, 13(2), 185-201.
    https://doi.org/10.1017/S1930297500007099 [high]

## See Also

- `library/probabilistic-thinking-forecasting/superforecasting.md` --
  the tournament setting in which calibration, resolution, updating, and
  forecaster selection are evaluated together.
- `library/probabilistic-thinking-forecasting/forecast-evaluation-and-scoring-rules.md`
  -- the wider framework for scoring conventions, baselines, weighting,
  uncertainty, and decision value.
- `library/probabilistic-thinking-forecasting/bayesian-reasoning.md` --
  the formal framework for updating probabilities within a stated model.
- `library/probabilistic-thinking-forecasting/inside-outside-view.md` --
  reference-class reasoning as an input to probability judgment.
- `library/psychology-behavior/overconfidence.md` -- the broader psychology
  of overestimation, overplacement, and overprecision.
