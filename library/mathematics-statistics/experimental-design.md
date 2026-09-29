---
name: experimental-design
id: 20260827T070125Z
tier: library-topic
domain: mathematics-statistics
author: Librarian
tags: [experimental-design, randomization, blocking, replication, factorial-designs, control-groups, blinding, validity, replication-crisis, sample-size, power-analysis]
links: [library/mathematics-statistics/causal-inference.md, library/mathematics-statistics/statistical-inference.md, library/mathematics-statistics/probability-theory-fundamentals.md, library/mathematics-statistics/regression-analysis.md, library/mathematics-statistics/bayesian-statistics.md]
reviewed: 2026-09-29
---

# Experimental Design -- The Architecture That Separates Evidence from Anecdote

Experimental design specifies how treatments, experimental units, measurements, and analyses will be arranged so that an empirical comparison can answer a defined question. It creates the assignment-based basis for causal inference, controls avoidable variation, and exposes the assumptions that analysis alone cannot repair. Its central lesson is that a precise calculation is not reliable evidence when the data-generating process does not identify the claimed effect [1][4][5].

## Background

The modern mathematical theory of experimental design grew largely from agricultural work at Rothamsted Experimental Station. Ronald A. Fisher joined Rothamsted in 1919 to analyze long-running crop experiments whose yields varied with soil, weather, treatment, and field position. The setting forced a separation between treatment effects and background heterogeneity: a fertilizer comparison could not be interpreted merely by applying treatments in convenient rows and analyzing the resulting means. Fisher's work at Rothamsted connected analysis of variance with replication, blocking, factorial arrangements, and deliberate randomization [2][3].

Fisher and Winifred Mackenzie's 1923 potato study examined manurial responses across varieties and helped establish analysis of variance for field experiments. The paper's correct identifier is DOI 10.1017/S0021859600003592; the DOI 10.2307/2682986 belongs instead to Joan Fisher Box's 1980 historical analysis of Fisher's design work. Box describes the 1922-1926 development as an interaction between analysis and design: randomization justified the probability analysis, blocking separated known heterogeneity, replication supplied information about variation, and factorial arrangements made several questions answerable in one coordinated experiment [2][3].

Fisher's 1925 *Statistical Methods for Research Workers* spread statistical methods among scientists, while his 1935 *The Design of Experiments* treated design as a subject in its own right. The latter opened its operational discussion with the Lady tasting tea problem: eight cups, four prepared milk-first and four tea-first, are presented in randomized order, and the subject must classify four as each type. Fisher used the physical randomization to define the reference set against which the observed classification would be judged. His argument was not that randomization makes every realized group identical; it was that the known assignment procedure supplies a reasoned probability basis for a test and protects it from deliberate or systematic allocation [1][3].

This design-based view changed the statistician's role. Analysis could no longer be treated as a rescue operation performed after uncontrolled data collection. The experimental unit, treatment assignment, timing, measurement process, and comparison had to be planned together. Fisher's framework did not originate every idea associated with experimentation, and randomized procedures existed before him, but his synthesis made randomization, replication, local control, and factorial structure a coherent statistical program [1][3].

The social sciences extended the framework to settings in which full random assignment was often infeasible. Campbell and Stanley's 1963 monograph examined 16 experimental and quasi-experimental designs against 12 threats to valid inference. They distinguished internal validity, whether the treatment caused the observed difference in the studied setting, from external validity, whether the result generalizes across populations, settings, treatments, and measurements. Their catalogue made clear that a comparison can be numerically exact yet remain compatible with history, maturation, testing, instrumentation, regression to the mean, selection, attrition, or interactions between treatment and setting [4].

Clinical research supplied a second major application. The British Medical Research Council's 1948 streptomycin investigation used centrally prepared allocations based on random sampling numbers, concealed in sequential envelopes for each center and sex. Fifty-five patients were assigned streptomycin plus bed rest and 52 bed rest alone. The trial is a landmark in the adoption of concealed random allocation, but later historical work cautions against calling it the first controlled trial or treating its methods as wholly unprecedented. Participants were not told that they were in a trial, but active treatment involved streptomycin injections while the control involved bed rest alone, so treatment delivery itself was not masked; radiographic assessors and bacteriologists were kept unaware of treatment assignment [8][9][10].

Industrial design of experiments developed the same logic for processes rather than patients. Full factorial designs run every combination of factor levels, allowing main effects and interactions to be estimated within one plan. Blocking protects comparisons from known batch, operator, or time shifts. Fractional factorial designs reduce the number of runs by deliberately aliasing effects according to a defining relation, so efficiency is purchased with explicit assumptions about which interactions can be neglected. The NIST/SEMATECH handbook presents these designs as choices governed by objectives, nuisance factors, resources, and the effects that must remain separately estimable [5].

