---
name: quantum-computing
id: 20260729T180233Z
tier: library-topic
domain: technology
author: Researcher-1
tags: [quantum-computing, qubits, superposition, entanglement, error-correction, shors-algorithm, grovers-algorithm]
links: [library/technology/semiconductors.md]
---

# Quantum Computing -- What It Promises and Why It Is So Hard

Quantum computing harnesses the counterintuitive rules of quantum
mechanics -- superposition and entanglement -- to perform calculations
that are exponentially faster than what any classical computer can
achieve for specific problem classes. Unlike classical bits that are
either 0 or 1, quantum bits (qubits) can exist in a blend of both
states simultaneously, enabling a single quantum processor to explore
vast solution spaces in parallel. Despite decades of progress and
billions in investment, the technology remains pinned in the NISQ
(Noisy Intermediate-Scale Quantum) era, where error rates and
decoherence prevent practical quantum advantage for all but a handful
of contrived demonstrations.

## Background

The intellectual foundations of quantum computing trace to the early
1980s, when physicist Richard Feynman observed that simulating quantum
mechanical systems on classical computers was fundamentally
intractable. The state space of a quantum system grows exponentially
with the number of particles: simulating a system of just 50 electrons
would require more classical bits than there are atoms in the
observable universe. Feynman proposed turning the problem into the
solution: build a computer that is itself quantum mechanical, and let
it simulate nature directly.

In 1985, David Deutsch at Oxford formalized the concept of a universal
quantum computer, showing that a quantum Turing machine could, in
principle, simulate any physical process. The field remained largely
theoretical until 1994, when Peter Shor at Bell Labs published an
algorithm demonstrating that a quantum computer could factor large
integers in polynomial time -- an exponential speedup over the best
known classical algorithms. Because the security of RSA encryption
rests on the difficulty of factoring, Shor's algorithm transformed
quantum computing from a physics curiosity into a technology with
direct national security implications.

The second algorithmic breakthrough came in 1996 when Lov Grover
showed that quantum search could find a marked item in an unsorted
database of N entries in roughly sqrt(N) steps, a quadratic speedup
over classical brute force. Together, Shor's and Grover's algorithms
established the two fundamental categories of quantum speedup:
exponential (Shor) and polynomial (Grover), and provided the
theoretical justification for the massive investment that followed.

The hardware challenge proved far harder than the algorithms. The
first two-qubit gate was demonstrated in 1995, and progress was
measured in single-digit qubit counts for two decades. The field
crossed into public consciousness in 2019 when Google's Sycamore
processor, with 53 qubits, completed a carefully designed sampling
calculation in 200 seconds that the company estimated would take a
classical supercomputer 10,000 years -- a claim IBM quickly contested,
arguing the classical simulation could be done in 2.5 days with better
algorithms. This "quantum supremacy" debate highlighted a recurring
theme: classical computers are a moving target, and quantum advantage
must be demonstrated on practically useful problems, not just
contrived benchmarks.

## Core Concepts

### Qubits, Superposition, and the Exponential State Space

A classical bit is a binary switch: 0 or 1. A qubit is a two-level
quantum system that can exist in a superposition of both states
simultaneously, described by complex probability amplitudes rather
than a single discrete value. The state of a qubit can be visualized
as a point on the surface of a Bloch sphere, where the north and south
poles represent the classical 0 and 1 states, and every other point
represents a distinct superposition.

The power of superposition emerges from the mathematics of combining
qubits. One qubit encodes a superposition of two basis states. Two
qubits encode four. Three qubits encode eight. Each additional qubit
doubles the dimensionality of the state space. With just 50 qubits in
full superposition, the number of simultaneous states exceeds a
quadrillion. With 300 qubits, the number of states exceeds the
estimated count of particles in the observable universe. This
exponential scaling is the fundamental source of quantum computing's
potential advantage: while a classical computer must process
combinations sequentially, a quantum computer can explore an entire
exponentially large space in a single run.

The crucial limitation is that when you measure a qubit, the
superposition collapses to a single classical outcome. A computation
on 50 qubits produces only 50 classical bits of output -- you never
get to read the entire exponentially large state. The art of quantum
algorithm design is structuring the computation so that the desired
answer interferes constructively while wrong answers cancel out,
making the correct result overwhelmingly likely when measurement
occurs.

### Entanglement: The Essential Computational Resource

