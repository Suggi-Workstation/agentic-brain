---
name: forecast-evaluation-and-scoring-rules
id: 20260930T103428Z
tier: library-topic
domain: probabilistic-thinking-forecasting
author: Librarian
tags: [forecast-evaluation, proper-scoring-rules, brier-score, logarithmic-score, ranked-probability-score, calibration, forecast-skill]
links: [library/probabilistic-thinking-forecasting/forecast-question-design.md, library/probabilistic-thinking-forecasting/calibration-and-overconfidence.md, library/probabilistic-thinking-forecasting/superforecasting.md, library/probabilistic-thinking-forecasting/communicating-forecast-uncertainty.md, library/probabilistic-thinking-forecasting/prediction-markets.md, library/self-improvement/decision-journals.md]
---

# Forecast Scores Measure Defined Forecasting Systems, Not Vague Predictive Reputation

A forecast score converts a stated probability distribution and a resolved outcome into evidence only when the target, scoring rule, baseline, cases, timestamps, and aggregation policy are fixed in advance. Proper scores discourage vagueness and strategic probability reports, but no single score can by itself establish calibration, discrimination, decision value, or the skill of a person, model, team, or complete forecasting system.[2][4][7][13]

## Background

Forecast evaluation arose from a practical problem: a forecast can be plausible in language yet impossible to compare with reality. A prediction such as "conditions may deteriorate" does not specify an event, probability, horizon, or resolution rule. Even an explicit probability remains hard to judge from one outcome. An event assigned 20 percent probability sometimes occurs, and an event assigned 80 percent probability sometimes does not. The European Centre for Medium-Range Weather Forecasts therefore states that an individual probabilistic forecast cannot ordinarily be classified as right or wrong, except at probabilities of zero or one; verification requires a sample of forecasts.[13] The object of evaluation is a repeated relationship between issued distributions and realized outcomes, not a collection of memorable successes.

Glenn Brier supplied an early formal answer in 1950. For mutually exclusive and exhaustive weather categories, his probability score summed squared differences between forecast probabilities and outcome indicators. The score gave zero to a perfect forecast and penalized probability placed away from the realized category.[1] In the common modern binary event-only convention, the Brier loss is `(p - o)^2`, where `p` is the stated event probability and `o` is 1 if the event occurs and 0 otherwise. This version ranges from zero to one. Brier's original two-category sum counts both event and non-event components and is twice the event-only value, so its binary range is zero to two.[1][2] Published Brier scores are not comparable until the convention and orientation are known.

The general theory developed around proper scoring rules. A scoring rule is proper when a forecaster minimizes expected loss, or maximizes expected reward, by reporting the probability distribution that represents the forecaster's belief. It is strictly proper when that optimum is unique.[2] Properness addresses an incentive problem: if the evaluation rule rewards a distorted report, observed probabilities no longer provide clean evidence about belief or skill. It does not certify that the belief is informed, that the question is useful, or that a competition pays prizes in an incentive-compatible way.[2][11]

The field also separated overall accuracy from diagnostic qualities. Murphy's decomposition of the Brier score divided mean loss into uncertainty, reliability, and resolution.[3] In a lower-is-better convention, the relationship is commonly written `score = uncertainty - resolution + reliability`. Uncertainty reflects the outcome variability in the evaluated set. Reliability, often called calibration, penalizes disagreement between issued probabilities and observed frequencies. Resolution rewards sorting cases into groups with meaningfully different outcome rates.[3] The same total score can therefore arise from different strengths and failures, which is why a scalar ranking should be accompanied by decomposition and diagnostic plots.

Continuous and ordered outcomes required other tools. Epstein introduced the ranked probability score for ordered categories so that probability assigned near the observed category would be treated differently from probability assigned far away.[5] Later work developed the continuous ranked probability score and quantile or interval scores for full predictive distributions and reported ranges.[2][6] These rules extended the same discipline beyond binary questions: the forecast object must match the score. A binary event probability, unordered category vector, ordered-category distribution, full continuous distribution, quantile, and interval are different claims and should not be evaluated as though they were interchangeable.[2][5][6]

Forecasting tournaments made these distinctions operational. The Good Judgment Project evaluated large numbers of geopolitical probability forecasts, permitted updating while questions remained open, and used Brier scores to compare performance. The project also had to address different question choices, durations, teams, and aggregation methods.[7][8] Merkle and Hartman showed why these design details matter: averaging all daily observations in one step gives more influence to questions that remain open longer, whereas averaging within each question and then across questions gives each question equal weight.[7] Neither policy is neutral. Each defines a different estimand.