Late twentieth- and early twenty-first-century concerns about selective analysis and replication renewed attention to design. Simmons, Nelson, and Simonsohn demonstrated that optional stopping, outcome choice, covariate choice, and selective comparison can make a nominal 5% test operate very differently when the successful analysis alone is reported. The Open Science Collaboration later repeated 100 studies from three psychology journals and found weaker effects under new data despite high planned power and methodological review. These results do not prove that one defect explains every discrepancy; they show why assignment, sample-size planning, analysis specification, transparent reporting, and replication belong to one evidence architecture [11][12].

The current framework is therefore broader than the classical list of randomization, replication, and blocking. A complete design identifies the estimand, experimental unit, assignment mechanism, treatment versions, outcome, measurement schedule, stopping rule, missing-data risks, analysis plan, and target population. It also anticipates interference, nonadherence, multiplicity, attrition, and transport beyond the sample. Modern reporting and preregistration standards make these commitments visible, but visibility does not substitute for a design capable of answering the question [6][14][15][17].

## Core Concepts

### The Question, Estimand, and Experimental Unit

Design begins with the contrast to be learned. The researcher must specify the units, treatments or interventions, comparison condition, outcome, time horizon, and target population. "Does the treatment work?" is incomplete when dose, delivery, adherence, outcome definition, and follow-up are unspecified. A design can estimate the effect of assignment, the effect of receiving treatment, a dose-response contrast, an interaction, or a local effect for a particular population; these are not interchangeable targets [4][8][14].

The experimental unit is the smallest unit independently assigned to a treatment under the design. If classrooms are assigned but pupils are measured, the classroom is the unit of assignment even though pupils provide observations. If one mouse supplies several tissue wells, the mouse may be the independent biological unit while the wells are technical measurements. Treating measurements nested within one assigned unit as independent treatment replications understates uncertainty and changes the question being tested [7].

Outcome definitions also belong in the design. A clinical symptom scale, radiographic assessment, mortality endpoint, manufacturing yield, and user-click rate answer different questions and have different vulnerability to expectation, measurement error, censoring, and competing outcomes. Timing can alter the estimand: an early response need not imply durable benefit, and a long follow-up can introduce treatment changes or attrition. Campbell and Stanley's validity framework and CONSORT's reporting requirements both treat measurement and follow-up as design features rather than clerical details [4][15].

### Random Assignment and Allocation Concealment

Random assignment uses a known chance mechanism to allocate treatments. Under the design, assignment is independent of fixed potential outcomes, so treatment groups are comparable in expectation and randomization-based probabilities can be calculated from the assignments that could have occurred. Randomization does not guarantee identical baseline groups in one realized experiment; chance imbalance remains possible, especially with small samples. Its protection is against systematic assignment bias and its provision of a known reference distribution, not automatic numerical balance [1][5].

Allocation concealment is distinct from random sequence generation. A valid random sequence can be subverted if the person enrolling units can foresee the next assignment and alter eligibility or timing. Central assignment or properly controlled sequential opaque containers protect the sequence until a unit is irrevocably entered. The MRC streptomycin trial is historically important in part because the random-number series was centrally controlled and unavailable to investigators before allocation [9][10].

Randomization also does not make observations independent or eliminate interference. Outcomes can be correlated within households, schools, batches, or repeated measurements. One unit's treatment can affect another unit through contagion, competition, communication, or shared resources. Rosenbaum defines interference precisely as treatment applied to one unit affecting other units; when it is plausible, the unit of randomization, exposure definition, and analysis must represent it rather than relying on an ordinary independent-observation model [6].

### Replication, Repeated Measurement, and Precision

Replication applies each treatment to multiple independent experimental units. It provides information about unit-to-unit variation and improves precision. Repeatedly measuring the same unit can reduce measurement error for that unit, but it does not create additional independent treatment assignments. The relevant replication count follows the assignment and inference structure, not the number of rows in a data table [5][7].

Classical residual variance cannot be estimated from a one-factor fixed-effects model with one observation at every treatment level and no other source of error information. That statement is narrower than saying no test is ever possible without conventional replication: some randomization tests or structured designs use other information. The general design lesson is that a claim about variation across units needs independent units or defensible external structure, while repeated technical readings answer only a measurement question [1][5][7].

Precision depends on more than the raw number of observations. Outcome variance, allocation ratio, clustering, repeated measures, attrition, multiplicity, covariate adjustment, effect size, and the chosen test all affect the sampling distribution. Power is the probability that a prespecified procedure rejects the null under a specified alternative and design. A target such as 80% is a convention, not a universal scientific standard, and the calculation is only as meaningful as its effect-size and variance assumptions [12][13][15].

### Blocking and Local Control

Blocking groups units that are similar on an important nuisance factor and randomizes treatments within each block. In a field trial, blocks may represent soil zones; in a multicenter trial, they may represent sites or prognostic strata; in manufacturing, they may represent material lots or shifts. The purpose is not to make nuisance variation disappear from reality but to keep it from obscuring the treatment comparison and to ensure that treatment contrasts are made within comparable sets [3][5].

