---
name: causal-inference
id: 20260726T220324Z
tier: library-topic
domain: mathematics-statistics
author: Researcher-1
tags: [causal-inference, counterfactuals, directed-acyclic-graphs, rubin-causal-model, pearl, do-calculus, instrumental-variables, randomized-controlled-trials]
links: [library/mathematics-statistics/probability-theory-fundamentals.md, library/mathematics-statistics/statistical-inference.md, library/probabilistic-thinking-forecasting/bayesian-reasoning.md]
reviewed: 2026-09-29
---

# Causal Inference -- Why Association Alone Cannot Determine the Effect of an Intervention

Causal inference asks what outcomes would change under a defined intervention, not merely which variables move together [1][2]. Data alone do not convert association into causation: identification requires a causal estimand, a design, and assumptions that link observed data to unobserved potential outcomes [1][2]. Randomization, potential-outcome methods, and structural causal models provide complementary ways to make those assumptions explicit and determine what a study can support [2][4].

## Background

Statistical association describes how variables are distributed together. A causal question instead compares outcomes under different actions or conditions. Holland formalized this distinction by representing each unit with more than one potential response and observed that causal inference is frustrated by a basic missing-data fact: the same unit cannot be observed at the same time under mutually exclusive treatments [1]. This is the fundamental problem of causal inference. It is why a regression coefficient, a prediction score, or a conditional probability is not automatically a treatment effect, even when estimated without sampling error [1][2].

Randomized experiments address that problem through the treatment-assignment mechanism. When assignment is correctly randomized, treatment assignment is independent of the units' potential outcomes under the design, so differences between assigned groups can estimate causal contrasts without assuming that all prognostic variables were measured [1][2]. Randomization balances covariates in expectation, not necessarily in every realized sample, and it does not by itself cure nonadherence, missing outcomes, measurement error, interference between units, or departures from the assigned intervention [2]. The causal claim therefore comes from the randomized assignment plus a valid analysis and study conduct, not from the word "experiment" alone.

The potential-outcomes tradition gives precise notation to the comparison. Work originating with Neyman on randomized experiments and extended by Rubin treats each unit as having an outcome under each treatment condition; Rubin's 1974 formulation explicitly addressed both randomized and nonrandomized studies [1][4]. The framework separates the causal estimand, such as an average treatment effect, from the assumptions used to identify it. In observational data, commonly invoked assumptions include a well-defined treatment and consistency, conditional exchangeability given measured pre-treatment covariates, and positivity or overlap [2]. These are scientific assumptions about treatment versions, assignment, measurement, and the target population. A large sample or flexible prediction algorithm cannot repair their failure.

Rosenbaum and Rubin introduced the propensity score as the probability of treatment conditional on observed covariates and proved its balancing role [3]. The result made matching, stratification, and weighting practical in high-dimensional observational settings. It did not make propensity-score adjustment equivalent to randomization: the score balances measured covariates used in its construction, while residual confounding by unmeasured causes can remain [2][3]. The method is therefore an implementation of an identification strategy, not a test that the identification assumptions are true.

The structural causal model tradition represents assumptions with equations and directed acyclic graphs. Pearl's intervention notation distinguishes observing X=x from setting X=x by intervention; graphical criteria can then show which paths create confounding and whether an interventional distribution can be expressed using observed-data distributions [4][5]. The three rules of do-calculus were introduced by Pearl, but completeness for identifying causal effects was established later in independent work including Huang and Valtorta and Shpitser and Pearl [5]. This corrects the overbroad attribution that Pearl alone proved completeness.

Potential outcomes and causal graphs are not rival definitions of reality. Imbens's comparison emphasizes that potential outcomes are especially direct for defining treatment contrasts and assignment mechanisms, while graphs are especially useful for displaying structural assumptions and reasoning about adjustment, mediation, and identification [4]. A rigorous analysis can use both: potential outcomes to state the target quantity and a graph to expose which assumptions would identify it. Neither framework eliminates the need for domain knowledge.

Modern causal analysis also treats study design as an attempt to emulate a specified experiment, even when the available data are observational. Hernan and Robins call this the target-trial approach: define eligibility, treatment strategies, assignment, follow-up, outcome, causal contrast, and analysis before using the observed records [2]. This sequence exposes avoidable errors such as beginning follow-up at different times for treated and untreated units, conditioning eligibility on future information, or comparing treatment initiators with a control group that was never eligible to initiate. The target trial is not evidence that randomization occurred. It is a protocol for making the intended causal comparison explicit and for locating where observational data depart from the experiment one would prefer to run [2].

