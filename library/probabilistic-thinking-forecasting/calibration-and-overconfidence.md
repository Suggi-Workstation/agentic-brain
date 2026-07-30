---
name: calibration-and-overconfidence
id: 20260730T113117Z
tier: library-topic
domain: probabilistic-thinking-forecasting
author: Researcher-1
tags: [calibration, overconfidence, dunning-kruger, tetlock, metacognition, confidence-intervals, brier-score]
links: [library/probabilistic-thinking-forecasting/superforecasting.md, library/probabilistic-thinking-forecasting/bayesian-reasoning.md, library/probabilistic-thinking-forecasting/inside-outside-view.md, library/psychology-behavior/cognitive-biases.md]
---

# Calibration and Overconfidence -- Why Most People Are Far More Confident Than They Are Correct, and How to Fix It

Calibration is the alignment between subjective confidence and
objective accuracy: when you say you are 70% sure, you should be right
roughly 70% of the time. Most people are catastrophically miscalibrated
-- they claim 90% confidence on judgments that turn out correct barely
50% of the time. This systematic overconfidence is not a minor quirk;
it is one of the most robust and consequential findings in the
judgment-and-decision-making literature. The good news, established
by decades of research from Philip Tetlock, the Good Judgment Project,
and the metacognition literature, is that calibration is a trainable
skill. Anyone willing to track predictions, sit with uncertainty, and
confront their own error can learn to match confidence to reality.

## Background

The study of calibration began in earnest in the 1970s, when
psychologists Sarah Lichtenstein and Baruch Fischhoff asked a
deceptively simple question: when people say they are certain, are
they actually right? In a series of experiments, they asked
participants to answer general knowledge questions and then state
their confidence in each answer as a probability. The results were
striking. When participants said they were 100% certain, they were
correct only about 80% of the time. At the 90% confidence level,
accuracy hovered around 65%. The pattern was consistent:
overconfidence was pervasive, and it grew worse as certainty
increased.

Lichtenstein and Fischhoff (1977) demonstrated that this was not a
failure of intelligence or education. Graduate students, doctors, and
experts all showed the same pattern. What made their work foundational
was the demonstration that calibration could be improved through
feedback: when participants received immediate information about
whether their answers were correct, their calibration improved
substantially. The implication was that overconfidence was not a fixed
personality trait but a skill deficit -- one that could be corrected
with practice and honest feedback.

The calibration research took a dramatic turn in the 1990s and 2000s
with the work of Philip Tetlock. His twenty-year study of expert
political judgment (1984-2005) revealed that professional forecasters
-- political scientists, economists, and intelligence analysts -- were
barely more accurate than random guessing on long-range predictions.
More importantly, the experts who appeared most confident on television
were systematically the least accurate. Tetlock's "foxes" -- thinkers
who held multiple frameworks, updated their views, and expressed
appropriate uncertainty -- consistently outperformed "hedgehogs," who
doubled down on a single big theory with high confidence.

The calibration paradigm reached its fullest expression in the Good
Judgment Project (2011-2015), an IARPA-sponsored forecasting tournament
in which Tetlock and Barbara Mellers demonstrated that ordinary
volunteers, when selected for cognitive style and trained in
probabilistic reasoning, could outperform intelligence analysts with
access to classified information. The very best performers --
superforecasters, roughly 2% of participants -- achieved near-perfect
calibration: their 70% predictions came true 70% of the time, their
90% predictions came true 90% of the time. Calibration was not an
abstract ideal; it was an achievable standard.

A parallel discovery emerged from social psychology. In 1999, Justin
Kruger and David Dunning published "Unskilled and Unaware of It," a
paper that demonstrated a compounding tragedy: the people who perform
worst on a task are also the least able to assess their own
performance. Incompetence deprives people of the metacognitive skill
needed to recognize their incompetence. Conversely, top performers tend
to underestimate their relative standing -- not because they lack
confidence, but because they assume tasks that are easy for them are
easy for everyone. The Dunning-Kruger effect is not a statement about
"stupid people thinking they are smart." It is a statement about
calibration: skill and the ability to self-assess that skill are the
same underlying capacity, and when the former is absent, so is the
latter.

