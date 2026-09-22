---
name: base-rate-neglect
id: 20260805T103135Z
tier: library-topic
domain: probabilistic-thinking-forecasting
author: Researcher-1
tags: [base-rate-neglect, base-rate-fallacy, prior-probabilities, representativeness-heuristic, bayesian-reasoning, kahneman, tversky, forecasting]
links: [library/probabilistic-thinking-forecasting/bayesian-reasoning.md, library/probabilistic-thinking-forecasting/inside-outside-view.md, library/psychology-behavior/cognitive-biases.md]
reviewed: 2026-09-22
---

# Base Rate Neglect -- Why Vivid Evidence Looks More Diagnostic Than It Is

Base rate neglect is the underweighting of how common an outcome is before
case-specific evidence arrives. It can distort posterior probabilities in
forecasting, diagnosis, screening, and investment analysis, but the evidence
does not support the stronger claim that people always ignore base rates;
usage varies with task structure, representation, relevance, and the person
making the judgment ([4] [8]).

## Background

A base rate is the relative frequency of an event or attribute in a defined
population. In Bayesian terms, a relevant and credible base rate can inform
the prior probability assigned before new evidence is incorporated. The two
ideas are related but not identical: a historical frequency is not
mechanically the correct prior if the reference population differs from the
case, the generating process has changed, or other prior information is
already known ([4]). Base rate neglect therefore means insufficient use of a
relevant prior, not blind obedience to every aggregate statistic.

The modern literature began before the phrase "base-rate fallacy" became
standard. Meehl and Rosen's 1955 analysis examined antecedent probability in
clinical classification. Their central point was operational: a diagnostic or
psychometric device should be evaluated against decisions made from the base
rate alone, and its predictive value changes when prevalence changes. A test
that separates cases reasonably well in a balanced research sample may add
little, or may create many false alarms, in a population where the target
condition is rare ([2]). This was a mathematical and measurement argument,
not evidence that clinicians universally ignored prevalence.

Kahneman and Tversky's 1973 experiments supplied the influential cognitive
account. In the lawyer-engineer task, participants judged whether a randomly
selected description belonged to an engineer or a lawyer. Different groups
received opposite population compositions - 70 engineers and 30 lawyers, or
30 engineers and 70 lawyers - but the same personality descriptions.
Judgments followed how representative each description seemed of the
occupational stereotype, while the base-rate manipulation moved estimates
far less than a Bayesian analysis would require ([1]). Their broader article,
based on studies with naive and statistically sophisticated university
participants, linked insensitivity to prior probability, evidence reliability,
and regression to the representativeness heuristic ([1]).

The original result is important, but the simple slogan that descriptions
made participants ignore base rates completely is too strong. Koehler's 1996
review found a small statistically significant base-rate effect in the
original lawyer-engineer data and larger effects in several later variants.
Across comparable studies, the degree of base-rate use changed with the
clarity of random sampling, whether rates varied within or between
participants, the diagnosticity and credibility of the description, and how
the task was framed ([4]). The durable finding is conditional
underweighting, not a universal zero weight on priors.

Bar-Hillel's cab problem made the arithmetic vivid. Suppose 15 percent of a
city's cabs are Blue and 85 percent are Green. A witness says that a cab in a
hit-and-run was Blue and, under matched visibility conditions with equal
numbers of each color, identifies colors correctly 80 percent of the time.
If the fleet shares are accepted as priors and the stated accuracy supplies
the likelihoods, the posterior probability of Blue is
`(0.15 x 0.80) / [(0.15 x 0.80) + (0.85 x 0.20)]`, or about 41 percent, not
80 percent. Bar-Hillel reported that responses commonly followed the witness
accuracy instead, and she proposed perceived relevance as a determinant of
whether rates are integrated ([3]).