Modern evaluation now covers human forecasters, numerical models, prediction markets, ensembles, and end-to-end AI systems. ForecastBench, for example, uses unresolved future questions to limit answer leakage and later compares systems on resolved outcomes; its updated methodology addresses unequal question sets and difficulty.[12] The same numerical score can refer to an individual's reports, a team's median, an aggregation algorithm, a base model, a research agent, or a full platform. A meaningful result must name that unit. Otherwise a strong aggregate may be misattributed to its members, or a strong model may be confused with a system that benefited from better question selection, data access, updating, and post-processing.

The historical lesson is that scoring is measurement design, not arithmetic applied after the fact. The question defines what can resolve. The timestamp defines what information was available. The scoring rule defines which probability errors matter. The baseline defines what counts as skill. The aggregation policy defines which cases dominate. The uncertainty analysis defines how much evidence the sample supplies. If any of these elements is chosen after outcomes are visible, the score can reward selective reporting while retaining the appearance of objectivity.[7][9][10][12]

## Core Concepts

### Define the forecast object and score orientation

Every evaluation begins with a forecast object. For a binary event, the object is one probability for a proposition with a fixed resolution rule. For `K` unordered outcomes, it is a probability vector whose entries sum to one. For ordered categories, order is part of the claim. For a continuous quantity, the object may be a density, cumulative distribution, set of quantiles, or collection of central intervals. Proper scoring rules target these objects differently.[2][5][6]

Score orientation must also be declared. Statistical theory often defines a score as a reward, so larger values are better. Operational systems often report a loss, so smaller values are better. This topic uses lower-is-better losses. Multiplying a proper loss by a positive constant preserves its incentive property but changes every reported number.[2] A result such as "Brier score 0.18" is incomplete without the formula, scale, outcome type, weighting, and case set.

The author's synthesis is to publish the exact equation with every leaderboard or study. This prevents three avoidable errors: comparing the original multicategory Brier scale with the binary event-only scale; comparing a reward with a loss; and comparing normalized and unnormalized forms of ranked or interval scores. Labels are not definitions.

### Brier loss rewards useful probability movement, not certainty alone

For a binary event, the event-only Brier loss is:

`BS(p,o) = (p - o)^2`

A forecast of 0.70 incurs loss 0.09 when the event occurs and 0.49 when it does not. Extreme errors receive larger penalties than moderate errors because the difference is squared. Across a sample, mean Brier loss is strictly proper for the binary probability under the standard assumptions.[1][2]

For multiple unordered categories, the quadratic form sums squared differences across the full probability vector. This preserves the idea that probability mass assigned to unrealized categories is costly, but it does not use any distance or ranking among those categories.[1][2] If categories are ordered, treating a one-category miss and a far-tail miss as equivalent can conceal important structure. That is the motivation for the ranked probability score.[5]

The Brier score is bounded and readily decomposed, which makes it useful for diagnosis and communication. Its boundedness also means that an impossible forecast on the realized outcome has a finite penalty. That is not always desirable: a system that repeatedly assigns exact zero to events that occur has made a qualitatively severe probability claim. The logarithmic loss treats that failure more harshly.[2]

### Logarithmic loss is local and strongly punishes excluded outcomes

For a discrete forecast with realized category `y`, logarithmic loss is:

`LogL(p,y) = -log p_y`

Only the probability assigned to the realized category enters the realized loss. The logarithmic rule is strictly proper for the full categorical distribution, and its continuous analogue evaluates the predictive density at the realized value.[2] If a forecaster assigns zero probability to the outcome that occurs, the loss is infinite. Very small realized-outcome probabilities receive large penalties.

This sensitivity makes logarithmic loss useful when excluding a possible outcome should be treated as a severe error. It also makes operational safeguards consequential. Capping, truncating, or adding an arbitrary probability floor changes the rule; Bracher and colleagues note that truncating logarithmic scores can destroy propriety.[6] A platform that needs finite scores should define its probability floor before forecasts are submitted and report the resulting rule rather than calling it unmodified log loss.

Brier and logarithmic losses can rank systems differently because they encode different error sensitivity. The Brier loss spreads attention across squared probability errors, while logarithmic loss reacts sharply to probability near zero on what occurs.[2] There is no score-free answer to which ranking is correct. The score should be selected before outcomes, justified by the forecast object and evaluation purpose, and supplemented by diagnostics showing where systems differ.

### Ranked probability scores respect ordered outcomes

For ordered categories, define cumulative forecast probabilities `F_k` through each threshold and cumulative outcome indicators `O_k`. A common ranked probability loss is:

`RPS = sum from k=1 to K-1 of (F_k - O_k)^2`

The score accumulates binary Brier losses across ordered thresholds. Probability assigned close to the realized category produces a smaller cumulative discrepancy than probability assigned far away. For two categories, RPS reduces to the binary Brier form under a matching normalization.[5]