## Core Concepts

### The Calibration Curve

The calibration curve is the graphical representation of the
relationship between stated confidence and actual accuracy. On the
x-axis is the forecaster's expressed probability (0% to 100%). On the
y-axis is the observed relative frequency of correctness at each
confidence level. A perfectly calibrated forecaster traces the 45-degree
identity line: 60% confidence = 60% accuracy. Most people trace a curve
that sits below the identity line, reflecting overconfidence. The
further the curve is from the diagonal, the worse the calibration.

A rarer pattern is underconfidence, where the curve sits above the
diagonal -- people are correct more often than their confidence
suggests. Underconfidence is most commonly observed at very low
confidence levels (below 30%) and among highly trained experts in
domains with clear performance feedback. Expert bridge players, weather
forecasters, and some specialized physicians show excellent calibration,
often with slight underconfidence because they are acutely aware of
what they do not know.

The calibration curve reveals a second dimension beyond simple
overconfidence: discrimination, or resolution. Discrimination measures
whether a forecaster assigns systematically higher probabilities to
events that occur and lower probabilities to events that do not. You
can be well-calibrated (your 50% predictions come true half the time)
but have zero discrimination (you assign 50% to everything). The ideal
forecaster maximizes both calibration and discrimination.

### The Brier Score: Measuring Calibration Quantitatively

The Brier score, introduced by meteorologist Glenn Brier in 1950, is
the standard metric for evaluating probabilistic forecasts. For a
single forecast with stated probability p and outcome o (1 if the event
occurs, 0 if it does not), the Brier score is (p - o)^2. For a set of
N forecasts, it is the mean of these squared errors.

The Brier score ranges from 0 (perfect forecasting) to 1 (worst
possible). A forecaster who always says 50% achieves a Brier score of
0.25 regardless of outcomes -- this is the baseline of maximum
uncertainty. A forecaster who says 100% on everything and gets half
wrong achieves 0.5. Superforecasters in the Good Judgment Project
achieved Brier scores around 0.10 to 0.15 over thousands of forecasts.

The power of the Brier score lies in its decomposition. Statistically,
the Brier score can be split into three terms: calibration (reliability),
resolution (discrimination), and uncertainty (the inherent
unpredictability of the events). This decomposition lets you diagnose
exactly why a forecaster is underperforming: are they miscalibrated
(overconfident or underconfident), or do they simply lack
discrimination (all forecasts cluster around the same probability)?

A forecaster who is always 90% confident and correct only 70% of the
time has a large calibration error. A forecaster who is always 50%
confident on everything eliminates calibration error entirely but has
zero resolution -- they provide no information. The Brier score
penalizes both failures, but it penalizes miscalibration more heavily
at extreme probabilities: being 99% sure and wrong is far more costly
than being 55% sure and wrong, because the squared error (0.99)^2 vs.
(0.55)^2 is vastly larger.

### The Overconfidence Effect: Why It Happens

Overconfidence is not a single phenomenon but a cluster of related
effects, each with distinct mechanisms. Understanding which type of
overconfidence is operating is essential for correcting it.

**Overprecision** is the tendency to be too certain that one's
judgments are accurate. It is most commonly measured through confidence
interval exercises: participants are asked to provide a 90% confidence
interval for an unknown quantity (e.g., the length of the Nile River),
and the interval captures the true value far less than 90% of the time.
Typical hit rates are 40-60% even when participants are explicitly
instructed to aim for 90%. Overprecision is the most robust form of
overconfidence and is highly resistant to debiasing.

