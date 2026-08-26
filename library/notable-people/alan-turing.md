---
name: alan-turing
id: 20260826T131602Z
tier: library-topic
domain: notable-people
author: Library Runner
tags: [alan-turing, computer-science, computability, enigma, bletchley-park, artificial-intelligence, turing-test, mathematical-biology]
links:
  - library/notable-people/ada-lovelace.md
  - library/history/world-war-ii.md
  - library/mathematics-statistics/information-theory.md
  - library/coding-agentic-ai/agent-evaluation-and-benchmarking.md
---

# Alan Turing -- The Architect of the Information Age

Alan Mathison Turing (1912-1954) was a British mathematician whose
single life defined the theoretical foundations, the practical
machinery, and the philosophical questions of the discipline now
called computer science. He invented the abstract machine that
bears his name, cracked the Nazi Enigma cipher that shortened World
War II, wrote the paper that founded artificial intelligence, and
devised a mathematical model of biological pattern formation that
remains influential seven decades later. He was also a gay man
prosecuted by the state he had served, driven to an early death,
and posthumously pardoned only after decades of campaigning. His
life is the case study par excellence of how one mind can reshape
multiple fields while being destroyed by the society that benefits
from its work.

## Background

Alan Mathison Turing was born on 23 June 1912 in Maida Vale,
London, the second son of Julius Turing, a civil servant in the
Indian Civil Service, and Ethel Sara Stoney, whose family had
engineering and scientific ties. His parents spent much of their
professional lives in India, and Alan and his brother John were
raised largely in England, fostered with a retired Army couple
during school holidays. This arrangement, common for British
colonial families of the era, meant that Turing spent significant
portions of his childhood separated from his parents -- an
experience that biographers suggest fostered his independence and
his tendency toward solitary intellectual pursuits.

Turing's academic path was unconventional from the start. At
Sherborne School, a traditional English public school, he showed
extraordinary aptitude in mathematics and science while struggling
with Latin and Greek, the classical subjects that formed the core
of the curriculum. His headmaster reportedly criticized his focus
on scientific reading as a distraction from the requirements that
would gain him university entrance. Turing persisted anyway,
conducting independent chemical experiments and winning a school
prize for a mathematical analysis of chemical clock reaction
kinetics -- an early hint of the cross-disciplinary curiosity that
would define his career.

In 1931, Turing entered King's College, Cambridge, to read
mathematics. He graduated with a distinguished degree in 1934 and
was elected a Fellow of King's College in 1935 on the strength of
a dissertation on the central limit theorem -- a result in
probability theory that would have constituted a respectable
career for a lesser mathematician. But Turing's most consequential
work was about to begin, triggered by a question that had haunted
mathematics since the late 1920s.

The question was the Entscheidungsproblem, or "decision problem,"
posed by David Hilbert. Hilbert, the towering figure of early
twentieth-century mathematics, had asked whether there exists a
definite mechanical procedure -- an algorithm -- that could
determine, for any given mathematical statement in a formal
logical system, whether that statement is provable. Hilbert
believed the answer was yes: that mathematics was complete,
consistent, and decidable. Kurt Godel had already shattered the
first two hopes with his incompleteness theorems of 1931, which
showed that any sufficiently powerful formal system contains true
statements that cannot be proved within the system. The question
of decidability remained open.

Turing attacked the Entscheidungsproblem from a direction no one
had tried before. Rather than working within a specific logical
calculus, he asked a more fundamental question: what does it mean
for a procedure to be "mechanical" or "effective" in the first
place? To answer this, he invented an abstract computing device --
a machine that reads and writes symbols on an infinite tape,
moving left or right according to a finite set of rules. This
device, now called the Turing machine, was not a physical machine
but a mathematical model of what any computation essentially is.
Turing argued that any procedure a human could carry out by
following rules mechanically could be carried out by such a
machine. This assertion -- that Turing-machine computability
captures the intuitive notion of effective calculability -- became
known as the Church-Turing thesis, since Alonzo Church at
Princeton had independently arrived at an equivalent conclusion
using his lambda calculus.

Turing's 1936 paper, "On Computable Numbers, with an Application
to the Entscheidungsproblem," contained two revolutionary results.
First, he showed that there exists a single "universal" machine
that can simulate any other Turing machine when given that
machine's description as input on its tape -- the theoretical
blueprint for the stored-program computer. Second, he proved that
no Turing machine can solve the halting problem: there is no
algorithm that can determine, for an arbitrary machine and input,
whether that machine will eventually halt or run forever. This
was the negative answer to Hilbert's Entscheidungsproblem -- the
problem is unsolvable.

