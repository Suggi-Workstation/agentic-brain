---
name: ergodicity-and-path-dependent-decision-making
id: 20260921T120751Z
tier: library-topic
domain: probabilistic-thinking-forecasting
author: Librarian
tags: [ergodicity, path-dependence, time-averages, ensemble-averages, multiplicative-growth, risk-of-ruin, kelly-criterion]
links: [library/probabilistic-thinking-forecasting/expected-value-decision-trees.md, library/probabilistic-thinking-forecasting/black-swan-theory.md, library/probabilistic-thinking-forecasting/scenario-planning-and-analysis.md]
---

# Ergodicity Changes Rational Choice -- Average Outcomes Can Mislead a Path-Dependent Decision-Maker

Ergodicity determines whether an average across many possible outcomes describes what one decision-maker is likely to experience through time. When wealth compounds, losses alter the base exposed to every later outcome, so a favorable expected value can coexist with declining typical wealth or ruin; sound decisions must therefore match the averaging rule to the process being lived ([1] [2]).

## Background

Ergodicity entered decision theory from statistical mechanics, where it addresses a precise substitution: under suitable conditions, the long-run time average of an observable along one trajectory equals its expectation across an ensemble of possible states. The substitution is powerful because it permits a difficult dynamical question about what happens through time to be replaced by a simpler probabilistic average. It is not automatic. Peters and Gell-Mann define the relevant property as convergence, with probability one, of the finite-time average of an observable to a time-independent expectation value as the averaging interval grows ([2]). Peters later argued that growth processes common in economics often lack this property for wealth itself, making the distinction consequential rather than terminological ([1]).

The distinction separates two questions that ordinary language often compresses into the word "average." An ensemble average asks what would be obtained by averaging many independent realizations at the same time. A time average asks what one realization accumulates as events occur sequentially. A casino, insurer, or pooled group may approximate an ensemble by spreading independent risks across many simultaneous members. An individual, firm, or fund that cannot reset its history instead experiences one path, with each result changing the state from which the next result begins ([2]). The two perspectives agree for the relevant observable only when the process has the required ergodic property.

The modern controversy has old roots. Early probability theory evaluated favorable gambles by expected monetary change. Daniel Bernoulli's response to the St. Petersburg paradox introduced logarithmic utility, linking the value of an additional unit of wealth to existing wealth. In the twentieth century, John Kelly derived a fraction-of-capital rule that maximizes the asymptotic exponential growth rate of capital in repeated betting with information. Kelly explicitly distinguished a reinvested, nonterminating game from a setting in which a fixed dollar could be wagered each week without reinvestment: the former calls for logarithmic growth, while the latter calls for expected gain on each independent dollar ([3]). Leo Breiman subsequently established rigorous optimality properties for favorable repeated games, including long-run dominance results for the log-optimal strategy under the paper's assumptions ([4]).

These results did not end the debate. Paul Samuelson accepted that maximizing geometric growth can make higher terminal wealth overwhelmingly likely over long sequences, but showed that this does not make the rule optimal for every finite horizon or every utility function. His counterexamples demonstrate that an investor with a different specified terminal-utility objective can rationally reject the growth-optimal strategy even for a very long sequence ([5]). The disagreement is therefore partly about the objective. Growth optimality asks which policy maximizes long-run compounding along a path. Expected utility permits objectives that value terminal outcomes differently and need not coincide with long-run growth.

Ergodicity economics reframes this history by making the dynamics explicit before choosing the quantity to optimize. Under purely additive dynamics, changes in wealth can serve as an ergodic observable, so maximizing expected change aligns with maximizing long-run change. Under purely multiplicative dynamics, changes in log wealth can serve as the corresponding observable, so maximizing expected log change aligns with maximizing long-run exponential growth ([2]). The framework does not establish that every real decision is additive or multiplicative, nor that every decision-maker must maximize wealth growth. Its durable contribution is the diagnostic question: does the average being calculated represent what the decision-maker can experience through time?