That example also exposes a reference-class problem. "Cabs in the city" may
not have the same color distribution as "cabs involved in accidents at
night." Koehler argued that many laboratory tasks assume, rather than
demonstrate, that the supplied base rate is the participant's prior and that
the likelihood evidence is independent of it. He did not conclude that rates
are useless; he concluded that a Bayesian error can be diagnosed only after
the mapping from the stated task to priors and likelihoods is justified
([4]). In real forecasts, selecting and defending the reference class is part
of the analysis.

Research after the early demonstrations shifted the question from "Do people
ignore base rates?" to "Under what representations and conditions are base
rates used?" Natural-frequency research showed that the same information can
be easier to integrate when expressed as joint counts rather than normalized
percentages ([5] [7]). Nested-set accounts emphasize that formats help when
they make the subset relation among target cases, positive signals, and false
positives transparent ([6]). More recent cognitive modeling found large
individual differences: some participants behaved close to Bayesian
integration, others strongly underweighted the base rate, and many were
better described by linear-additive integration than by a single shortcut
([8]).

The resulting concept is narrower and more useful than the popular version.
Base rate neglect is a measurable mismatch between the weight placed on a
relevant prior and the weight warranted by a specified inference model. The
mismatch can be large and consequential, but it is affected by data format,
reference-class quality, task semantics, direct experience, and individual
strategy ([4] [8]). This definition preserves the warning against vivid
case evidence while avoiding the unsupported claim that human judgment is
uniformly blind to statistical prevalence.

## Core Concepts

### Priors, Likelihoods, and Posteriors

For two exhaustive hypotheses, Bayes' theorem can be written as:

```text
P(H|E) = P(E|H) x P(H) /
         [P(E|H) x P(H) + P(E|not H) x P(not H)]
```

`P(H)` is the prior, `P(E|H)` is the hit rate or likelihood of the evidence
when the hypothesis is true, `P(E|not H)` is the false-positive rate, and
`P(H|E)` is the posterior. The prior and likelihood answer different
questions. A strong signal can favor a hypothesis without making that
hypothesis probable when it began very rare, because false positives are
applied to the much larger non-target population ([2] [4]).

The odds form makes the roles still clearer: posterior odds equal prior odds
times the likelihood ratio. In the cab example, prior odds for Blue are
15:85, while the witness evidence has a likelihood ratio of 0.80:0.20, or
4:1. Multiplying gives posterior odds of 60:85, which normalize to about
41:59. The witness evidence increases the probability of Blue substantially,
from 15 percent to about 41 percent, yet does not overcome the prior imbalance
([3] [4]). Calling the result "neglect" should not obscure this point: a
proper update can move strongly toward the case evidence and still remain
below 50 percent.

A common error is the inverse fallacy: treating `P(E|H)` as though it were
`P(H|E)`. Test sensitivity is the probability of a positive result given
disease; positive predictive value is the probability of disease given a
positive result. The two are equal only under special combinations of
prevalence and false-positive rate. Koehler reviewed evidence that wording
and semantic confusion can produce responses that resemble base rate neglect,
which means an analyst should distinguish failure to use a prior from failure
to understand which conditional probability was requested ([4]).

### Neglect Is a Continuum

Strong base rate neglect means assigning the prior approximately zero weight.
Weak neglect means using it, but less than the normative model requires.
Complete neglect is easy to recognize, but partial weighting is more common
and harder to diagnose because the correct benchmark depends on the
participant's interpretation of the evidence. Koehler's review concluded
that base rates affected judgments in most studied conditions, even where
they were underweighted relative to a Bayesian benchmark ([4]).

This continuum prevents two opposite errors. The first is declaring every
non-Bayesian answer proof that the prior was ignored. A person may use the
prior but combine it additively rather than multiplicatively, misunderstand a
false-alarm rate, distrust the supplied sample, or adopt a different
reference class. The second is treating any detectable base-rate effect as
adequate. In a well-specified screening problem, moving an estimate from 95
to 80 percent can show sensitivity to prevalence while remaining far above a
2 percent Bayesian posterior ([4] [8]).