Superposition alone is not enough. Without entanglement, each qubit
would be independent, and you would gain no advantage over processing
them classically one at a time. Entanglement is a quantum correlation
with no classical equivalent: when two qubits are entangled, measuring
one instantaneously determines the state of the other, regardless of
the physical distance between them. This correlation is stronger than
anything permitted by classical physics, formalized by Bell's
inequality and confirmed by decades of experimental tests that won the
2022 Nobel Prize in Physics for Alain Aspect, John Clauser, and Anton
Zeilinger.

Entanglement ties the entire exponentially large state space together
into a coherent computational resource. It is what makes quantum
algorithms work: by entangling qubits, the quantum computer processes
combinations of states that are not accessible to classical systems.
The simplest entangled state is the Bell state, in which two qubits
share an equal superposition of both being 0 and both being 1. The
Hadamard gate followed by a CNOT gate creates this state, and together
with arbitrary single-qubit rotations, these operations form a
universal gate set capable of implementing any quantum computation.

### Quantum Gates, Circuits, and Interference

Quantum computation is programmed using quantum gates: operations that
rotate or entangle qubits through precisely shaped microwave or laser
pulses. The Pauli-X gate is the quantum equivalent of a classical NOT,
flipping the 0 state to 1 and vice versa. The Hadamard gate creates an
equal superposition from a definite state. The CNOT gate entangles two
qubits by flipping the target if and only if the control is in the 1
state. A sequence of gates applied to qubits constitutes a quantum
circuit -- the quantum analog of a classical program.

Interference is the mechanism by which quantum computations produce
useful answers. Because probability amplitudes are complex numbers,
they can add constructively (reinforcing each other) or destructively
(cancelling each other out). A well-designed quantum algorithm steers
interference so that computational paths leading to wrong answers
cancel while paths leading to the correct answer reinforce. When
measurement finally collapses the superposition, the right answer
appears with high probability.

This three-step cycle -- initialize superposition, apply gates that
entangle qubits and steer interference, then measure -- is the
universal structure of every quantum algorithm. The difficulty is that
each step must occur in an extraordinarily fragile physical
environment, and gate operations must complete before the quantum
state is destroyed by interactions with the outside world.

### The NISQ Era and the Error Correction Wall

The current era of quantum computing is called NISQ: Noisy
Intermediate-Scale Quantum. NISQ devices have 50 to a few hundred
physical qubits with gate fidelities in the range of 99.0% to 99.9%.
At first glance, 99.9% fidelity sounds excellent, but consider: a
useful quantum computation may require thousands or millions of gate
operations. Even at 99.9% per gate, after 1,000 operations the
probability of an error-free computation is near zero.

Quantum error correction (QEC) provides a theoretical solution.
Information is encoded redundantly across multiple physical qubits to
form a single logical qubit, and errors are detected and corrected
without collapsing the quantum state. The surface code, the
best-studied QEC scheme, requires on the order of 1,000 physical
qubits to produce one logical qubit with sufficiently low error rates
for deep computation. This means a fault-tolerant quantum computer
capable of running Shor's algorithm on cryptographically relevant key
sizes would need millions of physical qubits.

The central milestone the field has chased is "below-threshold"
operation: the point where adding more physical qubits to a code
reduces the logical error rate rather than increasing it. Before
below-threshold, error correction adds more errors than it fixes.
Google's Willow processor, demonstrated in late 2024 and published in
Nature in 2025, became the first superconducting system to achieve
below-threshold surface code error correction, with a 101-qubit
distance-7 code showing that scaling up the code distance
exponentially suppressed the logical error rate. IBM has pursued a
complementary approach: error mitigation rather than full correction,
using classical post-processing on their 1,121-qubit Condor processor
to extract useful results from noisy computations.

## Hardware Approaches: The Four-Way Race

### Superconducting Qubits

Superconducting qubits are artificial atoms fabricated from aluminum
or niobium circuits cooled to approximately 15 millikelvin -- colder
than deep space -- in dilution refrigerators. This is the most mature
approach, used by IBM, Google, and Rigetti. Gate speeds are on the
order of 10-100 nanoseconds, making superconducting qubits the
fastest platform by orders of magnitude. IBM's Nighthawk processor
(2025) features 120 qubits with support for circuits of up to 5,000
two-qubit gates, and IBM's roadmap targets modular architectures
(Flamingo, Starling) that network multiple quantum processing units
together.

The tradeoff is coherence time: superconducting qubits maintain their
quantum state for hundreds of microseconds at best. They are also
fabricated with semiconductor manufacturing processes, giving them a
scaling advantage, but each chip is unique and requires individual
calibration. Google's Willow chip, with 105 qubits, demonstrated
below-threshold error correction, achieving a logical error rate of
approximately 0.143% per error correction cycle on a distance-7 code,
with the error rate decreasing as code distance increased.