## Core Concepts

### Start with the causal question and estimand

A causal analysis must specify the units, treatment strategies, comparison, outcome, follow-up time, and target population before selecting an estimator [2]. "Does X cause Y?" is usually underspecified. Changing a drug dose, offering insurance, receiving insurance, and adhering to treatment are different interventions; mortality at 30 days and quality of life at five years are different outcomes. The estimand is the exact contrast the study seeks, such as the average treatment effect (ATE), the average treatment effect among the treated (ATT), or an effect for a subgroup whose treatment changes in response to an instrument [2][7].

For a binary treatment A, let Y(1) be the outcome a unit would have under treatment and Y(0) the outcome under control. The individual effect is Y(1)-Y(0), but only one potential outcome is observed for each unit [1]. Population averages, such as E[Y(1)-Y(0)], can nevertheless be identified under a suitable design and assumptions. The observed-data estimator is not the estimand itself: an estimator may be unbiased for one target under one assignment mechanism and misleading for another target or population.

Consistency links the observed outcome to the potential outcome under the treatment actually received. It also requires treatment versions to be defined closely enough that the notation is meaningful [2]. If "treatment" combines incompatible doses, delivery channels, or adherence patterns with different effects, Y(1) is ambiguous. The usual no-interference condition similarly requires one unit's outcome not to depend on other units' treatment, unless spillovers are explicitly included in the estimand and design [2]. Vaccination, networks, classrooms, and markets often make interference a substantive issue rather than a technical footnote.

### Identification is distinct from estimation

Identification asks whether the causal estimand is uniquely determined by the observed-data distribution under stated assumptions. Estimation asks how to approximate that identified quantity from finite data [2][5]. This distinction prevents a common category error: a precise estimate with a narrow confidence interval can still target the wrong causal quantity because of confounding, selection, measurement error, or a failed structural assumption. Conversely, a valid design can identify an effect but estimate it imprecisely when the sample is small or treatment variation is weak.

In a randomized experiment, the known assignment mechanism supplies exchangeability by design for the assigned treatment [1][2]. In an observational study, conditional exchangeability assumes that, within levels of sufficient measured pre-treatment covariates L, treatment assignment is independent of the relevant potential outcomes. Positivity requires every treatment being compared to have positive probability in each covariate stratum needed for the comparison. Consistency links potential and observed outcomes [2]. Together these conditions can identify average causal effects, but they are not all empirically testable. Investigators must defend them using design knowledge, timing, measurement, and subject-matter reasoning.

Conditioning on more variables is not automatically safer. Pre-treatment common causes of treatment and outcome may need adjustment, but controlling for a collider can create an association that was absent, and controlling for a mediator can remove part of the total effect [2][4]. Post-treatment variables are especially hazardous because treatment may cause them. Variable selection for causal inference therefore differs from feature selection for prediction: predictive importance does not determine whether adjustment removes or creates bias.

### Propensity scores and overlap

The propensity score e(L)=P(A=1|L) summarizes treatment assignment using measured pre-treatment covariates [3]. Rosenbaum and Rubin showed that it is a balancing score: conditional on the true propensity score, the distribution of measured L is the same in treated and control groups under the relevant setup [3]. Matching seeks treated and untreated units with similar scores; stratification compares outcomes within score ranges; inverse-probability weighting creates a weighted pseudo-population in which treatment is independent of measured L under correct specification and positivity [2][3].

Three limitations are essential. First, balance concerns measured covariates, not unknown or omitted causes [2]. Second, extreme scores create unstable weights and reveal weak overlap; the target population or estimand may need to be changed rather than extrapolated beyond the data [2]. Third, a fitted score is a model, so investigators must inspect covariate balance and weight behavior rather than treating model convergence as validation. A propensity-score method can reduce measured confounding while leaving the causal conclusion dependent on an untestable no-unmeasured-confounding assumption.

### Causal graphs, interventions, and adjustment

