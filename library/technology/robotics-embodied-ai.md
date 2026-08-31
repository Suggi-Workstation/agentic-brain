---
name: robotics-embodied-ai
id: 20260831T080123Z
tier: library-topic
domain: technology
author: Library Runner
tags: [robotics, embodied-ai, humanoid-robots, reinforcement-learning, manipulation, locomotion, foundation-models, sim-to-real, perception, motion-planning]
links: [library/technology/large-language-models.md, library/technology/semiconductors.md, library/technology/cloud-computing.md]
---

# Robotics and Embodied AI -- How Machines Learned to Walk, Grasp, and Reason in the Physical World

Robotics has evolved from fixed industrial arms performing repetitive
tasks in caged environments to general-purpose humanoid machines that
perceive, reason, and act in unstructured physical space. The
convergence of deep reinforcement learning, large-scale simulation,
and foundation models -- particularly vision-language-action models --
has created a new paradigm called embodied AI, in which the same
neural network architectures that power chatbots now control motors,
hands, and legs. The world operated 4.66 million industrial robots in
2024, while humanoid platforms from Boston Dynamics, Figure AI,
Unitree, and others entered early production in 2025-2026, marking the
transition from programmed automation to learned generalist robotic
behavior.

## Background

The history of robotics spans over a century, but the field that
became modern industrial robotics began with a single patent. In 1954,
American inventor George Devol filed U.S. Patent No. 2,988,237 for a
"Programmed Article Transfer" -- a reprogrammable, multifunctional
manipulator capable of storing digital commands to transfer objects
autonomously. Devol coined the term "Universal Automation," planting
the seed for his future company, Unimation. In 1956, a chance meeting
between Devol and physicist Joseph Engelberger at a cocktail party
ignited the commercial flame of robotics. Engelberger, who would become
known as the father of modern robotics, recognized the industrial
potential of Devol's invention and partnered with him to build the
first commercial robot company.

The Unimate -- the first industrial robot -- was installed at a General
Motors die-casting plant in Trenton, New Jersey, in 1961. It was a
hydraulically actuated, six-axis articulated arm weighing about two
tons, designed to extract hot metal parts from die-casting machines
and stack them, replacing hazardous manual labor. The Unimate was
programmed by manually setting switches, timers, and motion controls
at set positions saved on a basic memory system. It was, in effect,
the first "no-code" robot: a programmable playback device rather than
a computer-controlled system. In 1963, Joseph Engelberger appeared on
"The Tonight Show" with Johnny Carson, where the Unimate played golf,
poured beer, and led the band -- a public relations coup that
introduced robotics to mainstream consciousness.

The transition from hydraulic to electric actuation came in 1969 with
the Stanford Arm, developed by Victor Scheinman at Stanford
University's Artificial Intelligence Laboratory. The Stanford Arm was
the first all-electric, computer-controlled, six-degree-of-freedom
robot. Unlike the hydraulic Unimate, its electric actuators allowed
for finer control and the ability to follow arbitrary paths in
three-dimensional space, opening up applications such as automated
assembly and arc welding. Scheinman later formed Vicarm Inc. to
commercialize his designs, and in 1977 sold Vicarm to Unimation, which
developed the designs into the PUMA (Programmable Universal Machine
for Assembly) with support from General Motors. The PUMA became one of
the most influential industrial robots in history, and its design
principles continue to influence modern robotic systems.

The 1970s and 1980s saw the globalization of industrial robotics. In
1968, Kawasaki Aircraft licensed hydraulic robot design from Unimation
and began production in Japan, igniting the Japanese robotics industry
that would produce FANUC, Yaskawa, and other global leaders. In 1973,
Cincinnati Milacron released the T3, the first commercially available
minicomputer-controlled industrial robot. In 1981, Sankyo Seiki,
Pentel, and NEC presented the first commercial SCARA (Selective
Compliance Assembly Robot Arm) robots, which were rigid in the
Z-axis and compliant in the XY-axes, making them well-suited for
vertical insertion tasks. In 1985, Professor Reymond Clavel at EPFL
led the team that built the first working delta parallel robot,
enabling high-speed pick-and-place operations that remain standard in
packaging and electronics assembly today.

