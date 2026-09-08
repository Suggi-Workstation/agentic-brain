---
name: optimization-theory
id: 20260908T093523Z
tier: library-topic
domain: mathematics-statistics
author: Librarian
tags: [optimization-theory, convex-optimization, linear-programming, duality, gradient-methods, combinatorial-optimization]
links: [library/mathematics-statistics/linear-algebra.md, library/mathematics-statistics/regression-analysis.md, library/mathematics-statistics/information-theory.md, library/portfolio-risk-management/modern-portfolio-theory.md]
---

# Optimization Theory -- A Common Language for Choosing the Best Feasible Action Under Constraints

Optimization theory turns a stated goal, a set of controllable variables, and a set of limits into a mathematical problem whose feasible solutions can be compared. Its central value is not that every problem has an exact answer, but that it separates modeling assumptions, feasibility, optimality conditions, and computational limits so that a claimed solution can be examined rather than merely asserted. The general framework connects linear programming, convex analysis, nonlinear methods, discrete search, statistical estimation, and portfolio construction while keeping their different guarantees explicit. (Sources: [1], [2])

## Background

Optimization is the mathematical study of selecting a feasible value of one or more variables that minimizes or maximizes an objective. A standard minimization problem asks for a vector x that minimizes f0(x), subject to inequality constraints fi(x) <= 0 and equality constraints hj(x) = 0. The objective represents the quantity being judged, while the constraints define the feasible set; changing either changes the problem. This separation is fundamental because a computationally precise answer to a badly specified objective is still an answer to the wrong problem. (Source: [1])

The modern development of optimization drew together several earlier traditions. The multiplier method associated with Lagrange supplied a way to reason about equality-constrained extrema. Linear inequalities, matrix methods, and resource-allocation questions later produced linear programming, in which both objective and constraints are linear. Dantzig's account describes the simplex method, duality, transportation, networks, and discrete-variable problems as parts of the same linear-programming framework, rather than isolated application tricks. (Source: [2])

Linear programming became especially important because many allocation questions can be expressed with a linear objective and linear resource limits. A production planner can represent quantities to make as variables, capacity limits as inequalities, conservation equations as equalities, and cost or contribution as the objective. The same formal grammar applies to flows through a network, assignment of tasks, and blends of inputs. That reuse does not mean the applications are identical; it means that their mathematical structure admits common feasibility and optimality tools. (Source: [2])

Nonlinear programming broadened the framework when objectives or constraints were not linear. Kjeldsen's historical analysis reports that Kuhn and Tucker introduced nonlinear programming at the 1950 Berkeley symposium and proved conditions for constrained local optima. The resulting Kuhn-Tucker conditions generalized multiplier reasoning to differentiable inequality constraints through stationarity, nonnegative multipliers, and complementary slackness. The historical record also matters: Karush's 1939 thesis and Fritz John's 1948 work contained related results, so the commonly used KKT name recognizes a development rather than a single isolated starting point. (Source: [3])

Convex analysis provided a decisive organizing principle. A convex feasible set contains the entire line segment between any two feasible points, and a convex objective has no value above the chord joining two points on its graph. For a convex minimization problem, local optimality conditions can often certify global optimality; for a nonconvex problem, a local method can find a locally good point without proving that no better distant point exists. Boyd and Vandenberghe therefore distinguish the tractable theory of convex optimization from the broader and generally more difficult class of nonlinear problems. (Source: [1])

The algorithmic history also changed what could be solved. The simplex method made linear programs operationally useful, while complexity theory identified worst-case limits independently of common practical performance. Karmarkar's 1984 paper gave a polynomial-time algorithm for linear programming and analyzed its operation through repeated projective transformations and interior points. The result did not make all optimization easy; it established that the method class and the problem representation determine both the available guarantee and the relevant computational cost. (Source: [4])