### Trapped-Ion Qubits

Trapped-ion qubits use individual atoms -- typically ytterbium or
calcium -- suspended in ultra-high vacuum by electromagnetic fields
and manipulated with laser beams. This is the approach of IonQ and
Quantinuum. Every trapped-ion qubit is a fundamental particle of
nature, perfectly identical to every other qubit of the same species,
eliminating the manufacturing variation that plagues solid-state
systems.

Trapped-ion systems offer the highest gate fidelities of any platform,
with two-qubit gate fidelities reaching 99.99% on Quantinuum's Helios
system. Coherence times reach seconds -- orders of magnitude longer
than superconducting qubits. The tradeoff is speed: trapped-ion gates
operate on the microsecond timescale (1-100 microseconds), roughly
1,000 times slower than superconducting gates. All-to-all qubit
connectivity is a key architectural advantage: any ion can be
entangled with any other ion in the trap without intermediate
swap operations, simplifying algorithm implementation.

Scaling trapped-ion systems has been historically difficult because
adding more ions to a single trap creates complex interactions that
degrade fidelity. Both IonQ and Quantinuum have adopted modular
architectures -- QCCD (Quantum Charge-Coupled Device) for Quantinuum
and RMQA (Reconfigurable Multicore Quantum Architecture) for IonQ --
that network multiple smaller traps, analogous to multi-core classical
processors. Quantinuum's Helios, the largest trapped-ion system as of
2026, operates 98 physical qubits.

### Topological Qubits

Topological quantum computing represents a radical departure from both
superconducting and trapped-ion approaches. Rather than battling
decoherence through active error correction, the goal is to build a
qubit that is naturally immune to local sources of error by encoding
quantum information in the global, topological properties of a
many-body quantum system. The information is stored in exotic
quasiparticles called non-Abelian anyons whose quantum states depend
on how they are "braided" -- moved around each other in spacetime.

If successful, topological qubits could leapfrog the immense overhead
of conventional quantum error correction by providing intrinsic fault
tolerance at the physical hardware level. However, the approach remains
the most theoretical and experimentally nascent: it requires creating
and manipulating states of matter -- specifically Majorana zero modes
-- whose very existence has been contested. Microsoft is the most
prominent and heavily invested proponent, having bet its quantum
strategy on the topological approach for over two decades.

In 2025, Microsoft claimed its Majorana 1 processor had passed a
"topological gap protocol" suggesting the presence of Majorana zero
modes, but the claim was met with significant skepticism from the
physics community. The protocol does not provide direct, unambiguous
evidence, and no consensus has been reached on whether a physical
topological qubit has been demonstrated.

An alternative "emergent" approach has gained traction: using
topological error correction codes such as the surface code on
conventional hardware to simulate the behavior of topological qubits.
Both Google and Quantinuum have demonstrated key components of this
approach, creating logical qubits whose properties mimic those of true
topological systems. The intrinsic (materials-science) path is a
high-risk bet on a physics breakthrough; the emergent (engineering)
path builds topological protection on top of improving conventional
hardware.

### Other Approaches

Neutral-atom qubits, using arrays of individual atoms trapped in
optical tweezers (pursued by QuEra and Pasqal), offer reconfigurable
qubit connectivity and have scaled to hundreds of qubits. Photonic
quantum computing (pursued by Xanadu and PsiQuantum) encodes qubits
in photons and operates at room temperature, avoiding the
cryogenic requirements of other platforms. Silicon spin qubits
leverage the semiconductor industry's manufacturing expertise by
encoding qubits in the spin of electrons in silicon -- the same
material classical computing is built on.

## Evidence and Research Foundation

The theoretical evidence for quantum computing's potential is
mathematically rigorous. Shor's algorithm (1994) provides a provable
exponential speedup for integer factorization and the discrete
logarithm problem, the two mathematical foundations of modern
public-key cryptography. Grover's algorithm (1996) provides a provable
quadratic speedup for unstructured search, with implications for
database queries, optimization, and brute-force attacks on symmetric
encryption. Neither result is contested; the question is whether
physical hardware can implement them at scale.

The empirical evidence for hardware progress is measured in steadily
improving gate fidelities and qubit counts. Two-qubit gate fidelity, a
critical metric for algorithm performance, has improved from roughly
90% in the early 2010s to 99.9%+ on the best superconducting systems
and 99.99% on the best trapped-ion systems as of 2026. IBM's Condor
processor reached 1,121 physical qubits in 2023, though qubit count
alone is misleading -- the number of qubits that can be entangled in a
single computation (circuit depth) is the more meaningful metric.

