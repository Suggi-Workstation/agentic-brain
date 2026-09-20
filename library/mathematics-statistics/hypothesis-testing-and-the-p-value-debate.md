---
name: hypothesis-testing-and-the-p-value-debate
id: 20260920T151308Z
tier: library-topic
domain: mathematics-statistics
author: Librarian
tags: [hypothesis-testing, p-values, statistical-significance, replication-crisis, research-methods, open-science]
links: [library/mathematics-statistics/statistical-inference.md, library/mathematics-statistics/experimental-design.md, library/mathematics-statistics/bayesian-statistics.md, library/mathematics-statistics/causal-inference.md]
---

# Hypothesis Testing and the p-Value Debate -- Reliable Inference Requires More Than a Threshold

A p-value can measure how incompatible observed data are with a specified statistical model, but it cannot by itself establish that a hypothesis is true, an effect is important, or a result will replicate. Reliable inference requires the test to be embedded in sound design, adequate power, effect-size estimation, transparent analysis, and evidence that survives new data. [2][3][5]

## Background

Statistical significance testing did not begin as the single mechanical procedure now often taught under the label null hypothesis significance testing. Ronald Fisher developed significance tests as tools for judging how surprising data were under a null model, and his 1925 book made the methods accessible to experimental scientists. In Fisher's approach, the p-value was a graded measure of discrepancy between data and a null hypothesis rather than the posterior probability that the null was true. The familiar 0.05 level became a convenient convention, not a natural boundary written into probability theory. [1]

Jerzy Neyman and Egon Pearson developed a different framework. Instead of treating a p-value as an evidential index after observing data, they compared a null and an alternative hypothesis through decision rules chosen before the experiment. Their framework introduced long-run Type I and Type II error rates, a prespecified significance level, and statistical power. The objective was not to assign truth probabilities to hypotheses but to control how often a repeated decision procedure would make defined errors. Fisher's evidential logic and the Neyman-Pearson decision logic answer related but distinct questions. [1][3]

Applied practice blended these traditions. Researchers commonly calculate a Fisher-style p-value, compare it with a Neyman-Pearson-style cutoff, and then use the result as a binary claim about an effect. Kennedy-Shaffer describes this as a historically contingent hybrid rather than a coherent theory delivered by any one founder. That history matters because the current ritual combines a continuous discrepancy measure with a decision threshold while often omitting the alternative hypothesis, power calculation, loss function, and repeated-sampling interpretation that would make the decision framework explicit. [1]

The basic calculation is conditional. For a selected test statistic T, a p-value is the probability, under the null model and the assumptions used to obtain its reference distribution, of a result at least as extreme as the observed result. In a one-sided schematic form, `p = P_H0(T(X) >= T(x_obs))`; a two-sided test requires an explicit definition of extremeness. The conditioning direction is from the hypothesis to possible data. It is not `P(H0 | data)`, not the probability that chance alone produced the data, and not the probability that a replication will cross the same threshold. [2][3]

Misinterpretation became consequential because the 0.05 boundary acquired institutional functions. Journals, reviewers, promotion systems, and research narratives often treated results below it as discoveries and results above it as absences. This selection rule can suppress estimates that do not cross the boundary, encourage repeated analysis until one result does, and make two nearly identical estimates appear categorically different when their p-values fall on opposite sides of 0.05. The American Statistical Association's 2016 statement responded with six principles, including that scientific decisions should not rest only on a threshold, full reporting is required, and statistical significance does not measure effect size or importance. [2]

The replication debate exposed the difference between a successful test and reliable knowledge. In 2015 the Open Science Collaboration repeated 100 studies from three psychology journals using high-powered designs and original materials when available. Replication effects averaged about half the original effects, 97% of original studies had statistically significant results, and 36% of replications did. Those figures do not imply that every non-significant replication falsified its original study; they show that a publication record dominated by threshold-crossing original results did not yield equally strong results under new data. [9]

Parallel evidence appeared outside psychology. Camerer and colleagues preregistered high-powered replications of 21 experimental social-science studies published in Nature and Science. Thirteen, or 62%, produced a significant effect in the original direction, while replication effect sizes averaged about half the original effect sizes. In preclinical oncology, Begley and Ellis reported that an industry team confirmed the scientific findings in 6 of 53 deliberately selected landmark papers; they also acknowledged that technical differences and model limitations could contribute to failed validation. These projects differ in sampling, methods, fields, and definitions of success, so they should not be collapsed into one universal replication rate. [10][11][16]