First-order methods developed along a parallel path for problems where exact linear-algebra factorizations or full second derivatives are too expensive. Nesterov's 1983 paper established a convex-programming method with an O(1/k^2) convergence rate in its stated setting. Robbins and Monro's 1951 stochastic approximation method addressed a different problem: finding a root of an unknown monotone response function by successive noisy observations. These works are historical foundations for modern iterative methods, but their assumptions and targets differ and should not be collapsed into a single claim about all gradient algorithms. (Sources: [5], [6])

Contemporary applications extend the framework without eliminating those distinctions. Bottou, Curtis, and Nocedal describe large-scale machine learning as a setting in which stochastic gradients have had a central role and conventional nonlinear methods can falter. Candes and Tao show a contrasting use of convex optimization: under stated conditions, recovery from corrupted measurements can be framed as an L1 minimization problem that is recast as a linear program. Together, these examples show why optimization is a mathematical foundation rather than a single algorithm: the problem geometry, data access pattern, and acceptable certificate govern the method choice. (Sources: [7], [8])

## Core Concepts

### 1. Decision Variables, Objective, and Feasible Set

Every optimization model begins by declaring the decision variables. A variable is a controllable mathematical quantity, such as a vector of production quantities, portfolio weights, regression coefficients, or a signal estimate. The objective f0(x) ranks feasible alternatives. Constraints encode requirements that cannot be violated, including balances, capacities, nonnegativity, bounds, and logical relations. The feasible set is the collection of variable values that satisfy every constraint. An optimum is meaningful only relative to all four ingredients: variables, objective, constraints, and the chosen direction of optimization. (Sources: [1], [2])

A compact generic form is:

    minimize    f0(x)
    subject to  fi(x) <= 0,  i = 1, ..., m
                hj(x) = 0,  j = 1, ..., p

This form separates what is optimized from what is allowed. A model can have no feasible point, a feasible region with no attained optimum, or multiple optima. Those are mathematically different outcomes. Reporting only an objective value hides whether the solution obeys all requirements and whether a different feasible solution could have the same value. A well-formed analysis therefore checks feasibility before treating an objective comparison as a decision recommendation. (Source: [1])

### 2. Linear Programming and Polyhedral Geometry

A linear program has a linear objective such as c^T x and linear equality or inequality constraints. Its feasible region is a polyhedron, the intersection of finitely many half-spaces and affine sets. In a bounded linear program with an attained optimum, an optimal solution can be found at an extreme point of that polyhedron. This geometric fact motivates pivoting methods such as simplex, which move among basic feasible solutions while improving or maintaining the objective. (Source: [2])

The common standard form is:

    minimize    c^T x
    subject to  A x = b
                x >= 0

Inequality constraints can be transformed with slack variables when appropriate, but transformations must preserve the original meaning. A bound such as x_i <= u_i is not a cosmetic detail; it changes the feasible polyhedron and may rule out a mathematically attractive but operationally impossible solution. Dantzig's treatment of linear programming connects standard forms, simplex pivots, duality, network problems, and discrete-variable extensions precisely because these transformations must be tracked rather than assumed away. (Source: [2])

### 3. Convexity, Local Optima, and Global Certificates

A set C is convex when, for any x and y in C and any t between zero and one, the point t x + (1 - t) y is also in C. A function f is convex when f(t x + (1 - t) y) <= t f(x) + (1 - t) f(y) over its domain. In a convex minimization problem, a feasible local minimizer is global under the usual differentiability or subgradient conditions. This does not guarantee uniqueness: a flat region may contain many global minimizers with the same objective value. (Source: [1])

Convexity is a structural property, not a synonym for smoothness. A convex function can be nondifferentiable, as with an L1 norm at zero, and a smooth function can be nonconvex. The distinction affects both guarantees and algorithms. A gradient-based local method applied to a nonconvex landscape can converge to a stationary point that is a local minimum, local maximum, or saddle point, while a convex formulation can support a certificate that no feasible alternative has a lower objective. (Source: [1])

### 4. Quadratic Objectives and Positive Semidefiniteness