This topic belongs in probabilistic thinking rather than pure probability theory because its central use is procedural. It does not require proving an ergodic theorem or building a stochastic-process model. It requires identifying whether outcomes add, compound, reset, pool, or cross an absorbing boundary before treating an expectation as a decision criterion. That identification connects expected-value reasoning to survival, path dependence, scenario analysis, and the separation of a good probabilistic average from a good decision rule.

## Core Concepts

### Ensemble averages and time averages answer different questions

Suppose a random process has possible states X. The expectation E[X] is an ensemble quantity: it weights the possible states by their probabilities. It can be interpreted as an average across many independent realizations observed at the same point in time. A time average follows one realization through repeated transitions and averages what actually occurs along that path. Ergodicity, stated for a particular observable and process, is the condition that permits these quantities to be treated as equivalent in the long run ([1] [2]). A process is not simply "ergodic" for every imaginable quantity; the observable matters.

This qualification prevents a common error. Wealth itself can fail to be ergodic even when a transformation of wealth has stationary increments whose time and ensemble averages agree. Peters and Gell-Mann identify absolute wealth changes as the useful quantity under additive dynamics and changes in log wealth as the useful quantity under multiplicative dynamics ([2]). The transformation is not cosmetic. It specifies what accumulates consistently through time.

An ensemble average remains real and useful when resources are actually pooled or risks are spread across independent units. If one thousand insured houses face approximately independent fire risks and premiums and claims are pooled, the insurer can experience something closer to the ensemble distribution than any one homeowner. If one entrepreneur must repeatedly expose the same capital to a sequence of compounding outcomes, there is no simultaneous population of independent personal balance sheets available to average together. The author's synthesis is that a decision memo should identify the physical or institutional mechanism that realizes the claimed average: repetition through time, pooling across entities, diversification across independent exposures, or no such mechanism.

### Additive and multiplicative dynamics produce different rational benchmarks

In an additive process, an outcome changes wealth by a fixed amount:

W(t + 1) = W(t) + delta-W.

If a fair coin adds 10 units on heads and subtracts 5 units on tails, the absolute gain or loss does not depend on current wealth. Repetition sums increments. Under the independent additive model analyzed by Peters and Gell-Mann, the long-run rate of change in wealth converges to the expected increment, so expected-value reasoning describes temporal performance for that observable ([2]). A loss does not mechanically shrink the size of every later gain because the increments are specified in units, not percentages.

In a multiplicative process, an outcome scales current wealth:

W(t + 1) = W(t) x r.

If a fair coin multiplies wealth by 1.5 on heads and by 0.6 on tails, the expected one-period factor is 1.05, which looks favorable. Yet the long-run factor for an equal mix of outcomes is the geometric mean, the square root of 1.5 x 0.6, approximately 0.95. The PLOS experiment by Meder and colleagues uses this example to show a positive expectation alongside negative time-average growth ([6]). Repetition multiplies factors, so log returns add. The expected log factor, not the expected factor, governs the asymptotic exponential growth rate under the model ([2] [6]).

The arithmetic mean is pulled upward by rare large outcomes, while the geometric mean records the compounding effect borne by a continuing path. This does not make the arithmetic mean false. Across a sufficiently large ensemble, average wealth can rise because a small set of very wealthy realizations dominates the mean. At the same time, most individual paths can shrink. The two statements describe different distributions and different averaging operations ([1] [6]).

### Path dependence begins when present outcomes change future opportunity

A process is path-dependent when the state reached along the way affects later possibilities or payoffs. Multiplicative compounding creates a basic form of path dependence because every percentage change acts on the wealth remaining after prior changes. A 50 percent loss followed by a 50 percent gain does not restore the starting value: the gain applies to the smaller base. This arithmetic fact is a special case of the broader principle that sequential exposure cannot be evaluated by averaging percentage changes before compounding them ([2] [3]).

Pure multiplication by a fixed multiset of factors gives the same final product regardless of their order ([2]). Real decisions add stronger path dependence through constraints. Margin calls, minimum capital requirements, debt covenants, health thresholds, project cancellation, and loss of access to financing can make intermediate states decisive. Once a threshold is crossed, later favorable outcomes may no longer be available. Vanhoyweghen and Ginis study this issue by introducing an absorbing ruin boundary into an additive setting; the boundary prevents a ruined path from returning to the ensemble average and thereby breaks the relevant equivalence ([8]).