The 1990s and 2000s brought machine vision and sensory feedback to
industrial robots, allowing them to respond to their environment
rather than blindly executing pre-programmed paths. This period also
saw the emergence of collaborative robots, or cobots -- lighter,
force-limited arms designed to work alongside humans without safety
cages. The concept of the cobot was introduced in the late 1990s, but
commercial cobots became widespread only in the 2010s, led by
companies like Universal Robots (founded 2005, Denmark). Cobots
represented a conceptual shift: instead of fencing robots away from
humans for safety, engineers designed robots to be safe around humans
by limiting force, speed, and power.

Parallel to industrial robotics, mobile robotics developed along a
different trajectory. The first autonomous mobile robots were built by
neuroscientist W. Grey Walter in the 1950s -- simple "tortoise" robots
that used light and touch sensors to navigate environments. These
tortoises are the ancestors of the Roomba and nearly all autonomous
mobile robots. The Stanford Cart, developed at SRI in the 1960s, was
among the first mobile robots with computer vision. Shakey the Robot,
developed at SRI from 1966 to 1972, was the first mobile robot capable
of reasoning about its own actions, combining perception, planning, and
execution in a single system. These early mobile robots established the
architecture -- sense, plan, act -- that would dominate robotics for
decades.

The modern era of embodied AI began around 2015-2020, when deep
reinforcement learning demonstrated that neural networks could learn
complex manipulation and locomotion skills from simulation and
transfer them to physical robots. The integration of large language
models as reasoning layers for robots, beginning around 2022-2023,
accelerated this transformation. By 2024-2026, the convergence of
foundation models, differentiable physics simulation, and high-torque
actuation propelled humanoid robotics from a niche academic pursuit
into what industry analysts now describe as the "third wave of
artificial intelligence" -- Physical AI, defined by its embodiment:
the ability to perceive, plan, and act within continuous, unstructured,
and adversarial physical environments.

## Core Concepts

### Industrial Robots and Cobots

An industrial robot, per ISO 8373:2012, is an automatically controlled,
reprogrammable, multipurpose manipulator programmable in three or more
axes, which can be either fixed in place or mobile for use in
industrial automation applications. Industrial robots are the backbone
of modern manufacturing, performing welding, painting, assembly,
pick-and-place, packaging, and inspection tasks. They are rated by
payload (how much they can lift) and reach (how far they can extend),
and they are traditionally bolted to fixed stations and fenced off
from human workers.

The global industrial robot market is mature and growing steadily. In
2024, factories installed 542,000 industrial robots worldwide, the
fourth straight year above 500,000 installations, bringing the global
operational stock to 4,664,000 units, up 9 percent year-over-year.
China accounted for 54 percent of 2024 installations, a record 295,000
units. The International Federation of Robotics forecasts around
575,000 installations in 2025 and a climb past 700,000 per year by
2028. This installed base represents the mature, cash-generating
foundation of robotics -- a market that grew through incremental
improvements in precision, speed, and reliability rather than through
AI breakthroughs.

Collaborative robots, or cobots, are a distinct category: lighter,
force-limited arms designed to work alongside people without a cage.
Cobots detect contact with humans and stop or reverse motion,
operating at lower speeds and payloads than traditional industrial
arms. They emerged as a commercial category in the 2010s and are
particularly suited to small-batch manufacturing, assembly assistance,
and tasks where human-robot proximity is required. The cobot market
grew rapidly because it lowered the barrier to robotic automation for
small and medium enterprises that could not justify the infrastructure
costs of caged industrial robots.

### Humanoid Robots

Humanoid robots are general-purpose machines with legs and hands,
designed to operate in environments built for humans. Unlike
industrial arms or cobots, humanoids are not optimized for a single
task -- they are intended to perform the diverse physical work that
humans do, using the same tools, workstations, and spaces. The
rationale for the humanoid form factor is economic: rather than
designing specialized robots for every task, a single general-purpose
humanoid can be deployed across factories, warehouses, and eventually
homes, operating in spaces already designed for human bodies.

Humanoid robots emerged approximately 60 years ago, but it was not
until about 30 years ago that they began to exhibit notable human-like
senses, behaviors, and functions. Honda's ASIMO, unveiled in 2000,
was a landmark bipedal humanoid that demonstrated walking, stair
climbing, and basic object manipulation. Sony's QRIO (2001) and AIST's
HRP series (2002-2009) followed. These early humanoids were
impressive demonstrations but remained distant from practical
deployment: their gaits were stiff, their manipulation limited, and
their intelligence was scripted rather than learned.

