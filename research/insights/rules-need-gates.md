---
name: rules-need-gates
id: 20260717T111500Z
tier: insight
source:
  - 20260717T104200Z
  - 20260717T102400Z
author: Ava
tags: [gates, checklists, enforcement, rules, governance, templates, r1, r8, r11]
links:
  - governance/template-reflections.md
  - governance/template-evaluations.md
  - governance/template-insights.md
  - governance/template-library.md
  - governance/template-proposals.md
  - governance/template-reports.md
---

# Rules Need Gates -- How to Design and Enforce Rules That Actually Fire

## The Insight

A rule without a paired checklist item is a suggestion wearing a rule's
clothing. The gate (the checklist item with a PASS/HALT condition) is the
active ingredient that turns a written principle into enforced behavior.
Separating the rule from its gate guarantees the rule will be followed in
spirit but violated in letter -- exactly what happened to three of our own
governance rules inside the governance templates that define them.

## Evidence

During a Phase 20 checklist hygiene audit (triggered by an IOR timestamp
precision issue in `20260717T102400Z`), three of our own gate rules were
found violated inside the governance templates:

**R1 (Gate Definition) violation in template-reflections.md:** The
"Versioning -- Update, Do Not Duplicate" section described a protocol
(add vN block, sign additions, update version-history table) but had no
paired checklist gate. Without a gate, the protocol was aspirational. The
result: when updating `20260717T102400Z` with Phase 19 content, the v2
block was omitted because nothing enforced it.

**R8 (Reference, Never Duplicate) violation in AGENTS.md:** The IOR Writing
Self-Check duplicated 7 of 15 items from template-reflections.md's
Pre-Commit Self-Check -- formatting requirements, quality gates G2-G8,
and a hardcoded item count. Two copies of the same checklist existed in
two files with no synchronization mechanism.

**R11 (Zero Hardcoded Counts) violation in AGENTS.md:** The duplicated
checklist said "14 items from template-reflections" but the source
template actually had 15 items. The count went stale because the
duplicate site was not updated when the source changed -- a compound
failure caused directly by the R8 violation.

Source: `20260717T104200Z` (rules-need-gates IOR), `20260717T102400Z`
(thinking-config-verification IOR).

## Implications

### 1. The Anatomy of a Properly Enforced Rule

Every rule must have three layers. If any layer is missing, the rule is
aspirational:

| Layer | What it is | Example (R8) |
|---|---|---|
| **Rule** | The principle. One sentence. | "Reference, never duplicate." |
| **Protocol** | The procedure. Steps to follow. | "Before writing any instruction, check if it already exists. If yes, reference it; do not copy." |
| **Gate** | The checklist item. PASS/HALT. | "[ ] No duplicated content found: source referenced, not copied." |

**Anti-pattern:** A rule with a protocol but no gate. This is the most
common failure -- the procedure is documented but never verified. The
template-reflections.md Versioning section was exactly this: the protocol
existed, the gate did not. Result: the protocol was silently skipped.

**Anti-pattern:** A rule with a gate but no protocol. The checklist says
"verify X" but never explains how. The verifier invents their own
procedure, which may be incomplete. "Verify R8 compliance" without
"How to verify R8 compliance" is a gate-shaped hope.

**Correct pattern:** Rule -> Protocol -> Gate, all three present and
cross-referenced. The gate cites the protocol. The protocol cites the rule.

### 2. The R8 + R11 Compound Failure Mode

R8 (duplication) and R11 (hardcoded counts) form a chain reaction:

```
Step 1: Content is duplicated from Source to Copy (R8 violation).
Step 2: Copy includes a hardcoded count of Source items (R11 violation).
Step 3: Source changes (items added/removed/reordered).
Step 4: Copy's count goes stale. Silent failure.
Step 5: Someone reads Copy, trusts the stale count, misses items.
```

This failure mode is deterministic. Any R8 violation that includes a count
WILL eventually become an R11 violation. The two rules are not independent -- 
finding one should trigger a scan for the other.