The most significant experimental milestone was Google's demonstration
of below-threshold quantum error correction on the Willow processor,
published in Nature in 2025. The experiment encoded a logical qubit
using a surface code of distance 7 (101 physical qubits) and distance
5 (49 physical qubits) and showed that the logical error rate per
error correction cycle was suppressed by a factor of Lambda = 2.14
when increasing the code distance by 2. This was the first
experimental confirmation that scaling up error correction codes
reduces rather than increases errors -- the inflection point the
field had pursued for decades.

The 2022 Nobel Prize in Physics, awarded to Aspect, Clauser, and
Zeilinger for experimental tests of Bell's inequalities, provided
definitive experimental confirmation of quantum entanglement. While
not a computing milestone itself, the Nobel recognition validated the
physical foundation on which quantum computing rests: entanglement is
real, operates as quantum theory predicts, and cannot be explained by
any classical mechanism.

The practical evidence is more sober. Quantum advantage has been
demonstrated only on contrived problems: Google's 2019 "supremacy"
experiment solved a random circuit sampling problem with no known
practical application. IBM's subsequent work showed that improved
classical algorithms can simulate these problems more efficiently than
initially claimed, narrowing the advantage gap. As of 2026, no quantum
computer has solved a commercially valuable problem faster than a
classical computer. The pharmaceutical industry, often cited as a key
beneficiary, has not yet used a quantum computer to discover a drug.
Financial institutions experimenting with quantum portfolio
optimization report that classical heuristics remain competitive at
practical problem sizes.

The state of the evidence supports a measured conclusion: the physics
works, error correction is crossing from theory to engineering, but
the timeline to practical quantum advantage on economically meaningful
problems remains uncertain and almost certainly longer than early
roadmaps suggested.

## Implications

### Cryptography: The Race Against Shor's Algorithm

A fault-tolerant quantum computer running Shor's algorithm would break
RSA, elliptic curve cryptography, and essentially all public-key
cryptography currently securing the internet. The implications are
difficult to overstate: every encrypted message, digital signature,
and secure connection that relies on the hardness of factoring or the
discrete logarithm problem would be vulnerable.

The practical question is timing. NIST has standardized post-quantum
cryptography (PQC) algorithms -- including CRYSTALS-Kyber for key
encapsulation and CRYSTALS-Dilithium for digital signatures -- that
are believed to be resistant to both classical and quantum attacks.
The transition from current cryptography to PQC is underway but
complex: it requires updating protocols, hardware security modules,
and embedded systems across the entire digital infrastructure.

The more immediate threat is "harvest now, decrypt later": an adversary
that collects encrypted data today could store it and decrypt it
once a fault-tolerant quantum computer becomes available. For secrets
with long shelf lives -- classified government communications,
intellectual property, financial records -- the quantum threat is
already present, even if the hardware is a decade away. This is the
argument for beginning PQC migration immediately, not waiting for
quantum hardware to arrive.

Symmetric cryptography faces a milder threat from Grover's algorithm.
A 256-bit AES key, which would require 2^256 operations in a classical
brute-force attack, requires sqrt(2^256) = 2^128 operations under
Grover's algorithm -- still far beyond any plausible computational
capacity. Doubling symmetric key lengths from 128 to 256 bits provides
adequate protection.

### Drug Discovery and Materials Science

Quantum computers are, in Feynman's original vision, natural simulators
of quantum mechanical systems. Classical computers struggle to
accurately simulate molecular interactions because the computational
cost of representing electron correlations scales exponentially with
molecular size. A quantum computer would simulate these systems
natively, potentially enabling accurate prediction of drug-target
binding, catalyst behavior, and material properties without the
approximations that limit classical methods.

The Variational Quantum Eigensolver (VQE) and Quantum Approximate
Optimization Algorithm (QAOA) are the leading near-term approaches for
molecular simulation and optimization on NISQ hardware. However,
current demonstrations are limited to small molecules (hydrogen,
lithium hydride) that classical computers simulate with higher
accuracy anyway. The consensus among computational chemists is that
fault-tolerant quantum computers -- not NISQ devices -- will be
required for practically useful molecular simulations. A 2026 review
in npj Drug Discovery found that across molecular simulation, drug
design, and clinical trial optimization, quantum computing's projected
advantages are substantial but dependent on fault-tolerant hardware
not yet available.

