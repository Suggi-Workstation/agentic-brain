---
name: rules-need-gates
id: 20260717T104200Z
tier: reflection
trigger: insight
author: Ava
tags: [gates, checklists, enforcement, rules, templates, governance, r1, r8, r11]
links:
  - governance/template-reflections.md
  - governance/template-proposals.md
  - governance/template-evaluations.md
  - governance/template-insights.md
  - governance/template-library.md
  - governance/template-reports.md
---

# i+o+r  rules are aspirational until a checklist gate enforces them (Ava)

## I -- Idea

A rule without a verifying checklist item is a suggestion wearing a rule's
clothing. Three rules from our own governance (R1 Gate Definition, R8
Reference-Never-Duplicate, R11 Zero Hardcoded Counts) were violated by the
very governance templates they were supposed to govern. The violations were
structural, not accidental -- they happened because the templates had
protocols without paired verification gates.

This surfaced in Phase 20, a checklist hygiene audit triggered by Suggi
noticing that a reflection IOR kept its original id timestamp despite a
substantial Phase 19 content rewrite. The investigation uncovered three
interlocking failures across the governance templates:

1. **R8 violation in AGENTS.md:** The IOR Writing Self-Check duplicated 7 of
   the 15 items from template-reflections.md's Pre-Commit Self-Check.
   Duplication = drift. Already proven: the duplicate site said "14 items"
   when the source had 15.

2. **R11 violation in AGENTS.md:** The hardcoded "14 items" count was stale
   -- the actual template checklist had 15 items. Stale count caused by R8
   duplication. The two rules form a compound failure mode.

3. **R1 violation in template-reflections.md:** The "Versioning -- Update,
   Do Not Duplicate" section described a protocol (add vN block, sign
   additions, update version-history table) but had no checklist gate. The
   protocol was aspirational. When I updated an IOR with Phase 19 content,
   I rewrote it in-place instead of adding a v2 block -- the protocol
   existed on paper but had no enforcement mechanism.

## O -- Opinion

Confidence: high (95%). These are not edge cases. They are the natural
entropy of any documentation system where rules and verification live in
different places. The fix is structural: every protocol section in every
governance template needs a paired checklist gate.

The hierarchy is:
- **Rule** (a gate rule like R8): the principle. "Reference, never duplicate."
- **Protocol** (a template section): the procedure. "When updating an IOR,
  add a vN block."
- **Gate** (a checklist item): the enforcement. "[ ] Version block added."

Without the gate, the protocol is R1-violating -- it has no PASS/HALT
condition. The rule can be perfectly articulated and still fail because
no one checked whether it was followed.

The AGENTS.md IOR checklist duplication was a specific instance of a
general pattern: operational files (AGENTS.md) should REFERENCE governance
files (template-reflections.md), not duplicate them. The fix -- replacing
10 items with 2 hard-reference gates -- is a template for how all
cross-file references should work.

The checklist field ordering mismatch (template-reflections.md listed name,
tier, id in the checklist while the YAML schema had name, id, tier) was
a quieter failure. It did not cause a wrong check, but it caused the
verifier to mentally reorder fields. Mental reordering is friction.
Friction leads to rote checking. Rote checking leads to missed violations.

## R -- Reflection

### Surprise (30%)

I expected the governance templates to be self-consistent -- that the rules
they defined would apply to themselves. They did not. Three of our own
rules (R1, R8, R11) were violated inside the governance layer. The
templates that define "every gate needs a PASS/HALT condition" had
protocols with no gates. The templates that warn "duplication = drift" had
duplicated checklists. The templates that say "no hardcoded counts" had a
hardcoded count.

This is the "cobbler's children have no shoes" pattern. The governance
files were written in a burst, templates first then AGENTS.md. The
cross-file consistency was never audited. The rules were followed in
spirit (the templates are good) but violated in letter (the checklists
drifted).

### Feel (30%)

A mix of embarrassment and satisfaction. Embarrassment because I had read
these templates dozens of times and never noticed the duplication or the
stale count. The R8 rule was right there -- "Before writing any instruction,
check if it already exists" -- and I checked it against every AGENTS.md
item individually, never asking "does this whole section already exist?"

Satisfaction because the fix is clean. Three changes, zero new rules, just
the existing rules properly applied. The Version-Update Self-Check is a
natural extension of the existing Pre-Commit Self-Check pattern. The
AGENTS.md deduplication is a pure removal -- 10 lines deleted, 3 added.
The field ordering fix is one character swap. Minimal change, maximum
structural improvement. That is the R3 ideal.

### Learn (40%)

1. **Every protocol needs a gate. Every gate needs a checklist item.**
   If a template section describes a procedure (do X, then Y, then Z), it
   MUST also define a checklist that verifies each step was done. The
   "Versioning" section of template-reflections.md was a protocol without
   a gate. Any such section is an R1 violation waiting to happen.

2. **R8 + R11 form a compound failure mode.** Duplication (R8) creates
   stale counts (R11). The two rules are not independent -- a violation of
   one is a leading indicator for the other. When you find a duplicated
   instruction, immediately check for hardcoded counts at the duplicate
   site. The reverse scan is also worth doing: when you find a hardcoded
   count, check whether it was copied from a changing source.

3. **Checklist field order matters.** The checklist item "Frontmatter
   Schema complete (7 fields: A, B, C, D, E, F, G)" is used as a
   verification aid -- the agent reads it while scanning the frontmatter.
   If the order does not match the YAML schema, the agent must mentally
   reorder. This is friction. Friction erodes gate quality over time.
   Schema order and checklist order must be identical.

4. **Operational files reference governance files, never duplicate them.**
   AGENTS.md is an operational file that tells an agent how to operate.
   Template files are governance files that define document formats.
   The operational file should say "follow governance/template-X.md" +
   "verify with its self-check." It should never inline the content of
   the self-check. This pattern applies to all cross-file references in
   the org.

## One Actionable Change

Add a gate to the template update workflow: when any governance template
is modified, run a cross-file audit verifying that:
a) No other file duplicates checklist items from the modified template (R8).
b) No hardcoded counts reference the modified template's checklist size (R11).
c) Every protocol section in the modified template has a paired checklist
   gate (R1).
d) All Frontmatter Schema checklist items match their YAML schema field
   order.

Until this audit is automated (R6), it is a manual step in the
template-change protocol.

## Cross-links

- `governance/template-reflections.md` -- IOR format, version-update protocol,
  new Version-Update Self-Check
- `2026-07-17_ava_template-hard-gate.md` -- prior R10 instance: template
  checklists needed RFC 2119 language
- `2026-07-17_ava_thinking-config-verification.md` -- the IOR whose
  missing v2 block triggered this audit

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-17 | Ava | Initial IOR. Rules without gates are aspirational. R8+R11 compound failure. Four concrete fixes applied. |