Quadratic programs use an objective of the form one-half x^T P x + q^T x + r, usually with linear constraints. If P is positive semidefinite, the quadratic term is convex, so the problem is a convex quadratic program. If P has a negative curvature direction, the objective is not convex and the global problem changes character. Linear algebra therefore supplies a direct diagnostic: the eigenvalue structure of the Hessian or quadratic matrix determines the curvature classification. (Sources: [1], [2])

Least squares is a central quadratic example. Minimizing the squared residual norm ||A x - b||_2^2 asks for the point in the model space closest to the data vector in Euclidean distance. Regression analysis uses this geometry when it estimates coefficients by ordinary least squares; optimization supplies the objective and linear algebra supplies the projection and numerical solution methods. Regularization adds a penalty to the objective, which changes the target from best in-sample fit alone to a stated trade-off between fit and parameter size or structure. (Sources: [1], [2])

### 5. Lagrangians, Duality, and Sensitivity

The Lagrangian augments the objective with weighted constraints. For a minimization problem with inequality constraints fi(x) <= 0 and equality constraints hj(x) = 0, it can be written as:

    L(x, lambda, nu) = f0(x) + sum_i lambda_i fi(x) + sum_j nu_j hj(x)

The multipliers lambda_i associated with inequalities are constrained to be nonnegative. The dual function takes the infimum of this Lagrangian over x, producing a lower bound on the primal objective for every dual-feasible multiplier vector. Maximizing that lower bound gives the dual problem. Weak duality is the statement that every dual-feasible value is no larger than every primal-feasible minimization value. (Source: [1])

Strong duality is more demanding: it says that the best primal and dual values coincide under specified conditions. For many convex problems, a constraint qualification such as Slater's condition supports this equality. When strong duality holds, dual variables have a sensitivity interpretation: a multiplier can describe the first-order change in the optimum as the corresponding constraint is relaxed, subject to the model's assumptions. That interpretation is useful only when the relevant regularity conditions are checked; it is not a universal price label that can be read from any numerical solver output. (Source: [1])

### 6. KKT Conditions and Active Constraints

For differentiable constrained problems, the KKT conditions combine four tests: primal feasibility, dual feasibility, stationarity of the Lagrangian, and complementary slackness. Complementary slackness requires lambda_i fi(x) = 0 for each inequality constraint. Thus a slack constraint has zero multiplier, while a positive multiplier can occur only for a binding constraint. Kjeldsen's exposition presents these conditions as necessary conditions for a local minimum under an active-constraint regularity assumption; convexity plus suitable regularity can strengthen them into sufficient conditions. (Sources: [1], [3])

The active-set viewpoint is practical as well as theoretical. At a candidate solution, some constraints bind and define the local boundary, while others are inactive and can be locally ignored in the first-order balance. Algorithms that estimate or update an active set can exploit this structure. However, declaring a constraint inactive because a floating-point residual is small is a numerical judgment, not a mathematical proof; tolerances, scaling, and solver diagnostics matter. (Sources: [1], [2])

### 7. First-Order, Second-Order, and Stochastic Methods

Gradient descent updates x in the negative gradient direction, because the gradient points toward local increase for a differentiable objective. Step size is essential: a direction can be correct while an oversized step increases the objective or leaves the feasible region. Newton and quasi-Newton methods use curvature information to choose a scaled direction and can converge rapidly near a well-behaved solution, but they require more computation and can be unreliable without safeguards when curvature is indefinite or the local quadratic approximation is poor. (Source: [1])

Accelerated first-order methods use past iterates or auxiliary sequences to improve convergence rates under their stated smooth convex assumptions. Nesterov's cited 1983 result is an important example, but its O(1/k^2) rate is not a license to promise that rate for a noisy, nonsmooth, constrained, or nonconvex production problem. Convergence statements must retain the objective class, norm, initialization, step rule, and performance metric from the theorem that supports them. (Source: [5])

Stochastic methods use noisy or sampled estimates of a full gradient or response. Robbins and Monro showed that successive experiments can approach the root of an unknown monotone response under their specified setup. Bottou, Curtis, and Nocedal explain why stochastic gradients are central in large-scale machine learning: one can process portions of the data rather than compute a full gradient at every iteration. The trade-off is variance and imperfect directional information, so practical methods balance step schedules, minibatches, regularization, and stopping criteria rather than treating each update as an exact descent calculation. (Sources: [6], [7])