A causal DAG encodes proposed direct causal relationships among variables. Under a causal Markov interpretation, d-separation connects graphical structure to conditional independence; the graph can then reveal open noncausal paths, colliders, mediators, and candidate adjustment sets [2][4]. The graph is not learned from correlations alone unless additional assumptions are imposed. Its arrows represent substantive claims, so omitted variables or incorrect directions can invalidate the resulting adjustment strategy.

Pearl's do-operator distinguishes P(Y|X=x), an observational conditional distribution, from P(Y|do(X=x)), the distribution under an intervention that sets X and replaces its usual generating mechanism [4][5]. A set Z meeting the back-door criterion blocks every relevant path entering X and contains no descendant of X; adjustment for Z can then identify the intervention distribution under the graph. The front-door criterion can identify some effects despite unmeasured exposure-outcome confounding when a measured mediator and its relations satisfy stronger graphical conditions [4]. These criteria are sufficient in their applicable settings, not evidence that the assumed graph is true.

Do-calculus provides three transformation rules for interventional distributions. Huang and Valtorta proved that the rules are complete for the identification problem they study: if a causal effect is identifiable in the specified causal Bayesian-network setting, a sequence of do-calculus transformations can express it in observational quantities [5]. Completeness is conditional on the model class and graph. It does not say every causal effect is identifiable, that the graph can be verified from the same data, or that a finite-sample estimator will perform well.

### Association, intervention, and counterfactual questions

Pearl's causal hierarchy distinguishes associational questions about seeing, interventional questions about doing, and counterfactual questions about what would have happened to a particular unit under a different action [6]. Moving upward requires information or assumptions not contained in an observational joint distribution alone. A predictive model can estimate P(Y|X) accurately while failing to estimate P(Y|do(X=x)); a model of average intervention effects can still be insufficient for an individual retrospective counterfactual [6].

This hierarchy should not be read as saying that all statistics or machine learning is confined to association. Causal estimators can use regression and machine learning as components, but those algorithms inherit identification from the design and assumptions around them [2][6]. Flexible nuisance-function estimation may reduce model misspecification while leaving confounding, positivity, measurement, and transportability problems untouched.

### Quasi-experimental identification strategies

Instrumental variables use a variable Z that shifts treatment but is otherwise suitably unrelated to potential outcomes. A standard interpretation requires instrument relevance, an independence or as-if-random condition, an exclusion restriction ruling out direct paths from Z to the outcome outside treatment, and usually monotonicity for the local average treatment effect interpretation [7]. Under heterogeneous effects, the resulting estimand commonly applies to compliers whose treatment changes with the instrument, not automatically to the whole population [7][17]. Exclusion and monotonicity are substantive assumptions, not consequences of a strong first-stage regression.

Difference-in-differences compares outcome changes over time between treated and comparison groups. Its central counterfactual assumption is parallel trends: absent treatment, the groups' average untreated outcomes would have changed similarly over the study period [10][11]. The method can allow stable level differences, but it does not automatically remove time-varying confounding. With staggered adoption and heterogeneous effects, conventional two-way fixed-effects regressions can combine invalid comparisons or contaminate event-time coefficients; group-time methods and cohort-specific estimators were developed to address these failures under generalized parallel-trends assumptions [11][12].

Regression discontinuity uses a treatment rule that changes at a cutoff. In a sharp design, a discontinuity in expected outcomes at the threshold can identify a local effect when potential-outcome regression functions are continuous at the cutoff; fuzzy designs use the discontinuity in treatment probability and have an instrumental-variable interpretation [13]. The result is local to units near the threshold. Sorting or manipulation, other policies changing at the same cutoff, bandwidth choice, and functional-form sensitivity can undermine the design [13]. Units just above and below a cutoff are not literally randomized merely because a threshold exists.

### Diagnostics do not prove the assumptions

Balance checks, placebo outcomes, negative controls, density tests near an RD cutoff, and pre-treatment trend plots can expose certain failures. They cannot prove the absence of unmeasured confounding or establish a counterfactual trend that is never observed [2][11][13]. Sensitivity analysis is therefore part of causal reasoning: it asks how strong an unmeasured bias or assumption violation would have to be to change the conclusion. Robustness across methods is most informative when the methods fail for different reasons, not when they repeat the same identifying assumption in different software.

## The Rubin-Pearl Complementarity

