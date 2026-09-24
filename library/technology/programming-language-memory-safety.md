---
name: programming-language-memory-safety
id: 20260924T180449Z
tier: library-topic
domain: technology
author: Librarian
tags: [memory-safety, programming-languages, ownership, type-systems, garbage-collection, rust, secure-software]
links: [library/technology/cybersecurity-principles-threats-and-defense-in-depth.md, library/technology/software-architecture-patterns-principles.md, library/technology/software-supply-chain-security-and-sboms.md]
---

# Programming-Language Memory Safety Prevents Whole Bug Classes but Does Not Remove Software Risk

Programming-language memory safety prevents programs from accessing memory outside permitted bounds or after its valid lifetime by enforcing invariants in the language, compiler, runtime, or a combination of them [1][3][5]. Ownership and borrowing, managed runtimes, bounds checks, and type systems can therefore prevent broad classes of buffer, lifetime, and data-race defects, but unsafe escape hatches, foreign code, dependencies, logic errors, and flawed authorization remain outside or at the edge of those guarantees [4][6][7][11]. The practical objective is not to rewrite everything at once; it is to stop creating new memory-unsafe code, isolate unavoidable unsafe boundaries, and migrate the highest-risk legacy components with evidence that the resulting system preserves both safety and required performance [2][5][8][9].

## Background

Memory safety concerns whether a program accesses memory only in ways that are valid for the object, operation, and time involved. A spatial error crosses an allocation boundary, as when a write extends past the end of a buffer. A temporal error uses storage at the wrong time, as when code dereferences a pointer after the referenced object has been freed. Related failures include uninitialized reads, double frees, invalid pointer arithmetic, and type confusion. These errors can corrupt data, crash a process, disclose adjacent information, or redirect execution when an attacker can control the corrupted state [1][2][3][5].

The problem is rooted in a useful but hazardous programming model. C and C++ let programmers represent addresses directly, compute with pointers, choose allocation strategies, and control object lifetimes with little mandatory runtime machinery. That control supports operating systems, device interfaces, embedded software, browsers, and other resource-sensitive systems, but the language generally relies on the programmer and supporting tools to preserve bounds, initialization, aliasing, and lifetime invariants. A locally plausible operation can therefore become undefined behavior when a pointer is stale, a length is wrong, two aliases mutate the same storage, or an interface describes the memory differently on each side [1][2][5][10].

Decades of engineering have made memory-unsafe software harder to exploit without eliminating the root defects. Compilers and operating systems can add stack canaries, non-executable memory, address-space layout randomization, control-flow integrity, hardened allocators, and sanitizers. Static analysis, dynamic analysis, code review, and fuzzing can find many defects before release. These controls are valuable defense in depth, but they either search for examples, constrain an exploit after a defect exists, or impose continuing testing and operational work. CISA's roadmap report documents bypasses and limits across several mitigations, while Microsoft's security-response team reported that extensive tools, training, reviews, and compiler improvements had not displaced memory-safety issues as a persistent share of its assigned vulnerabilities [2][10].

The prevalence data explain the shift from defect discovery toward defect prevention. Microsoft reported that approximately 70 percent of the vulnerabilities to which it assigned CVEs each year remained memory-safety issues across the period summarized in 2019. CISA's multi-agency roadmap also cites roughly 70 percent for Microsoft and Chromium, 32 of 34 critical or high Mozilla bugs in one analysis, and 67 percent of Project Zero's 2021 zero-days [2][10]. These figures describe different products, periods, reporting rules, and severity populations, so they should not be combined into one universal rate. They nevertheless show the same repeated pattern: in large C and C++ codebases, memory errors constitute a material and often severe vulnerability class [1][2][10].

A memory-safe language changes where the obligation is enforced. Instead of asking every feature developer to remember every rule on every path, the language implementation rejects or traps invalid memory operations, manages object lifetimes, or restricts which references can coexist. NSA describes this as protection supplied by inherent compile-time and runtime checks rather than by application code that each programmer must add correctly. Examples include managed languages such as C#, Java, Go, Python, Ruby, and Swift, as well as Rust, which targets low-level systems work through compile-time ownership and borrowing rather than a tracing garbage collector [1][5][6].