### 8. Discrete Decisions and Combinatorial Optimization

Some decisions are inherently discrete: assign or do not assign, open or do not open, choose an integer number of units, or select a subset. Linear-programming relaxations can replace discrete requirements with continuous variables to obtain bounds or approximations, but the relaxed answer may not satisfy the original integer restrictions. Dantzig's treatment of discrete-variable extremum problems places this distinction inside the linear-programming tradition rather than obscuring it behind a common objective notation. (Source: [2])

The resulting difficulty is structural. A linear objective with continuous variables may be solved by linear-programming methods, whereas adding integrality can create a combinatorial search problem. Convex reformulations can sometimes recover tractable surrogates. Candes and Tao provide an example in which an L1 minimization problem can be expressed as a linear program and, under their conditions, exactly recovers a signal from corrupted measurements. This is not a general conversion of every discrete problem into an easy one; it is a result tied to a specific measurement model and stated conditions. (Source: [8])

### 9. Modeling Error, Numerical Error, and Algorithmic Error

An optimization result can fail for at least three separate reasons. Modeling error occurs when the objective, constraints, or inputs do not represent the decision problem. Numerical error occurs when finite precision, poor scaling, ill conditioning, or termination tolerances distort a computed solution. Algorithmic error occurs when a method's assumptions do not match the problem, such as using a local method when a global certificate is required. These categories are distinct, so a better solver cannot repair an incorrectly specified objective and a more elaborate model cannot cure unstable arithmetic automatically. (Sources: [1], [2], [7])

The author's synthesis is that optimization should be treated as a chain of evidence: formulate the decision, prove or test feasibility, classify the structure, choose a method whose guarantee matches that structure, and report the residual uncertainty. This framing is more durable than selecting a fashionable algorithm because it makes clear which conclusion follows from mathematics, which follows from measured inputs, and which remains conditional on the model. (Sources: [1], [2], [7])

## Evidence

### Linear Programming: Polynomial-Time Progress Without a Universal Winner

Karmarkar's 1984 paper provides a precise case study of how theory changes an algorithm class. The paper states a polynomial-time algorithm for linear programming with a worst-case operation bound expressed in the number of variables and input-bit length. Its method starts from a strictly interior point of a polytope, applies projective transformations, and repeatedly optimizes over an inscribed sphere to produce a sequence converging to the optimum in polynomial time. The evidence is a mathematical proof with an explicit complexity claim, not a claim that one implementation dominates every linear-programming instance in practice. (Source: [4])

This case separates three questions that are often conflated. First, is a solution feasible and optimal for a particular model? Second, does an algorithm have a favorable worst-case complexity bound? Third, does a solver run fastest on a particular data representation and hardware configuration? Karmarkar's result directly addresses the second question. It also helped establish the practical importance of interior-point approaches, but selecting between simplex and interior-point methods still depends on sparsity, warm starts, precision, and the application. The general lesson is that asymptotic theory is evidence about a defined class, not a substitute for instance-specific benchmarking. (Sources: [2], [4])

### Accelerated Convex Optimization: A Rate With Explicit Assumptions

Nesterov's 1983 article is an original source for an accelerated method whose title states an O(1/k^2) convergence rate for a convex-programming problem. The result is evidence that first-order methods can use more than the current gradient information to improve a theoretical rate over basic gradient schemes in the relevant smooth convex setting. The paper is especially important because it makes the rate a theorem tied to a specified method and problem class, rather than an informal observation about faster-looking iterates. (Source: [5])

The applicable inference is narrow but powerful. When an objective is convex and smooth enough for the theorem's framework, an accelerated first-order method provides a principled candidate. When an objective is nonsmooth, noisy, constrained in a different way, or nonconvex, one must use a theorem or diagnostic for that altered setting. This boundary is evidence of rigor, not a limitation of optimization theory: a result that preserves its assumptions tells the user exactly what additional facts are needed before applying it. (Sources: [1], [5])