Potential outcomes and structural causal models emphasize different stages of a causal analysis. Potential-outcome notation begins with contrasts such as E[Y(1)-Y(0)] and forces the analyst to define treatment versions, populations, and estimands. It aligns naturally with randomized assignment, matching, weighting, instrumental variables, and design-based analyses [2][4]. A statement such as "the ATT" is incomplete until the treatment, outcome horizon, and treated population are specified, but once specified the notation makes the target explicit.

A structural causal model begins with causal mechanisms and their graphical relationships. It is strong at displaying which variables are common causes, mediators, colliders, or descendants; at distinguishing observation from intervention; and at deriving identification in systems with multiple pathways [4][5]. The graph makes structural commitments visible. That visibility is an advantage only when the analyst treats arrows and omissions as assumptions to defend rather than as facts inferred from visual neatness.

The two languages often describe equivalent identification logic. Conditional exchangeability in a potential-outcomes analysis corresponds, in an appropriate graph, to blocking noncausal paths with a valid pre-treatment adjustment set [2][4]. An IV analysis can be expressed with potential outcomes and compliance types or with a graph containing an instrument, treatment, outcome, and excluded paths [7]. Neither translation removes the substantive content of exclusion, no unmeasured confounding, or positivity.

Their combination supplies a useful division of labor. First define the intervention and estimand in potential-outcome language. Then use a graph to state structural knowledge, check whether the proposed adjustment set opens or closes paths, and determine whether the target is identified. Finally select an estimator appropriate to the design, overlap, treatment timing, and data structure [2][4]. The author's synthesis is that disagreement between frameworks is often diagnostically useful: if a target is easy to write but its graph requires implausible missing arrows, or if a graph is elegant but the intervention is not well defined, the causal question needs revision before estimation.

## Evidence

Randomized trials provide the clearest evidence when assignment, adherence, measurement, and follow-up are handled correctly. The 1954 Salk polio vaccine field trial illustrates both the strength of randomization and the importance of reading the actual design. It was not one uniform randomized trial: 623,972 schoolchildren received vaccine or placebo, more than one million others served as observed controls, 84 areas in 11 states used a randomized blinded vaccine-placebo design, and 127 areas in 33 states used an observed-control design [14]. The evaluation reported 80-90% effectiveness against paralytic poliomyelitis, while the dual protocol exposed why selection and lack of blinding make observed controls weaker than randomized placebo controls [14]. The case supports randomization, but it also warns against describing all enrolled children as randomized.

The Oregon Health Insurance Experiment shows how randomization, noncompliance, and instrumental variables can interact. Oregon used lottery drawings from a waiting list to allocate the opportunity to apply for Medicaid. About two years later, the clinical-outcomes study analyzed 6,387 adults selected in the lottery and 5,842 not selected; lottery selection increased Medicaid coverage by 24.1 percentage points rather than determining coverage perfectly [15]. The investigators therefore used lottery selection as an instrument for coverage and explicitly assumed that selection affected outcomes only through Medicaid enrollment [15]. Coverage increased health-care use, diabetes detection and management, reduced depression, and reduced financial strain, but it did not produce statistically significant improvements in measured blood pressure, cholesterol, or glycated hemoglobin during the first two years [15]. The study also limited generalization to low-income, able-bodied, uninsured adults who entered the lottery and noted that longer-run effects could differ [15].

The Women's Health Initiative demonstrates why a randomized estimate must name the intervention. The combined-hormone trial randomized 16,608 postmenopausal women with an intact uterus to conjugated equine estrogen plus medroxyprogesterone acetate or placebo [16]. After an average 5.2 years, the trial stopped early because the overall risk-benefit profile was unfavorable. For this regimen and population, the reported hazard ratio for coronary heart disease was 1.29, and the absolute excesses included 7 additional coronary events per 10,000 person-years; fractures and colorectal cancer moved in the beneficial direction, while all-cause mortality was not significantly changed [16]. The correct inference concerns this combined regimen in the studied women. It does not justify the blanket statement that every form of hormone therapy has the same cardiovascular effect.

