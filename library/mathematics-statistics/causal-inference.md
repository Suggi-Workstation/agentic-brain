---
name: causal-inference
id: 20260726T220324Z
tier: library-topic
domain: mathematics-statistics
author: Researcher-1
tags: [causal-inference, counterfactuals, directed-acyclic-graphs, rubin-causal-model, pearl, do-calculus, instrumental-variables, randomized-controlled-trials]
links: [library/mathematics-statistics/probability-theory-fundamentals.md, library/mathematics-statistics/statistical-inference.md, library/probabilistic-thinking-forecasting/bayesian-reasoning.md]
---

# Causal Inference -- Why Most Statistical Tools Only Measure Association, Not Causation

Causal inference is the subfield of statistics and methodology that
asks the question standard statistics cannot answer: what would happen
if we intervened in the world? Most statistical tools -- regression,
correlation, machine learning -- measure association, not causation.
They tell us that two things occur together, but not whether one causes
the other. Causal inference provides the conceptual frameworks (the
Rubin causal model, Pearl's structural causal models and do-calculus)
and the practical methods (randomized experiments, instrumental
variables, difference-in-differences, regression discontinuity) that
make it possible to move from "X is correlated with Y" to "X causes Y"
-- the distinction upon which medicine, policy evaluation, and
evidence-based decision-making depend.

## Background

The distinction between correlation and causation is not a recent
discovery. The philosopher David Hume argued in 1748 that causation
cannot be directly observed -- we see only constant conjunction, the
regular succession of events. John Stuart Mill formalized methods of
inductive causal reasoning (the Method of Difference, the Method of
Concomitant Variation) in his 1843 "A System of Logic." But the modern
discipline of causal inference -- as a mathematical and statistical
enterprise -- was born in the 20th century from the convergence of
three intellectual streams.

The first stream is the randomized experiment, pioneered by Ronald A.
Fisher at Rothamsted Experimental Station in the 1920s. Fisher
demonstrated that random assignment of treatments to experimental
units breaks the link between treatment assignment and all confounding
variables -- both measured and unmeasured. Randomization does not
eliminate confounding; it makes confounding statistically ignorable,
allowing the difference in group means to be interpreted as a causal
effect. Fisher's 1935 "The Design of Experiments" established the
randomized controlled trial (RCT) as the gold standard for causal
evidence, a status it retains in medicine, agriculture, and
increasingly in social policy and technology.

The second stream is the potential outcomes framework, formalized by
Donald Rubin in the 1970s but tracing its intellectual roots to Jerzy
Neyman's 1923 work on agricultural experiments and to the statistician
William Cochran. Neyman introduced the idea that each experimental unit
has a potential outcome under treatment and a potential outcome under
control, and that the causal effect is the difference between these two
quantities. Only one of the two potential outcomes is ever observed --
the "fundamental problem of causal inference." Rubin generalized
Neyman's framework beyond randomized experiments to observational
studies, introducing the concept of the propensity score (the
probability of receiving treatment given covariates) and showing that
conditioning on the propensity score can, under certain assumptions,
mimic randomization in observational data. His 1974 paper "Estimating
Causal Effects of Treatments in Randomized and Nonrandomized Studies"
established the potential outcomes framework as one of the two dominant
approaches to causal inference.

The third stream is the structural causal model (SCM) approach,
developed by Judea Pearl beginning in the 1990s and synthesized in his
landmark 2000 book "Causality: Models, Reasoning, and Inference."
Pearl introduced directed acyclic graphs (DAGs) as a visual language
for encoding causal assumptions, the do-operator to distinguish
observation from intervention, and do-calculus -- a set of three rules
for determining whether causal effects can be estimated from
observational data given a causal graph. Pearl also articulated the
Ladder of Causation, a three-level hierarchy: association (seeing),
intervention (doing), and counterfactual (imagining). Each level
requires strictly more information than the one below it. Standard
statistics and machine learning operate entirely at the first level;
answering causal questions requires climbing to the second or third.

These three frameworks -- Fisher's randomization, Rubin's potential
outcomes, Pearl's DAGs and do-calculus -- are not competitors. They are
complementary tools. The potential outcomes framework defines the
estimand (what we want to estimate) with precision. Pearl's DAGs make
causal assumptions transparent and provide graphical criteria for
determining which variables to condition on. Randomization provides the
cleanest path from data to estimand. Together, they constitute the
modern discipline of causal inference.

## Core Concepts

### The Fundamental Problem of Causal Inference

Every causal question is, at bottom, a missing-data problem. For any
individual unit i, let Y_i(1) denote the outcome if the unit receives
treatment and Y_i(0) denote the outcome if the unit receives control.
The causal effect for unit i is the difference: Y_i(1) - Y_i(0). But we
can never observe both Y_i(1) and Y_i(0) for the same unit at the same
time. If the unit receives treatment, we observe Y_i(1) but Y_i(0) is
counterfactual -- it is what would have happened but did not. If the
unit receives control, we observe Y_i(0) but Y_i(1) is the missing
value. This is the fundamental problem of causal inference, identified
by Paul Holland in 1986.

Because individual causal effects are unobservable, causal inference
shifts its target to average causal effects: the average treatment
effect (ATE), the average treatment effect on the treated (ATT), or
other aggregate estimands. The challenge then becomes: under what
conditions can we estimate these averages from observed data? The
answer depends on the assignment mechanism -- how units came to receive
treatment or control. If treatment is randomly assigned, the two groups
are comparable in expectation, and the simple difference in group means
estimates the ATE. If treatment is not random -- as in most
observational studies -- selection bias contaminates the comparison.
The treated and control groups differ systematically in ways that
affect outcomes, and the observed difference confounds the causal
effect with pre-existing differences.

### The Rubin Causal Model and the Propensity Score

The Rubin causal model formalizes causal inference by making the
assumptions needed to proceed explicit. The key assumption, called
"unconfoundedness" or "ignorability," states that treatment assignment
is independent of potential outcomes conditional on observed
covariates. In notation: (Y_i(0), Y_i(1)) is perpendicular to T_i
given X_i. This means that, after controlling for the observed
covariates X, there are no remaining systematic differences between
treated and control units. Under unconfoundedness, causal effects are
identifiable from observational data.

The propensity score, introduced by Rosenbaum and Rubin in 1983,
dramatically simplifies estimation. The propensity score e(X) is the
probability of receiving treatment given covariates X: e(X) = P(T=1 |
X). Rosenbaum and Rubin proved that if unconfoundedness holds given X,
then it also holds given e(X). This is a dimensionality-reduction
result: instead of conditioning on a potentially high-dimensional
vector of covariates, one need only condition on a single scalar, the
propensity score. This enables matching, stratification, and inverse
probability weighting -- practical methods that estimate causal effects
by comparing treated and control units with similar propensity scores.

Propensity score matching pairs each treated unit with a control unit
that has a similar propensity score. Inverse probability weighting
reweights the data so that the treatment and control groups balance on
the covariates -- treated units with low propensity scores are
up-weighted, control units with high propensity scores are
up-weighted. Both methods rely on the unconfoundedness assumption and
on overlap: for every value of X, there must be both treated and
control units. Violations of overlap (some covariate values always or
never receive treatment) mean the data contain no information about
causal effects for those subpopulations.

### Pearl's Causal Graphs and Do-Calculus

Judea Pearl's framework begins with a structural causal model: a set of
equations describing how each variable is generated from its direct
causes and an exogenous error term. The causal structure is represented
as a directed acyclic graph (DAG) in which nodes are variables and
directed edges represent direct causal relationships. A DAG encodes a
set of conditional independence relations: two variables are
d-separated (conditionally independent) given a set Z if all paths
between them are blocked by Z. This allows the analyst to read off what
can and cannot be learned from observational data about the causal
structure.

The do-operator is Pearl's notation for intervention: P(Y | do(X=x))
represents the probability distribution of Y when X is actively set to
x, breaking any arrows into X from its natural causes. This is
fundamentally different from P(Y | X=x), which conditions on the
observed value of X. In the observational quantity, X is correlated
with its causes, which may also affect Y through backdoor paths. In the
interventional quantity, those backdoor paths are cut. The central
challenge of causal inference in Pearl's framework is: when can
P(Y | do(X=x)) be expressed in terms of observational probabilities,
and how?

The backdoor criterion provides a sufficient condition: a set of
variables Z satisfies the backdoor criterion relative to (X, Y) if Z
blocks every path between X and Y that contains an arrow pointing into
X, and no variable in Z is a descendant of X. If such a Z exists, then
the causal effect of X on Y can be estimated by adjusting for Z. The
front-door criterion provides an alternative when unobserved
confounders prevent the backdoor approach.

Do-calculus is a set of three rules for transforming expressions
involving the do-operator into expressions that can be estimated from
observational data. The rules govern when variables can be added to or
removed from conditioning sets, and when do-operators can be inserted
or removed. Together, the rules are complete: Pearl proved that if a
causal effect is identifiable from observational data given a causal
graph, do-calculus can derive the identifying expression. This
transformed causal inference from an art of clever study design into a
calculus with formal rules.

### Pearl's Ladder of Causation

Pearl organizes causal reasoning into three strictly ordered levels.
Level 1, Association, answers questions like P(Y | X) -- what is the
probability of Y given that I observe X? This is the domain of standard
statistics and machine learning. Regression, classification, clustering
all operate at this level. Level 1 requires only observational data and
makes no causal claims.

Level 2, Intervention, answers questions like P(Y | do(X=x)) -- what
is the probability of Y if I actively set X to x, regardless of what X
would have been naturally? This is the domain of experiments and policy
evaluation. Answering Level 2 questions requires causal assumptions
encoded in a DAG, plus data. Randomized experiments answer Level 2
questions directly; observational studies require identification
strategies like the backdoor criterion, instrumental variables, or
front-door adjustment.

Level 3, Counterfactuals, answers questions like P(Y_x = y | X = x',
Y = y') -- given that I observed X = x' and Y = y' for this specific
individual, what would Y have been if X had been x instead? This is the
domain of attribution, blame, and individual-level reasoning.
Counterfactual questions require the full structural causal model --
not just the DAG but the functional equations. Two SCMs can agree on
all interventional distributions but differ in their counterfactual
implications. The hierarchy is strict: Level 1 information alone cannot
answer Level 2 questions without additional assumptions; Level 2
information alone cannot answer Level 3 questions without the full SCM.

### Key Observational Methods

When randomized experiments are infeasible -- too expensive, unethical,
or impractical -- causal inference relies on quasi-experimental methods
that exploit naturally occurring variation that approximates
randomization.

Instrumental variables (IV) exploit a variable Z that affects the
treatment X but has no direct effect on the outcome Y except through X.
If such a variable exists, it can be used to estimate the causal effect
of X on Y even in the presence of unobserved confounders. The canonical
example is Angrist's (1990) use of the Vietnam draft lottery (Z) as an
instrument for military service (X) to estimate the causal effect of
military service on subsequent earnings (Y). The lottery was random, so
it is independent of confounders, and it affects earnings only through
its effect on military service. IV estimates the local average
treatment effect (LATE) -- the causal effect for compliers, those whose
treatment status changes in response to the instrument. This is not
necessarily the same as the average treatment effect for the entire
population, limiting generalizability.

Difference-in-differences (DiD) compares the change in outcomes over
time between a treatment group and a control group. The identifying
assumption is parallel trends: in the absence of treatment, the
treatment and control groups would have followed parallel trajectories.
DiD removes both time-invariant differences between groups and
time-varying factors that affect both groups equally. Card and
Krueger's 1994 study of the minimum wage used DiD: they compared
employment changes in New Jersey (which raised its minimum wage) to
Pennsylvania (which did not), finding no disemployment effect --
contrary to standard economic theory.

Regression discontinuity design (RDD) exploits a threshold or cutoff
that determines treatment assignment. Units just above and just below
the threshold are effectively randomly assigned -- their exact position
relative to the cutoff is as-if random. Comparing outcomes for units
immediately on either side of the threshold yields a causal estimate
local to the cutoff. RDD is considered the strongest quasi-experimental
design because its assumptions are transparent and often testable. It
has been used to estimate the effect of class size on test scores
(Angrist and Lavy, 1999, exploiting Maimonides' rule), the effect of
incumbency on election outcomes, and the effect of financial aid on
college enrollment.

## The Rubin-Pearl Complementarity

The relationship between the Rubin causal model (potential outcomes)
and Pearl's SCM framework is often characterized as a rivalry. The
author's assessment is that this characterization is misleading. The
two frameworks are complementary, not competing. They address the same
underlying problem with different notation and emphasis.

In the potential outcomes framework, the analyst specifies the
estimand -- the causal quantity to be estimated -- with precision. The
notation forces clarity about whether the target is ATE, ATT, LATE, or
some other quantity. The emphasis is on the assignment mechanism and
the conditions (unconfoundedness, overlap) required for identification.
The framework is particularly well-suited to the design-based approach
that dominates empirical economics and political science, where the
analyst starts with a clear question and designs a study to answer it.

In Pearl's SCM framework, the analyst encodes causal assumptions in a
graphical model and uses graphical criteria (backdoor, front-door) and
do-calculus to determine whether and how the causal effect can be
estimated. The emphasis is on making assumptions transparent and on
deriving identification conditions algorithmically. The framework is
particularly well-suited to complex causal systems with many variables
and to questions about mediation, transportability, and data fusion.

The backdoor criterion in Pearl's framework corresponds to the
condition that the set of covariates Z renders treatment assignment
ignorable in the potential outcomes framework. Pearl's do-calculus
provides an algorithmic way to determine whether there exists any set
of observed variables that satisfies the backdoor criterion, while the
potential outcomes approach typically relies on the analyst's judgment
to select conditioning variables. The DAG makes assumptions visible and
testable; the potential outcomes estimand makes the target precise.

## Evidence

The empirical track record of causal inference methods provides strong
evidence for their validity -- when assumptions hold. The RCT remains
the single most reliable tool for establishing causality. The Salk
polio vaccine trial of 1954, which randomized over 400,000 children and
demonstrated 80-90% efficacy, established the RCT as the standard of
evidence in medicine. More recently, the Oregon Health Insurance
Experiment (2008) used a lottery to randomly assign Medicaid coverage
to low-income adults, providing the first rigorous causal evidence on
the effects of health insurance. The experiment found that Medicaid
increased health care utilization, reduced financial strain, and
reduced depression, but did not produce statistically significant
improvements in physical health measures in the first two years --
findings that shaped the Affordable Care Act debate.

The instrumental variables approach has a mixed but instructive track
record. The Vietnam draft lottery study (Angrist, 1990) estimated that
military service reduced civilian earnings by approximately 15% for
white veterans in the 1980s -- a finding that withstood scrutiny
because the instrument (draft lottery number) was demonstrably random
and strongly predictive of service. Conversely, the weak instruments
problem has produced cautionary tales: when the instrument is only
weakly correlated with the treatment, IV estimates become unreliable,
with inflated standard errors and bias toward the ordinary least
squares estimate. Bound, Jaeger, and Baker (1995) demonstrated that
weak instruments can produce IV estimates more biased than the naive
OLS estimate they were intended to correct.

The difference-in-differences method has been validated through
"placebo tests" -- applying the method to outcomes or time periods
where no treatment effect should exist. Card and Krueger's minimum wage
study passed such tests, and replications across different contexts
have confirmed DiD's reliability when parallel trends hold. However,
recent methodological work has highlighted that the standard two-way
fixed effects DiD estimator can produce misleading results when
treatment timing varies across units, because it compares
newly-treated units to already-treated units as controls. New
estimators (Callaway and Sant'Anna, 2021; Sun and Abraham, 2021) have
been developed to address this problem, demonstrating that causal
inference methods themselves evolve through critical scrutiny.

The 2021 Nobel Prize in Economics was awarded to David Card, Joshua
Angrist, and Guido Imbens for their methodological contributions to
causal inference from natural experiments. Card's work on minimum wage,
immigration, and education demonstrated that natural experiments could
answer questions previously thought intractable. Angrist and Imbens
developed the theoretical framework for IV estimation -- clarifying
what IV estimates (LATE), under what conditions, and with what
limitations. The Nobel committee's citation explicitly credited these
researchers with the "credibility revolution" in empirical economics:
the shift from estimating associative models with long lists of control
variables to designing studies that exploit exogenous variation to
identify causal effects.

The replication crisis in social psychology indirectly validates the
importance of causal inference methodology. Many celebrated findings --
power posing, priming effects, ego depletion -- were based on
observational or weakly experimental designs that did not adequately
address confounding. When replicated with larger samples, proper
randomization, and pre-registered analysis plans, the effects shrank or
disappeared. The crisis is not evidence against causal inference; it is
evidence for the necessity of rigorous causal inference. Bad causal
inference produces false positives; good causal inference protects
against them.

## Implications

For science and medicine, causal inference is not optional -- it is the
difference between effective treatment and harmful intervention.
Correlation-based medicine produced decades of misguided advice:
hormone replacement therapy was widely prescribed based on
observational studies showing that women taking HRT had lower heart
disease rates. When the Women's Health Initiative RCT tested this in
2002, it found that HRT actually increased heart disease risk. The
observational association was confounded: women who took HRT were
healthier, wealthier, and more health-conscious in ways that
independently reduced heart disease risk. The lesson is not that
observational studies are useless but that observational evidence
without causal reasoning about confounding is actively dangerous.

For policy evaluation, causal inference methods have transformed how
governments assess program effectiveness. The rise of randomized
evaluations in development economics -- championed by Esther Duflo,
Abhijit Banerjee, and Michael Kremer (2019 Nobel laureates) -- replaced
ideological debates about what works with empirical evidence. Does
deworming improve school attendance? Does microcredit reduce poverty?
Does conditional cash transfer improve child health? These questions,
once answered by theory or anecdote, are now answered by randomized
trials, often with surprising results that contradict expert
predictions.

For investing and business decisions, causal inference provides the
conceptual tools to distinguish drivers from correlates. A company's
stock price correlates with many things -- market indices, interest
rates, news sentiment, the CEO's public appearances. But correlation
does not reveal what drives intrinsic value. The value investor's
task -- understanding the causal mechanisms that produce sustainable
earnings -- is fundamentally a causal inference problem. Why does this
company earn high returns on capital? Is it a cause (durable
competitive advantage) or a correlate (temporary industry tailwind)?
Regression-based factor models identify correlations between returns
and characteristics (value, momentum, size), but they do not identify
whether these characteristics cause higher returns or are proxies for
something else. The author's assessment is that causal reasoning about
business models -- asking "why" rather than "what" -- is the
distinguishing cognitive advantage of successful fundamental investors.

For everyday reasoning, causal inference inoculates against one of the
most pervasive cognitive errors: mistaking correlation for causation.
The ubiquity of spurious correlations -- the divorce rate in Maine
correlates with per capita margarine consumption, the number of people
who drowned by falling into a pool correlates with Nicholas Cage film
appearances -- is not just statistical humor. It is a warning. Most
correlations in complex systems are spurious. The disciplined habit of
asking "what is the mechanism?", "what is the confounder?", and "how
would we design an experiment to test this?" -- the habits that causal
inference formalizes -- is one of the highest-leverage thinking skills
a person can develop.

## Sources

1. Pearl, J. & Mackenzie, D. (2018). "The Book of Why: The New Science
   of Cause and Effect." Basic Books. An accessible introduction to
   Pearl's causal revolution, covering the Ladder of Causation, DAGs,
   and do-calculus with historical context. [high]

2. Pearl, J. (2009). "Causality: Models, Reasoning, and Inference"
   (2nd ed.). Cambridge University Press. The definitive technical
   treatment of structural causal models, do-calculus, and graphical
   criteria for causal identification. [high]

3. Imbens, G. W. & Rubin, D. B. (2015). "Causal Inference for
   Statistics, Social, and Biomedical Sciences: An Introduction."
   Cambridge University Press. The comprehensive reference for the
   potential outcomes framework covering randomized experiments,
   propensity scores, matching, IV, and RDD. [high]

4. Angrist, J. D. & Pischke, J.-S. (2009). "Mostly Harmless
   Econometrics: An Empiricist's Companion." Princeton University
   Press. The applied researcher's guide to causal inference with
   natural experiments, covering IV, DiD, RDD, and the credibility
   revolution in economics. [high]

5. Rosenbaum, P. R. & Rubin, D. B. (1983). "The Central Role of the
   Propensity Score in Observational Studies for Causal Effects."
   Biometrika, 70(1), 41-55. The seminal paper introducing propensity
   scores and proving that conditioning on the propensity score is
   sufficient for unbiased estimation under unconfoundedness. [high]

6. Holland, P. W. (1986). "Statistics and Causal Inference." Journal
   of the American Statistical Association, 81(396), 945-960. The paper
   that named the "fundamental problem of causal inference" and
   articulated the Rubin-Holland framework with exceptional clarity.
   [high]

## See Also

- `library/mathematics-statistics/statistical-inference.md` -- the
  broader framework of estimation, hypothesis testing, and confidence
  intervals that causal inference extends from correlation to
  causation.
- `library/mathematics-statistics/probability-theory-fundamentals.md` --
  the axiomatic foundation (Kolmogorov axioms, Bayes' theorem,
  conditional probability) on which all statistical inference,
  including causal inference methods, is built.
- `library/probabilistic-thinking-forecasting/bayesian-reasoning.md` --
  applied Bayesian updating as a thinking discipline, the practical
  counterpart to Bayesian inference that shares causal inference's
  concern with updating beliefs in response to evidence.
