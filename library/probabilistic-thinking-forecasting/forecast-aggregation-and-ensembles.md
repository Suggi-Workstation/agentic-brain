---
name: forecast-aggregation-and-ensembles
id: 20260930T193346Z
tier: library-topic
domain: probabilistic-thinking-forecasting
author: Librarian
tags: [forecast-aggregation, forecast-combination, ensembles, opinion-pools, extremizing, model-averaging, correlated-errors, judgmental-forecasting]
links: [library/probabilistic-thinking-forecasting/superforecasting.md, library/probabilistic-thinking-forecasting/prediction-markets.md, library/probabilistic-thinking-forecasting/forecast-evaluation-and-scoring-rules.md, library/probabilistic-thinking-forecasting/communicating-forecast-uncertainty.md, library/probabilistic-thinking-forecasting/calibration-and-overconfidence.md]
---

# Forecast Aggregation Improves Robustness Only When Dependence and Incentives Are Modeled

Forecast aggregation combines multiple model outputs or human judgments into one point forecast, probability, predictive distribution, or ordered decision input. The research record shows that combinations often reduce model-selection risk and idiosyncratic error, but the gain is conditional on component quality, informational diversity, stable evaluation, and honest elicitation.[1][2][3] Treating correlated forecasts as independent evidence can create false confidence, so a defensible ensemble must preserve provenance, measure dependence, and be tested prospectively against simple baselines.[3][5][11]

## Background

Forecasting rarely presents a decision-maker with only one plausible estimate. Different statistical models encode different trend, seasonality, covariate, and structural assumptions; different people observe different facts and apply different reference classes; and different institutions impose different incentives and information cutoffs. Forecast aggregation addresses the resulting problem by treating the forecasts themselves as inputs to a second-stage rule. That rule may be an arithmetic average, a median, a weighted regression, a probability pool, a Bayesian model average, a stacking procedure, a market price, or another mapping from component forecasts to a common output.[3][4][17]

The modern statistical literature is commonly traced to Bates and Granger's 1969 study of two forecasts for airline passenger data. They used past forecast errors to derive combination weights and showed that a composite could have lower mean squared error than either component.[1] The result mattered because it changed the object of attention. A forecaster no longer had to identify one permanently superior model; the combination could retain information from models whose errors differed. Clemen's 1989 review surveyed forecasting, psychology, statistics, and management science and concluded that multiple forecasts could substantially improve accuracy, while simple combination rules often performed competitively with more elaborate ones.[2]

The early point-forecast problem expanded into two related traditions. Forecast combination in economics and operations research asked how to combine numerical predictions of the same quantity. Expert-opinion pooling asked how to combine subjective probability distributions or beliefs. Genest and Zidek organized the latter field around consensus belief formation, expert use, and group decision-making, showing that aggregation rules embody substantive assumptions about what expert probabilities mean.[4] These traditions overlap mathematically, but they are not identical. Averaging two expected sales figures, pooling two event probabilities, and mixing two full predictive distributions produce different objects and require different loss functions and calibration checks.[3][4][5]

Three empirical developments widened the field. First, economic surveys generated panels of professional forecasts with long histories, repeated updates, entry, exit, and missing reports. These panels made it possible to compare equal weighting, trimming, performance weights, regressions, shrinkage, and regime-sensitive weights in pseudo-out-of-sample tests.[6][8][18] Second, forecasting tournaments elicited large numbers of explicit probabilities from human participants. The Good Judgment Project used training, teams, tracking, and statistical aggregation, allowing behavioral interventions and combination algorithms to be evaluated on resolved geopolitical questions.[9][12][13] Third, forecasting competitions and machine-learning practice normalized ensembles of statistical and algorithmic models. The M4 competition evaluated 61 methods on 100,000 time series and included both point forecasts and prediction intervals, providing a large comparative test bed for hybrid and combination methods.[14]

Probabilistic aggregation made an important limitation visible. A linear opinion pool takes a weighted arithmetic average of predictive cumulative distribution functions or event probabilities. It is simple and preserves a valid distribution, but even well-calibrated components need not yield a calibrated pool, and the pooled distribution can be too dispersed.[5][9] Nonlinear pools, spread adjustments, beta transformations, logarithmic pooling, and extremizing were developed partly to correct those failures.[5][9][10] The required correction depends on the information structure: when forecasters contribute partly independent evidence, a plain average can be too close to the prior or to 0.5; when they repeat the same evidence, aggressive extremizing can count that evidence more than once.[10][11]

Model uncertainty produced another branch. Bayesian model averaging assigns posterior probabilities to candidate models and averages their predictive implications, thereby representing uncertainty about which candidate generated the data.[15] Stacking instead learns weights for predictive distributions by optimizing out-of-sample predictive performance, and it is particularly relevant when none of the candidate models is assumed to be the true data-generating process.[16] Both methods are ensembles, but their weights answer different questions. Posterior model probability is not the same as a coefficient chosen to maximize a cross-validated score, and neither is automatically the same as a judgment about causal credibility.[15][16]

