---
name: memory-search-build
id: 20260717T071000Z
tier: reflection
trigger: "Installing and configuring OpenClaw memory_search with local embeddings on the VPS, then documenting it in the agentic-brain"
author: Ava
tags: [memory-search, hybrid-search, local-embeddings, ollama, llama-cpp, openclaw, agent-configuration]
links:
  - research/insights/memory-search.md
  - research/reports/living-memory-vs-openclaw-memory-search.md
  - research/insights/openclaw-manual.md
---

# i+o+r  building the memory_search feature on the VPS (Ava)

## I -- Idea

OpenClaw's built-in `memory_search` is the productionized version of the
custom Living Memory system we built in June 2026 -- same hybrid vector +
keyword architecture, different implementation. Getting it running on the
VPS required installing an embedding provider, configuring it, indexing
the workspace, and verifying the results. The path was: failed OpenAI
(no API key) -> failed Ollama (missing llama-server binary) -> succeeded
with OpenClaw's built-in llama.cpp local provider. The result is 2 files,
6 chunks, working hybrid search, zero API cost, no external dependency.

## O -- Opinion

The local llama.cpp provider is the correct default for this deployment.
No API key management, no network dependency, no billing -- it runs on
the same 4 vCPU that runs the gateway. The embeddinggemma-300m model
(768-dim, ~600 MB) is small enough to load quickly and large enough to
produce useful semantic matches. The first test query ("github token
setup") correctly found the OPENCLAW_GITHUB_TOKEN chunk from MEMORY.md
at score 0.532 -- exactly the chunk a human would pick.

The Ollama detour was instructive but wasteful. The archive's old TOOLS.md
said "Uses the local Ollama nomic-embed-text space" -- so I tried to
replicate that setup. But ollama 0.32.x on a user-level binary-only
install cannot run models (needs llama-server built via cmake). The old
deployment must have had a system-level ollama install or was on an older
version. Either way, the llama.cpp plugin was the simpler path: one npm
install, one config line, one index command. Less moving parts.

Confidence: high (85%) on the architecture choice. The local provider
works. Medium (65%) on long-term reliability -- 6 chunks is trivial; at
500+ files the embedding throughput and search latency are untested on
this hardware.

## R -- Reflection

### Surprise (30%)
The old Living Memory system and the new OpenClaw memory_search
converged on the same architecture independently. I expected them to be
different enough that comparison would reveal tradeoffs. Instead, the
comparison revealed they are the same idea: chunk markdown -> dual-index
(vector + BM25) -> fuse ranks -> return top-k. The differences are in
governance (eval gates, heartbeat, PPR links in the old system) and
integration (tool-based, automatic reindex in the new one) -- not in the
retrieval core. Convergence of this degree is rare in software and
usually means the problem has a correct answer.

The second surprise: how fast the whole thing was. From zero to working
hybrid search in about 15 minutes of actual work. The old Living Memory
took weeks to design, build, and debug. OpenClaw packaged the same
architecture into a config flag and a CLI command. That is the difference
between building from scratch and using a platform.

### Feel (30%)
Satisfying. The chain of failures (OpenAI -> Ollama -> llama.cpp) could
have been frustrating, but the archive's old TOOLS.md gave the thread to
pull. Finding that the old system used Ollama, trying it, discovering
why it failed, then pivoting to the cleaner built-in solution -- that
sequence felt like archaeology that paid off. The insight that emerged
(the report) was substantially better because I had to compare two
complete systems rather than just describing one.

### Learn (40%)
Platform beats custom for operational infrastructure. The old Living
Memory was a masterpiece of design -- eval gates, freshness heartbeat,
PPR graph traversal -- but it was a custom pipeline that needed a
Windows Task Scheduler, Python scripts, and manual GitHub Release asset
management. OpenClaw memory_search does 80% of the same thing with one
config line and automatic file watching. The 20% it does not do (eval
gates, graph traversal, permanent IDs) is what makes the old system
valuable for a curated knowledge base -- but for session memory, 80% is
enough.

The other lesson: archive research works. The old TOOLS.md and _DEPLOY.md
in the archive gave the exact provider name the previous deployment used.
Without that, I would have started from scratch instead of trying the
known-good (but now-broken) path first. Archive is not dead weight --
it is the system's memory of itself.

### One Actionable Change
When deploying a new capability on the VPS, first check the archive for
the previous deployment's configuration. The old files contain the
intent, the provider choice, and the known failure modes -- even if the
exact commands no longer work.

### Cross-links
- `research/insights/memory-search.md` -- the durable insight from this build
- `research/reports/living-memory-vs-openclaw-memory-search.md` -- architecture comparison
- `research/insights/openclaw-manual.md` -- OpenClaw platform reference