No single mechanism defines every memory-safe language. Managed runtimes usually retain information about objects, enforce type and bounds rules, and reclaim unreachable storage automatically. Other systems use reference counting or ownership rules to determine when storage can be reclaimed. Rust associates values with owners, permits temporary borrows under lifetime and aliasing rules, and limits operations that the compiler cannot prove safe to explicit `unsafe` regions. The common result is a default programming model in which ordinary well-typed code cannot freely create dangling references or unchecked out-of-bounds accesses, although the exact guarantees, failure behavior, and runtime costs differ by language and implementation [5][6][11][12].

The policy shift followed technical and operational evidence. NSA recommended a strategic move toward memory-safe languages in its 2023 guidance. CISA, NSA, the FBI, and international partners then called for public memory-safety roadmaps in December 2023. The White House Office of the National Cyber Director identified programming languages as a high-leverage software building block in 2024, and NSA and CISA published broader adoption guidance in 2025 covering mechanisms, incremental migration, tools, training, and organizational constraints [1][2][3][5]. These documents do not establish that one language fits every product. They establish that language choice is a security architecture decision rather than merely a matter of syntax or developer taste [2][3][5].

This topic concerns language-level engineering: what memory safety guarantees mean, how ownership and managed runtimes provide them, where foreign-function and unsafe boundaries weaken them, and how legacy systems can migrate incrementally. General threat governance and incident response belong in the broader cybersecurity topic; component provenance and dependency inventory belong in the software supply-chain topic; and general modularity and interface design belong in the software-architecture topic. Hardware tagging and capability architectures are relevant complementary controls, but they are not substitutes for examining the programming-language boundary and are not the primary subject here [2][3].

## Core Concepts

### Spatial and temporal safety are separate invariants

Spatial safety requires each read or write to stay within the memory region that the program is authorized to access. A classic buffer overflow violates that rule by using a length or index that extends beyond an allocated array. Language implementations can enforce the invariant with bounds-checked arrays and slices, safe iterator APIs, type layouts that carry lengths, and restrictions on converting integers into freely dereferenceable pointers. An invalid access may be rejected at compile time or detected at runtime before the memory operation occurs. The check prevents the out-of-bounds access; it does not prove that the chosen in-bounds element was logically correct [1][3][5].

Temporal safety requires a reference to remain valid for every use. Use-after-free violates the rule because storage has been reclaimed and may already hold another object. Double free corrupts the allocator's view of ownership by reclaiming the same storage twice. Managed runtimes address much of this problem by retaining objects while they remain reachable. Ownership systems address it by controlling who may dispose of a value and by ensuring that borrowed references do not outlive the owner. The mechanisms differ, but both make lifetime a language or runtime property instead of an undocumented convention between callers [1][5][6].

Initialization and type validity add related constraints. A program should not read bytes as a value before that value has been initialized, and it should not reinterpret storage as an incompatible type unless the language defines the conversion. Safe constructors, definite-initialization analysis, tagged variants, and restricted casts reduce the states that ordinary code can express. The author's synthesis is that memory safety is best understood as a family of enforceable invariants over address, extent, lifetime, initialization, type, and concurrent access rather than as one check called "safe" [1][5][11].

### Managed runtimes trade explicit lifetime control for automatic reclamation

A tracing garbage collector begins from a set of roots, discovers objects that remain reachable, and reclaims storage that is no longer reachable. This prevents ordinary managed-code references from pointing to objects that the runtime has already reclaimed. Runtime array bounds checks and type checks cover spatial and representation rules. Java, C#, Go, Python, and other managed environments differ substantially in compilation, object models, collection algorithms, pause behavior, and foreign interfaces, but each moves important lifetime work from application code into a shared language implementation [1][5].

The trade-off is not simply "safe but slow." A managed runtime can optimize allocation, move objects, collect concurrently, or compile frequently executed code, while an application gains simpler shared-object graphs and a mature library ecosystem. The costs can include larger runtime and memory footprints, unpredictable or workload-dependent collection latency, less direct control over object placement, and dependence on runtime availability. CISA's roadmap specifically notes that garbage collection can introduce latency and CPU or memory costs that matter in constrained or time-sensitive systems [2]. The correct comparison is therefore workload-specific: throughput, tail latency, memory ceiling, startup, binary size, platform support, and operational predictability all matter [2][5].