The paper brought Turing to the attention of Church, and Turing
travelled to Princeton in 1936 for two years of doctoral study
under Church's supervision. He completed his PhD in 1938 with a
dissertation on ordinal logic, but he had the opportunity to
remain in the United States and chose to return to Britain. That
return placed him at the center of the most urgent applied
mathematics problem of the era: breaking German ciphers.

## Core Concepts

### The Turing Machine and the Definition of Computation

The Turing machine is the single most important abstraction in
computer science. It consists of an infinite tape divided into
cells, each capable of holding one symbol from a finite alphabet;
a read-write head that can examine one cell at a time, write a
symbol, and move left or right; and a finite set of internal
states with transition rules that determine the machine's action
based on the current state and the symbol read. The machine starts
in a designated initial state with some input on the tape and
proceeds step by step until it halts (or runs forever).

The genius of this model is its minimality. Turing stripped
computation down to its barest essentials -- reading, writing,
moving, and changing state -- and showed that this impoverished
apparatus is nonetheless sufficient to compute anything that any
more elaborate model can compute. The Turing machine defines the
boundary of the computable: a function is computable if and only
if a Turing machine exists that can compute it. This definition,
the Church-Turing thesis, has held for nearly a century. Every
model of computation proposed since -- lambda calculus, recursive
functions, register machines, modern programming languages -- has
proven equivalent in power to the Turing machine. The thesis
asserts that this equivalence is not coincidental but reflects a
deep truth about the nature of computation itself.

Turing's model had a second, equally profound implication. The
universal Turing machine -- a single machine that can simulate
any other machine by reading its description from the tape --
established the principle of the stored-program computer. Rather
than building a different physical machine for each task, one
could build one general-purpose machine and feed it different
instructions. This is the architecture of every computer ever
built. Turing identified it in 1936, a decade before the first
electronic stored-program computers were constructed. Ada
Lovelace had glimpsed the generality of computation a century
earlier in her notes on the Analytical Engine, but Turing
provided the rigorous mathematical foundation that made the
concept precise and demonstrable.

### The Halting Problem and the Limits of Computation

Turing did not merely define what can be computed; he proved what
cannot. The halting problem asks: given a description of a Turing
machine and its input, is there an algorithm that can determine
whether the machine will eventually halt or run forever? Turing
proved that no such algorithm exists. The proof uses a diagonal
argument: suppose a halting-detecting machine H exists. Construct
a new machine D that, given input X, uses H to check whether X
halts on input X, and then does the opposite -- if H says X halts,
D loops forever, and if H says X does not halt, D halts. Now feed
D's own description to D. If D halts on D, then H says D halts on
D, so D loops forever -- contradiction. If D does not halt on D,
then H says D does not halt, so D halts -- contradiction. Either
way, the assumption that H exists leads to a contradiction.

This was more than a clever paradox. It established that there
are fundamental limits to what computation can achieve --
boundaries that no amount of cleverness or technological progress
can overcome. The halting problem is the computability-theoretic
analogue of Godel's incompleteness theorems: just as Godel showed
that truth outruns provability in formal systems, Turing showed
that computability outruns the reach of any single algorithm. The
result connects directly to the scientific method's emphasis on
falsifiability: some questions are not merely difficult to answer
but are provably unanswerable by mechanical means. This insight
shaped the philosophy of mathematics, the theory of programming
language semantics, and the understanding of what software can
and cannot do.

### Cryptanalysis and the Bombe

Turing's cryptanalytic work at Bletchley Park was the application
of his theoretical genius to a problem of existential urgency.
The German military encrypted communications using the Enigma
machine, an electromechanical device with rotating rotors that
substituted letters according to a daily-changing key. The number
of possible configurations was astronomical -- on the order of
10^23 for the naval Enigma -- making brute-force attack
impossible by hand or by the calculators of the era.

