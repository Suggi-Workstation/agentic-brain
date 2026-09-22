---
name: law-of-small-numbers
id: 20260922T200717Z
tier: library-topic
domain: probabilistic-thinking-forecasting
author: Librarian
tags: [law-of-small-numbers, sample-size-neglect, sampling-variability, regression-to-mean, selection-bias, forecasting, decision-making]
links: [library/probabilistic-thinking-forecasting/base-rate-neglect.md, library/probabilistic-thinking-forecasting/calibration-and-overconfidence.md, library/probabilistic-thinking-forecasting/inside-outside-view.md, library/probabilistic-thinking-forecasting/pre-mortems-and-post-mortems.md, library/mathematics-statistics/statistical-inference.md]
---

# The Law of Small Numbers -- Why Small Samples Produce False Certainty

The law of small numbers is the mistaken expectation that a short record will display the stable proportions, alternation, and regularity of the process that generated it. Small samples can contain real information, but they fluctuate more than intuition expects, so streaks, extreme averages, apparent winners, and early reversals often justify less confidence than their vividness suggests ([1] [2]). The author's synthesis for decisions under uncertainty is not to reject every small sample; it is to make sample size, selection, measurement noise, base rates, and plausible process change explicit before updating a forecast.

## Background

Amos Tversky and Daniel Kahneman named the "belief in the law of small numbers" in 1971. Their phrase was intentionally ironic. The mathematical law of large numbers describes convergence as sample size grows; the psychological law of small numbers describes an intuition that acts as if convergence has already occurred in a short sequence. People therefore expect a small random sample to resemble its parent population in more respects and with less variability than sampling theory warrants ([1]). The error concerns representativeness, not merely ignorance of a formula: a result looks persuasive because its local pattern resembles a familiar population pattern or causal story.

The original paper focused on scientific judgment as well as everyday chance. Tversky and Kahneman asked 84 participants drawn from meetings of mathematical psychologists and the American Psychological Association to assess problems involving replication, sample size, and research design. In one item, respondents evaluated the probability that a statistically significant result from 20 observations would be significant again in a new group of 10. Only 9 of 84 placed the probability in the approximately correct interval of 0.40 to 0.60; the median answer was about 0.85. The authors argued that trained researchers were extracting more certainty from small samples than the data contained and were consequently vulnerable to underpowered designs and overinterpretation ([1] [10]).

Their 1974 review placed sample-size neglect within the representativeness heuristic. In the well-known hospital problem, people were asked whether a small or a large hospital would record more days on which more than 60 percent of births were boys. Many judged the hospitals equally likely, although a smaller daily sample has greater sampling variation and therefore produces extreme proportions more often. The review linked this insensitivity to sample size with excessive faith in small studies, mistaken beliefs about random sequences, and predictions that follow the resemblance of a case rather than the reliability of the evidence ([2]).

The bias has two directions that appear contradictory. When the generating probability is treated as known, people may expect a short sequence to self-correct, producing the gambler's fallacy: after several heads, a tail feels "due." When the generating probability is uncertain, the same observer may treat a streak as evidence that the process or performer is unusually strong, producing overinference or a hot-hand belief. Matthew Rabin formalized how local representativeness can generate both reactions: short sequences are expected to balance too quickly, while longer or sufficiently salient streaks are taken as evidence of hidden differences among sources ([3]).

Regression to the mean is a related statistical mechanism, not a force that pushes observations toward an average. If a measurement combines a persistent component with transitory noise, an unusually high or low first observation is likely to contain an unusually favorable or unfavorable noise component. A later measurement will, on average, be less extreme because the new noise is unlikely to be extreme in the same direction. The effect becomes especially visible when cases are selected because their initial measurements were extreme, and it becomes stronger as measurement error increases ([4]).