Blocking has costs. Blocks must be defined before outcomes are known, very small blocks can make assignment predictable when concealment is weak, and analysis must respect the blocked assignment. Blocking on many weak factors can complicate implementation without improving precision. The design question is which few nuisance variables are strongly related to the outcome and operationally available before treatment assignment [5][15].

A randomized complete block design places every treatment in every block. A Latin square controls two blocking factors by placing each treatment exactly once in every row and column. The standard additive Latin-square analysis requires the number of levels of each blocking factor to equal the number of treatment levels and assumes away treatment-by-block and block-by-block interactions. Those restrictions are not minor formatting details; when important interactions exist, the design cannot separate them from the terms it was built to estimate [5].

### Factorial and Fractional Factorial Designs

A factorial design varies two or more factors together. A full two-level design with k factors has 2^k treatment combinations, so five factors require 32 combinations before replication or center points. Main effects summarize average changes across the levels of other factors, while interactions ask whether one factor's effect changes with another factor. This ability to estimate interactions is the main conceptual advantage over changing one factor at a time [5].

A main effect can be misleading when interactions are strong. If a treatment helps under one operating condition and harms under another, the average can be near zero even though both conditional effects matter. Factorial analysis therefore begins with the estimable interaction structure and scientific hierarchy rather than interpreting main effects mechanically. The design should also distinguish fixed factor levels chosen for comparison from broader populations of possible levels [5].

Fractional factorial designs run a selected fraction of all combinations. Their defining relation determines the alias structure: in a resolution III design, main effects can be aliased with two-factor interactions; in resolution IV, main effects are clear of two-factor interactions but two-factor interactions may be aliased with one another. A fraction does not discover which aliased effect caused an observed contrast. It is efficient only when the assumed sparsity or hierarchy of effects is scientifically defensible and follow-up runs can resolve important ambiguities [5].

### Controls, Blinding, and Comparable Treatment

A control condition supplies the counterfactual benchmark built into the study. Depending on the question and ethics, it may be placebo, no treatment, usual care, an active treatment, another dose, or an external historical comparison. A control group does not literally hold every other condition constant. Comparable treatment, follow-up, and measurement must be maintained, and differential adherence, co-intervention, attrition, or observation can reintroduce bias after random assignment [13][14].

Blinding withholds assignment information from people whose behavior or assessments could be influenced by it. Participants, care providers, outcome assessors, adjudicators, and data analysts are distinct roles. Terms such as "single blind" and "double blind" are ambiguous because different reports use them for different combinations. CONSORT 2025 therefore asks authors to state who was blinded, how blinding was achieved, and how similar the interventions appeared [15].

Blinding is not always feasible. Surgical procedures, behavior programs, workplace policies, and obvious side effects can reveal assignment. The response is not to call an open study blinded, but to use feasible safeguards: concealed allocation, blinded outcome assessment, objective endpoints where appropriate, standardized co-interventions, prespecified decision rules, and transparent reporting. The MRC streptomycin trial illustrates this separation: treatment was apparent, yet radiographic and bacteriological assessment was blinded [8][10].

### Internal, Construct, External, and Statistical Conclusion Validity

Internal validity asks whether the observed contrast can be attributed to the treatment rather than a rival process in the study. Selection, history, maturation, testing effects, instrumentation changes, regression to the mean, and differential attrition are classic rivals. Random assignment addresses baseline selection under correct implementation, but it does not automatically prevent missing outcomes, treatment crossover, biased measurement, or post-randomization selection [4][15].

Construct validity asks whether the operational treatment and measurement represent the intended concepts. External validity asks where the result transports: other units, settings, treatment versions, outcomes, and times. Statistical conclusion validity concerns whether the data and analysis support the asserted covariation with appropriate control of error and adequate precision. Cook and Campbell's 1979 framework assessed designs against these four validity types, extending Campbell and Stanley's earlier emphasis on internal and external validity and concrete threats [4][18].

These validities can conflict but should not be reduced to a slogan that control always sacrifices realism. A tightly standardized study can fail to represent ordinary implementation, while a broad field study can preserve strong internal validity through random assignment and careful measurement. Generalization requires a model of effect modifiers and implementation, not merely a larger or more diverse sample. The design should say which validity threats it addresses and which remain [4][14].

### Analysis Plans, Multiplicity, and Transparency

A design includes the analysis choices that determine its operating characteristics. Primary outcomes, exclusions, transformations, covariates, subgroup analyses, stopping rules, and multiplicity procedures should be specified before outcome patterns can influence them when the analysis is intended to be confirmatory. Simmons and colleagues showed in simulations that individually plausible freedoms can combine to produce a false-positive rate far above the nominal level when only the favorable result is disclosed [12].