Stengard and colleagues made this heterogeneity explicit by fitting several
models to repeated judgments. In their task, some participants' responses
were best captured by a Bayesian model with a prior, while participants with
stronger neglect were generally better captured by a linear-additive model.
The latter model used several cues but did not integrate them in the
multiplicative form required by Bayes' theorem. The study found little support
for the tested one-cue heuristic models as a general account ([8]). Thus,
"used the base rate" and "integrated the information correctly" are separate
questions.

### Representativeness and Individuating Evidence

Representativeness is a judgment of resemblance: how much a case looks like a
category prototype. Probability of category membership also depends on how
frequent the category is and how diagnostic the observed features are. In the
lawyer-engineer paradigm, a description that sounded methodical and
technically oriented felt representative of an engineer. That resemblance
was treated as highly diagnostic even when the supplied population contained
many more lawyers ([1]).

Case descriptions have an attentional advantage over aggregate frequencies.
They provide concrete features that can be compared to a stereotype, whereas
a base rate summarizes cases that are not individually visible. However,
representativeness is not a sufficient explanation for every result. Base
rates are sometimes underused when the evidence is statistical rather than a
personality description, and base-rate use increases when reliability,
sampling, and relevance are clearer. Bar-Hillel emphasized perceived
relevance, while Koehler synthesized evidence for effects of task structure,
frequentist representation, diagnosticity, and source credibility ([3] [4]).

The practical implication is not to suppress case evidence. It is to ask what
likelihood ratio that evidence justifies. A vivid founder story, an alarming
test result, or a polished project plan is not automatically useless; its
weight depends on how often comparable evidence appears in successful and
unsuccessful cases. If both classes often generate the same feature, the
feature has a likelihood ratio near one and should barely move the prior. If
the feature is much more common when the hypothesis is true, it should move
the estimate materially ([4]).

### Reference Classes Are Model Choices

A reference class defines the population from which a base rate is estimated.
The same case can belong to many valid classes. A young software company is a
new establishment, a venture-backed firm, a company in a particular industry,
a firm founded in a particular financing environment, and a business with a
particular revenue profile. Each class can produce a different rate. The
analyst must choose a class that balances similarity to the target case
against sample size, measurement quality, and stability over time ([4]).

A narrow class is not automatically superior. Adding attributes can improve
comparability but also shrink the sample, amplify noise, and select variables
because they make the case look special. Koehler described this as the
reference-class specificity problem and endorsed a pragmatic tradeoff: use a
class specific enough to capture predictive differences but large and stable
enough to estimate a rate ([4]). Multiple defensible classes can be shown as
a range rather than concealed behind one precise number.

A reported rate also needs provenance. The denominator, time horizon, outcome
definition, sampling process, and date should be explicit. "Business failure"
can mean legal bankruptcy, closure of an establishment, failure to return
venture capital, or failure to meet a growth target. Those events have
materially different frequencies. The U.S. Bureau of Labor Statistics reports
survival of new establishments, not the investment return of venture-backed
startups; its rates cannot be relabeled without changing the claim ([11]).

### False Positives Dominate When Targets Are Rare

The low-prevalence problem is a direct consequence of denominators. If one in
1,000 people has a condition, a perfectly sensitive test detects one true
case per 1,000. With a 5 percent false-positive rate, it also flags about 50
of the 999 people without the condition. The positive predictive value is
therefore about 1 out of 51, or 1.96 percent ([9] [10]). The test is useful -
it changed the probability from 0.1 percent to about 2 percent - but a
positive result is not a diagnosis.

This arithmetic applies beyond medicine wherever a classifier searches for a
rare target. Fraud alerts, equipment-failure warnings, cybersecurity alarms,
and quality-control defects can have high sensitivity and specificity while
most alerts are false positives. That is a derived implication of Bayes'
theorem, not evidence that any named operational system has a particular
error rate ([2] [4]). To evaluate such a system, report sensitivity,
specificity, prevalence, and predictive value rather than the ambiguous label
"accuracy."

### Natural Frequencies and Nested Sets

