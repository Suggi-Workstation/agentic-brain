---
name: experimental-design
id: 20260827T070125Z
tier: library-topic
domain: mathematics-statistics
author: Library Runner
tags: [experimental-design, randomization, blocking, replication, factorial-designs, control-groups, blinding, validity, replication-crisis, sample-size, power-analysis]
links: [library/mathematics-statistics/causal-inference.md, library/mathematics-statistics/statistical-inference.md, library/mathematics-statistics/probability-theory-fundamentals.md, library/mathematics-statistics/regression-analysis.md, library/mathematics-statistics/bayesian-statistics.md]
---

# Experimental Design -- The Architecture That Separates Evidence from Anecdote

Experimental design is the discipline of structuring empirical studies
so that their results support valid causal inference. It is not
enough to collect data and run a statistical test -- the way data is
collected determines whether a test can answer the question posed.
Good experimental design controls confounding variables, quantifies
random error, and produces results that other researchers can
replicate. Without it, statistical analysis becomes sophisticated
arithmetic applied to biased data, yielding precise answers to the
wrong question. Experimental design is the architecture upon which
all empirical science stands: it is what separates evidence from
anecdote.

## Background

The intellectual history of experimental design is the story of how
agricultural statistics became the foundation of modern science. The
discipline was not born in a laboratory or a medical center but in the
fields of Rothamsted Experimental Station in England, where a
statistician named Ronald Aylmer Fisher (1890-1962) was hired in 1919
to analyze decades of crop yield data. Fisher found himself
confronted with a problem that had no existing solution: how do you
isolate the effect of a fertilizer treatment when soil quality,
rainfall, pest activity, and dozens of other variables vary across
every plot of land? The answer he developed over the next fifteen
years would reshape not only agriculture but medicine, psychology,
manufacturing, and every field that relies on empirical evidence.

Before Fisher, agricultural experiments were conducted using
systematic designs -- treatments were applied in orderly rows or
alternating strips. This approach had a fatal flaw: any systematic
arrangement creates a correlation between treatment assignment and
uncontrolled environmental variables. If the north end of a field
happens to be wetter, and the fertilizer is always applied to the
north rows, the experiment confounds fertilizer effect with moisture
effect. The results are uninterpretable. Fisher recognized that the
solution was not better measurement of confounders but a design that
makes confounding statistically ignorable. That solution was
randomization.

Fisher's first major publication on experimental design was the 1923
paper with Winifred Mackenzie on crop variation, which introduced the
analysis of variance (ANOVA) for field experiments. His 1925 book
"Statistical Methods for Research Workers" laid down the key
principles of replication, randomization, and local control (blocking)
for a broader audience. The pivotal work was his 1935 book "The Design
of Experiments," which codified these principles and introduced
concepts that remain central today: the null hypothesis, the
randomized controlled trial, factorial designs, and the Latin square.
The book's opening example -- the Lady tasting tea experiment -- is
still the canonical illustration of how a randomized design produces a
valid significance test. Fisher asked: can a woman distinguish whether
milk or tea was poured first into a cup? He designed an experiment
with eight cups, four of each preparation, presented in random order.
Under the null hypothesis that she cannot distinguish, the probability
of guessing all eight correctly is 1/70. The design made the test
valid: randomization ensured that any correct ordering beyond chance
could be attributed to a real ability, not to a biased presentation.

Fisher's innovation was radical because it shifted the statistician's
responsibility. Before Fisher, statisticians assumed their job was to
analyze whatever data they were given. Fisher recognized that the
quality of data depended on how it was produced, and that a
statistician "had no responsibility for the value or the worthlessness
of his estimates" if the data collection process was flawed. The
weight of responsibility, he argued, must be "thrown back on to the
processes by which the data had come into existence." This insight
elevated experimental design from a practical concern to a
mathematical discipline with its own principles, models, and
optimization criteria.

The second major stream in the history of experimental design came
from the social sciences. In the 1950s and 1960s, Donald Campbell and
Julian Stanley developed the framework of internal and external
validity, published in their influential 1963 monograph "Experimental
and Quasi-Experimental Designs for Research." Campbell and Stanley
cataloged the threats to valid inference -- history, maturation,
testing, instrumentation, regression to the mean, selection bias,
attrition, and interaction effects -- and showed how different
experimental designs address or fail to address each threat. Their
work extended Fisher's agricultural framework to educational and
social research, where randomization was often impractical, giving
rise to quasi-experimental designs that approximate randomized
experiments through matching, interrupted time series, and regression
discontinuity.