The modern research record also supplies an important correction to a simplistic bias story. Joshua Miller and Adam Sanjurjo showed that a common estimator used in hot-hand research has a finite-sample selection bias: after researchers select shots that follow a streak, the expected comparison is not centered where the canonical analysis assumed. Correcting that bias reversed the conclusion of a prominent hot-hand study ([7]). The lesson is not that every perceived streak is real. It is that small-sample skepticism must be applied to the analyst's estimator as well as to the subject's intuition.

This topic belongs in probabilistic thinking and forecasting because it concerns how strongly a decision-maker should update from limited evidence. Formal derivations of sampling distributions, power, and estimation belong primarily in mathematics and statistics; the psychology of representativeness belongs primarily in psychology and behavior. The applied problem here is disciplined belief revision: deciding whether an observed pattern is signal, sampling variation, selection, or evidence that the generating process has changed ([1] [2] [3]).

## Core Concepts

### Sample Size Changes the Distribution of Estimates

A sample average or proportion is itself a random variable. Across repeated independent samples from the same stable population, small samples produce a wider distribution of estimates than large samples. Under standard independent sampling assumptions, the standard error of an average falls in proportion to one divided by the square root of sample size. Increasing a sample from 25 observations to 100 therefore halves, rather than quarters, the standard error. The exact formula depends on the design and data-generating process, but the governing principle is general: more independent information usually narrows uncertainty, while a short record permits larger chance deviations ([1] [2]).

This relationship explains why an extreme percentage can be less informative than a moderate percentage based on many observations. Six successes in eight trials equal 75 percent, but the estimate is compatible with a broad range of underlying success rates. Seven hundred fifty successes in 1,000 trials also equal 75 percent, but such a result is much harder to produce by chance if the underlying rate is near one-half. A percentage without its denominator suppresses the variable that controls sampling precision. Treating the two percentages as equally strong evidence is sample-size neglect ([1] [10]).

More data do not automatically solve every problem. Dependence among observations reduces the amount of independent information; repeated measurements of the same underlying event do not equal independent trials. Biased selection can make a large sample precisely estimate the wrong target, and a changing process can make old observations less relevant than recent ones. The author's synthesis is that effective sample size, representativeness of the sampling process, and stability of the target must be examined together. Raw observation count is necessary context, not a universal quality score ([4] [9]).

### Local Representativeness Is Not Randomness

People often imagine a random sequence as irregular in a carefully balanced way. A sequence such as H-T-H-T-T-H may look more random than H-H-H-T-T-T, even though any specified six-toss sequence has the same probability under independent fair tosses. The first sequence alternates frequently and stays close to a 50-50 proportion, so it resembles the long-run properties of a fair coin locally. Actual short random sequences cluster more than this intuition predicts. The law of small numbers mistakes the expected long-run composition for a rule that each short segment should obey ([1] [2]).

This mistake produces the gambler's fallacy when a stable independent process is assumed. If roulette outcomes are independent, a run of red does not make black more likely on the next spin. Yet a believer in local balance expects the short sequence to repair its imbalance. The same mental model can produce excessive switching in forecasts, premature bets on reversal, or the belief that recent business performance must immediately return to an average even when no causal mean-reversion mechanism has been established ([3]).

The hot-hand belief begins with a different inference. A decision-maker who is uncertain whether the process is stable may interpret a streak as evidence that the success probability has changed or that the performer belongs to a higher-quality type. That inference is not logically irrational: real processes can change, and people differ in skill. The error occurs when the observer infers too much hidden heterogeneity or persistence from too little noisy evidence. Rabin's model shows how a person who expects small samples to look representative can infer nonexistent differences among analysts or fund managers after short performance records ([3]).

The practical question is therefore conditional, not categorical. First ask whether the data-generating process is plausibly independent and stable. If it is, a streak is expected sampling variation unless evidence shows otherwise. If the process can change, ask how likely the observed streak would be under both a stable-process model and a changed-process model, and update by the relative likelihood rather than by the pattern's visual force. This is the author's synthesis of the forecasting discipline implied by the original bias research and the later economic models ([1] [3]).

### Selection Makes Extremes Look Persistent or Corrective

