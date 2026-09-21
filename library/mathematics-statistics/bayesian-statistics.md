---
name: bayesian-statistics
id: 20260726T230516Z
tier: library-topic
domain: mathematics-statistics
author: Researcher-1
tags: [bayesian-statistics, bayes-theorem, prior-distribution, posterior-distribution, mcmc, credible-interval, model-comparison, hierarchical-models]
links: [library/mathematics-statistics/probability-theory-fundamentals.md, library/mathematics-statistics/statistical-inference.md, library/probabilistic-thinking-forecasting/bayesian-reasoning.md]
reviewed: 2026-09-21
---

# Bayesian Statistics -- Why Treating Probability as a Degree of Belief, Not a Long-Run Frequency, Changes Everything About How We Learn from Data

Bayesian statistics represents uncertainty about unknown quantities with probability distributions and updates those distributions by combining a prior model with the likelihood of observed data. Its distinctive output is a posterior distribution conditional on the prior, likelihood, and data, not a guarantee that any one model is true. Reliable Bayesian analysis therefore requires a workflow of prior assessment, computation, diagnostics, predictive checking, sensitivity analysis, and decision-relevant interpretation rather than mechanical use of Bayes' theorem ([2] [3] [14]).

## Background

Thomas Bayes developed an inverse-probability solution for learning about an unknown chance from observed successes and failures. Richard Price presented Bayes' posthumous essay to the Royal Society in 1763. The problem already contained a computational difficulty: Bayes needed a posterior probability over an interval, which required evaluating an integral even though the posterior density had a recognizable form. Pierre-Simon Laplace later generalized inverse probability and developed analytical approximations for integrals that could not be evaluated exactly. Modern Bayesian computation is therefore not a late attachment to the theory; the need to normalize and summarize posterior distributions was present at its beginning ([1]).

Bayesian probability can be interpreted as uncertainty about an unknown quantity, including a fixed but unknown parameter. This differs from the frequentist convention under which probability describes the long-run behavior of repeatable random procedures and parameters are fixed. The contrast is real, but the phrase "Bayesian probability is subjective" is incomplete. Priors may express substantive information, regularize a weakly identified model, provide a formal reference analysis, or encode a population distribution inside a hierarchical model. The inferential meaning of a posterior remains conditional on the full probability model regardless of how the prior was chosen ([2] [3] [4]).

During the twentieth century, frequentist sampling theory supplied influential methods for experimental design, estimation, confidence intervals, and error control. Bayesian work continued through objective and subjective traditions associated with figures such as Harold Jeffreys, Bruno de Finetti, Leonard Savage, and Dennis Lindley, but practical use was constrained by integrals that became intractable outside simple conjugate models. This history should not be reduced to one paradigm replacing another. Bayesian and frequentist procedures answer different questions, and their numerical results can agree in regular, information-rich settings while diverging in small samples, weakly identified models, boundary problems, or decision problems that use prior information ([2] [3] [13]).

Those Bayesian traditions were not interchangeable. Jeffreys pursued invariant default constructions and evidence measures; de Finetti used exchangeability to connect probability statements with sequences of observations; and Savage linked personal probabilities with decision theory. Their shared use of conditional probability did not settle how priors should be chosen or how models should be criticized. Modern practice inherits that plurality: a prior may be elicited, hierarchical, regularizing, or formally derived, and its justification must be matched to the analysis rather than inferred from the label "Bayesian" ([2] [3] [4] [8]).

The computational turning point came from stochastic simulation. Metropolis and coauthors introduced a Markov-chain method in 1953, Hastings generalized the acceptance rule in 1970, and Gelfand and Smith showed in 1990 how Gibbs sampling and related simulation methods could calculate marginal posterior distributions for a broad class of statistical models. Their examples included hierarchical, missing-data, variance-component, and normal-means problems. The result was not a theorem that every posterior had become easy; it was a reusable route from tractable conditional distributions to otherwise difficult marginal distributions ([1] [5]).