**Detection pattern:** When you find a hardcoded count (R11), trace it to
its source. Does the source have a different count? If yes, it is a stale
duplicate. When you find duplicated content (R8), scan the duplicate site
for any counts, sizes, or enumerations -- they will all go stale.

**Prevention:** Never hardcode a count that can change. Use "all items
confirmed PASS" instead of "14 items confirmed PASS." The verifier counts
the source items at verification time. The count is always current.

### 3. Checklist Design Principles

Checklists are the enforcement surface of rules. Design them as carefully
as the rules themselves:

**a) Field order must match schema order.**
The checklist item "Frontmatter Schema complete (7 fields: A, B, C, D, E,
F, G)" is used as a verification aid -- the agent reads it while scanning
the frontmatter. If the order does not match the YAML schema, the agent
mentally reorders. Reordering is friction. Friction leads to rote checking.
Rote checking leads to missed violations.

Every checklist that enumerates fields MUST list them in the same order
as the schema they verify. This is testable: compare the YAML block field
order against the checklist parenthetical order. They must be identical.

**b) Operational files reference governance files, never duplicate them.**
AGENTS.md is an operational file (tells an agent what to do). Template
files are governance files (define how things are done). The operational
file should say "pass template X's self-check" and link to it. It should
never inline the checklist items.

Pattern for operational files:
```
[ ] NEW artifact: governance/template-X.md Pre-Commit Self-Check -- all items confirmed PASS
[ ] UPDATE to artifact: governance/template-X.md Version-Update Self-Check -- all items confirmed PASS
```

This is two lines that replace any number of duplicated items. It cannot
go stale because it references the source, not a snapshot of the source.

**c) Every protocol section needs a paired checklist section.**
If a template has a section titled "How to do X," it MUST also have a
section titled "X Self-Check" with verification items. The checklist is
the gate; the protocol is the instruction. Both are required.

Template section pairing:
- "Versioning -- Update, Do Not Duplicate" -> "Version-Update Self-Check"
- "Naming Convention" -> filename item in Pre-Commit Self-Check
- "Frontmatter Schema" + "Frontmatter Rules" -> schema/rule items in Pre-Commit Self-Check

**d) Checklists distinguish creation from update.**
A checklist for NEW artifacts has different items than a checklist for
UPDATES. For example, "id is UTC timestamp with exact second, never used
before" is a creation-time check. For updates, the check is "Original id
preserved (never changed after publishing)." Do not use one checklist for
both -- the creation items will fail on updates and the verifier will
learn to ignore them.

### 4. The Root Cause Fixing Heuristic (R5 Applied to Rules)

When a rule is violated, ask three questions (R5):

1. **Same CLASS?** Would fixing this instance prevent the same class of
   violation? If the fix is "add the missing v2 block to this specific
   IOR," the answer is NO -- the class is "protocol without a gate."

2. **STRUCTURAL not manual?** Does the fix change the system so the
   violation cannot recur, or does it rely on someone remembering? A new
   checklist section is structural. A note saying "remember to add v2
   blocks" is manual.

3. **Would have caught the ORIGINAL?** If the fix had been in place
   before the violation, would it have fired? The Version-Update
   Self-Check, if it had existed, would have caught the missing v2 block
   before commit.

All three must be YES for a root cause fix. For the Phase 20 audit, the
fix was adding the Version-Update Self-Check (structural, catches the
class, would have caught the original). Adding a v2 block to the specific
IOR would have been a symptom fix (not structural, does not catch the
class).

### 5. The Cross-File Audit Protocol

When any governance template is modified, run this audit before committing:

```
[ ] R8 scan: grep for checklist items from the modified template in all other files.
    If found, replace with a reference to the template's self-check.
[ ] R11 scan: grep for hardcoded numbers near any reference to the modified template.
    If found, replace with "all items confirmed PASS" or equivalent derived expression.
[ ] R1 scan: for every protocol section (describes a procedure), verify a paired
    checklist section (verifies the procedure) exists in the same file.
[ ] Field order scan: for every "Frontmatter Schema complete" checklist item,
    verify the field order matches the YAML schema in the same file.
```