The resulting field is not a claim that crowds or ensembles are inherently wise. It is a set of conditional methods for reducing avoidable error. The recurring empirical finding is that simple averages are difficult to beat consistently, in part because estimated optimal weights introduce sampling error and can fail after structural change.[2][3][6] The recurring theoretical warning is that diversity, dependence, calibration, missingness, incentives, and regime stability determine whether apparent multiplicity represents additional information or merely repeated versions of the same mistake.[5][8][11][18][19]

## Core Concepts

### Define the forecast object before choosing the aggregator

Aggregation begins with a common measurement contract. Every component should refer to the same target, unit, horizon, information cutoff, and resolution rule. A one-quarter-ahead GDP growth point forecast cannot be averaged coherently with a probability of recession unless both are first translated into a common object. Likewise, a median, an expected value, a conditional scenario, and an unconditional predictive distribution are not interchangeable summaries.[3][5]

Four common output types require distinct rules. A point forecast gives one value and can be combined by means, medians, regressions, or other functions. A categorical probability forecast assigns probabilities that sum to one and can be pooled arithmetically, geometrically, or through a learned transform. A predictive distribution describes uncertainty across a continuous outcome and requires attention to calibration, dispersion, tails, and the distinction between mixing distributions and averaging their parameters. A ranked set orders alternatives but does not, by itself, identify probability differences or expected losses.[4][5] The author's synthesis is that an aggregator should never manufacture a stronger output than its inputs support: a consensus ranking is not a calibrated probability distribution, and an average of conditional scenarios is not automatically an unconditional forecast.

Forecast aggregation is also distinct from forecast evaluation and uncertainty communication. Aggregation is the ex ante operation that maps components into a combined forecast. Evaluation occurs after outcomes resolve and estimates calibration, accuracy, sharpness, skill, or utility under a declared rule. Communication determines how the resulting uncertainty and dissent are presented to users. Historical scores may inform weights, but scoring the past is not itself the act of combining the next set of forecasts.[3][5][6]

### Equal-weighted means are strong default estimators

For point forecasts `f_1` through `f_N`, the simple average is:

`f_bar = (1/N) * sum(f_i)`

Its appeal is not that all forecasters or models are known to be equally good. It is that the rule has no fitted weight parameters, distributes influence, and often cancels errors when components differ.[2][3] In finite samples, an estimated weighting rule must overcome both the average's forecast error and its own estimation error. If performance differences are weak, unstable, or measured on too few comparable cases, fitted weights can overreact to noise.[3][6]

The median is a more robust location rule. It ignores the magnitudes of extreme components once their rank is known, so a grossly erroneous or strategically extreme forecast has limited influence. A trimmed mean discards a declared fraction from each tail and averages the remainder; a Winsorized mean replaces tail observations with the nearest retained values. Jose and Winkler found that moderate trimming or Winsorizing slightly improved accuracy and reduced high-error risk in their data sets, with more robustification useful when component forecasts varied more widely.[7] Robust rules trade some efficiency under clean, homogeneous errors for protection against outliers, data mistakes, and occasional model breakdowns.

A simple average should be a baseline, not a religious commitment. It can deteriorate when poor forecasts dominate the pool, when the pool contains many near-duplicates of one method, or when one component has a persistent and measurable advantage.[3] The relevant comparison is prospective: does a more complex rule outperform equal weighting on cases generated after its weights and hyperparameters were chosen? Genre and colleagues found that several sophisticated combinations of ECB professional forecasts rarely beat equal weighting for GDP growth and unemployment, while inflation offered more evidence of improvement; multiple-comparison adjustments weakened confidence that every apparent gain would persist.[6]

### Performance weighting must account for estimation error and dependence

A weighted point combination has the form:

`f_combined = sum(w_i * f_i)`, with `sum(w_i) = 1`

Weights can be based on inverse historical error, recent performance, regression coefficients, expertise, or a learned loss function. In the classical two-forecast setting, minimum-variance weights depend on each forecast's error variance and the covariance between their errors.[1][3] This covariance term is essential. Two individually accurate forecasts that fail on the same cases may add less joint value than one accurate forecast paired with a somewhat weaker but genuinely different forecast.

Unconstrained regression weights can be negative or larger than one. Such weights may be justified when one forecast corrects another's bias, but they can also signal unstable estimation or collinearity. Nonnegative weights that sum to one keep the aggregate within the convex hull of point forecasts and are easier to explain, at the cost of excluding potentially useful bias corrections.[3] Shrinkage offers a reversible compromise: estimate performance differences, but pull noisy weights toward equality rather than treating short track records as permanent skill.

Weighting must match the loss. Squared-error optimization emphasizes large misses and leads naturally to means. Absolute-error optimization favors medians. A decision with asymmetric costs may justify a quantile or a custom utility, but the loss should be declared before outcomes are observed.[3] A model selected because it minimizes one score may not minimize another, and a probability pool optimized for log loss can behave differently from one optimized for Brier loss.

