# Building Rules

[English](README.md) · [简体中文](README.zh-CN.md)

Building Rules helps coding agents deliver the requested feature or repair with
proportionate investigation, implementation, verification and records. It preserves
necessary quality and safety while giving extra work a concrete stopping condition.

Use it for features, debugging, refactoring and code review. It does not impose
a fixed development ceremony, replace project instructions or turn unrelated
writing and research into coding tasks.

Version: 0.1.0. The optional lifecycle hook uses the Python standard library.
One shared Skill is packaged for Codex, Claude Code, Kimi Code and zCode.

## Install and use

### Codex

```sh
codex plugin marketplace add rocky2431/building-rule-skill
codex plugin add building-rules@rocky-building-rules
```

Start a new session or reload plugins, then ask Codex to use Building Rules.
Review and trust its hook when the host asks. Installation alone does not establish
that a hook ran or that the model followed the instructions.

### Claude Code

```sh
claude plugin marketplace add rocky2431/building-rule-skill
claude plugin install building-rules@rocky-building-rules
```

Start a new session and invoke `/building-rules:building-rules`, or ask for the
Skill by name. The native hook supplies its brief core on supported events.

### Kimi Code and zCode

Use the installed host's native plugin manager. Kimi Code loads
`plugins/building-rules` through its `kimi.plugin.json`. zCode uses
`building-rules@rocky-building-rules` from this repository's marketplace.
Host installation interfaces vary; check the current native manager.

Other Agent Skills hosts can load
`plugins/building-rules/skills/building-rules` as a portable Skill. Without a
compatible hook, invoke it explicitly and read its core from the Skill.

## What loads

| Surface | Entry |
|---|---|
| Codex and Claude Code | Session start, resume, clear, compaction and subagent start |
| zCode | Session start, resume, clear and compaction |
| Kimi Code | UserPromptSubmit before the next user-origin model request |
| Portable Skill | Explicit or host-selected invocation |

Hook support depends on the installed host and trust settings. Kimi's entry does
not prove recovery during autonomous continuation without a new user message.
The hook emits the engineering core and a Skill path. It does not call a model,
edit projects, block tools or create task records. It is advisory, not a security
boundary. Disable it with the native plugin/hook controls.

The core applies only to engineering. Conditional references load when useful.
Avoid duplicate installations through both a plugin manager and a user Skill folder.

## Working with it

Describe the outcome and important constraints in ordinary language. A clear task
needs no form or mandatory interview. For example:

> Fix the parser bug without changing the public API. Preserve unrelated
> working-tree changes and use the existing regression checks.

The Skill covers scope drift, excessive exploration, misleading green checks,
missing integration, disproportionate hardening, recovery errors, coordination
overhead, external effects and excessive records.

Owner policies remain separate from reusable advice. If an owner requires an
allocation such as 80% business code, apply it across the whole feature delivery
without padding or weakening necessary tests. This package does not impose that
percentage on every user or task.

## Contents and verification

- [Skill](plugins/building-rules/skills/building-rules/SKILL.md)
- [Brief core](plugins/building-rules/skills/building-rules/references/core.md)
- [Conditional cases](plugins/building-rules/skills/building-rules/references/pitfalls.md)
- [Sources and limitations](plugins/building-rules/skills/building-rules/references/sources.md)
- [Behavior evaluation scenarios](plugins/building-rules/skills/building-rules/references/behavior-cases.md)

```sh
python3 -m unittest discover -s tests -v
```

Package and hook checks establish file discovery and emitted context, not model
compliance or productivity gains. No comparative model result is claimed for this
release. Native runtime behavior beyond documented local checks is unverified;
the Windows command adapter has not been run on Windows.

Publication, registration in another marketplace and installation are separate
actions. This repository is independently installable, with no mandatory dependency
on another Skill, MCP server or agent framework.

License: MIT.