The third stream emerged in clinical medicine. The randomized
controlled trial (RCT), first used in a 1948 streptomycin trial for
tuberculosis conducted by the British Medical Research Council,
applied Fisher's agricultural principles to human subjects. The
double-blind placebo-controlled RCT became the gold standard for
medical evidence, institutionalized by the FDA drug approval process
and the CONSORT reporting guidelines. The placebo control, formalized
by Henry Beecher's 1955 paper "The Powerful Placebo," ensured that
observed treatment effects were not artifacts of expectation, natural
disease progression, or the act of receiving care itself.

The most recent chapter in this history is the replication crisis.
Beginning in the early 2010s, large-scale replication projects
revealed that many published findings across psychology, medicine, and
other fields could not be reproduced. The crisis was not primarily a
failure of statistics but a failure of experimental design: small
samples, selective reporting, flexibility in analysis, and inadequate
controls produced a literature of false positives. The response --
pre-registration, registered reports, open data, and larger sample
sizes -- is a return to Fisher's core insight: the validity of a
conclusion depends on the process by which the data came into
existence.

## Core Concepts

### Randomization

Randomization is the cornerstone of experimental design. It is the
process of assigning experimental units to treatment groups using a
mechanism that gives each unit a known, non-zero probability of
receiving each treatment -- typically equal probability, implemented
through a random number generator, coin flip, or shuffled cards.
Fisher insisted that randomization be a "physical experimental
process," not a systematic or purposive assignment. The reason is
mathematical: randomization breaks the statistical link between
treatment assignment and all confounding variables, both measured and
unmeasured. It does not eliminate confounding in any single
experiment -- by chance, one group may still differ from another --
but it makes confounding a random variable whose expected value is
zero and whose magnitude can be estimated from the data.

Randomization provides three guarantees. First, it eliminates
systematic bias: no confounder, known or unknown, is over-represented
in one treatment group by design. Second, it provides a valid
probabilistic basis for significance testing: the null hypothesis
distribution of the test statistic is generated by the randomization
process itself, a concept Fisher called the "physical basis of the
validity of the test." Third, it justifies the assumption that
observations are independent, which underlies nearly all standard
statistical tests.

A common misconception is that randomization guarantees balanced
groups. It does not -- by chance, randomization can produce
imbalanced groups, especially in small samples. What it guarantees is
that any imbalance is due to chance, not design, and can be accounted
for by the probability model. This is why Fisher advocated
randomization even in experiments where a balanced systematic design
might seem more efficient: the systematic design's balance is
illusory if it correlates with an unmeasured confounder.

### Replication

Replication means applying each treatment to multiple experimental
units, not measuring the same unit multiple times (which is
repetition). Replication serves two purposes: it provides an estimate
of experimental error (the variance against which treatment effects
are judged), and it increases the precision of effect estimates by
reducing the standard error of the mean.

Without replication, there is no error variance, and no significance
test is possible. An experiment with one observation per treatment
can estimate differences but cannot assess whether those differences
are larger than what chance would produce. The number of replicates
determines statistical power -- the probability of detecting a true
effect of a given size. Power analysis, developed by Neyman and
Pearson and formalized by Cohen, uses the expected effect size, the
desired significance level, and the target power to calculate the
required sample size before the experiment begins.

A critical distinction is between biological replication (independent
subjects receiving the same treatment) and technical replication
(repeated measurements on the same subject). Biological replication
generalizes to a population; technical replication only improves the
precision of measurement for that subject. Many flawed experiments
confuse the two, using technical replicates as if they were
independent observations, which inflates the apparent sample size and
produces false-positive results.

### Blocking and Local Control

Blocking is the technique of grouping experimental units into
homogeneous blocks before randomizing treatments within blocks. It
addresses a problem that randomization alone cannot solve: if a known
nuisance factor (soil type, patient age, time of day, operator
identity) affects the response, randomization will distribute it
across groups but will not remove its contribution to error variance.
Blocking removes that contribution by making comparisons within
homogeneous groups, so the nuisance factor's variability does not
enter the error term.

The guiding principle, attributed to Fisher, is: "Block what you can,
randomize what you cannot." Use blocking for a few primary nuisance
factors that are known and measurable. Use randomization for the
remainder -- the unmeasured and unknown confounders that no design can
explicitly control.

