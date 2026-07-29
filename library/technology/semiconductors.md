---
name: semiconductors
id: 20260729T073337Z
tier: library-topic
domain: technology
author: Researcher-1
tags: [semiconductors, transistors, moores-law, chip-fabrication, tsmc, lithography, integrated-circuits, ai-chips]
links: [library/technology/large-language-models.md, library/technology/cloud-computing.md]
---

# Semiconductors -- The Most Complex Manufacturing Achievement in Human History Underpins Everything Digital

Semiconductors are materials with electrical conductivity between that
of a conductor and an insulator, and they are the physical foundation
of every digital device on Earth. By precisely controlling the flow of
electricity through silicon doped with impurities, engineers build
transistors -- tiny switches that form logic gates, the building blocks
of all computation. The extraordinary concentration of advanced
semiconductor manufacturing in a single company (TSMC) on a single
island (Taiwan) has made chip fabrication the most geopolitically
sensitive technology of the twenty-first century, triggering hundreds
of billions of dollars in government subsidies to redistribute
production capacity.

## Background

The semiconductor age began in 1947 at Bell Labs when John Bardeen,
Walter Brattain, and William Shockley demonstrated the first
point-contact transistor, replacing the bulky, fragile vacuum tube
with a solid-state switch. Silicon quickly emerged as the preferred
substrate -- abundant, stable, and capable of forming a high-quality
insulating oxide layer. The breakthrough that enabled mass adoption
came in 1958-1959 when Jack Kilby at Texas Instruments and Robert
Noyce at Fairchild Semiconductor independently invented the integrated
circuit: multiple transistors fabricated together on a single piece of
silicon.

In 1965, Gordon Moore, then director of R&D at Fairchild and later
co-founder of Intel, published a four-page article in Electronics
magazine observing that the number of components on integrated circuits
had doubled roughly every year and predicted this would continue for at
least a decade. In 1975 he revised the cadence to approximately every
two years. This observation -- Moore's Law -- became the organizing
principle of the semiconductor industry for half a century. It was
never a physical law; it was an economic prediction that became a
self-fulfilling prophecy through concentrated engineering effort and
capital investment.

The industry evolved along two axes. The first was the relentless
shrinking of transistor dimensions, measured in process nodes named
after the minimum feature size: from 10,000 nanometers in the early
1970s to 3 nanometers in volume production by 2023. The second was the
vertical disintegration of the industry. In 1987, Morris Chang founded
the Taiwan Semiconductor Manufacturing Company (TSMC) as a pure-play
foundry -- a company that only manufactures chips designed by others.
This "fabless" model separated chip design (Qualcomm, AMD, Nvidia,
Apple) from fabrication, enabling fabless companies to access the best
manufacturing without building their own billion-dollar factories.

Dennard Scaling, the principle that as transistors shrink their power
density stays constant, held from roughly 1974 to 2004. When it broke
down, clock speeds stopped doubling and the industry pivoted to
multi-core architectures and energy efficiency. Today, the physical
limits of silicon scaling are approaching the atomic level: at
dimensions below roughly 1 nanometer, quantum tunneling causes
electrons to leak through barriers that classical physics says should
contain them.

## Core Concepts

### The Physics of Semiconductors

Pure silicon is a poor conductor. Its atoms form a crystal lattice
where each silicon atom shares four valence electrons with its
neighbors, leaving no free charge carriers. Doping -- the deliberate
introduction of impurity atoms -- changes this. Adding phosphorus or
arsenic (group V elements with five valence electrons) creates n-type
silicon with extra free electrons. Adding boron (a group III element
with three valence electrons) creates p-type silicon with "holes" --
absences of electrons that behave as positive charge carriers.

The fundamental device is the metal-oxide-semiconductor field-effect
transistor (MOSFET). A MOSFET has three terminals: source, drain, and
gate. The gate sits on top of a thin insulating layer (the oxide)
above the channel between source and drain. Applying a voltage to the
gate creates an electric field that either attracts charge carriers
into the channel (turning the transistor on) or repels them (turning
it off). This makes the transistor a voltage-controlled switch -- the
basis of digital logic.

### From Transistors to Logic Gates to Processors

A single transistor by itself is just a switch. Combining transistors
in specific configurations creates logic gates:

- A NOT gate (inverter): one transistor. When input is high, the
  transistor conducts and pulls output low. When input is low, output
  is pulled high.
- A NAND gate: two transistors in series. Output is low only when both
  inputs are high.
- A NOR gate: two transistors in parallel. Output is low when either
  input is high.

CMOS (Complementary MOS) technology pairs n-type and p-type transistors
so that current flows only during switching transitions, dramatically
reducing power consumption. From these primitive gates, engineers build
flip-flops (memory cells), adders, multipliers, and ultimately complete
processor cores containing billions of transistors.

### Moore's Law and Its Limits

Moore's Law drove a 50-year exponential improvement unprecedented in
industrial history. The Intel 4004 (1971) had 2,300 transistors. The
Apple M2 Ultra (2023) has 134 billion -- a factor of roughly 58
million. This scaling enabled computers to move from room-sized
machines serving institutions to devices carried in pockets that are
millions of times more powerful.

However, Moore's Law is confronting fundamental limits:

1. **Quantum tunneling:** At gate lengths approaching 1-2 nm, electrons
   can tunnel through the gate oxide even when the transistor is
   "off," creating leakage current that wastes power and corrupts
   signals.

2. **Thermal dissipation:** The heat generated per unit area -- the
   "power wall" -- has become the primary design constraint. Modern
   data center chips dissipate hundreds of watts and require
   sophisticated liquid cooling. A hypothetical 0.2 nm transistor
   would generate heat density high enough to melt interconnects.

3. **Economic limits:** A leading-edge fabrication plant now costs
   approximately $25-30 billion. Only three companies remain capable
   of advanced-node manufacturing: TSMC, Samsung, and Intel. The
   economics of Moore's Law -- "Moore's Second Law" or Rock's Law --
   states that the cost of a fab doubles roughly every four years.

By 2016, the semiconductor industry's own International Technology
Roadmap for Semiconductors (ITRS) had abandoned Moore's Law as a
planning guide. The industry consensus is that traditional 2D CMOS
scaling will plateau by approximately 2030, with further gains coming
from 3D stacking (vertical integration), heterogeneous integration
(combining different chip types in one package), and domain-specific
architectures rather than smaller transistors.

### The Fabrication Process

Semiconductor fabrication is arguably the most complex manufacturing
process ever developed. A modern chip requires hundreds of process
steps across three to four months, executed in cleanrooms a thousand
times cleaner than a hospital operating room. A single dust particle
can destroy an entire wafer worth millions of dollars.

The chain begins with purified silicon grown into a single crystal
ingot, sliced into wafers, and polished to atomic smoothness. The
critical patterning step is photolithography. A photosensitive chemical
(photoresist) is applied to the wafer. Light is projected through a
mask containing the circuit pattern, and the exposed (or unexposed,
depending on resist type) photoresist is washed away. The wafer is then
etched -- exposed to plasma that removes material where photoresist is
absent -- or subjected to ion implantation to dope specific regions.
The remaining photoresist is stripped, and the process repeats with the
next mask layer. A modern processor may require 80 or more mask layers.

The resolution limit of lithography is determined by the Rayleigh
criterion: minimum feature size is proportional to the wavelength of
light used divided by the numerical aperture of the lens system. For
decades, the industry shortened wavelengths: from visible light to
ultraviolet (UV) at 365 nm, to deep ultraviolet (DUV) at 248 nm and
then 193 nm. The current frontier is extreme ultraviolet (EUV)
lithography at 13.5 nm wavelength, a technology so difficult that it
took over 20 years and an estimated $10+ billion in R&D to
commercialize.

EUV light is produced by vaporizing tin droplets with a high-powered
carbon dioxide laser to create a plasma that emits at 13.5 nm. Because
EUV light is absorbed by air and by conventional lenses, the entire
system operates in a vacuum using reflective mirrors rather than
transmissive lenses -- each mirror requiring atomic-level precision.
ASML, a Dutch company, is the world's sole supplier of EUV lithography
systems. Each machine costs approximately $200-400 million, contains
over 100,000 parts, and requires 40 freight containers to ship. ASML
produces only a few dozen per year.