The phrase replication crisis therefore names a bundle of problems rather than proof that one statistical tool caused scientific failure. The National Academies distinguishes reproducibility, obtaining consistent computational results with the same data and procedures, from replicability, obtaining consistent results in a new study addressing the same question. Poor design, insufficient data, model misspecification, selective reporting, undisclosed flexibility, measurement differences, and genuine heterogeneity can all disrupt one or both. The 2021 ASA task force similarly stated that properly applied p-values and significance tests remain important while locating replication problems in design, data, model choice, analytical description, and result selection. [5][16]

The debate is consequently not a contest between keeping p-values unchanged and banning them everywhere. Proposals include interpreting exact p-values without bright-line language, emphasizing effect estimates and intervals, requiring justification for decision thresholds, lowering thresholds for some new claims, adopting Bayesian or likelihood measures, controlling multiplicity, preregistering confirmatory analyses, publishing registered reports, sharing data and code, and valuing direct replication. These proposals solve different failure modes and carry different assumptions. The durable question is not which single statistic should replace 0.05, but which inferential design makes the scientific claim auditable and proportionate to the evidence. [4][5][12][17][18]

## Core Concepts

### 1. A p-Value Is a Model-Conditional Tail Area

A p-value is computed from a test statistic, a null hypothesis, and a reference distribution implied by a statistical model. Its validity is therefore conditional on more than the point null. Sampling or assignment procedures, independence, measurement, missing-data handling, model form, stopping rules, and the selection of the reported analysis may all matter. Greenland and colleagues emphasize that every inferential calculation sits inside a larger model containing both mathematical and study-conduct assumptions. A numerically correct p-value can answer the wrong question when that model does not represent how the data were generated or selected. [3]

A smaller p-value means that the observed statistic lies farther into the chosen null reference distribution, but it does not identify why. The null may be false, an assumption may be wrong, the data may contain an error, or the analysis may have been selected after examining many alternatives. Conversely, a large p-value can arise from compatibility with the null, low precision, weak measurement, small sample size, or a test insensitive to the relevant alternative. The logical asymmetry is central: the calculation evaluates data under a model; it does not directly evaluate the probability of the model given the data. [2][3]

### 2. Error Control and Evidence Are Different Uses

In a Neyman-Pearson design, the researcher specifies a decision rule, a Type I error rate, an alternative or effect-size region, and desired power before observing outcomes. The significance level is a property of that repeated procedure. In a Fisherian reading, the observed p-value is evidence about incompatibility with the null model after the data arrive. Applied reports often slide between these meanings, describing an observed p-value as both graded evidence and proof that a fixed error-controlled decision succeeded. [1][3]

The distinction becomes operational when costs differ. Screening thousands of exploratory associations, approving a drug, and checking a calibrated physical model need not share one threshold because false positives, false negatives, prior plausibility, multiplicity, and decision consequences differ. A justified rule can use a p-value, but the rule needs its error objective and context stated. The author's synthesis is that thresholding is most defensible when it is designed as a decision procedure in advance; evidential interpretation should retain the exact estimate, uncertainty, assumptions, and alternatives rather than reduce the result to a label. [3][5]

### 3. Statistical Significance Is Not Effect Importance

For a fixed standardized effect, larger samples generally produce more precise estimates and can produce smaller p-values. A very small but practically negligible effect can therefore cross a conventional threshold in a large study, while an important but imprecisely estimated effect can fail to cross it in a small study. The p-value is not an effect-size measure and does not encode clinical, scientific, economic, or policy importance. [2][3][14]

Effect estimates answer a different question: how large is the observed association or contrast in units relevant to the claim? Confidence intervals describe a range generated by a procedure with stated repeated-sampling coverage; they do not assign a 95% probability to a fixed parameter under the ordinary frequentist interpretation. They are often called compatibility intervals to emphasize that values inside the interval are more compatible with the data and model than values outside at the corresponding test level. Reporting the estimate and interval makes magnitude and precision visible, but it does not remove model assumptions or prevent dichotomizing the interval around zero. [3][4][14]

### 4. Multiplicity Changes the Meaning of a Discovery Rule