### Linear opinion pools preserve distributions but not calibration

For predictive cumulative distribution functions `F_i(y)`, a linear opinion pool is:

`F_pool(y) = sum(w_i * F_i(y))`

with nonnegative weights summing to one. For binary events, the same rule reduces to a weighted average of probabilities. The result is a valid probability distribution and can represent disagreement through a mixture.[4][5] However, the operation does not automatically preserve the statistical properties of its components. Research on predictive distributions shows that a nontrivial linear pool of calibrated components can be overdispersed and uncalibrated.[5]

This point resolves an apparent paradox. Mixing component distributions preserves between-model disagreement as additional spread, which can be desirable when that disagreement reflects unresolved model uncertainty. Yet if every component has already represented the same uncertainty and shares much of the same evidence, the mixture may count uncertainty in the wrong way. Conversely, averaging distribution parameters rather than distributions may erase multimodality and understate tails. The correct object depends on what the members represent, not on a universal preference for narrower or wider output.[3][5]

Generalized linear pools transform component cumulative probabilities before combination. Spread-adjusted pools modify component dispersion. Beta-transformed linear pools recalibrate the combined cumulative distribution with a flexible nonlinear transformation.[5] These methods can correct systematic under- or overdispersion when adequate training data exist. They also add parameters, so they require held-out or rolling-origin evaluation and should be compared with the untransformed pool.

Logarithmic opinion pooling combines probability densities or odds multiplicatively after assigning weights. It can produce sharper consensus than arithmetic pooling because common support is reinforced and disagreement is penalized differently.[4][9] For binary probabilities, averaging log odds and mapping back through the logistic function is one practical form. Zero or one reports require explicit handling because their log odds are infinite; arbitrary clipping changes the method and should be disclosed.

### Extremizing is an information correction, not a confidence ritual

Probability averages often move toward 0.5. Baron and colleagues identified two mechanisms: bounded probabilities create scale compression near zero and one, and individual forecasters condition on only part of the information collectively available.[10] An extremizing transform moves an aggregate away from 0.5 toward the nearer endpoint. Satopaa and colleagues derived a simple logit-based aggregator and found it superior to several widely used algorithms on forecasts from more than 1,300 experts covering 69 geopolitical events.[9]

Extremizing is justified only when the aggregate underuses distinct information. A model of partially overlapping information sources shows that the optimal amount depends on overlap: more nonredundant evidence can justify stronger movement, while extensive sharing reduces it.[11] Extremizing correlated forecasts as if they were independent can create severe overconfidence. The practical control is to estimate the transform on past, comparable questions and validate it out of sample; if the available sample is small or the information structure changed, the simple mean or median is safer.

The direction of correction can also reverse. A pool of overconfident components may need anti-extremizing or another recalibration toward the center. Calibration and sharpness must therefore be evaluated together. A forecast can become sharper by moving toward zero and one while becoming less reliable, and apparent calibration can be achieved by staying near the base rate while contributing little discrimination.[5][9]

### Bayesian combinations and stacking encode different assumptions

Bayesian model averaging starts with candidate models, prior model probabilities, and model-specific priors. Bayes' rule updates the model probabilities with observed data, and the predictive distribution averages model-specific predictions using those posterior probabilities.[15] Its advantage is coherence within the declared model space: uncertainty over model identity is propagated instead of being discarded after selecting one model. Its vulnerability is also explicit: posterior weights depend on the candidate set, likelihoods, and priors, and the method is strained when every candidate is materially misspecified.[15][16]

Stacking chooses nonnegative weights for predictive distributions to optimize a cross-validated predictive score. Yao and colleagues extended stacking to Bayesian predictive distributions and, in simulations and real-data applications, recommended it over Bayesian model averaging in the M-open setting where the true process is not assumed to be among the candidate models.[16] Stacking is performance-oriented rather than a posterior probability statement. Its weights should not be interpreted as probabilities that models are true.

Both methods can overfit if the evaluation sample is small relative to the number of components or if cross-validation ignores temporal dependence. Time-series applications need rolling or expanding windows that respect the direction of time. Human-forecast panels need question-level splits that prevent repeated updates on one event from leaking into both training and validation. The author's synthesis is to use the simplest combination whose assumptions and validation design fit the available history.

### Diversity is useful only when it changes error structure

Counting components is not measuring diversity. Ten models trained on the same data with nearly identical features, objectives, and architectures may behave like one model with ten random seeds. Ten analysts who read the same report may repeat one evidence set. The useful quantity is not surface variety but differential error: do components make different mistakes on comparable cases, and are those mistakes informative rather than random?[3][11]

Dependence can arise from common data, shared preprocessing, copied forecasts, common priors, organizational hierarchy, social influence, or the same unresolved causal assumption. Error correlations estimated from history are one diagnostic, but they are imperfect. Correlations can change by horizon and regime, and two forecasts can show low historical correlation while still sharing a hidden failure mode that has not yet occurred.[3][8] Provenance metadata therefore complements covariance estimates: record data sources, model families, information cutoffs, human collaboration, and known shared assumptions.

