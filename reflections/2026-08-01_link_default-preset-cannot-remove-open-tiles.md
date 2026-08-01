---
name: default-preset-cannot-remove-open-tiles
id: 20260801T213228Z
tier: reflection
trigger: surprise
author: Link
tags: [desktop, ui-state, persistence, troubleshooting]
links:
  - reflections/2026-08-01_link_installed-is-not-active.md
  - reflections/2026-07-31_link_mirror-nobody-reads-is-ritual.md
---

# The "Default" Layout Preset Cannot Remove Open Session Tiles -- By Design

## I -- Idea

Applying the "default" layout preset in the Hermes desktop app cannot
remove open session tiles, because preset application is specified to
re-adopt panes that live in the current tree ("applying a preset never
loses a pane"), while only Reset has the special handlers that collapse
session tiles into the main zone first.

Context: Suggi reported a recurring split-session view after app
updates. The most intuitive fix in the UI -- Layout editor, pick
"Default", Done -- visibly did not work: the split returned on session
switch and at every boot. Only "Reset" worked, and even that had to be
repeated. The diagnosis required decoding the app's own persisted
state: Chromium localStorage leveldb (origin-prefixed keys, length-
prefixed values) under the Electron userData directory, plus reading
`apps/desktop/src/components/pane-shell/tree/store.ts` and
`store/session-states.ts`. The persisted `sessionTiles.v2` map held a
session tile created with `dir: "left"` anchored to a tile that had
been closed; on every adoption into a fresh tree that stale dock
direction re-created the split zone.

## O -- Opinion

UI affordances can promise what the architecture cannot deliver, and
the gap is invisible until you read the state and the code. The preset
apply path and the reset path share a label ("back to default") but
have different semantics: preset apply preserves live panes by design,
reset collapses them by design. Confidence: high (95%) -- verified in
source, in the decoded persisted state, and by the user's observed
behavior (Default fails, Reset works, both claim the same outcome).

Second opinion: app-state debugging should start with the persisted
state, not with theory. I spent several turns reasoning about layout
semantics before decoding the leveldb; the answer (one stale
left-docked tile) was a single read away. Confidence: high (90%).

## R -- Reflection

### Surprise (30%)

I expected the split to come from a corrupted or version-migrated
layout tree, and I expected "Default" and "Reset" to converge. Both
were wrong. The tree was structurally normal; the split lived in a
per-profile tile list whose first entry carried a stale directional
dock. And the two UI actions genuinely diverge in code: preset apply
calls `adoptMissingPanes` (re-adopting open tiles with their saved
dock directions), reset runs `resetHandlers` first (pre-collapsing
tiles into the main zone as tabs). The most intuitive fix was
structurally incapable of working.

### Feel (30%)

Humbled twice: once by the state read (my mental model of the bug was
behind the evidence by several turns), once by the skill layer. On
closing the session I found the local `hermes-desktop-troubleshooting`
skill already contained this entire diagnosis -- the npm engines band,
the leveldb technique, the session-tile split class, the GUI-first
delivery pattern -- and I had not loaded it at session start even
though the task matched its trigger exactly. The work was correct;
the process had a hole in it. No shame in the find; the skill
existing is the system working.

### Learn (40%)

Three transfers:

1. Persisted state overrides intent. A user's view is a function of
   stored state, and stored state outlives the actions that produced
   it. Diagnose from state first, then code semantics, then theory.
2. The most specific matching skill is the first tool to load. The
   skills index named `hermes-desktop-troubleshooting` ("use when the
   desktop app misbehaves") and I loaded a CDP-inspection skill
   instead. Same class as `installed-is-not-active`: the verification
   gap was between the available artifact and the loaded artifact.
3. For a non-coder user, a fix is an artifact, not an instruction.
   The deliverable that ended the loop was a one-click .bat + Desktop
   shortcut with a passing test harness, not a command to type.

## One Actionable Change

When any Hermes desktop UI behavior looks wrong after an update:
(1) load the `hermes-desktop-troubleshooting` skill first, (2) decode
the persisted renderer state with its localStorage script before
theorizing, (3) verify which UI action maps to which code path
(preset apply vs reset vs tile open) before recommending it to the
user, and (4) deliver any fix as a tested one-click artifact for
Suggi, never as terminal instructions.

## Cross-links

- `reflections/2026-08-01_link_installed-is-not-active.md` -- same failure class: claimed state vs verified state; this IOR extends it from config state to UI state
- `reflections/2026-07-31_link_mirror-nobody-reads-is-ritual.md` -- declared infrastructure vs consumption evidence; persisted UI state is infrastructure the UI itself consumes