The randomized complete block design (RCBD) controls for one nuisance
factor. The Latin square design controls for two nuisance factors
simultaneously by arranging treatments in a square grid where each
treatment appears exactly once in each row and once in each column.
Latin squares require that the number of treatments equal the number
of levels of each blocking factor, and they assume no interaction
between the treatment and the blocking factors -- an assumption that
must be validated, not assumed.

### Factorial Designs

A factorial design tests multiple factors simultaneously, running
every combination of factor levels. A 2x2 factorial tests two factors
each at two levels, producing four treatment groups; a 2x3 design
produces six. The advantage over one-at-a-time experimentation is
efficiency: a single factorial experiment estimates all main effects
and all interactions, while sequential single-factor experiments
would require more runs and still miss interactions.

A main effect is the average change in response when a factor moves
from its low to high level, averaged across all levels of the other
factors. An interaction effect exists when the effect of one factor
depends on the level of another. Interactions are where factorial
designs earn their keep: if factor A has a positive effect only when
factor B is at its high level, a one-at-a-time design would never
discover this. The factorial design reveals it because every level of
A is tested under every level of B.

Fractional factorial designs sacrifice the ability to estimate all
interactions in exchange for fewer runs. A 2^(k-1) half-fraction runs
half the combinations of a full 2^k design, at the cost of aliasing
(confounding) certain effects with each other. The choice of which
effects to alias is an editorial decision: the researcher decides
which interactions are least likely to be important and aliases them
with main effects or lower-order interactions. The defining relation
of the design (e.g., I = ABCD for a 2^(4-1) design) determines the
complete alias structure.

### Control Groups and Blinding

A control group receives either no treatment, a placebo, or a standard
treatment, providing the baseline against which the experimental
treatment is compared. Without a control group, any observed change
could be due to natural progression, regression to the mean, placebo
effects, or environmental shifts. The control group isolates the
treatment effect by holding all other conditions constant.

Blinding prevents bias from entering through the expectations of
participants or experimenters. In a single-blind study, participants
do not know which treatment they receive. In a double-blind study,
neither participants nor experimenters know the assignment until the
data are analyzed. Blinding is necessary because expectations affect
behavior and even physiological responses: the placebo effect in
patients and the experimenter expectancy effect in researchers can
produce real differences in measured outcomes that have nothing to do
with the treatment itself. Beecher's 1955 analysis estimated that up
to 35 percent of therapeutic effects in clinical trials could be
attributed to placebo responses, though later reanalyses suggested
this figure was inflated by failing to control for natural disease
fluctuation.

### Threats to Validity

Donald Campbell and Julian Stanley formalized the concept of validity
threats -- alternative explanations that can account for observed
results independently of the treatment. They distinguished internal
validity (did the treatment cause the observed effect in this specific
study?) from external validity (can the effect be generalized to other
populations, settings, and times?).

Threats to internal validity include: history (events between pretest
and posttest that affect the outcome), maturation (natural changes in
subjects over time), testing (the pretest itself changes the
response), instrumentation (changes in measurement tools),
statistical regression to the mean (extreme scores tend toward the
average on retesting), selection bias (groups differ before the
treatment), and attrition (differential dropout between groups).

Threats to external validity include: interaction of testing and
treatment (pretesting sensitizes subjects to the treatment),
interaction of selection and treatment (the selected sample is not
representative), and reactive arrangements (the experimental setting
itself alters behavior -- the Hawthorne effect).

Cook and Campbell later expanded the typology to four types:
statistical conclusion validity (is the covariation real?),
internal validity (is the covariation causal?), construct validity
(do the operations capture the intended constructs?), and external
validity (do the results generalize?). Each type has its own set of
threats, and a well-designed experiment must address all four.

### Power Analysis and Sample Size Determination

Statistical power is the probability that a test will detect a true
effect of a specified size at a given significance level. Power is
determined by four quantities: the significance level (alpha, usually
0.05), the effect size (the magnitude of the true difference), the
sample size, and the population variance. Given any three, the fourth
is determined. Power analysis runs this calculation before data
collection to determine the sample size needed to achieve a target
power (conventionally 0.80 or higher).