Selection determines which small samples become visible. A company highlights the product test with the largest conversion lift, a newspaper profiles the best-performing manager, and a team investigates a branch after an unusually bad month. If many noisy candidates were examined, the selected winner or loser probably combines a persistent component with favorable or unfavorable noise. Repeating the measurement removes the original selection advantage, so the observed result often becomes less extreme even if nothing causal changes ([4] [6] [9]).

Regression to the mean follows directly from this conditioning. Suppose branch performance equals stable capability plus monthly noise. Selecting the worst branch selects both lower capability and unusually negative noise. On the next measurement, capability persists but a fresh noise draw is unlikely to be equally negative, so average performance improves. Rewarding or punishing the branch between measurements can then receive causal credit for a change that would partly have occurred without the intervention. Barnett, van der Pols, and Dobson emphasize that regression to the mean becomes more noticeable with greater measurement error and selection based on the baseline value ([4]).

Selection also shapes claims about streaks. Miller and Sanjurjo demonstrated that conditioning on positions following a run changes which observations enter the comparison. In finite sequences, the usual difference between success rates after successes and after failures can be biased even when trials are independent. Their result is a warning against using a naive benchmark for selected subsequences. A small-sample analyst must model the selection rule itself, not merely count the selected outcomes ([7]).

### Base Rates and Sample Size Answer Different Questions

A base rate describes how common an outcome, type, or transition is in a relevant reference class before case-specific evidence is considered. Sample size describes how variable the estimate or evidence is likely to be. These are distinct dimensions. A large sample from an irrelevant reference class can provide a precise but poorly targeted prior, while a small sample from a relevant process can provide noisy but useful likelihood evidence. Sound forecasting requires both a credible starting rate and a calibrated estimate of how much the new data should move it ([2] [3]).

The distinction matters when evaluating rare outcomes. Even an apparently strong result may have low positive predictive value when the tested proposition had low prior odds, the study had low power, or many alternative relationships were searched. Ioannidis modeled how power, bias, prior odds, and multiplicity jointly affect the probability that a reported finding reflects a true relationship. The model is conditional on its assumptions and does not establish that every field has a particular false-finding rate, but it shows why a significance label alone cannot substitute for sample size and pre-study plausibility ([9]).

An outside view supplies a reference distribution, while sample-size awareness controls the strength of adjustment away from that distribution. The author's synthesis is a two-stage rule: anchor on the most relevant defensible base rate, then update according to the amount and quality of independent evidence. A compelling narrative based on three cases should normally move the prior less than a comparable pattern based on 300 independent cases, unless the three cases contain unusually diagnostic evidence ([3] [6]).

### Low Power Can Exaggerate the Results That Survive

A small study has a lower probability of detecting a true effect of a given size. A subtler problem arises after conditioning on statistical significance or another selection threshold. When measurement is noisy, only estimates that happen to be unusually far from zero cross the threshold. The published or promoted subset can therefore exaggerate the magnitude of real effects, and in sufficiently weak designs can even report the wrong direction. Gelman and Carlin call these Type M, for magnitude, and Type S, for sign, errors ([6]).

This mechanism is sometimes called the winner's curse. It applies beyond scientific papers. The top salesperson in a short contest, the best fund in a short ranking period, the highest-performing advertisement among many variants, or the fastest-growing small cohort has survived a selection rule that favors positive noise. The right response is not to assume the winner has no skill. It is to shrink the observed performance toward a relevant prior, demand an independent holdout or replication, and widen uncertainty to account for the number of candidates examined. Fama and French use bootstrap simulations to distinguish luck from skill across mutual fund returns, illustrating why many funds can show extreme estimates by chance when the cross-section is large ([8]).

### Small Samples Are Not Automatically Worthless

Sample size should be judged relative to effect size, noise, dependence, and the decision at stake. A small sample can be decisive when an effect is very large, measurement is reliable, the mechanism is specific, and alternative explanations are implausible. Conversely, a very large observational dataset can mislead when selection, confounding, dependence, or measurement error dominates. The law-of-small-numbers correction is therefore not "wait for a large number" in every case; it is "represent uncertainty honestly and identify what the sample can support" ([4] [5] [9]).

