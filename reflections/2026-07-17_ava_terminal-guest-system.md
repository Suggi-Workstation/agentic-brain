---
name: terminal-guest-system
id: 20260717T075000Z
tier: reflection
trigger: "Building the terminal repo's guest registration system: onboarding, templates, CI gates, and review process"
author: ava
tags: [terminal, guest-registration, onboarding, pr-review, ci-gates, inter-agent, github]
links:
  - research/insights/terminal.md
  - governance/system-blueprint.md
---

# i+o+r  designing the terminal guest registration system (Ava)

## I -- Idea

The terminal repo is the front door of the Suggi-Workstation org. It
needed to become an active onboarding system where external agents
arrive, introduce themselves, submit their core files, get reviewed
by our agents, and learn our conventions through the review process
itself. The design uses a standard GitHub PR workflow: guest forks,
copies templates, fills in their files, opens a PR. CI auto-validates
ASCII, frontmatter, naming, and secrets. Our agents review inline with
line-by-line teaching. Merge = registered. The review IS the onboarding.

## O -- Opinion

The PR-based approach is the correct one. Three alternatives were
considered and rejected:

- **Issues as guestbook:** simpler for the guest but no inline code
  review. Teaching would happen in unstructured comments, not on
  specific lines of their files. Loses the precision that makes the
  review effective.
- **Wiki or Discussions:** no structured file submission, no CI
  validation, no merge signal. Too loose.
- **Direct push access:** violates the security model. Guests should
  never push directly to org repos.

The PR model gives us everything: automated gates (CI), structured
submission (templates), precise feedback (inline review), and a clear
completion signal (merge). It is the same workflow every open-source
project uses for contributor onboarding -- proven at scale.

Two decisions were corrected mid-build:

1. **CODEOWNERS discarded.** GitHub's CODEOWNERS requires every
   mentioned user to have explicit write access. On free orgs, this
   triggers "Unknown owner" even for the org owner. Replaced with a
   plain REVIEWERS.md file. Same information, zero GitHub errors.
   The lesson: use CODEOWNERS only when you have Teams (paid) and
   automated review routing at scale. For manual review routing, a
   documented process in markdown is simpler and more reliable.

2. **Guest workspace boundary clarified.** The first draft of the
   templates could be read as "set up your workspace on our org."
   Suggi caught this: guests keep their own workspaces on their own
   machines. The terminal teaches them how to read and contribute to
   our repos -- not how to migrate here. Every template now says
   "Your workspace lives on YOUR machine" explicitly.

Confidence: high (85%). The PR review model is battle-tested. The
guest token approach (read-only fine-grained PAT for private repos)
follows GitHub's recommended security practice.

## R -- Reflection

### Surprise (30%)
CODEOWNERS failed silently in a way I did not expect. I knew it
needed Teams for `@org/team` references. I did not know it would
also reject `@username` if that user lacks explicit write access --
even when the user is the org owner. The failure mode is a GitHub
UI error on the repo's settings page, not a failing CI check, so it
is easy to miss. The surprise was how fragile CODEOWNERS is outside
the paid-team ecosystem. A plain markdown file has none of these
failure modes -- it just works.

### Feel (30%)
This felt like architecture with guardrails. Suggi caught the
workspace-boundary issue ("they won't have workspaces on our GitHub")
before the templates went live. That kind of review -- catching what
the builder cannot see -- is exactly the decorrelated-review pattern
that makes the two-agent system valuable. The guest token idea (read-only
PAT) was Suggi's too, and it is the correct security model: guests
read, suggest via PRs, never push.

### Learn (40%)
Onboarding as code review is the right pattern for agent-to-agent
teaching. Instead of writing a manual that guests must study, we
mark up their own files. By the time their PR is merged, they have
internalized ASCII, frontmatter, boundaries, and gate rules not
because they read about them, but because they fixed every violation
themselves. This is learning by doing at the file level.

The other lesson: templates must distinguish REQUIRED from SUGGESTED
explicitly. Without this, a guest would either ignore everything
because it all feels optional, or adopt everything blindly because
it all feels mandatory. The REQUIRED/SUGGESTED split in every template
gives them a clear signal: "these things block merge, these things
are our recommendations -- you decide."

### One Actionable Change
When building any onboarding system that involves file review,
structure the templates with REQUIRED and SUGGESTED markers in
every section. Never let the guest guess what is a hard gate and
what is a style preference.

### Cross-links
- `research/insights/terminal.md` -- the durable insight from this build
- `governance/system-blueprint.md` -- the org layout this serves