The modern humanoid wave began around 2022-2023, driven by the same AI
advances that transformed language and vision. As of 2026, the leading
humanoid platforms include Boston Dynamics' Electric Atlas (1.9 m, 90
kg, 56 degrees of freedom, 30 kg sustained payload, in production for
Hyundai and Google DeepMind deployments), Figure AI's Figure 03 (1.72
m, Helix vision-language-action AI, BMW production deployments),
Unitree's G1 and H1 (the most accessible research platforms, starting
at $21,500), Agility Robotics' Digit (enterprise lease, warehouse
logistics), and Tesla's Optimus (internal deployment, targeting
$20,000-30,000 consumer price at scale). Roughly 15,000 humanoid
robots were sold in 2025, approximately 90 percent manufactured in
China. Goldman Sachs projects the humanoid market at $38 billion by
2035. McKinsey estimates the general-purpose robotics market could
reach approximately $370 billion by 2040.

### Sensing and Perception

A robot's ability to act in the world depends on its ability to sense
the world. Robotic perception encompasses the sensors, algorithms, and
representations that convert raw physical signals into actionable
understanding of the environment. The primary sensing modalities in
modern robotics are vision (cameras, depth sensors, LiDAR), touch
(tactile sensors, force-torque sensors), proprioception (joint
encoders, IMUs), and audition (microphones).

Computer vision is the dominant perception modality. Cameras provide
rich information about object identity, position, and geometry, and
modern deep learning models -- particularly convolutional neural
networks and, more recently, vision transformers -- have made visual
object detection, segmentation, and pose estimation highly reliable in
structured settings. Depth sensors and LiDAR add three-dimensional
geometric information, critical for navigation and manipulation in
unstructured environments. Event cameras, which report only changes in
brightness rather than full frames, provide microsecond latency and
high dynamic range, enabling kilohertz feedback for agile robots.

Simultaneous Localization and Mapping (SLAM) is the foundational
algorithm for mobile robot perception. SLAM addresses the chicken-and-
egg problem of building a map of an unknown environment while
simultaneously tracking the robot's position within that map. The
core SLAM pipeline consists of sensor data acquisition, feature
extraction, data association (matching observations to map features),
state estimation (updating robot pose and map), and loop closure
(recognizing previously visited locations to correct accumulated
drift). Modern SLAM systems use extended Kalman filters, particle
filters, or graph optimization backends. Visual SLAM, which uses
camera data as the primary sensing modality, has been augmented by
deep learning methods that improve feature extraction, place
recognition, and dynamic object handling. SLAM is essential for
autonomous navigation in warehouses, factories, and outdoor
environments where pre-built maps are unavailable or stale.

Tactile sensing is critical for manipulation but has lagged behind
vision in maturity. Tactile sensors measure contact forces, pressure
distributions, and slip, enabling robots to grasp delicate objects,
adjust grip force, and detect when an object is slipping. Recent work
on tactile sensors -- such as GelSight, which uses a camera embedded
in a elastomer to capture high-resolution contact geometry -- has
improved grasping stability and enabled more dexterous manipulation.
Soft gripping technology, which uses compliant materials that conform
to object shapes, further improves grasping robustness for irregular
and fragile objects.

### Motion Planning and Control

Motion planning is the process of computing a collision-free path from
a start configuration to a goal configuration, while control is the
process of executing that path by commanding joint torques or
velocities. These two problems -- planning and control -- are the
motion layer of robotics, bridging perception and action.

Classical motion planning algorithms include graph-based search (A*,
Dijkstra), sampling-based methods (RRT, PRM), and optimization-based
methods (trajectory optimization, model predictive control). These
algorithms operate in the robot's configuration space, where each
point represents a valid robot pose and obstacles are expanded by the
robot's geometry. Sampling-based planners like RRT (Rapidly-exploring
Random Tree) and its variants are widely used because they scale to
high-dimensional configuration spaces, which are common in humanoid
robots with 30-56 degrees of freedom.