The category order, included thresholds, and normalization must be reported. Some implementations sum the `K-1` nontrivial thresholds, some include a final zero term, and some divide by `K-1`. These choices can preserve rankings while changing numerical values. RPS is inappropriate for nominal outcomes with no defensible order. Imposing an order for convenience makes the score encode a distance structure that the forecast did not claim.[2][5]

The continuous ranked probability score extends the threshold idea to a continuous cumulative distribution. It integrates squared differences between the forecast cumulative distribution and the step function at the observation. CRPS is strictly proper on distributions with a finite first moment and has the same physical unit as the observation in its lower-is-better form.[2] It is less dominated by one density value than logarithmic loss and can be interpreted through threshold-specific Brier losses, but that does not make it universally superior. It rewards a different aspect of the predictive distribution.[2][4]

### Quantile and interval scores evaluate reported ranges

A central prediction interval communicates lower and upper quantiles rather than a full distribution. Its evaluation must reward narrowness when the interval covers while penalizing misses below and above. For a central interval with nominal miscoverage `alpha`, lower endpoint `l`, upper endpoint `u`, and outcome `y`, the interval score is:

`IS_alpha(l,u;y) = (u-l) + (2/alpha)(l-y) if y<l + (2/alpha)(y-u) if y>u`

The width term rewards sharp intervals, and the miss terms penalize underprediction and overprediction in proportion to distance.[2][6] A very wide interval can attain high empirical coverage while conveying little information; a very narrow interval can look decisive while missing too often. A proper interval score evaluates both properties together.

The weighted interval score combines a point forecast and several central intervals. Bracher and colleagues developed its operational interpretation for epidemic forecasts and showed that it is a proper approximation to CRPS when forecasts are supplied as quantiles rather than full distributions.[6] It can be decomposed into dispersion, underprediction, and overprediction contributions. A finite quantile grid is proper for the reported quantiles but does not uniquely identify every possible full distribution.[2][6]

Interval scoring must not be confused with checking coverage alone. Coverage asks how often outcomes fall inside intervals. It does not reward narrower intervals among systems with adequate coverage, and a system can manipulate it by issuing nearly unbounded ranges. Proper interval scores make vagueness costly without rewarding unjustified precision.[2][4][6]

### Properness aligns a report with belief, not belief with truth

Strict propriety creates an expected-score incentive to report the believed distribution honestly.[2] It does not make that distribution accurate. A forecaster can sincerely use a poor model, omit decisive evidence, or apply the wrong reference class. Proper scoring evaluates the report against outcomes over cases; it cannot infer why the probability was wrong.

Properness also depends on the payment or ranking mechanism. Witkowski and colleagues show that proper scores incentivize truthful reports when forecasters are rewarded according to their scores, but a single prize for the highest realized score can reward strategic extremity.[11] The probability of winning a noisy rank competition is not the same objective as expected score. A tournament must therefore test the incentive mechanism separately from the propriety of the underlying scoring rule.

Transformations can introduce another failure. A skill score expresses performance relative to a reference. For a lower-is-better loss with optimum zero, a common form is `1 - L_forecast/L_reference`. A value of one is perfect, zero matches the reference, and a negative value is worse. Gneiting and Raftery warn that ratio-form skill scores can be improper when the reference is estimated from the same evaluation sample, even if the underlying rule is proper.[2] Skill scores are useful descriptive comparisons, not automatically safe elicitation mechanisms.

### Calibration, resolution, discrimination, and sharpness are distinct

Calibration asks whether probabilities agree with observed frequencies over comparable forecasts. Among cases assigned about 70 percent, roughly 70 percent should resolve positively in a calibrated binary system. Calibration is a joint property of forecasts and outcomes.[4] It requires grouping, smoothing, or model-based estimation, each with sampling uncertainty.

Resolution asks whether forecast-conditioned groups have different outcome frequencies. A constant base-rate forecast can be calibrated but have no resolution. Discrimination reverses the conditioning question: do forecast values differ between events and non-events? Measures such as receiver operating characteristic summaries address that distinction. Sharpness describes how concentrated or extreme the forecasts are without using outcomes.[4][13] Sharpness is valuable only subject to calibration; unsupported confidence is not skill.

Murphy's Brier decomposition makes the trade-off visible. In a lower-is-better convention, reliability is a penalty, resolution is a benefit, and uncertainty is fixed by the outcome distribution in the evaluated set.[3] Decomposition estimates can depend on probability bins, weights, and sample size. They explain a score only under the stated procedure; they do not replace the raw cases or uncertainty intervals.