Polish cryptanalysts had broken Enigma in the 1930s using a
machine called the bomba, but the Germans had added complexity
and the Polish methods were no longer sufficient by 1940. Turing
designed an improved electromechanical machine, the Bombe, that
exploited known weaknesses in German operating procedures --
particularly the practice of encoding message keys twice and the
use of predictable phrases like weather reports. The Bombe
worked by simulating multiple Enigma rotors simultaneously and
rapidly testing configurations against known plaintext fragments
("cribs") until a consistent setting was found. Turing's
statistical approach, later refined with collaborator Gordon
Welchman's diagonal board, made the Bombe dramatically more
efficient.

Turing led Hut 8, the section responsible for German naval
cryptanalysis. The naval Enigma was the hardest variant, and
breaking it was strategically critical because German U-boats
were devastating Atlantic convoys supplying Britain. The
intelligence derived from decrypted Enigma traffic, codenamed
Ultra, gave Allied commanders visibility into German submarine
positions and operational plans. Historians estimate that Ultra
intelligence shortened the war by up to two years and saved
millions of lives. Turing's contribution was not merely the
design of a machine but the development of a systematic
cryptanalytic methodology -- a fusion of mathematical reasoning,
probability theory, and engineering that became the template for
signals intelligence.

### The Turing Test and the Foundations of Artificial Intelligence

In 1950, Turing published "Computing Machinery and Intelligence"
in the journal Mind. The paper opened with a question that
defined a field: "I propose to consider the question, 'Can
machines think?'" Recognizing that the terms "machine" and
"think" were too vague to answer directly, Turing replaced the
question with an operational test. In the "imitation game," a
human judge converses via text with two unseen interlocutors --
one human, one machine. If the judge cannot reliably distinguish
the machine from the human, the machine is said to have passed
the test.

The brilliance of this formulation lies in what it sidesteps.
Rather than defining intelligence (a question philosophers had
failed to resolve for millennia), Turing defined a behavioral
criterion for intelligence that is concrete, testable, and
independent of internal mechanism. This operational approach
became the founding methodological principle of artificial
intelligence: judge intelligence by what a system does, not by
how it does it or what it is made of. Turing anticipated and
rebutted nine classes of objection to machine intelligence --
theological, consciousness ("other minds"), mathematical (the
halting problem means machines have limits), and others --
demonstrating a remarkable prescience about the debates that
would dominate the field for the next seventy years.

The Turing test also established a specific prediction: Turing
wrote that by the year 2000, a computer with sufficient storage
would be able to play the imitation game well enough that an
average interrogator would have less than 70 percent chance of
correctly identifying the machine after five minutes of
conversation. This prediction, made before the first commercial
computer existed, was remarkably calibrated. It shaped the
evaluation criteria for AI systems for decades and connects
directly to the modern challenge of evaluating language model
behavior.

### Reaction-Diffusion Systems and Mathematical Biology

In 1952, Turing published "The Chemical Basis of Morphogenesis"
in the Philosophical Transactions of the Royal Society. The
paper addressed a problem that seemed to belong to biology, not
mathematics: how does a spherical embryo, initially uniform,
develop the asymmetric structures that become organs, limbs, and
body plans? Turing proposed that chemical substances he called
"morphogens" -- signaling molecules that react with each other
and diffuse through tissue -- could spontaneously generate
patterns from an initially homogeneous state. The key insight
was counterintuitive: diffusion, which normally tends to smooth
out concentration differences, can under certain conditions
destabilize a uniform equilibrium and produce stable, periodic
patterns. These "Turing patterns" -- stripes, spots, spirals,
and dappling -- emerge not from any external template but from
the interaction of reaction kinetics and spatial diffusion.

Turing analyzed the mathematics of these reaction-diffusion
systems in detail, working by hand through equations on a ring
of cells and on a sphere. He identified six distinct forms of
instability and suggested biological correlates: tentacle
patterns on Hydra, whorled leaf arrangements, gastrulation, and
animal coat dappling. The paper was decades ahead of its time.
Experimental confirmation of Turing patterns in chemical systems
did not come until 2014, and the biological relevance of the
mechanism remains an active research frontier. That Turing,
in the last two years of his life, opened a new field --
mathematical biology -- with a single paper demonstrates the
range and fertility of his thinking. The work connects to
evolutionary biology and developmental genetics as a model for
how form emerges from process.

## Evidence

### The 1936 Paper and the Founding of Computability Theory

