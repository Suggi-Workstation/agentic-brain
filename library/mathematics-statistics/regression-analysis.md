---
name: regression-analysis
id: 20260826T133131Z
tier: library-topic
domain: mathematics-statistics
author: Library Runner
tags: [regression-analysis, linear-regression, logistic-regression, ordinary-least-squares, bias-variance-tradeoff, regularization, generalized-linear-models, multicollinearity]
links: [library/mathematics-statistics/statistical-inference.md, library/mathematics-statistics/bayesian-statistics.md, library/mathematics-statistics/causal-inference.md, library/mathematics-statistics/linear-algebra.md, library/mathematics-statistics/probability-theory-fundamentals.md]
---

# Regression Analysis -- Why Modeling Relationships Between Variables Is the Backbone of Quantitative Reasoning

Regression analysis is the statistical method for estimating how a
dependent variable changes when one or more independent variables
change, producing equations that quantify relationships, isolate
effects, and generate predictions from data. From Francis Galton's
19th-century study of hereditary traits to the generalized linear
models that underpin modern data science, regression has evolved into
the most widely used family of statistical techniques in science,
industry, and policy. Its power lies in a deceptively simple idea:
fit a line (or surface) through noisy data, then use the geometry of
that fit to separate signal from noise, measure uncertainty, and make
defensible claims about the world.

## Background

The concept of regression entered statistics through Francis Galton's
work on heredity in the late 19th century. Galton (1822-1911), a
cousin of Charles Darwin, was studying how traits like height passed
from parents to children. In his 1877 lecture at the Royal Institution
and subsequent publications, he observed a phenomenon he initially
called "reversion" and later "regression toward mediocrity": tall
parents tended to have children who were taller than average, but not
as tall as the parents themselves. The offspring regressed toward the
population mean. Galton's sweet pea experiments, where he plotted
daughter seed sizes against mother seed sizes, produced the first
two-dimensional regression diagram -- a scatterplot with a line of
best fit drawn through the data points. The slope of that line, which
he found to be less than 1.0, quantified the regression effect.

What began as a biological observation was soon recognized as a
general statistical phenomenon. Karl Pearson, building on Galton's
work, formalized the mathematical relationship between two variables
through the product-moment correlation coefficient and the method of
least squares fitting. Pearson's work in the 1890s established that
regression and correlation were two sides of the same coin: the
regression slope could be expressed as the correlation multiplied by
the ratio of standard deviations. This unification gave regression
analysis its mathematical foundation independent of the heredity
problem that motivated it.

The method of least squares itself predates Galton. Carl Friedrich
Gauss claimed to have used it as early as 1795, and Adrien-Marie
Legendre published the method in 1805. Both were working on
astronomical problems -- combining multiple imperfect observations of
the same celestial body into a single best estimate. The idea of
minimizing the sum of squared residuals was, from the beginning, a
practical solution to the problem of measurement error. Gauss proved
that the least squares estimator is optimal under certain assumptions,
a result later formalized as the Gauss-Markov theorem. The theorem
states that among all linear unbiased estimators, ordinary least
squares (OLS) has the minimum variance -- it is the Best Linear
Unbiased Estimator (BLUE) -- provided the errors have mean zero,
constant variance (homoscedasticity), and are uncorrelated with each
other.

The 20th century saw regression expand from two variables to many.
Multiple regression allowed researchers to control for confounding
variables, isolate the effect of a single predictor while holding
others constant, and build predictive models from dozens or hundreds
of variables. R.A. Fisher's work on the analysis of variance (ANOVA)
in the 1920s showed that ANOVA and regression were mathematically
equivalent -- both were special cases of the general linear model.
This insight meant that virtually every standard statistical test
(t-test, ANOVA, ANCOVA) could be expressed as a regression problem,
giving regression a unifying role in statistical methodology.

The next major breakthrough came in 1972, when John Nelder and Robert
Wedderburn published "Generalized Linear Models" in the Journal of the
Royal Statistical Society. They showed that ordinary linear
regression, logistic regression, Poisson regression, and several other
models all shared a common structure: a response variable from the
exponential family, a linear predictor (a weighted sum of
independent variables), and a link function connecting the two. This
framework unified what had been separate techniques under a single
estimation algorithm -- iteratively reweighted least squares (IRLS).

