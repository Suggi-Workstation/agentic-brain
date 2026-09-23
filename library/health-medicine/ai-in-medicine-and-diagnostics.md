---
name: ai-in-medicine-and-diagnostics
id: 20260829T131915Z
tier: library-topic
domain: health-medicine
author: Librarian
tags: [artificial-intelligence, machine-learning, deep-learning, medical-imaging, clinical-decision-support, radiology, diagnostic-ai, large-language-models, algorithmic-bias]
links: [library/technology/large-language-models.md, library/health-medicine/drug-development-from-molecule-to-medicine.md, library/health-medicine/public-health-epidemiology.md]
reviewed: 2026-09-23
---

# AI in Medicine and Diagnostics -- How Deep Learning Reached Clinician-Level Accuracy and Why Clinical Deployment Still Lags the Benchmarks

AI in medicine and diagnostics applies machine learning to images, text, and
structured records to detect, classify, or triage disease. On narrow imaging
tasks, controlled studies have shown performance comparable with specialists,
and a direct count of unique submission identifiers in the US Food and Drug
Administration's (FDA's) September 4, 2026 public list yields 1,614 authorized
AI-enabled devices ([1] [2] [5]). Yet
benchmark performance has advanced faster than prospective evidence about
patient care, external validity, human interaction, and postmarket behavior
([13] [14] [18] [20]).

## Background

Automated medical reasoning predates modern machine learning. Edward
Shortliffe's 1974 MYCIN dissertation described a rule-based system designed
to help physicians select antimicrobial treatment for bacterial infections;
experts supplied rules that the consultation program used to generate and
explain recommendations ([17]). This architecture exposed a lasting
constraint: clinical knowledge had to be elicited, encoded, and maintained
explicitly. The systems were difficult to update and integrate into routine
care, even when demonstrations appeared technically capable ([15] [17]).

Image analysis developed along a separate path. In 1998, the FDA authorized
the first computer-aided detection system for screening mammography. It
marked suspicious regions for a radiologist's review rather than making an
autonomous diagnosis ([23]). This early second-reader model established a
pattern that persists: a device can be marketed for a bounded task while the
clinical value of the complete human-machine workflow remains an additional
evidence question ([14] [23]).

The deep-learning turning point came with the 2012 ImageNet competition.
AlexNet was trained on about 1.2 million labeled images and achieved a 15.3
percent top-five test error rate, compared with 26.2 percent for the
second-place entry ([16]). Convolutional neural networks could learn visual
features from data instead of depending entirely on hand-designed image
features. Because medical images are also arrays of pixel values, researchers
could adapt the same family of architectures to bounded classification tasks,
although the clinical labels, acquisition processes, and consequences of
error were different from those in a photographic benchmark ([1] [2] [15]).

Two retrospective studies demonstrated the new capability. Gulshan and
colleagues trained a network on 128,175 retinal photographs graded three to
seven times by a panel of 54 ophthalmologists and ophthalmology senior
residents. On the independent EyePACS-1 and Messidor-2 datasets, the model's
area under the receiver operating characteristic curve for referable diabetic
retinopathy was 0.991 and 0.990, respectively ([1]). Esteva and colleagues
trained a network on 129,450 clinical images spanning 2,032 diseases and
compared image-based classification with 21 board-certified dermatologists on
selected skin-lesion tasks ([2]). These studies support a narrow claim:
well-trained systems can equal specialist discrimination on specified image
tasks under controlled evaluation. They do not by themselves establish better
patient outcomes or reliable performance in every site and population.

Regulation then reached autonomous diagnosis. On April 11, 2018, the FDA
granted De Novo authorization to IDx-DR for
automatic detection of more-than-mild diabetic retinopathy in specified adults
with diabetes. The pivotal study prospectively enrolled 900 participants at
10 primary-care sites, and the FDA described the device as the first
authorized autonomous AI diagnostic system in medicine ([3] [4]). Its scope
was constrained by intended population, camera, image-quality, and referral
rules rather than being an open-ended diagnostic system.

The regulated market expanded rapidly. A direct count of unique submission
identifiers in the FDA list current September 4, 2026 yields 1,614 AI-enabled
devices authorized for US marketing. The FDA warns that the list is not
comprehensive and is updated as relevant authorization documents are
identified ([5]). In a separate 2025 analysis of
903 devices listed through August 2024, 692 (76.6 percent) were in radiology
and 877 (97.1 percent) used the 510(k) pathway ([13]). These dated cohorts
should not be mixed with the current FDA total: they describe the composition
of earlier snapshots, not the September 2026 denominator.

Language models extended medical AI from perception to question answering and
text generation. A 2023 study reported that ChatGPT reached or approached the
passing threshold across three USMLE steps without specialized medical
training, but it excluded questions containing images and tested exam-style
items rather than patient care ([12]). Med-PaLM 2 later scored up to 86.5
percent on the MedQA benchmark and was preferred to physician answers on eight
of nine evaluated axes in a pairwise study of consumer questions; its authors
still called for real-world validation, and specialist answers remained
preferred overall in a pilot of real clinical questions ([11]). Benchmark
success therefore demonstrates a capability, not a clinical indication.