Reference counting is another automatic lifetime technique. It reclaims an object when its ownership count falls to zero, making many destruction points more predictable than tracing collection. It also imposes count-update costs and cannot by itself reclaim strongly connected cycles. Languages and libraries can combine reference counting with weak references, cycle detection, arenas, or tracing. The author's assessment is that these techniques should be evaluated as different lifetime policies, not arranged on a universal ladder from manual to managed [5][11].

### Ownership and borrowing encode lifetime and aliasing in the type system

Rust's model assigns each value an owner and normally reclaims the value when that owner leaves scope. Moving a value transfers ownership rather than silently leaving two independent owners. Borrowing permits temporary references without transferring the value: a shared reference permits access under rules that prevent conflicting mutation, while a mutable reference requires exclusive access for its lifetime. Lifetimes connect the validity of a reference to the resource from which it was borrowed, allowing the compiler to reject many dangling-reference patterns before execution [6][11].

The model also links memory safety to concurrency. Rust restricts which types can cross or be shared across threads through type properties such as `Send` and `Sync`, and its aliasing discipline rules out ordinary unsynchronized mutable access in safe code. RustBelt formalized a realistic core of this design and proved that semantically well-typed programs in its model avoid invalid memory accesses and data races. That result supports the architecture of ownership-based safety, but it is not a proof of every compiler version, library, platform, or line of real-world Rust [6].

Compile-time enforcement shifts costs as well as risks. Ownership can avoid a general tracing collector and preserve explicit control over allocation and destruction, making it suitable for latency-sensitive and low-level components. It can also reject programs that a human can see are safe when the compiler cannot establish the necessary lifetime or aliasing proof. Developers must learn moves, borrows, lifetimes, trait bounds, synchronization types, and safe abstraction design. CMU SEI describes this conservatism as an engineering trade-off: reject some safe programs rather than accept memory-unsafe ones [11].

Ownership does not imply that every resource has one simplistic pointer. Libraries can build reference-counted objects, locks, cells, arenas, collections, and other abstractions, but the unsafe implementation beneath a safe interface must establish the interface's promised invariants. RustBelt's central contribution is a method for stating verification conditions for such libraries. The author's synthesis is that a safe abstraction converts a small, auditable proof obligation inside the implementation into a reusable guarantee for many callers; an unsound abstraction performs the opposite conversion by exporting hidden risk through an apparently safe API [6][7].

### Unsafe code and foreign-function interfaces are explicit trust boundaries

Systems languages need operations that a compiler cannot generally verify: dereferencing raw pointers, interacting with device memory, implementing allocators, calling a foreign ABI, or constructing low-level abstractions. Rust therefore permits `unsafe` operations, but the keyword does not disable the rest of the language. It marks a region where the programmer must uphold additional conditions that the compiler cannot prove. Safe callers may rely on those conditions if the region is wrapped behind a sound safe interface [11][12].

A foreign-function interface is especially important because memory crosses language, compiler, allocator, and calling-convention boundaries. Rust's official documentation notes that a compiler cannot verify that a declared foreign signature matches the actual function, and that raw pointers supplied by C may be dangling or otherwise invalid. Correctness depends on the ABI, integer widths, alignment, ownership transfer, allocator pairing, mutability, aliasing, nullability, string encoding, callback lifetime, unwinding behavior, and thread-safety contract matching on both sides [12]. A memory-safe caller cannot repair an invalid pointer that foreign code has already produced.

CISA's open-source analysis demonstrates the architectural consequence. The agencies identified 172 public repositories from a critical-project list and then examined language composition. In a deeper dependency analysis of three projects written primarily in memory-safe languages, all three depended on components containing memory-unsafe code. The unsafe dependencies commonly supplied interfaces to C, graphics, cryptography, or compression. A project's top-level language therefore does not establish end-to-end memory safety; dependency and interface boundaries remain part of the trusted computing base [4].

The correct response is containment, not denial. Unsafe regions and bindings should be kept small, reviewed against written preconditions, tested with sanitizers and fuzzing, and hidden behind APIs that expose lengths and owned or borrowed types rather than unstructured pointers. Ownership transfer should have one documented allocator and destruction route. The build should identify unsafe dependencies and the code paths that reach them. This paragraph is the author's operational synthesis of the Rust documentation, RustBelt, CISA's dependency findings, and empirical Rust bug studies [4][6][7][12].