An absorbing state is a condition that cannot be exited under the model. Literal bankruptcy at zero is the clearest financial example, but the logic extends to any irreversible exclusion: loss of a license, depletion of a nonrenewable reserve, death of an organism, or termination of a project. The author's synthesis is that "Can the process continue after this outcome?" is a more important question than "Is the expectation positive?" whenever adverse states remove future trials.

### Ruin is not an ordinary negative outcome

Expected value treats each outcome according to probability and magnitude, but it does not by itself encode whether an outcome ends participation. A strategy can have high expected terminal wealth because rare successes are enormous while still giving most paths a poor result. If some losses create an absorbing state, the decision-maker cannot rely on future favorable repetitions to repair the damage. The relevant opportunity set has changed.

Kelly's analysis illustrates the distinction between maximizing expected capital and maximizing long-run growth. In his noisy-channel betting model, wagering all capital could maximize expected capital, yet continued play would make bankruptcy overwhelmingly likely; a fractional wager maximized the exponential growth rate instead ([3]). Breiman formalized related long-run properties for favorable games ([4]). These are model-dependent results, not a universal command to use the Kelly formula. They establish a general lesson: bet selection and bet size are separate decisions, and a favorable edge does not justify exposure large enough to destroy the ability to continue.

Ruin can also be practical rather than mathematical. A 70 percent drawdown may not set wealth to zero, but it can violate an investor's liquidity needs, trigger redemptions, or make recovery infeasible within the available horizon. The author's assessment is that the absorbing boundary should be defined by the actual mission constraint, not automatically by zero. A household, business, endowment, and insurer can face different effective boundaries even when they hold the same asset.

### The Kelly criterion links edge, sizing, and long-run growth

Kelly's criterion chooses the fraction of current capital that maximizes expected log wealth under a specified repeated-bet model. Its defining objective is asymptotic exponential growth, and its theoretical appeal follows from the additive behavior of log wealth under multiplicative repetition ([3]). Peters' analysis of geometric Brownian motion similarly derives an optimal leverage by maximizing time-average growth and shows why expected return alone can recommend excessive leverage when the underlying process is non-ergodic ([11]).

The criterion has boundaries. Kelly assumed a known probabilistic structure, repeated opportunities, reinvestment, and an objective centered on long-run growth. Parameter error can make a nominally optimal fraction too large. Finite horizons, consumption needs, taxes, transaction costs, correlated losses, changing opportunity sets, and nonfinancial objectives can all alter the decision. Samuelson's critique is decisive against treating geometric growth as the unique expression of rationality for every utility function and every finite horizon ([5]). The practical mental model is therefore not "always use full Kelly." It is "size a favorable exposure so that the path remains viable under estimation error and adverse sequences."

### Expected value is conditional, not obsolete

Ergodicity does not refute expected value. It identifies when an expected value of a particular observable maps to temporal experience and when it does not. Expected monetary value remains appropriate for genuinely additive, repeatable exposures, for pooled independent risks, and for decisions whose objective is explicitly an ensemble or aggregate quantity. Even under multiplicative dynamics, expectation values remain useful for pricing, accounting, or describing the distribution across realizations. The error is to infer without further argument that expected wealth equals the growth experienced by a continuing individual path ([1] [2]).

Expected utility theory also does not literally require belief in parallel worlds. Doctor, Wakker, and Wang argue that expected utility is a representation of preferences over lotteries and that Peters' critique overstates the role of ergodicity in mainstream economics ([9]). Ford and Kay similarly argue that growth optimization supplies one objective rather than a complete general theory of choice under uncertainty, because people can rationally value security, consumption, or terminal outcomes differently ([10]). The ergodicity response is that the dynamics still determine which transformations yield meaningful long-run rates, and empirical risk preferences may adapt to those dynamics ([6] [7]).