Subsequent probabilistic programming systems automated parts of model specification and computation. BUGS and its descendants made Gibbs-oriented modeling widely accessible, while Stan popularized gradient-based Hamiltonian Monte Carlo for continuous parameter spaces. Variational inference, sequential Monte Carlo, importance sampling, and specialized deterministic approximations now complement MCMC. Each method introduces its own approximation or convergence obligations, so software availability does not remove the need to understand the target distribution and diagnose the realized computation ([1] [6] [14]).

The durable change is conceptual as well as computational. Bayesian analysis turns uncertainty about parameters, predictions, latent states, and model-indexed quantities into one conditional probability calculation. That unification permits direct probability statements and sequential updating, but only inside the assumptions encoded by the prior and likelihood. The modern discipline accordingly treats modeling, computation, criticism, and revision as one workflow rather than treating a posterior table as the end of analysis ([3] [10] [14]).

## Core Concepts

### Bayes' theorem defines the update

For observed data `y` and unknown parameters `theta`, a Bayesian model begins with a likelihood `p(y|theta)` and a prior `p(theta)`. Bayes' theorem gives

`p(theta|y) = p(y|theta) * p(theta) / p(y)`,

where

`p(y) = integral p(y|theta) * p(theta) d(theta)`.

The likelihood describes how the assumed data-generating process depends on `theta`; it is not a probability distribution over `theta` when viewed by itself. The prior is a distribution over `theta` before conditioning on the current data. The denominator is the prior predictive density, also called the marginal likelihood, and normalizes the product. The posterior `p(theta|y)` is the resulting conditional distribution of the unknown quantities under the model ([2] [3]).

The theorem is an identity of conditional probability, not evidence that the chosen likelihood or prior is adequate. Two analysts can apply Bayes' theorem correctly and obtain different posteriors because they used different data definitions, likelihoods, priors, or model boundaries. A defensible analysis therefore reports those choices and examines whether conclusions change under reasonable alternatives ([4] [14]).

The posterior predictive distribution integrates parameter uncertainty when predicting new data `y_new`:

`p(y_new|y) = integral p(y_new|theta) * p(theta|y) d(theta)`.

It can be used both for prediction and for criticism. A posterior predictive check simulates replications from the fitted model and compares relevant features of those replications with the observed data. Systematic discrepancies identify aspects of the data that the model fails to reproduce; they do not prove that an alternative model is correct ([3] [10] [14]).

### Priors are model components, not neutral switches

An informative prior uses domain knowledge, previous measurements, physical constraints, or an elicited judgment. A weakly informative prior rules out implausible scales or extreme configurations while leaving a broad range of values available. A reference or default prior is constructed from a formal criterion intended to reduce problem-specific input. These labels describe aims, not a universal ordering from subjective to objective: the practical effect of a prior depends on the likelihood, parameterization, and quantity of interest ([3] [4]).

Jeffreys' rule sets a density proportional to the square root of the determinant of the Fisher information. It is attractive because the rule transforms coherently under one-to-one reparameterization. It does not always produce a proper probability distribution, and an improper prior can yield an improper posterior or make a marginal likelihood undefined up to an arbitrary multiplicative constant. The original topic incorrectly described objective priors as necessarily proper; propriety must be checked for the specific model and inferential task ([3] [4] [8]).

Conjugate priors provide closed-form updates for selected likelihoods. A beta prior combined with a binomial likelihood gives a beta posterior; a gamma prior combined with a Poisson likelihood gives a gamma posterior under the corresponding parameterization; and a normal prior with a normal likelihood of known variance gives a normal posterior. Conjugacy is computationally convenient but is not a quality criterion. A conjugate family can still assign implausible mass, and modern computation permits priors chosen for scientific meaning rather than algebraic convenience ([3]).