### Memory safety narrows the vulnerability space but does not equal security

Memory-safe code can still implement the wrong behavior. Injection, broken authorization, weak cryptography, insecure defaults, race conditions outside a language's guarantees, denial of service, secret leakage through logic, and dependency compromise do not disappear because a buffer is bounded. CMU SEI's comparative assessment explicitly limits Rust's default protection to memory and selected concurrency properties and notes that misuse of third-party code and injection remain possible [11]. NSA and CISA likewise present memory-safe languages as part of a broader secure-development approach, not as a complete security system [1][5].

Even the phrase "memory safe" needs a scope. Safe source code may call native libraries, use an unsafe escape hatch, depend on a runtime implemented in unsafe code, or contain generated code and assembly. A compiler defect or unsound library can violate promised properties. The Qin et al. study of reported Rust memory-safety bugs found residual failures associated with unsafe functions, foreign interfaces, generic or trait bounds, automatic reclamation, and related low-level patterns. Its evidence supports concentrating review on unsafe boundaries rather than claiming that the language makes those boundaries harmless [7].

Legacy mitigations therefore remain relevant. For code that cannot yet migrate, NSA and CISA recommend combinations of bounds checking, safer functions and libraries, smart pointers, compiler hardening, static and dynamic analysis, fuzzing, hardened allocators, sandboxing, and operating-system protections [1][2][5]. These measures reduce prevalence or impact without providing the same default guarantee as a language that makes the invalid operation unrepresentable or checked. The author's assessment is that the mature architecture is asymmetric: use language guarantees broadly, reserve expensive detection and mitigation for the shrinking unsafe surface, and retain isolation because no language prevents every software or operational failure [2][5][9].

### Language selection is a system decision

A memory-safe language should be selected against the component's actual constraints. Relevant questions include whether the program needs deterministic destruction, hard real-time latency, direct device access, a small runtime, a stable ABI, particular libraries, certification support, or deployment on a restricted platform. Team skill, debugging and profiling tools, package governance, compiler maturity, long-term support, and interoperability are also engineering inputs. The 2025 NSA-CISA guide cautions against choosing a language merely because it is fashionable and emphasizes ecosystem, tooling, integration, training, and lifecycle fit [5].

The choice need not be one language for an entire product. A managed language may be appropriate for services and control logic, while Rust may fit parsers, native libraries, drivers, or latency-sensitive components. Existing C or C++ may remain behind a hardened interface while new development uses a safer default. The author's synthesis is that the unit of decision should be a component with a defined trust boundary and measurable requirements, not an ideological contest between language communities [2][5][9].

## Evidence

### Microsoft vulnerability triage shows persistence despite layered mitigations

Microsoft's Security Response Center based its 2019 report on vulnerabilities that Microsoft had triaged and assigned CVEs since 2004. Its published chart states that about 70 percent of the vulnerabilities assigned each year continued to be memory-safety issues. The organization also described the surrounding controls already in use: secure-development guidance, static analysis, fuzzing, code review, training, threat modeling, compiler changes, and exploit mitigations. The finding was not that these practices had no value; it was that they had not eliminated the defect class from a very large C and C++ estate [10].

This is operational primary evidence from the vendor that handled the vulnerabilities, not a controlled comparison of otherwise identical programs in different languages. The denominator is Microsoft's assigned CVEs, and product mix, reporting practices, code age, and attacker attention can affect the observed share. It nevertheless tests an important real-world proposition: whether mature organizations can reliably train and tool their way out of memory corruption while retaining a default-unsafe language model. Microsoft's reported persistence across years is evidence against treating voluntary discipline and defect discovery as a complete solution [10].

### Android supplies a longitudinal migration case

Google's Android team compared vulnerabilities in Android security bulletins with changes in the language composition of new platform code. It reported that annual memory-safety vulnerabilities fell from 223 in 2019 to 85 in 2022 and from 76 percent to 35 percent of Android vulnerabilities over the same period. Android 13 was the first release in which a majority of newly added code was written in memory-safe languages; approximately 21 percent of new native C, C++, and Rust code was Rust, and the team reported no memory-safety vulnerability in the roughly 1.5 million lines of Rust then present [8].