Preregistration timestamps hypotheses and methods before results are known. It separates planned tests from exploratory analyses but does not make a weak measure valid, force investigators to follow a mistaken plan, or guarantee honest implementation. Deviations can be scientifically necessary; they must be disclosed and labeled. Registered reports add review and in-principle publication decisions before outcomes, further reducing selection on whether results are striking [17].

Transparent reporting is not identical to sound design. CONSORT can reveal how a trial was conducted, but complete reporting of biased allocation does not remove the bias. Conversely, an excellent design reported incompletely cannot be critically appraised or replicated. Design, conduct, analysis, and reporting are separate links whose failures require different corrections [14][15].

## Evidence

### Fisher's Tea Experiment Shows How Assignment Creates a Test

In Fisher's eight-cup design, the subject knows that exactly four cups are milk-first and must identify four. There are C(8,4) = 70 possible four-cup selections under the null assignment logic, and only one is entirely correct, so the probability of a perfect classification by chance is 1/70, approximately 0.0143. If three of each type are correctly classified, the forced four-and-four response entails one swap in each direction; 16 such selections plus the perfect one give an upper-tail probability of 17/70, approximately 0.243. The calculation is exact because the randomized design and response rule define the reference set [1].

The case also exposes what randomization does not protect. If all milk-first cups differed systematically in sugar, temperature, cup texture, or another feature, the subject could classify the preparation without detecting pour order. Fisher explicitly used such examples to show that randomization cannot excuse the experimenter from avoiding treatment-linked differences introduced during preparation or measurement. Assignment protects against uncontrolled allocation of other causes; it does not erase a second intervention confounded with the treatment [1].

The published book explains the hypothetical design and inferential logic but does not establish the later folklore that Muriel Bristol completed this exact formal experiment and classified all eight cups correctly. That anecdote should not be used as the evidentiary result of Fisher's text. The durable evidence is methodological: a small experiment can have a transparent exact test when its assignments, response space, and decision rule are specified before the result [1].

### Rothamsted Linked Heterogeneity, Blocking, and Factorial Structure

Fisher and Mackenzie's potato study analyzed variety and manure response in field data using an analysis that separated sources of variation. Box's historical reconstruction explains how this work and related Rothamsted problems led Fisher to connect analysis of variance with randomized blocks, replication, factorial arrangements, and confounding. The contribution was not a general finding that blocking always produces a particular percentage reduction in variance; it was a method for allocating known heterogeneity to design terms so treatment comparisons could be made against an appropriate error structure [2][3].

This history corrects two errors in the prior topic. The 1923 Fisher-Mackenzie paper and Box's 1980 article do not share a DOI: their identifiers are 10.1017/S0021859600003592 and 10.2307/2682986, respectively. The potato study also should not be described as simple evidence from six varieties in a generic randomized complete block unless the exact layout and estimand are established from the paper. The verified claim is narrower: it examined manurial responses of potato varieties and helped develop factorial ANOVA for field experimentation [2][3].

### The MRC Streptomycin Trial Separates Allocation, Masking, and Outcome

The primary 1948 report's six-month radiographic-outcome table records four deaths among 55 patients assigned streptomycin plus bed rest and 14 deaths among 52 assigned bed rest alone, approximately 7.3% and 26.9%. Crofton's later first-person retrospective reports 15 control deaths for the same interval; because the contemporaneous table and the retrospective disagree, the primary table governs the counts used here and the discrepancy remains explicit. The trial used a centrally controlled random-number sequence concealed until allocation, and radiographic assessors and bacteriologists were blinded even though treatment delivery itself was not masked [8][9][10].

The study therefore demonstrates several separable design protections. Concealed random allocation limited enrollment and assignment bias. A concurrent control represented the disease course under bed rest. Blinded assessment reduced knowledge-of-treatment bias in radiographic and bacteriological judgments. Defined eligibility, follow-up, and outcomes made the comparison interpretable. Scarcity of streptomycin also gave random allocation an allocation-fairness role, but methodological merit does not remove the ethical need for uncertainty, consent standards, monitoring, and justified control conditions [8][9][10].

Historical precision matters. The trial is commonly described as inaugurating the modern randomized clinical trial, but earlier controlled and chance-based allocations existed. Yoshioka concludes that it deserves recognition for careful design and implementation while being less novel than popular accounts imply. The defensible claim is that its clearly documented central randomization and masked outcome assessment became an influential model, not that random treatment allocation first appeared in medicine in 1948 [9][10].

### Campbell and Stanley Made Rival Explanations Auditable

Campbell and Stanley assessed 16 designs against 12 threats, including three pre-experimental designs, three true experiments, and multiple quasi-experimental arrangements. Their one-group pretest-posttest design could not isolate treatment from history, maturation, testing, instrumentation, or regression. Randomized control-group designs blocked many internal-validity rivals, while interrupted time series, nonequivalent controls, and regression discontinuity addressed specific settings with remaining assumptions [4].