Diversity also interacts with quality. Adding an independent but systematically uninformed forecast can worsen the aggregate. The current review literature treats forecast selection as a balance among accuracy, diversity, robustness, and the estimation cost of selecting or weighting components.[3] A defensible pool uses inclusion rules fixed before the evaluation period, rather than adding or removing members after seeing which outcome occurred.

### Regime change makes permanent weights fragile

A combination weight estimated in one environment is a forecast about future relative performance. When the data-generating process changes, that forecast can fail. Elliott and Timmermann developed a regime-switching combination in which weights vary with a latent state and showed favorable results in macroeconomic applications and simulations under relevant processes.[8] More generally, rolling weights, discounting, dynamic model averaging, and change-point methods trade stability for adaptation.[3][8]

Fast adaptation is not automatically superior. Short windows respond quickly but estimate weights noisily; long windows estimate more precisely but retain stale regimes. Dynamic systems can mistake ordinary variance for structural change and chase recent winners. The author's synthesis is to maintain three comparisons: a stable equal-weight benchmark, a slowly adapting rule, and a regime-sensitive challenger. Weight movement should be explained by new evidence or a declared state model, not by discretionary reactions to each error.

### Missing forecasts and incentives are part of the model

Human panels and production model fleets are rarely balanced. Participants enter and leave, some questions receive more attention, systems fail, and experts may abstain when uncertain. Capistran and Timmermann showed that entry and exit can materially affect real-time combination performance; they proposed bias adjustment and an expectation-maximization approach for back-filling a panel, while emphasizing that conventional regressions can become infeasible under missingness.[18] A dynamic hierarchical model applied to more than 2,300 experts and 166 international political events was designed for sparse, irregular updates and produced sharp, calibrated aggregate probabilities in and out of sample.[12]

Missingness should not be treated automatically as a neutral absence. A forecaster who answers only easy questions, a model that fails under extreme inputs, and a participant who abstains when privately uncertain create different selection mechanisms. Complete-case analysis can change the pool over time; carrying forecasts forward can make stale beliefs look current; imputation can create precision that was never observed. The procedure should preserve counts, timestamps, eligibility, abstentions, and the reason for missingness.[12][18]

Incentives shape the reports being aggregated. Proper scoring rules can reward truthful probabilities when each participant is paid by score, but a winner-take-all competition can reward strategic extremity instead.[19] Prediction markets use trades and prices to aggregate dispersed information, but their output depends on participation, liquidity, contract definition, budgets, and incentives; they are mechanisms, not automatic truth machines.[20] Organizational forecasts face parallel problems when promotion rewards bold calls, consensus, or avoidance of blame. Elicitation design therefore precedes aggregation: independent initial estimates, clear questions, protected dissent, proper rewards, and visible revision histories improve the inputs before any algorithm combines them.[13][19][20]

## Evidence

### Foundational point combinations reduced error in a real series

Bates and Granger combined two forecasts of airline passenger data and compared methods for deriving weights from past errors. Their principal result was that the composite could attain lower mean squared error than either original forecast.[1] The method supplied a concrete variance-covariance explanation: if components contain different error information, neither has to dominate everywhere for the combination to help. The case does not prove that every average beats every member; it demonstrates that choosing one model and combining models are distinct statistical decisions.

Clemen's review examined the accumulated theoretical and empirical literature through the late 1980s. It reported two durable findings: combinations often improve forecast accuracy, and simple methods frequently compare well with more complex estimators.[2] The review covered several disciplines, reducing the likelihood that the result was an artifact of one application. Its limitation is temporal and methodological: later work added predictive distributions, machine learning, dynamic panels, cross-validation, and modern calibration diagnostics.[3][5]

### Professional forecast panels expose the combination puzzle

Genre, Kenny, Meyler, and Timmermann evaluated ECB Survey of Professional Forecasters data using principal components, trimmed means, performance weights, least-squares weights, and Bayesian shrinkage. In pseudo-out-of-sample comparisons, few methods beat the simple average for GDP growth and unemployment, while inflation provided stronger evidence for improvement.[6] After accounting for multiple model comparisons, the authors cautioned that identified gains might not persist. The study directly illustrates why in-sample optimality is insufficient: a flexible combination can fit historical rankings without establishing a durable future advantage.

Missingness is not incidental in such panels. Capistran and Timmermann analyzed frequent entry and exit of individual forecasters, showed through simulations and macroeconomic applications that it can have a large effect on real-time performance, and proposed bias-adjusted equal weighting and panel completion by an expectation-maximization algorithm.[18] Their result establishes that an aggregate over whoever happened to report is not necessarily comparable across dates. Composition, not only beliefs, can move the published consensus.

### Robust averages reduce exposure to extreme components