A calibration diagram alone is also insufficient. A system that always reports the base rate can lie on the calibration diagonal while adding no information. A probability integral transform histogram for continuous forecasts can look uniform even when individual forecast distributions are deficient; Gneiting, Balabdaoui, and Raftery show that calibration diagnostics and proper scores must be interpreted together.[4] The evaluation should report overall score, reliability, resolution or discrimination, sharpness, and uncertainty rather than use one favorable diagnostic as a substitute for the others.

### Baselines turn accuracy into skill only when comparisons are homogeneous

An absolute score says how forecasts compared with outcomes. A skill score says whether they improved on a declared alternative. Plausible references include unconditional climatology, seasonal or conditional climatology, persistence, a market price, a simple model, or the prior production system.[2][13][14] The baseline must be generated for the same cases, horizons, timestamps, and information set. NOAA's hurricane-verification guidance warns that non-homogeneous comparisons can produce incorrect rankings when models are available at different times or evaluated on different storms.[14]

Baseline choice changes the claim. Beating 50 percent on a rare event is weak evidence if the event rate is 2 percent. Beating unconditional climatology may still fail to beat seasonal climatology or persistence. A sophisticated system can have good absolute accuracy while adding no incremental value to information already available to users. The author's synthesis is to report at least one naive reference and the strongest operationally available reference, with both run prospectively on the same eligible cases.

### Time, case, and participant aggregation define the reported estimand

Forecasts are often updated. An evaluation must decide whether to score the first report, final report, every timestamp, a fixed set of lead times, or a time-weighted path. Scoring every day and then averaging all forecast-days gives more weight to long-lived questions. Averaging days within each question and then averaging questions gives equal weight to questions. Merkle and Hartman document the latter policy in geopolitical tournaments and explain why it prevents question duration from determining influence.[7]

Neither policy is universally correct. A warning system may need performance at fixed lead times. A trading system may care about the full path. A research question about initial judgment should use first forecasts. A question about updating should preserve versions and use a predeclared temporal weighting. The author's synthesis is to report a score surface by lead time when operational action changes with horizon, then state the scalar aggregation used for ranking.

Selective participation creates a separate problem. Forecasters may choose easier questions, enter only after informative news, or skip low-confidence cases. Mellers and colleagues standardized scores within questions because tournament participants selected questions.[8] Modern benchmarks use difficulty adjustment when systems answer overlapping but nonidentical sets.[12] Such adjustments depend on model assumptions and adequate overlap. The cleanest comparison remains a common, prospectively assigned case set.

Missing forecasts, unresolved outcomes, and disputed resolutions must not be collapsed into one category. A missing forecast is an absent report for a case that may later resolve. A pending question has no outcome yet. An annulled question is excluded because its measurement contract failed. A disputed resolution has not completed adjudication. Outcome-dependent proper scores cannot be computed for genuinely unresolved cases. Penalties or imputations for skipped questions affect participation incentives and must be predeclared, reported separately, and tested for sensitivity.[7][8][12]

### Rare events require prospective emphasis and uncertainty estimates

Rare events create low information per case. Bradley and colleagues show that a few hundred forecast-outcome pairs may be needed merely to establish positive skill for an infrequent event, and that dependence reduces effective sample size further.[9] A dramatic success or failure therefore supplies weak evidence about stable calibration on its own.

Selecting only realized extremes after observing outcomes creates the forecaster's dilemma. Lerch and colleagues show that conditioning evaluation on extreme observations can discredit skillful probabilistic forecasts and violate the assumptions of conventional evaluation.[10] The correct alternative is not to ignore rare consequences. It is to define the region of interest before outcomes and use a proper weighted score or decision analysis that retains the relevant non-extreme cases.[10]

Rare-event reports should include event counts, base rates, case construction, confidence intervals, and dependence handling. A score difference without these quantities can turn random variation into a reputation claim. Statistical uncertainty is part of the result, not a footnote.[9][10]

### Accuracy and decision value answer different questions

A proper score evaluates probability distributions. A decision uses probabilities together with actions, costs, benefits, constraints, and reversibility. ECMWF distinguishes accuracy, skill against a reference, and utility to a user.[13] Two forecasts can have similar average proper scores yet lead to different outcomes under an asymmetric loss function, and a small score improvement can be valuable near a critical action threshold.

The author's synthesis is to keep two layers. The first reports general probabilistic quality with a proper score and diagnostics. The second evaluates decisions with a predeclared utility or cost-loss model for the intended user. Replacing the proper score with realized profit or avoided loss can confound forecast quality with position size, prices, policy, and luck. Replacing utility with the proper score can reward statistically better probabilities that do not change any decision. Both layers are needed when the forecast exists to support action.

## Evidence

### Foundational scoring rules establish incentives and non-equivalent sensitivities