**Overestimation** is the tendency to believe one performs better than
one actually does. Students consistently overestimate their exam scores.
Entrepreneurs overestimate their chances of success (roughly 80% of
founders believe they will succeed; roughly 80% fail). Drivers rate
themselves as above-average. Overestimation is partly driven by
motivated cognition -- people want to believe they are competent -- and
partly by the difficulty of acquiring accurate comparative data about
oneself.

**Overplacement** is the tendency to believe one ranks higher than
others on some dimension. The classic "better-than-average effect" --
93% of American drivers rate themselves above the median, a
mathematical impossibility -- is overplacement. Unlike overprecision
and overestimation, overplacement can sometimes be reversed: on tasks
perceived as difficult (e.g., juggling, computer programming among
novices), people rate themselves below average. This "worse-than-average
effect" suggests that placement judgments are sensitive to perceived
task difficulty.

### The Dunning-Kruger Effect: When Incompetence Blinds Itself

The Dunning-Kruger effect describes a specific calibration failure: the
least competent individuals in a domain dramatically overestimate their
ability, while the most competent slightly underestimate theirs. In the
original 1999 experiments, Kruger and Dunning tested participants on
humor, logical reasoning, and English grammar. Across all three domains,
participants in the bottom quartile of performance estimated they had
performed above the 60th percentile. Their actual performance was at
the 12th percentile. The gap was enormous.

The mechanism is elegant and troubling. The skills needed to perform
well in a domain -- knowledge of grammar rules, logical principles,
what makes a joke funny -- are the same skills needed to evaluate
whether one's own performance in that domain is any good. If you do not
know what a valid syllogism looks like, you cannot tell whether your
own attempted syllogism is valid. Incompetence is a double curse: it
produces poor performance and simultaneously disables the metacognitive
machinery needed to detect that poor performance.

Crucially, the Dunning-Kruger effect is not about intelligence or
character. When Kruger and Dunning gave the bottom-quartile
participants a brief training session in logical reasoning, two things
happened. Their performance improved, and -- more importantly -- their
self-assessments became dramatically more accurate. Training did not
just teach logic; it taught the metacognitive skill of recognizing bad
arguments, including one's own. The effect is not a statement that some
people are hopelessly deluded. It is a statement that calibration is a
learned skill that rides on top of domain competence.

### Metacognition and the Feeling of Knowing

Metacognition -- thinking about thinking, knowing about knowing -- is
the cognitive infrastructure on which calibration rests. Asher Koriat's
cue-utilization framework (1997) explained that when people assess how
well they know something, they do not directly inspect the strength of
their memory. Instead, they rely on cues: how easily information comes
to mind (fluency), how familiar the subject feels, how coherent the
retrieved narrative is. These cues are informative but fallible. A
well-rehearsed false narrative can feel more fluent than a fragmented
true memory.

The illusion of knowing arises when these cues are misleading. You
re-read a chapter and it feels familiar, so you conclude you know it --
but familiarity during reading is a poor predictor of recall during a
test. Retrieval practice -- closing the book and trying to recall the
material -- produces more accurate calibration because it forces you to
experience the gap between recognition and recall. Desirable
difficulties, a concept introduced by Robert Bjork, are learning
conditions that feel harder in the moment (spaced practice,
interleaving, testing) but produce more durable learning and more
accurate self-assessment.

Calibration training in educational settings follows a simple formula:
predict, test, compare, reflect. Before a quiz, students predict their
score item by item. After the quiz, they compare predictions to
outcomes. The gap is the calibration error. Repeating this cycle over
weeks systematically narrows the gap, and the students who improve
their calibration most also improve their performance most. Accurate
self-assessment drives effective self-regulation: if you know you do
not know the Krebs cycle, you study it. If you mistakenly believe you
do, you skip it.

## Evidence

Lichtenstein and Fischhoff (1977) provided the foundational
demonstration that calibration is simultaneously terrible and
improvable. In their experiments, participants' overconfidence was
robust across knowledge domains, but a single session of outcome
feedback -- telling participants whether their answer was correct after
each question -- produced significant improvement. A subsequent study
by Sharp, Cutler, and Penrod (1988) replicated the effect with
extended feedback cycles: calibration continued to improve across
multiple sessions, suggesting that the skill compounds with practice.

