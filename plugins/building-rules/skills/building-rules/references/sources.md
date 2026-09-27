# Evidence and limitations

Sources inform conditional rules. Official documentation describes supported
mechanisms; an issue describes a reported experience; neither alone proves that a
particular policy improves all engineering work. Last checked: 2026-09-27.

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

## Maintaining a rule

Add or revise a rule for a concrete failure or decision-changing source. Record its
scope and counterexample. Retire rules that are obsolete, redundant or cause more
cost than benefit. Test actual behavior rather than counting instructions or
asserting that a concise prompt must be efficient.