Brier's 1950 paper constructed a quadratic probability score for mutually exclusive and exhaustive weather categories and identified zero as perfect performance under its original orientation.[1] The method supplied a computable record for repeated probability forecasts rather than relying on verbal retrospective judgment. Its multicategory formulation also explains the enduring scale ambiguity: the original binary two-class sum is twice the common event-only squared error.[1][2]

Gneiting and Raftery's 2007 review developed the general proper-scoring framework on probability spaces and examined categorical quadratic, logarithmic, continuous ranked probability, quantile, interval, and skill scores.[2] Their method is mathematical: compare expected scores when the reported distribution equals or differs from the forecaster's believed distribution. The central finding is that strict propriety makes truthful reporting the unique optimum under the score. The same paper shows that proper rules are not interchangeable and warns that some skill-score transformations are generally improper.[2] This evidence supports using a declared proper rule, not the stronger claim that one rule supplies a universal ordering of all forecasting systems.

Epstein's 1969 paper addressed probability forecasts for ranked categories.[5] Its scoring construction made category order part of the evaluation, unlike an unordered quadratic score. The case established a durable design principle: the score must respect the geometry of the outcome space. A severity forecast with ordered levels and a forecast over unrelated political outcomes require different representations even when both contain several categories.[2][5]

### Decomposition shows why one average loss cannot diagnose performance

Murphy's 1973 analysis partitioned the probability score into uncertainty, reliability, and resolution.[3] The method takes a set of forecasts and outcomes and separates the outcome-set difficulty from disagreement between forecast probabilities and conditional event frequencies and from useful variation in those conditional frequencies. The finding is structural: a mean Brier score can improve through better reliability, better resolution, or a different mix of event uncertainty.[3]

Gneiting, Balabdaoui, and Raftery examined continuous probabilistic forecasts through calibration and sharpness.[4] They defined calibration as statistical consistency between predictive distributions and observations and sharpness as concentration of the forecasts alone. Their diagnostics include probability integral transform and marginal-calibration assessments, but their examples show that seemingly favorable calibration diagnostics are not sufficient for ideal forecasts.[4] The evidence supports a joint evaluation using diagnostics and proper scores, rather than accepting a calibration curve or sharp distribution as a complete quality measure.

### Forecasting tournaments reveal weighting and selection effects

Mellers and colleagues embedded randomized interventions in the Good Judgment Project's geopolitical forecasting tournament.[8] Forecasters supplied probabilities on questions that later closed, could update reports, and were evaluated with Brier scores. Training, teaming, and tracking improved forecast accuracy in the reported tournament, while statistical aggregation produced a separate system-level improvement.[8] The study also standardized scores within questions because participants chose which questions to answer. Its design demonstrates that a forecaster score is conditional on the question set, participation rule, update policy, and unit of analysis.

Merkle and Hartman analyzed weighted Brier decompositions for topically heterogeneous tournaments.[7] Their method first averaged daily Brier scores within each active question and then averaged across questions so that long-duration questions would not dominate. They also noted that their decompositions did not automatically solve missing data when forecasters chose different question sets or entry times.[7] The evidence establishes that temporal aggregation and missingness are design decisions. It does not establish one weighting policy as correct for every use.

### Interval forecasts can be evaluated without rewarding width alone

Bracher and colleagues studied epidemic forecasts reported as medians and central prediction intervals rather than full densities.[6] They developed the interpretation of weighted interval score as a proper approximation to CRPS and decomposed it into dispersion and penalties for underprediction and overprediction. The method lets evaluators score a finite set of reported quantiles while retaining an incentive to report those quantiles honestly.[6]

The paper also identifies a boundary. Logarithmic scores require full predictive distributions and are not directly available when a submission contains only selected intervals. Attempting to reconstruct an unsupported density or truncate log penalties changes the evaluation problem.[6] The practical finding is that forecast format should be specified before score choice; evaluators should not demand information the submitted object does not contain.

### Rare-event studies show why case selection and sample size matter

Bradley, Schwartz, and Hashino derived sampling uncertainty for the Brier score and Brier skill score and applied it to confidence intervals and hypothesis tests.[9] They found that the Brier score is an unbiased estimator of accuracy under their assumptions, whereas the climatology-referenced Brier skill score is biased in finite samples. Their examples show that infrequent events may require hundreds of forecast-outcome pairs to establish positive skill and that serial correlation reduces effective sample size.[9] A leaderboard difference without uncertainty can therefore exaggerate evidence, especially for repeated or rare events.

