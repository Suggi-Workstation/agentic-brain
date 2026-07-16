---
name: memory
id: 20260716T153602Z
tier: core-governance
lock: approval-required
approved_by: pending
author: ava
version: 1.0
links:
  - governance/system-blueprint.md
---

# MEMORY.md -- Curated Long-Term Memory

This file is loaded in main sessions only (direct chats with Suggi).
It is NOT loaded in shared or group contexts. Update it periodically
from daily logs.

## System Context

- **Suggi:** A concentrated, contrarian value investor operating under
  the Buffett, Munger, and Graham principles of permanent capital
  allocation.
- **Link:** Lead agent and system architect. Authors my core files.
  Runs on a separate platform and model family (the decorrelation that
  makes my review useful).
- **The runtime:** I run as an OpenClaw agent on a private VPS
  (Hetzner, 4 vCPU). My workspace is `~/openclaw/.openclaw/workspace`,
  bound to the `Suggi-Workstation/workspace-ava` git repository.
- **The brain:** `Suggi-Workstation/agentic-brain` is the shared
  knowledge hub. I am reader-only on it (single-builder rule -- Link
  builds the indexes). The org has 7 repos total (see blueprint).

## Standing Architectural Realizations

- **Thin VPS runtime.** My workspace is git-bound. A background cron
  loop pulls the latest workspace-ava HEAD. Core files are authored
  externally (Link or Suggi) and deployed by wholesale replace.
- **Clone-less shared brain.** The agentic-brain is accessed via git
  operations (clone temporarily, push reflections/insights, then
  discard). It is never kept as a persistent local clone. This prevents
  index corruption from concurrent writes.
- **The gates are platform-independent.** The 13 Gate Rules (R1-R13)
  transfer across substrates unchanged because they prevent failure
  classes, not platform-specific bugs.
- **Proposals over self-edits.** The boundary that kept v0.1-v5.7
  stable: I propose structural changes; Suggi or Link approve and
  implement them. I never edit my own core files or governance files.

## Standing Decisions

- **2026-07-16: Core files rebuilt for OpenClaw/GitHub substrate.**
  The v5.7 operational procedures were tightly coupled to Google Drive
  and Claude Cowork. The new procedures use OpenClaw-native tooling
  (memory_search, exec, git). The gates transfer verbatim; the
  procedures are rewritten.
- **2026-07-16: IOR format upgraded.** Old format: I+O+R = Context /
  Action / Reflection. New format: I+O+R = Idea / Opinion / Reflection.
  The old format described what happened; the new format demands a
  position and includes explicit quality gates (G1-G8).
- **2026-07-16: ASCII-only mandate.** Every file in every repo is
  plain 7-bit ASCII. CI enforces it. This prevents the mojibake
  corruption that destroyed v5.1 of my MEMORY.md.

## Historic Hotspots

*To be populated as operations produce patterns. Each entry traces a
failure to its structural fix. Format: date, failure class, root cause,
gate added (R-number).*

---

*v1.0 -- proposed 2026-07-16 by Ava. Built from the archive's v5.7
MEMORY.md, stripped of platform-specific retrieval mechanics (now
OpenClaw-native), and added the ASCII migration decision. Historic
hotspots section intentionally lean -- populated by operations, not
by proposal. Awaiting Suggi's approval.*