Jose and Winkler compared the mean, median, and multiple trimmed and Winsorized combinations across a pool of 22 individual methods. They found that moderate trimming of 10 to 30 percent or Winsorizing of 15 to 45 percent slightly improved forecast accuracy and reduced the risk of large errors in their data, with stronger robustification indicated when component variability was greater.[7] The evidence supports robust rules as practical alternatives, not universal optimal percentages. A pool with only a few members, legitimate tail information, or asymmetric loss can require a different treatment.

### Geopolitical tournaments show gains from both people and algorithms

Mellers and colleagues studied five university teams in a two-year geopolitical forecasting tournament. Probability training, collaboration, and tracking of high performers improved calibration and resolution, while statistical algorithms added further aggregation gains.[13] This design matters because it separates improvement of individual inputs from improvement of the aggregation rule. The best system was not merely a larger crowd; it combined elicitation, learning, team process, and statistical pooling.

Satopaa and colleagues evaluated a one-parameter logit aggregator on forecasts from more than 1,300 experts covering 69 geopolitical events and reported superior performance to several widely used alternatives.[9] A related dynamic hierarchical study used more than 2,300 experts making irregular updates on different subsets of 166 events and reported sharp, calibrated in-sample and out-of-sample aggregates.[12] These studies support extremizing and dynamic modeling when their assumptions fit the information structure. They do not support applying the same transform to a tightly coordinated team whose members share evidence; partial-information theory predicts that overlap changes the required amount of extremizing.[11]

### Large forecasting competitions favor combinations but preserve context

The M4 competition evaluated 61 methods across 100,000 time series and included point forecasts and prediction intervals. Its published results report that the top-performing methods were combinations or hybrids rather than isolated pure methods, while performance varied by series and horizon.[14] This is strong evidence that ensemble design can scale across heterogeneous time-series tasks. It is not proof that any generic ensemble will win: competition entries included specialized preprocessing, model selection, cross-series learning, and tailored combination structures, and the evaluation reflected the M4 data distribution and metrics.[14]

The broader 50-year review confirms that the field has progressed from fixed simple averages to time-varying weights, nonlinear pooling, dependence-aware methods, and cross-learning.[3] It also retains the combination puzzle: equal weighting is surprisingly robust because sophisticated estimates pay a price for sampling error, parameter instability, and correlations that are difficult to estimate accurately.[3][6] The empirical lesson is comparative rather than absolute. Complexity earns adoption only when it beats a simple combination prospectively and repeatedly.

### Predictive-distribution studies show that averaging can miscalibrate

Gneiting and Ranjan studied aggregation of discrete, mixed, and continuous predictive distributions from the perspectives of calibration and dispersion. They examined linear and nonlinear approaches, including generalized, spread-adjusted, and beta-transformed pools, using theory, simulations, and case studies on S&P 500 returns and daily maximum temperature at Seattle-Tacoma Airport.[5] Their work shows why probability aggregation cannot be reduced to point averaging: a pooled distribution may be valid as a distribution yet have the wrong dispersion or calibration.

Bayesian model averaging and stacking provide two further evidence streams. Hoeting and colleagues reviewed BMA and presented examples in which representing model uncertainty improved out-of-sample predictive performance.[15] Yao and colleagues compared stacking of predictive distributions with stacking of means, BMA, and pseudo-BMA variants; based on simulations and real-data applications, they recommended predictive-distribution stacking in M-open settings.[16] The studies support conditional method choice. BMA is coherent when the model space and priors are credible; stacking is attractive when prediction is primary and all candidates may be wrong.

### Regime and incentive evidence identify structural failure modes

Elliott and Timmermann proposed latent regime-switching weights and found that the method performed well for several macroeconomic variables, with simulations identifying processes under which it could outperform alternatives.[8] The evidence supports time-varying weights when performance changes with a persistent state. It does not eliminate the need for a stable baseline because a falsely detected regime can add variance.

Witkowski and colleagues showed that proper scores support truthful reports when participants are rewarded according to their scores, but a single-prize contest can instead encourage more extreme reporting.[19] Arrow and colleagues described prediction markets as mechanisms for collecting dispersed information while acknowledging possible biases and institutional restrictions.[20] Together these sources establish that the aggregate cannot be evaluated independently of how forecasts were elicited. A mathematically refined pool of strategically distorted inputs is not a trustworthy consensus.

## Implications

### For forecasters and model builders

Begin with an explicit inventory. For every component, record the target, horizon, issue time, data vintage, model version or human identifier, conditioning assumptions, training window, and known shared inputs. Reject combinations of forecasts that answer different questions. This metadata is necessary to distinguish independent evidence from repeated evidence and to reconstruct the aggregate after a revision.[3][11][18]

Use equal weighting as the minimum benchmark. Add a median, a modest trimmed mean, or a Winsorized mean when operational mistakes or occasional extreme outputs are plausible.[6][7] A proposed performance-weighted method should be trained only on information available at each historical forecast origin and evaluated on later cases. Report whether the gain survives alternative windows, horizons, metrics, and component subsets. If the gain disappears under a small perturbation, the fitted weights are not stable enough to carry interpretive weight.