### Stochastic Approximation: Learning From Noisy Measurements

Robbins and Monro's 1951 article studies a problem in which the expected response M(x) is monotone but unknown and the goal is to locate x such that M(x) equals a target level. Their method chooses successive experimental levels so that the sequence tends to the target root in probability under the paper's conditions. This is evidence for iterative learning under noisy observations, not for deterministic exact minimization at each step. (Source: [6])

The distinction became operationally important in large-data optimization. Bottou, Curtis, and Nocedal review text classification and deep-network training and identify stochastic gradients as central in large-scale machine learning, while noting the shortcomings of conventional gradient-based nonlinear methods in that setting. Their review supplies a case-based account of why one trades exact full-gradient calculations for inexpensive noisy estimates: the data volume can make the full calculation impractical at every iteration. The method's usefulness therefore rests on statistical and computational conditions, not on an assertion that randomness is inherently superior. (Source: [7])

### Convex Relaxation: Exact Recovery in a Specific Signal Model

Candes and Tao study recovery of a vector from corrupted linear measurements. Their paper states that, under suitable conditions on the coding matrix and a limit on corrupted entries, the original vector is the unique solution of an L1 minimization problem. They further show that this problem can be recast as a linear program. The method and finding form a concrete demonstration that a convex program can solve a problem related to sparse recovery exactly when the stated structural assumptions hold. (Source: [8])

The paper also documents the boundary of that claim. It contrasts the L1 program with finding the sparsest solution, which it describes as computationally intractable in general, and explains why L1 supplies a tractable surrogate in its setting. The evidence does not support replacing every combinatorial objective with L1 and expecting exact recovery. It supports a more disciplined conclusion: identify a structure such as restricted near-orthogonality or a compatible measurement system, then use the associated convex formulation and theorem. (Source: [8])

### Constrained Nonlinear Optimization: Necessary Conditions Made Visible

Kjeldsen's historical and mathematical account states the constrained nonlinear problem as minimizing f(x) subject to inequality constraints gi(x) <= 0. It presents the Kuhn-Tucker theorem with stationarity, complementary slackness, nonnegative multipliers, feasibility, and a linear-independence condition on active constraint gradients. The evidence is both a historical account of the theory's development and a concise statement of why constraints must enter optimality analysis rather than being checked only after an unconstrained calculation. (Source: [3])

The case supports a practical protocol. First solve or estimate a candidate under the actual constraints. Then test primal feasibility, the multiplier signs, stationarity residuals, and complementarity against a stated tolerance. Finally, classify whether the mathematical conditions are merely necessary or also sufficient for the problem class. Boyd and Vandenberghe provide the convex-duality framework that explains when the latter stronger conclusion can be reached. This is stronger evidence than reporting that a solver stopped, because a termination message alone does not identify which optimality conditions were satisfied. (Sources: [1], [3])

### Cross-Case Synthesis

Across these studies, the empirical pattern is not that one method wins universally. Karmarkar supplies a complexity result for linear programming; Nesterov supplies a rate result for convex programming; Robbins and Monro supply a stochastic root-finding framework; Candes and Tao supply an exact-recovery result under measurement conditions; and Bottou, Curtis, and Nocedal analyze large-scale learning where stochastic gradients are central. The common evidence is conditional: performance and guarantees arise from the pairing of a model class, an information pattern, and an algorithm. (Sources: [4], [5], [6], [7], [8])

## Implications

### For Mathematical and Scientific Work: Formulation Is the First Experiment

For scientists and analysts, optimization formalizes a decision rule before data or computation make the answer look persuasive. The objective should state what error, cost, risk, or utility is being minimized; constraints should state what the model is not allowed to violate; and variables should correspond to quantities that can actually be chosen or estimated. A change from least squares to absolute error, for example, changes the estimator's criterion. A change from unconstrained coefficients to nonnegative coefficients changes the feasible set. These are model decisions with scientific consequences, not formatting choices in solver software. (Sources: [1], [2])