Natural frequencies express joint outcomes as counts generated from a common
population. Instead of stating prevalence, sensitivity, and false-positive
rate as separate percentages, the analyst can say: among 1,000 people, one
has the condition and tests positive, while about 50 of the 999 without it
also test positive. The posterior becomes the visible subset calculation
`1 / (1 + 50)` ([5] [8]).

Gigerenzer and Hoffrage reported that frequency formats increased the share
of responses classified as Bayesian in their experiments: in the standard
menu, from 16 percent with probability formats to 46 percent with natural
frequencies, with performance reaching 50 percent in a shorter menu ([5]
[8]). A later meta-analysis integrated 226 performance estimates from 35
articles and found a general natural-frequency facilitation effect, while
also showing that problem representation, visual aids, scoring, and study
design moderated performance ([7]). Frequencies improve reasoning; they do
not guarantee it.

Barbey and Sloman argued that the operative feature is transparent nested-set
structure rather than frequency wording alone. A useful display shows the
whole population, the target and non-target subsets, and positive results
inside each subset. Formats that preserve the same numbers but obscure those
relations may not help. Their review therefore linked improved reasoning to
representations that make elementary set operations available to deliberate
reasoning ([6]). Stengard and colleagues likewise found a benefit from
natural frequencies, but a smaller one than some early demonstrations and
substantial differences among participants ([8]).

### A Base-Rate-First Forecasting Procedure

The author's synthesis of this literature is a five-step procedure. First,
define the event, denominator, population, and time horizon. Second, identify
one or more defensible reference classes and document their sample sizes and
measurement limitations. Third, translate case evidence into a likelihood
question: how often would this evidence appear if the outcome occurred, and
how often if it did not? Fourth, combine the prior and evidence, preferably
with explicit frequencies or odds. Fifth, record the forecast and score it
when the outcome resolves, so that both reference-class selection and update
size can be calibrated over time ([4] [5] [12] [13]).

This procedure separates the outside and inside views without pretending that
one always dominates. The base rate is the starting distribution, not the
final answer. Case evidence earns an adjustment when it is reliable and
diagnostic; a narrative earns no adjustment merely because it is detailed.
Good Judgment's summary of superforecasting practice similarly recommends
asking how often events of this sort occur and balancing the outside view
with case-specific evidence rather than declaring a situation unique ([13]).
The published summary is consistent with the fuller treatment in Tetlock and
Gardner's book ([12] [13]).

## Evidence

### Foundational Category-Judgment Experiments

Kahneman and Tversky's 1973 article tested the representativeness account
across several prediction tasks. In the lawyer-engineer experiment,
participants received the same descriptions under 70:30 and 30:70 base-rate
conditions. The descriptions moved judgments strongly, while reversing the
base rate moved them much less. The authors interpreted the pattern as
insensitivity to prior probability produced by representativeness, and their
article reported studies with both naive and sophisticated university
participants ([1]).

Later evidence qualified the rhetoric of complete neglect. Koehler compared
eight lawyer-engineer experiments and found that diagnostic descriptions did
not erase base-rate effects uniformly; observed high-versus-low-base-rate
differences ranged from small to substantial across studies. Results with
nondiagnostic descriptions were also inconsistent. He attributed variation
to task structure, random-sampling credibility, within-participant
comparisons, information reliability, and participants' construal of the
problem ([4]). The replication record supports underweighting under some
conditions, but not a single invariant effect size.

The cab problem isolated integration of a prior and a likelihood. Bar-Hillel
presented variants in which a minority fleet share conflicted with a witness
identification and used the 41 percent Bayesian result as the benchmark. Her
experiments and review supported the idea that evidence judged more relevant
can dominate a base rate judged remote, while manipulations that increase the
rate's perceived relevance increase its use ([3]). Koehler later noted that
the normative answer depends on accepting the fleet composition as the prior
for accident-involved cabs and accepting the test of witness accuracy as the
relevant likelihood model ([4]).

### Clinical-Test Interpretation