Control theory provides the mathematical framework for making a robot
execute a planned motion despite disturbances, modeling errors, and
sensor noise. Model-based controllers use a mathematical model of the
robot's dynamics to compute the forces needed to track a desired
trajectory. Model Predictive Control (MPC) optimizes control actions
over a receding time horizon, accounting for constraints on joint
limits, torque limits, and obstacle avoidance. Whole-body MPC is
particularly important for humanoids, where the controller must
coordinate leg locomotion, arm manipulation, and balance simultaneously.
Whole-body MPC for bipedal locomotion must solve a high-dimensional
nonlinear optimization problem in real time, typically at 100-1000 Hz
control rates.

The sim-to-real gap is the central challenge in learned control. A
policy trained in simulation can exploit simulation-specific dynamics
that do not hold in reality, causing catastrophic failure when
deployed on a physical robot. Domain randomization addresses this by
randomizing simulation parameters (friction, mass, actuator dynamics)
during training, forcing the policy to be robust to parameter
variation. Domain adaptation fine-tunes the policy using real-world
data. Digital twin approaches create high-fidelity simulation models
of specific robots to narrow the gap. Despite these techniques, the
sim-to-real gap remains a fundamental barrier, particularly for tasks
involving contact-rich manipulation where friction and deformation are
difficult to simulate accurately.

### Reinforcement Learning for Manipulation

Deep reinforcement learning (DRL) has become a dominant approach for
teaching robots complex manipulation skills. Reinforcement learning
frames robot learning as an agent interacting with an environment,
receiving rewards for desired behaviors and penalties for undesired
ones. The agent learns a policy -- a mapping from observations to
actions -- that maximizes cumulative reward over time. Deep
reinforcement learning replaces the hand-crafted features of classical
RL with neural network function approximators, enabling learning from
high-dimensional sensory inputs like images and point clouds.

The major DRL algorithm families for robotic manipulation are
value-based methods (DQN and variants), policy-based methods (policy
gradient, REINFORCE), and actor-critic methods (PPO, SAC, TD3).
Value-based methods learn a value function that estimates the expected
return for each action and select actions greedily. Policy-based
methods directly optimize the policy parameters by estimating the
gradient of expected return. Actor-critic methods combine both,
learning a policy (actor) and a value function (critic) simultaneously.
Soft Actor-Critic (SAC), which optimizes a maximum-entropy objective
that encourages exploration, has become one of the most widely used
algorithms for continuous control tasks like manipulation because of
its sample efficiency and stability.

Robotic manipulation poses specific challenges for RL. The state space
is continuous and high-dimensional. The action space includes joint
torques, velocities, or end-effector poses. Rewards are sparse --
a robot receives reward only after completing a task (e.g.,
successfully grasping an object), and random exploration rarely
achieves the goal. Reward engineering, the process of designing reward
functions that guide learning without creating unintended behaviors,
is a significant practical challenge. Sim-to-real transfer is
essential because training in the real world is slow, expensive, and
risky -- a robot learning to grasp might drop thousands of objects
before becoming proficient.

Imitation learning offers an alternative to RL that avoids the
exploration problem. In imitation learning, a human demonstrator
provides examples of desired behavior -- through teleoperation,
kinesthetic teaching, or video demonstration -- and the robot learns
to imitate these examples. Behavior cloning directly maps observations
to actions from demonstration data. Inverse reinforcement learning
infers the reward function that the demonstrator is optimizing, then
uses RL to learn a policy under that reward. Imitation learning is
data-efficient but limited by the quality and diversity of
demonstrations. Diffusion policies, which learn action distributions
using diffusion models, have emerged as a powerful imitation learning
approach, enabling robots to learn complex manipulation skills from
relatively few demonstrations while maintaining multimodal action
distributions that capture the variability of human behavior.

### Foundation Models for Robotics

The integration of large language models and vision-language models
into robotics represents the most significant paradigm shift in the
field since the introduction of deep reinforcement learning. Foundation
models -- large neural networks pre-trained on internet-scale data --
bring semantic understanding, high-level reasoning, and cross-modal
generalization to robotic systems. The review by Khan and Waheed (2025)
categorizes foundation model applications in robotics across four
domains: perception, planning, control, and human-robot interaction.

