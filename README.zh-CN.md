# Building Rules

[English](README.md) · [简体中文](README.zh-CN.md)

Building Rules 帮助 coding agent 完整交付约定功能，并控制调查、实现、验证和记录的投入。
它保留必要的质量与安全要求，为额外工作设定具体的结束条件。

适用于功能开发、修复、重构和代码审查。插件遵守用户要求与项目规则；
普通写作、事实问答与非工程研究无需加载工程流程。

版本：0.1.2。可选生命周期 hook 仅使用 Python 标准库。
共享 Skill 提供 Codex、Claude Code、Kimi Code 和 zCode 的原生插件包。

## 安装与使用

### Codex

```sh
codex plugin marketplace add rocky2431/building-rule-skill
codex plugin add building-rules@rocky-building-rules
```

新开会话或重新加载插件，然后要求 Codex 使用 Building Rules。
宿主要求时，检查并信任 hook。安装成功不代表 hook 已运行，也不代表模型一定遵守规则。

### Claude Code

```sh
claude plugin marketplace add rocky2431/building-rule-skill
claude plugin install building-rules@rocky-building-rules
```

新开会话后使用 `/building-rules:building-rules`，或直接要求使用这个 Skill。
原生 hook 也会在受支持事件中提供简短核心。

### Kimi Code 与 zCode

在 Kimi Code 的插件管理器中安装 `https://github.com/rocky2431/building-rule-skill`。
仓库根目录的 `kimi.plugin.json` 指向共享插件包。zCode 从本仓库 marketplace 加载
`building-rules@rocky-building-rules`，通过 `hooks/hooks.json` 只加载其支持的
SessionStart 事件。Codex 和 Claude Code 另外加载 `hooks/subagent.json`；zCode
不加载该文件。安装界面可能随版本变化，以实际管理器为准。

其他支持 Agent Skills 的宿主可加载
`plugins/building-rules/skills/building-rules`。
没有兼容 hook 时，显式调用 Skill 并按其指引读取核心。

## 加载范围

| 宿主 | 入口 |
|---|---|
| Codex、Claude Code | 启动、恢复、清空、压缩后，以及子 agent 启动 |
| zCode | 启动、恢复、清空、压缩后 |
| Kimi Code | UserPromptSubmit，在下一条用户消息发起的模型请求前 |
| 仅支持 Skill 的宿主 | 显式调用或宿主自动选择 |

执行取决于宿主版本和信任设置。Kimi 的入口不证明没有新用户消息时也能在自主续跑中恢复。
hook 只输出简短工程核心与 Skill 路径，不调用模型、不编辑项目、不阻断工具、不创建任务记录。
它提供行为指导，真正的安全边界由运行环境执行。停用时使用原生插件或 hook 控制。

核心只适用于工程任务。详细案例按需读取，不要同时安装插件和用户目录下的重复 Skill。

## 如何协作

直接描述结果和重要约束，例如：

> 修复这个解析错误，保持公共 API 不变。保留工作树里的其他改动，使用现有回归检查验证。

清楚的任务不需要填写模板或额外访谈。规则覆盖范围膨胀、无限探索、虚假验证、
遗漏集成、安全投入失衡、恢复后偏离原意、协作成本、外部效果和过量记录。

个人政策与通用建议分开。如果用户明确要求业务代码占比 80%，应按完整功能轮核算，
不得凑代码或削弱必要测试。公共插件不替所有用户设定这个百分比。

## 内容与验证

- [Skill](plugins/building-rules/skills/building-rules/SKILL.md)
- [简短核心](plugins/building-rules/skills/building-rules/references/core.md)
- [条件化案例](plugins/building-rules/skills/building-rules/references/pitfalls.md)
- [来源与限制](plugins/building-rules/skills/building-rules/references/sources.md)
- [行为评估场景](plugins/building-rules/skills/building-rules/references/behavior-cases.md)

```sh
python3 -m unittest discover -s tests -v
```

结构与 hook 检查证明文件可发现、上下文会按约定输出，不证明模型遵守率或生产率改善。
本版没有宣称完成对照模型实验。本地检查以外的原生运行结果仍未验证，
Windows 命令适配也尚未在 Windows 运行。

源码发布、加入其他 marketplace、安装到本机是不同的动作。
本仓库可以独立安装，不依赖其他 Skill、MCP 服务或代理框架。

许可证：MIT。