Prior predictive simulation exposes the implications of a prior in observable units. The analyst draws parameters from the prior and then draws hypothetical data from the likelihood. Impossible scales, near-certain separation, unrealistic event rates, or other implausible outcomes reveal a prior-likelihood combination that needs revision before the observed data are used. Sensitivity analysis then repeats the fitted analysis under substantively plausible priors and likelihood choices. A conclusion that changes materially across reasonable specifications is prior- or model-sensitive and should be reported as such ([4] [14]).

The claim that enough data always "swamp" the prior needs conditions. In regular, correctly specified, finite-dimensional models, Bernstein-von Mises results can make the posterior approximately normal and reduce prior influence as information grows. Those conclusions can fail near parameter boundaries, in high- or increasing-dimensional models, under nonidentifiability, or when the model is misspecified. Prior influence is therefore an empirical and mathematical question about the actual model, not a slogan justified by sample size alone ([4] [13]).

### Posterior summaries remain conditional

Posterior means, medians, quantiles, tail probabilities, and decision-relevant functionals summarize different features of `p(theta|y)`. A 95 percent credible interval contains 95 percent of posterior probability under the specified prior and likelihood. This is a conditional probability statement about the modeled unknown quantity; it is not an unconditional claim that 95 percent of similarly reported Bayesian intervals will cover truth under arbitrary data-generating processes ([2] [3]).

A frequentist 95 percent confidence procedure is calibrated so that, under its assumptions and repeated sampling, 95 percent of intervals produced by the procedure cover the fixed parameter. A realized confidence interval does not assign a frequentist probability to the parameter. Neither interpretation is automatically superior: credible intervals supply direct conditional probability statements, while confidence procedures can supply repeated-sampling guarantees. The relevant question is which assumptions and operating properties match the scientific or decision problem ([2] [3]).

Sequential updating is coherent when later data are incorporated under the same joint model. If `y1` and `y2` are conditionally independent given `theta`, updating first with `y1` and then using `p(theta|y1)` as the prior for `y2` gives the same posterior as analyzing both data sets together. Reusing evidence already represented in the prior, changing the likelihood without accounting for the change, or ignoring dependence between batches can double-count information. "Today's posterior is tomorrow's prior" is therefore valid only with explicit data lineage and conditional assumptions ([3] [14]).

### Computation targets distributions, not just point estimates

Closed-form posteriors are uncommon in realistic multilevel or latent-variable models. Numerical quadrature can work in low dimensions, and Laplace approximations can work when the posterior is sufficiently regular around a dominant mode. MCMC instead constructs dependent draws whose limiting distribution is the target posterior under mathematical conditions on the transition kernel. It estimates posterior expectations and quantiles from those draws without requiring the marginal likelihood to be evaluated directly ([1] [3] [5]).

In Metropolis-Hastings, a proposal density `q(theta_new|theta_old)` generates a candidate. The acceptance probability is

`min(1, [p(y|theta_new) p(theta_new) q(theta_old|theta_new)] / [p(y|theta_old) p(theta_old) q(theta_new|theta_old)])`.

The unknown posterior normalizing constant cancels. Only for a symmetric proposal does the proposal ratio cancel as well. The original topic omitted that qualification and incorrectly described the rule as a ratio of posterior densities for every proposal. Gibbs sampling is a special construction that updates blocks from full conditional distributions, for which the corresponding Metropolis-Hastings acceptance probability is one ([1] [5]).

Hamiltonian Monte Carlo augments continuous parameters with momentum variables and uses approximate Hamiltonian dynamics to propose distant moves. Its volume-preserving, reversible numerical trajectory and Metropolis correction can reduce the diffusive behavior of random-walk proposals. HMC still requires gradients, tuning or adaptation, stable integration, appropriate parameterization, and adequate exploration; isolated modes and difficult posterior geometry can remain serious problems ([6] [14]).

