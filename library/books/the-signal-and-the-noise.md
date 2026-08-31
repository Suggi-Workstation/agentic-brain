---
name: the-signal-and-the-noise
id: 20260831T101748Z
tier: library-topic
domain: books
author: Library Runner
tags: [nate-silver, signal-and-noise, prediction, forecasting, bayesian-reasoning, calibration, probability, uncertainty]
links: [library/probabilistic-thinking-forecasting/bayesian-reasoning.md, library/probabilistic-thinking-forecasting/superforecasting.md, library/books/the-black-swan-taleb.md]
---

# The Signal and the Noise -- Why So Many Predictions Fail but Some Do Not

"The Signal and the Noise: Why So Many Predictions Fail -- but Some
Don't" (2012) is Nate Silver's argument that most predictions fail
because forecasters mistake noise for signal, overestimate their
certainty, and refuse to update their beliefs when new evidence
arrives. Drawing on case studies from weather forecasting, earthquake
prediction, baseball, poker, elections, economics, climate science,
and terrorism, Silver builds a case for probabilistic thinking
grounded in Bayes' theorem as the discipline that separates
forecasters who improve from those who do not. The book is not a
mathematics text -- it is a book-length argument for intellectual
humility in the face of uncertainty.

## Background

Nate Silver (born 1978) is an American statistician, writer, and
forecaster best known as the founder of FiveThirtyEight, a website
that aggregated polling data and applied statistical models to
political elections. Silver first gained public attention during the
2008 U.S. presidential election, when his model correctly predicted
the winner in 49 of 50 states. Before entering political forecasting,
Silver had spent years in baseball analytics, developing PECOTA
(Player Empirical Comparison and Optimization Test Algorithm), a
system for projecting Major League Baseball player performance that
relied on comparing current players to historical "comparable" players
and calculating ranges of probable outcomes rather than single point
estimates [1]. He also spent several years as a professional online
poker player, reportedly earning approximately $400,000 over a
three-year period, an experience that shaped his thinking about risk,
variance, and the difference between skill and luck in uncertain
environments [2].

Silver's intellectual lineage connects to several traditions. The
most important is Bayesian statistics, named for the 18th-century
English minister and mathematician Thomas Bayes, whose theorem
provides a formal method for updating the probability of a hypothesis
as new evidence arrives. Silver explicitly positions himself against
the "frequentist" school of statistics associated with Ronald Fisher,
which dominates academic statistics teaching but, in Silver's view,
relies on overly rigid hypothesis testing and arbitrary significance
levels that rarely hold in real-world conditions [1]. Silver also
draws on the work of psychologist Philip Tetlock, whose
twenty-year study of expert political judgment found that
specialist "hedgehog" forecasters -- those who explain the world
through a single grand theory -- performed worse than "fox"
forecasters, who draw on many ideas and remain willing to revise
their beliefs [3]. This fox-hedgehog distinction, which Tetlock
adapted from Isaiah Berlin (who in turn drew on the ancient Greek
poet Archilochus), becomes one of the book's organizing metaphors.

The book was published by Penguin Group on September 27, 2012, in the
United States, roughly one month before the presidential election in
which Silver would correctly predict all 50 states. The timing was
propitious: after election night on November 6, the book's sales
jumped 800% on Amazon, and it became the No. 1 Best Non-Fiction Book
on Amazon for 2012 [1]. The Wall Street Journal named it one of the
ten best nonfiction books of 2012. In 2013, the Phi Beta Kappa
Society awarded it the book award in science, recognizing
"outstanding contributions by scientists to the literature of
science" [1]. The book has been translated into more than a dozen
languages, including German, Italian, Spanish, Japanese, Chinese,
Korean, and Finnish editions.

The cultural moment mattered. The early 21st century had already
produced a string of catastrophic prediction failures: the September
11 attacks, the 2003 Iraq War intelligence failures, Hurricane
Katrina, and the 2008 financial crisis. The "big data" revolution was
also underway, with the explosion of digital information promising
answers to every question. Silver's central warning -- that more data
produces more noise as fast as it produces more signal, and that the
volume of data alone improves nothing without disciplined thinking --
cut against the techno-optimism of the era [3]. The book arrived at
the intersection of two anxieties: that experts could not predict the
events that mattered most, and that the information age was drowning
us in data without making us wiser.