If one valid null test uses an alpha level of 0.05, its long-run false-positive probability is controlled at 5% under the stated conditions. If a researcher tries many outcomes, subgroups, transformations, stopping points, covariates, or models and reports only a favorable test, the family of possible analyses has a larger chance of producing at least one threshold-crossing result. Formal multiple-testing procedures can control a family-wise error rate or a false discovery rate when the family is defined, but undisclosed flexibility prevents readers from knowing which family was searched. [3][7][8]

Preregistration addresses this information problem by recording hypotheses, outcomes, exclusions, sample-size rules, and analysis plans before outcomes are known. It does not ban exploration; it makes the distinction between confirmatory tests and data-dependent discovery visible. Exploratory analyses can generate valuable hypotheses, but testing those hypotheses on the same data without adjustment does not provide an independent confirmation. Nosek and colleagues describe preregistration as a means of separating prediction from postdiction, not as a guarantee that a study's theory, measurement, or execution is correct. [12][13]

### 5. Power, Selection, and Exaggerated Effects Interact

Power is the probability that a prespecified test rejects the null under a specified alternative and design. Low-powered studies miss many real effects, but the subset that crosses a publication threshold tends to contain unusually favorable sampling error. This selection can exaggerate reported effect sizes even when the underlying effect is real. Ioannidis modeled how low pre-study odds, low power, multiplicity, bias, and competition among research teams can reduce the positive predictive value of published claims. His model is not an empirical count proving that most results in every field are false; it is a conditional demonstration of how research design and selection determine credibility. [6]

Power cannot be repaired by computing it after seeing the observed effect and treating that as independent evidence. Planning requires a scientifically meaningful effect, variance assumptions, a design, and a desired operating characteristic before data collection. After the study, estimates and intervals communicate what the data support. The author's synthesis is that researchers should plan around the smallest effect that would matter, not around the sample size needed to make any nonzero effect cross 0.05. [3][14]

### 6. Replication Is Not Repeating the Same Binary Label

A replication can be evaluated through several criteria: direction, effect-size consistency, interval overlap or prediction intervals, a meta-analytic estimate, a Bayes factor, or a prespecified decision rule. Comparing only whether the original and replication each produced `p < 0.05` is unstable because two estimates can be similar while falling on different sides of a threshold, or materially different while both cross it. The Open Science Collaboration therefore reported multiple replication indicators rather than one definitive success count. [9][16][18]

New data also test the transportability of methods, populations, settings, and measurements. A discrepant replication may reveal an original false positive, a replication false negative, a hidden moderator, procedural mismatch, or an effect too heterogeneous for the original claim. The National Academies cautions that non-replication can advance discovery when it exposes conditions under which a result changes. Replication should narrow the claim toward the populations and procedures supported by accumulated evidence, not serve as a ritual vote on whether one paper was true. [16]

### 7. Bayesian Measures Answer Different Conditional Questions

A Bayes factor compares how probable the observed data are under two specified models, such as `BF10 = P(data | H1) / P(data | H0)`. Posterior odds equal prior odds multiplied by the Bayes factor. Unlike a p-value, the comparison includes an alternative model and can provide evidence favoring a null model as well as an alternative. For a composite alternative, however, the result depends on the prior distribution assigned to possible effect sizes; an automatic default can hide a scientifically consequential assumption. [15]

Bayesian credible intervals can support direct probability statements about a parameter conditional on the model, likelihood, and prior. They do not eliminate design error, selective reporting, poor measurement, or sensitivity to model choice. Replacing `p < 0.05` with an unexamined Bayes-factor cutoff would recreate the same mechanical failure in a different notation. The proper comparison is between complete inferential designs, not between slogans attached to individual statistics. [3][5][15]

### 8. Threshold Reform Has Competing Proposals

Benjamin and colleagues proposed changing the default discovery threshold for many new claims from 0.05 to 0.005, arguing that stronger evidence would reduce false positives. Amrhein, Greenland, and McShane instead argued for retiring declarations of statistical significance and reporting estimates, intervals, exact p-values, and context without dichotomizing them. The 2019 American Statistician editorial likewise recommended abandoning the phrase statistically significant, whereas the 2021 ASA task force clarified that properly applied and interpreted significance tests remain useful. [4][5][17][18]