Lerch and colleagues analyzed the practice of evaluating only cases whose observed outcomes were extreme.[10] Through theoretical and applied analysis, they showed that outcome-conditioned subsets can produce undesirable rankings and conflict with established forecast-evaluation assumptions. They proposed proper weighted scoring rules as a prospective way to emphasize extremes.[10] This evidence rejects selective retrospective evaluation, not attention to rare events. The distinction is whether emphasis is defined before the outcome and preserves proper incentives.

### Modern benchmarks separate prospective questions from system rankings

ForecastBench evaluates machine-learning systems on dynamically generated questions about future events whose answers are unknown at submission time.[12] Its initial study compared expert forecasters, the public, and language-model systems on a random subset; its later methodology adjusted rankings for question difficulty when forecasters answered different sets.[12] The benchmark treats leakage prevention, question overlap, and difficulty estimation as parts of evaluation rather than preprocessing details.

The evidence also exposes model dependence. Difficulty adjustment requires enough direct or indirect overlap and assumptions about how ability varies across questions or domains.[12] A difficulty-adjusted score is useful when a common set is impossible, but it is not equivalent to random assignment. The stronger design remains prospective common cases, with adjustment used transparently when operational constraints prevent them.

### Incentive research separates score propriety from competition design

Witkowski and colleagues studied forecasting competitions that award a single prize.[11] Their mechanism-design analysis starts from a conflict: proper scores encourage truthfulness when participants receive score-based rewards, but winner-take-all ranking can encourage exaggerated reports that increase the chance of finishing first. They designed mechanisms intended to select accurate forecasters while retaining truthful incentives.[11]

This evidence matters because many evaluation systems are also reward systems. A statistically proper loss can become strategically improper through the surrounding payment, promotion, or publicity rule. Evaluators must test both the scoring equation and the institution that acts on it.[2][11]

## Implications

### For individual forecasters

A forecaster needs a prospective record, not a remembered hit rate. Each entry should preserve the exact question, probability or distribution, timestamp, information cutoff, resolution source, and update history. The evaluation should begin only after the stated resolution process completes.[7][8][12] Selectively presenting correct calls, ignoring unresolved questions, or scoring only the final revision destroys the evidence needed to distinguish initial judgment from updating skill.

The author's synthesis is to review a forecaster with four views. First, report a proper overall loss under a printed formula. Second, show calibration and resolution or discrimination, with case counts and uncertainty. Third, compare against declared base-rate and operational baselines on the same cases. Fourth, stratify by horizon, topic, and forecast extremity while preserving prospectively defined strata.[2][3][4][9] A single rank can summarize these results, but it should not replace them.

Small personal samples require restraint. Ten resolved forecasts cannot establish stable 10 percent probability calibration, and one spectacular rare-event call does not demonstrate repeatable skill.[9][13] The appropriate output may be an audit trail and a list of model failures rather than a numerical reputation. The worst personal practice is to increase reported precision because a scoring formula exists; the formula measures stated precision but does not create supporting evidence.

### For tournament and platform designers

The evaluation protocol should be part of the question contract. Before forecasts open, publish the score orientation and scale, eligibility window, update cadence, carry-forward rule, weighting unit, baseline, minimum participation, treatment of missing reports, resolution policy, dispute process, and uncertainty method.[7][8][11][12] Changes after outcomes begin to emerge can alter incentives and invalidate comparisons.

Question assignment is the cleanest control for difficulty and selection. If forecasters choose questions, the platform should preserve overlap, model question difficulty, and report sensitivity to missingness assumptions.[8][12] Late entry should not receive an accidental advantage over early forecasts unless the objective is explicitly final pre-resolution accuracy. A system can report first-forecast, fixed-horizon, and full-path scores separately rather than force distinct abilities into one number.

The platform should identify its unit of performance. Individual reports, team discussion, aggregation, post-processing, retrieval, and question selection can each add value.[8][12] An end-to-end score is legitimate when the deployed system includes all of them. It should not be presented as evidence that any one component has the same skill. Component ablations or matched comparisons are needed for attribution.

Competition incentives need separate review. If status or money depends on winning rather than on expected score, a proper rule alone may not preserve truthful reports.[11] The reversible design is to reward score-based performance across many cases, cap no losses after observing outcomes, and test strategic behavior before making the ranking consequential. Where a winner must be selected, use a mechanism whose incentive properties match that purpose rather than assuming a standard leaderboard is neutral.

### For model and AI-system evaluation

A model benchmark must be prospective. Questions should be unresolved when forecasts are submitted, and the information cutoff, tool access, model version, prompt or policy, and later outcome source should be retained.[12] Otherwise the evaluation can measure answer leakage, retrieval differences, or post-outcome knowledge rather than forecasting.

