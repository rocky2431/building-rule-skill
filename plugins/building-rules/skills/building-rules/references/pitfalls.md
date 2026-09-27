# Conditional engineering cases

Read the matching case only. These cases guide decisions; they do not require
new documents or checklists for each task.

<a id="scope"></a>
## Scope expands or shrinks

**Trigger:** a feature or small repair starts turning into an architecture rewrite,
or the agent substitutes a smaller result without owner agreement.
**Failure:** attractive engineering work replaces the requested outcome.
**Minimum response:** connect the proposed edit to the current user behavior;
reuse the existing mechanism and isolate the smallest complete repair.
**Stop:** the original result works and necessary checks pass.
**Exception:** a shared root cause can require a wider change. Establish it from
callers or a distinguishing check; do not preserve a broken design merely to keep
the diff short.
**Evidence:** the historical [KISS report](sources.md#kiss-report) is a user report,
not a reproduced performance benchmark.

<a id="exploration"></a>
## Investigation keeps expanding

**Trigger:** repeated broad searches, unchanged file reads or increasingly large
tool outputs without a change in the implementation decision.
**Failure:** collecting information becomes the task.
**Minimum response:** name the unresolved decision and inspect the nearest
distinguishing evidence. Request a bounded section rather than a full dump.
**Stop:** the cause, relevant consumers and sufficient solution are understood.
**Exception:** unfamiliar trust boundaries, unclear behavior or a high-impact
migration can justify more investigation. Explain the actual unknown.
**Evidence:** [Claude guidance](sources.md#claude-guidance) names infinite
exploration and context pollution.

<a id="verification"></a>
## A green check hides the failure

**Trigger:** changing assertions, deleting checks, adding broad mocks, suppressing
errors or retrying until a favorable output appears.
**Failure:** the gate passes while the requested behavior remains broken.
**Minimum response:** preserve the assertion's intended contract and isolate the
failing premise. Add one meaningful regression only when existing coverage is
insufficient. Retain failed attempts.
**Stop:** relevant checks and the required real behavior agree.
**Exception:** a test may encode an obsolete contract; verify the authorized new
contract before changing it. A UI-copy edit already covered by an existing check
does not need a new framework.
**Evidence:** [review guidance](sources.md#review-guidance) emphasizes working,
reviewable changes and validated descriptions.

<a id="integration"></a>
## Components work but the product does not

**Trigger:** fixtures, a successful build or a worker report are presented as
proof that a real frontend/backend journey works.
**Failure:** incompatible fields, missing wiring or stale runtime versions remain.
**Minimum response:** inspect the affected producer and consumer and exercise the
smallest real boundary required by this task.
**Stop:** the requested path is observed working; report remaining untested surfaces.
**Exception:** an explicitly scoped library change need not launch an unrelated
application. Evidence must match the requested outcome, not a universal E2E ritual.

<a id="risk"></a>
## Safety is skipped or expands without limit

**Trigger:** pressure to remove needed safeguards, or every imagined edge case
starts blocking feature work.
**Failure:** either present harm or indefinite defensive development.
**Minimum response:** identify a reachable trigger, relevant assets and concrete
harm. Preserve necessary trust-boundary protection and repair serious current risk.
Schedule optional hardening after major features.
**Stop:** the present risk and the feature's required checks are addressed.
**Exception:** required security audits, regulated environments or explicitly
requested security work can demand broader coverage. Never invent an exemption
from the owner's or project's real requirements.

<a id="recovery"></a>
## A summary changes intent or authority

**Trigger:** after compaction, memory retrieval or handoff, an agent treats its
own proposal as approval, repeats settled work or loses a user correction.
**Failure:** recovery text becomes a new source of authority.
**Minimum response:** reconcile the latest user request with the accepted task and
current artifacts. Separate decisions, proposals, observations and unverified claims.
Reuse the existing continuity record when one is needed.
**Stop:** the next action is consistent with actual intent and existing evidence.
**Exception:** new evidence can invalidate a prior approach; preserve the unchanged
goal and revisit only affected decisions.

<a id="coordination"></a>
## Coordination costs exceed useful work

**Trigger:** polling unchanged workers, repeated reviews or parallel edits without
independent ownership.
**Failure:** more messages, merges and rework without a better deliverable.
**Minimum response:** delegate only when authorized and useful, include original
requirements, keep ownership clear and reuse completion notifications and task IDs.
Count the coordinator and reviewers in the same delivery budget.
**Stop:** collect the result once, verify what matters and continue or deliver.
**Exception:** explicit monitoring or independent review requirements remain valid;
use host scheduling instead of empty model turns.

<a id="effects"></a>
## An action exceeds authority or overwrites work

**Trigger:** unrelated dirty files, destructive commands, messages, production
changes or publication beyond the request.
**Failure:** data loss or an unintended external effect.
**Minimum response:** preserve existing work and verify the exact target and scope.
Use already granted authority; pause only the unauthorized consequential effect.
**Stop:** the requested effect is verified with its actual result.
**Exception:** permission for the same action need not be asked again. Do not turn
routine reversible editing into an approval ceremony.

<a id="records"></a>
## Records and ratios replace delivery

**Trigger:** elaborate logs, duplicated task books or source-file counts are used
as the main measure of progress.
**Failure:** material is produced while useful behavior is delayed.
**Minimum response:** keep only decision and recovery information; evaluate the
whole delivery. Apply an explicit allocation policy honestly, including inline tests.
**Stop:** the user can assess the outcome, checks and material limits.
**Exception:** a requested report, documentation change or Skill is itself a
deliverable; do not invent application code or silently reclassify a feature task.