The catalogue is evidence about logical control, not a trial showing that every randomized design generalizes or every quasi-experiment fails. Its value lies in forcing a design-specific question: which rival explanations can produce this exact observed pattern, and which features rule them out? The tables are not a mechanical scorecard detached from context; Campbell and Stanley themselves warned that the design notation must be interpreted with the underlying psychological and institutional processes [4].

### Researcher Flexibility Changes the Actual Error Process

Simmons, Nelson, and Simonsohn simulated four researcher freedoms: choosing among outcomes, adding observations after an interim result, choosing covariate specifications, and selecting comparisons among conditions. In their specified simulation, using all four while reporting the favorable analysis produced a 61% false-positive rate rather than the nominal 5%. Individual freedoms also raised the rate, such as outcome choice to 9.5% and flexible covariate handling to 11.7% under their settings [12].

The 61% figure is not an estimate of the proportion of published science that is false. It is a causal demonstration that an unreported search process changes the probability attached to the reported result. Prespecification, full disclosure, multiplicity adjustment, and independent confirmation address different parts of that problem. A preregistered plan can still be wrong, while an exploratory result can be useful when it is labeled and tested with new data [12][17].

### The Reproducibility Project Bounds Claims About Replication

The Open Science Collaboration completed replications of 100 experimental and correlational studies drawn from three psychology journals. Ninety-seven percent of original studies had statistically significant results, compared with 36% of replications. Mean replication effect size was about half the mean original effect size; 47% of original effect estimates fell within the replication estimate's 95% confidence interval, and 39% were subjectively rated as replicated. The teams planned high power to detect the original effect sizes and obtained original materials where available [11].

No single percentage is a universal replication rate. The project used several criteria because threshold crossing, interval compatibility, effect-size change, meta-analysis, and expert assessment answer different questions. Its sample covered selected journals and a defined period; incomplete access to materials, contextual differences, original selection, sampling variation, and genuine heterogeneity can all contribute. The published conclusion is appropriately bounded: many replications produced weaker evidence despite methodological review and high power for the original effect size [11].

### Low Power Distorts More Than the Chance of Detection

Button and colleagues reviewed neuroscience evidence and argued that low power reduces the chance of detecting a true effect and, in a literature selected for positive results, contributes to effect-size exaggeration and poor reproducibility. The mechanism is selection: among noisy estimates, those that cross a threshold tend to be unusually large. This does not mean lowering sample size changes a valid test's conditional Type I error from 5% under a true null when all assumptions are met. It means that power, prior prevalence of real effects, bias, and publication selection jointly affect how credible and how exaggerated published positives are [13].

Power analysis therefore belongs before data collection and must name the alternative, variance, test, allocation, and losses it assumes. CONSORT 2025 requires reporting how sample size was determined and all supporting assumptions. After results are observed, uncertainty intervals and sensitivity analyses are more informative than treating power recomputed from the observed effect as new evidence [13][15].

### Placebo History Shows Why a Control Response Is Not a Placebo Effect

Beecher's 1955 paper reviewed 15 studies involving 1,082 patients and attributed improvement in about 35% to a powerful placebo response. Kienle and Kiene's later reanalysis argued that the cited studies did not isolate a causal placebo effect because improvement could reflect spontaneous recovery, symptom fluctuation, regression to the mean, additional treatment, or measurement processes. The historical claim should therefore be reported as Beecher's estimate, not as a settled fraction of therapeutic effects caused by suggestion [16].

This distinction is a compact lesson in control design. Change from baseline in a placebo group is not itself the placebo effect; identifying a causal effect of receiving placebo generally requires a suitable no-treatment comparison and protection against other differences. A placebo-controlled drug trial can identify the drug's effect relative to the placebo condition without separately identifying every component of the placebo response [14][16].

## Implications

### For Scientific Research

The first implication is to design backward from the claim. Define the experimental unit, treatment contrast, primary outcome, timing, and target population; then choose assignment, blocking, replication, and measurement procedures that identify that contrast. Analysis should respect the assignment mechanism and clustering. A sophisticated model cannot turn repeated measurements into independent assignments, reconstruct an outcome never measured, or distinguish a treatment from a factor perfectly confounded with it [5][7].

Confirmatory and exploratory work should be separated without devaluing either. Preregistered hypotheses, outcomes, exclusions, stopping rules, and models make the intended error process auditable. Exploratory patterns can generate new hypotheses, but the same data that revealed a pattern do not provide an independent test of it. The author's synthesis is that the reversible design is to preserve exploratory findings, label them, and allocate new data to confirmation rather than suppress exploration or relabel it after the fact [12][17].

Replication should target the scientific claim rather than reproduce only a threshold label. A direct replication tests a closely matched procedure; a conceptual replication changes operations while preserving a proposed construct; a multisite study tests variation across settings. Effect estimates, uncertainty, protocol fidelity, and heterogeneity are needed to interpret discrepancies. The Open Science Collaboration demonstrates why several indicators are preferable to declaring success solely from whether both studies have p below 0.05 [11].

### For Clinical Trials and Regulation