A defensible workflow is therefore: write the optimization problem; test that units and signs are compatible; identify whether the model is linear, convex, smooth, stochastic, or discrete; select a method with an applicable guarantee; and retain diagnostics for feasibility and optimality. This workflow is the author's synthesis of the source literature. Its purpose is to prevent the worst failure mode: treating a numerical output as evidence without knowing which mathematical question the computation answered. (Sources: [1], [2], [3])

### For Data Analysis and Machine Learning: Separate Training Loss From Decision Quality

Regression and machine learning often present optimization as minimizing a loss over parameters. That formulation is useful because it makes fitting, regularization, and constraints explicit. But a lower training objective does not by itself establish a better decision system: the objective may omit distribution shift, measurement error, fairness constraints, interpretability, or the cost of different mistakes. Optimization can enforce a chosen formulation; it cannot infer omitted values or validate an unrepresentative dataset. (Sources: [1], [7])

Large-scale learning adds an operational trade-off. Stochastic gradients allow iterations based on sampled data, which can make training feasible when full gradients are too costly. The price is noisy direction estimates and sensitivity to step policies and stopping rules. The practical implication is not to demand exact descent at every update, but to define validation criteria, monitor objective and constraint residuals, compare baselines, and preserve the distinction between an optimization guarantee and a generalization claim. Bottou, Curtis, and Nocedal support the method-selection premise; the monitoring protocol is an explicitly labeled synthesis. (Source: [7])

### For Engineers and Operations: Constraints Are Design Knowledge

In operations research and engineering, constraints often encode physical conservation, legal limits, service requirements, safety margins, capacity, or integrality. Optimization makes trade-offs visible by assigning a cost to alternative feasible plans and, through duality, can quantify local sensitivity to certain constraint changes when the relevant regularity conditions hold. This can guide which bottleneck is worth relaxing, but it should not be read as a proof that the original model captured all operational risks. (Sources: [1], [2])

A useful application pattern is to distinguish hard and soft requirements. Hard requirements belong in the feasible set because violating them is unacceptable. Soft preferences belong in the objective or in a separately reported trade-off analysis. Mixing the two without documentation can create a false appearance of precision: a large penalty may approximate a constraint but still permit violations that a true hard constraint would exclude. The distinction follows directly from the problem definition and is a practical synthesis of the modeling framework. (Sources: [1], [2])

### For Portfolio Construction: Optimization Is a Conditional Allocation Tool

Portfolio construction can be written as a constrained optimization problem in which weights are variables, expected return or another reward measure is part of the objective, and budget, position, liquidity, turnover, or exposure limits are constraints. The mathematical contribution is clarity: a proposed allocation can be tested against the stated risk measure and limits. It does not convert uncertain return estimates into known inputs. The separate library topic on modern portfolio theory develops the financial interpretation and estimation-risk critique; this topic supplies the general mathematical vocabulary. (Sources: [1], [2])

For a value investor, the critical question is not merely whether an optimizer found a weight vector with an attractive historical objective. It is whether the objective represents durable economics, whether constraints reflect permanent-loss and liquidity risks, and how sensitive the recommendation is to uncertain inputs. The following is the author's synthesis: use optimization to expose the consequences of assumptions, run sensitivity scenarios, impose explicit concentration and liquidity limits where appropriate, and reject the claim that a numerically optimal portfolio is automatically a prudent one. The discipline is analogous to checking a valuation model's drivers rather than accepting a point estimate. (Sources: [1], [2])

### For Discrete and High-Stakes Decisions: Require the Right Certificate

When decisions are discrete or high stakes, the relevant guarantee may be feasibility, a provable optimality gap, a global certificate, or a verified conservative bound. A local stationary point can be adequate for some exploratory nonlinear fitting tasks but inadequate for a safety-critical design decision. Convexity and duality can provide stronger certificates when the model meets their conditions; integer restrictions may require bounds or branch-and-bound style reasoning rather than a continuous relaxation presented as final. (Sources: [1], [2], [8])