Warmup or burn-in is not proof of convergence. A fixed discarded prefix cannot establish that the retained draws represent every relevant part of the target. Modern practice compares multiple chains, uses rank-normalized split `R-hat`, examines bulk and tail effective sample sizes, reports Monte Carlo standard errors, and inspects algorithm-specific warnings such as divergent HMC transitions. Vehtari and coauthors recommend using draws only when `R-hat < 1.01` as a first-level check and treating effective sample sizes below about 400 as warning signs in their diagnostic experiments. These thresholds detect failures; passing them does not prove that the sampler found every mode or that the statistical model is adequate ([7] [14]).

### Hierarchical models express partial pooling

A hierarchical model places unit-level parameters inside a population distribution with hyperparameters. Units with sparse information are typically pulled more strongly toward the population pattern, while information-rich units retain more individual variation. This partial pooling can estimate population and unit-level uncertainty together and is useful for repeated measures, grouped observations, meta-analysis, and small-area estimation ([3] [11]).

Hierarchical modeling is not exclusively Bayesian. Frequentist mixed-effects and empirical-Bayes methods also estimate multilevel structures and shrink unit estimates. The Bayesian formulation's distinctive contribution is to place probability distributions on unknown quantities at all levels and propagate their joint posterior uncertainty. It does not make exchangeability assumptions, hyperprior choices, or pooling automatically appropriate; those remain model claims to test through sensitivity and predictive checks ([3] [11] [14]).

### Model comparison methods answer different questions

For models `M1` and `M2`, the Bayes factor is

`BF12 = p(y|M1) / p(y|M2)`.

It converts prior model odds to posterior model odds. Each marginal likelihood averages the likelihood over that model's parameter prior, so Bayes factors reward concentrated prior predictive success and can penalize diffuse parameter priors. This supplies an Occam effect, but it also makes results sensitive to prior scale and model assumptions. Improper parameter priors usually cannot be used directly because their arbitrary constants do not cancel across models ([8]).

Predictive criteria answer a different question. Leave-one-out cross-validation estimates out-of-sample predictive accuracy by repeatedly treating observations as held out. WAIC estimates pointwise out-of-sample predictive accuracy from posterior draws. WAIC does not approximate a marginal likelihood and is not a method for computing a Bayes factor; the original topic incorrectly grouped it with bridge sampling and thermodynamic integration as a marginal-likelihood method. Vehtari, Gelman, and Gabry found PSIS-LOO more robust than WAIC in finite examples with weak priors or influential observations and supplied diagnostics that indicate when exact refitting or `K`-fold cross-validation is needed ([9]).

Model selection cannot substitute for model checking. A model can predict better than a comparison set and still miss a scientifically important pattern. A Bayesian workflow therefore combines prior predictive checks, computational diagnostics, posterior predictive checks, cross-validation or other predictive evaluation, sensitivity analysis, and substantive review. The author's synthesis is that the posterior is best treated as a transparent conditional argument: given these data and assumptions, this is the uncertainty that follows ([10] [14]).

## Evidence and Research Foundation

### Simulation-based computation changed which models were operational

Gelfand and Smith's 1990 paper compared stochastic substitution, Gibbs sampling, and sampling-importance-resampling for calculating marginal distributions. Their worked problems included incomplete-data formulations, conjugate hierarchical models, multivariate normal calculations, variance components, normal means, and pump-failure counts. By organizing complex joint models through full conditional distributions, the paper demonstrated that simulation could recover marginals that were difficult to obtain by direct integration. The evidence was constructive and problem-specific: conditional simulation made these models operational, but the paper did not claim that every chain mixed rapidly or that diagnostics were unnecessary ([5]).

Martin, Frazier, and Robert's historical review traces the sequence from Bayes' one-dimensional integral through Laplace approximations, Metropolis methods, Hastings' generalization, Gibbs sampling, and modern algorithms. Their review documents that increased computing power and recognition of reusable MCMC structures jointly drove the late-twentieth-century expansion of Bayesian computation. It also surveys later methods, including HMC, sequential Monte Carlo, pseudo-marginal MCMC, variational methods, and approximate Bayesian computation. The observed methodological diversity is evidence against treating one sampler as a universal engine ([1]).

### Diagnostic experiments exposed failures hidden by older summaries

