# Evidence and limitations

Sources inform conditional rules. Official documentation describes supported
mechanisms; an issue describes a reported experience; neither alone proves that a
particular policy improves all engineering work. Last checked: 2026-09-27.
The pstack material below was inspected separately on 2026-10-17; this does not
refresh the older sources' verification dates.

<a id="claude-guidance"></a>
## Claude guidance

[Claude Code best practices](https://code.claude.com/docs/en/best-practices)
identifies unbounded exploration, repeated corrections and overlong instruction
files. It also recommends runnable verification and allows small clear tasks to
skip planning overhead. The relevant lesson is proportionality, not mandatory
planning or mandatory avoidance of planning.

<a id="kiss-report"></a>
## Historical KISS report

[Claude Code issue #4361](https://github.com/anthropics/claude-code/issues/4361)
reports a parameter repair expanding into broader architecture and technology
discussion despite simple-solution guidance. It is a historical user report,
not independently reproduced evidence or a current model comparison. Its suggested
hardware-detection shortcut was not validated and is not a rule in this package.

<a id="review-guidance"></a>
## Reviewable working changes

[Simon Willison, Anti-patterns](https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/)
argues against handing others large, unreviewed AI changes and unchecked PR
descriptions. Keep changes understandable and support completion claims with
appropriate evidence; do not require a new evidence bundle for every small edit.

## Skill activation is a separate problem

[OpenAI Skills](https://learn.chatgpt.com/docs/build-skills) and
[Claude Skills](https://code.claude.com/docs/en/skills) describe explicit and
implicit invocation with progressive disclosure.
[Vercel's Next.js evaluation](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)
found unreliable implicit activation in that particular evaluation. It is not a
universal comparison of engineering policies, current models or all Skill hosts.

[OpenAI lifecycle hooks](https://learn.chatgpt.com/docs/hooks) and
[plugin packaging](https://developers.openai.com/plugins/build/plugins)
describe native event contracts and hook trust. Package installation, hook
execution and model compliance are separate observations.

## Engineering discipline can become overhead

[Ultra Builder Pro's archived README](https://github.com/rocky2431/ultra-builder-pro/blob/ec1f2bcb3ac09a3b6f3e4c99624d5d995d3197ea/README.md)
records semantic drift, simulated validation and the adverse effects of excessive
blocking. It motivates retaining intent and evidence without inheriting every
historical workflow stage. This package does not depend on that runtime.

<a id="pstack-methods"></a>
## Conditional methods adapted from pstack

Inspected the upstream source on 2026-10-17 at commit
`6f131f137de64fdaf928278c0fd9ecec520ccbee`. These are author-proposed engineering
methods, not independent model comparisons or evidence of general productivity gains.

- [Model the Domain](https://github.com/backnotprop/pstack/blob/6f131f137de64fdaf928278c0fd9ecec520ccbee/skills/principle-model-the-domain/SKILL.md):
  use a data shape that captures real invariants; retain simple local code when
  abstraction adds no benefit.
- [Attack the Premise](https://github.com/backnotprop/pstack/blob/6f131f137de64fdaf928278c0fd9ecec520ccbee/skills/principle-attack-the-premise/SKILL.md):
  test the assumption shared by failed repairs before another adjustment.
- [Test Behavior, Not Implementation](https://github.com/backnotprop/pstack/blob/6f131f137de64fdaf928278c0fd9ecec520ccbee/skills/principle-test-behavior-not-implementation/SKILL.md):
  judge a test by a broken observable result and a behavior-preserving refactor.
- [Sequence Verifiable Units](https://github.com/backnotprop/pstack/blob/6f131f137de64fdaf928278c0fd9ecec520ccbee/skills/principle-sequence-verifiable-units/SKILL.md):
  localize failures by verifying a coherent unit before building on it.
- [Build the Lever](https://github.com/backnotprop/pstack/blob/6f131f137de64fdaf928278c0fd9ecec520ccbee/skills/principle-build-the-lever/SKILL.md):
  make important work rerunnable. Building Rules narrows this to justified reuse,
  repetition or error risk; it does not demand a new file for every nontrivial task.
- [Performance Issue](https://github.com/backnotprop/pstack/blob/6f131f137de64fdaf928278c0fd9ecec520ccbee/skills/poteto-mode/playbooks/perf-issue.md):
  measure comparable workloads and try removing unused or repeated work first.

Adoption is selective. The package does not inherit pstack's mandatory agent
workflow, model choices, tool-building default, rebasing or publication steps.
Existing authority, project contracts and trust-boundary validation still apply.
Portable-Skill behavior observations belong in the repository's `tests/observations/`;
one successful case does not establish broad reliability or causal improvement.

## Maintaining a rule

Add or revise a rule for a concrete failure or decision-changing source. Record its
scope and counterexample. Retire rules that are obsolete, redundant or cause more
cost than benefit. Test actual behavior rather than counting instructions or
asserting that a concise prompt must be efficient.