These positions disagree about whether better thresholds, no default thresholds, or broader inferential reform should dominate. They agree on more than the rhetoric suggests: a p-value is not a posterior probability, practical importance is distinct from threshold crossing, uncertainty must be reported, multiplicity and selection matter, and conclusions require design and subject knowledge. The author's assessment is that no universal threshold policy can substitute for explicit error costs, prior plausibility, effect-size relevance, and independent verification. [2][3][4][5][17][18]

### 9. Open-Science Reforms Target Different Failure Modes

Preregistration timestamps a plan; registered reports add peer review and in-principle publication acceptance before outcomes are known; data and code sharing permit computational checks; complete reporting exposes all measured outcomes and analyses; and direct replication supplies new data. These mechanisms are complementary. A preregistered but poorly measured study remains weak, shared code cannot repair biased sampling, and a replication that silently changes the estimand may not address the original claim. [12][13][16]

Registered reports directly weaken publication bias because acceptance is based on the question and methods rather than whether results cross a threshold. Munafo and colleagues place this reform within a wider system that includes methods, reporting, dissemination, evaluation, and incentives. The author's synthesis is that the future of hypothesis testing is institutional as well as mathematical: researchers respond to what journals, funders, employers, and collaborators reward, so reliable inference requires changing both calculations and selection mechanisms. [12][13]

## Evidence

### Researcher Flexibility Can Inflate False Positives

Simmons, Nelson, and Simonsohn used computer simulations and two experiments to test how common analytical freedoms affect false-positive results. Their simulated researcher could choose among dependent variables, continue collecting data after an interim look, include or exclude a covariate, and report selected comparisons among conditions. Each option can appear individually defensible, but using all of them while reporting only the successful analysis produced a 61% false-positive rate in their specified simulation rather than the nominal 5%. This is a demonstration of one workflow, not an estimate that 61% of published findings are false. Its evidential value is causal and procedural: undisclosed selection changes the operating characteristics of a test. [7]

Head and colleagues tested for a related pattern in published literature rather than in a simulation. They text-mined reported p-values in Open Access papers indexed by PubMed and examined distributions near the 0.05 boundary across 14 disciplines. They found an excess of values just below 0.05 consistent with widespread p-hacking. Their meta-analytic work also suggested that the inflation was weak relative to the real effects being measured and probably did not drastically alter scientific consensus derived from meta-analyses. The result therefore supports concern about selection without supporting the stronger claim that every threshold-crossing literature is devoid of signal. [8]

### Psychology Replications Found Smaller and Less Often Significant Effects

The Open Science Collaboration coordinated more than 270 contributors to repeat 100 experimental and correlational studies from three psychology journals. Teams used high-powered designs and original materials when available, and the project published materials, data, and analysis resources openly. Replication effects averaged roughly half the original magnitude. Ninety-seven percent of original studies reported statistically significant results, compared with 36% of replications; 47% of original effect sizes fell within the replication effect's 95% confidence interval, and 39% were rated by teams as replicating. The use of several criteria is itself evidence that replication cannot be reduced to one threshold comparison. [9]

The study's scope limits its interpretation. It sampled selected studies from three journals and one publication year, and each result was usually paired with one replication. Differences in context, implementation, sampling variability, and original selection can contribute to discrepancies. The project nevertheless supplied a direct audit of a defined literature and showed that effect magnitudes and significance labels from selected original publications were not stable under systematic repetition. [9][16]

### Social-Science Replications Used Preregistered, Higher-Powered Designs

Camerer and colleagues selected 21 experimental social-science studies published in Nature and Science between 2010 and 2015. Original authors reviewed the protocols, replication analysis plans were preregistered, and replication samples averaged about five times the original sample sizes. Thirteen studies, or 62%, produced a significant effect in the original direction; complementary criteria placed replicability between 57% and 67%. Replication effect sizes averaged about half the originals, while a Bayesian analysis estimated a 67% true-positive rate and suggested that both false positives and inflated estimates among true positives contributed to imperfect replication. [10]

This design addresses some objections to post hoc replication scoring because methods and success criteria were specified before outcomes were known. It still does not estimate a timeless rate for economics or all social science: the sample was restricted to experimental papers in two journals, and results depend on the selected claims and replication protocols. Its stronger contribution is methodological evidence that prespecification, high power, and multiple evaluation criteria can turn replication into a planned statistical study rather than an argument after results appear. [10]

### Preclinical Cancer Reports Exposed a Different Failure Pattern