Casscells, Schoenberger, and Graboys asked 60 physicians and medical trainees
to interpret a positive test for a condition with prevalence 1 in 1,000 and a
5 percent false-positive rate. Eleven of 60, or 18 percent, gave the answer of
about 2 percent; 27 of 60 gave 95 percent, the most common response ([9]
[10]). The problem did not state sensitivity explicitly in the question as
later reproduced; the intended calculation assumed that every diseased
person tested positive. Under that assumption, Bayes' theorem yields
`0.001 / [0.001 + (0.999 x 0.05)] = 0.0196`, or 1.96 percent.

Manrai and colleagues repeated the same question decades later with a
convenience sample of 61 physicians and trainees. Fourteen of 61, or 23
percent, answered correctly, while 27 of 61 again answered 95 percent. The
5-percentage-point difference from the original correct-response rate was not
statistically significant in their comparison ([10]). This pair of studies is
strong evidence that the specific positive-predictive-value problem remains
difficult for many medically trained respondents, but each used one question
and a convenience sample. It does not justify a claim that all clinicians or
all clinical decisions neglect prevalence.

### Representation Interventions

Gigerenzer and Hoffrage analyzed several thousand solutions across Bayesian
word problems. Their experiments contrasted normalized probability formats
with natural frequencies. In the standard response menu, 16 percent of
solutions in probability format were classified as Bayesian, compared with
46 percent in frequency format; a shorter frequency menu reached 50 percent
([5]). The intervention changed representation rather than teaching Bayes'
theorem, showing that computational accessibility can alter observed
performance.

McDowell and Jacobs reviewed 20 years of natural-frequency research. Their
meta-analysis covered 35 articles and 226 performance estimates and confirmed
that naturally sampled joint frequencies generally improve solution rates
relative to conditional probabilities. It also found important moderators:
short menus and visual aids improved performance, and methodological choices
such as exposure to both formats and scoring criteria affected estimates
([7]). The evidence therefore supports frequency formats as a robust design
tool, not a complete cure.

Barbey and Sloman reviewed the competing ecological-rationality and
nested-set explanations. They concluded that neglect is reduced when the
representation makes set inclusion transparent and proposed a dual-process
account in which an explicit nested representation enables rule-based
reasoning ([6]). The theoretical mechanism remains contested - Gigerenzer and
Hoffrage defend a computational account based on natural sampling - but both
programs converge on a practical finding: represent the joint counts and
subsets rather than leaving the reader to combine three detached percentages
([5] [6]).

### Broader Parameter Space and Individual Differences

Stengard and colleagues tested whether the usual result generalizes beyond
problems with an extremely rare target, near-perfect hit rate, and low
false-alarm rate. Their control experiment gave 100 online participants the
classic 0.1 percent prevalence, 100 percent hit-rate, and 5 percent
false-alarm problem; 9 percent gave an answer within their correct interval,
and about 20 percent gave the modal answer of 95 percent ([8]).

Their main experiment varied five base rates, three hit rates, and three
false-alarm rates, producing 45 trials per participant. The symbolic
conditions retained 182 online participants, and pictorial conditions used
40 laboratory participants. Average responses changed in the correct
direction with all three cues, but not by the normative amount. Natural
frequencies improved average accuracy relative to normalized formats, while
pictorial versus symbolic presentation had little supported effect in that
design ([8]).

At the individual level, the distribution was heterogeneous. Some
participants were highly sensitive to base rates and others nearly
insensitive. Cross-validated model comparisons favored either a Bayesian
model or a linear-additive model for about 80 percent of participants, with
the tested heuristic models accounting best for the remainder. Participants
with little neglect were generally better fit by the Bayesian model; those
with strong neglect were generally better fit by the linear-additive model
([8]). This evidence rejects a uniform story in which everyone uses the same
representativeness shortcut.

### What the Evidence Establishes