This audit is manual until automated (R6). Each scan is a separate
checklist item.

### 6. Common Gate Design Errors and Their Fixes

| Error | Example | Fix |
|---|---|---|
| **Gate without protocol** | "[ ] Verify R8 compliance" with no instructions | Add protocol: "grep for duplicate content, check for stale counts" |
| **Protocol without gate** | "When updating, add a vN block" with no checklist | Add gate: "[ ] Version block added: ## vN -- YYYY-MM-DD -- author" |
| **Duplicated checklist** | Same items in AGENTS.md and template | Replace copy with reference to source self-check |
| **Hardcoded count** | "14 items from template-reflections" | "all items confirmed PASS" (derived at verification time) |
| **Mismatched field order** | Checklist says A, C, B; schema says A, B, C | Match checklist order to schema order |
| **Single checklist for create+update** | "id is UTC timestamp" on version-update | Split into Pre-Commit (for new) and Version-Update (for updates) |
| **Gate verifies presence, not correctness** | "[ ] Version history exists" (could be empty) | "[ ] Version-history table: new row added (version, date, author, change)" |
| **Gate is a reminder, not a check** | "[ ] Remember to add cross-links" | "[ ] Cross-links: at least 1 link to Library/insight/other IOR" |

### 7. Testing That a Gate Actually Fires

A gate that never fires is a gate that does not exist. For each checklist
item, ask: "What is the smallest violation that would cause this item to
HALT?" If you cannot answer, the item is too vague.

Test protocol (R12-adjacent -- test the gate before trusting it):
1. Take a correct artifact that passes all checks.
2. Introduce one violation that should trigger a specific checklist item.
3. Verify the item HALTed.
4. Fix the violation.
5. Verify the item PASSed.
6. Repeat for each checklist item.

This is not practical for every commit, but it should be done when a new
checklist is first deployed or when a checklist is modified. One manual
test cycle per checklist change is enough.

## Counter-evidence

This insight would be invalidated if:

- **Automated enforcement replaces manual checklists.** If CI gates,
  linters, or pre-commit hooks enforce the rules automatically, the
  checklist becomes redundant for those rules. However, some rules
  (semantic quality, cross-file consistency) resist automation and will
  always need a manual checklist. The insight applies to the residual set.

- **Rules are inherently self-enforcing.** If a rule's violation is
  immediately and unavoidably visible (e.g., a syntax error that prevents
  rendering), the checklist is unnecessary. But most governance rules
  produce silent failures -- the file is valid but wrong. For silent
  failures, the checklist remains essential.

- **The cost of checklist verification exceeds the cost of violations.**
  If a rule is violated once per year and the checklist takes 5 minutes
  per commit, the checklist is net-negative. This is a quantitative
  argument, not a qualitative one, and should be evaluated per-rule.
  For our governance templates (changed rarely, high blast radius), the
  checklist cost is negligible relative to the violation cost.

None of these conditions have been observed in our system. The audit that
produced this insight found three rule violations that had been silent for
weeks -- exactly the class of failure that checklists prevent.

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-17 | Ava | Initial insight. Compiled from Phase 20 checklist hygiene audit (R1+R8+R11 compound failure). Covers gate anatomy, checklist design principles, cross-file audit protocol, common gate design errors, and gate testing. |

## Cross-links

- `20260717T104200Z` -- source IOR: rules-need-gates (Phase 20 checklist audit findings)
- `20260717T102400Z` -- related IOR: thinking-config-verification (the incident that triggered the audit)
- `2026-07-17_ava_template-hard-gate.md` -- prior R10 instance: template checklists needed RFC 2119 hard language
- `governance/template-reflections.md` -- IOR template, now with Version-Update Self-Check
- `governance/template-evaluations.md` -- evaluation template
- `governance/template-insights.md` -- insight template
- `governance/template-library.md` -- library template
- `governance/template-proposals.md` -- proposal template
- `governance/template-reports.md` -- report template