Begley and Ellis described attempts by an Amgen team to confirm 53 landmark preclinical oncology findings before pursuing related drug-development programs. Scientific findings were confirmed in 6 cases, or 11%. The authors reported that papers had been deliberately selected for novel, consequential claims and acknowledged that failed validation could reflect technical differences, model limitations, or other complications. They compared their experience with a Bayer report in which about one quarter of published preclinical studies were validated sufficiently for projects to continue. [11]

This report is influential but differs from a randomized or systematically sampled replication project. Its project-level methods and case details were not disclosed to the degree of the psychology and social-science collaborations, and its selected landmark studies do not represent all biomedical research. The evidence supports concern about preclinical validation and incentives for striking findings; it does not justify treating 11% as a general biomedical replicability rate or attributing all failures to p-values. [11][16]

### Models Explain Why a Threshold Cannot Supply Positive Predictive Value

Ioannidis constructed a mathematical framework in which the probability that a published positive claim is true depends on pre-study odds, power, Type I error, the number of tested relationships, bias, and competition. The model demonstrates that a p-value threshold cannot by itself determine the post-study probability of a hypothesis. When plausible hypotheses are rare, studies are weak, many relationships are tested, or selective processes favor positives, threshold-crossing claims can have low positive predictive value even when each nominal test appears conventional. [6]

The framework should be read conditionally. Its conclusion follows from chosen inputs and assumptions, so it is not a direct survey of all research findings. It is nevertheless valuable because it isolates variables that threshold reasoning suppresses. The same observed p-value can imply different evidential assessments when prior plausibility, power, multiplicity, or selection differs. That is why the ASA states that a p-value by itself is not a good measure of evidence about a model or hypothesis. [2][6]

### Registered Reports Provide Early Evidence for Incentive Reform

Soderberg and colleagues compared 29 published registered reports in psychology and neuroscience with 57 non-registered comparison papers. A total of 353 researchers reviewed paired papers on 19 criteria. Registered reports were rated more favorably on average across all criteria, with sizeable estimated advantages for methodological rigor, analytical rigor, and overall quality; estimated differences in novelty and creativity were small and compatible with no difference. Because the study was observational and depended on matched papers and reviewer judgments, it does not prove that the format caused every quality difference. [19]

The method nonetheless tests an institutional intervention rather than another inferential statistic. Registered reports move initial peer review and in-principle acceptance before results, reducing the incentive to select publication on threshold crossing. Combined with preregistration, complete reporting, data and code access, and replication, this evidence supports a portfolio of reforms aimed at the research process. It also illustrates the appropriate standard for reform claims: proposed solutions should themselves be evaluated empirically and revised when evidence reveals limitations. [12][13][19]

### Evidence Across Cases Supports a Multi-Cause Account

Across the reviewed cases, no single mechanism explains every failure. Simulations show that analytical flexibility can inflate false positives; literature mining detects selection near a threshold; replication projects find selected original effects shrink under new data; biomedical validation reveals model and reporting problems; and registered-report comparisons suggest that publication design can improve assessed rigor. The sources also identify limits: p-hacking may have modest influence on some meta-analytic conclusions, non-replication can arise from heterogeneity, and a valid p-value remains useful when its assumptions and role are clear. [5][7][8][9][10][11][16][19]

The author's synthesis is that the replication crisis is best modeled as a system failure. Threshold incentives interact with low power, flexible analysis, publication selection, weak measurement, insufficient documentation, and rewards for novelty. Removing p-values alone would leave most of that system intact; keeping them without reform would preserve a convenient selection target. The evidence favors layered controls in which design, estimation, transparent reporting, and independent verification constrain one another. [2][5][12][16]

## Implications

### For Researchers: Design the Claim Before Testing It

A reliable analysis begins with the scientific estimand and the smallest effect that would matter. Researchers should state the population, intervention or exposure, comparison, outcome, time horizon, and target magnitude before selecting a test. They should then choose a design and sample size capable of estimating that quantity with useful precision or meeting a justified error criterion. This reverses the common workflow in which available data are searched first and the scientific claim is written around whichever test crosses 0.05. [3][12][14]

Confirmatory analyses should be preregistered when feasible, including stopping rules, exclusions, transformations, primary outcomes, subgroup tests, and multiplicity procedures. Deviations should be disclosed rather than concealed, and exploratory findings should be labeled as hypotheses that require new data. This does not make exploratory research inferior; it prevents postdictions from receiving the evidential status of predictions. The worst preventable failure is an analysis whose apparent error rate ignores the choices that produced it. [7][12][13]