The author's synthesis is a layered rule. First specify the process and the objective. Second determine which quantity is additive through time or otherwise maps to the mission. Third use expected values only after identifying the observable whose expectation answers that question. Fourth test finite-horizon and boundary effects rather than assuming that an asymptotic theorem settles a near-term decision.

### A practical diagnostic for path-dependent choices

Before accepting a favorable average as a recommendation, ask five questions:

1. Does the outcome add a fixed amount, multiply the current state, or follow another dynamic?
2. Is the decision genuinely one-shot, repeatable with reset, or sequential with reinvestment?
3. Can losses cross a boundary that removes future choices?
4. Is risk pooled across independent entities, or must one entity live through one path?
5. Is the objective expected terminal value, long-run growth, survival to a horizon, consumption, or another stated goal?

This diagnostic is the author's synthesis from the theoretical and experimental sources ([1] [2] [5] [6] [8]). It does not calculate the answer. It prevents a category error before calculation begins.

## Evidence

### Theoretical results establish the ensemble-time gap

Kelly's 1956 paper provides an early formal demonstration that maximizing expected capital and maximizing long-run capital growth can prescribe different wagers. In the paper's repeated noisy-channel game, an all-in wager can maximize expected capital while leading to bankruptcy with probability one under indefinite continuation. Kelly instead chooses a fraction that maximizes the expected logarithm of capital and shows that, among fixed allocation rules in his setting, it eventually stays ahead with probability one ([3]). The result is strong but conditional: it concerns a repeated, nonterminating game with specified probabilities and fixed allocation policies.

Breiman's 1961 analysis generalized the mathematical treatment of favorable repeated games. He compared growth and goal-attainment criteria and proved long-run properties of log-optimal systems under stated assumptions ([4]). These results support the narrow claim that geometric-growth maximization has rigorous asymptotic advantages in repeated multiplicative settings. They do not establish that every finite-horizon decision-maker has logarithmic utility.

Peters and Gell-Mann made the ergodic structure explicit in 2016. Their analysis identifies stationary increments in wealth for additive dynamics and stationary increments in log wealth for multiplicative dynamics. The corresponding expected rates equal the relevant time averages under their models, while wealth itself lacks the required ergodic property ([2]). Peters' 2019 Nature Physics Perspective generalized the argument into a research program and proposed that several apparent decision-theory anomalies arise from optimizing an expectation that does not describe what happens along one path ([1]).

Peters' 2011 leverage paper applies the distinction to a self-financing investment modeled by geometric Brownian motion. It shows that ensemble-average growth rises linearly with leverage while time-average growth has an interior optimum because volatility impairs compound growth. The paper also warns that its model assumes reinvestment without consumption or fresh deposits, so its quantitative optimum should not be transferred mechanically to different financial processes ([11]).

### Human experiments show context-sensitive risk taking

Meder and colleagues tested whether risk preferences change when otherwise comparable outcomes are presented under additive and multiplicative wealth dynamics. Eighteen participants completed consequential choices after learning the two environments. The fitted risk-aversion parameter increased strongly in the multiplicative condition, with a Bayes factor of 2.9 x 10^7 for the change; participants whose fitted parameters moved closer to the time-optimal values also achieved higher time-average growth in both conditions ([6]). The result supports the prediction that behavior adapts to dynamics rather than reflecting one fixed risk preference.

The study has important limitations. Its achieved sample was 18, and participants received extensive exposure to the task. It demonstrates adaptive behavior in a controlled repeated-gamble environment, not a universal human instinct for ergodicity. The authors themselves frame the finding as evidence for grounding decision models in ergodic considerations, not as proof that expected utility is invalid in every setting ([6]).

Skjold and colleagues published a preregistered replication and generalization in 2026 using 58 participants and hierarchical Bayesian models. All 58 showed an increase in the estimated risk-aversion parameter from the additive to the multiplicative condition. In the multiplicative condition, the group posterior mode was 1.062 with a 95 percent Bayesian credible interval from 0.655 to 1.463, close to the logarithmic transformation predicted for multiplicative growth. The authors report strong convergent evidence for time-average growth maximization while also recovering stable individual differences across conditions ([7]). This larger study strengthens the behavioral result and clarifies that dynamic adaptation and trait-like variation can coexist.