After lithography and etching, additional steps include deposition
(adding layers of insulating or conducting material), chemical
mechanical polishing (planarizing the surface for the next layer),
and metallization (creating the wiring that connects transistors).
Process control is statistical: at advanced nodes, thousands of
parameters must be maintained within nanometer tolerances, and the
yield -- the fraction of chips on a wafer that function correctly --
determines economic viability.

### The Foundry Model and Industry Structure

The semiconductor industry has stratified into:

- **Fabless design companies** (Nvidia, AMD, Qualcomm, Apple, Broadcom):
  design chips but do not manufacture them. This is the dominant model
  for advanced logic chips, representing roughly 50% of the value
  added in the semiconductor chain on only 13% of the capital
  expenditure.

- **Foundries** (TSMC, Samsung Foundry, GlobalFoundries): manufacture
  chips designed by others. TSMC alone controls approximately 90% of
  the world's advanced-process (sub-7 nm) manufacturing capacity and
  roughly 60% of total foundry revenue.

- **Integrated Device Manufacturers** (Intel, Samsung): design and
  manufacture their own chips. Intel historically led in process
  technology but lost its lead to TSMC in the 2017-2020 period, a
  shift with enormous strategic consequences.

- **Equipment suppliers**: ASML (lithography), Applied Materials, Lam
  Research, Tokyo Electron, and KLA provide the machines used in fabs.
  This layer is also highly concentrated; ASML's EUV monopoly is the
  most extreme example.

- **Electronic Design Automation (EDA)** : Synopsys and Cadence provide
  the software tools used to design chips. Designing a modern chip
  without EDA tools is effectively impossible.

## Evidence

### Moore's Law in Practice: A Half-Century of Exponential Growth

The empirical record of transistor scaling is one of the most
documented phenomena in industrial history. In 1971, Intel's 4004
processor contained 2,300 transistors on a 10,000 nm process. By 2023,
Apple's M2 Ultra contained 134 billion transistors on a 5 nm process,
and Nvidia's H100 GPU contained 80 billion transistors on a custom 4
nm process. The GB202 graphics processor shipped in 2025 with over 92
billion transistors.

The rate of scaling has demonstrably slowed. From 1995 to 2005,
transistor density doubled roughly every 24 months. From 2010 to 2020,
the cadence stretched to approximately 30-36 months. Intel's own CEO
acknowledged that transistor doubling now occurs closer to every three
years. TSMC and Samsung, however, have sustained a faster pace:
TSMC moved from 7 nm (2018 risk production) to 5 nm (2020) to 3 nm
(2022-2023 volume production) and announced 2 nm for 2025.

### The Cost Escalation

The economics of advanced manufacturing tell a stark story. A 200 mm
wafer fab in the 1990s cost approximately $1-2 billion. A 300 mm fab
for the 90 nm node cost roughly $3-4 billion. A 3 nm fab today costs
an estimated $20-30 billion. TSMC's capital expenditure reached $36.3
billion in 2022, $30.4 billion in 2023, and was projected at $30-32
billion in 2024 -- exceeding the GDP of many countries. A single
High-NA EUV lithography tool from ASML costs approximately $380 million
and TSMC is reported to operate over 100 EUV systems. These costs have
reduced the number of companies capable of leading-edge manufacturing
from roughly 25 in the early 2000s to three today, and arguably two at
the most advanced nodes (TSMC and Samsung).

### The Geopolitics of Concentration

Taiwan's dominance in advanced semiconductor manufacturing has been
quantified by multiple government and academic sources. According to
the Congressional Research Service and Boston Consulting Group, Taiwan
produces more than 90% of the world's most advanced logic chips
(sub-10 nm), with TSMC alone accounting for virtually all of this
capacity. A 2021 BCG/SIA study estimated that a year-long disruption
of Taiwan's semiconductor supply could cost the global electronics
industry approximately $500 billion in lost revenue. A disruption
extending beyond a year would reset the global technology industry.

The United States, which invented the integrated circuit and once
accounted for 37% of global semiconductor manufacturing capacity in
1990, had dropped to approximately 12% by 2020. In response, the U.S.
CHIPS and Science Act of 2022 allocated $52.7 billion in subsidies to
rebuild domestic manufacturing capacity. TSMC committed over $65
billion to build three fabs in Arizona spanning 4 nm to 2 nm
processes. Samsung is building a $17 billion fab in Texas. Intel is
building new fabs in Ohio and Arizona with CHIPS Act support. The
European Union passed its own European Chips Act targeting 20% of
global production capacity by 2030. Japan, South Korea, and India
have all launched major subsidy programs.