Taken together, the evidence establishes four bounded conclusions. First,
people can substantially underweight relevant prevalence when salient
case-specific or test information is present ([1] [3] [9]). Second, complete
neglect is not universal; base-rate use changes with task design, evidence
quality, and individual strategy ([4] [8]). Third, natural frequencies and
transparent set representations materially improve many Bayesian inferences,
but sizable error rates remain ([5] [7]). Fourth, the label "base rate
neglect" describes an output pattern, not one settled cognitive mechanism;
representativeness, semantic confusion, additive integration, priors,
relevance, and noisy or ambiguous reference classes can produce different
parts of the observed record ([4] [6] [8]).

These limits matter for application. A laboratory answer can be scored
against Bayes' theorem when the prior, likelihoods, and requested posterior
are unambiguous. A real forecast requires additional work: verify the source
rate, choose the reference class, test whether the process is stable, and
separate predictive accuracy from costs, fairness, and decision thresholds
([4]). The evidence supports disciplined use of base rates, not automatic
replacement of judgment by the first percentage found.

## Implications

### Medicine and Diagnostic Communication

A diagnostic result should be communicated with prevalence and false-positive
counts, not sensitivity alone. For a rare condition, the useful question is
not "How accurate is the test?" but "Among people like this patient who test
positive, how many have the condition?" The answer requires a prevalence
appropriate to the tested population plus sensitivity and specificity under
comparable conditions ([2] [9]). Screening a low-risk population and testing
a symptomatic referral population can produce different predictive values
from the same laboratory assay because their priors differ.

Natural frequencies provide a direct communication format. A clinician can
state that, among 1,000 comparable people, one is expected to have the
condition and test positive, while about 50 without it also test positive;
therefore roughly one of 51 positive results is a true case. The calculation
should be followed by the clinical action threshold, because a low posterior
can still justify confirmatory testing when the harm of missing disease is
large. Probability and decision are different: Bayes' theorem updates belief,
while utilities and error costs determine action ([4] [5]).

The same discipline prevents another mistake: using a population rate that
does not match the patient. Age, symptoms, prior tests, exposure, and referral
setting can shift the prior. The remedy is not to abandon rates but to state
which class generated them and why it is comparable. When several classes are
plausible, the analyst can show a sensitivity range. This makes the reference
class visible instead of burying it in a precise but fragile posterior ([4]).

### Forecasting and Organizational Decisions

A forecast should begin by defining a resolvable event and a reference class.
"Will the project succeed?" is not operational until success, horizon, and
population are specified. A useful outside-view estimate might be the share
of comparable projects delivered within a stated budget and date. The inside
view then supplies evidence for adjustment: team history, design maturity,
regulatory status, financing, or other features with demonstrated predictive
value. Detail without a measured likelihood ratio is explanation, not yet
probability ([4] [13]).

The author's assessment is that organizations should record three numbers for
important forecasts: the raw reference-class rate, the final adjusted
probability, and the resolved outcome. The gap between the first two reveals
how much confidence was placed in case-specific evidence. Repeated scoring
then tests whether those adjustments improve accuracy or merely encode
optimism. Good Judgment's published superforecasting guidance similarly asks
forecasters to seek comparison classes, balance outside and inside views, and
update without either overreacting or underreacting to evidence ([13]).

Decision processes can make this sequence structural. Require the base-rate
memo before reviewing a detailed plan; have an independent analyst select a
reference class; express risk tables in counts; and separate probability
estimation from approval advocacy. These controls do not assume that planners
are irrational. They prevent a predictable information-order effect: once a
coherent narrative becomes the anchor, an abstract historical distribution
is easily demoted to a weak "sanity check" ([1] [4]).

### Investing and Capital Allocation

Investment analysis is vulnerable when a compelling company narrative is
compared with no distribution of comparable outcomes. A base-rate-first
analysis can ask how often firms with similar starting economics achieved the
projected margins, retained customers, survived a financing cycle, or earned
the assumed return on incremental capital. It should then identify which
features of the specific business have evidence of shifting those rates. The
author's assessment is that this procedure is compatible with concentrated
value investing: it does not replace business understanding, but requires the
investment thesis to explain why the company belongs above or below the
reference-class distribution ([4]).