The team explicitly cautioned that correlation does not establish causation and named concurrent investment in hardened allocation, sanitizers, hardware-assisted detection, kernel fences, and fuzzing. Its severity data add a separate observation: in 2022, memory-safety issues were 36 percent of bulletin vulnerabilities but 86 percent of critical-severity and 89 percent of remotely exploitable vulnerabilities, and they had represented 78 percent of confirmed in-the-wild exploited Android vulnerabilities over the preceding years [8]. These are product-specific operator measurements, but they connect the language transition to both defect count and security consequence rather than to a benchmark alone.

Google's 2024 update extended the series. It reported that memory-safety issues had fallen to 24 percent of Android vulnerabilities, down from 76 percent in 2019, while most existing code remained memory-unsafe. Google argues that new and recently modified code contains most vulnerabilities and that older code's vulnerability density declines as bugs are found and fixed. On that basis, Android prioritized safe languages for new work and interoperability with existing code rather than wholesale rewrites; the team also reported that Rust changes had less than half the rollback rate of C++ changes [9]. The causal model is Google's interpretation of its operational data and a cited vulnerability-lifetime study, not a randomized migration experiment. Its practical value lies in showing a feasible incremental path in a large production system [9].

### Critical open-source dependency analysis exposes transitive unsafety

CISA, the FBI, and Australian and Canadian cyber authorities studied repositories on the OpenSSF Securing Critical Projects list. They confirmed public repositories for 172 projects, measured language composition with `cloc`, and documented that classification and repository selection could introduce error. They then used multiple dependency-analysis tools and source inspection for three projects written in memory-safe languages, downloaded identified dependencies, and measured those dependencies' language composition [4].

All three selected projects depended on components containing memory-unsafe code. The report describes common reasons as interfaces to C and functions such as graphics, cryptography, and compression. It also documents tool limits: dependency declarations can omit imports, standard libraries and distribution choices complicate resolution, vendored code changes the apparent project boundary, and deeper native dependencies may require additional methods. The finding is therefore not a census of every transitive line. It is direct evidence that source-language labels at the top of a project can conceal an unsafe trusted base below it [4].

### Formal and empirical Rust research delimit the guarantee

RustBelt constructed a formal language representing a realistic subset of Rust, interpreted its types in a concurrent separation logic, and produced a machine-checked safety proof. The proof covers ownership, borrowing, lifetimes, selected concurrency properties, and verified examples of important unsafe library abstractions. Its adequacy result establishes that semantically well-typed programs in the model do not perform invalid memory accesses or data races. The method gives library authors a verification condition for deciding whether an unsafe implementation is a sound extension behind a safe interface [6].

The proof has defined limits. The authors did not model the full Rust language, and a formal result about a core calculus is not evidence that every compiler optimization, foreign library, crate, or unsafe block is correct. Qin and coauthors approached the remaining surface empirically by collecting reported real-world Rust memory-safety bugs, including Rust CVEs, and manually classifying their causes. Their analysis found patterns involving unsafe APIs, foreign-function interfaces, automatic memory reclamation, function signatures, and insufficient generic or trait bounds [7]. Together, the studies support a bounded conclusion: safe Rust has a rigorous foundation, while the unsafe implementation and interoperability boundary remains a concrete source of defects [6][7].

### Independent guidance converges on prevention plus incremental migration

NSA's 2023 information sheet, the 2023 multi-agency roadmap, ONCD's 2024 technical report, and the 2025 NSA-CISA guide were produced by different combinations of security agencies and policy offices. They converge on several engineering points: language-level defaults can prevent memory errors before testing; new code is the least costly place to change direction; high-impact legacy components should be prioritized; unsafe-language mitigations remain necessary during transition; and constraints such as latency, resource use, libraries, platforms, skills, and regulation can alter the appropriate migration path [1][2][3][5].

These documents are technical guidance and policy synthesis, not independent experimental replications. Some of their prevalence claims trace back to the same Microsoft, Google, and Mozilla observations, so citation count should not be mistaken for independent measurements. Their evidentiary contribution is institutional convergence around a mechanism and an implementation strategy: prevent common spatial and temporal errors by default, acknowledge exceptions, and make the transition measurable rather than declaring a product safe because one component uses a memory-safe language [1][2][3][5].

## Implications