The late 20th and early 21st centuries brought regression into the
machine learning era. Regularization methods like ridge regression
(Hoerl and Kennard, 1970) and the lasso (Tibshirani, 1996) added
penalty terms to the least squares objective to prevent overfitting,
trading a small amount of bias for a large reduction in variance.
These techniques bridged classical statistics and modern predictive
modeling, making regression not just an inferential tool but a
predictive one -- the baseline model against which more complex
machine learning algorithms are measured.

## Core Concepts

### The Linear Model and Ordinary Least Squares

At its core, a linear regression model posits that the expected value
of a response variable Y is a linear function of one or more predictor
variables X. In simple linear regression with one predictor, the model
is:

    Y = beta_0 + beta_1 * X + epsilon

where beta_0 is the intercept, beta_1 is the slope coefficient, and
epsilon is the error term -- the difference between the observed and
predicted values. In multiple regression with p predictors, the model
generalizes to:

    Y = beta_0 + beta_1*X_1 + beta_2*X_2 + ... + beta_p*X_p + epsilon

The ordinary least squares (OLS) estimator finds the values of the
beta coefficients that minimize the sum of squared residuals -- the
squared differences between observed and predicted Y values. In matrix
notation, with the design matrix X (where each row is an observation
and each column is a predictor) and the response vector y, the OLS
estimator is:

    beta_hat = (X'X)^(-1) X'y

This formula is the cornerstone of regression analysis. The matrix
X'X captures the structure and interrelationships among the predictors,
while X'y captures the relationships between predictors and response.
The inverse of X'X transforms these into the estimated coefficients.
Geometrically, OLS projects the response vector y onto the column
space of X -- the fitted values are the orthogonal projection of the
data onto the subspace spanned by the predictors.

### The Gauss-Markov Theorem

The Gauss-Markov theorem provides the theoretical justification for
OLS. It states that if the following assumptions hold:

1. Linearity: the relationship between X and Y is linear in the
   parameters.
2. Independence: the errors are uncorrelated with each other.
3. Homoscedasticity: the errors have constant variance.
4. Zero conditional mean: E(epsilon | X) = 0.

then the OLS estimator is the Best Linear Unbiased Estimator (BLUE) --
it has the smallest variance among all linear unbiased estimators.
The theorem does NOT require the errors to be normally distributed;
normality is needed only for hypothesis testing and confidence
intervals in finite samples, not for the BLUE property itself. When
the homoscedasticity assumption fails, OLS remains unbiased but is no
longer efficient -- generalized least squares (GLS) or
heteroscedasticity-consistent (Huber-White) standard errors are used
instead.

### Coefficient Interpretation and the Design Matrix

Each regression coefficient beta_j represents the expected change in
Y for a one-unit increase in X_j, holding all other predictors
constant. This "holding constant" property is what makes multiple
regression powerful for isolating effects: it partials out the
contribution of each predictor from the shared variance among
predictors. The design matrix X encodes all predictor information,
including an intercept column of ones, continuous variables, and
categorical variables (via dummy or indicator coding). Interaction
terms (products of two predictors) can be added to model situations
where the effect of one variable depends on the level of another.

### Logistic Regression and Generalized Linear Models

When the response variable is binary (0 or 1, success or failure), the
linear model is inappropriate: it can produce predicted probabilities
below 0 or above 1. Logistic regression solves this by modeling the
log-odds of the probability as a linear function of the predictors:

    log(p / (1 - p)) = beta_0 + beta_1*X_1 + ... + beta_p*X_p

The logit function maps probabilities from (0, 1) to the entire real
line, ensuring that predicted probabilities always fall in the valid
range. The inverse transformation -- the logistic (sigmoid) function
-- converts the linear predictor back to a probability:

    p = 1 / (1 + exp(-(beta_0 + beta_1*X_1 + ... + beta_p*X_p)))

Logistic regression parameters are estimated by maximum likelihood
estimation (MLE) rather than least squares, because the binary
response is not normally distributed. The log-likelihood function is
concave, guaranteeing a unique maximum that can be found by iterative
algorithms like Newton-Raphson or IRLS. Coefficients in logistic
regression are interpreted as the change in log-odds per unit increase
in the predictor; exponentiating a coefficient gives the odds ratio.

Logistic regression is a specific case of the generalized linear
model (GLM) framework introduced by Nelder and Wedderburn (1972). A
GLM has three components: (1) a response variable whose distribution
belongs to the exponential family (normal, binomial, Poisson, gamma,
etc.), (2) a linear predictor eta = X*beta, and (3) a link function
g() connecting the mean of the response to the linear predictor:
g(mu) = eta. For normal responses, the link is the identity function
and we get OLS. For binary responses, the link is the logit and we
get logistic regression. For count data, the link is the log and we
get Poisson regression. This unification means that a single
estimation algorithm -- iteratively reweighted least squares -- can
fit all these models.

### Model Fit and Diagnostics

Assessing how well a regression model fits the data requires multiple
tools. The coefficient of determination, R-squared, measures the
proportion of variance in Y explained by the model:

    R^2 = 1 - (SS_residual / SS_total)

R-squared ranges from 0 to 1 in standard settings, with higher values
indicating better fit. However, R-squared always increases when
predictors are added, even useless ones. Adjusted R-squared corrects
for this by penalizing model complexity:

    R^2_adj = 1 - (1 - R^2) * (n - 1) / (n - p - 1)

where n is the sample size and p is the number of predictors. Unlike
R-squared, adjusted R-squared can decrease when a non-informative
predictor is added, making it a better tool for model comparison.

Residual analysis is the primary diagnostic tool. A residual is the
difference between observed and fitted values (y_i - y_hat_i). Plotting
residuals against fitted values reveals non-linearity (a curved
pattern suggests the linear model is misspecified), heteroscedasticity
(a fan-shaped pattern indicates non-constant variance), and outliers
(points with large residuals). A normal quantile-quantile (Q-Q) plot
of residuals checks the normality assumption. Leverage measures how
far an observation's predictor values are from the center of the
predictor space; high-leverage points can disproportionately
influence the fitted model. Cook's distance combines leverage and
residual size to identify influential observations -- points that, if
removed, would substantially change the coefficients.

### Multicollinearity

Multicollinearity occurs when two or more predictors are highly
correlated with each other. This does not bias the coefficients, but
it inflates their standard errors, making individual coefficients
statistically insignificant even when the overall model fit is strong.
The model cannot distinguish the separate contributions of correlated
predictors -- the shared signal is split between them unstably. The
variance inflation factor (VIF) quantifies multicollinearity: a VIF
of 10 or more (some use a threshold of 5) indicates problematic
collinearity. Remedies include dropping one of the correlated
variables, combining them into an index, or using regularization
methods (ridge regression) that stabilize the estimates by shrinking
coefficients.

### The Bias-Variance Tradeoff

Every regression model faces a fundamental tradeoff between bias and
variance. Bias is the systematic error from incorrect model
assumptions -- a linear model fitted to a nonlinear relationship has
high bias. Variance is the sensitivity of the estimates to the
particular sample drawn -- a model with many predictors fitted to
few observations has high variance, because the coefficients change
dramatically with small changes in the data. The total expected
prediction error decomposes as:

    Error = Bias^2 + Variance + Irreducible Error

Simple models (few predictors, linear functional form) tend to have
high bias but low variance. Complex models (many predictors,
polynomial terms, interactions) tend to have low bias but high
variance. Regularization methods navigate this tradeoff by adding a
penalty term to the loss function. Ridge regression (L2 penalty)
shrinks all coefficients toward zero but never sets them exactly to
zero. The lasso (L1 penalty) shrinks some coefficients to exactly
zero, performing variable selection. Both introduce a small amount of
bias in exchange for a large reduction in variance, often improving
out-of-sample prediction substantially.

## Evidence

### Gauss-Markov and the Optimality of OLS

The Gauss-Markov theorem, proven in its modern form by Andrey Markov
in the early 20th century and extended by Alexander Aitken to
non-spherical errors, provides the theoretical foundation for OLS.
The proof shows that any other linear unbiased estimator beta_tilde
can be written as beta_tilde = (X'X)^(-1)X'y + D*y for some matrix D
satisfying DX = 0 (the unbiasedness condition). The variance of this
estimator is:

    Var(beta_tilde) = Var(beta_hat) + sigma^2 * D*D'

Since D*D' is positive semidefinite, the variance of beta_tilde is at
least as large as the variance of beta_hat. This result, verified by
simulation studies in econometrics courses (e.g., the Econometrics
with R project), demonstrates that OLS weights (1/n for the mean-only
model) produce tighter sampling distributions than alternative
weighting schemes. The theorem's power is that it requires no
distributional assumption on the errors beyond zero mean, constant
variance, and zero correlation -- normality is not needed.

### Galton's Sweet Pea Experiments and the Discovery of Regression

Galton's experiments with sweet peas, documented in his 1877 lecture
and later publications, provided the first empirical demonstration of
regression. He distributed seeds of seven different sizes to friends
across England and measured the sizes of the resulting offspring
plants. Plotting daughter seed size against mother seed size, he
found the slope of the regression line was approximately 0.33 --
offspring regressed one-third of the way back toward the population
mean. This was initially interpreted as a biological law of
reversion, but Galton later recognized it as a purely statistical
phenomenon: any two variables with imperfect correlation will show
regression toward the mean. The historical analysis by Stanton (2001)
in the Journal of Statistics Education traces how Galton's pea
experiments led to the conceptualization of linear regression, and how
Karl Pearson subsequently generalized these ideas into multiple
regression and the product-moment correlation coefficient.

### Nelder and Wedderburn's Generalized Linear Models (1972)

The 1972 paper by Nelder and Wedderburn in the Journal of the Royal
Statistical Society unified a collection of seemingly distinct
regression models under a single framework. They demonstrated that
ordinary linear regression (normal response, identity link), logistic
regression (binomial response, logit link), Poisson regression (Poisson
response, log link), and gamma regression (gamma response, inverse
link) all share the exponential family structure. Their key technical
contribution was showing that maximum likelihood estimates for all
these models could be computed by iteratively reweighted least squares
(IRLS) -- the same algorithm, with different weights and link
functions. This meant that a single computational engine could fit
the entire family of GLMs. The framework, later elaborated in
McCullagh and Nelder's 1989 textbook "Generalized Linear Models"
(2nd edition), became the standard framework for regression with
non-normal responses and is implemented in the glm() function in R
and equivalent procedures in SAS, Stata, and Python's statsmodels.

### Ridge Regression and the Bias-Variance Tradeoff

Hoerl and Kennard (1970) introduced ridge regression as a solution to
the instability of OLS under multicollinearity. Their paper showed
that adding an L2 penalty term -- lambda * sum(beta_j^2) -- to the
least squares objective shrinks the coefficients toward zero,
stabilizing the estimates. The ridge estimator is:

    beta_ridge = (X'X + lambda*I)^(-1) X'y

The tuning parameter lambda controls the shrinkage: lambda = 0
recovers OLS, while large lambda shrinks all coefficients toward
zero. The bias-variance tradeoff is explicit: increasing lambda
increases bias but decreases variance, and the optimal lambda
minimizes total prediction error. Cross-validation is used to select
lambda. Tibshirani (1996) extended this idea to the lasso, which uses
an L1 penalty -- lambda * sum(|beta_j|) -- that performs variable
selection by setting some coefficients exactly to zero. The lasso is
particularly useful when many predictors are irrelevant and only a
subset matters. Both methods are now standard tools in statistical
learning, implemented in scikit-learn, glmnet, and other libraries.

### The Anscombe Quartet and the Limits of Summary Statistics

Francis Anscombe (1973) constructed four datasets that have identical
means, variances, correlations, regression lines, and R-squared
values, yet look completely different when plotted. One dataset shows
a clean linear relationship; another has a nonlinear (quadratic)
pattern; a third has a perfect linear relationship except for one
outlier; the fourth is dominated by a single high-leverage point. The
Anscombe quartet demonstrates that regression summary statistics
alone are insufficient -- graphical analysis of residuals is essential
to detect model misspecification, nonlinearity, and influential
points. This result has been reinforced by the "Datasaurus Dozen"
(Matejka and Fitzmaurice, 2017), which extended Anscombe's idea to
show that datasets with radically different visual patterns can share
identical summary statistics. The practical lesson is that every
regression analysis should include a residual-vs-fitted plot, a
Q-Q plot for normality, and a leverage or Cook's distance plot for
influence -- without these, the numerical output may mask serious
model failures that invalidate every inference drawn from the model.

### Logistic Regression in Medical Research

The Penn State STAT 504 course materials document a canonical
application of logistic regression in clinical research: modeling
the probability of a binary outcome (such as death or disease
remission) as a function of patient characteristics and treatment
variables. In a representative study, seven deaths occurred among 182
patients, yielding an estimated baseline probability of approximately
0.04. Logistic regression extends this by allowing the probability to
vary with predictors: age, treatment group, comorbidity score, and
other covariates. Maximum likelihood estimation finds the coefficient
values that make the observed data most probable under the model. The
log-likelihood function for n independent Bernoulli observations is:

    L = sum(y_k * log(p_k) + (1 - y_k) * log(1 - p_k))

where p_k is the predicted probability for observation k. This
function is concave, guaranteeing a unique maximum. The method
produces odds ratios that clinicians can interpret directly: an odds
ratio of 2.0 for a treatment variable means the odds of the outcome
double for treated patients relative to controls, holding other
covariates constant. The Hosmer-Lemeshow goodness-of-fit test and
the area under the receiver operating characteristic (ROC) curve
provide complementary assessments of calibration and discrimination,
the two dimensions on which a logistic model is evaluated.

## Implications

### For Scientific Research and Causal Inference

Regression analysis is the primary quantitative tool in empirical
research across the social sciences, epidemiology, economics, and
psychology. When researchers want to know whether a treatment has an
effect, whether a policy intervention works, or whether a risk factor
is associated with an outcome, they fit a regression model. The
ability to control for confounding variables -- to estimate the effect
of one variable while holding others constant -- is what makes
regression indispensable for observational studies where randomized
experiments are impractical or unethical. However, regression
controls only for measured confounders. Unmeasured confounders can
bias estimates, which is why causal inference methods (instrumental
variables, difference-in-differences, regression discontinuity) extend
regression with additional identifying assumptions. The relationship
between regression and causation is subtle: regression measures
association, and causal claims require assumptions that go beyond the
statistical model. The candidate's scope correctly positions
regression as the foundation that connects to causal inference rather
than a substitute for it.

### For Business and Finance

In finance, regression is used to estimate the Capital Asset Pricing
Model (CAPM), where stock returns are regressed on market returns to
estimate beta (systematic risk). Factor models like the Fama-French
three-factor model extend this to multiple regressors. In marketing,
regression quantifies the return on advertising spend across channels,
controlling for seasonality and competitor activity. In operations,
regression models demand forecasting, quality control, and process
optimization. The bias-variance tradeoff has direct business
implications: an overfit model performs well on historical data but
fails on new data, leading to costly decisions. Regularization and
cross-validation are not just academic exercises -- they prevent
organizations from deploying models that do not generalize. Credit
scoring, where logistic regression predicts the probability of default
from applicant characteristics, is one of the most widespread
commercial applications of regression, affecting millions of lending
decisions daily. The interpretability of regression coefficients is a
regulatory advantage: under fair lending laws, financial institutions
must be able to explain why an applicant was denied credit, and
linear or logistic regression models produce coefficient-based
explanations that complex black-box models cannot match without
additional interpretability tooling.

### For Machine Learning and Data Science

Regression is the baseline model in predictive modeling. Before
deploying a neural network or gradient boosting model, practitioners
fit a linear or logistic regression to establish a performance
benchmark. If the complex model cannot beat the regression baseline,
the complexity is not justified. The concepts developed in regression
-- the bias-variance tradeoff, regularization, cross-validation,
feature engineering, residual diagnostics -- are the conceptual
foundation of all supervised learning. Linear regression is the
simplest case of a broader family: polynomial regression adds
nonlinear features, basis splines add flexibility, generalized
additive models combine multiple smooth functions, and neural
networks can be viewed as nonlinear regression with learned feature
transformations. The mathematical foundations of regression --
matrix algebra, optimization, probability distributions -- are
prerequisites for understanding these more complex models. A data
scientist who understands regression deeply can diagnose problems in
any model, because the diagnostic principles transfer: residuals
reveal bias, cross-validation reveals variance, and regularization
controls the tradeoff. The success of gradient boosting and random
forests -- which dominate tabular data competitions -- does not make
regression obsolete; it makes regression the essential baseline and
the interpretability fallback. When a stakeholder asks why a model
made a particular prediction, a regression model provides a
coefficient-weighted answer. Complex models require SHAP values, LIME
explanations, or attention plots to produce the same answer, and
these explanation methods themselves rest on regression-like local
approximations.

### For Education and Statistical Literacy

Regression analysis is taught in virtually every introductory
statistics course, and for good reason: it is the most commonly used
statistical method in practice, and it illustrates core statistical
concepts -- uncertainty, sampling variability, model assumptions,
the distinction between correlation and causation -- in a concrete,
accessible way. Understanding regression is a prerequisite for
interpreting research findings in medicine (clinical trials report
adjusted odds ratios from logistic regression), economics (policy
effects are estimated from regression discontinuity designs), and
social science (survey results are analyzed with multiple regression).
The widespread misuse of regression -- interpreting observational
associations as causal, ignoring assumption violations, chasing high
R-squared without validating out-of-sample -- makes statistical
literacy about regression a public health issue. Misinterpreted
regression results have driven erroneous policy, fueled spurious
health claims, and wasted research funding. Teaching regression
diagnostics alongside the mechanics of fitting models is essential
for producing practitioners who use the tool responsibly. The
replication crisis in psychology and other fields has roots partly in
regression misuse: researchers testing many specifications until one
produces significance (p-hacking), or failing to pre-register their
analysis plan, turn the inferential machinery of regression into a
machine for false discoveries. Pre-registration, specification curves,
and the move toward reporting all tested models rather than only
significant ones are methodological responses that depend on
understanding what regression can and cannot do.

### For the Agentic Brain Knowledge Base

Within this knowledge base, regression analysis serves as a
foundational topic that connects to several existing domains.
Statistical inference provides the framework for hypothesis testing
and confidence intervals around regression coefficients. Bayesian
statistics offers Bayesian regression as an alternative to frequentist
OLS, treating coefficients as random variables with posterior
distributions. Causal inference extends regression with identifying
assumptions to estimate causal effects rather than mere associations.
Linear algebra provides the matrix operations (matrix inversion,
projection, eigenvalues) that underlie the OLS estimator. Probability
theory provides the distributional assumptions (normal errors,
exponential families) that justify the estimation procedures. Each of
these connections represents a path through which knowledge compounds:
understanding regression deepens the understanding of each adjacent
topic, and vice versa.

## Sources

1. Nelder, J.A. & Wedderburn, R.W.M. (1972). "Generalized Linear
   Models." Journal of the Royal Statistical Society, Series A,
   135(3), 370-384.
   https://www.jstor.org/stable/2344614 [high]

2. Greene, W.H. "Estimating the Regression Model by Least Squares."
   Chapter 4, Econometric Analysis, 8th Edition. New York University.
   https://pages.stern.nyu.edu/~wgreene/Text/Edition8/PDF/M04_GREE1366_08_SE_C04.pdf
   [high]

3. Stanton, J.M. (2001). "Galton, Pearson, and the Peas: A Brief
   History of Linear Regression for Statistics Instructors." Journal
   of Statistics Education, 9(3).
   https://tandfonline.com/doi/abs/10.1080/10691898.2001.11910537 [high]

4. Wikipedia. "Gauss-Markov theorem."
   https://en.wikipedia.org/wiki/Gauss-Markov_theorem [medium]

5. Wikipedia. "Generalized linear model."
   https://en.wikipedia.org/wiki/Generalized_linear_model [medium]

6. Wikipedia. "Logistic regression."
   https://en.wikipedia.org/wiki/Logistic_regression [medium]

7. Wikipedia. "Coefficient of determination."
   https://en.wikipedia.org/wiki/Coefficient_of_determination [medium]

8. Penn State University, STAT 504. "Binary Logistic Regression."
   https://online.stat.psu.edu/stat504/Lesson06.html [high]

9. Anscombe, F.J. (1973). "Graphs in Statistical Analysis." American
   Statistician, 27(1), 17-21. [high]

10. Hoerl, A.E. & Kennard, R.W. (1970). "Ridge Regression: Biased
    Estimation for Nonorthogonal Problems." Technometrics, 12(1),
    55-67. [high]

11. Tibshirani, R. (1996). "Regression Shrinkage and Selection via
    the Lasso." Journal of the Royal Statistical Society, Series B,
    58(1), 267-288. [high]

12. McCullagh, P. & Nelder, J.A. (1989). "Generalized Linear Models,"
    2nd Edition. Chapman and Hall. [high]

## See Also

- `library/mathematics-statistics/statistical-inference.md` -- the
  inferential framework for hypothesis testing and confidence
  intervals around regression coefficients.
- `library/mathematics-statistics/bayesian-statistics.md` -- Bayesian
  regression as an alternative estimation paradigm with posterior
  distributions for coefficients.
- `library/mathematics-statistics/causal-inference.md` -- extending
  regression with identifying assumptions to estimate causal effects.
- `library/mathematics-statistics/linear-algebra.md` -- the matrix
  operations (projection, inversion, eigendecomposition) underlying
  the OLS estimator.
- `library/mathematics-statistics/probability-theory-fundamentals.md`
  -- the distributional assumptions (normal errors, exponential
  families) that justify estimation procedures.