Underpowered experiments are a leading cause of the replication
crisis. A study with 30 percent power has a high probability of
missing true effects and, when it does find significance, a high
probability that the finding is a false positive inflated by
sampling error (the "winner's curse"). Power analysis forces
researchers to confront the question: if my hypothesis is true, how
many subjects do I need to detect it? Answering this question before
collecting data prevents the most common form of wasted research --
experiments that cannot answer the question they pose.

## Evidence

### The Lady Tasting Tea (Fisher, 1935)

The most famous illustration of experimental design principles is
Fisher's Lady tasting tea experiment, described in the opening chapter
of "The Design of Experiments" (1935). A colleague, Dr. Muriel Bristol,
claimed she could tell whether milk or tea was poured first into a
cup. Fisher designed an experiment to test this claim: eight cups
were prepared, four with milk first and four with tea first, presented
to Bristol in random order. She was told there were four of each type
but not which was which.

Under the null hypothesis that Bristol could not distinguish the
preparations, her answers would be due to chance. The number of ways
to choose 4 cups out of 8 (labeling them as "milk first") is C(8,4) =
70. Only one of these 70 orderings is entirely correct. So the
probability of a perfect score by chance alone is 1/70, approximately
0.014. If Bristol got all eight cups right, Fisher would reject the
null hypothesis at a significance level below 0.05. If she got one
wrong, the probability would be (1 + 16)/70 = 17/70, approximately
0.243 -- not significant.

This experiment demonstrates several principles simultaneously:
randomization (cups presented in random order), control (equal numbers
of each type, subject told the design), a well-defined null
hypothesis, and a test whose validity rests on the randomization
process. The design is so simple that it requires no parametric
assumptions -- the significance level is exact, derived from the
combinatorial structure of the randomization. Bristol reportedly
identified all eight cups correctly, and Fisher had his demonstration
that a rigorous design can test even an implausible-sounding claim.

### The Streptomycin Trial (MRC, 1948)

The first modern randomized controlled trial in medicine was the 1948
British Medical Research Council trial of streptomycin for pulmonary
tuberculosis. The trial randomized 107 patients to either streptomycin
plus bed rest or bed rest alone. Randomization was conducted using
sealed envelopes containing random number assignments, and neither
patients nor treating physicians knew which group a patient was in.

The results were dramatic: 51 percent of streptomycin patients showed
significant improvement at six months, compared to 8 percent of
controls. Seven streptomycin patients died versus 27 controls. The
trial established not only the efficacy of streptomycin but the
methodology of the RCT as the standard for medical evidence. The
design incorporated randomization (to eliminate selection bias),
blinding (to eliminate expectation bias), a control group (to
isolate the treatment effect from natural disease progression), and
predefined outcome criteria (to prevent post-hoc cherry-picking of
results).

The streptomycin trial also illustrates the ethical dimension of
experimental design. Streptomycin was in short supply; randomization
was not only methodologically superior but also a fair way to
distribute a scarce resource. The tension between scientific rigor
and ethical obligation -- randomizing patients to potentially inferior
treatment -- remains a central challenge in clinical trial design,
addressed through equipoise (genuine uncertainty about which treatment
is better), stopping rules (predefined criteria for ending a trial if
one treatment proves clearly superior), and informed consent.

### The Reproducibility Project (Open Science Collaboration, 2015)

The most consequential evidence for the importance of experimental
design comes from the replication crisis itself. In 2015, the Open
Science Collaboration published the results of a massive replication
effort in Science. The project attempted to replicate 100 experimental
and correlational studies published in three top psychology journals,
using high-powered designs and original materials whenever possible.

The findings were sobering. While 97 percent of the original studies
reported statistically significant results, only 36 percent of the
replications achieved significance. The mean effect size of the
replication studies was approximately half the mean effect size of the
originals. Only 47 percent of original effect sizes fell within the 95
percent confidence interval of the replication effect size. Subjective
assessments by the replication teams judged that 39 percent of effects
had replicated the original result.

The project identified several design failures that contributed to the
discrepancy. Many original studies were underpowered -- small samples
that inflated effect sizes through sampling error. Publication bias
meant that significant results were more likely to be published,
creating a literature skewed toward false positives. Flexibility in
analysis -- the researcher's freedom to choose among many statistical
tests and reporting only those that yielded significance -- inflated
the false positive rate far beyond the nominal 5 percent. The
replication studies addressed these problems through pre-registration
(committing to hypotheses and analyses before data collection), larger
samples (higher power), and transparent reporting of all analyses.