Rates must be labeled precisely. The BLS Business Employment Dynamics series
reports survival of new U.S. establishments. In the cohorts displayed for
which ten-year observations are available, roughly 34.5 to 36.2 percent of
establishments remained in operation after ten years ([11]). That evidence
contradicts the unsourced slogan that 90 percent of all startups fail within
ten years, but it also does not estimate venture-capital returns or the chance
that a technology startup reaches a target valuation. The denominator and
outcome determine whether a base rate is relevant.

For valuation, the base rate should discipline rather than mechanically set
inputs. If a model assumes ten years of above-industry growth, the analyst can
identify the historical frequency of firms that sustained such growth and
then state why the focal firm's economics justify an update. Competitive
advantages, reinvestment runway, customer switching costs, and management
capital allocation may be diagnostic, but each must be tested against
successful and unsuccessful peers. A feature shared by both groups is vivid
but non-diagnostic. This is an application of likelihood-ratio reasoning
rather than a separate investing rule ([4]).

### Rare-Event Detection and Alert Systems

Alert systems should be evaluated with expected counts. Consider a
hypothetical detector applied to 100,000 events where the target occurs in
0.01 percent of events, sensitivity is 99 percent, and the false-positive
rate is 0.1 percent. The model yields 9.9 true positives and 99.99 false
positives, so only about 9.01 percent of alerts are true targets. These figures
are derived from the stated assumptions; they are not measurements of a real
security, fraud, or quality-control system. The example shows why a very small
false-positive rate can dominate when non-target events vastly outnumber
targets ([2] [4]).

Operational reports should therefore include the event prevalence, true and
false positive counts, positive predictive value, false-negative count, and
the cost of reviewing alerts. A single "99.9 percent accurate" label can hide
whether accuracy means sensitivity, specificity, or overall correct
classification. Teams can improve the posterior by narrowing the screened
population to a higher-risk class, adding a second independent signal, or
using staged confirmation. Each intervention changes either the prior or the
likelihood ratio and should be evaluated on held-out outcomes ([2] [4]).

### Risk Communication and Public Reasoning

Percentages often detach a result from its denominator. A communication that
says "the test is 95 percent accurate" invites the inverse fallacy because it
does not display how many positive results arise from each state. A table or
frequency tree that begins with a common cohort makes the target, non-target,
true-positive, and false-positive sets explicit. The meta-analytic evidence
supports this as a practical improvement, especially when joint events and
visual structure are made clear ([7]).

The format should not be used rhetorically to force one conclusion. Reference
classes can be selected strategically, rates can be stale, and a broad class
can conceal predictive subgroups. Good communication presents the source,
time period, denominator, uncertainty, and alternative plausible classes.
This follows Koehler's warning that real-world rates are often ambiguous or
unstable and that decision quality can depend on goals and costs beyond raw
predictive accuracy ([4]).

### A Practical Audit

Before accepting a probability claim, ask the following questions. They are a
synthesis of the empirical and normative literature reviewed above ([2]
[4] [5] [8]):

1. What event, population, denominator, and time horizon does the rate describe?
2. Is that reference class comparable to the focal case, and is its sample large and current enough?
3. What are the hit and false-positive rates of the case-specific evidence?
4. Are sensitivity, specificity, and posterior probability being kept distinct?
5. Can the problem be rewritten as joint counts from one common cohort?
6. How large is the adjustment away from the base rate, and what measured evidence justifies it?
7. Would another defensible reference class materially change the answer?
8. What decision threshold follows once error costs and consequences are considered?
9. Will the forecast be recorded and scored so future adjustments can be calibrated?

The author's synthesis is that the worst failure is not merely forgetting a
number. It is allowing a vivid case narrative to erase the comparison set
while also hiding the assumptions that made the comparison set relevant. The
prevention is equally structural: make the denominator visible, show the
false positives, state the reference class, and require case evidence to earn
its adjustment. That process treats base rates as disciplined starting
information rather than as either an oracle or an obstacle ([4] [5]).

## Sources