Vanhoyweghen and Ginis extended the empirical question beyond multiplicative compounding. They introduced an absorbing ruin boundary into an additive environment and found that participants' risk taking varied with distance from and likelihood of ruin. Their theoretical point is that additive increments can become non-ergodic for actual wealth when a boundary prevents ruined paths from rejoining the ensemble. Their experiment supports sensitivity to this boundary, although it does not imply that every observed choice exactly maximizes a single time-average criterion ([8]).

Together, the experiments provide three distinct tests: adaptation between additive and multiplicative dynamics, replication in a larger preregistered sample, and sensitivity to an absorbing boundary in an additive setting. The convergence is meaningful because the manipulations change the temporal structure rather than merely relabeling outcomes ([6] [7] [8]). The evidence nevertheless remains concentrated in stylized laboratory tasks with learned, repeated gambles. Field evidence on organizations, households, and investors is less controlled and must account for objectives other than wealth growth.

### Critical evidence limits the universal claim

Samuelson's 1971 result is the classic mathematical limitation. He agreed that the maximum-geometric-mean strategy can make superior long-run wealth virtually certain, but showed that this does not imply optimality for a finite number of periods under arbitrary expected-utility objectives. For power utility with a parameter other than the logarithmic case, the geometric strategy remains suboptimal for every finite horizon in his construction ([5]). This establishes that asymptotic path dominance and preference-based optimality are different propositions.

Doctor, Wakker, and Wang argue that expected utility does not assume that expectation values must be physically realized as time or population averages. In their account, expected utility represents preferences over uncertain outcomes, so no ergodic premise is needed merely to use the representation. They credit ergodicity economics with a fresh perspective but reject the claim that it displaces standard decision theory ([9]). Ford and Kay extend this objection: growth optimality is one criterion, and a general choice theory still requires assumptions about what decision-makers value ([10]).

The evidence therefore supports a bounded verdict. Ergodicity is demonstrably relevant to repeated growth processes, and human behavior can adapt in the predicted direction when dynamics change. It does not supply a preference-free answer to every uncertain choice. The reliable conclusion is procedural: state the dynamics, averaging operation, horizon, boundary conditions, and objective before calling a positive expectation rational.

## Implications

### For individual decision-makers

The first implication is to separate opportunity quality from exposure size. A positive expected payoff identifies an edge under the stated probabilities; it does not say how much of a path-dependent resource should be exposed. Kelly's and Peters' results show why maximizing expected wealth can recommend leverage or bet sizes that damage long-run growth in multiplicative settings ([3] [11]). The author's synthesis is to evaluate every important risk in two passes: first estimate the payoff distribution, then test whether the contemplated size preserves the capacity to continue after adverse sequences.

The second implication is to define ruin operationally. Ruin may mean zero wealth, but it may instead mean failing a tuition payment, losing required liquidity, breaching a covenant, exhausting a research budget, or suffering a drawdown that changes behavior. Vanhoyweghen and Ginis show that an absorbing boundary can create the relevant ensemble-time divergence even in an otherwise additive process ([8]). A decision model that omits the boundary can therefore be internally correct and practically irrelevant.

The third implication is to match the horizon to the theorem. Long-run growth criteria concern repeated decisions over enough time for stochastic fluctuations in the growth rate to average out. Kelly explicitly notes that a finite stopping point can make the answer depend on the decision-maker's values for bankruptcy and fortune ([3]). Samuelson proves that long-run dominance does not erase finite-horizon utility differences ([5]). A person with one irreversible decision should not cite an asymptotic result as though thousands of independent retries were available.

### For investors and capital allocators

Ergodicity provides a precise foundation for the margin-of-safety instinct. An investment thesis can have attractive expected value and still be unacceptable at a size that threatens survival. Debt and leverage intensify path dependence because interim price moves, collateral rules, and refinancing conditions can force an exit before the expected payoff arrives. Peters' geometric-Brownian-motion model shows mathematically how leverage raises ensemble-average return while eventually reducing time-average growth beyond an optimum ([11]). The model is simplified, but the direction of the warning is robust: expected return without financing dynamics is an incomplete risk description.

