---
name: building-rules
description: >-
  Apply proportionate engineering judgment when implementing features, fixing
  bugs, refactoring or reviewing code. Preserve the requested outcome, choose
  the smallest complete change, verify real behavior and stop unnecessary work.
  Skip general writing, factual answers and open-ended non-engineering inquiry.
license: MIT
---

# Building Rules

Deliver the owner's requested behavior with the necessary quality and protection.
Control the cost of investigation, implementation, verification and coordination
together. A shorter diff is useful only when it solves the actual problem.

Read [the shared core](references/core.md) once if a lifecycle hook has not already
supplied it. Preserve the current request and applicable project instructions.
This Skill supplies methods, not additional authority or acceptance requirements.

## Understand enough to act

Start from the user's outcome, reported failure and named entry point. Inspect
the affected code, its immediate dependencies and consumers of shared changes.
For a bug, reproduce or isolate the failure before selecting the repair location.
For a new feature, identify how the user reaches and observes the result.

Use existing context and settled decisions. Ask only for a missing choice that
changes the work; continue independent work meanwhile. A clear small request
needs no planning document, interview, repository audit or mandatory delegation.

Before expanding a search or investigation, identify the unresolved decision.
Stop reading when the behavior and a sufficient approach are clear. Bound tool
output to the relevant files or sections; do not repeatedly load unchanged results.

## Make the smallest complete change

Look for the capability already in the codebase, then the standard library,
native platform and installed dependencies. Use the first sufficient option.
Understand its callers before changing shared behavior. Preserve unrelated work.

Do not shrink the requested functionality to make implementation easier. Add
abstractions, retries, permission layers or persistence only for a current
requirement, observed failure or concrete credible constraint. Optional cleanup
stays out of the critical path.

Protect credentials, authorization boundaries and data from currently reachable
serious harm. Defer extra defensive frameworks until the agreed major features
work. Input validation at a real trust boundary is part of usable functionality.
Read [pitfalls](references/pitfalls.md#risk) when safety and delivery priorities
conflict; neither a hypothetical attack nor a small diff decides severity.

## Verify the behavior that changed

Select the smallest sufficient existing checks for the changed behavior, shared
contracts and affected consumers. Required project gates still apply; a cheap
full suite can be the simplest check. Do not expand testing just because a
focused check passed.

Add a regression check only for an inadequately covered concrete failure.
Exercise a rejecting counterexample when adding a runtime-enforced constraint.
Do not weaken assertions, fabricate data or replace a required integration path
with a mock to obtain a pass. For UI changes, inspect the actual render; for an
integration, check the real boundary needed by the requested outcome.

Reuse passing evidence while its code, inputs and relevant environment remain
valid. Triage a failure with the smallest distinguishing check. Confirmed unrelated
failures are reported, not repaired unless they block the task or the owner asks.
Repeated failure requires revisiting a premise rather than blindly adding retries.

## Finish and report

Deliver when the requested outcome and necessary checks are complete, with no
unresolved blocking defect. Additional findings do not silently become acceptance
criteria. State a material remaining limitation plainly; never call a build,
commit, upload or successful agent turn proof of a working product.

Write only records needed for a decision, continuity or the requested deliverable.
Reuse the current task record when one exists. A commit or completion note normally
needs the behavior change, material reason, actual verification and known limitation,
not the investigation transcript.

Honor an explicit owner allocation policy across the entire delivery, including
coordinator and reviewer artifacts. Classify inline tests as tests; do not pad,
move or relabel work to improve a percentage. Reduce optional work first. If
necessary validation conflicts with a hard owner constraint, surface that conflict
without claiming success or waiving it yourself. Do not invent a universal ratio.

## Read only the relevant case

- Scope drift, repeated exploration, failing checks, safety, integration,
  recovery, coordination or records: [pitfalls](references/pitfalls.md).
- Limits and provenance of community advice: [sources](references/sources.md).
- Evaluating a rule change: [behavior cases](references/behavior-cases.md).

These are conditional references, not a per-task checklist. No extra Skill, model
call, hook, persistent tracker or approval process is required to apply this Skill.