Climate scientist Michael E. Mann offered the most prominent
criticism of the book, arguing that Silver analyzed the "hard
science" of climate trends with the same approach used for the
"social phenomena" of voter preferences, which Mann characterized as
"laden with subjective and untestable assumptions" [1]. This
criticism highlights a genuine tension in the book: Silver's
 Bayesian framework is general enough to apply across domains, but
the quality of its inputs varies enormously between physical sciences
(where underlying laws are well understood) and social sciences
(where they are not). Murray Cantor, an IBM Distinguished Engineer,
praised the book for correctly describing the discipline of making
predictions "without explicitly invoking the math," reaching a broad
audience with compelling examples despite leaving out the underlying
mathematics [1].

## Core Concepts

### Signal and Noise

The book's title metaphor comes from signal processing, where "signal"
is the meaningful information a receiver wants to extract and "noise"
is everything else -- interference, distortion, irrelevant
fluctuation. Silver applies this metaphor to prediction: the signal
is the genuine pattern or relationship in the data that allows you to
anticipate future outcomes; the noise is the random variation,
measurement error, and spurious correlation that mimics signal but
carries no predictive power [4]. The fundamental challenge of
prediction is separating the two.

Silver's critical insight is that the growth of data does not
inherently improve prediction. As the total volume of available
information increases, the amount of noise grows at least as fast as
the amount of signal. More data means more opportunities to find
patterns that do not exist, to overfit models to historical
coincidences, and to cherry-pick evidence that confirms pre-existing
beliefs [3]. The proliferation of data can actually worsen
predictions when forecasters mistake the noise it generates for
signal, producing "convincingly precise yet faulty predictions"
[3]. This is the book's most counterintuitive claim and its most
important warning: information abundance without disciplined
interpretation is a liability, not an asset.

### Bayesian Reasoning as a Thinking Discipline

Silver devotes an entire chapter to Bayes' theorem, which he
describes not primarily as a mathematical formula but as a framework
for thinking about uncertainty. The theorem states that the
probability of a hypothesis being true, given some new evidence, can
be calculated from three quantities: the prior probability of the
hypothesis (before the new evidence), the probability of observing
the evidence if the hypothesis is true, and the probability of
observing the evidence if the hypothesis is false [4]. In essence,
Bayes' theorem tells you how much to revise your belief when new
information arrives.

Silver argues that good forecasters think Bayesianly even when they
do not compute the formula explicitly. The Bayesian approach
"encourages us to hold a large number of hypotheses in our head at
once, to think about them probabilistically, and to update them
frequently when we come across new information that might be more or
less consistent with them" [5]. This is a discipline of intellectual
humility: you begin with a prior belief, you acknowledge that it
might be wrong, and you adjust it incrementally as evidence
accumulates rather than clinging to it or abandoning it wholesale
based on a single data point.

The contrast Silver draws is with "frequentist" statistics, the
approach taught in most university statistics courses, which
emphasizes hypothesis testing at arbitrary significance levels
(typically p < 0.05). Silver criticizes this approach for reducing
complex questions to binary accept-or-reject decisions, for assuming
ideal experimental conditions that rarely hold in practice, and for
encouraging the false belief that a single study can definitively
confirm or refute a hypothesis [1]. The Bayesian approach, by
contrast, treats every piece of evidence as a nudge to a probability,
never a definitive verdict.

### Calibration: The Measure of a Forecast

Silver identifies calibration as the single most important test of a
forecast. Calibration measures whether a forecaster's stated
probabilities match the observed frequency of outcomes. If a
forecaster says there is a 40% chance of rain, and over many
forecasts it actually rains about 40% of the time, the forecasts are
well calibrated. If it rains 20% or 60% of the time, they are not
[6]. Calibration is distinct from accuracy: a forecaster who always
predicts the climatological average will be well calibrated but not
very accurate, while a forecaster who makes bold predictions that are
sometimes spectacularly right and sometimes spectacularly wrong may
be accurate on average but poorly calibrated.

