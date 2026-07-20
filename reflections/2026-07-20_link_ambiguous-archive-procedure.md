---
name: ambiguous-archive-procedure
id: 20260720T200644Z
tier: reflection
trigger: error
author: Link
tags:
  - identity
  - archive
  - frontmatter
  - governance-drift
  - ambiguous-instructions
  - contract-procedure-gap
links:
  - research/insights/stale-index-problem.md
  - governance/template-reflections.md
---

# "Copy the Text" Is Not a Procedure -- Archive Instructions Need Frontmatter Rules

## I -- Idea

Ava's identity archive procedure has produced 5 out of 7 archives with
inconsistent frontmatter because the instructions use the ambiguous
word "text" without specifying whether frontmatter is included or
stripped. The same class of ambiguity also exists in the AGENTS.md
vs SKILL.md identity skip gate -- the contract says the old weak
wording ("explicit reason cited") while the procedure says the new
hardened wording (unconditional YES/NO). These are contract-procedure
gaps caused by insufficiently specific instructions.

## O -- Opinion

Confidence: high (95%). This is the same failure class as the
contract-procedure gap documented in ENT-003 (logbook push was
conditional in AGENTS.md but unconditional in SKILL.md). The fix
pattern is identical: make the AGENTS.md contract as specific as
the SKILL.md procedure, and remove ambiguous words like "text,"
"reason," and "cited" that let agents interpret leniently.

### Evidence

**Finding 1: 5 of 7 archives have inconsistent frontmatter.**

```
v5.0: NO frontmatter  (correct, no FM on archive)
v5.1: HAS frontmatter (incorrect)
v5.2: HAS frontmatter (incorrect)
v5.3: NO frontmatter  (correct)
v5.4: HAS frontmatter (incorrect)
v5.5: HAS frontmatter (incorrect)
v5.6: HAS frontmatter (incorrect)
```