Clinical design must align the control with the question and ethical setting. FDA regulation recognizes placebo, dose-comparison, no-treatment, active-treatment, and historical controls rather than requiring every approval trial to be randomized, double-blind, and placebo-controlled. Concurrent controls ordinarily use randomization to minimize bias, while historical controls are reserved for special circumstances because patient comparability is harder to establish. Blinding is one bias-reduction method, not a universal legal design formula [14].

Reports should state the random sequence, restrictions such as stratification or blocks, concealment mechanism, access to the sequence, roles blinded, intervention similarity, outcomes, harms, sample-size assumptions, analysis populations, attrition, and protocol changes. CONSORT 2025 is a reporting minimum, not a certificate that every choice was valid. Its practical value is that readers need not guess whether allocation was concealed, who assessed outcomes, or how the analysis population was defined [15].

Adaptive and sequential designs can modify enrollment, allocation, sample size, or stopping under prespecified rules. Their validity depends on accounting for those rules in inference and protecting interim information. An unplanned stop after a favorable look is not equivalent to a planned group-sequential design. The general principle is unchanged: flexibility can be valid when its probability consequences are designed in advance, and misleading when hidden after results are known [12][15].

### For Engineering and Industrial Experimentation

Engineers should use factorial designs when interactions are plausible and several controllable factors must be studied together. A five-factor, two-level full factorial requires 32 combinations, not 160 one-factor-at-a-time runs. One-factor-at-a-time testing uses a different and often smaller run set, but it cannot estimate interactions efficiently and can miss settings whose performance depends on combinations. The comparison should therefore concern information per run, not an invented universal run multiplier [5].

Fractional designs require an alias audit before data collection. The researcher should list which main effects and interactions are confounded, choose a resolution appropriate to the scientific hierarchy, randomize run order within operational constraints, block predictable shifts, and reserve follow-up runs for de-aliasing. A software-generated design is not self-interpreting; its defining relation states exactly which explanations the data cannot distinguish [5].

Robust process improvement also needs confirmation. Screening experiments identify a small set of candidate factors; response-surface or follow-up designs refine settings; confirmation runs test performance under new conditions. The author's synthesis is that this sequence prevents an optimization algorithm from exploiting noise in the same runs used to discover the setting. It is the industrial analogue of separating exploration from confirmation [5][12].

### For Digital Products and AI Evaluation

Online controlled experiments inherit ordinary design requirements and add interference, rapid iteration, and large multiplicity. User-level randomization may fail when one user's treatment affects another through a network, marketplace, ranking system, or shared capacity. Cluster randomization, geographic or temporal designs, or explicit interference models can be appropriate, but each changes the estimand and effective sample size. Large numbers of users do not correct a wrong unit of randomization [6].

Benchmark evaluation of AI systems similarly needs prespecified prompts or tasks, sampling rules, model versions, decoding settings, blinded or otherwise protected assessment, and uncertainty across items and raters. Repeated outputs from the same prompt are not automatically independent evidence about population performance. Testing many prompts, metrics, evaluators, and checkpoints and publishing only the most favorable comparison recreates the researcher-flexibility problem at computational scale [7][12].

The author's synthesis is to separate development and evaluation data. Development sets can guide prompt, model, and metric choices; locked evaluations or prospectively sampled tasks test the resulting system. When deployment changes user behavior or the data distribution, a static benchmark answers a narrower question than a randomized field evaluation. The scope of the claim should follow the design actually used [6][12].

### For Policy and Quasi-Experiments

When random assignment is infeasible, the experimental-design framework still clarifies the missing comparison. Interrupted time series, regression discontinuity, matched comparison groups, and natural experiments each rule out some rivals while requiring assumptions about trends, thresholds, selection, or concurrent events. Calling a study quasi-experimental is not itself an identification argument; the institutional assignment process and specific threats must be stated [4].

Policy trials also face treatment variation across sites, spillovers, implementation failure, and outcomes measured through administrative systems. Blocking or stratification can protect balance on key site characteristics, cluster designs can align assignment with delivery, and process measures can distinguish a failed program theory from failed implementation. External validity requires describing which institutions and populations implemented which version of the policy [4][6].

### For Business and Investing

Business experiments should define the unit that can be changed and the metric that represents value rather than convenience. A price test can affect customer mix and competitor response; a retention intervention can spill over through referrals; a store-level treatment analyzed as customer-level independence can overstate precision. The same design logic that distinguishes experimental units from measurements prevents a large transaction table from masquerading as a large number of independent tests [6][7].

For investors, the author's synthesis is that reported experimental evidence should be audited as a data-generating process. Ask who or what was assigned, which outcome was primary, whether attrition differed, how many analyses were available, whether effect sizes are economically material, and whether the studied treatment and population match the business decision. A statistically precise lift in a proxy metric may not identify durable cash-flow impact, and a failed threshold test may still leave economically important effects compatible with the data [12][13].