Silver uses weather forecasting as his model of a field that has
improved its calibration over time. The National Weather Service, he
reports, produces precipitation forecasts that are approximately 25%
more accurate and temperature forecasts approximately 10% more
accurate than raw computer model output alone, because human
meteorologists supplement the models with judgment [5]. More
importantly, when the National Weather Service forecasts a 40% chance
of rain, it rains approximately 40% of the time -- the forecasts are
well calibrated [5]. By contrast, local television weather
forecasters in Kansas City were found to provide much worse forecasts
than the National Weather Service and were unapologetic about it, with
one stating "Accuracy is not a big deal" -- because television
rewards ratings, not accuracy [5]. The Weather Channel exhibits a
slight "wet bias," overestimating low-probability rain events because
viewers are angrier when caught without an umbrella than when they
carry one unnecessarily [5].

### The Fox and the Hedgehog

Borrowing from Philip Tetlock's research, Silver distinguishes
between two types of forecasters. Hedgehogs are specialists who
believe in "governing principles about the world that behave as
though they were physical laws" [7]. They are confident, ideologically
committed, and tend to make bold predictions derived from their
favored theory. Foxes are "scrappy creatures who believe in a plethora
of little ideas and in taking a multitude of approaches toward a
problem" [7]. They are intellectually eclectic, willing to draw on
multiple frameworks, and quicker to adjust when evidence contradicts
their beliefs.

In Tetlock's twenty-year study, foxes significantly outperformed
hedgehogs in political forecasting accuracy. Silver argues that this
pattern generalizes: predictions typically fail when hedgehog
forecasters ignore new information that conflicts with their
worldview [7]. The hedgehog's weakness is not lack of intelligence or
expertise but lack of flexibility. A hedgehog economist who believes
in a particular model of the economy will interpret every data point
through that model, treating disconfirming evidence as noise and
confirming evidence as signal. The fox, holding multiple models
simultaneously, is better positioned to recognize when one model is
failing and shift weight to another.

### The Distinction Between Risk and Uncertainty

Silver draws on Frank Knight's distinction between risk and
uncertainty, a concept central to the book's argument. Risk, as
Knight defined it in 1921, refers to situations where the
probabilities of different outcomes are known or calculable -- a
roulette wheel, a hand of poker, an insurance actuarial table.
Uncertainty (sometimes called "Knightian uncertainty") refers to
situations where the probabilities themselves are unknown and
perhaps unknowable [8]. Silver argues that many prediction failures
occur when forecasters treat uncertainty as if it were risk --
dressing up an incalculable unknown with the trappings of a
calculable gamble with discrete odds [7].

This distinction is most vivid in Silver's discussion of the 2008
financial crisis. The rating agencies that assigned AAA ratings to
mortgage-backed securities used mathematical models that assumed
housing prices would not decline nationally (they had not in the
data the models were built on) and that the correlation between
mortgage defaults in different regions was low [4]. These assumptions
converted genuine uncertainty -- what would happen to housing prices
in a national downturn, an event outside the historical data -- into
seeming risk, producing precise-sounding probability estimates that
concealed enormous ignorance. The models were mathematically
sophisticated but built on assumptions that were, in hindsight,
fatally wrong [4]. The cardinal mistake, as Silver describes it, is
"dressing up uncertainty -- an incalculable unknown -- with risk, a
highly calculable gamble with discrete odds" [7].

### Aggregation and the Wisdom of Crowds

Silver argues that combining independent forecasts consistently
improves accuracy. The Survey of Professional Forecasters, a
quarterly poll produced by the Federal Reserve Bank of Philadelphia,
is "about 20 percent more accurate than the typical individual's
forecast at predicting GDP, 10 percent better at predicting
unemployment, and 30 percent better at predicting inflation" [5].
Aggregation works because individual forecasters have different
information, different models, and different biases; averaging across
them cancels idiosyncratic errors while preserving the signal they
share. Silver applied this principle in his own election forecasting,
aggregating multiple polls rather than relying on any single survey
[5].