The cost of delay also matters. Decisions often cannot wait for statistical certainty. A reversible pilot may rationally proceed on limited evidence because the downside is bounded and the next action will generate more information. An irreversible acquisition, medical intervention, or concentrated investment demands a higher evidential threshold. The author's synthesis is to match evidence requirements to consequence and reversibility while refusing to translate urgency into false precision. A probability range, staged commitment, or explicit stop rule preserves action without pretending that eight observations provide the stability of 800 ([5] [6]).

## Evidence

### Professional Researchers Also Neglect Sample Size

Tversky and Kahneman's 1971 questionnaire was designed to test the statistical intuitions of people with research training rather than only those of statistical novices. The replication item described a significant result from 20 observations and asked about significance in a new sample of 10. The median response of about 0.85 was far above the approximately 0.48 probability calculated under the stated assumptions, and only 9 of 84 respondents answered within the interval 0.40 to 0.60. Other items elicited similarly optimistic judgments about power and replication. The method and result support a specific claim: statistical training does not by itself guarantee an intuitive appreciation of the variability of small samples ([1] [10]).

The 1974 hospital problem tested the same mechanism in a simpler setting. A small hospital and a large hospital were assumed to have births with an equal underlying probability of a boy. Respondents often judged the hospitals equally likely to experience days above a stated extreme proportion. Sampling theory predicts more extreme daily proportions in the small hospital because fewer births permit wider proportional variation. The study links the response error to insensitivity to sample size under representativeness, although the vignette by itself does not establish how a person will reason in every real-world domain ([2]).

### Training Improves Task Performance More Easily Than Transfer

Dorothy Bishop studied 100 participants with science or social-science backgrounds using a preregistered online task that displayed samples of different sizes. Participants practiced judging whether two groups came from the same population while receiving feedback and seeing the underlying distribution. Performance on the training task improved, and 38 percent reported learning to wait for larger samples before responding. However, the learning index did not predict improvement on separate sample-size-neglect quiz items; the reported Bayes factor provided moderate support for the null relationship ([10]).

That result narrows the practical claim that simulation alone debiases judgment. Seeing repeated samples can build sensitivity to variability within the trained task, but the insight may not generalize automatically to differently framed questions. Bishop concluded that simulation may need explicit conceptual instruction to support broader transfer. The author's assessment is that organizational training should connect visual sampling exercises directly to the decisions people actually make, such as evaluating a pilot, a manager, a customer cohort, or an investment record ([10]).

### Underpowered Research Produces Both Misses and Exaggerations

Button and colleagues reviewed statistical power in neuroscience and concluded that average power was low across the studies they examined. Their review emphasized two linked consequences: low power reduces the chance of detecting a true effect, and the significant results that do appear are more likely to overestimate the effect and to replicate poorly. The authors also identified ethical costs because unreliable research consumes participants, animals, funding, and attention without producing commensurate knowledge ([5]).

Gelman and Carlin formalized a complementary design analysis. Instead of asking only whether a study has conventional power, they recommend estimating the probability that a statistically significant estimate has the wrong sign and the factor by which its magnitude is exaggerated. Their published examples show that a low-power design can have a large Type M ratio even when a Type S error remains uncommon. This matters for practical decisions because an effect can point in the correct direction yet still be too inflated to support the expected payoff, forecast, or resource allocation attached to it ([6]).

Ioannidis's model reaches a related conclusion through positive predictive value. Holding other factors constant, smaller studies have lower power and reported positive findings are less likely to identify true relationships, especially when prior odds are low, many relationships are tested, and bias affects selection or analysis. The paper is a theoretical analysis whose quantitative conclusions depend on assumed prior odds and bias, and a correction to one table was later published. Its robust decision lesson is narrower than its title: interpreting a selected result requires the study's power, multiplicity, bias, and prior plausibility, not only whether a threshold was crossed ([9]).