### For Ethics and Governance

Design quality is an ethical issue because weak studies expose participants or consume resources without a realistic chance of answering the stated question. Underpowered or pseudoreplicated studies can waste scarce samples, while concealed multiplicity can produce confident but unstable claims. Adequate planning should balance precision and information against burden rather than treating the largest feasible sample or most measurements as automatically best [7][13].

Random allocation can be fair when scarce treatment cannot be given to all eligible participants, as in the streptomycin setting, but fairness is context-dependent. Equipoise, consent, monitoring, stopping rules, access after the trial, and protection of vulnerable groups remain separate obligations. A statistically valid randomization does not by itself make an experiment ethically justified [8][10].

Governance should favor auditable stages: protocol approval, registered hypotheses and analyses, controlled access to allocation sequences, monitored deviations, complete outcome reporting, and independent verification for consequential claims. The single worst failure is a design whose hidden choices allow a desired conclusion to determine which data and analysis become visible. Preregistration and reporting standards reduce that risk only when institutions enforce disclosure and preserve unfavorable results [12][15][17].

### A Practical Design Audit

A practical audit begins with ten questions. What is the estimand? What is the experimental unit? How were units assigned, and was allocation concealed? Which nuisance variables were blocked or stratified? What outcomes and times were primary? Which roles were blinded? How were sample size and stopping determined? Which exclusions and analyses were prespecified? Could interference, attrition, or nonadherence alter the contrast? To which population and treatment version can the result generalize? [4][6][14][15].

The answers should be connected rather than checked as isolated boxes. Cluster assignment changes the effective sample size; blinding may change measurement validity; attrition can break the initial comparability; multiple outcomes change the error process; and transport may fail even when internal validity is strong. The author's synthesis is that experimental design is best understood as a dependency graph: each conclusion depends on an estimand, an assignment, a measurement, and an analysis that remain mutually consistent.

## Common Pitfalls

### Treating Randomization as Guaranteed Balance

Randomization balances fixed characteristics in expectation, not exactly in each sample. Baseline imbalances can occur without proving failure, while suspicious assignment patterns can arise from implementation defects. Report the actual assignment procedure, examine baseline data descriptively, and improve precision through prespecified adjustment or blocking rather than using significance tests to certify that randomization worked [1][5][15].

### Counting Measurements Instead of Experimental Units

Ten measurements from one assigned unit do not equal ten independent assignments. Identify the level at which treatment could have differed, model nested dependence, and state the population of units to which the claim applies. Pseudoreplication is a design error because the denominator of inference does not match the treatment replication [7].

### Calling Every Controlled Trial Double-Blind

Blinding labels conceal role-specific information. State separately whether participants, care providers, outcome assessors, adjudicators, and analysts knew assignment. When a role cannot be blinded, explain the protection used instead. The streptomycin trial's masked assessors did not make its visible injections double-blind for all roles [8][10][15].

### Confusing Placebo-Group Change with a Placebo Effect

Improvement in a placebo group includes natural history, regression to the mean, co-intervention, measurement, and context. A causal placebo effect needs a design that separates those components, often through an appropriate no-treatment comparison. Beecher's historical 35% estimate did not achieve that isolation and should not be repeated as a universal therapeutic constant [16].

### Ignoring Interactions

A main effect averages over other factor levels. If conditional effects differ, the average can obscure the operational result. Inspect interactions that the design can estimate, and do not claim to resolve effects that the fractional design aliases. One-factor-at-a-time testing avoids neither confounding nor interaction; it mainly leaves interactions unmeasured [5].

### Planning Power from an Inflated Published Effect

A replication powered only for an original selected estimate may be too small for the true effect if the original was exaggerated. Plan around a scientifically meaningful effect and plausible variance, report sensitivity across assumptions, and distinguish precision goals from a ritual 80% target. Low power plus outcome selection can exaggerate the estimates that enter later planning [11][13].

### Treating Preregistration as Infallibility

A timestamped plan can contain a bad measure, implausible model, or coding error. Follow justified corrections, disclose deviations, preserve the original plan, and label new analyses. The value of preregistration is provenance: readers can distinguish prediction from post hoc accommodation [17].

### Interpreting Non-Replication as One Unique Diagnosis

A weaker replication can reflect an original false positive, an exaggerated original effect, a replication false negative, implementation differences, measurement error, or effect heterogeneity. Compare protocols, effects, intervals, fidelity, and target populations before attributing cause. Multiple indicators in the Reproducibility Project were designed precisely because no single binary criterion settles the diagnosis [11].

## Sources

1. Fisher, R. A. (1935; 8th ed. 1966). "The Design of Experiments."
   Oliver and Boyd. Primary treatment of randomization and the Lady
   tasting tea design.
   https://archive.org/details/in.ernet.dli.2015.502684 [high]