Estimate diversity at the error level and document it at the provenance level. A correlation matrix of forecast errors is useful, but it should be stratified by horizon, regime, and target where sample size permits. Cluster near-duplicate models or analysts before weighting so that copying one method does not multiply its vote. Stress-test shared assumptions by adding scenarios in which the common data source, causal model, or market regime fails.[3][8][11]

For probabilities, retain the raw individual forecasts as well as the pool. Plot calibration and resolution by probability range, inspect the distribution of disagreement, and compare arithmetic, log-odds, and any transformed aggregate under proper scores.[5][9][10] Extremize only after prospective or cross-validated evidence shows that the raw pool is systematically too central. The transform should depend on observed information overlap or out-of-sample calibration, not on a preference for decisive numbers.[10][11]

For full predictive distributions, state whether the procedure mixes cumulative distributions, densities, quantiles, samples, or parameters. Those operations are not equivalent. Evaluate empirical coverage, sharpness, tails, and a proper distributional score. A linear pool can preserve multimodality but become overdispersed; parameter averaging can look smooth while deleting legitimate modes.[5] The user's decision may require the mixture distribution even when its mean is similar to a simpler point average.

For Bayesian ensembles, separate belief about model identity from predictive weighting. Use BMA when priors, likelihoods, and the candidate model space support that interpretation.[15] Use stacking when the objective is predictive performance and no candidate is presumed true.[16] Do not describe stacking weights as posterior probabilities or BMA weights as proof of causal validity. For time series, use rolling-origin validation; ordinary random folds can leak future regimes into past training.

### For human forecasting systems

Elicit initial judgments independently before discussion. Independence prevents early anchors, senior voices, and visible consensus from collapsing informational diversity before it can be measured.[11][13] After the first forecast, allow structured exchange of evidence and record revisions. The aggregate can then distinguish the value of independent collection from the value of deliberation.

Track both forecaster skill and question difficulty. Performance weights require enough comparable resolved cases; otherwise they reward luck or specialization. Shrink individual weights toward equality and publish uncertainty about the ranking. The Good Judgment evidence supports training, teaming, and tracking together, not the claim that one permanent elite should dominate every domain.[13]

Handle missing forecasts explicitly. Define eligibility before each question, preserve abstentions, mark stale forecasts, and distinguish nonparticipation from system failure.[12][18] Do not silently carry forward a probability after the forecaster's information set has changed. If imputation is necessary, report the method and compare the aggregate with a complete-case or equal-weight sensitivity analysis.

Align incentives with truthful probability reports. Proper scoring can elicit honest beliefs under its assumptions, while winner-take-all rewards can encourage strategic extremity.[19] Organizational incentives can be equally distorting: analysts may herd to avoid blame, exaggerate to gain attention, or conceal uncertainty to satisfy management. Reward a long prospective record, documented updating, and calibration rather than memorable single calls.

Prediction markets are one option when information is dispersed and trading is appropriate. Their prices should be interpreted alongside liquidity, participation, contract wording, position limits, and the possibility of common public information.[20] A market price can be one component in a broader ensemble, but adding both the market and forecasts derived from that same market may double count the signal.

### For organizations and decision-makers

Preserve disagreement instead of publishing only one consensus number. The combined forecast is useful for action, but the component range, clusters, and common assumptions reveal fragility. A narrow consensus among highly correlated models should not be presented as stronger evidence than a similar consensus among genuinely independent methods.[3][11] Show how the aggregate changes when each major model family or information source is removed.

Separate the belief layer from the decision layer. Aggregation estimates an outcome or distribution. The decision also depends on payoffs, constraints, reversibility, and risk tolerance. A small improvement in average forecast score may have no operational value if it does not change an action threshold; a modest improvement in a critical tail can be valuable even if the mean score changes little. The aggregate should feed an explicit decision rule rather than silently embed one.

Maintain a champion-challenger architecture. The champion is a simple, stable average or median. Challengers can use performance weighting, nonlinear pooling, stacking, or regime switching.[3][6][8] Promote a challenger only after it wins on a prospectively defined evaluation and remains interpretable under sensitivity tests. Keep the old method available for rollback because aggregation systems can fail precisely when regimes change.

Monitor composition. If the number of models rises but all new members inherit the same base model, vendor data, or prompting policy, nominal ensemble size will overstate effective diversity. If experts enter and exit, track whether movement in the consensus reflects beliefs or membership.[18] Report both the number of components and a dependence-adjusted description, such as clusters of shared model lineage or data provenance.

### For investing and capital allocation

Analyst estimates, valuation models, and scenario forecasts are usually correlated. They may share company guidance, consensus industry assumptions, commodity curves, interest rates, or terminal-value conventions. Averaging them without tracing those common inputs creates an illusion of independent confirmation. The author's synthesis is to aggregate at two levels: first combine distinct estimates within a shared assumption family, then combine across families with explicit dependence and scenario labels.[3][11]