Models should be compared on homogeneous cases and information availability whenever possible.[14] If one system receives later data, more browsing, or easier questions, a lower score does not isolate forecasting quality. Difficulty adjustment can help with incomplete overlap, but its assumptions and connectivity requirements should be disclosed.[12] The author's synthesis is to pair any adjusted leaderboard with raw common-case comparisons and coverage statistics.

Automated systems also create dependence. Many questions may share data, templates, model components, or a common event. Daily updates from one system are not independent observations. Confidence intervals should preserve temporal and question-level dependence; otherwise apparent differences can be much more precise than the evidence warrants.[9] Report the number of resolved questions, event counts, unique information episodes, and effective rather than merely nominal sample size where a defensible estimate exists.

### For rare-event and safety evaluation

Safety-critical evaluators should define tails prospectively. Evaluating only disasters that occurred rewards systems that assign high risk everywhere and removes the non-events needed to judge false alarms.[10] Proper weighted scores can emphasize a predeclared region, but weighting changes which parts of the distribution are identified most strongly. The score should be accompanied by event counts, false-alarm behavior, calibration in the relevant probability range, and uncertainty.[9][10]

Exact zero and one probabilities deserve governance. Logarithmic loss makes a realized zero-probability event infinitely costly, while Brier loss remains finite.[1][2] A platform may prohibit exact endpoints or impose a predeclared floor, but that is a policy choice with incentive consequences. It should not silently edit forecasts after resolution. In systems where omitted possibilities represent catastrophic model failure, stress tests and open-world scenario analysis should supplement scores because a closed outcome set cannot measure events it never represented.

Pending, annulled, and disputed cases should remain visible. Removing them without counts creates survivorship bias; assigning outcomes to them invents evidence. The evaluation report should state how many questions opened, received forecasts, closed normally, remained pending, were annulled, and were disputed, then score only the set for which the declared rule supplies an outcome.[7][8][12]

### For organizations and decision-makers

An organization should separate four claims: accuracy, calibration, incremental skill, and decision utility. Accuracy is performance under the chosen proper loss. Calibration is frequency consistency. Skill is improvement over a reference. Utility is the consequence of using the forecast under a particular decision rule.[2][4][13] A system can improve one while leaving another unchanged.

The author's synthesis is a minimum evaluation report with twelve fields:

1. forecast object and exact outcome definition;
2. scoring equation, orientation, range, and normalization;
3. eligible cases and information cutoff;
4. update and temporal-weighting policy;
5. case, topic, and participant weights;
6. missing, pending, annulled, and disputed-case policy;
7. reference forecasts on homogeneous cases;
8. calibration and resolution or discrimination diagnostics;
9. sharpness or interval width where applicable;
10. score uncertainty and dependence treatment;
11. separate individual, aggregate, model, and system results; and
12. decision utility under an explicit consequence model.

This framework is the author's synthesis of the scoring, tournament, operational-verification, and benchmark evidence.[2][7][8][9][12][13][14] It is deliberately auditable: a later reviewer can reconstruct what was scored and why.

For capital allocation, policy, medicine, or operations, the final decision layer should state which probability or quantile changes action. A proper score averaged over all cases may improve without changing the forecasts near that threshold. Conversely, a modest average improvement can be highly valuable if it corrects systematic errors at a costly boundary. Decision analysis should therefore be reported beside, not substituted for, general forecast evaluation.[2][13]

### Limits and stopping rule

A score is evidence about a specified forecast process on a specified case set. It is not a permanent trait of a person or model. Regime change, topic shift, new information access, altered incentives, or revised question design can change performance.[7][8][12] Rankings should include the evaluation period and scope rather than become timeless labels.

No diagnostic rescues an invalid measurement contract. If a question is vague, a resolution is changed after forecasts, or only favorable calls are retained, precise scoring produces precise-looking bias. The existing forecast-question-design framework in this library addresses the upstream contract; scoring begins only after that contract is sound.

The stopping rule is practical. Evaluation is adequate when an independent reviewer can reproduce the eligible cases, forecast versions, outcomes, formula, weights, baseline, diagnostics, and uncertainty, and when the result answers the decision-relevant comparison. If those elements cannot be reconstructed, another decimal place does not add knowledge. It only makes an undefined comparison look exact.

## Sources

1. Brier, G. W. (1950). "Verification of Forecasts Expressed in Terms
   of Probability." Monthly Weather Review, 78(1), 1-3.
   https://doi.org/10.1175/1520-0493(1950)078%3C0001:VOFEIT%3E2.0.CO;2
   [high]

2. Gneiting, T., and Raftery, A. E. (2007). "Strictly Proper Scoring
   Rules, Prediction, and Estimation." Journal of the American
   Statistical Association, 102(477), 359-378.
   https://doi.org/10.1198/016214506000001437 [high]