### The AI Chip Boom and Supply Chain Stress

The launch of ChatGPT in late 2022 triggered an extraordinary surge
in demand for AI accelerators -- specialized chips designed for the
matrix multiplications that dominate neural network computation.
Nvidia's data center revenue grew from $3.6 billion in Q1 2023 to over
$22 billion in Q1 2025. This demand cascaded through the semiconductor
supply chain:

- **CoWoS advanced packaging** became the primary bottleneck. TSMC's
  Chip-on-Wafer-on-Substrate (CoWoS) technology integrates logic dies
  with High-Bandwidth Memory (HBM) stacks on a silicon interposer,
  essential for AI chips. CoWoS capacity grew at roughly 80% CAGR from
  2024 to 2026 (from ~35,000 to ~130,000 wafers per month) yet still
  fell short of demand. Nvidia reserved over 60% of total CoWoS
  capacity for 2025-2026, leaving AMD, Google, Amazon, and others
  competing for the remainder.

- **TSMC 3 nm lead times** exceeded 50 weeks by early 2026, with
  capacity fully allocated 18-24 months in advance. Wafer prices at
  3 nm reached approximately $20,000 per wafer -- roughly 1.8 times
  the cost of a mature 7 nm wafer.

- **HBM memory** became the bottleneck after CoWoS eased in 2025.
  SK Hynix, Samsung, and Micron produce HBM, and Nvidia consumed an
  estimated 75% of global HBM supply by late 2025.

Total spending on AI chip components (logic, HBM, packaging) across the
top four designers (Nvidia, AMD, Google, Amazon) more than doubled from
$22 billion in 2024 to an estimated $52 billion in 2025, according to
Epoch AI's chip component analysis.

### Beyond Silicon: The Post-Moore Roadmap

As traditional scaling approaches physical limits, the industry is
pursuing multiple paths forward. Gate-All-Around (GAA) transistors,
where the gate surrounds the channel on all four sides for better
electrostatic control, replaced FinFET at the 3 nm/2 nm boundary
(TSMC calls this "nanosheet" technology). Backside power delivery,
which moves power rails to the back of the wafer to free routing space
on the front, is entering production at 2 nm and below. After that,
complementary FET (CFET) technology stacks n-type and p-type
transistors vertically rather than side-by-side.

Beyond the CMOS roadmap, research continues into carbon nanotubes,
graphene, transition metal dichalcogenides (TMDs), and photonic
computing -- each promising to bypass silicon's physical limits but
none yet at commercial scale. In the near term, the most impactful
advances are coming from architectural innovation: chiplet-based
designs (AMD's approach), 3D V-Cache (stacking additional cache dies
vertically), and domain-specific architectures like Google's TPUs
that optimize for specific workloads rather than general-purpose
computation.

## Implications

### For Technology and Innovation

The semiconductor is not just one technology among many -- it is the
enabling technology for essentially all modern computation. Every
smartphone contains chips fabricated at advanced nodes. Every AI
model runs on GPUs or TPUs that depend on semiconductor scaling. The
pace of progress in AI, scientific computing, autonomous vehicles,
robotics, and consumer electronics is gated by semiconductor
capability. When Moore's Law slows, every downstream technology that
depends on cheaper, faster computation slows with it.

The shift from general-purpose scaling to domain-specific architectures
has important second-order effects. It means that hardware is becoming
specialized for specific workloads -- AI training, AI inference, video
transcoding, networking -- which in turn means that software must be
written to exploit specific hardware. The era when any program would
automatically run faster on next year's processor is ending. This
raises the stakes for software-hardware co-design and favors
vertically integrated companies (Apple, Google, Amazon) that control
both the chip and the software stack.

### For Geopolitics and National Security

Semiconductors have become a first-order national security concern.
Advanced chips are used in weapons systems, intelligence gathering,
and cyber operations. The ability to manufacture advanced chips
domestically is now viewed by the United States, China, the EU, Japan,
and India as a strategic necessity rather than a commercial
consideration. The U.S. has imposed escalating export controls on
advanced chips and semiconductor manufacturing equipment to China
since 2022, extending to "compute ceiling" limits on AI training chips
and restrictions on equipment sold by third-country companies.