### Regression to the Mean Can Mimic Improvement

Barnett, van der Pols, and Dobson reviewed regression to the mean in repeated measurements. They define it as the tendency for unusually large or small initial measurements to be followed by measurements closer to the mean and show that it can make natural variation look like real change. Their review identifies two conditions that amplify the effect: greater measurement error and follow-up restricted to a subgroup selected by an extreme baseline value. They recommend addressing it through study design and appropriate analysis rather than interpreting every post-selection movement as an intervention effect ([4]).

This mechanism is directly relevant to forecasts and performance reviews. If an intervention begins only after a metric breaches an extreme threshold, the before-after comparison is selected to contain an extreme first measurement. A control group subject to the same selection rule, repeated baseline measurements, or a model that accounts for measurement error can separate part of the natural reversion from treatment effects. Without such a comparison, the direction of movement is predictable even when its cause is not ([4]).

### The Hot-Hand Reanalysis Shows Skepticism Must Be Symmetric

Miller and Sanjurjo analyzed the estimator used to compare success after streaks with success after misses in finite sequences. They proved that the estimator has a streak-selection bias whose magnitude decreases with sequence length but increases with the required streak length. When they corrected for this bias in the canonical basketball shooting data, the prior conclusion of no hot-hand effect was reversed. Their result does not validate every claimed streak; it shows that the benchmark used to dismiss a streak can itself be distorted by finite-sample conditioning ([7]).

This study is especially important for the law of small numbers because it prevents the corrective principle from becoming a slogan. "Small samples are noisy" is true but incomplete. Analysts must specify what is sampled, what is conditioned on, which estimator is used, and what its finite-sample expectation is. A debiasing method that ignores those details can create false certainty in the opposite direction ([7]).

### Financial Records Confound Skill, Luck, and Biased Inference

Rabin's model predicts that believers in the law of small numbers can infer more variation in source quality than actually exists. Applied to investment management, short noisy records can make some managers appear exceptionally skilled and others exceptionally poor even when their underlying abilities are less dispersed. The model also connects short-run reversal expectations with longer-run extrapolation, showing how apparently opposite beliefs can arise from one misspecified view of local representativeness ([3]).

Fama and French studied actively managed U.S. equity mutual funds and used bootstrap simulations to compare the cross-section of estimated performance with what luck would generate. Their aggregate results show that active-management costs appear in lower investor returns, while extreme estimated alphas require simulation to distinguish skill from chance. The study illustrates both multiplicity and selection: with many funds, some records will look extraordinary without extraordinary expected returns, and ranking on short histories can be dominated by noise ([8]).

Jin and Peng developed a later model of the law of small numbers in financial markets and tested predictions with account-level transaction data. In their model, investors expect short price trends to reverse but longer trends to persist; the mechanism generates predictions about purchases, sales, doubling down, and the disposition effect. As an NBER working paper, the study is primary research rather than a final peer-reviewed consensus. It nevertheless provides evidence that the law-of-small-numbers framework can organize observed trading patterns beyond laboratory coin-toss judgments ([11]).

## Implications

### Forecasting Requires an Evidence-Weight Decision, Not a Pattern Verdict

A forecast update should answer three questions separately: what was believed before the observation, how diagnostic the observation is under competing explanations, and how uncertain the observation is because of sample size and dependence. Small samples do not mandate no update; they usually mandate a smaller update and a wider posterior range. Rabin's model shows why short sequences can prompt overinference, while the original experiments show that people often fail to widen uncertainty when the denominator shrinks ([1] [3]).

The author's synthesis is to write the update before stating the conclusion. Record the prior or reference-class range, the sample size, the unit of observation, the number of effectively independent observations, and the likelihood of the data under at least two plausible models. Then record what would count as a replication. This format makes it harder for a streak to become a causal story merely because it is coherent, vivid, or recent ([2] [6]).