The economic stakes are enormous: the average cost of bringing a new
drug to market exceeds $1 billion and requires over a decade. If
quantum simulation could eliminate even a fraction of failed clinical
trials by improving pre-clinical target validation, the savings would
dwarf the investment in quantum hardware.

### Optimization and Finance

Many real-world optimization problems -- supply chain routing,
portfolio allocation, traffic management, logistics -- are
combinatorial in nature, meaning the number of possible solutions
grows factorially with problem size. Quantum algorithms including QAOA
and quantum annealing offer theoretical speedups for these problems,
though the speedup is polynomial (Grover-type) rather than exponential
(Shor-type), meaning the advantage is more modest and classical
heuristics may close the gap for many practical problem sizes.

Financial institutions have been early adopters of quantum computing
research, exploring applications in portfolio optimization, risk
analysis, and option pricing. The quantum advantage for these
applications remains unproven at commercially relevant scales, and
quantum-inspired classical algorithms (tensor networks, approximate
optimization) have narrowed the expected gap.

### The Hardware Timeline and Investment Landscape

Global investment in quantum computing, combining government and
private funding, is estimated at over $40 billion cumulatively as of
2026. The United States, China, and the European Union each operate
national quantum programs funding hardware development, algorithm
research, and workforce training. The commercial quantum computing
market, dominated by cloud access to early-stage processors, generated
approximately $1-2 billion in revenue in 2025.

Most industry roadmaps target the demonstration of practically useful
quantum advantage -- solving a problem of economic value faster than
classical computers -- in the 2028-2035 window. Fault-tolerant quantum
computing at cryptographically relevant scale is generally projected
for the 2035-2045 timeframe, though these estimates have a history of
being revised outward. The key uncertainty is whether error correction
overhead will require hundreds or thousands of physical qubits per
logical qubit. At 1,000:1, a million-physical-qubit machine produces
1,000 logical qubits. At 10,000:1, it produces only 100.

## Sources

1. Feynman, R. (1982). "Simulating Physics with Computers."
   International Journal of Theoretical Physics, 21(6), 467-488.
   https://link.springer.com/article/10.1007/BF02650179 [high]

2. Deutsch, D. (1985). "Quantum theory, the Church-Turing principle
   and the universal quantum computer." Proceedings of the Royal
   Society of London A, 400, 97-117. [high]

3. Shor, P.W. (1994). "Algorithms for quantum computation: discrete
   logarithms and factoring." Proceedings 35th Annual Symposium on
   Foundations of Computer Science, 124-134.
   https://ieeexplore.ieee.org/document/365700 [high]

4. Grover, L.K. (1996). "A fast quantum mechanical algorithm for
   database search." Proceedings of the 28th Annual ACM Symposium
   on Theory of Computing, 212-219.
   https://arxiv.org/abs/quant-ph/9605043 [high]

5. Google Quantum AI and Collaborators. (2025). "Quantum error
   correction below the surface code threshold." Nature, 638, 920-926.
   https://www.nature.com/articles/s41586-024-08449-y [high]

6. Nielsen, M.A. & Chuang, I.L. (2010). "Quantum Computation and
   Quantum Information: 10th Anniversary Edition." Cambridge
   University Press. [high]

7. Quantum Zeitgeist. (2026). "What Is Quantum Computing? The Complete
   Guide [2026]."
   https://quantumzeitgeist.com/what-is-quantum-computing-the-complete-guide-2026/
   [medium]

8. Entangled Future. (2026). "Superconducting vs Trapped-Ion Qubits."
   https://entangledfuture.com/compare/superconducting-vs-trapped-ion/
   [medium]

9. uplatz. (2025). "Architectures of Quantum Computation: A
   Comparative Analysis of Superconducting, Trapped-Ion, and
   Topological Hardware."
   https://uplatz.com/blog/architectures-of-quantum-computation-a-comparative-analysis-of-superconducting-trapped-ion-and-topological-hardware/
   [medium]

10. Zhou, Y. et al. (2026). "Quantum-machine-assisted drug discovery."
    npj Drug Discovery, 3, 1.
    https://www.nature.com/articles/s44386-025-00033-2 [high]

## See Also

- `library/technology/semiconductors.md` -- the semiconductor
  manufacturing techniques that enable superconducting qubit
  fabrication and the classical computing substrate quantum processors
  depend on for control and readout.
- `library/technology/cybersecurity-principles-threats-and-defense-in-depth.md` --
  the cryptographic systems that Shor's algorithm threatens and the
  post-quantum cryptography migration currently underway.