Turing's "On Computable Numbers, with an Application to the
Entscheidungsproblem" (published in the Proceedings of the
London Mathematical Society, 1936-1937) is the founding document
of theoretical computer science. The paper introduced the Turing
machine, the universal machine, and the halting problem in a
single sustained argument. Church reviewed the paper and
acknowledged the superiority of Turing's formulation over his
own lambda-calculus approach, writing that Turing's concept of
computability "has the advantage of making the identification
with effectiveness evident immediately." The Church-Turing
thesis -- the claim that Turing-machine computability captures
the intuitive notion of effective calculability -- was born from
the convergence of these two independent results. The Stanford
Encyclopedia of Philosophy notes that Turing's 1936 paper "gave
a definition of computation and an absolute limitation on what
computation can achieve, which makes it the founding work of
modern computer science."

The paper's influence extends beyond mathematics. The universal
machine concept directly informed the design of the first
electronic stored-program computers in the 1940s. Turing himself
designed the Automatic Computing Engine (ACE) at the National
Physical Laboratory after the war, one of the earliest designs
for a stored-program computer, though the full version was never
built during his tenure. He later joined Max Newman's Computing
Machine Laboratory at the University of Manchester in 1948,
contributing to the Manchester Mark I and its successors. The
path from the 1936 theoretical paper to working hardware runs
through Turing's own hands -- he was both the architect and a
builder of the Information Age.

### Bletchley Park and the Strategic Impact of Ultra

The cryptographic work at Bletchley Park is documented through
declassified intelligence records and the testimony of
colleagues. Turing was recruited to the Government Code and
Cypher School in 1938, before the war began, and moved to
Bletchley Park at the outbreak of hostilities in September 1939.
The Polish cipher bureau had shared its Enigma-breaking methods
and the bomba design with British and French intelligence in
July 1939, providing the foundation on which Turing built.

Turing's Bombe first produced results in 1940, and the
operation scaled dramatically over the course of the war. By
1943, hundreds of Bombes were operating around the clock at
Bletchley Park and at satellite sites in the United States. The
decrypted intelligence, codenamed Ultra, was distributed through
a carefully controlled channel to Allied commanders. The impact
was most dramatic in the Battle of the Atlantic: breaking the
naval Enigma allowed the Allies to reroute convoys around U-boat
wolf packs, dramatically reducing shipping losses. The cognitive
scientist Douglas Hofstadter writes that "it is fair to say we
owe much to Alan Turing for the fact that we are not under Nazi
rule today." The Grokipedia summary of Turing's legacy notes that
historians attribute Ultra intelligence with "accelerating the
war's end by up to two years."

The secrecy surrounding Bletchley Park meant that Turing's
cryptanalytic contributions were not publicly known during his
lifetime. The work was classified, and the thousands of people
who worked at Bletchley Park were bound by the Official Secrets
Act. The full story emerged only in the 1970s and 1980s as
documents were declassified and veterans began to speak. This
secrecy meant that Turing died without public recognition for
his war service -- a fact that adds bitterness to the story of
his persecution.

### The Turing Test and Seventy Years of AI Evaluation

"Computing Machinery and Intelligence" (Mind, October 1950)
introduced the imitation game and established the behavioral
approach to machine intelligence that would define AI research.
The paper considered nine categories of objection to the
proposition that machines can think, ranging from the
theological (only humans have souls) to the mathematical (the
halting problem proves machines have inherent limitations).
Turing addressed each with a combination of logical argument and
pragmatic deflection, demonstrating an intellectual style that
was at once rigorous and playful.

The Turing test has been the subject of sustained philosophical
debate. John Searle's Chinese Room argument (1980) challenged
the test's validity by arguing that passing the test demonstrates
simulation, not understanding. Others have argued that the test
sets the bar too low (a machine could pass by trickery) or too
high (it requires capabilities unrelated to intelligence). But
the test's enduring influence is not as a pass/fail gate but as
a methodological orientation: evaluate machine intelligence by
behavioral criteria, not by introspection about internal states.
This orientation directly shapes modern AI evaluation, where
benchmarks for language models assess performance on tasks that
require human-like reasoning, not claims about the model's inner
experience.

### The Morphogenesis Paper and Its Legacy

"The Chemical Basis of Morphogenesis" (Philosophical
Transactions of the Royal Society B, 1952) introduced
reaction-diffusion systems as a mechanism for biological pattern
formation. The paper was, by Turing's own description, a
"simplification and an idealization, and consequently a
falsification" -- a mathematical model whose value lay in
capturing essential dynamics rather than biological detail. The
model proposed that morphogens -- chemicals that diffuse and
react -- can produce stable spatial patterns from homogeneous
initial conditions through a process now called
diffusion-driven instability.