Calibration should be evaluated across repeated forecasts rather than inferred from one success. A forecaster who makes ten high-confidence predictions and gets the first three right has not yet demonstrated stable accuracy; the record remains compatible with a broad range of skill. Scoring many resolved forecasts, preserving the original probabilities, and separating domains provides more evidence than retrospective recollection of a short winning streak. This practice connects sample-size discipline with calibration and decision review ([1] [10]).

### Business Pilots Need Denominators, Holdouts, and Precommitted Rules

A pilot should identify its unit of analysis and minimum decision threshold before results arrive. Customer clicks may not be independent if the same customers return, stores may share regional shocks, and daily outcomes may be autocorrelated. Reporting the raw denominator without checking dependence can overstate effective sample size. The author's synthesis is to pair every pilot result with uncertainty, exposure duration, cohort construction, exclusions, and the number of alternatives tested ([6] [9]).

Winner selection should be followed by confirmation. If a company tests 30 advertisements and promotes the variant with the highest observed conversion, that winner was selected partly for positive noise. Reusing the same data to estimate its lift preserves the winner's curse. A holdout sample, a second preregistered experiment, or shrinkage toward the overall average gives a less biased basis for deployment. Gelman and Carlin's Type M framework explains why the selected effect may have the right sign yet still be too large for a revenue forecast ([6]).

Threshold-triggered interventions need a comparison that handles regression to the mean. A branch chosen because complaints spiked, a factory line chosen because defects surged, or a salesperson coached after an unusually poor month is likely to improve partly because the trigger selected an extreme observation. Repeated baselines, comparable untreated units, randomized rollout, or interrupted time-series designs can help separate intervention effects from natural variation. A simple before-after chart cannot make that separation ([4]).

### Investment Records Should Be Treated as Noisy Estimates, Not Identities

A short record of superior returns is evidence, but it is not a direct measure of enduring skill. The investor should ask how many independent decisions produced the record, how much market exposure explains it, how many managers were screened, whether failed funds disappeared from the dataset, and whether the strategy was specified before or after seeing the results. Multiplicity means that an extreme winner is expected somewhere in a large field even when expected skill is modest ([3] [8]).

The author's synthesis is to use a hierarchy of evidence. First examine process evidence: mandate, incentives, decision consistency, capacity, and exposure. Next estimate performance relative to a defensible benchmark over multiple market regimes. Then shrink extreme estimates toward a reference-class prior and test whether outperformance persists out of sample. Finally, distinguish a changed process from a random streak rather than mechanically expecting either reversal or continuation. Fama and French's simulations and Rabin's model support the need to distinguish luck, heterogeneity, and overinference rather than choosing one by narrative ([3] [8]).

Price streaks require the same discipline. Independent short-run noise does not become more likely to reverse because it has formed a visible sequence, but actual returns can contain time-varying expected returns, investor behavior, and changing fundamentals. Jin and Peng's model links local-representativeness beliefs to both reversal and extrapolation, while Miller and Sanjurjo show that streak estimators can be biased. The practical implication is to specify a causal and statistical model before trading on a pattern, then test it on data not used to discover it ([7] [11]).

### Scientific and Policy Claims Need Replication That Changes the Information Set

Replication is valuable when it adds independent evidence. Reanalyzing the same small dataset with many specifications may reveal robustness to modeling choices, but it does not create new observations. A new sample, a different site, or a prospectively registered test changes the information set and can reveal whether the original estimate was inflated by sampling variation or selection. Low-power studies may miss real effects, and their selected significant effects may exaggerate magnitude, so replication should estimate effect size and uncertainty rather than ask only whether a second p-value crosses a threshold ([5] [6]).

Policy pilots create a special risk because decision-makers may select sites with unusually bad outcomes, apply a program, and attribute subsequent improvement to the program. Regression to the mean predicts some improvement without treatment. Randomized or matched comparisons, multiple pre-intervention measurements, and explicit modeling of the selection rule are therefore central to causal interpretation. The evidence standard should rise when the intervention is costly, irreversible, or likely to be scaled broadly ([4]).