The central evidence gap is measurable. A 2025 systematic review examined 950
FDA-authorized AI or machine-learning devices through June 2024, including 723
radiology devices. Among 717 radiology devices with submission documentation,
33 (5 percent) underwent prospective testing, 56 (8 percent) included a human
operator, and 208 (29 percent) incorporated clinical testing ([14]). The
problem is no longer whether an algorithm can produce a high score on a
curated dataset; it is whether the device, users, workflow, and monitoring
system together improve care in the population where they are deployed.

## Core Concepts

### Convolutional Neural Networks and Supervised Learning

Most image-classification systems discussed in this topic use supervised
deep learning. A convolutional neural network learns a hierarchy of numerical
representations from labeled examples: earlier layers respond to local image
patterns, while later layers combine them into features useful for the target
classification. Training adjusts model parameters to reduce error against the
provided labels; validation guides development; and a held-out test set
estimates performance after development decisions are complete
([1] [2] [16]). The labels are part of the measurement system, not unquestionable
truth. In the Gulshan study, 128,175 retinal images were graded three to seven
times by a panel of 54 ophthalmologists and ophthalmology senior residents,
and the majority decision of expert graders defined the reference standard
([1]). A model learns the relationship between images and that operational
standard.

Separation among development, validation, and test data prevents direct
reuse of examples, but it does not by itself establish generalizability. Data
from one institution may share scanner settings, acquisition protocols,
patient mix, disease prevalence, and documentation practices. Random splitting
within that pool can leave all three sets with the same site-specific
correlations. External validation instead evaluates a fixed model on data
from a different source. Liu and colleagues found external validation in only
25 of 82 eligible studies and direct model-clinician comparison on the same
external sample in only 14 ([6]). Yu and colleagues later reviewed 83
external-validation articles covering 86 algorithms; 70 algorithms (81
percent) performed worse externally than on development data, and 21 (24
percent) declined by at least 0.10 on the reported unit scale ([18]). External
validation does not guarantee safe deployment, but its absence leaves transfer
to a new setting untested.

### Metrics, Thresholds, and the Clinical Denominator

Diagnostic performance cannot be summarized by one accuracy number.
Sensitivity measures the proportion of reference-positive cases detected,
whereas specificity measures the proportion of reference-negative cases
correctly rejected. A receiver operating characteristic curve shows the
trade-off between those quantities as the decision threshold changes, and its
area summarizes discrimination across thresholds. Clinical use occurs at a
particular threshold, however, so the relevant sensitivity and specificity
must be reported at that operating point ([1] [3] [6]).

Prevalence and workflow determine what follows a positive result. The same
sensitivity and specificity can yield different positive predictive values in
a referral clinic and a low-prevalence screening population. The pivotal
IDx-DR evidence therefore reported sensitivity, specificity, positive and
negative predictive values, and imageability in the intended primary-care
population rather than only an area under a curve ([3]). Imageability matters
because a system that cannot produce an output for difficult images can appear
accurate among the cases it accepts while transferring unresolved cases to the
human workflow. Evaluation must report how failures, indeterminate outputs,
and exclusions enter the denominator.

Calibration answers another question: whether predicted probabilities match
observed frequencies in the deployment population. A model may discriminate
well yet be poorly calibrated after prevalence, equipment, or practice
changes. Threshold selection then becomes a clinical policy decision about
the relative consequences of missed disease, false alarms, delay, and
follow-up capacity. The author's synthesis is that procurement should require
the complete operating point and denominator -- not a headline area under the
curve -- because resource use and patient consequences arise from the chosen
threshold in a defined population ([1] [3] [7]).

### Autonomous, Assistive, and Decision-Support Use

Deployment configuration determines who sees the primary data and who acts on
the output. Autonomous AI returns a clinical result without a specialist
interpreting the source image. IDx-DR is the reference case: the authorized
use covers adults aged 22 years or older who have diabetes and no previous
diabetic-retinopathy diagnosis, using specified retinal imaging and referral
rules ([3] [4]). The narrow indication, image-quality control, and defined
next action are parts of the system's safety case.

Assistive systems mark, prioritize, segment, or provide a second read while a
clinician remains responsible for interpretation. Clinical decision support
uses images, structured data, or text to generate risk estimates, alerts,
summaries, or recommendations. These categories can overlap technically, but
their evidence questions differ. A stand-alone classifier asks whether model
outputs agree with a reference standard. An assistive system asks whether
clinicians using it outperform clinicians without it and whether new errors or
delays appear. In image-based cancer diagnosis, Xue and colleagues found pooled
sensitivity of 88 percent for assisted clinicians versus 83 percent for
unassisted clinicians and pooled specificity of 88 percent versus 86 percent,
while noting that 47 of 48 included studies were retrospective ([8]). The
result supports evaluation of the human-machine pair; it does not prove that
every assistive product improves every workflow.

### Regulatory Pathways and Lifecycle Change