Experimental confirmation came decades later. In 2014,
researchers reproduced Turing patterns in chemical cells. The
Royal Society commentary on the 1952 paper, published in 2014 to
celebrate the paper's legacy, notes that the formation of
regular structures through activator-inhibitor dynamics "now
appears to have possible relevance not just for developmental
biology but for pure and applied chemistry, geomorphology, plant
biology, ecology, sociology and perhaps even astrophysics." A
2022 Nature Computational Science article on the 70th
anniversary of the paper observes that applications of Turing
patterns have been found in shell patterning, human settlement
dynamics, water filter design, mammalian palate ridge formation,
and even the surface structure of bismuth monolayers on niobium
diselenide. Turing's last major paper, written in the final two
years of his life, opened a research program that is still
expanding.

## Implications

### For Computer Science and the Theory of Computation

Turing's most direct legacy is the entire framework of
theoretical computer science. The Turing machine remains the
standard model of computation; the Church-Turing thesis remains
the foundational assumption of the field. Every analysis of
computational complexity, every proof of undecidability, every
discussion of what algorithms can and cannot do operates within
the framework Turing established in 1936. The halting problem is
not a curiosity but a structural fact that shapes programming
language design (you cannot build a perfect compiler optimizer
that handles all cases), software verification (you cannot build
a tool that proves all programs correct), and artificial
intelligence (certain meta-level questions about agent behavior
are undecidable).

The universal machine concept -- the idea that a single
general-purpose device can simulate any computation -- is the
blueprint for every computer, smartphone, and server on Earth.
This is not a metaphor: the stored-program architecture that
Turing described in 1936 is literally how modern computers
operate. Turing's theoretical work and his postwar hardware
designs (the ACE at the National Physical Laboratory, his work
on the Manchester computers) together constitute the bridge from
abstract mathematics to the information infrastructure of the
modern world. The compounding value of Turing's ideas across
the brain's knowledge base is immense: information theory,
software architecture, large language models, and agent
evaluation all rest on foundations Turing laid.

### For Cryptography and National Security

Turing's cryptanalytic work at Bletchley Park established the
discipline of modern signals intelligence. The methodology he
developed -- combining mathematical analysis, statistical
inference, and electromechanical automation -- became the
template for Cold War and contemporary cryptography. The
Government Communications Headquarters (GCHQ) that Turing
joined after the war grew directly out of Bletchley Park and
remains one of the world's leading signals intelligence
agencies. The National Security Agency in the United States
similarly traces its intellectual lineage to the Bletchley
collaboration.

The strategic impact of Ultra intelligence is a case study in
how abstract mathematics can alter geopolitical outcomes. Turing
was a mathematician who had no military training, no interest in
soldiering, and no prior experience in cryptography. Yet his
theoretical work on computation gave him the mental tools --
algorithmic thinking, formal models, the ability to reason about
symbol manipulation -- that made him the most effective
codebreaker of the war. The connection between Turing's
theoretical and applied work illustrates a broader pattern: the
deepest practical innovations often emerge from the deepest
theoretical foundations, not from applied research aimed
directly at a problem.

### For Artificial Intelligence and Cognitive Science

Turing's 1950 paper founded the field of artificial intelligence
six years before the Dartmouth workshop that formally named it.
The behavioral, operational approach to intelligence that Turing
proposed -- judge by what a system does, not by what it is --
remains the default methodology of AI evaluation. Modern
benchmarks for language models, agent systems, and automated
reasoning tools are all descendants of the Turing test in
spirit: they assess performance on tasks that require
intelligence, not claims about consciousness or understanding.

The philosophical questions Turing raised are unresolved and
arguably more pressing than ever. If a language model can
produce text indistinguishable from human writing, does that
constitute intelligence? Searle's Chinese Room and subsequent
arguments suggest that behavioral equivalence does not imply
understanding. But Turing's response -- that we judge other
humans' intelligence behaviorally, since we cannot access their
internal states -- remains a powerful counter. The tension
between these positions defines the contemporary debate over
machine consciousness, AI safety, and the evaluation of
increasingly capable systems. For anyone working with
autonomous agents, Turing's questions are not historical
curiosities but live design constraints: how do you know an
agent is behaving intelligently, and what does that mean?