In perception, vision-language models (VLMs) enable robots to identify
objects, scenes, and spatial relationships using natural language
descriptions, generalizing to novel objects without task-specific
training. In planning, large language models decompose abstract
instructions into sequences of sub-tasks, leveraging common sense
reasoning and world knowledge. A sufficiently large pre-trained LLM can
convert an instruction like "clean the kitchen" into a plausible
sequence of sub-tasks -- find dishes, pick up dishes, carry to sink,
place in sink, turn on water -- in a zero-shot setting without
additional training. In control, foundation models generate robot
control code on demand, synthesizing motion planners and manipulation
skills for novel tasks. In human-robot interaction, foundation models
enable robots to interpret natural language commands and respond with
contextual fluency.

The vision-language-action (VLA) model is the architecture that unifies
these capabilities into a single system. A VLA model takes visual
input (camera images), language input (task instructions), and
produces action output (robot motor commands). Google's PaLM-E, which
integrated the PaLM language model with embodied sensing, demonstrated
that internet-scale language and vision pre-training could transfer to
embodied agents, allowing them to handle multimodal reasoning tasks
across multiple robot types in a zero-shot fashion. Figure AI's Helix
is a production VLA model that enables humanoid robots to perform
complex manipulation tasks with dynamic object recognition and
collaboration without prior training. NVIDIA's GR00T is an open
foundation model for humanoid robots, paired with the Jetson Thor
onboard computer as the inference platform. Diffusion-VLA (DiVLA)
integrates autoregressive language reasoning with diffusion-based
action generation, combining the interpretability of chain-of-thought
reasoning with the robustness of diffusion policies.

Cross-embodiment learning is an emerging capability in which a single
foundation model controls different robot platforms -- arms, humanoids,
quadrupeds -- by learning platform-agnostic action representations.
This addresses a fundamental data scarcity problem: each robot platform
generates its own data, but a generalist model trained across platforms
can leverage all available data. The concept parallels the
generalist language models that serve many tasks through a single
architecture.

## Evidence

### The Industrial Robot Scale and Trajectory

The International Federation of Robotics (IFR) World Robotics 2025
report provides the definitive quantitative picture of industrial
robotics. In 2024, global industrial robot installations reached
542,000 units, the fourth consecutive year above 500,000. The global
operational stock reached 4,664,000 units, up 9 percent year-over-year.
China installed 295,000 units, accounting for 54 percent of the world
total -- a record. The IFR forecasts approximately 575,000 installations
in 2025 and a climb past 700,000 per year by 2028. This data
establishes that industrial robotics is a mature, large-scale
technology with a proven economic case, and that the installed base
provides the hardware foundation on which AI-driven capabilities are
being layered.

Analysis Atlas research corroborates this scale: factories installed
542,000 industrial robots in 2024 and the global operational stock hit
4.66 million. This mature, slow-growing market for caged industrial
arms sits beside a second story moving at venture speed. Capital is
pouring into humanoid robots at valuations that bear no relation to
current revenue: Figure AI raised more than $1 billion in September
2025 at a $39 billion post-money valuation, a roughly fifteenfold
step-up from its $2.6 billion mark eighteen months earlier. Apptronik
reached $5 billion. Skild AI, which builds robot software rather than
hardware, hit a $14 billion valuation in January 2026. These
valuations reflect the market's belief that the same model architecture
behind large language models could control a physical body, and that
the physical labor market dwarfs the digital one.

### Deep Reinforcement Learning for Manipulation -- Survey Evidence

Han, Mulyana, Stankovic, and Cheng (2023) published a comprehensive
survey of deep reinforcement learning algorithms for robotic
manipulation in the journal Sensors. The survey covered value-based
methods, policy-based methods, and actor-critic approaches applied to
grasping and object manipulation. The authors identified several key
challenges that remain unsolved: improving sample efficiency (the
number of environment interactions needed to learn a task), developing
transfer learning capabilities (applying skills learned in one task to
new tasks), achieving real-time control (many DRL algorithms are too
slow for real-time robot control), enabling safe exploration (robots
must explore their environment without harming themselves or their
surroundings), and integrating multiple learning paradigms. The survey
concluded that while DRL has enabled robots to learn manipulation
tasks that were previously infeasible, the field has not yet achieved
the sample efficiency and reliability needed for widespread real-world
deployment. This finding is consistent with the assessment by Frontiers
researchers that "current learning-based methods fail to achieve a
reliable percentage for real-world-ready products and are not yet ready
for production line deployment" for grasping unknown objects.