### Stop adding unsafe code before attempting wholesale replacement

For most large systems, the highest-leverage first rule is to use a suitable memory-safe language for new components and substantial new features. Android's experience indicates that this can reduce vulnerability inflow while legacy code continues to operate and mature, avoiding the risk and opportunity cost of rewriting every stable component at once [8][9]. The 2025 NSA-CISA guide likewise recommends beginning with new code and using modular boundaries to integrate it with existing systems [5]. This does not make the legacy base safe; it changes the direction of travel and allows migration resources to be focused where risk is highest.

Legacy prioritization should combine exposure and consequence. ONCD cites criteria such as widespread use, position on a network boundary, performance of a critical function, and implementation in a memory-unsafe language. CISA's roadmap adds code that handles untrusted content, keys, network connections, authentication, authorization, firmware, or other low-level operations [2][3]. The author's proposed decision rule is to rank components by reachable unsafe operations multiplied by consequence and replacement feasibility, then begin with parsers and privileged boundary code where a memory defect can most directly become attacker-controlled execution.

A rewrite is not automatically safer. Reimplementation can introduce logic regressions, incompatible behavior, performance failure, and new unsafe bindings. Migration should therefore preserve a testable contract: inputs, outputs, error behavior, performance limits, resource ownership, concurrency semantics, and security invariants. Run differential and compatibility tests where old and new components overlap, use staged deployment, and retain a reversible fallback until the evidence supports removal. This is the author's synthesis of the incremental and interoperability strategies described by CISA, NSA, and Google [2][5][9].

### Make the safe-to-unsafe boundary an architectural object

Every unsafe block, native binding, generated wrapper, assembly routine, and memory-unsafe dependency should have an owner and a written contract. The contract should state valid pointer ranges, lengths, initialization, alignment, nullability, aliasing, lifetime, allocator and deallocator pairing, thread requirements, callback rules, error propagation, and unwinding behavior. Rust's FFI documentation explains why the compiler cannot verify these facts across a foreign declaration, and CISA's dependency study shows how native code enters apparently safe projects transitively [4][12].

Bindings should expose safe types to the rest of the application. Prefer slices over pointer-plus-untrusted-length pairs, owned handles over ambiguous raw pointers, tagged results over sentinel values, and destructors or explicit close operations tied to one ownership rule. Keep conversions adjacent to the boundary, reject invalid representation before calling foreign code, and avoid allowing borrowed foreign storage to outlive the owner. The author's assessment is that a binding is complete only when its safe caller cannot violate the foreign preconditions and foreign failure cannot silently invalidate the caller's assumptions [6][7][12].

Review effort should be concentrated rather than diluted. A small unsafe core can receive manual audit, sanitizer builds, fuzzing, model checking where practical, and strict change control. Safe callers then benefit from the reviewed abstraction. An unsafe wrapper that exposes a safe-looking API without proving its invariants is more dangerous than an openly unsafe call because it hides the need for scrutiny. RustBelt and the empirical Rust studies both make this boundary central to real assurance [6][7].

### Match the memory-management mechanism to the workload

Managed runtimes are often the simplest safe choice for application and service code because their object models, collectors, libraries, and tooling remove much manual lifetime work. They should not be rejected through a generic claim that garbage collection is slow. Measure the actual service-level constraints: steady-state throughput, peak memory, tail latency, pause sensitivity, startup, binary footprint, platform support, and observability. Modern collectors and just-in-time or ahead-of-time compilers vary enough that language labels alone do not predict the outcome [2][5].

Ownership-based languages are strong candidates where predictable destruction, native integration, small runtime assumptions, or low-level control matter. The cost appears in compiler-enforced design constraints, developer learning, and careful unsafe abstraction work rather than in a general tracing collector. CISA and Microsoft identify Rust as an option intended to combine systems-level performance and control with strong default safety, while CMU SEI documents both the benefits and the conservative borrow checker's learning and expressiveness costs [2][10][11]. A pilot should therefore test team productivity and maintainability as well as runtime benchmarks.

Do not accept a performance claim without equivalent security controls. Memory-unsafe code may appear faster when the comparison excludes sandboxing, sanitizers, hardened allocation, process isolation, or incident-response costs that production needs to compensate for unsafety. Google's Android team reported examples in which Rust components avoided some process and thread overhead, while its 2024 account described a Chromium Rust component becoming faster after an otherwise necessary sandbox was removed [8][9]. These are product cases, not universal benchmarks, but they show why system-level cost can differ from a microbenchmark of language primitives.