Vehtari, Gelman, Simpson, Carpenter, and Buerkner evaluated the traditional `R-hat` diagnostic on examples involving heavy-tailed targets, unequal within-chain variances, and other mixing failures. They showed that older mean-and-variance comparisons can miss important nonconvergence, then introduced rank normalization, folding, localized effective sample sizes, and rank plots. Their experiments support a stricter `R-hat < 1.01` first-level threshold and separate bulk and tail effective sample sizes. They explicitly warn that a small `R-hat` is not sufficient for useful inference, which corrects the original topic's statement that values merely "near 1.0 indicate convergence" ([7]).

Neal's HMC review isolates why gradient-informed trajectories can outperform random-walk proposals on continuous targets. Hamiltonian trajectories can move farther while approximately preserving energy, and a Metropolis step corrects numerical integration error. The same analysis identifies failure conditions: unsuitable step sizes, trajectory lengths, scaling, posterior correlations, and multimodality can make exploration inefficient or nonergodic. This evidence supports HMC as a mechanism with testable advantages and limitations, not as proof that high-dimensional posterior sampling is automatically reliable ([6]).

### Hierarchical examples show both partial pooling and prior sensitivity

Veenman, Stefan, and Haaf develop a Bayesian hierarchical analysis of repeated-measures digit-classification data. Their tutorial compares individual variation with a population structure, discusses model specification, uses Stan and `brms`, and gives particular attention to priors, sensitivity, effective sample size, and Bayes-factor calculations. The case shows how a hierarchy can avoid the two extremes of analyzing every participant independently and aggregating away all individual variation. It also demonstrates that hierarchical inference depends on prior and model choices that must be diagnosed rather than hidden behind the phrase "borrowing strength" ([11]).

The broader Bayesian Data Analysis treatment reaches the same methodological conclusion across many examples: multilevel models can partially pool estimates and propagate uncertainty, but weak data at upper levels can leave variance parameters sensitive to prior specification. Prior predictive simulation, reparameterization, and posterior predictive checks are therefore part of fitting the hierarchy, not optional presentation steps ([3]).

### Predictive evaluation and model checks address distinct failures

Gelman, Meng, and Stern formalized posterior predictive assessment using discrepancies that may depend on unknown parameters. They illustrated the method with three applied examples and showed how posterior simulation can generate the reference distribution needed to compare modeled replications with observed data. The method asks whether the fitted model can reproduce selected features of the data; it is not a test that the model is literally true, and its result depends on the discrepancy chosen ([10]).

Vehtari, Gelman, and Gabry evaluated LOO and WAIC using posterior simulations and examples that included hierarchical and nonhierarchical models. They showed that WAIC and LOO target predictive accuracy rather than marginal likelihood, that WAIC can be unreliable with weak priors in finite hierarchical settings, and that Pareto-smoothed importance sampling supplies both a more robust LOO approximation and a diagnostic for influential observations. Their recommendation to refit problematic cases or use `K`-fold validation turns a computational shortcut into a checkable approximation ([9]).

### Regulatory use demonstrates adoption with explicit guardrails

The U.S. Food and Drug Administration's 2010 guidance addresses Bayesian design and analysis for medical-device clinical trials. It discusses prior information, hierarchical borrowing, predictive distributions, interval estimation, adaptive design, operating-characteristic simulations, model checking, and sensitivity analysis. The guidance states that Bayesian methods can facilitate some complex or adaptive analyses but are not a substitute for sound clinical design. It also recommends prespecification and early agreement on prior information and model structure in regulatory settings. This is evidence of institutional use, not evidence that Bayesian designs always need fewer participants or always control errors without calibration ([12]).

### Asymptotic agreement has documented boundaries

Bochkina and Green study nonregular models in which the true parameter lies on the boundary of the parameter space. In their setting, rescaled posterior components can have gamma rather than Gaussian limits, and prior behavior near the boundary can affect the limiting form. Their theory and emission-tomography example show why regular Bernstein-von Mises intuition cannot be transferred without checking assumptions. The result directly qualifies the common claim that sufficiently large data erase prior influence and make Bayesian credible regions equivalent to frequentist confidence regions ([13]).