"FDA authorized" is more precise than treating every device as
"FDA approved." The 510(k) pathway generally compares a device with a legally
marketed predicate to establish substantial equivalence; clinical data may be
required when necessary, but they are not compulsory for every 510(k)
submission ([22]). De Novo classification covers novel low- or moderate-risk
device types without a suitable predicate, while Premarket Approval is the
path for specified high-risk devices. In the 2025 radiology review's cohort of
950 AI or machine-learning devices authorized through June 2024, 924 (97
percent) used 510(k), 22 used De Novo, and four used Premarket Approval
([14]). These figures describe that cohort and date, not a permanent ratio for
all future devices.

Authorization establishes that a device met the applicable premarket
requirements for its intended use; it does not itself show that purchasing the
device will improve patient outcomes in a particular health system ([5] [14]).
That distinction becomes important when software changes after authorization.
The FDA's current PCCP guidance allows a manufacturer to propose a
Predetermined Change Control Plan describing planned modifications, the
methods for developing, validating, and implementing them, and an assessment
of their effects. FDA can review that plan within the marketing submission so
covered changes can be implemented without a separate submission for each
modification ([21]). A PCCP is a lifecycle control, not permission for
unbounded adaptation.

### Generalizability, Dataset Shift, and Monitoring

Dataset shift occurs when the relationships seen during development differ
from those at use. New scanner vendors, acquisition protocols, disease
prevalence, referral patterns, patient characteristics, or documentation
practices can alter inputs and outcomes. The direction and size of change
cannot be inferred from the original benchmark. Yu and colleagues' finding
that 81 percent of externally evaluated radiology algorithms declined on the
external dataset demonstrates why transfer must be measured rather than
assumed ([18]).

Public regulatory documentation also leaves important uncertainty. Windecker
and colleagues analyzed 903 FDA-listed devices through August 2024. Clinical
performance studies were reported for 505 (55.9 percent), 218 (24.1 percent)
explicitly reported no performance studies, and information was missing for
180 (19.9 percent). Among the 505 devices with reported studies, 41 were
prospective and 12 randomized; sex-specific results were available for 145 and
age-specific results for 117 ([13]). A separate radiology review found
prospective testing in 33 of 717 devices with submission documentation and
human-in-the-loop testing in 56 ([14]). These studies assessed public records,
so incomplete summaries can understate submitted evidence; they nevertheless
show what clinicians and purchasers could verify publicly ([5] [13] [14]).

Monitoring is therefore part of the clinical intervention. Inputs, output
rates, indeterminate cases, sensitivity and specificity where outcomes become
available, subgroup performance, overrides, delays, incidents, and use outside
the authorized scope can all change after launch. Ren and colleagues studied
the same 903-device cohort and found 43 recalls by August 2024. Devices with
missing public information about clinical studies had a higher estimated
recall hazard than devices with reported studies, although the 95 percent
credible interval for that estimate included no difference; use-related
problems also showed an elevated estimated hazard ([20]). The cautious lesson
is not that missing documentation causes recall, but that postmarket evidence
and human use belong in the safety model.

### Algorithmic Bias and Proxy Labels

Bias can enter through sampling, measurement, labels, objectives, thresholds,
and access to care. Obermeyer and colleagues examined a commercial population
health algorithm that used predicted healthcare cost as a proxy for health
need. Because less money was spent on Black patients than on White patients at
the same level of illness, the proxy understated need among Black patients.
Replacing the proxy would have increased the share of Black patients selected
for additional care from 17.7 percent to 46.5 percent ([9]). The model could
predict its chosen target and still fail the clinical purpose.

This example separates model error from target error. Better optimization
cannot repair a label that measures spending when the intended concept is
illness. Representation also matters: average performance can conceal failure
in a smaller subgroup, and a threshold calibrated for one population can
allocate different false-positive and false-negative burdens in another.
Safe deployment therefore requires subgroup-specific reporting, examination
of what each label measures, and access analysis across the full path from
prediction to treatment ([9] [13]). Fairness is not an extra metric attached
after accuracy; it begins with the definition of the clinical task.

### Large Language Models in Medicine

Language models broaden the input and output space. Med-PaLM was the first
model reported to exceed the passing threshold on MedQA, and Med-PaLM 2 later
reached 86.5 percent. In pairwise evaluation of 1,066 consumer medical
questions, physicians preferred Med-PaLM 2 answers to physician-written
answers on eight of nine evaluated dimensions, while the study's real-world
pilot found specialists preferred Med-PaLM 2 answers to generalist answers 65
percent of the time but still preferred specialist answers overall
([10] [11]). A separate study found that ChatGPT reached or approached passing
performance on text-only USMLE questions without medical fine-tuning ([12]).

These benchmarks test knowledge retrieval, question answering, and generated
explanations under specified conditions. They do not measure longitudinal
care, physical examination, source verification, changing patient state, or
accountability for action. The Med-PaLM studies explicitly used physician
human evaluation because multiple-choice accuracy and automated text metrics
were insufficient for long-form medical answers ([10] [11]). Plausible
language can contain unsupported or incorrect content, and a citation can be
irrelevant even when formatted correctly. Clinical use therefore requires
grounded source retrieval, verification of the cited passage, uncertainty
handling, and a defined human review process rather than trust based on
fluency.