Tetlock's Expert Political Judgment study (1984-2005) remains the
largest longitudinal calibration study ever conducted. Tracking 284
experts and roughly 28,000 predictions over two decades, Tetlock found
that expert predictions were barely distinguishable from random chance
on the hardest questions. When experts assigned probabilities of 80%
or higher, the events they predicted occurred less than 60% of the
time. The calibration curves for most experts were dramatically below
the identity line. But the sub-group of experts who thought like foxes
-- probabilistic, self-critical, updating -- showed significantly
better calibration than the hedgehogs. The cognitive style predicted
accuracy independent of domain expertise, IQ, or political ideology.

The Good Judgment Project (2011-2015) demonstrated that calibration
can be systematically trained at scale. Thousands of volunteer
forecasters were randomly assigned to training conditions: some
received instruction in probabilistic reasoning (base rates, Bayesian
updating, avoiding cognitive biases), some were placed in teams, and
some received both. The trained forecasters, especially those in teams,
achieved Brier scores 30-40% better than the untrained control group.
The top 2% -- superforecasters -- maintained near-perfect calibration
across four years and hundreds of forecasts. Mellers, Stone, Atanasov,
et al. (2015) documented that superforecaster performance was not a
fluke: their calibration improved over time, suggesting deliberate
practice effects, and they continued to outperform controls years after
the formal tournament ended.

Kruger and Dunning (1999) provided the evidence that calibration
failure is most severe among the least competent. Across four studies
with tasks ranging from logical reasoning to grammar to humor
assessment, participants in the bottom quartile of performance
overestimated their ability by an average of 40-50 percentile points.
The effect was replicated with Cornell University undergraduates --
not a population lacking confidence -- and has been reproduced across
dozens of domains including financial literacy, medical
self-diagnosis, political knowledge, and chess skill. A 2020
meta-analysis confirmed the general pattern but noted that the effect
size varies substantially by domain and that the asymmetry (bottom
quartile overestimates, top quartile underestimates) is especially
pronounced on tasks where performance feedback is absent or ambiguous.

Field evidence for calibration training comes from intelligence and
business settings. The U.S. intelligence community, stung by the Iraq
WMD failure (a catastrophic calibration error in which analysts
assigned near-certainty to incorrect assessments), adopted
probabilistic training programs modeled on the Good Judgment Project.
A 2016 study by Mellers, Tetlock, and colleagues published in
Management Science tracked multi-year calibration improvements among
professional intelligence analysts who received structured forecasting
training. The analysts who participated showed sustained improvements
in Brier scores and calibration curves compared to controls who
received no training. In business, companies that adopted
calibration-based forecasting -- requiring managers to assign explicit
probabilities to revenue and project timelines and then score those
predictions against outcomes -- reported reduced planning errors and
more realistic capital allocation.

## Implications

For individual decision-makers, the most actionable implication is that
calibration is a trainable skill, not a fixed trait. The playbook is
simple and backed by evidence: make explicit probabilistic predictions
in a log, score them against outcomes using Brier scores, and review
the calibration curve periodically. The mere act of keeping a
prediction log reduces overconfidence because it forces you to confront
the difference between what you thought would happen and what actually
happened. Most people never do this, which is why their overconfidence
persists indefinitely. A prediction log is a calibration gym -- the
feedback loop that turns vague confidence into measurable accuracy.

Confidence interval exercises provide a fast, practical way to diagnose
and reduce overprecision. Pick ten factual questions with verifiable
answers. For each, provide a range where you are 90% confident the true
value lies. If you are well-calibrated, nine of ten answers should fall
within your ranges. Most people hit four to six on their first attempt
-- severe overprecision. Repeating the exercise weekly with different
question sets typically narrows the gap within two to three months.
This is not intelligence training; it is calibration training. The
knowledge being tested (trivia) is less important than the skill being
built (matching confidence to knowledge).