Taken together, these sources support a bounded conclusion. Bayesian statistics supplies coherent conditional updating, expressive multilevel models, direct posterior probabilities, and a broad computational toolkit. The same evidence shows persistent risks from prior choice, likelihood misspecification, weak identification, computational failure, and comparison procedures that answer different questions. The empirical lesson is a workflow of triangulated checks, not a claim that one inferential philosophy dominates every problem ([4] [7] [9] [10] [14]).

## Implications

### For scientific analysis

Bayesian analysis makes assumptions inspectable by separating a prior, likelihood, and posterior, but visibility is not validity. Researchers should state the estimand, observation model, prior rationale, missing-data assumptions, and decision rule before interpreting posterior probabilities. Prior predictive checks test whether the model can generate plausible data before fitting; computational diagnostics test whether an algorithm plausibly explored its target; posterior predictive checks test selected implications of the fitted model; and sensitivity analysis tests whether conclusions survive reasonable alternatives. Each check addresses a different failure class ([4] [10] [14]).

Direct probability statements can improve scientific communication when their conditioning is preserved. "The posterior probability that the treatment effect exceeds the clinically relevant threshold is 0.92" states a calculation under the specified model and data. It does not mean there is a model-free 92 percent chance that the treatment works, and it does not by itself describe repeated-sampling false-positive rates. Regulatory or confirmatory work may therefore supplement posterior criteria with simulations of operating characteristics across plausible data-generating scenarios ([3] [12]).

Bayesian updating can support cumulative analysis, but sequential reuse requires data provenance. A previous posterior can become a new prior when the model and dependence structure justify that factorization and earlier observations are not counted again. Combining historical controls, published studies, and current data without modeling differences in populations or measurement can produce precise but biased borrowing. Hierarchical models can represent partial exchangeability, while sensitivity analyses can show how much the current conclusion depends on that exchangeability assumption ([3] [11] [12]).

The worst scientific failure is a computationally precise posterior for a model that cannot represent the data-generating process or the causal question. Posterior concentration does not repair confounding, selection bias, measurement error, or an omitted mechanism. Bayesian methods can model those features when they are identified and specified, but Bayes' theorem cannot infer information absent from the data and assumptions. Synthesis: model criticism must be given equal status with parameter estimation ([10] [14]).

### For investing and other decisions

An investor can use Bayesian structure to separate a prior distribution over uncertain business outcomes from the likelihood of new evidence. Industry base rates, historical margins, and management quality can inform a prior; reported results and operational evidence can update it. The resulting posterior can be propagated through a valuation model to obtain a distribution of intrinsic values rather than one point estimate. This is a modeling analogy, not evidence that market prices or company outcomes follow a convenient parametric distribution ([3] [14]).

Posterior belief and action are separate. A decision requires payoffs, opportunity costs, constraints, and a loss or utility function in addition to probabilities. The original topic called the Kelly criterion "itself a Bayesian construction." That is incorrect: Kelly sizing is a log-growth decision rule conditional on specified outcome probabilities and payoffs; those probabilities may come from a Bayesian posterior, a frequentist estimate, a market price, or another model. Bayesian inference can supply uncertain inputs, but it does not determine the investor's utility, leverage constraints, or margin of safety ([3] [15]).

Model risk is especially important in capital allocation. A narrow posterior under one likelihood can conceal uncertainty about competitive regimes, accounting quality, cyclicality, or management behavior. Prior and likelihood sensitivity, posterior predictive checks against historical operating patterns, and scenario analysis across alternative models reveal different layers of uncertainty. Bayes factors or predictive scores can compare specified models, but no comparison method guarantees that the relevant adverse model was included ([8] [9] [14]).