### Clinical Integration and Human Factors

A device enters an existing sociotechnical system: orders, interfaces,
worklists, staffing, escalation rules, reimbursement, documentation, and
professional accountability. Automation bias is the tendency to over-rely on
automation. A systematic review found that workload, time pressure, trust, and
task complexity can mediate it, while training, explicit accountability,
confidence information, and interface design can mitigate it ([19]). An
accurate model can still reduce net performance if users defer to a wrong
output, spend time resolving excessive alerts, or lose the independent skill
needed to detect failure.

Local implementation must test the complete workflow. The author's synthesis
from the external-validation, regulatory, and human-factors evidence is to run
a fixed system silently on representative local cases before activation;
measure its intended operating point and indeterminate rate; define who sees,
confirms, overrides, and escalates each result; monitor input and output drift;
retain model and data version information; and establish thresholds for pause,
rollback, or withdrawal ([13] [14] [18] [19] [20]). These controls do not
substitute for evidence that the device improves care. They prevent a
validated model from becoming an unmeasured intervention after its connection
to the clinical system changes.

## Evidence

The evidence base answers different questions at different levels. Retrospective
benchmarks test discrimination on fixed datasets; prospective pivotal studies
test a frozen system in an intended workflow; reader studies test the
human-machine pair; regulatory-document reviews describe what evidence was
publicly reported across devices; and postmarket studies examine failures after
authorization. Combining those levels without preserving their denominators
creates false confidence.

### Retrospective Benchmarks Established Narrow Technical Capability

Gulshan and colleagues developed a diabetic-retinopathy classifier with
128,175 retinal photographs and evaluated it on two independent datasets. The
EyePACS-1 set contained 9,963 images and the Messidor-2 set 1,748. For referable
diabetic retinopathy, the areas under the receiver operating characteristic
curve were 0.991 and 0.990. At the high-specificity operating point,
sensitivity was 90.3 percent and specificity 98.1 percent on EyePACS-1;
sensitivity was 87.0 percent and specificity 98.5 percent on Messidor-2. At
the high-sensitivity point, sensitivity was 97.5 and 96.1 percent while
specificity was 93.4 and 93.9 percent, respectively ([1]). The two operating
points show why a model does not have one context-free accuracy: the threshold
changes the balance of missed disease and false referral.

Esteva and colleagues used 129,450 clinical images representing 2,032 diseases
to train one convolutional neural network. They compared it with 21
board-certified dermatologists on biopsy-proven images for selected binary
classification tasks involving keratinocyte carcinoma and melanoma, including
dermoscopic images. The model performed on par with the tested dermatologists
on those image-only tasks ([2]). The method was retrospective and did not test
history taking, physical examination, biopsy decisions, treatment, or patient
outcomes. Its contribution was proof that learned visual features could reach
specialist-level discrimination under a bounded comparison.

### A Prospective Pivotal Study Tested Autonomous Use

The IDx-DR pivotal study prospectively enrolled 900 adults with diabetes and no
known diabetic retinopathy at 10 US primary-care sites. Non-specialist
operators acquired retinal images, the autonomous system returned a result,
and an independent reading center used stereoscopic photography and optical
coherence tomography to define the reference standard. Enrichment-corrected
sensitivity for more-than-mild diabetic retinopathy was 87.2 percent against a
prespecified 85 percent performance threshold; specificity was 90.7 percent
against an 82.5 percent threshold; and imageability was 96.1 percent ([3]).
The FDA's De Novo authorization followed this study and constrained use to the
evaluated indication and population ([4]).

This study is stronger than a retrospective benchmark because it measured an
autonomous workflow prospectively across multiple primary-care sites. It
still answers a bounded question: whether this system, camera protocol,
operator training, and referral output met specified diagnostic endpoints. It
does not show that every autonomous diagnostic system transfers to a new task,
or that authorization alone establishes long-term outcome benefit.

### Systematic Reviews Qualified Human-Comparison Claims

Liu and colleagues searched four major literature databases for medical-image
deep-learning studies and included 82 studies describing 147 patient cohorts.
Only 25 used out-of-sample external validation, and only 14 compared models
with healthcare professionals on the same external sample. In those 14,
pooled sensitivity was 87.0 percent for deep-learning models and 86.4 percent
for professionals; pooled specificity was 92.5 and 90.5 percent,
respectively. The authors interpreted the performance as equivalent and
emphasized poor reporting and the scarcity of direct, external comparison
([6]). These figures correct stronger claims that the review found pooled
sensitivities above 90 percent or established machine superiority.

Aggarwal and colleagues screened 11,921 records and included 503 studies in a
systematic review of diagnostic medical imaging; 279 studies entered the
meta-analysis. Reported performance was
high, but heterogeneity in methods, terminology, outcomes, and reporting was
also high. Prospective data and external validation were uncommon in the
ophthalmology, respiratory, and breast-imaging groups, and none of those
reported studies provided a prespecified sample-size calculation ([7]). The
review concluded that this variation can overestimate diagnostic performance
and called for AI-specific reporting guidance. It supports caution about the
literature as a body rather than a claim that one pooled number transfers to
clinical practice.