For a value investor, the relevant question is not only whether price is below estimated value. It is also whether the ownership and financing structure permits waiting for value realization through an adverse path. The author's assessment is that cash reserves, limited leverage, diversified sources of liquidity, and position-size limits function as options on continued participation. They may lower the highest modeled payoff while protecting the ability to act when estimates are wrong or markets remain adverse longer than expected. This is consistent with growth-optimal logic but does not require using full Kelly or reducing all preferences to log wealth.

Parameter uncertainty deserves special emphasis. Kelly sizing is derived from the estimated edge and payoff distribution ([3]). The author's assessment is that real investment probabilities and correlations are uncertain, so fractional exposure, conservative probability estimates, and explicit stress scenarios are not departures from rationality; they are responses to model error and unstable dynamics. Scenario planning complements ergodic analysis by asking which pathways could invalidate the assumed process, while black-swan analysis asks whether the modeled distribution omits destructive states.

### For organizations and strategy

Organizations often approve projects by comparing expected benefits with expected costs. That calculation is incomplete when one failure can terminate the organization, block later projects, or consume a scarce resource that cannot be replenished. The author's synthesis is to add a continuation test: after each material downside scenario, can the organization still fund operations, meet legal obligations, and pursue future opportunities? If not, the decision is path-dependent even when its expected net present value is positive.

Research portfolios illustrate the difference between pooling and concentration. Many small, partly independent experiments can approximate an ensemble because failures are contained and learning is shared. One all-consuming project exposes the institution to a single path. The same expected payoff can support opposite decisions depending on whether losses are partitioned or coupled. This is an application of the mechanism identified by Peters and Gell-Mann: resource sharing and independent parallel exposure can make an ensemble average more physically relevant, while sequential reinvestment makes the time path central ([2]).

Pre-mortems and scenario planning become more useful when tied to boundaries rather than generic lists of risks. A scenario should specify not only the probability and loss but also whether the loss changes future choice: Does it trigger cancellation? Does it remove financing? Does it create legal or reputational constraints? Does it increase the size of later losses? The author's assessment is that this boundary-centered approach converts scenario planning from narrative exploration into a test of whether the average-case strategy remains executable.

### For forecasting and probabilistic reasoning

Ergodicity changes the question asked of a forecast. A probability distribution over next-period outcomes may be well calibrated and still be insufficient for a repeated decision. The forecaster must also describe how outcomes update the state, whether the distribution is stable after those updates, and whether any state ends participation. Expected-value decision trees handle branching explicitly, but a tree that uses the same payoff scale and probability model after every branch can miss state-dependent dynamics.

A practical forecast should therefore report at least four layers: the distribution of immediate outcomes, the transition rule from one state to the next, the effective boundary conditions, and the objective over the stated horizon. The author's synthesis is that ensemble summaries such as the mean should be paired with path summaries such as median terminal state, drawdown or threshold-crossing probability, and the distribution of compound growth when the process is multiplicative. These measures answer different questions and should not be collapsed into one score.

This framework also clarifies the relationship between ergodicity and black swans. Black-swan analysis asks whether rare or unmodeled events dominate consequences. Ergodic analysis asks whether the chosen average describes one path even if the distribution is known. A process can be non-ergodic without unknown events, as the simple 1.5-or-0.6 gamble demonstrates ([6]). Conversely, an ergodic model can still be wrong because its distribution excludes structural breaks. The two lenses diagnose different failure modes.

### What should not be inferred

Ergodicity does not imply that the geometric mean is always the correct objective. It is appropriate for specified multiplicative growth under conditions that make expected log change the relevant long-run rate. Additive dynamics, mixed dynamics, consumption, replenishment, changing probabilities, finite horizons, and nonfinancial values require different models ([2] [5] [9]). Nor does avoiding ruin mean avoiding all risk. A strategy that never risks a loss can sacrifice valuable opportunities; the decision problem is to preserve continuation while taking compensated risk.