### Keep defense in depth during and after migration

Memory safety reduces a major vulnerability class; it does not justify removing authentication, authorization, input validation, cryptographic review, sandboxing, dependency controls, logging, or incident response. Safe languages can still express command injection, insecure access decisions, weak protocol state machines, denial-of-service loops, and accidental disclosure. CMU SEI explicitly separates memory and concurrency guarantees from injection and third-party misuse, and NSA-CISA guidance embeds language adoption inside secure development rather than replacing it [5][11].

Legacy memory-unsafe components need stronger compensating controls while they remain. Enable available compiler hardening and bounds checks, replace hazardous APIs, use safer containers and ownership conventions, run static analysis and sanitizer builds, fuzz exposed parsers, isolate high-risk components, and retain operating-system exploit mitigations [1][2][5]. As the unsafe surface shrinks, testing can become more concentrated and more thorough. Google's 2024 interpretation is that proactive detection remains useful but may become more effective when focused on small encapsulated unsafe regions [9].

Dependencies require the same treatment as first-party code. Record which components contain memory-unsafe languages, which APIs expose them, which builds and versions are deployed, and who owns remediation. The software supply-chain topic addresses inventory and provenance broadly; for memory safety, the additional question is whether the dependency can violate a language guarantee through native calls or unsound wrappers. CISA's open-source study shows why a top-level language count is insufficient [4].

### Measure outcomes rather than adoption theater

A credible migration program should track the share of new security-sensitive code written under memory-safe guarantees, the number and size of unsafe regions, native and unsafe dependency paths, newly introduced memory-safety defects, time spent triaging those defects, and the distribution of severity and exploitability. It should also track build time, binary size, runtime memory, tail latency, rollback rate, developer onboarding, and interface defects so that safety gains are not purchased through an unmeasured operational failure. This metric set is the author's synthesis of the outcomes and constraints reported by Google, CISA, NSA, and Microsoft [2][5][8][9][10].

Language percentages alone are weak evidence. A service can be mostly safe by lines of code while routing attacker-controlled data through one unsafe parser. Conversely, a small amount of well-contained native code may be a rational boundary in an otherwise managed system. Report the location, reachability, privilege, and contract of unsafe code rather than only its volume. A useful release gate asks whether new unsafe code was introduced, whether its necessity and invariants were reviewed, whether tests exercise the boundary, and whether a memory-safe alternative was evaluated [4][6][7].

Claims should preserve their denominators. Microsoft's approximately 70 percent refers to Microsoft-assigned CVEs in its reported period; Android's 24 percent refers to Android vulnerability data in 2024; the open-source report's findings refer to its selected repositories and dependency methods [4][9][10]. Keeping these populations visible prevents a persuasive industry statistic from becoming a false universal constant.

### Use a staged migration sequence

Stage one is inventory and policy. Identify languages, unsafe features, foreign interfaces, allocators, native dependencies, exposed parsers, privileged components, and platform constraints. Establish a default that substantial new security-sensitive code uses an approved memory-safe language unless a documented exception is accepted [2][5]. Stage two is a bounded pilot in a component whose contract and performance can be measured. Train the team, build the toolchain, and test interoperability before expanding the policy [2][5].

Stage three is risk-directed replacement. Migrate network-facing, untrusted-input, privileged, and high-consequence components when the replacement can preserve behavior and operational requirements. Improve modularity where tight coupling prevents incremental replacement. Keep stable legacy code behind narrowing interfaces rather than automatically rewriting low-risk code whose behavior is poorly specified [3][5][9]. Stage four is assurance: minimize unsafe regions, audit safe abstractions, test foreign boundaries, trace transitive native dependencies, and make release evidence visible to maintainers and security reviewers [4][6][7][12].

The single worst outcome is false assurance: declaring a product memory safe because its new module uses Rust, Java, or another safe language while attacker-controlled data still crosses an unsound binding or vulnerable native dependency. Prevent that outcome by defining the guarantee end to end, naming every exception, assigning ownership, verifying interfaces, and measuring vulnerability outcomes rather than language branding. This is the author's synthesis of the strongest recurring limitation in the evidence [4][6][7][11][12].