This study transformed the debate from a theoretical concern into
documented evidence. It demonstrated that design choices --
randomization, blinding, sample size, pre-registration, analysis
transparency -- are not mere methodological niceties but the
determinants of whether scientific findings are true. A finding
produced by a flawed design is not merely imprecise; it can be
systematically wrong, and no amount of statistical sophistication can
repair data collected under a design that permits confounding or
selective reporting.

### Blocking in Agricultural Trials (Fisher and Mackenzie, 1923)

Fisher's 1923 paper with Winifred Mackenzie on crop variation at
Rothamsted provides the foundational evidence for blocking. They
analyzed data from a trial comparing six varieties of potatoes
arranged in a randomized block design. The field was divided into
blocks (rows) and plots (columns within rows), with varieties
randomly assigned within each block. The analysis of variance
partitioned the total variation into components: variation between
blocks (due to soil heterogeneity), variation between varieties (the
treatment effect), and residual error.

The key finding was methodological, not agricultural. By blocking on
the known nuisance factor (soil heterogeneity across the field) and
randomizing within blocks, Fisher and Mackenzie obtained a treatment
comparison with substantially smaller error variance than a
completely randomized design would have produced. The blocking
removed the between-block variation from the error term, increasing
the precision of the variety comparison. This demonstration
established the randomized block design as the default for
agricultural research and, by extension, for any experiment where a
known nuisance factor can be identified and controlled.

### Campbell and Stanley's Validity Catalog (1963)

Campbell and Stanley's 1963 monograph provided systematic evidence for
how design choices affect validity. They analyzed sixteen experimental
and quasi-experimental designs, evaluating each against twelve
threats to valid inference. The result was a catalog showing
precisely which threats each design can and cannot rule out.

The pre-experimental designs -- the one-shot case study (X O), the
one-group pretest-posttest design (O X O), and the
nonequivalent-control-group design -- were shown to be vulnerable to
most or all threats. The true experimental designs -- the
posttest-only control group design (R X O, R O), the pretest-posttest
control group design (R O X O, R O O), and the Solomon four-group
design -- were shown to rule out most internal validity threats
through randomization. The quasi-experimental designs -- the
interrupted time series and the nonequivalent control group time
series -- were shown to address specific threats while remaining
vulnerable to others.

This catalog converted experimental design from an art into a
decision framework. A researcher could select a design by identifying
which threats are most pressing for their context and choosing the
design that best addresses them. The framework also made explicit the
trade-off between internal and external validity: the most tightly
controlled laboratory experiments maximize internal validity at the
cost of generalizability, while field experiments sacrifice some
control for ecological validity.

## Implications

### For Scientific Research

The most direct implication of experimental design is for the practice
of science itself. Every empirical discipline -- medicine, psychology,
economics, education, biology, engineering -- depends on experimental
design to produce credible evidence. The replication crisis has made
this dependence explicit: the fields that experienced the worst
replication failures were those that tolerated the weakest design
practices. The reforms that followed -- pre-registration, registered
reports, mandatory sample size justification, open data, and
standardized reporting guidelines like CONSORT for clinical trials and
PRE-ANALYSIS PLANS for economics -- are all design reforms, not
statistical reforms. They change how data is collected, not how it is
analyzed.

For individual researchers, experimental design is a planning
discipline, not an afterthought. The design is specified before data
collection begins: the hypothesis, the treatment and control
conditions, the randomization scheme, the sample size (justified by
power analysis), the outcome measures, and the analysis plan. This
specification is the substance of pre-registration. It forces
researchers to confront design questions while they can still change
them -- before the data reveals which design choices would have been
convenient. The shift from exploratory to confirmatory research --
from fishing for patterns to testing pre-specified hypotheses -- is
the most important methodological reform of the past decade.

For fields that cannot randomize -- observational epidemiology, labor
economics, education policy -- experimental design provides the
framework for evaluating quasi-experimental alternatives. The Campbell
tradition's validity threat catalog lets researchers identify which
threats their design cannot rule out and triangulate with additional
evidence. Difference-in-differences, regression discontinuity, and
instrumental variables are all attempts to approximate the properties
of a randomized experiment when randomization is impossible. Their
credibility is judged by how closely they approach the design
standards that randomization achieves directly.

### For Clinical Medicine and Drug Development