Ergodicity also does not make preferences irrelevant. The empirical studies show that risk behavior changes with dynamics, but the 2026 replication also finds persistent individual differences ([7]). Expected utility and growth optimality can be treated as complementary descriptions: one states what outcomes a person values, while the other tests whether the temporal process makes a proposed average representative. The strongest practical conclusion is modest but consequential: no average should guide a path-dependent decision until the decision-maker can explain why that average is realizable along the path that must actually be lived.

## Sources

1. Peters, O. (2019). "The Ergodicity Problem in Economics."
   Nature Physics, 15, 1216-1221.
   https://doi.org/10.1038/s41567-019-0732-0 [high]

2. Peters, O. & Gell-Mann, M. (2016). "Evaluating Gambles Using
   Dynamics." Chaos, 26, 023103.
   https://doi.org/10.1063/1.4940236 [high]

3. Kelly, J. L., Jr. (1956). "A New Interpretation of Information
   Rate." Bell System Technical Journal, 35(4), 917-926.
   https://doi.org/10.1002/j.1538-7305.1956.tb03809.x [high]

4. Breiman, L. (1961). "Optimal Gambling Systems for Favorable Games."
   Proceedings of the Fourth Berkeley Symposium on Mathematical
   Statistics and Probability, 1, 65-78.
   https://projecteuclid.org/ebooks/berkeley-symposium-on-mathematical-statistics-and-probability/Proceedings-of-the-Fourth-Berkeley-Symposium-on-Mathematical-Statistics-and/chapter/Optimal-Gambling-Systems-for-Favorable-Games/bsmsp/1200512159 [high]

5. Samuelson, P. A. (1971). "The 'Fallacy' of Maximizing the Geometric
   Mean in Long Sequences of Investing or Gambling." Proceedings of
   the National Academy of Sciences, 68(10), 2493-2496.
   https://doi.org/10.1073/pnas.68.10.2493 [high]

6. Meder, D., Rabe, F., Morville, T., Madsen, K. H., Koudahl, M. T.,
   Dolan, R. J., Siebner, H. R., & Hulme, O. J. (2021).
   "Ergodicity-Breaking Reveals Time Optimal Decision Making in
   Humans." PLOS Computational Biology, 17(9), e1009217.
   https://doi.org/10.1371/journal.pcbi.1009217 [high]

7. Skjold, B., Steinkamp, S. R., Connaughton, C., Hulme, O. J., &
   Peters, O. (2026). "Ergodicity Transformations Predict Human
   Decision-Making under Risk." PLOS Computational Biology, 22(7),
   e1014409. https://doi.org/10.1371/journal.pcbi.1014409 [high]

8. Vanhoyweghen, A. & Ginis, V. (2023). "Human Decision-Making in a
   Non-Ergodic Additive Environment." Proceedings of the Royal Society
   A, 479(2278), 20230544.
   https://doi.org/10.1098/rspa.2023.0544 [high]

9. Doctor, J. N., Wakker, P. P., & Wang, T. V. (2020). "Economists'
   Views on the Ergodicity Problem." Nature Physics, 16, 1168.
   https://doi.org/10.1038/s41567-020-01106-x [high]

10. Ford, M. C. & Kay, J. A. (2023). "The Limitations of Growth-Optimal
    Approaches to Decision Making Under Uncertainty." Econ Journal
    Watch, 20(2), 314-334.
    https://econjwatch.org/articles/the-limitations-of-growth-optimal-approaches-to-decision-making [medium]

11. Peters, O. (2011). "Optimal Leverage from Non-Ergodicity."
    Quantitative Finance, 11(11), 1593-1602.
    https://doi.org/10.1080/14697688.2010.513338 [high]

## See Also

- `library/probabilistic-thinking-forecasting/expected-value-decision-trees.md` -- the expected-value framework that ergodic analysis qualifies for repeated, state-dependent choices.
- `library/probabilistic-thinking-forecasting/black-swan-theory.md` -- a complementary test for rare or unmodeled outcomes that dominate consequences.
- `library/probabilistic-thinking-forecasting/scenario-planning-and-analysis.md` -- a method for testing whether a strategy survives multiple plausible paths rather than one average future.