Yu and colleagues asked a more direct generalizability question. Their
systematic review identified 83 articles reporting 86 radiology algorithms
that had both development and external performance measurements. Seventy
algorithms (81 percent) performed worse on external data, 42 (49 percent)
declined by at least 0.05 on the reported unit scale, and 21 (24 percent)
declined by at least 0.10 ([18]). These were studies that had performed
external validation; the review therefore does not estimate how all published
algorithms would transfer. It demonstrates that performance loss is common
even among the subset for which transfer was tested.

### Human-Machine Studies Tested Assistance Rather Than Replacement

Xue and colleagues reviewed 48 studies comparing unassisted clinicians with
deep-learning-assisted clinicians in image-based cancer diagnosis; 25 supplied
sufficient binary data for meta-analysis. Pooled sensitivity increased from 83
percent without assistance to 88 percent with assistance, and pooled
specificity increased from 86 to 88 percent. The pooled relative sensitivity
and specificity were 1.07 and 1.03, respectively ([8]). However, 47 of 48
included studies used retrospectively collected data, only one was prospective,
and only four reported a prespecified sample-size calculation ([8]). The
result supports further prospective evaluation of assistance; it does not
justify a universal assertion that adding AI always improves clinicians.

### Regulatory Reviews Measured the Validation Gap

Sivakumar and colleagues reviewed FDA premarket authorizations from November
1995 through June 2024. Their cohort contained 950 AI or machine-learning
devices, of which 723 (76 percent) were radiology devices. Among 717 radiology
devices with submission documentation, 33 (5 percent) underwent prospective
testing, 56 (8 percent) included a human operator, and 208 (29 percent)
incorporated clinical testing. Fifteen combined prospective and clinical
testing, and six included prospective, clinical, and human-in-the-loop testing
([14]). The review evaluated public summaries, which varied in completeness;
it measured publicly documented testing, not every item a sponsor may have
submitted confidentially.

Windecker and colleagues examined a separate FDA list snapshot through August
2024. Among 903 devices, public information reported clinical performance
studies for 505 (55.9 percent), explicitly reported none for 218 (24.1
percent), and was missing for 180 (19.9 percent). Of the 505 devices with
reported studies, 193 were retrospective, 41 prospective nonrandomized, and 12
randomized; study design was missing for 259. Sex-specific data were available
for 145 and age-specific data for 117 ([13]). The two reviews used different
questions and denominators, but both found that prospective, human-workflow,
and subgroup evidence was limited in public documentation.

### Postmarket Evidence Revealed Target and Use Failures

Obermeyer and colleagues supplied a mechanism-level case rather than a device
count. They showed that a commercial risk algorithm affecting millions of
patients assigned lower risk to Black patients who were sicker than White
patients at the same score because the system predicted cost rather than
illness. Correcting the target would have increased the share of Black
patients selected for additional care from 17.7 to 46.5 percent ([9]). The
failure was not merely insufficient discrimination; the proxy encoded unequal
access and spending.

Ren and colleagues linked regulatory and postmarket data for 903 authorized
devices through August 2024. Forty-three devices (4.8 percent) had been
recalled after a median 458 days. Devices with missing public information
about clinical studies had an estimated recall hazard ratio of 1.39 compared
with devices with reported studies, but the 95 percent credible interval of
0.84 to 3.52 included no difference. Incorrect use was also associated with a
higher estimated hazard, with substantial uncertainty ([20]). The study does
not prove that more clinical studies prevent recalls. It adds evidence that
public documentation, user interaction, and postmarket surveillance are part
of the clinical safety problem.

Across these studies, the stable conclusion is narrower than either optimism
or rejection. Deep learning can match specialists on specified retrospective
image tasks; one autonomous retinal system met prospective diagnostic
endpoints in a defined primary-care workflow; assisted clinicians improved on
average in a largely retrospective cancer-imaging literature; external
performance commonly declined; and public regulatory records often lacked
prospective, human-in-the-loop, randomized, or subgroup evidence. The author's
synthesis is that the principal bottleneck is no longer demonstration of
technical discrimination. It is evidence that a defined human-machine system
improves care, remains reliable across settings and groups, and is monitored
after deployment.

## Implications

### Clinicians and Clinical Teams

The first implication for clinicians is that the unit of judgment is an
intended use, not "AI" in general. IDx-DR was evaluated for a specified adult
population, image-acquisition process, reference standard, operating point,
and referral action ([3] [4]). The Esteva and Gulshan studies answered
different, image-classification questions ([1] [2]). A clinician evaluating a
tool should therefore ask whether the current patient, device input, and
decision fall inside the population and workflow actually studied. A high
score from another disease, scanner, institution, or output type does not
transfer by analogy.