A PMC review of robotic dexterous grasping methods based on point cloud
and deep learning traced the evolution of grasp learning from 2015 to
the present. The earliest state-of-the-art work, Grasp Pose Detection
(GPD), sampled candidate grasp poses from point clouds and used deep
learning to evaluate them. Most subsequent work followed this
generate-and-evaluate framework, contributing to either the generation
stage (producing better candidate grasps) or the evaluation stage
(scoring grasps more accurately). The survey noted that domain
randomization approaches suffer from low interpretability, and that
non-real hypotheses in domain adaptation make sim-to-real transfer
difficult to solve. Imitation learning, meta-learning, and knowledge
distillation were identified as promising directions for addressing
these gaps.

### Foundation Models in Robotics -- The Review Literature

Khan and Waheed (2025) published a comprehensive review of foundation
model-driven robotics, categorizing applications across simulation-
driven design, open-world execution, sim-to-real transfer, and
adaptable robotics. The review highlighted that existing surveys tend
to focus on isolated capabilities (perception alone, planning alone)
while overlooking the integration of components in practical settings.
The authors identified four core components of any robotic system --
perception, planning, control, and human-robot interaction -- and
mapped foundation model contributions to each. In perception, VLMs
provide semantic understanding of scenes and objects. In planning,
LLMs decompose abstract goals into actionable sub-task sequences
using common sense reasoning and world knowledge, with zero-shot
generalization to unfamiliar tasks. In control, foundation models
generate robot control code on demand, synthesizing motion planners
for novel scenarios. In human-robot interaction, foundation models
enable natural language command interpretation with contextual
fluency.

The review also identified critical limitations. Foundation models
lack embodiment -- they are trained on internet data, not physical
interaction data, creating a grounding gap between semantic
understanding and physical execution. Multimodal robot data is scarce:
unlike text and images, which exist in internet-scale quantities,
robot interaction data (tactile, proprioceptive, force) is expensive to
collect and platform-specific. Safety risks arise when LLM-generated
control code propagates incorrect reasoning into unsafe actions. Chain-
of-thought prompting, while improving reasoning traceability, remains
sensitive to ambiguous task specifications. The review concluded that
the critical open challenges are real-time operation, grounding,
resilience, and trust -- the gap between semantic reasoning and
physical intelligence remains the central research problem.

The arXiv survey by Cao (2024) on humanoid robots and humanoid AI
provided the historical and conceptual framework for the humanoid
wave. Cao traced the approximately century-long journey of robotics,
noting that humanoid robots emerged about 60 years ago and began
exhibiting notable human-like senses and behaviors about 30 years ago.
The rapid advancement of generative AI and multimodal large language
models has "reignited and escalated interest in humanoids towards
real-time, interactive, and multimodal designs and applications,"
including humanoid workers, advisers, educators, medical
professionals, and caregivers. Cao framed this as a transformation
from "AI robotics" into "humanoid AI" -- a shift from robots with
human-like appearances to robots with human-like behaviors,
expressions, and reasoning.

### Humanoid Deployment Evidence

The deployment record for humanoid robots in 2025-2026 provides early
empirical evidence of the transition from demonstration to production.
Boston Dynamics' Electric Atlas entered production in January 2026,
with all 2026 deployments committed to Hyundai's Robotics Metaplant
Application Center and Google DeepMind. Atlas has 56 degrees of
freedom, a 30 kg sustained payload, and a 4-hour swappable battery. At
CES 2026, Atlas won CNET's Best of CES "Best Robot" award, and Boston
Dynamics announced a partnership with Google DeepMind to run Gemini
Robotics models on the platform.

Figure AI's Figure 02 logged over 90,000 parts handled across eleven
months at a BMW plant before its successor, Figure 03, was announced
in October 2025. Figure 03 is built around Helix, the company's in-
house vision-language-action model. The BotQ factory is tooled for up
to 12,000 units per year, targeting 100,000 robots over four years.
Unitree's average selling price collapsed from approximately $85,000 in
2023 to roughly $25,000 in 2025, with the stripped-down R1 launched at
$5,900. AgiBot reported its 10,000th robot on March 30, 2026, three
months after reporting 5,000 in December 2025. An AgiBot A2 set a
Guinness World Record in January 2026 for the longest humanoid walk:
106 km from Suzhou to Shanghai.