The Vietnam-era draft lottery is a canonical instrumental-variable design. Angrist used randomly assigned draft-eligibility risk to instrument for military service and reported that, in the early 1980s, white Vietnam veterans in the studied cohorts earned about 15% less than comparable nonveterans [8]. The design did not make military service random: draft eligibility shifted the probability of service. Its causal interpretation therefore depended on IV assumptions, including the absence of pathways from lottery assignment to earnings other than through service, and the estimand need not equal the population-wide ATE when effects are heterogeneous [7][8]. The official 2021 Nobel background emphasizes this local interpretation: under the relevant assumptions, natural-experiment IV methods identify effects for people whose participation changes because of the instrument [17].

Instrument strength is a separate issue from instrument validity. Bound, Jaeger, and Baker showed that when instruments explain little variation in the endogenous treatment, small correlations between instruments and structural errors can cause large inconsistency; in finite samples, IV bias can approach OLS bias as the first-stage relationship weakens [9]. They recommended reporting first-stage diagnostics such as partial R-squared and the F statistic [9]. A large data set does not neutralize a weak first stage, and a strong first stage does not prove the exclusion restriction.

Card and Krueger's New Jersey-Pennsylvania minimum-wage study illustrates both the appeal and limits of difference-in-differences. They surveyed 410 fast-food restaurants before and after New Jersey raised its minimum wage from $4.25 to $5.05 while Pennsylvania's did not change, and reported no indication that the increase reduced employment in their sample [10]. The causal reading requires the counterfactual that, absent the policy, employment in the treated New Jersey restaurants would have followed the comparison trend. The study's result is an empirical finding for that design and period, not proof that minimum wages can never affect employment. Modern DiD work further shows that multiple periods, staggered timing, and heterogeneous effects require care beyond a single two-group comparison [11][12].

Callaway and Sant'Anna identify group-time treatment effects under generalized parallel-trends assumptions and provide outcome-regression, inverse-probability-weighting, and doubly robust estimands for staggered designs [11]. Sun and Abraham show that conventional event-study coefficients can be contaminated by effects from other relative periods when adoption timing and effects vary, and that apparent pre-trends can arise from treatment-effect heterogeneity [12]. These results correct the older blanket claim that a standard two-way fixed-effects DiD regression is reliable whenever a graph of pre-period coefficients looks flat.

Regression discontinuity supplies another form of local evidence. Imbens and Lemieux explain that sharp RD identifies an effect at the cutoff through the discontinuity in expected outcomes when the relevant potential-outcome functions are continuous there; fuzzy RD uses the ratio of outcome and treatment-probability discontinuities [13]. The design invites concrete diagnostics, including covariate discontinuities, density behavior, bandwidth sensitivity, and alternative specifications [13]. Those diagnostics are evidence about the design, not a license to call all threshold comparisons randomized.

Across these examples, the recurring empirical pattern is conditional validity. Randomization identifies effects of assignment under preserved follow-up and measurement; IV identifies a local effect under relevance, independence, exclusion, and monotonicity; DiD identifies effects under no anticipation and parallel untreated trends; RD identifies local effects under continuity or a defensible local-randomization formulation [2][7][11][13]. The methods are powerful because their assumptions are specific enough to criticize.

## Implications

For researchers, the first practical implication is to design backward from the estimand. State the treatment strategies, outcome horizon, target population, and effect measure before choosing regression, matching, weighting, or machine learning [2]. Draw a causal graph using knowledge that precedes outcome analysis, identify which variables are pre-treatment common causes, and explain why each adjustment variable is included [2][4]. Report what variation identifies the effect: randomized assignment, measured conditional exchangeability, an instrument, a policy-time contrast, or a threshold. A table of coefficients is not a design.

The second implication is to separate identification claims from statistical precision. Confidence intervals quantify sampling uncertainty under a model; they do not include bias from an invalid exclusion restriction, unmeasured confounding, failed parallel trends, ambiguous treatment versions, or poor transport to the target population [2][7][11]. Analysts should present assumption-specific diagnostics and sensitivity analyses beside effect estimates. Null results also require attention to power and estimand: "no statistically significant effect" is not the same as evidence of zero effect, as the Oregon study's discussion of measured physical outcomes illustrates [15].

For medicine, causal inference protects treatment decisions from being based on prognostic differences between treated and untreated patients. Randomized assignment is especially valuable because patients selected for treatment can differ in health, access, and behavior before treatment begins [1][2]. Yet the WHI and Oregon examples show why treatment and population definitions matter. The combined estrogen-progestin result cannot be generalized without qualification to every hormone regimen [16], and the Oregon estimates apply to a specific low-income population over a limited follow-up period [15]. Clinical decisions require both internal validity and transportability.