A median or trimmed mean can reduce the influence of one broken model, but it can also suppress a legitimate tail case. Preserve bear, base, and bull scenarios as conditional distributions rather than treating their labels as fixed quantiles. If probabilities are assigned, elicit them separately and check whether scenarios are mutually exclusive and collectively adequate. A probability-weighted valuation is only as credible as the dependence assumptions among revenue, margins, financing, and terminal value.

Regime-sensitive weights deserve particular caution in markets. Recent performance can reflect one factor regime rather than durable skill. A model that dominated during falling rates may be redundant with several peers and fail jointly after a policy shift. Compare dynamic weighting with equal weighting, cap turnover in weights, and require an economic explanation for state changes.[8] Margin of safety should respond to unresolved dependence and model misspecification rather than to the superficial precision of a large ensemble.

### For human-AI and multi-model workflows

Multiple language models or agents are not automatically independent forecasters. Shared pretraining data, retrieval sources, prompts, tools, and reward models can produce correlated errors even when wording differs. Preserve each agent's evidence citations and intermediate assumptions, then deduplicate common sources before treating agreement as corroboration. The same rule applies to conventional models: diversity must be demonstrated through errors and provenance, not vendor names.[3][11]

A useful workflow assigns components different information or methods before aggregation: one model uses base rates, another builds a structural decomposition, another searches for disconfirming evidence, and a human reviews unresolved source conflicts. This design seeks complementary error patterns rather than several votes on the same prompt. Performance weights should be learned on future-resolving tasks comparable to the intended use, and the ensemble should include a simple baseline that no agent can tune after resolution.

### An auditable aggregation protocol

The author's synthesis of the evidence is a twelve-step protocol:

1. Define one target, horizon, unit, information cutoff, and resolution rule.
2. Specify whether the output is a point, event probability, distribution, interval, or ranking.
3. Capture every component before discussion or exposure to the aggregate.
4. Record provenance, common data, model lineage, and known shared assumptions.
5. Screen only for predeclared eligibility failures; do not remove inconvenient forecasts after outcomes.
6. Produce equal-weight mean and median baselines, plus a robust trimmed alternative when the pool is large enough.
7. Estimate skill and error dependence on prior comparable cases with uncertainty intervals.
8. Fit any weighted, transformed, Bayesian, stacked, or regime-sensitive rule without future leakage.
9. Evaluate prospectively with a proper score and decision-relevant utility, keeping those two results separate.
10. Test missingness, component removal, regime shifts, correlation clusters, and extreme inputs.
11. Publish the aggregate with disagreement, composition, assumptions, and revision history.
12. Revert to the simple baseline when complex weights lose out-of-sample support.

This protocol does not guarantee accuracy. It prevents the most damaging category error: mistaking the number of forecasts for the amount of independent evidence. Aggregation is most valuable when it combines genuinely different, reasonably competent views under stable and honest measurement. When those conditions fail, the ensemble can become a machine for converting shared ignorance into precise-looking confidence.[3][5][11][19]

## Sources

1. Bates, J. M., and Granger, C. W. J. (1969). "The Combination of
   Forecasts." Journal of the Operational Research Society, 20(4),
   451-468. https://doi.org/10.1057/jors.1969.103 [high]

2. Clemen, R. T. (1989). "Combining Forecasts: A Review and Annotated
   Bibliography." International Journal of Forecasting, 5(4), 559-583.
   https://doi.org/10.1016/0169-2070(89)90012-5 [high]

3. Wang, X., Hyndman, R. J., Li, F., and Kang, Y. (2023). "Forecast
   Combinations: An over 50-Year Review." International Journal of
   Forecasting, 39(4), 1518-1547.
   https://doi.org/10.1016/j.ijforecast.2022.11.005 [high]

4. Genest, C., and Zidek, J. V. (1986). "Combining Probability
   Distributions: A Critique and an Annotated Bibliography."
   Statistical Science, 1(1), 114-135.
   https://doi.org/10.1214/ss/1177013825 [high]

5. Gneiting, T., and Ranjan, R. (2013). "Combining Predictive
   Distributions." Electronic Journal of Statistics, 7, 1747-1782.
   https://doi.org/10.1214/13-EJS823 [high]

6. Genre, V., Kenny, G., Meyler, A., and Timmermann, A. (2013).
   "Combining Expert Forecasts: Can Anything Beat the Simple Average?"
   International Journal of Forecasting, 29(1), 108-121.
   https://doi.org/10.1016/j.ijforecast.2012.06.004 [high]

7. Jose, V. R. R., and Winkler, R. L. (2008). "Simple Robust Averages
   of Forecasts: Some Empirical Results." International Journal of
   Forecasting, 24(1), 163-169.
   https://doi.org/10.1016/j.ijforecast.2007.06.001 [high]

8. Elliott, G., and Timmermann, A. (2005). "Optimal Forecast
   Combination under Regime Switching." International Economic Review,
   46(4), 1081-1102.
   https://doi.org/10.1111/j.1468-2354.2005.00361.x [high]