However, aggregation has limits. It works best when the individual
forecasts are independent -- if they all rely on the same
information or the same model, averaging produces no benefit. Silver
notes that aggregating earthquake predictions would not help because
seismologists lack the basic understanding of earthquake mechanisms
needed to make predictions worth averaging [5]. Aggregation improves
forecasts when the underlying signal exists and individual forecasters
are capturing parts of it; it cannot manufacture signal where none
exists.

## Evidence

### Weather Forecasting: The Success Story

Silver uses meteorology as his primary example of a forecasting field
that has improved dramatically over decades. The National Weather
Service has become roughly 350% more accurate over 25 years,
particularly in hurricane forecasting [9]. Three-day hurricane
landfall predictions that were impossible 25 years ago are now
accurate enough to enable timely evacuations [9]. This improvement
has real human value: a 2024 National Bureau of Economic Research
study found that improved hurricane forecasts led to a 19% reduction
in total hurricane-related costs, averaging approximately $5 billion
per major hurricane in benefits -- far exceeding the $250 million
cumulatively spent on the Hurricane Forecast Improvement Project
from 2009 to 2019 [10].

Silver attributes this success to several factors. First, the
underlying physics of the atmosphere is well understood, providing a
solid theoretical foundation for models. Second, meteorologists
produce probabilistic forecasts rather than deterministic ones,
expressing uncertainty explicitly rather than hiding it. Third, the
forecasting system has strong feedback loops: meteorologists can
check their forecasts against actual weather, identify systematic
biases, and correct them. Fourth, human judgment supplements
computational models: at the National Weather Service, meteorologists
adjust raw model output based on experience, improving precipitation
forecasts by about 25% and temperature forecasts by about 10%
relative to the models alone [5].

The contrast with local television weather is instructive. A study of
Kansas City stations found that local forecasters provided much worse
predictions than the National Weather Service and were unconcerned
about accuracy because their incentives were aligned with ratings,
not precision [5]. The Weather Channel showed a systematic "wet bias"
-- overestimating the probability of rain at the low end because
viewers penalize missed rain more than they reward correctly forecast
sunshine [5]. These cases illustrate Silver's broader point: forecast
quality depends on institutional incentives, not just technical
capability. Where accuracy is rewarded, forecasts improve. Where it
is not, forecasts degrade even when the underlying science is sound.

### Earthquake Prediction: The Persistent Failure

If weather forecasting is Silver's success story, earthquake
prediction is his cautionary tale. Despite decades of effort and
significant funding, seismologists cannot predict the timing,
location, or magnitude of individual earthquakes with any useful
precision [11]. The fundamental problem is that the relevant
processes occur miles underground, where direct observation is
impossible. Weather forecasters can look at the sky and measure
atmospheric conditions from satellites and weather stations;
seismologists must infer the state of fault systems from indirect
signals at the surface [11].

Silver documents the history of failed earthquake prediction
attempts, including notable false alarms and missed predictions. The
Parkfield, California prediction experiment, which installed
dense instrumentation on a segment of the San Andreas Fault that
had produced magnitude 6 earthquakes at roughly regular intervals,
waited years beyond the predicted window for the next event [11].
Silver uses this case to illustrate that even when a pattern appears
to exist in historical data, it may be noise rather than signal --
particularly when the physical mechanism behind the pattern is not
understood. Unlike weather, where the governing equations are known,
the physics of earthquake nucleation involves complex, chaotic
processes in heterogeneous rock that resist both observation and
modeling.

The lesson Silver draws is not that earthquake prediction is
impossible, but that it cannot be forced by statistical pattern
matching alone. The fields where forecasting has improved -- weather,
elections, baseball -- all have a solid understanding of the
underlying process. Where that understanding is absent, more data and
more sophisticated statistics cannot substitute for it. Aggregating
earthquake predictions, Silver notes, would do no good because the
individual predictions are not good enough to benefit from
combination [5].

### The 2008 Financial Crisis: A Systematic Failure