Programming-language memory safety is therefore a structural reduction in risk, not a final security state. It moves common spatial and temporal invariants into mechanisms that scale across developers and releases, allowing scarce review and testing effort to focus on explicit unsafe boundaries and the logic risks that remain. The evidence supports a disciplined transition: safe defaults for new work, risk-based legacy migration, small and verified interoperability surfaces, and defense in depth for everything a language cannot prove [1][2][5][8][9].

## Sources

1. National Security Agency (2023). "Software Memory Safety." Cybersecurity Information Sheet, version 1.1.
   https://media.defense.gov/2022/Nov/10/2003112742/-1/-1/1/CSI_SOFTWARE_MEMORY_SAFETY.PDF [high]

2. CISA, NSA, FBI, ASD's ACSC, CCCS, NCSC-UK, NCSC-NZ, and CERT-NZ (2023). "The Case for Memory Safe Roadmaps: Why Both C-Suite Executives and Technical Experts Need to Take Memory Safe Coding Seriously."
   https://www.cisa.gov/sites/default/files/2023-12/The-Case-for-Memory-Safe-Roadmaps-508c.pdf [high]

3. Office of the National Cyber Director (2024). "Back to the Building Blocks: A Path Toward Secure and Measurable Software."
   https://bidenwhitehouse.archives.gov/wp-content/uploads/2024/02/Final-ONCD-Technical-Report.pdf [high]

4. CISA, FBI, ASD's ACSC, and Canadian Centre for Cyber Security (2024). "Exploring Memory Safety in Critical Open Source Projects."
   https://www.cisa.gov/sites/default/files/2024-06/joint-guidance-exploring-memory-safety-in-critical-open-source-projects-508c.pdf [high]

5. National Security Agency and CISA (2025). "Memory Safe Languages: Reducing Vulnerabilities in Modern Software Development."
   https://media.defense.gov/2025/Jun/23/2003742198/-1/-1/0/CSI_MEMORY_SAFE_LANGUAGES_REDUCING_VULNERABILITIES_IN_MODERN_SOFTWARE_DEVELOPMENT.PDF [high]

6. Jung, R., Jourdan, J.-H., Krebbers, R., and Dreyer, D. (2018). "RustBelt: Securing the Foundations of the Rust Programming Language." Proceedings of the ACM on Programming Languages, 2(POPL), Article 66.
   https://doi.org/10.1145/3158154 [high]

7. Xu, H., Chen, Z., Sun, M., Zhou, Y., and Lyu, M. R. (2021). "Memory-Safety Challenge Considered Solved? An In-Depth Study with All Rust CVEs." ACM Transactions on Software Engineering and Methodology, 31(1), Article 3.
   https://doi.org/10.1145/3466642 [high]

8. Vander Stoep, J., Google Android Security and Privacy Team (2022). "Memory Safe Languages in Android 13."
   https://security.googleblog.com/2022/12/memory-safe-languages-in-android-13.html [high]

9. Vander Stoep, J., and Rebert, A., Google (2024). "Eliminating Memory Safety Vulnerabilities at the Source."
   https://security.googleblog.com/2024/09/eliminating-memory-safety-vulnerabilities-Android.html [high]

10. Microsoft Security Response Center (2019). "A Proactive Approach to More Secure Code."
    https://www.microsoft.com/en-us/msrc/blog/2019/07/a-proactive-approach-to-more-secure-code [high]

11. Sible, J., and Svoboda, D., Carnegie Mellon University Software Engineering Institute (2022). "Rust Software Security: A Current State Assessment."
    https://doi.org/10.58012/0px4-9n81 [high]

12. The Rust Project Developers (accessed 2026). "Foreign Function Interface." The Rustonomicon.
    https://doc.rust-lang.org/nomicon/ffi.html [high]

## See Also

- `library/technology/cybersecurity-principles-threats-and-defense-in-depth.md` -- places language-level prevention inside a broader layered security architecture.
- `library/technology/software-architecture-patterns-principles.md` -- explains the modular boundaries and interface contracts needed for incremental migration.
- `library/technology/software-supply-chain-security-and-sboms.md` -- covers inventory, provenance, and remediation for unsafe transitive dependencies.