9. Satopaa, V. A., Baron, J., Foster, D. P., Mellers, B. A., Tetlock,
   P. E., and Ungar, L. H. (2014). "Combining Multiple Probability
   Predictions Using a Simple Logit Model." International Journal of
   Forecasting, 30(2), 344-356.
   https://doi.org/10.1016/j.ijforecast.2013.09.009 [high]

10. Baron, J., Mellers, B. A., Tetlock, P. E., Stone, E., and Ungar,
    L. H. (2014). "Two Reasons to Make Aggregated Probability Forecasts
    More Extreme." Decision Analysis, 11(2), 133-145.
    https://doi.org/10.1287/deca.2014.0293 [high]

11. Satopaa, V. A., Pemantle, R., and Ungar, L. H. (2016). "Modeling
    Probability Forecasts via Information Diversity." Journal of the
    American Statistical Association, 111(516), 1623-1633.
    https://doi.org/10.1080/01621459.2015.1100621 [high]

12. Satopaa, V. A., Jensen, S. T., Mellers, B. A., Tetlock, P. E., and
    Ungar, L. H. (2014). "Probability Aggregation in Time-Series:
    Dynamic Hierarchical Modeling of Sparse Expert Beliefs." Annals of
    Applied Statistics, 8(2), 1256-1280.
    https://doi.org/10.1214/14-AOAS739 [high]

13. Mellers, B., Ungar, L., Baron, J., Ramos, J., Gurcay, B., Fincher,
    K., Scott, S. E., Moore, D., Atanasov, P., Swift, S. A., Murray, T.,
    Stone, E., and Tetlock, P. E. (2014). "Psychological Strategies for
    Winning a Geopolitical Forecasting Tournament." Psychological
    Science, 25(5), 1106-1115.
    https://doi.org/10.1177/0956797614524255 [high]

14. Makridakis, S., Spiliotis, E., and Assimakopoulos, V. (2020). "The
    M4 Competition: 100,000 Time Series and 61 Forecasting Methods."
    International Journal of Forecasting, 36(1), 54-74.
    https://doi.org/10.1016/j.ijforecast.2019.04.014 [high]

15. Hoeting, J. A., Madigan, D., Raftery, A. E., and Volinsky, C. T.
    (1999). "Bayesian Model Averaging: A Tutorial." Statistical Science,
    14(4), 382-417. https://doi.org/10.1214/ss/1009212519 [high]

16. Yao, Y., Vehtari, A., Simpson, D., and Gelman, A. (2018). "Using
    Stacking to Average Bayesian Predictive Distributions." Bayesian
    Analysis, 13(3), 917-1003.
    https://doi.org/10.1214/17-BA1091 [high]

17. McAndrew, T., and Reich, N. G. (2021). "Aggregating Predictions
    from Experts: A Review of Statistical Methods, Experiments, and
    Applications." Wiley Interdisciplinary Reviews: Computational
    Statistics, 13(2), e1514. https://doi.org/10.1002/wics.1514 [high]

18. Capistran, C., and Timmermann, A. (2009). "Forecast Combination
    with Entry and Exit of Experts." Journal of Business and Economic
    Statistics, 27(4), 428-440.
    https://doi.org/10.1198/jbes.2009.07211 [high]

19. Witkowski, J., Freeman, R., Vaughan, J., Pennock, D., and Krause,
    A. (2018). "Incentive-Compatible Forecasting Competitions."
    Proceedings of the AAAI Conference on Artificial Intelligence,
    32(1). https://doi.org/10.1609/aaai.v32i1.11471 [high]

20. Arrow, K. J., Forsythe, R., Gorham, M., Hahn, R., Hanson, R.,
    Ledyard, J. O., Levmore, S., Litan, R. E., Milgrom, P., Nelson,
    F. D., Neumann, G. R., Ottaviani, M., Schelling, T. C., Shiller,
    R. J., Smith, V. L., Snowberg, E., Sunstein, C. R., Tetlock, P. C.,
    Tetlock, P. E., Varian, H. R., Wolfers, J., and Zitzewitz, E.
    (2008). "The Promise of Prediction Markets." Science, 320(5878),
    877-878. https://doi.org/10.1126/science.1157679 [high]

## See Also

- `library/probabilistic-thinking-forecasting/superforecasting.md` --
  develops the human practices, teams, and tracking systems that supply
  judgmental forecasts to an aggregator.
- `library/probabilistic-thinking-forecasting/prediction-markets.md` --
  examines a market mechanism for eliciting and combining dispersed
  beliefs.
- `library/probabilistic-thinking-forecasting/forecast-evaluation-and-scoring-rules.md`
  -- distinguishes ex ante combination from the proper scoring and
  diagnostics applied after outcomes resolve.
- `library/probabilistic-thinking-forecasting/communicating-forecast-uncertainty.md`
  -- explains how a combined probability or distribution should be
  presented without hiding assumptions, dispersion, or dissent.
- `library/probabilistic-thinking-forecasting/calibration-and-overconfidence.md`
  -- develops the calibration tests needed to detect a pool that is too
  central, too extreme, or otherwise unreliable.