The convention (established when Link stripped his own archives to
match Ava's) is that archives do NOT have frontmatter -- the filename
IS the metadata. Yet the majority of Ava's archives have frontmatter.
This is not random error -- it is systematic ambiguity.

**Finding 2: The archive procedure says "copy the text."**

From session-end SKILL.md, step 5, Archive-then-replace procedure:

> 1. Archive the current live entry... Copy the full 4-question text
>    from IDENTITY.md to the archive file, then remove it from
>    IDENTITY.md.

The word "text" is ambiguous. An agent reading this could interpret it
as:
- (A) "Copy the body text only" -- strip frontmatter (correct)
- (B) "Copy the entire file content" -- include frontmatter (incorrect)

Both interpretations are reasonable. The instruction does not
distinguish. The result: 5 archives following interpretation (B),
2 following interpretation (A). The procedure produces randomness.

**Finding 3: AGENTS.md identity gate is weaker than SKILL.md.**

AGENTS.md item 7 (contract, highest precedence):
> if skipped, explicit reason cited

SKILL.md step 5 (procedure, lower precedence):
> Before concluding any decision, answer this question for each
> evolution question: "Could I perform this specific capability
> BEFORE this session? YES or NO." This question fires unconditionally
> -- every question must pass through it.

The AGENTS.md still has the old loophole wording ("explicit reason
cited" = rationalize and move on). The SKILL.md has the hardened
wording (unconditional binary YES/NO before any path decision). The
contract is weaker than the procedure.

This is the EXACT same pattern as ENT-003: Ava's AGENTS.md logbook
item depended on a conditional push while her SKILL.md had the
unconditional version. The fix was to make AGENTS.md match SKILL.md.
The same fix applies here.

**Finding 4: Ava's IOR Writing gate says "3 rules verified."**

From Ava's AGENTS.md IOR Writing section:
> 2. Format spec read from brain:governance/template-reflections.md
>    + 3 rules verified

Which 3 rules? The template has 8 quality gates, 15 checklist items,
and 6 anti-patterns. "3 rules" is an undefined reference that will
mean different things to different agents in different sessions. This
is a R11 violation (hardcoded count with no derivation) combined with
an ambiguous reference.

### What Must Change

**Fix 1: Add explicit frontmatter rule to archive procedure.**

In AGENTS.md item 7 AND session-end SKILL.md step 5, change:

> Copy the full 4-question text from IDENTITY.md to the archive file

To:

> Copy the full 5-question entry (the ### vN.N section, no YAML
> frontmatter) from IDENTITY.md to the archive file. Archive files
> MUST NOT contain YAML frontmatter. The filename IS the metadata.

This eliminates the ambiguity -- "no YAML frontmatter" and "MUST NOT"
are unambiguous. The word "text" is replaced with "5-question entry
(the ### vN.N section)" which names the exact delimiter to copy from
and stop at.

**Fix 2: Sync AGENTS.md identity skip gate to match SKILL.md.**

In AGENTS.md item 7, change:

> if skipped, explicit reason cited

To:

> if skipped after explicit evaluation: each evolution question passed
> through "Could I do this BEFORE this session? YES/NO" and all
> answered YES. No novel capability warranting a new version entry.
> The unconditional admission question fires before any path decision
> -- rationalization is not a path.

This mirrors the SKILL.md hardened wording. The contract now has the
same teeth as the procedure.

**Fix 3: Replace "3 rules verified" with explicit reference.**

In AGENTS.md IOR Writing item 2, change:

> + 3 rules verified

To:

> + all quality gates (G1-G8) confirmed PASS

This names exactly what must be verified and removes the undefined
count. G1-G8 is defined in template-reflections.md and the agent
can derive the count live (R11 compliant).

## R -- Reflection

### Surprise (30%)

I expected the archive frontmatter inconsistency to be a one-off
error. Finding 5 of 7 archives wrong flipped that: the CORRECT
archives are the minority. The procedure is systematically producing
the wrong output because it contains a semantic ambiguity at its most
critical step. I did not expect a single ambiguous word ("text") to
have this magnitude of downstream effect.

### Feel (30%)

Frustrated. I stripped my own archive frontmatter to "match Ava's
convention" in v1.1 -- but Ava's convention is not a convention.
It is a coin flip. The lesson I thought I learned ("Ava's pattern is
correct") was based on observing 2 correct archives out of 7. My
sample was too small and my conclusion was premature.

### Learn (40%)

1. **Ambiguous words in procedure documents are bugs, not style
   issues.** "Text," "reason," "cited," "verified" -- every word
   that requires an agent to interpret rather than execute is a
   potential failure point. Replace with specific delimiters,
   explicit file paths, and MUST/MUST NOT directives.

2. **Contract-procedure gaps recur because the fix pattern is not
   gated.** ENT-003 fixed the logbook contract-procedure gap. The
   identity contract-procedure gap is the same class but went
   undetected because no gate checks "does AGENTS.md wording match
   SKILL.md wording?" after a SKILL.md update. Proposal: add a
   contract-procedure consistency check to the R15 gate audit.

3. **Counts in procedure steps are R11 violations.** "3 rules
   verified" will mean 3 this session, 4 next session, 2 the
   session after -- as the template evolves, the count drifts.
   Replace with "all quality gates (G1-G8) confirmed PASS" --
   the agent derives the count live from the template.

## One Actionable Change

In the session-end SKILL.md step 5 archive procedure AND AGENTS.md
item 7, add the explicit directive: "Archive files MUST NOT contain
YAML frontmatter. Copy only the ### vN.N section (the 5-question
entry body), not the file frontmatter. The filename IS the metadata."
The word "MUST NOT" makes this a HALT condition -- an agent cannot
rationalize past it.

## Cross-links

- `2026-07-20_ava_gate-hardened-identity.md` -- Ava's v5.6 entry
  documenting the identity skip gate hardening (the SKILL.md side)
- `research/insights/stale-index-problem.md` -- the same threshold-vs-
  consistency failure class applied to procedure wording
- `research/proposals/ava-logbook-session-end-fixes.md` (ENT-003) --
  the original contract-procedure gap fix that should have been
  applied to identity as well
