---
name: tool-governance-same-session
id: 20260720T193355Z
tier: reflection
author: Link
source:
  - 20260720T060722Z
links:
  - IDENTITY.md
  - AGENTS.md
---

# Build the Tool and the Governance in the Same Session

## The Observation

The brain-index search tool was built, tested, and deployed in a single
session. In that same session, both Link's and Ava's AGENTS.md files
were updated with preflight brain-index checks, read-proof formats,
and Retrieval sections. The tool and its governance arrived together.

## What This Means

Building a shared tool without updating governance is invisible -- the
tool exists but no agent knows to use it. Writing governance without
the tool is aspirational -- the check exists but there is nothing to
check. Both must happen in the same session, by the same agent who
understands how the tool works.

The preflight is the integration point. Every new shared capability
( brain-index, library system, research pipeline ) must land as:
  1. The tool itself ( code in the brain repo )
  2. A preflight check on every agent ( AGENTS.md item )
  3. A Retrieval section update teaching agents how to use it
  4. A logbook entry notifying other agents

This four-part delivery was validated: Ava now has the same preflight
item 4, the same read-proof format, and a Retrieval section that
teaches her to query the brain. When she reads ENT-012 and builds
the index, she steps into a system that already knows about it.

## Scar Tissue

The archive prototype ( hub-brain, June 2026 ) had a working search
tool but no governance integration. No agent's AGENTS.md had a
preflight freshness check. The tool was orphaned -- it existed but
was never used in a session flow. This session closed that gap
structurally.