### Decisions Under Time Pressure Should Preserve Optionality

Waiting for a large sample can itself be costly, especially when delay sacrifices learning, market access, or safety. The author's synthesis is to separate the decision to learn from the decision to commit. A reversible, bounded pilot can proceed with weak evidence if it is designed to produce stronger evidence and has precommitted stop conditions. A large irreversible commitment should not inherit the pilot's optimistic point estimate without adjustment for sampling variation, selection, and implementation scale ([5] [6]).

Probability ranges are more honest than false precision. When data are sparse, a decision memo can show a base case, a plausible low case, and a plausible high case, with the observation count and assumptions that move the estimate. Sensitivity analysis should identify whether the action changes across that range. If the decision is robust, sparse data may be sufficient; if a small change reverses the recommendation, the value of more information is high. This is the author's synthesis of the decision discipline supported by the source evidence ([3] [6]).

A decision review should preserve what was known at the time. After an outcome, a short sequence can invite a new story that makes success or failure seem inevitable. Recording the original base rate, evidence, probability, sample limitations, and alternative explanations makes later review less vulnerable to hindsight. It also permits aggregation across many decisions, which is how an organization can learn whether its confidence is calibrated rather than merely remember a few vivid wins and losses ([1] [2]).

## Practical Framework

The following framework is the author's synthesis of the evidence. It is designed for forecasts, business pilots, manager evaluation, investment claims, and decision reviews rather than as a substitute for formal statistical analysis.

### 1. Define the Generating Process

State what produces each observation and whether observations are plausibly independent, clustered, repeated, or time-dependent. Name the mechanism that could make the process change. Without this step, the same streak can be called random noise, mean reversion, momentum, or structural change after the fact. The law-of-small-numbers literature shows that the assumed process determines whether a reversal or continuation appears intuitive ([3] [11]).

### 2. Expose the Denominator and Effective Sample

Report counts with rates, durations with returns, and the number of units with averages. Then ask whether the raw count overstates independent information because several observations share one customer, manager, market regime, or underlying event. Do not compare percentages whose denominators differ without showing the uncertainty that follows from those denominators ([1] [2]).

### 3. Reconstruct Selection

List how many candidates, metrics, subgroups, time windows, or model specifications were examined before the reported result was chosen. Record whether the case entered the analysis because it was extreme. Selection among many noisy estimates creates apparent winners and losers, while baseline selection creates regression toward the mean. The correction must address the selection rule, not merely add a generic warning that the sample is small ([4] [6] [7]).

### 4. Anchor and Update Separately

Choose a relevant reference class and record its base-rate range. Then identify what feature of the new evidence is genuinely diagnostic and update in proportion to its reliability and effective sample size. If several reference classes are plausible, show the result under each rather than selecting the class that best supports the preferred conclusion. This prevents vivid case details from erasing prior information while preserving room for real exceptions ([2] [3]).

### 5. Seek Independent Confirmation

Use a holdout, later cohort, different site, new time period, or preregistered replication. Confirmation should not reuse the same selection noise. Define in advance what result would strengthen, weaken, or falsify the claim, and evaluate effect magnitude and uncertainty rather than only a threshold label. This addresses the exaggeration and reproducibility problems identified in low-power research ([5] [6] [9]).

### 6. Match Commitment to Evidence

The author's synthesis is to classify the action by downside, reversibility, and information value. Weak evidence may justify a small reversible experiment; it rarely justifies an irreversible scale decision with a narrow forecast range. Use staged commitments, stop rules, and explicit probability ranges to keep learning possible. The goal is not paralysis until a magical sample size is reached, but action whose exposure is proportional to what the evidence can support.

The author's synthesis is that a concise decision note can contain six lines: process, denominator, selection, base rate, replication plan, and commitment limit. If any line is unknown, label it unknown. This does not eliminate uncertainty; it prevents a small sample from disguising uncertainty as a stable pattern.

## Sources