### For Ethics, Justice, and the Social Context of Science

Turing's prosecution in 1952 for "gross indecency" -- the legal
term for homosexual acts, then a criminal offense in Britain --
and his subsequent chemical castration and death from cyanide
poisoning in 1954 constitute one of the most infamous cases of
a society destroying the person it most needed. Turing had been
convicted after admitting a sexual relationship with a man; the
conviction cost him his security clearance, ended his government
work, and subjected him to estrogen injections intended to
suppress his libido. He died on 7 June 1954, aged 41, with a
half-eaten apple laced with cyanide beside him. The inquest
ruled suicide, though some biographers note the evidence is also
consistent with accidental poisoning from a chemical experiment.

The posthumous recognition was slow. A public campaign beginning
in 2009 led Prime Minister Gordon Brown to issue an official
apology. Queen Elizabeth II granted a royal pardon on 24
December 2013, fifty-nine years after Turing's death. The
"Turing Law" of 2017 extended posthumous pardons to
approximately 50,000 other men convicted under the same gross
indecency statutes. Turing's face appeared on the British 50
pound note in 2021.

The ethical lesson is not merely that injustice was done -- it
was -- but that the social and legal context in which science
operates can destroy the very people who advance it. Turing's
genius did not protect him from the state; his service did not
earn him tolerance. The lesson compounds across the brain's
knowledge base: scientific achievement is not separable from
the social conditions that enable or destroy it. The history of
science is also the history of who is allowed to do science, and
what happens to those who transgress the boundaries their
society draws.

## Sources

1. Turing, A. M. (1936). "On Computable Numbers, with an
   Application to the Entscheidungsproblem." Proceedings of the
   London Mathematical Society, s2-42(1), 230-265.
   https://doi.org/10.1112/plms/s2-42.1.230 [high]

2. Turing, A. M. (1950). "Computing Machinery and Intelligence."
   Mind, LIX(236), 433-460.
   https://doi.org/10.1093/mind/LIX.236.433 [high]

3. Turing, A. M. (1952). "The Chemical Basis of Morphogenesis."
   Philosophical Transactions of the Royal Society of London B,
   237(641), 37-72.
   https://doi.org/10.1098/rstb.1952.0012 [high]

4. Hodges, A. "Alan Turing." Stanford Encyclopedia of Philosophy.
   https://plato.stanford.edu/entries/turing/ [high]

5. "Alan Turing." Encyclopaedia Britannica.
   https://www.britannica.com/biography/Alan-Turing [high]

6. "Alan Turing." Wikipedia.
   https://en.wikipedia.org/wiki/Alan_Turing [high]

7. Ball, P. (2014). "Forging patterns and making waves from
   biology to geology: a commentary on Turing (1952)." Phil.
   Trans. R. Soc. B, 369.
   https://doi.org/10.1098/rstb.2014.0218 [high]

8. Anon. (2022). "Turing patterns, 70 years later." Nature
   Computational Science.
   https://www.nature.com/articles/s43588-022-00306-0 [high]

9. "The Church-Turing Thesis." Stanford Encyclopedia of
   Philosophy.
   https://plato.stanford.edu/entries/church-turing/ [high]

10. "Royal pardon for codebreaker Alan Turing." BBC News, 24
    December 2013.
    https://www.bbc.com/news/technology-25495315 [medium]

11. Grokipedia. "Alan Turing."
    https://grokipedia.com/page/Alan_Turing [medium]

## See Also

- `library/notable-people/ada-lovelace.md` -- the other foundational
  figure of computing biography; Lovelace saw the generality of
  computation a century before Turing formalized it.
- `library/history/world-war-ii.md` -- the strategic context for
  Turing's cryptanalytic work at Bletchley Park and the Ultra
  intelligence operation.
- `library/mathematics-statistics/information-theory.md` -- the
  mathematical framework that, alongside computability theory,
  defines the theoretical limits of communication and computation.
- `library/coding-agentic-ai/agent-evaluation-and-benchmarking.md`
  -- the modern descendant of Turing's behavioral approach to
  evaluating machine intelligence.
- `library/science/scientific-method-falsifiability.md` -- Turing's
  halting problem connects to the epistemological limits of what
  can be known and proven by mechanical means.
- `library/notable-people/richard-feynman.md` -- a contemporary
  scientist whose philosophy of intellectual honesty complements
  Turing's operational approach to difficult questions.