### For Reporting: Replace Verdicts With an Evidence Profile

A report should present the effect estimate in meaningful units, its uncertainty interval, the exact p-value when a test is used, sample size, design assumptions, missing-data and exclusion rules, all prespecified outcomes, multiplicity handling, and sensitivity analyses. A result should not become important because `p = 0.049` or disappear because `p = 0.051`. The estimate, precision, prior evidence, decision cost, and robustness to plausible analyses are the relevant profile. [2][3][4][18]

Language should follow that profile. Instead of saying an effect exists because it is statistically significant, state what contrast was estimated, how precise it is, and which values remain compatible with the data and model. Instead of saying there is no effect after a large p-value, state that the data did not distinguish among a specified range of effects and identify whether that range excludes effects of practical importance. Equivalence tests or non-inferiority designs may be appropriate when the question is whether differences are sufficiently small, but their margins must be justified before results are seen. [3][4][18]

### For Reviewers and Journals: Remove Outcome-Based Selection

Review should ask whether the question matters, the design can answer it, the analysis matches the design, and the evidence supports the claim. Requiring a threshold-crossing result as a publication condition creates selection on sampling noise and leaves the literature without informative null, imprecise, or contradictory findings. Registered reports address this directly by deciding in-principle publication before outcomes are available. Journals can also require protocols, complete outcome reporting, data and code where ethically possible, and explicit separation of confirmatory and exploratory analyses. [12][13][19]

Threshold reform alone is insufficient. Lowering a default from 0.05 to 0.005 can reduce false positives under specified designs, but it can also increase false negatives or shift p-hacking toward a new boundary if sample sizes, incentives, and reporting do not change. Removing the term statistical significance can reduce dichotomous language, but readers may recreate a hidden cutoff unless estimates, uncertainty, and decision criteria are taught and enforced. Policy should target selection and transparency as well as numerical rules. [4][5][17][18]

### For Medicine and Public Policy: Separate Evidence From Action

Clinical and policy decisions combine evidence with consequences. A treatment estimate, uncertainty interval, adverse-effect profile, baseline risk, cost, feasibility, and patient values all matter; no p-value contains those inputs. A decision threshold can still be legitimate when regulators or trials prespecify acceptable error rates, but statistical rejection is one component of the decision rather than a synonym for benefit. [2][3][5]

The preclinical cancer case shows why this separation is essential. A finding can cross a statistical threshold in a model system yet fail to transfer across laboratories, biological models, or clinical settings. The appropriate response is stronger design, protocol detail, validation in independent systems, and cumulative evidence, not merely a different cutoff. For high-stakes claims, replication and external validity are part of the evidence chain before action. [11][16]

### For Economics, Business, and Investment Research: Guard Against Data Mining

Economic and financial datasets invite repeated testing across factors, periods, transformations, sectors, and outcome definitions. If many strategies or explanatory variables are searched and only successful backtests are reported, nominal p-values do not describe the search process. Prespecified holdout periods, correction for multiple comparisons, transparent reporting of the full research universe, and genuinely out-of-sample validation are therefore more informative than one in-sample significance label. This implication is the author's synthesis from the selection and replication evidence. [3][7][8][10]

For value investors, statistical association should remain subordinate to causal business understanding and economic magnitude. A statistically detectable return pattern may be too small after costs, unstable across regimes, or a proxy for an omitted exposure. Conversely, a strategically important operational effect may be estimated imprecisely in limited company data. The disciplined question is not only whether a coefficient differs from zero, but whether the mechanism is credible, the magnitude matters, and the result survives alternative specifications and new periods. This is an application of the broader evidence profile, not a separate statistical law. [3][10]

### For Statistics Education: Teach Conditional Logic, Not a Ritual

Students should learn the direction of conditioning in a p-value before learning a cutoff. They should compare Fisherian evidence, Neyman-Pearson error control, estimation, likelihood, and Bayesian updating as different frameworks with different outputs. Exercises should require students to identify the sampling plan, test statistic, null and alternative, effect size, uncertainty interval, multiplicity family, power target, and decision consequences. Historical context explains why the familiar hybrid arose and why its components should not be treated as interchangeable. [1][3][15]