1. Tversky, A. and Kahneman, D. (1971). "Belief in the Law of Small
   Numbers." Psychological Bulletin, 76(2), 105-110.
   http://www.stats.org.uk/statistical-inference/TverskyKahneman1971.pdf [high]

2. Tversky, A. and Kahneman, D. (1974). "Judgment under Uncertainty:
   Heuristics and Biases." Science, 185(4157), 1124-1131.
   https://www.anderson.ucla.edu/sites/default/files/documents/areas/fac/accounting/Class%202%20-%20Kahneman%20and%20Tversky%20-%20Judgment%20Under%20Uncertainty%2C%20Heuristic%20and%20Biases.pdf [high]

3. Rabin, M. (2000). "Inference by Believers in the Law of Small
   Numbers." Prepublication manuscript; published in Quarterly Journal
   of Economics, 117(3), 775-816 (2002).
   http://www.econ.yale.edu/~shiller/behfin/2000-05/rabin.pdf [high]

4. Barnett, A. G., van der Pols, J. C., and Dobson, A. J. (2005).
   "Regression to the Mean: What It Is and How to Deal with It."
   International Journal of Epidemiology, 34(1), 215-220.
   https://pubmed.ncbi.nlm.nih.gov/15333621/ [high]

5. Button, K. S., Ioannidis, J. P. A., Mokrysz, C., Nosek, B. A.,
   Flint, J., Robinson, E. S. J., and Munafo, M. R. (2013). "Power
   Failure: Why Small Sample Size Undermines the Reliability of
   Neuroscience." Nature Reviews Neuroscience, 14, 365-376.
   https://doi.org/10.1038/nrn3475 [high]

6. Gelman, A. and Carlin, J. (2014). "Beyond Power Calculations:
   Assessing Type S (Sign) and Type M (Magnitude) Errors."
   Perspectives on Psychological Science, 9(6), 641-651.
   https://sites.stat.columbia.edu/gelman/research/published/PPS551642_REV2.pdf [high]

7. Miller, J. B. and Sanjurjo, A. (2018). "Surprised by the Hot Hand
   Fallacy? A Truth in the Law of Small Numbers." Econometrica, 86(6),
   2019-2047.
   https://www.econometricsociety.org/publications/econometrica/2018/11/01/surprised-hot-hand-fallacy-truth-law-small-numbers [high]

8. Fama, E. F. and French, K. R. (2010). "Luck versus Skill in the
   Cross-Section of Mutual Fund Returns." Journal of Finance, 65(5),
   1915-1947.
   http://mba.tuck.dartmouth.edu/bespeneckbo/default/AFA611-Eckbo%20web%20site/AFA611-S8C-FamaFrench-LuckvSkill-JF10.pdf [high]

9. Ioannidis, J. P. A. (2005). "Why Most Published Research Findings
   Are False." PLOS Medicine, 2(8), e124; corrected 2022.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC1182327/ [high]

10. Bishop, D. V. M. (2022). "Can We Shift Belief in the 'Law of Small
    Numbers'?" Royal Society Open Science, 9, 211028.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC8889191/ [high]

11. Jin, L. J. and Peng, C. (2024). "The Law of Small Numbers in
    Financial Markets: Theory and Evidence." NBER Working Paper 32519.
    https://www.nber.org/papers/w32519 [high]

## See Also

- `library/probabilistic-thinking-forecasting/base-rate-neglect.md` --
  separates prior frequency from the reliability of case-specific evidence.
- `library/probabilistic-thinking-forecasting/calibration-and-overconfidence.md` --
  explains how repeated scoring reveals whether confidence matches accuracy.
- `library/probabilistic-thinking-forecasting/inside-outside-view.md` --
  applies reference classes and base rates before case-specific adjustment.
- `library/probabilistic-thinking-forecasting/pre-mortems-and-post-mortems.md` --
  preserves forecasts and assumptions for review before outcomes rewrite them.
- `library/mathematics-statistics/statistical-inference.md` -- provides the
  formal statistical methods that this applied decision framework relies on.