Silver devotes his opening chapter to the 2008 financial crisis as
the book's central case study of prediction failure. He identifies
four parties whose bad assumptions produced the crisis: the rating
agencies (Moody's, S&P, Fitch) that assigned AAA ratings to
mortgage-backed securities; the banks that originated and packaged
the mortgages; the regulators who failed to constrain the risk; and
the homebuyers and investors who assumed housing prices would
continue rising [4].

The rating agencies' models assumed that historical patterns of
mortgage default would persist, that housing prices would not decline
nationally (as they had not in the decades the models were trained
on), and that regional housing markets were sufficiently
uncorrelated that geographic diversification reduced risk [4]. Each
assumption was reasonable in isolation and catastrophically wrong in
combination. When housing prices declined nationally for the first
time since the Great Depression, defaults rose across regions
simultaneously, and the AAA-rated securities turned out to be backed
by assets whose value had collapsed. The models had converted genuine
uncertainty -- what would happen in a scenario outside the historical
data -- into seeming risk, producing precise probability estimates
that concealed the ignorance beneath [7].

Silver argues that this was not a failure of statistical methodology
but a failure of the forecasters' assumptions. The mathematical
models were sophisticated; the assumptions embedded in them were
not. The hedgehog forecasters at the rating agencies and banks
believed in their models the way a ideologue believes in a theory,
and they ignored or dismissed evidence that the housing market was
behaving differently than their models predicted [7]. The Bayesian
discipline Silver advocates -- holding multiple hypotheses, treating
models as provisional, updating beliefs when evidence contradicts
assumptions -- is precisely what the financial system failed to
practice.

### Political Forecasting: Polls and Pundits

Silver's own field, political forecasting, provides evidence for the
value of aggregation and probabilistic thinking. He reports that
political pundits and experts "usually don't do much better than
chance when forecasting political events, and usually do worse than
crude statistical models" [12]. The pundits who appear on television
are selected for confidence and narrative coherence, not forecasting
accuracy. They make deterministic predictions ("Obama will win Ohio")
rather than probabilistic ones, and they are rarely held accountable
for their track record because the media environment does not
systematically measure it.

Silver's own approach was to aggregate polls, weight them by sample
size and recency, adjust for house effects (systematic biases in
individual pollsters), and produce probabilistic forecasts expressed
as win probabilities rather than binary predictions. In 2008, his
model correctly predicted 49 of 50 states; in 2012, he predicted all
50 [1]. Silver is careful to note that this success does not prove
his model is correct in any absolute sense -- a well-calibrated
forecast can be wrong on any individual call, and a poorly calibrated
one can be right by luck. The test is calibration over many forecasts,
not the outcome of a single election [6].

## Implications

### For Forecasting Practitioners

The book's most direct audience is people who make predictions
professionally or semi-professionally: economists, meteorologists,
epidemiologists, intelligence analysts, sports modelers, financial
analysts. Silver's prescriptions for this audience are concrete.
Express uncertainty: replace point forecasts ("GDP will grow 2.1%")
with probability distributions ("GDP will grow between 1.5% and 2.8%
with 90% confidence"). Measure calibration: track the relationship
between stated probabilities and observed outcomes over many forecasts
and correct systematic biases. Seek independence: combine forecasts
from models and forecasters that use different information and
different approaches, and be suspicious when independent methods
converge for the wrong reasons. Think Bayesianly: start with a prior,
update it with new evidence, and resist the temptation to cling to a
single model or abandon it based on one data point [4] [5].

These prescriptions challenge common institutional practices. Most
organizations reward confident, precise predictions and punish
admissions of uncertainty. An economist who says "I think there is a
65% chance of a recession next year" sounds less authoritative than
one who says "A recession is coming." But the probabilistic statement
is more honest and more useful -- it allows the decision-maker to
weigh the forecast against other information and to plan for multiple
outcomes. The institutional incentive to appear certain produces
forecasts that are poorly calibrated and less useful than they could
be [5].

### For Decision-Makers and Consumers of Forecasts

For people who use forecasts but do not make them -- investors,
policymakers, managers, ordinary citizens -- the book offers a
framework for evaluating forecast quality. Do not judge a forecast by
whether a single prediction came true; a 70% probability forecast that
fails was not necessarily wrong, and a 30% probability forecast that
succeeds was not necessarily right. Judge forecasters by their
calibration over many predictions: do their stated probabilities
match observed frequencies? Be wary of forecasters who never express
uncertainty, who never update their predictions, or who explain every
outcome as consistent with their theory after the fact. Distinguish
between fields where the underlying process is understood (weather,
elections) and fields where it is not (earthquakes, economics, stock
prices), and discount forecasts accordingly [4] [5].

Silver's argument has particular force for investors. The stock
market, in his analysis, is a domain where prediction is
extraordinarily difficult because the system is reflexive (predictions
affect the thing being predicted), the noise-to-signal ratio is high,
and the incentives reward confident-sounding forecasts over
calibrated ones. He notes that the efficient market hypothesis, while
not literally true, is close enough to true that consistently beating
the market through prediction is extremely rare [4]. The implication
is not that investors should give up but that they should approach
the market with the same humility a good meteorologist brings to a
hurricane forecast: express uncertainty, plan for multiple outcomes,
and resist the illusion that more data or more sophisticated models
will convert uncertainty into calculable risk.

### For the Broader Culture of Expertise

The book's deepest implication is about the relationship between
expertise and humility. In a culture that increasingly demands
confident, binary answers from experts -- will the economy grow? who
will win the election? is the climate warming? -- Silver argues that
the most honest and useful thing an expert can do is express
uncertainty in probabilistic terms. This is not a retreat from
expertise but a more rigorous form of it. The forecaster who says
"there is a 40% chance of X" is claiming less than one who says "X
will happen," but the claim is testable, falsifiable, and useful in a
way that the confident prediction is not.

This has implications for how institutions select and reward experts.
If the media rewards hedgehogs -- confident, theory-driven, narrative
coherent -- with airtime and influence, while foxes -- uncertain,
probabilistic, multi-model -- are dismissed as wishy-washy, then the
public receives worse forecasts than it could. Silver's own career
illustrates the alternative: by publishing his methodology, expressing
his predictions as probabilities, and building a track record over
multiple election cycles, he demonstrated that probabilistic
forecasting could be both accurate and compelling to a broad
audience [1]. The book is, in part, an argument that this model
should become the norm rather than the exception.

### For Science and the Reproducibility Crisis

The book's argument intersects with the broader reproducibility crisis
in science, which was gaining public attention around the time of
publication. Silver's critique of frequentist hypothesis testing --
that it reduces complex questions to binary significance tests at
arbitrary thresholds, that it encourages p-hacking (finding
statistically significant results by testing many hypotheses), and
that it treats a single study as definitive rather than as one
incremental update to a probability -- anticipated concerns that
would become central to the replication crisis in psychology,
medicine, and social science [4]. The Bayesian framework Silver
advocates treats every study as a piece of evidence that shifts a
prior, never as a standalone verdict. This is closer to how science
actually works in practice -- a finding is not accepted because one
study achieved p < 0.05, but because it replicates across studies,
methods, and labs, gradually shifting the scientific consensus.

Silver's emphasis on calibration also applies to scientific
forecasting in domains like epidemiology and climate science. During
disease outbreaks, forecasters must predict case counts, spread
rates, and intervention effects under enormous uncertainty, with
incomplete data and rapidly changing conditions. The discipline of
expressing uncertainty probabilistically, tracking calibration, and
updating forecasts as new data arrives -- the practices Silver
praises in weather forecasting -- are directly applicable to
epidemic forecasting, where overconfident predictions can lead to
both panic and complacency. The COVID-19 pandemic, which occurred
after the book's publication, would provide a dramatic illustration
of both the need for probabilistic forecasting and the consequences
of its absence.

### Connection to Value Investing

For value investors, the book connects to several principles in the
Buffett and Munger school. Charlie Munger's advocacy of a
"latticework of mental models" -- drawing on multiple disciplines
rather than a single framework -- mirrors Silver's praise of foxes
over hedgehogs [7]. Warren Buffett's insistence on margin of safety
-- demanding that the price be significantly below intrinsic value to
account for uncertainty -- parallels Silver's argument that
forecasters should express uncertainty rather than pretending to
precision they do not have [4]. The 2008 financial crisis case study
illustrates what happens when investors treat uncertainty as risk:
the rating agencies' models assigned precise probabilities to
events whose true probabilities were unknowable, and the resulting
false confidence led to catastrophic losses [4] [7]. The Bayesian
discipline Silver advocates -- start with a prior, update with
evidence, never treat a single data point as definitive -- is close
kin to the incremental, evidence-weighted approach to valuation that
value investors practice.

## Sources

1. Wikipedia. "The Signal and the Noise." 
   https://en.wikipedia.org/wiki/The_Signal_and_the_Noise [high]

2. Wikipedia. "Nate Silver."
   https://en.wikipedia.org/wiki/Nate_Silver [high]

3. Shortform. "The Signal and the Noise by Nate Silver: Book Overview."
   https://www.shortform.com/blog/the-signal-and-the-noise-nate-silver [medium]

4. Shortform. "The Signal and the Noise Book Summary by Nate Silver."
   https://www.shortform.com/summary/the-signal-and-the-noise-summary-nate-silver [medium]

5. The New Republic. "Nate Silver and the Future of Prediction."
   https://newrepublic.com/article/111243/tomorrow-today [high]

6. StackExchange (Cross Validated). "How can we judge the accuracy of
   Nate Silver's predictions?" (citing Silver's definition of
   calibration).
   https://stats.stackexchange.com/questions/239134/how-can-we-judge-the-accuracy-of-nate-silvers-predictions [medium]

7. Bookforum. Chris Wilson. "The Signal and the Noise."
   https://www.bookforum.com/print/1904/nate-silver-s-the-signal-and-the-noise-10254 [medium]

8. Farnam Street (fs.blog). "Nate Silver: The Difference Between Risk
   and Uncertainty."
   https://fs.blog/the-difference-between-risk-and-uncertainty [medium]

9. The Philadelphia Inquirer. "'The Signal and the Noise': Secrets of
   a master numbers cruncher."
   https://www.inquirer.com/philly/entertainment/20121023__The_Signal_and_the_Noise___Secrets_of_a_master_numbers_cruncher.html [medium]

10. Yale Climate Connections. "The National Hurricane Center set an
    all-time record for forecast accuracy in 2024."
    https://yaleclimateconnections.org/2025/02/the-national-hurricane-center-set-an-all-time-record-for-forecast-accuracy-in-2024/ [high]

11. Medium (Andrew Dawson). "Book Summary of The Signal and the Noise."
    https://andrewjdawson2016.medium.com/book-summary-of-the-signal-and-the-noise-why-so-many-predictions-fail-but-some-dont-2058a2c6c081 [low]

12. LessWrong. "Some highlights from Nate Silver's The Signal and the
    Noise."
    https://www.lesswrong.com/posts/rGj2K8vu5qQCTWCar/some-highlights-from-nate-silver-s-the-signal-and-the-noise [low]

## See Also

- `library/probabilistic-thinking-forecasting/bayesian-reasoning.md` --
  the formal framework Silver advocates as a thinking discipline for
  updating beliefs under uncertainty.
- `library/probabilistic-thinking-forecasting/superforecasting.md` --
  Tetlock's research program that extends the fox-hedgehog findings
  into a methodology for producing calibrated forecasters.
- `library/probabilistic-thinking-forecasting/calibration-and-overconfidence.md` --
  the measurement discipline Silver identifies as the single most
  important test of a forecast.
- `library/books/the-black-swan-taleb.md` -- Taleb's complementary
  argument that rare, unpredictable events dominate history and that
  our statistical tools are blind to them.
- `library/books/thinking-fast-and-slow.md` -- Kahneman's account of
  the cognitive biases that cause forecasters to mistake noise for
  signal and overestimate their own accuracy.
- `library/probabilistic-thinking-forecasting/black-swan-theory.md` --
  the theoretical underpinning of Taleb's critique of forecasting,
  which Silver engages with directly in the book.