Assistance should be evaluated as a new team configuration. The Xue
meta-analysis found higher pooled sensitivity and specificity for assisted
clinicians, but nearly all included studies were retrospective ([8]). This
supports prospective testing of an assisted workflow rather than assuming
that a model's stand-alone accuracy will add to a clinician's accuracy. The
tool can change attention, ordering, confidence, and time allocation. It can
also create commission errors when a clinician follows an incorrect output or
omission errors when an unflagged case receives less scrutiny. Workload,
trust, time pressure, interface design, and explicit accountability influence
automation bias ([19]). The author's synthesis is that useful oversight
requires protected independence: clinicians need enough information and skill
to disagree with the model, and the workflow must make overrides observable
rather than treating them as friction.

Clinical training should add three competencies. First, clinicians need to
read validation evidence: cohort selection, reference standard, exclusions,
operating threshold, uncertainty, and subgroup results. Second, they need to
recognize shift: changes in disease prevalence, scanner protocols, patient
mix, and care pathways that can invalidate calibration or threshold choices
([18]). Third, they need to distinguish generated language from verified
evidence. Medical-language-model benchmarks show knowledge and communication
capability under controlled evaluation, while their authors still call for
real-world validation and physician assessment of long-form answers
([10] [11] [12]). Fluency is an interface property, not proof of correctness.

### Health Systems and Procurement

FDA authorization is a necessary regulatory fact for regulated devices, but
it is not a health-system effectiveness study. The FDA list records devices
that met applicable premarket requirements, and 510(k) clearance rests on a
comparative substantial-equivalence determination that may use nonclinical or
clinical data as appropriate ([5] [22]). The public evidence reviews found
that prospective, human-in-the-loop, randomized, and subgroup testing were
limited in their dated cohorts ([13] [14]). Procurement should therefore
separate four questions: may the device be marketed, does it perform on an
external population, does the human-machine workflow improve care, and does
that improvement justify its total cost and harms.

A procurement evidence packet should identify the exact model and software
version; authorized indication; training and validation sites; study design;
external and prospective cohorts; comparator; reference standard; threshold;
sensitivity, specificity, predictive values, calibration, and indeterminate
rate; subgroup results; human-factors evaluation; and adverse-event or recall
history. Missing information is itself a procurement finding, not a value to
fill with a vendor claim. Public authorization summaries are not complete
records of everything submitted to FDA, but they define what an outside
evaluator can verify without confidential access ([5] [13] [14]).

Local evaluation should preserve the intended threshold and assess
representative scanners, sites, populations, and workloads before activation.
During a silent phase, teams can measure output rates, indeterminate cases,
processing failures, latency, disagreement with clinicians, and subgroup
differences without allowing the system to direct care. A prospective rollout
can then compare the complete workflow against current practice, including
time to action, false-positive work, missed cases, and downstream utilization.
The author's synthesis is that these endpoints should be chosen before launch
to prevent a faster worklist or a higher detection count from being mistaken
automatically for patient benefit.

Contracts should make lifecycle evidence possible. Health systems need notice
of model, threshold, data-pipeline, and user-interface changes; access to
version history and incident information; rights to audit subgroup and local
performance; and a reversible exit plan. An authorized PCCP can cover specified
future modifications and their validation protocol, but it does not make every
future change equivalent or safe ([21]). A deployer still needs to know which
version produced each result and whether local performance remained within
predefined limits.

### Patients, Screening Programs, and Public Health

Autonomous retinal diagnosis illustrates both access value and system
dependence. Non-specialist operators acquired images at primary-care sites,
and the device produced a referral result without an eye specialist reading
the image ([3] [4]). This can move case finding closer to patients. It also
moves the bottleneck: a positive result has value only if confirmatory care,
treatment, and follow-up are accessible. A program that increases detection
without expanding referral capacity can increase delay, anxiety, and unequal
access to the next step. The author's synthesis is that screening AI must be
evaluated as the whole pathway from invitation and image acquisition through
diagnosis and treatment, consistent with the broader logic in
`library/health-medicine/preventive-screening-and-overdiagnosis.md`.

Thresholds distribute benefits and burdens. Higher sensitivity can reduce
missed disease while increasing false referrals; higher specificity can reduce
unnecessary follow-up while missing more cases ([1] [3]). Prevalence changes
predictive value, so a result observed in a referral cohort cannot be assumed
for population screening. Patients should be told whether the system is
autonomous or assistive, what result it produces, who reviews it, what happens
when no result is returned, and who remains responsible for follow-up. Those
disclosures are practical components of consent rather than abstract demands
for explainability.

Equity assessment must include the target and the pathway. The Obermeyer case
showed how a cost proxy reproduced unequal spending even when the algorithm
predicted that proxy successfully ([9]). Windecker and colleagues found that
public age- and sex-specific results were absent for most devices with
reported clinical studies in their 2024 cohort ([13]). A subgroup audit should
therefore ask who entered the dataset, how labels were produced, whether error
rates and indeterminate outputs differ, and whether patients receive the same
follow-up after an alert. This connects technical validation to the governance
questions developed in `library/ethics-philosophy/ai-ethics.md`.