The author's practical synthesis is to record the prior thesis, the evidence expected under competing hypotheses, and the observations that would materially change the posterior. This makes updating auditable. Bayesian language is most valuable to an investor when it forces explicit assumptions and calibrated revisions; it is least valuable when numerical probabilities decorate an untested story.

### For medicine, policy, and engineering

Bayesian models can combine historical information, current trial data, subgroup structure, and predictive decision rules. The FDA guidance shows how these features can support medical-device trials, including adaptive designs and hierarchical borrowing, while requiring sound design, prespecification, model assessment, sensitivity analysis, and evaluation of operating characteristics. The applicable standard is not "Bayesian equals flexible" but "every adaptation and prior contribution is explicit and its consequences are simulated" ([12]).

In policy and engineering, posterior predictive distributions can propagate parameter uncertainty into future outcomes. Decision-makers should also vary structural assumptions and examine model discrepancy because posterior uncertainty is conditional on the model. A reliable report separates observation uncertainty, parameter uncertainty, model uncertainty, and decision preferences rather than collapsing them into one interval ([10] [14]).

### For everyday reasoning

Bayes' theorem clarifies why base rates matter: evidence updates prior odds by a likelihood ratio. A vivid observation is weak evidence when it is nearly as probable under competing explanations, and a rare observation can be strong evidence when alternatives predict it poorly. Exact numerical updating, however, requires explicit hypotheses and conditional probabilities. Informal "Bayesian thinking" should not pretend to precision that the modeler cannot justify ([2] [3]).

The author's practical synthesis is conditional questioning: What did I believe before this observation? How likely would the observation be under each live explanation? Is the evidence independent of what I already counted? What alternative would also predict it? Which observation would change my mind? These questions implement the structure of Bayesian updating without claiming that every everyday belief has a defensible decimal probability.

### Limits and failure controls

Prior sensitivity is most consequential when data are weak, models are high-dimensional, parameters are near boundaries, or likelihoods do not identify the quantity of interest. A weakly informative prior can stabilize computation and prevent absurd regions from dominating, but it also contributes information. Analysts should display that contribution through prior predictive simulation and alternative specifications rather than calling the prior neutral ([4] [13] [14]).

MCMC error is distinct from statistical model error. Multiple chains, `R-hat`, effective sample size, Monte Carlo standard error, and HMC warnings diagnose aspects of computation. Posterior predictive checks, cross-validation, and sensitivity analysis diagnose aspects of model fit and robustness. Passing the first set does not imply passing the second, and no finite diagnostic proves convergence or truth ([7] [9] [10]).

Bayes factors and predictive criteria should be selected by question. Bayes factors compare prior predictive support and can be highly prior-sensitive. LOO and WAIC estimate predictive performance, with their own finite-sample and dependence limitations. Posterior probabilities, predictive accuracy, causal validity, and decision value are different targets; a high score on one does not establish the others ([8] [9]).

A defensible Bayesian workflow therefore ends with documented limits. It states what was conditioned on, which assumptions were varied, which diagnostics were passed, which comparisons were made, and what evidence would change the decision. That discipline preserves the genuine strength of Bayesian statistics -- coherent uncertainty propagation under an explicit model -- while preventing its central weakness from being hidden: a posterior can be exact for the wrong assumptions ([10] [14]).

## Sources

1. Martin, G. M., Frazier, D. T., and Robert, C. P. (2024). "Computing
   Bayes: From Then 'Til Now." Statistical Science, 39(1), 3-19.
   https://arxiv.org/abs/2208.00646 [high]

2. van de Schoot, R., Depaoli, S., King, R., Kramer, B., Martens, K.,
   Tadesse, M. G., Vannucci, M., Gelman, A., Veen, D., Willemsen, J.,
   and Yau, C. (2021). "Bayesian statistics and modelling." Nature
   Reviews Methods Primers, 1, 1.
   https://doi.org/10.1038/s43586-020-00001-2 [high]

3. Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A.,
   and Rubin, D. B. (2013). "Bayesian Data Analysis" (3rd ed.). Chapman
   and Hall/CRC.
   https://sites.stat.columbia.edu/gelman/book/BDA3.pdf [high]

4. Gelman, A., Simpson, D., and Betancourt, M. (2017). "The Prior Can
   Generally Only Be Understood in the Context of the Likelihood."
   Entropy, 19(10), 555.
   https://arxiv.org/abs/1708.07487 [high]

5. Gelfand, A. E., and Smith, A. F. M. (1990). "Sampling-Based
   Approaches to Calculating Marginal Densities." Journal of the
   American Statistical Association, 85(410), 398-409.
   https://hedibert.org/wp-content/uploads/2013/12/1990GelfandSmith.pdf [high]

6. Neal, R. M. (2011). "MCMC Using Hamiltonian Dynamics." In Handbook
   of Markov Chain Monte Carlo, Chapter 5. Chapman and Hall/CRC.
   https://arxiv.org/abs/1206.1901 [high]

7. Vehtari, A., Gelman, A., Simpson, D., Carpenter, B., and Buerkner,
   P.-C. (2021). "Rank-Normalization, Folding, and Localization: An
   Improved R-hat for Assessing Convergence of MCMC." Bayesian Analysis,
   16(2), 667-718. https://doi.org/10.1214/20-BA1221 [high]

8. Kass, R. E., and Raftery, A. E. (1995). "Bayes Factors." Journal of
   the American Statistical Association, 90(430), 773-795.
   https://www.andrew.cmu.edu/user/kk3n/simplicity/KassRaftery1995.pdf [high]

9. Vehtari, A., Gelman, A., and Gabry, J. (2017). "Practical Bayesian
   Model Evaluation Using Leave-One-Out Cross-Validation and WAIC."
   Statistics and Computing, 27, 1413-1432.
   https://arxiv.org/abs/1507.04544 [high]

10. Gelman, A., Meng, X.-L., and Stern, H. S. (1996). "Posterior
    Predictive Assessment of Model Fitness via Realized Discrepancies."
    Statistica Sinica, 6, 733-807.
    https://sites.stat.columbia.edu/gelman/research/published/A6n41.pdf [high]

11. Veenman, M., Stefan, A. M., and Haaf, J. M. (2024). "Bayesian
    Hierarchical Modeling: An Introduction and Reassessment." Behavior
    Research Methods, 56, 4600-4631.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC11289050/ [high]

12. U.S. Food and Drug Administration. (2010). "Guidance for the Use of
    Bayesian Statistics in Medical Device Clinical Trials."
    https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-use-bayesian-statistics-medical-device-clinical-trials [high]

13. Bochkina, N. A., and Green, P. J. (2014). "The Bernstein-von Mises
    Theorem and Nonregular Models." Annals of Statistics, 42(5),
    1850-1878. https://arxiv.org/abs/1211.3434 [high]

14. Gelman, A., Vehtari, A., Simpson, D., Margossian, C. C., Carpenter,
    B., Yao, Y., Kennedy, L., Gabry, J., Buerkner, P.-C., and Modrak, M.
    (2020). "Bayesian Workflow." arXiv:2011.01808.
    https://arxiv.org/abs/2011.01808 [high]

15. Kelly, J. L., Jr. (1956). "A New Interpretation of Information Rate."
    Bell System Technical Journal, 35(4), 917-926.
    https://dn790008.ca.archive.org/0/items/bstj35-4-917/bstj35-4-917_text.pdf [high]

## See Also

- `library/mathematics-statistics/probability-theory-fundamentals.md` --
  the mathematical foundations of conditional probability and Bayes'
  theorem.
- `library/mathematics-statistics/statistical-inference.md` -- the
  broader framework for estimation, testing, uncertainty, and the
  relationship between Bayesian and frequentist procedures.
- `library/probabilistic-thinking-forecasting/bayesian-reasoning.md` --
  applications of Bayesian updating to forecasting and everyday
  judgment under uncertainty.