Experimental design is the regulatory foundation of evidence-based
medicine. The FDA requires randomized, double-blind,
placebo-controlled trials for drug approval because these designs
rule out the threats -- selection bias, expectation bias, placebo
effects, regression to the mean -- that have historically produced
ineffective or harmful treatments. The phases of clinical development
(phase I safety, phase II efficacy, phase III confirmatory, phase IV
post-market) are a design sequence, each phase addressing a different
question with a different design.

The implications extend to comparative effectiveness research, where
the question is not whether a treatment works but which of several
treatments works best. Pragmatic trials -- large, simple trials
conducted in real-world clinical settings -- sacrifice some internal
validity for external validity, enrolling broader populations and
using clinically relevant outcomes. The tension between explanatory
trials (tightly controlled, homogeneous populations, surrogate
endpoints) and pragmatic trials (loosely controlled, diverse
populations, clinical endpoints) is a design choice with no
universally correct answer. The right design depends on the question:
does this treatment work under ideal conditions, or does it work in
the patients I actually treat?

Adaptive trial designs -- basket trials, umbrella trials, and
sequential designs that modify enrollment based on interim results --
represent the frontier of clinical experimental design. They use
Bayesian methods and pre-specified adaptation rules to answer more
questions with fewer patients, but they introduce new validity
threats (inflated false positive rates, complexity-driven opacity)
that traditional fixed designs avoid. The trade-off between efficiency
and rigor is the central design tension in modern clinical research.

### For Industry and Engineering

Experimental design originated in agriculture but found its most
extensive industrial application in manufacturing, through the work of
George Box and the quality movement. Design of experiments (DOE) is a
core methodology in Six Sigma and quality engineering: factorial
designs identify the factors that affect a process, response surface
methodology optimizes the factor settings, and robust design (Taguchi
methods) makes products insensitive to environmental variation.

The implications for product development are direct. A factorial
experiment can test five factors at two levels in 32 runs, replacing
what would require 160 runs if each factor were tested one at a time.
The interaction effects that factorials reveal -- a factor that
matters only in combination with another -- are often the most
actionable findings, because real processes are multivariate and
interdependent. Industries that adopted DOE systematically (Japanese
manufacturing in the 1980s, semiconductor fabrication, pharmaceutical
process development) achieved quality and efficiency gains that
competitors using trial-and-error could not match.

### For Technology and AI Evaluation

The most recent frontier for experimental design is the evaluation of
AI systems. As machine learning models become more capable, the
question of whether a model improvement is real or an artifact of
benchmark selection, prompt engineering, or sampling variance has
become pressing. A/B testing -- the online controlled experiment --
is experimental design applied at scale, with millions of users
randomized to treatment and control conditions to measure the effect
of a change in a product or algorithm.

The design challenges in AI evaluation mirror those in other fields:
selection bias (benchmarks may not represent real use), multiple
comparisons (testing many configurations inflates false positives),
and the interaction between model and evaluator (an evaluator who
knows which model generated which output introduces expectation
bias). The solution is the same: randomization, blinding,
pre-registration of evaluation protocols, and adequate sample sizes.

The implications extend to the design of the AI systems themselves.
Reinforcement learning from human feedback, the training method
behind modern language models, is an experimental design problem: the
reward model is trained on comparisons, and the quality of those
comparisons depends on whether the human raters were blinded to the
model identity, whether the prompts were sampled representatively,
and whether the comparison protocol was pre-specified. A model
trained on biased comparisons will optimize for the bias, not for
genuine quality. The same design principles that protect clinical
trials and agricultural experiments -- randomization, blinding,
pre-registration, adequate sampling -- protect the integrity of the
training signal that shapes AI behavior. Experimental design is not
a historical artifact but a living discipline whose principles apply
wherever empirical evidence is sought, and the frontier of that
application is now computational.

## Common Pitfalls

### Confusing Technical and Biological Replication

A pervasive error in preclinical research is treating repeated
measurements on the same subject as independent replicates. If five
wells of cells from the same mouse are treated and measured, the
sample size for generalizing to mice is one, not five. Pseudoreplication
inflates the apparent degrees of freedom, underestimates standard
errors, and produces false positives. The fix is to design the
experiment around the unit of inference: if the claim is about mice,
each mouse is one replicate.

### P-Hacking and Researcher Degrees of Freedom