The Candes and Tao case offers a general lesson in disciplined simplification. A convex surrogate can be highly effective when a theorem connects it to the original goal under explicit structural assumptions. The right question is therefore not "can this hard problem be made convex?" but "what is changed by the relaxation, and what evidence says the changed problem still recovers or bounds the decision we care about?" This question prevents a tractable surrogate from being mistaken for an exact model without supporting conditions. (Source: [8])

### For Communicating Results: Report Assumptions and Residuals

An optimization report should state the objective, variables, constraints, input provenance, solver or algorithm class, stopping rule, feasibility residuals, and sensitivity or uncertainty analysis. If a result is local rather than global, that limitation should be explicit. If inputs are estimated, the report should separate the optimizer's conditional conclusion from the uncertainty in those estimates. This reporting standard is the author's synthesis of the duality, KKT, complexity, and stochastic-optimization evidence reviewed above. (Sources: [1], [3], [4], [7])

The durable implication is epistemic. Optimization is strongest when it narrows a claim to what the mathematics and inputs warrant: "this point is feasible and optimal for the stated convex model," "this method has the stated bound," or "this sampled method reached the reported stopping criterion." It is weakest when those conditional claims are inflated into certainty about the external system. Maintaining that boundary makes optimization a tool for disciplined decision-making rather than a rhetorical substitute for judgment. (Sources: [1], [4], [5], [6], [7])

## Sources

1. Boyd, S. and Vandenberghe, L. (2004). "Convex Optimization."
   Cambridge University Press; author-hosted full text.
   https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf [high]

2. Dantzig, G. B. (1963; 2016 edition). "Linear Programming and Extensions."
   Princeton University Press.
   https://books.google.com/books?id=hUWPDAAAQBAJ [high]

3. Kjeldsen, T. H. (2000). "A Contextualized Historical Analysis of the
   Kuhn-Tucker Theorem in Nonlinear Programming: The Impact of World War II."
   Historia Mathematica, 27, 331-361. doi:10.1006/hmat.2000.2289.
   https://competitionandappropriation.econ.ucla.edu/wp-content/uploads/sites/95/2020/12/NonLPHistory.pdf [high]

4. Karmarkar, N. (1984). "A New Polynomial-Time Algorithm for Linear Programming."
   Combinatorica, 4, 373-395. doi:10.1007/BF02579150.
   https://doi.org/10.1007/BF02579150 [high]

5. Nesterov, Y. E. (1983). "A Method of Solving a Convex Programming Problem
   with Convergence Rate O(1/k^2)." Doklady Akademii Nauk SSSR, 269(3), 543-547.
   https://www.mathnet.ru/eng/dan/v269/i3/p543 [high]

6. Robbins, H. and Monro, S. (1951). "A Stochastic Approximation Method."
   Annals of Mathematical Statistics, 22(3), 400-407. doi:10.1214/aoms/1177729586.
   https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-22/issue-3/A-Stochastic-Approximation-Method/10.1214/aoms/1177729586.full [high]

7. Bottou, L., Curtis, F. E., and Nocedal, J. (2018). "Optimization Methods for
   Large-Scale Machine Learning." SIAM Review, 60(2), 223-311.
   https://bottou.org/papers/bottou-curtis-nocedal-2018 [high]

8. Candes, E. J. and Tao, T. (2005). "Decoding by Linear Programming."
   IEEE Transactions on Information Theory, 51(12), 4203-4215.
   https://candes.su.domains/software/l1magic/downloads/papers/DecodingLP.pdf [high]

## See Also

- `library/mathematics-statistics/linear-algebra.md` -- matrix geometry,
  definiteness, and linear systems used by optimization algorithms.
- `library/mathematics-statistics/regression-analysis.md` -- least squares,
  regularization, and statistical estimation as optimization problems.
- `library/mathematics-statistics/information-theory.md` -- entropy and
  constrained information-theoretic optimization.
- `library/portfolio-risk-management/modern-portfolio-theory.md` -- constrained
  mean-variance allocation as a financial application of optimization.