For public policy, natural experiments can turn lotteries, eligibility rules, and phased policy changes into credible comparisons when their institutional details support the assumptions [17]. The design must still distinguish an offer from receipt, local from population-wide effects, and short-run from long-run outcomes. In Oregon, lottery selection was an encouragement rather than compulsory enrollment [15]. In an IV policy study, the effect for compliers can be decision-relevant, but it should not be presented as the effect on always-takers, never-takers, or every eligible person [7][17].

For business and investing, the author's synthesis is that causal reasoning is most useful when it tests an operating mechanism rather than decorates a correlation. Customer retention may correlate with product usage because usage creates value, because satisfied customers use the product more, or because both arise from an unmeasured customer trait. A price change can alter demand, customer mix, and measurement at the same time. Cohort comparisons, randomized product tests, threshold rules, and staggered launches can improve evidence, but each inherits the assumptions of its design [2][11][13]. Fundamental analysis should therefore ask which action changes cash flows, through which mechanism, over what horizon, and for which customers or assets. That is an interpretation built from the causal framework, not a claim that a particular financial ratio identifies causation.

For machine learning, prediction and intervention are different objectives. A model trained to minimize forecast error estimates patterns in the observed environment; deploying a policy can change the distribution that generated those patterns [6]. Causal machine-learning methods can flexibly estimate nuisance functions or heterogeneous effects, but they do not manufacture overlap, define the intervention, or justify exchangeability [2][6]. High-dimensional adjustment is particularly dangerous when variables are selected only by predictive association, because colliders and post-treatment variables can be highly predictive while biasing a causal estimate [2][4].

For everyday reasoning, causal inference supplies a disciplined question set. What exactly is the intervention? What comparison represents the unobserved alternative? Why are the compared groups exchangeable, or what design makes them approximately so? Could selection, reverse causation, measurement, interference, or a common cause explain the pattern? Does the estimate apply locally or to the target population? These questions do not guarantee an answer, but they prevent association from being smuggled into a causal conclusion.

Effect heterogeneity and transportability require their own analysis. An internally valid average can conceal different effects across baseline risk, geography, institutions, adherence, or time. Subgroup estimation is not automatically credible: repeated searches create multiplicity problems, and data-driven subgroups may be too small or poorly supported. The causal target should therefore state whether it is a sample effect, a complier effect, an effect at a threshold, or an effect transported to another population [2][7][13]. Transport requires evidence that the effect modifiers and treatment implementation in the target are sufficiently represented or modeled. The Oregon investigators, for example, explicitly limited generalization because lottery entrants and the duration of coverage differed from other Medicaid populations and longer exposure [15].

Measurement and missingness belong inside the causal model rather than after it. Misclassified treatment can mix distinct interventions; outcome measurement that differs by treatment can create an apparent effect; selective attrition can break the comparability created by random assignment; and spillovers can make one unit's treatment part of another unit's exposure [2]. Investigators should specify when variables are measured, why data are missing, whether loss to follow-up depends on prognosis, and whether interference is plausible. These questions may change the estimand or require weighting, sensitivity bounds, cluster-level designs, or explicit network effects. No statistical adjustment can recover information that the design never recorded without adding assumptions.

A practical review can be organized in six steps. First, define the estimand. Second, map the assignment or data-generating process. Third, state the identifying assumptions in words and, where useful, in a graph. Fourth, examine overlap, balance, timing, attrition, and measurement. Fifth, estimate with methods appropriate to the design and report diagnostics. Sixth, test sensitivity and limit the conclusion to the population, treatment version, and horizon actually supported [2][7][11][13]. The author's assessment is that this sequence is more durable than choosing a favored method first, because it exposes the single worst failure: a precise answer to a causal question the data never identified.

## Sources

1. Holland, P. W. (1986). "Statistics and Causal Inference." Journal of
   the American Statistical Association, 81(396), 945-960.
   https://www.cs.columbia.edu/~blei/fogm/2019F/readings/Holland1986.pdf [high]

2. Hernan, M. A. & Robins, J. M. (2020; updated 2025). "Causal
   Inference: What If." Chapman & Hall/CRC.
   https://miguelhernan.org/whatifbook [high]