For organizations, calibration has profound implications for hiring,
performance evaluation, and strategic planning. The Dunning-Kruger
effect implies that the least competent candidates will be the most
confident in interviews -- confidence is a weak signal of competence.
Structured assessments with objective scoring outperform unstructured
interviews precisely because they reduce the opportunity for
miscalibrated confidence to masquerade as expertise. In performance
evaluation, requiring employees to self-assess against objective metrics
before receiving manager feedback -- the predict-receive-compare cycle
-- improves both self-awareness and subsequent performance.

For forecasting and risk assessment, calibration is the difference
between informed probability and dangerous certainty. A risk manager
who says "this investment has a 95% chance of success" but whose 95%
predictions actually succeed 70% of the time -- a common calibration
gap -- is systematically underestimating risk. The expected value
calculation built on that miscalibrated probability is wrong. In
high-stakes domains -- intelligence, medicine, finance, nuclear safety
-- miscalibration is not an academic concern. It kills people and
destroys capital. The solution is not to eliminate confidence but to
calibrate it: to build systems that track predictions, score them
honestly, and feed the results back to the decision-makers.

A deeper philosophical implication concerns the relationship between
confidence and competence in a society that rewards the former more
visibly than the latter. The most confident voices in any public debate
-- the pundits who speak in certainties, the commentators who never
admit error -- are statistically the least likely to be correct. The
experts worth listening to express their views in probabilities,
acknowledge uncertainty, and update when evidence changes. Calibration
is not just a forecasting skill. It is an intellectual virtue: the
disciplined alignment between what you believe and how strongly you
believe it, maintained by the habit of checking.

## Sources

1. Lichtenstein, S. & Fischhoff, B. (1977). "Do those who know more
   also know more about how much they know?" Organizational Behavior
   and Human Performance, 20(2), 159-183.
   https://doi.org/10.1016/0030-5073(77)90001-0 [high]

2. Kruger, J. & Dunning, D. (1999). "Unskilled and unaware of it: How
   difficulties in recognizing one's own incompetence lead to inflated
   self-assessments." Journal of Personality and Social Psychology,
   77(6), 1121-1134. https://doi.org/10.1037/0022-3514.77.6.1121 [high]

3. Tetlock, P. E. & Gardner, D. (2015). "Superforecasting: The Art and
   Science of Prediction." Crown Publishing Group. Chapters on
   calibration, Brier scores, and the Good Judgment Project results.
   [high]

4. Mellers, B., Stone, E., Atanasov, P., et al. (2015). "The
   psychology of intelligence analysis: Drivers of prediction accuracy
   in world politics." Journal of Experimental Psychology: Applied,
   21(1), 1-14. https://doi.org/10.1037/xap0000040 [high]

5. Griffiths, R. (2026). "Probability Calibration: Predict Like a
   Superforecaster." Expected Value Blog.
   https://expectedvalue.co.uk/blog/probability-calibration-training/
   [medium]

6. Moore, D. A. & Healy, P. J. (2008). "The trouble with
   overconfidence." Psychological Review, 115(2), 502-517.
   https://doi.org/10.1037/0033-295X.115.2.502 [high]

## See Also

- `library/probabilistic-thinking-forecasting/superforecasting.md` --
  the full superforecasting framework from which calibration training
  emerged, including the Good Judgment Project methods.
- `library/probabilistic-thinking-forecasting/bayesian-reasoning.md` --
  Bayesian updating is the mathematical framework that disciplined
  calibration supports: you cannot update correctly if your priors are
  miscalibrated.
- `library/probabilistic-thinking-forecasting/inside-outside-view.md` --
  the outside view is a calibration technique: it anchors subjective
  confidence to objective base rates, reducing overprecision.
- `library/psychology-behavior/cognitive-biases.md` -- overconfidence
  is one of the most pervasive cognitive biases; this file covers the
  broader bias landscape.