Education should also make variation visible. Simulations can show how p-values change across repeated samples, how underpowered significant estimates are selected upward, and how flexible analysis changes false-positive rates. Replication exercises should compare effect estimates and intervals, not only labels. This makes uncertainty an object of study rather than a defect hidden by a binary answer. [7][9][14]

### For Readers: Audit the Evidence Chain

A reader can evaluate a threshold-based claim by asking a short sequence of questions. Was the hypothesis and analysis specified before outcomes were known? What effect was estimated, in what units, and with what precision? How many outcomes, subgroups, models, and stopping opportunities were available? Are the data, code, exclusions, and deviations documented? Does the conclusion depend on one threshold, one model, or one study? Has the result been tested with new data? These questions map directly to the main failure modes identified by the ASA, replication projects, and open-science literature. [2][5][9][12][16]

The answers need not produce certainty. A transparent exploratory result can be valuable, and a preregistered replication can still be inconclusive. The purpose of the audit is calibration: the strength and scope of the claim should match the design and accumulated evidence. A single p-value is one observation in that chain, not the chain itself. [3][5][16]

### A Balanced Future for Hypothesis Testing

The evidence does not support declaring p-values either sufficient or inherently invalid. The 2016 ASA principles and 2021 task force agree that misuse is widespread but that properly designed statistical tests can communicate uncertainty and control errors. The 2019 editorial and critics of statistical significance add that threshold language encourages false certainty and should not dominate scientific conclusions. These positions are in tension over terminology and defaults, and that disagreement should remain visible rather than be forced into a false consensus. [2][4][5][18]

The author's assessment is that the durable reform is modular. Use hypothesis tests when a prespecified decision or model check needs them; use estimates and intervals to show magnitude and precision; use Bayesian or likelihood measures when their models answer the scientific question; use multiplicity control when a defined family is searched; and use preregistration, registered reports, sharing, and replication to protect the research process from selective outcomes. Reliable science comes from agreement among these layers, not from finding a universally privileged number. [3][5][12][13][15][16][19]

## Sources

1. Kennedy-Shaffer, L. (2019). "Before p < 0.05 to Beyond p < 0.05:
   Using History to Contextualize p-Values and Significance Testing."
   The American Statistician, 73(sup1), 82-90.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC6693672 [high]

2. Wasserstein, R. L. and Lazar, N. A. (2016). "The ASA's Statement on
   p-Values: Context, Process, and Purpose." The American Statistician,
   70(2), 129-133.
   https://www.amstat.org/asa/files/pdfs/P-ValueStatement.pdf [high]

3. Greenland, S., Senn, S. J., Rothman, K. J., Carlin, J. B., Poole, C.,
   Goodman, S. N., and Altman, D. G. (2016). "Statistical Tests, P Values,
   Confidence Intervals, and Power: A Guide to Misinterpretations."
   European Journal of Epidemiology, 31, 337-350.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC4877414/ [high]

4. Wasserstein, R. L., Schirm, A. L., and Lazar, N. A. (2019). "Moving to
   a World Beyond p < 0.05." The American Statistician, 73(sup1), 1-19.
   https://sites.pitt.edu/~bertsch/Moving%20to%20a%20World%20Beyond%20p%200%2005.pdf [high]

5. Benjamini, Y., De Veaux, R. D., Efron, B., Evans, S., Glickman, M.,
   Graubard, B. I., He, X., Meng, X.-L., Reid, N., Stigler, S. M.,
   Vardeman, S. B., Wikle, C. K., Wright, T., Young, L. J., and Kafadar,
   K. (2021). "The ASA President's Task Force Statement on Statistical
   Significance and Replicability." Annals of Applied Statistics, 15(3),
   1084-1085.
   https://projecteuclid.org/journals/annals-of-applied-statistics/volume-15/issue-3/The-ASA-presidents-task-force-statement-on-statistical-significance-and/10.1214/21-AOAS1501.pdf [high]

6. Ioannidis, J. P. A. (2005). "Why Most Published Research Findings Are
   False." PLOS Medicine, 2(8), e124.
   https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124 [high]

7. Simmons, J. P., Nelson, L. D., and Simonsohn, U. (2011).
   "False-Positive Psychology: Undisclosed Flexibility in Data Collection
   and Analysis Allows Presenting Anything as Significant." Psychological
   Science, 22(11), 1359-1366.
   https://dmg5c1valy4me.cloudfront.net/wp-content/uploads/2020/09/08145800/simmons-nelson-simonsohn-false_positive_statistics-psycholsci2011.pdf [high]