### Researchers, Manufacturers, and Regulators

Research design should match the claim. A stand-alone accuracy claim requires
an independent test set and a defensible reference standard. A transfer claim
requires external sites and populations. A workflow claim requires the
intended users, interface, comparator, and process outcomes. A patient-benefit
claim requires prospective evidence that follows management and outcomes.
The external-validation review and regulatory reviews show that these are not
interchangeable levels of evidence ([13] [14] [18]). Prespecified protocols,
sample-size calculations, complete denominators, and reporting of failures and
subgroups reduce the flexibility that can make retrospective results appear
more certain than they are ([6] [7] [8]).

Manufacturers should treat monitoring as part of product design. A useful
monitoring plan specifies inputs and outputs to track, ground-truth delay,
subgroup analysis, expected rates, alert thresholds, investigation ownership,
and rollback criteria. The recall study associated use-related problems with
an elevated estimated hazard, although its estimates were uncertain ([20]).
That finding makes human factors and misuse foreseeable product risks, not
implementation details that begin after sale.

Regulators face a transparency problem in addition to an authorization
problem. The FDA explains that its device list is not comprehensive and that
public summaries omit much of the information submitted in an application
([5]). The author's synthesis is that standardized public reporting of study
design, sites, demographics, operating points, indeterminate results,
human-in-the-loop evaluation, and authorized PCCPs would let clinicians,
patients, and purchasers compare evidence without implying that every device
requires the same trial. Postmarket reporting must then connect failures to
the exact model and version.

Across audiences, the governing question is simple: what changed in care
because this defined system was used? Technical discrimination is necessary,
but clinical value depends on the threshold, population, user, workflow,
follow-up capacity, and lifecycle controls. The evidence supports neither a
general promise of replacement nor a general rejection of medical AI. It
supports bounded claims, prospective measurement, and reversible deployment.

## Common Pitfalls

Confusing authorization with validation is the most expensive error in the
field. A 510(k) determination compares a device with a predicate and may use
clinical data when necessary, but it does not imply a prospective effectiveness
trial in the buyer's workflow ([14] [22]).

Reporting only area under the curve on balanced test sets overstates
real-world value. The operating-point sensitivity and specificity, disease
prevalence, indeterminate outputs, and follow-up consequences determine what a
screening or diagnostic program actually does ([1] [3] [7]).

Skipping external validation is the research-side version of the same
failure. A random split can preserve site-specific correlations across all
sets, and 81 percent of algorithms in one external-validation review performed
worse on external data ([6] [18]).

Proxy-label blindness produces biased systems that are technically
"accurate" by their own metrics. The cost-proxy algorithm in the Obermeyer
study was well calibrated to its target; its target was wrong ([9]).

Treating human review as a universal safety net ignores automation bias.
Incorrect automated advice can change decisions, and workload, trust, time
pressure, and interface design affect the risk ([19]). The human-machine pair
must be tested, not inferred from separate model and clinician scores ([8]).

Treating LLM fluency as clinical reliability is the newest pitfall.
USMLE-style and consumer-question benchmarks measure bounded question
answering, not longitudinal patient management or source verification
([10] [11] [12]). Every generated clinical claim still requires passage-level
verification and accountable human review.

Ignoring indeterminate cases creates a hidden denominator. Reporting
performance only for cases on which a system returned an answer can conceal
work transferred to clinicians or failures concentrated in a subgroup. The
IDx-DR trial reported imageability alongside sensitivity and specificity,
making this denominator visible ([3]).

Allowing an untracked software update breaks the evidence chain. A PCCP covers
only specified modifications and methods reviewed with the authorization; it
does not eliminate the need for version control, local monitoring, or rollback
criteria ([21]).

## Sources

1. Gulshan, V. et al. (2016). "Development and Validation of a Deep
   Learning Algorithm for Detection of Diabetic Retinopathy in Retinal Fundus
   Photographs." JAMA, 316(22), 2402-2410.
   https://jamanetwork.com/journals/jama/fullarticle/2588763 [high]

2. Esteva, A. et al. (2017). "Dermatologist-level classification of skin
   cancer with deep neural networks." Nature, 542, 115-118.
   https://www.nature.com/articles/nature21056 [high]

3. Abramoff, M. D. et al. (2018). "Pivotal trial of an autonomous AI-based
   diagnostic system for detection of diabetic retinopathy in primary care
   offices." npj Digital Medicine, 1, 39.
   https://www.nature.com/articles/s41746-018-0040-6 [high]

4. US Food and Drug Administration (2018). "FDA permits marketing of
   artificial intelligence-based device to detect certain diabetes-related eye
   problems." April 11, 2018.
   https://www.fda.gov/news-events/press-announcements/fda-permits-marketing-artificial-intelligence-based-device-detect-certain-diabetes-related-eye
   [high]

5. US Food and Drug Administration (2026). "Artificial
   Intelligence-Enabled Medical Devices." Authorized-device list and scope
   notes; content current September 4, 2026.
   https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices
   [high]