McKinsey's June 2025 report "Will embodied AI create robotic
coworkers?" found that general-purpose robotics funding grew fivefold
from 2022 to 2024, surpassing $1 billion in annual investment. Patent
filings surged with a 40 percent CAGR since 2022. China designated
embodied AI a national priority, anchoring a $138 billion innovation
fund. McKinsey estimated the general-purpose robotics market could
reach approximately $370 billion by 2040, while noting that general-
purpose robots "capable of grasping, lifting and placing items are not
here yet, but the building blocks are emerging fast." The barriers
identified -- task-specific data, battery life, component supply chains,
and autonomy -- define the research and engineering frontier.

## Implications

### For Manufacturing and Logistics

The most immediate application of embodied AI is in manufacturing and
logistics, where robots have been deployed for decades but remain
limited to structured, repetitive tasks. The integration of foundation
models and reinforcement learning promises to extend robotic
capabilities into unstructured environments -- variable product
shapes, changing layouts, and tasks that require adaptation. Humanoid
robots are entering automotive plants (Hyundai, BMW), warehouses
(Agility Robotics' Digit at GXO Logistics), and logistics hubs. The
economic case is straightforward: if a general-purpose humanoid can
perform the diverse physical tasks that human workers do, using
existing infrastructure, then the cost of physical labor becomes a
function of robot price and operating cost rather than human wages.

The trajectory of robot costs supports this case. Unitree's price
collapse from $85,000 to $25,000 in two years mirrors the cost curve
of other technology products driven by scale and learning. If humanoid
prices follow a similar trajectory toward the $20,000-30,000 target
that Tesla and others have stated, the payback period for replacing
human labor in structured industrial settings becomes compelling.
However, current deployments remain pilots with on-site engineering
support, not autonomous operations. The honest assessment from the
Robotics Center buyer's guide is that "if you are buying a humanoid in
2026, you are buying a research platform or a data collection tool, not
an autonomous worker." The gap between demonstration and deployment
remains the central practical challenge.

### For AI Research and Development

Robotics is becoming a primary frontier for AI research, not a
peripheral application. The argument, articulated by multiple frontier
labs, is that the road to artificial general intelligence runs through
the body, not around it. Physical embodiment forces AI systems to
confront problems that purely digital AI does not: continuous state
spaces, partial observability, real-time constraints, safety
requirements, and the sim-to-real gap. These challenges drive the
development of new architectures -- vision-language-action models,
cross-embodiment learning, world models -- that may ultimately
contribute back to digital AI.

The data problem is distinctive. Language and image data exist in
internet-scale quantities, but robot interaction data is scarce,
expensive, and platform-specific. This creates an incentive for
data-sharing consortia, simulation-based data generation, and
cross-platform generalization. NVIDIA's strategy -- providing the
compute platform (Jetson Thor) and open foundation models (GR00T) that
many robot makers build on -- positions it to capture value regardless
of which hardware platform wins, mirroring its data center strategy.
The compute requirements for real-time robot inference are substantial:
a VLA model running at 10-50 Hz control rates on a power-constrained
mobile platform demands specialized hardware, driving demand for the
same AI accelerators that power language model inference.

### For Work and the Labor Market

The long-term implications of general-purpose robotics for the labor
market are significant but uncertain. If humanoid robots achieve
generalist physical capabilities at a cost below human wages, the
economic calculus for a wide range of physical labor shifts. Goldman
Sachs projects the humanoid market at $38 billion by 2035, and
McKinsey projects the general-purpose robotics market at $370 billion
by 2040 -- but these projections assume that current technical barriers
(dexterity, battery life, data, autonomy) are overcome. The historical
pattern of industrial automation suggests that robotics tends to
displace specific tasks rather than entire jobs, augmenting human
workers in some contexts while displacing them in others. The
transition from caged industrial arms to general-purpose humanoids
widens the set of tasks that can be automated, but the pace and
distribution of this transition depend on factors -- cost curves,
regulatory frameworks, safety standards, and social acceptance -- that
remain unresolved.

The safety dimension is critical. Industrial robots are fenced off
precisely because they are dangerous to humans in their workspace.
Humanoid robots, designed to work alongside humans, must meet safety
standards that traditional industrial robots do not face. ISO 13482
(safety requirements for personal care robots) and ISO 10218 (safety
requirements for industrial robots) define the regulatory landscape,
but these standards are evolving to accommodate general-purpose
humanoids. Safe exploration -- the ability of a learning robot to
explore its environment without harming itself, humans, or property --
is both a research challenge and a regulatory prerequisite for
deployment.

The distributional question -- who benefits and who bears the cost of
robotic automation -- is unresolved. Historical automation displaced
routine physical labor while creating demand for higher-skill work in
robot programming, maintenance, and oversight. General-purpose
humanoids, if they achieve their stated capabilities, would automate a
broader range of physical tasks, potentially affecting occupations
that were previously insulated from automation. The policy responses
under discussion include retraining programs, tax incentives for
human-augmenting rather than human-replacing automation, and social
safety net expansions. None of these has been tested at scale against
general-purpose robotic automation, because the automation itself has
not yet arrived at scale. The McKinsey finding that general-purpose
robots "are not here yet" means the labor market impacts remain
speculative, but the trajectory of investment and cost reduction
suggests the window for proactive policy is narrowing.

### For Adjacent Technology Domains

Robotics intersects with multiple technology domains in the brain.
Semiconductors provide the compute substrate: NVIDIA's Jetson Thor,
Tesla's AI5 chip, and the broader AI accelerator market are driven
partly by robotics demand alongside data center demand. Cloud
computing provides the infrastructure for simulation, training, and
fleet management: robots are increasingly connected systems that
offload heavy computation to the cloud while running real-time control
locally. Large language models provide the reasoning and planning
layers that are being adapted into vision-language-action models for
robot control. The convergence of these domains -- compute, cloud, AI
models, and physical hardware -- is what makes embodied AI possible,
and advances in any one domain ripple through the others.

## Sources

1. IFR World Robotics 2025. "World Robotics 2024-2025: Industrial
   Robots." International Federation of Robotics.
   https://ifr.org/worldrobotics [high]

2. Han, D., Mulyana, B., Stankovic, V., & Cheng, S. (2023). "A Survey
   on Deep Reinforcement Learning Algorithms for Robotic Manipulation."
   Sensors, 23(7), 3762. https://www.mdpi.com/1424-8220/23/7/3762 [high]

3. Khan, M. T. & Waheed, A. (2025). "Foundation Model Driven Robotics:
   A Comprehensive Review." arXiv:2507.10087.
   https://arxiv.org/pdf/2507.10087v1 [high]

4. Cao, L. (2024). "Humanoid Robots and Humanoid AI: Review,
   Perspectives and Directions." arXiv:2405.15775.
   https://arxiv.org/pdf/2405.15775v3 [high]

5. McKinsey & Company (2025). "Will embodied AI create robotic
   coworkers?" McKinsey Robotics Research, June 2025.
   https://www.mckinsey.com [medium]

6. Goldman Sachs Research (2025). "Humanoid Robots: The Next Wave of
   Automation." Goldman Sachs.
   https://www.goldmansachs.com/insights [medium]

7. Analysis Atlas (2026). "Robotics and Industrial Automation: 542,000
   Installs and the Humanoid Capital Wave."
   https://analysis-atlas.com/research/robotics-industrial-automation-market [medium]

8. Robotics Center (2026). "Humanoid Robot Buyer's Guide 2026: Compare
   Models, Costs & Use Cases."
   https://www.roboticscenter.ai/guides/humanoid-robot-buyers-guide-2025 [medium]

9. Boston Dynamics (2026). "Atlas Humanoid Robot -- Product Page."
   https://bostondynamics.com/products/atlas/ [high]

10. arXiv survey: "Large Language Models for Robotics: A survey."
    arXiv:2311.07226. https://arxiv.org/html/2311.07226v2 [high]

11. RoboZaps Blog (2026). "38 Best Humanoid Robots in 2026
    (Evidence-Ranked)." https://blog.robozaps.com/b/best-humanoid-robots [medium]

12. De Valence, G. (2025). "Embodied AI and General Purpose Robots."
    https://gerard-de-valence.blogspot.com/2025/11/embodied-ai-and-general-purpose-robots.html [low]

## See Also

- `library/technology/large-language-models.md` -- the foundation models
  being adapted as reasoning and planning layers for robotic control.
- `library/technology/semiconductors.md` -- the compute substrates (NVIDIA
  Jetson, Tesla AI5) that enable real-time robot inference.
- `library/technology/cloud-computing.md` -- the cloud infrastructure for
  robot simulation, training, and fleet management.