3. Murphy, A. H. (1973). "A New Vector Partition of the Probability
   Score." Journal of Applied Meteorology, 12(4), 595-600.
   https://doi.org/10.1175/1520-0450(1973)012%3C0595:ANVPOT%3E2.0.CO;2
   [high]

4. Gneiting, T., Balabdaoui, F., and Raftery, A. E. (2007).
   "Probabilistic Forecasts, Calibration and Sharpness." Journal of the
   Royal Statistical Society: Series B, 69(2), 243-268.
   https://doi.org/10.1111/j.1467-9868.2007.00587.x [high]

5. Epstein, E. S. (1969). "A Scoring System for Probability Forecasts
   of Ranked Categories." Journal of Applied Meteorology, 8(6), 985-987.
   https://doi.org/10.1175/1520-0450(1969)008%3C0985:ASSFPF%3E2.0.CO;2
   [high]

6. Bracher, J., Ray, E. L., Gneiting, T., and Reich, N. G. (2021).
   "Evaluating Epidemic Forecasts in an Interval Format." PLOS
   Computational Biology, 17(2), e1008618.
   https://doi.org/10.1371/journal.pcbi.1008618 [high]

7. Merkle, E. C., and Hartman, R. (2018). "Weighted Brier Score
   Decompositions for Topically Heterogeneous Forecasting Tournaments."
   Judgment and Decision Making, 13(2), 185-201.
   https://doi.org/10.1017/S1930297500007099 [high]

8. Mellers, B., Ungar, L., Baron, J., et al. (2014). "Psychological
   Strategies for Winning a Geopolitical Forecasting Tournament."
   Psychological Science, 25(5), 1106-1115.
   https://doi.org/10.1177/0956797614524255 [high]

9. Bradley, A. A., Schwartz, S. S., and Hashino, T. (2008). "Sampling
   Uncertainty and Confidence Intervals for the Brier Score and Brier
   Skill Score." Weather and Forecasting, 23(5), 992-1006.
   https://doi.org/10.1175/2007WAF2007049.1 [high]

10. Lerch, S., Thorarinsdottir, T. L., Ravazzolo, F., and Gneiting, T.
    (2017). "Forecaster's Dilemma: Extreme Events and Forecast
    Evaluation." Statistical Science, 32(1), 106-127.
    https://doi.org/10.1214/16-STS588 [high]

11. Witkowski, J., Freeman, R., Vaughan, J., Pennock, D., and Krause, A.
    (2018). "Incentive-Compatible Forecasting Competitions."
    Proceedings of the AAAI Conference on Artificial Intelligence,
    32(1). https://doi.org/10.1609/aaai.v32i1.11471 [high]

12. Karger, E., Bastani, H., Chen, Y.-H., Jacobs, Z., Halawi, D.,
    Zhang, F., and Tetlock, P. E. (2025). "ForecastBench: A Dynamic
    Benchmark of AI Forecasting Capabilities." International Conference
    on Learning Representations.
    https://proceedings.iclr.cc/paper_files/paper/2025/hash/ea74e45a229dac70b5b63b28d8934db6-Abstract-Conference.html
    [high]

13. European Centre for Medium-Range Weather Forecasts. "Forecast User
    Guide, Section 12.B: Statistical Concepts -- Probabilistic Data."
    https://confluence.ecmwf.int/display/FUG/Section+12.B+Statistical+Concepts+-+Probabilistic+Data
    [high]

14. National Hurricane Center. "Forecast Verification Procedures" and
    "Model Error Trends." National Oceanic and Atmospheric
    Administration.
    https://www.nhc.noaa.gov/verification/verify2.shtml
    https://www.nhc.noaa.gov/verification/verify6.shtml [high]

## See Also

- `library/probabilistic-thinking-forecasting/forecast-question-design.md`
  -- defines the event, resolution, timing, and participation contract
  that must exist before a score has a stable meaning.
- `library/probabilistic-thinking-forecasting/calibration-and-overconfidence.md`
  -- develops calibration curves and the distinction between frequency
  agreement and informative probability separation.
- `library/probabilistic-thinking-forecasting/superforecasting.md` --
  applies Brier scoring, updating, teams, and aggregation in forecasting
  tournaments.
- `library/probabilistic-thinking-forecasting/communicating-forecast-uncertainty.md`
  -- explains prediction intervals, coverage, sharpness, and the forecast
  object received by decision-makers.
- `library/probabilistic-thinking-forecasting/prediction-markets.md` --
  examines incentive-driven aggregation systems whose performance should
  be distinguished from individual forecasts.
- `library/self-improvement/decision-journals.md` -- preserves ex ante
  forecasts and separates repeated calibration evidence from memorable
  outcomes.