When researchers have flexibility in how they analyze data -- which
variables to include, which outliers to exclude, which transformation
to apply, which covariate to adjust for -- the probability of finding
a significant result by chance alone far exceeds the nominal alpha.
Simulations show that with enough researcher degrees of freedom, a
researcher can produce statistically significant results from pure
noise. Pre-registration and pre-analysis plans eliminate this
flexibility by committing to the analysis before seeing the data.

### Ignoring Interactions in Factorial Designs

A main effect in a factorial design is the average effect across all
levels of other factors. If an interaction exists, the main effect may
be misleading or meaningless: a drug that helps men but harms women
has a main effect near zero, but concluding "the drug has no effect"
is wrong. Always examine interaction plots and interaction terms
before interpreting main effects. The principle extends to
subgroup analyses in clinical trials, where treatment effects may
differ by sex, age, or genotype.

## Sources

1. Fisher, R.A. (1935). "The Design of Experiments." Oliver and Boyd,
   Edinburgh. The foundational text that established randomization,
   replication, and blocking as principles of experimental design,
   illustrated by the Lady tasting tea experiment.
   https://en.wikipedia.org/wiki/The_Design_of_Experiments [high]

2. Fisher, R.A. & Mackenzie, W.A. (1923). "Studies in Crop Variation.
   II. The Manurial Response of Different Potato Varieties." Journal
   of Agricultural Science, 13(3), 311-320. The first application of
   ANOVA to a randomized block design in field experiments.
   https://doi.org/10.2307/2682986 [high]

3. Box, J.F. (1980). "R.A. Fisher and the Design of Experiments,
   1922-1926." The American Statistician, 34(1), 1-7. Historical
   analysis of how Fisher developed the principles of experimental
   design at Rothamsted.
   https://doi.org/10.2307/2682986 [high]

4. Campbell, D.T. & Stanley, J.C. (1963). "Experimental and
   Quasi-Experimental Designs for Research." Rand McNally. The
   monograph that introduced the internal/external validity framework
   and the catalog of validity threats.
   https://onlinelibrary.wiley.com/doi/10.1002/ev.1433 [high]

5. Cook, T.D. & Campbell, D.T. (1979). "Quasi-Experimentation: Design
   and Analysis Issues for Field Settings." Houghton Mifflin. Expanded
   the validity typology to four types: statistical conclusion,
   internal, construct, and external validity.
   https://onlinelibrary.wiley.com/doi/10.1002/ev.1433 [high]

6. Open Science Collaboration. (2015). "Estimating the
   reproducibility of psychological science." Science, 349(6251),
   aac4716. The large-scale replication project that documented the
   replication crisis and demonstrated the consequences of weak
   experimental design.
   https://www.science.org/doi/10.1126/science.aac4716 [high]

7. Beecher, H.K. (1955). "The Powerful Placebo." Journal of the
   American Medical Association, 159(17), 1602-1606. The paper that
   established the placebo effect as a measurable phenomenon and
   formalized placebo controls in clinical trials.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC11944128/ [high]

8. Montgomery, D.C. (2017). "Design and Analysis of Experiments," 9th
   edition. Wiley. The standard modern textbook covering factorial
   designs, blocking, response surface methodology, and fractional
   factorials.
   https://www.wiley.com/en-us/Design+and+Analysis+of+Experiments
   [high]

9. NIST/SEMATECH. "e-Handbook of Statistical Methods: Randomized Block
   Designs." The online reference covering blocking, Latin squares,
   and nuisance factor control with worked examples.
   https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm
   [high]

10. Senn, S. (2006). "Transferability of randomised trials and
    naturalistic studies." Statistical Methods in Medical Research,
    15(4), 299-308. Discusses the tension between explanatory and
    pragmatic trial designs and the internal-external validity
    trade-off.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC7144753 [medium]

## See Also

- `library/mathematics-statistics/causal-inference.md` -- the
  framework for moving from association to causation that experimental
  design enables.
- `library/mathematics-statistics/statistical-inference.md` -- the
  mathematical tools for drawing conclusions from experimental data,
  including hypothesis testing and confidence intervals.
- `library/mathematics-statistics/probability-theory-fundamentals.md`
  -- the probabilistic foundations underlying randomization and
  significance testing.
- `library/mathematics-statistics/regression-analysis.md` -- the
  analytical methods used to estimate treatment effects in
  experimental and observational data.
- `library/mathematics-statistics/bayesian-statistics.md` -- the
  alternative inferential framework used in adaptive trial designs and
  sequential analysis.