8. Head, M. L., Holman, L., Lanfear, R., Kahn, A. T., and Jennions, M. D.
   (2015). "The Extent and Consequences of P-Hacking in Science." PLOS
   Biology, 13(3), e1002106.
   https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002106 [high]

9. Open Science Collaboration. (2015). "Estimating the Reproducibility of
   Psychological Science." Science, 349(6251), aac4716.
   https://osf.io/ezcuj/overview [high]

10. Camerer, C. F., Dreber, A., Holzmeister, F., Ho, T.-H., Huber, J.,
    Johannesson, M., Kirchler, M., Nave, G., Nosek, B. A., Pfeiffer, T.,
    and others. (2018). "Evaluating the Replicability of Social Science
    Experiments in Nature and Science Between 2010 and 2015." Nature
    Human Behaviour, 2, 637-644.
    https://www.nature.com/articles/s41562-018-0399-z [high]

11. Begley, C. G. and Ellis, L. M. (2012). "Raise Standards for
    Preclinical Cancer Research." Nature, 483, 531-533.
    https://www.nature.com/articles/483531a [high]

12. Munafo, M. R., Nosek, B. A., Bishop, D. V. M., Button, K. S.,
    Chambers, C. D., du Sert, N. P., Simonsohn, U., Wagenmakers, E.-J.,
    Ware, J. J., and Ioannidis, J. P. A. (2017). "A Manifesto for
    Reproducible Science." Nature Human Behaviour, 1, 0021.
    https://www.nature.com/articles/s41562-016-0021 [high]

13. Nosek, B. A., Ebersole, C. R., DeHaven, A. C., and Mellor, D. T.
    (2018). "The Preregistration Revolution." Proceedings of the National
    Academy of Sciences, 115(11), 2600-2606; author preprint.
    https://osf.io/preprints/osf/2dxu5 [high]

14. Cumming, G. (2014). "The New Statistics: Why and How." Psychological
    Science, 25(1), 7-29.
    https://www.est.ufmg.br/~enricoc/pdf/medicina/artigos/Psychological%20Science-2014-Cumming-7-29.pdf [high]

15. Stern, H. S. (2016). "A Test by Any Other Name: P-Values, Bayes
    Factors and Statistical Inference." Multivariate Behavioral Research,
    51(1), 23-29.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC4809350/ [high]

16. National Academies of Sciences, Engineering, and Medicine. (2019).
    "Reproducibility and Replicability in Science." National Academies
    Press. https://doi.org/10.17226/25303.
    https://nap.nationalacademies.org/catalog/25303/reproducibility-and-replicability-in-science [high]

17. Benjamin, D. J., Berger, J. O., Johannesson, M., Nosek, B. A.,
    Wagenmakers, E.-J., Berk, R., Bollen, K. A., Brembs, B., Brown, L.,
    Camerer, C., and others. (2018). "Redefine Statistical Significance."
    Nature Human Behaviour, 2, 6-10.
    https://www.nature.com/articles/s41562-017-0189-z [high]

18. Amrhein, V., Greenland, S., and McShane, B. (2019). "Scientists Rise
    Up Against Statistical Significance." Nature, 567, 305-307.
    https://www.nature.com/articles/d41586-019-00857-9 [high]

19. Soderberg, C. K., Errington, T. M., Schiavone, S. R., Bottesini, J.,
    Thorn, F. S., Vazire, S., Esterling, K. M., and Nosek, B. A. (2021).
    "Initial Evidence of Research Quality of Registered Reports Compared
    With the Standard Publishing Model." Nature Human Behaviour, 5,
    990-997.
    https://www.nature.com/articles/s41562-021-01142-4 [high]

## See Also

- `library/mathematics-statistics/statistical-inference.md` -- the broader framework for estimation, confidence intervals, frequentist testing, and Bayesian inference.
- `library/mathematics-statistics/experimental-design.md` -- randomization, power, replication, and design controls that determine whether a statistical test can support its claim.
- `library/mathematics-statistics/bayesian-statistics.md` -- posterior distributions and Bayes factors as model-dependent alternatives or complements to frequentist tests.
- `library/mathematics-statistics/causal-inference.md` -- why statistical association and threshold crossing do not by themselves identify causal effects.