2. Fisher, R. A. and Mackenzie, W. A. (1923). "Studies in Crop
   Variation. II. The Manurial Response of Different Potato Varieties."
   Journal of Agricultural Science, 13(3), 311-320.
   https://doi.org/10.1017/S0021859600003592 [high]

3. Box, J. F. (1980). "R. A. Fisher and the Design of Experiments,
   1922-1926." The American Statistician, 34(1), 1-7.
   https://doi.org/10.2307/2682986 [high]

4. Campbell, D. T. and Stanley, J. C. (1963). "Experimental and
   Quasi-Experimental Designs for Research." Houghton Mifflin.
   https://jwilson.coe.uga.edu/EMAT7050/articles/CampbellStanley.pdf
   [high]

5. NIST/SEMATECH. "e-Handbook of Statistical Methods," sections on
   completely randomized, block, Latin-square, full-factorial, and
   fractional-factorial designs. NIST Handbook 151.
   https://doi.org/10.18434/M32189 [high]

6. Rosenbaum, P. R. (2007). "Interference Between Units in Randomized
   Experiments." Journal of the American Statistical Association,
   102(477), 191-200.
   https://doi.org/10.1198/016214506000001112 [high]

7. Hurlbert, S. H. (1984). "Pseudoreplication and the Design of
   Ecological Field Experiments." Ecological Monographs, 54(2),
   187-211. https://doi.org/10.2307/1942661 [high]

8. Medical Research Council. (1948). "Streptomycin Treatment of
   Pulmonary Tuberculosis: A Medical Research Council Investigation."
   British Medical Journal, 2(4582), 769-782.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC2091872/ [high]

9. Yoshioka, A. (1998). "Use of Randomisation in the Medical Research
   Council's Clinical Trial of Streptomycin in Pulmonary Tuberculosis in
   the 1940s." BMJ, 317, 1220-1223.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC1114162/ [high]

10. Crofton, J. (2006). "The MRC Randomized Trial of Streptomycin and
    Its Legacy: A View from the Clinical Front Line." Journal of the
    Royal Society of Medicine, 99(10), 531-534.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC1592068/ [high]

11. Open Science Collaboration. (2015). "Estimating the Reproducibility
    of Psychological Science." Science, 349(6251), aac4716.
    https://doi.org/10.1126/science.aac4716 [high]

12. Simmons, J. P., Nelson, L. D., and Simonsohn, U. (2011).
    "False-Positive Psychology: Undisclosed Flexibility in Data
    Collection and Analysis Allows Presenting Anything as Significant."
    Psychological Science, 22(11), 1359-1366.
    https://doi.org/10.1177/0956797611417632 [high]

13. Button, K. S., Ioannidis, J. P. A., Mokrysz, C., Nosek, B. A.,
    Flint, J., Robinson, E. S. J., and Munafo, M. R. (2013). "Power
    Failure: Why Small Sample Size Undermines the Reliability of
    Neuroscience." Nature Reviews Neuroscience, 14, 365-376.
    https://doi.org/10.1038/nrn3475 [high]

14. U.S. Food and Drug Administration. "21 CFR 314.126 -- Adequate and
    Well-Controlled Studies." Electronic Code of Federal Regulations.
    https://www.ecfr.gov/current/title-21/chapter-I/subchapter-D/part-314/subpart-D/section-314.126
    [high]

15. Hopewell, S., Chan, A.-W., Collins, G. S., et al. (2025). "CONSORT
    2025 Statement: Updated Guideline for Reporting Randomised Trials."
    BMJ, 389, e081123.
    https://doi.org/10.1136/bmj-2024-081123 [high]

16. Kienle, G. S. and Kiene, H. (1997). "The Powerful Placebo Effect:
    Fact or Fiction?" Journal of Clinical Epidemiology, 50(12),
    1311-1318. https://doi.org/10.1016/S0895-4356(97)00203-5 [high]

17. Nosek, B. A., Ebersole, C. R., DeHaven, A. C., and Mellor, D. T.
    (2018). "The Preregistration Revolution." Proceedings of the
    National Academy of Sciences, 115(11), 2600-2606.
    https://doi.org/10.1073/pnas.1708274114 [high]

18. Cook, T. D. and Campbell, D. T. (1979). "Quasi-Experimentation:
    Design and Analysis Issues for Field Settings." Houghton Mifflin.
    https://archive.org/details/quasiexperimenta00cook [high]

## See Also

- `library/mathematics-statistics/causal-inference.md` -- the estimands and assumptions that connect assignment mechanisms to causal effects.
- `library/mathematics-statistics/statistical-inference.md` -- estimation and uncertainty after the design defines a valid comparison.
- `library/mathematics-statistics/probability-theory-fundamentals.md` -- the probability structures underlying random assignment and sampling.
- `library/mathematics-statistics/regression-analysis.md` -- analytical models that must preserve the assignment, blocking, and dependence structure.
- `library/mathematics-statistics/bayesian-statistics.md` -- model-based updating and adaptive analysis that still depend on sound design.