China, cut off from advanced EUV lithography tools and leading-edge
chips, has responded with a whole-of-nation effort toward
self-sufficiency, including massive state investment through the "Big
Fund" (China Integrated Circuit Industry Investment Fund). However,
the gap between China's domestic capability (currently limited to a
reported 7 nm equivalent using older DUV tools through multi-patterning)
and TSMC's leading edge (2 nm entering risk production) remains
substantial and may take a decade or more to close without access to
EUV.

Taiwan's position as the linchpin of global semiconductor manufacturing
creates what strategists call the "silicon shield" -- the theory that
China would hesitate to invade Taiwan because doing so would destroy
the chip fabrication capacity on which China's own technology industry
(and the broader global economy) depends. Whether this deterrence
calculus holds in a crisis is one of the most consequential
unanswered questions in contemporary geopolitics.

### For Investment and Business Strategy

The semiconductor industry's extreme capital intensity and
concentration create unique dynamics. Because building a fab takes
3-5 years and tens of billions of dollars, supply and demand are
perpetually out of phase. Semiconductor cycles -- periods of shortage
followed by oversupply -- have been a feature of the industry since
its inception. The AI boom has compressed lead times to unprecedented
levels and created pricing power for TSMC that is historically unusual
in the foundry business.

The CHIPS Act and equivalent international programs are reshaping the
geographic distribution of capacity, but the effectiveness of these
programs remains uncertain. Building a fab is one thing; operating it
competitively is another. TSMC's Arizona fab has faced delays, labor
shortages, and cultural friction between Taiwanese management and
American workers. The fundamental question is whether advanced
semiconductor manufacturing can be replicated outside of the dense
ecosystem of suppliers, talent, and infrastructure that has
accumulated in Taiwan over four decades.

For individual companies, access to leading-edge capacity is becoming a
source of competitive advantage. Companies that can secure capacity
allocations at TSMC's most advanced nodes (Apple, Nvidia, AMD) can ship
products that competitors cannot match. This dynamic creates a
power-law distribution of outcomes in which being a preferred customer
of TSMC is worth billions. The 3 nm supply constraint has made
semiconductor fabrication allocation a boardroom-level concern at the
world's largest technology companies.

## Sources

1. Moore, G. (1965). "Cramming More Components onto Integrated
   Circuits." Electronics, 38(8), 114-117.
   https://processorhistory.com/moores-law/ [high]

2. TSMC. "Logic Technology." Official TSMC technology portfolio.
   https://www.tsmc.com/english/dedicatedFoundry/technology/logic
   [high]

3. Congressional Research Service. (2023). "Semiconductors and the
   CHIPS Act: The Global Context." CRS Report R47558.
   https://www.congress.gov/crs-product/R47558 [high]

4. ASML. "Lithography Principles" and "Our History."
   https://www.asml.com/en/technology/lithography-principles
   https://www.asml.com/en/company/about-asml/history [high]

5. Epoch AI. (2026). "AI Chip Supply Chain Bottlenecks and Capacity."
   https://epoch.ai/latest/introducing-the-ai-chip-components-explorer
   [medium]

6. Markakis, M.G. (2025). "TSMC: Lessons in Strategy and Operational
   Excellence from the World's Most Important Company." IESE Insight.
   https://www.iese.edu/insight/articles/tsmc-geopolitics-operations-strategy/
   [medium]

7. Chen, H.-Y. (2026). "Taiwan Semiconductor Geopolitical Risk 2026:
   TSMC and the Chip War."
   https://www.hungyichen.com/en/insights/semiconductor-geopolitics
   [medium]

8. Mehta, A. (2026). "The Packaging Bottleneck: Why TSMC's CoWoS
   Lines -- Not Its Fabs -- Now Control AI Chip Supply." Next Waves
   Insight.
   https://nextwavesinsight.com/tsmc-advanced-packaging-nvidia-ai-supply-chain-2026
   [medium]

## See Also

- `library/technology/large-language-models.md` -- the AI systems
  whose training and inference depend entirely on semiconductor
  scaling and create the demand driving the current chip boom.
- `library/technology/cloud-computing.md` -- the data center
  infrastructure built on semiconductors that delivers computation
  as a utility.