3. Rosenbaum, P. R. & Rubin, D. B. (1983). "The Central Role of the
   Propensity Score in Observational Studies for Causal Effects."
   Biometrika, 70(1), 41-55.
   https://doi.org/10.1093/biomet/70.1.41 [high]

4. Imbens, G. W. (2020). "Potential Outcome and Directed Acyclic Graph
   Approaches to Causality: Relevance for Empirical Practice in
   Economics." Journal of Economic Literature, 58(4), 1129-1179.
   https://arxiv.org/abs/1907.07271 [high]

5. Huang, Y. & Valtorta, M. (2006). "Pearl's Calculus of Intervention Is
   Complete." Proceedings of the Twenty-Second Conference on Uncertainty
   in Artificial Intelligence, 217-224.
   https://arxiv.org/abs/1206.6831 [high]

6. Pearl, J. (2019). "The Seven Tools of Causal Inference, with
   Reflections on Machine Learning." Communications of the ACM, 62(3),
   54-60. https://doi.org/10.1145/3241036 [high]

7. Imbens, G. W. (2014). "Instrumental Variables: An Econometrician's
   Perspective." Statistical Science, 29(3), 323-358.
   https://doi.org/10.1214/14-STS480 [high]

8. Angrist, J. D. (1990). "Lifetime Earnings and the Vietnam Era Draft
   Lottery: Evidence from Social Security Administrative Records."
   American Economic Review, 80(3), 313-336.
   https://www.jstor.org/stable/2006669 [high]

9. Bound, J., Jaeger, D. A., & Baker, R. M. (1995). "Problems with
   Instrumental Variables Estimation When the Correlation Between the
   Instruments and the Endogenous Explanatory Variable Is Weak."
   Journal of the American Statistical Association, 90(430), 443-450.
   https://doi.org/10.1080/01621459.1995.10476536 [high]

10. Card, D. & Krueger, A. B. (1994). "Minimum Wages and Employment: A
    Case Study of the Fast-Food Industry in New Jersey and Pennsylvania."
    American Economic Review, 84(4), 772-793.
    https://davidcard.berkeley.edu/papers/njmin-aer.pdf [high]

11. Callaway, B. & Sant'Anna, P. H. C. (2021). "Difference-in-Differences
    with Multiple Time Periods." Journal of Econometrics, 225(2), 200-230.
    https://doi.org/10.1016/j.jeconom.2020.12.001 [high]

12. Sun, L. & Abraham, S. (2021). "Estimating Dynamic Treatment Effects
    in Event Studies with Heterogeneous Treatment Effects." Journal of
    Econometrics, 225(2), 175-199.
    https://doi.org/10.1016/j.jeconom.2020.09.006 [high]

13. Imbens, G. W. & Lemieux, T. (2008). "Regression Discontinuity
    Designs: A Guide to Practice." Journal of Econometrics, 142(2),
    615-635. https://doi.org/10.1016/j.jeconom.2007.05.001 [high]

14. Meldrum, M. (1998). "A Calculated Risk: The Salk Polio Vaccine Field
    Trials of 1954." BMJ, 317(7167), 1233-1236.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC1114166 [high]

15. Baicker, K. et al. (2013). "The Oregon Experiment -- Effects of
    Medicaid on Clinical Outcomes." New England Journal of Medicine,
    368, 1713-1722. https://doi.org/10.1056/NEJMsa1212321 [high]

16. Rossouw, J. E. et al. (2002). "Risks and Benefits of Estrogen Plus
    Progestin in Healthy Postmenopausal Women." JAMA, 288(3), 321-333.
    https://doi.org/10.1001/jama.288.3.321 [high]

17. Royal Swedish Academy of Sciences (2021). "Natural Experiments Help
    Answer Important Questions." Popular science background for the
    Prize in Economic Sciences 2021.
    https://www.nobelprize.org/prizes/economic-sciences/2021/popular-information [high]

## See Also

- `library/mathematics-statistics/statistical-inference.md` -- estimation,
  uncertainty, and hypothesis testing used after a causal target is identified.
- `library/mathematics-statistics/probability-theory-fundamentals.md` --
  conditional probability and random variables underlying causal notation.
- `library/probabilistic-thinking-forecasting/bayesian-reasoning.md` --
  belief updating, which answers a different question from intervention effects.