6. Liu, X. et al. (2019). "A comparison of deep learning performance against
   health-care professionals in detecting diseases from medical imaging: a
   systematic review and meta-analysis." The Lancet Digital Health, 1(6),
   e271-e297.
   https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30123-2/fulltext
   [high]

7. Aggarwal, R. et al. (2021). "Diagnostic accuracy of deep learning in
   medical imaging: a systematic review and meta-analysis." npj Digital
   Medicine, 4, 65. https://www.nature.com/articles/s41746-021-00438-z [high]

8. Xue, P. et al. (2023). "Unassisted Clinicians Versus Deep
   Learning-Assisted Clinicians in Image-Based Cancer Diagnostics: Systematic
   Review With Meta-analysis." Journal of Medical Internet Research, 25,
   e43832. https://www.jmir.org/2023/1/e43832 [high]

9. Obermeyer, Z., Powers, B., Vogeli, C. & Mullainathan, S. (2019).
   "Dissecting racial bias in an algorithm used to manage the health of
   populations." Science, 366(6464), 447-453.
   https://www.science.org/doi/10.1126/science.aax2342 [high]

10. Singhal, K. et al. (2023). "Large language models encode clinical
    knowledge." Nature, 620, 172-180.
    https://www.nature.com/articles/s41586-023-06291-2 [high]

11. Singhal, K. et al. (2025). "Toward expert-level medical question
    answering with large language models." Nature Medicine, 31, 943-950.
    https://www.nature.com/articles/s41591-024-03423-7 [high]

12. Kung, T. H. et al. (2023). "Performance of ChatGPT on USMLE: Potential
    for AI-assisted medical education using large language models." PLOS
    Digital Health, 2(2), e0000198.
    https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000198
    [high]

13. Windecker, D. et al. (2025). "Generalizability of FDA-Approved
    AI-Enabled Medical Devices for Clinical Use." JAMA Network Open, 8(4),
    e258052. https://doi.org/10.1001/jamanetworkopen.2025.8052 [high]

14. Sivakumar, R., Lue, B. & Kundu, S. (2025). "FDA Approval of Artificial
    Intelligence and Machine Learning Devices in Radiology: A Systematic
    Review." JAMA Network Open, 8(11), e2542338.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC12595527/ [high]

15. Topol, E. J. (2019). "High-performance medicine: the convergence of
    human and artificial intelligence." Nature Medicine, 25, 44-56.
    https://www.nature.com/articles/s41591-018-0300-7 [high]

16. Krizhevsky, A., Sutskever, I. & Hinton, G. E. (2012). "ImageNet
    Classification with Deep Convolutional Neural Networks." Advances in
    Neural Information Processing Systems, 25.
    https://papers.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
    [high]

17. Shortliffe, E. H. (1974). "MYCIN: A Rule-Based Computer Program for
    Advising Physicians Regarding Antimicrobial Therapy Selection." Stanford
    University doctoral dissertation, report STAN-CS-74-465.
    https://apps.dtic.mil/sti/citations/ADA001373 [high]

18. Yu, A. C., Mohajer, B. & Eng, J. (2022). "External Validation of Deep
    Learning Algorithms for Radiologic Diagnosis: A Systematic Review."
    Radiology: Artificial Intelligence, 4(3), e210064.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC9152694/ [high]

19. Goddard, K., Roudsari, A. & Wyatt, J. C. (2012). "Automation bias: a
    systematic review of frequency, effect mediators, and mitigators."
    Journal of the American Medical Informatics Association, 19(1), 121-127.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/ [high]

20. Ren, Y. et al. (2026). "Clinical Evidence and FDA Recalls of Artificial
    Intelligence-Enabled Medical Devices." JAMA Network Open, 9(6), e2617920.
    https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2850190 [high]

21. US Food and Drug Administration (2025). "Marketing Submission
    Recommendations for a Predetermined Change Control Plan for Artificial
    Intelligence-Enabled Device Software Functions." Guidance for industry
    and FDA staff.
    https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence
    [high]

22. US Food and Drug Administration (2024). "Premarket Notification 510(k)."
    https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k
    [high]

23. Nightingale, S. L. (1998). "New Mammography Screening Aid Approved."
    JAMA, 280(5), 410.
    https://jamanetwork.com/journals/jama/fullarticle/187810 [high]

## See Also

- `library/technology/large-language-models.md` -- foundation models and the
  capabilities that medical-language-model evaluations adapt.
- `library/health-medicine/preventive-screening-and-overdiagnosis.md` -- the
  downstream benefits and harms that apply when AI changes a screening program.
- `library/ethics-philosophy/ai-ethics.md` -- fairness, accountability,
  transparency, and governance for algorithmic systems.
- `library/health-medicine/drug-development-from-molecule-to-medicine.md` -- a
  separate medical application of machine learning with related validation
  requirements.
- `library/health-medicine/public-health-epidemiology.md` -- population-level
  evaluation of screening access, prevalence, and case finding.
- `library/health-medicine/chronic-disease-cvd-diabetes.md` -- diabetes care
  surrounding the autonomous diabetic-retinopathy use case.