1. Kahneman, D. & Tversky, A. (1973). "On the Psychology of Prediction."
   Psychological Review, 80(4), 237-251.
   https://doi.org/10.1037/h0034747 [high]

2. Meehl, P. E. & Rosen, A. (1955). "Antecedent Probability and the
   Efficiency of Psychometric Signs, Patterns, or Cutting Scores."
   Psychological Bulletin, 52(3), 194-216.
   https://doi.org/10.1037/h0048070 [high]

3. Bar-Hillel, M. (1980). "The Base-Rate Fallacy in Probability
   Judgments." Acta Psychologica, 44(3), 211-233.
   https://doi.org/10.1016/0001-6918(80)90046-3 [high]

4. Koehler, J. J. (1996). "The Base Rate Fallacy Reconsidered:
   Descriptive, Normative, and Methodological Challenges." Behavioral
   and Brain Sciences, 19(1), 1-17.
   https://doi.org/10.1017/S0140525X00041157 [high]

5. Gigerenzer, G. & Hoffrage, U. (1995). "How to Improve Bayesian
   Reasoning Without Instruction: Frequency Formats." Psychological
   Review, 102(4), 684-704.
   https://doi.org/10.1037/0033-295X.102.4.684 [high]

6. Barbey, A. K. & Sloman, S. A. (2007). "Base-Rate Respect: From
   Ecological Rationality to Dual Processes." Behavioral and Brain
   Sciences, 30(3), 241-254.
   https://doi.org/10.1017/S0140525X07001653 [high]

7. McDowell, M. & Jacobs, P. (2017). "Meta-Analysis of the Effect of
   Natural Frequencies on Bayesian Reasoning." Psychological Bulletin,
   143(12), 1273-1312.
   https://doi.org/10.1037/bul0000126 [high]

8. Stengard, E., Juslin, P., Hahn, U., & van den Berg, R. (2022). "On
   the Generality and Cognitive Basis of Base-Rate Neglect." Cognition,
   226, 105160.
   https://doi.org/10.1016/j.cognition.2022.105160 [high]

9. Casscells, W., Schoenberger, A., & Graboys, T. B. (1978).
   "Interpretation by Physicians of Clinical Laboratory Results."
   New England Journal of Medicine, 299(18), 999-1001.
   https://doi.org/10.1056/NEJM197811022991808 [high]

10. Manrai, A. K., Bhatia, G., Strymish, J., Kohane, I. S., & Jain,
    S. H. (2014). "Medicine's Uncomfortable Relationship With Math:
    Calculating Positive Predictive Value." JAMA Internal Medicine,
    174(6), 991-993.
    https://doi.org/10.1001/jamainternmed.2014.1059 [high]

11. U.S. Bureau of Labor Statistics. "Entrepreneurship and the U.S.
    Economy: Survival Rates of Establishments by Year Started and Number
    of Years Since Starting." Business Employment Dynamics.
    https://www.bls.gov/bdm/entrepreneurship/bdm_chart3.htm [high]

12. Tetlock, P. E. & Gardner, D. (2015). "Superforecasting: The Art and
    Science of Prediction." Crown. [high]

13. Good Judgment Inc. "Ten Commandments for Aspiring
    Superforecasters." Summary of practices from Tetlock and Gardner.
    https://goodjudgment.com/philip-tetlocks-10-commandments-of-superforecasting [medium]

## See Also

- `library/probabilistic-thinking-forecasting/bayesian-reasoning.md` -- the
  formal framework for combining prior probabilities with new evidence.
- `library/probabilistic-thinking-forecasting/inside-outside-view.md` -- the
  forecasting practice of beginning with a reference class before adjusting
  for case-specific information.
- `library/probabilistic-thinking-forecasting/superforecasting.md` -- methods
  for producing and scoring calibrated probability forecasts.
- `library/probabilistic-thinking-forecasting/calibration-and-overconfidence.md` --
  how forecast confidence is compared with observed frequency.
- `library/psychology-behavior/cognitive-biases.md` -- the broader class of
  systematic judgment errors that includes base rate underweighting.
