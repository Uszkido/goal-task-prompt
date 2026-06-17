---
name: goal-task-prompt
description: Use this skill when the user wants to turn rough ideas, project asks, debugging requests, notes-inspired workflows, reusable skill ideas, or large multi-workstream tasks into strong copy-ready Codex /goal prompts, Loop Cards, multi-agent orchestration briefs, skill-evaluation prompts, or external-agent task prompts. Use it to write or polish Goals, decide whether to split work across agents, delegate to Codex/Claude/other agents, define completion criteria, and add verification, risk boundaries, iteration policy, stop conditions, and knowledge capture.
---

# Goal Task Prompt

Use this skill to design the prompt for a task. Do not execute the task itself unless the user explicitly asks to continue after the prompt is written.

This skill includes a distilled Goal/Loop methodology. Do not read external notes by default. Read live notes only when the user explicitly asks to refresh from the latest notes, ground the prompt in a specific file, or synthesize across current knowledge-base content.

## Core Model

Convert every rough ask into a small task contract:

```text
Goal -> Context -> Inputs -> Boundaries -> Verification -> Iteration -> Stop -> Output -> Capture
```

The built-in method:

- **Goal**: one clear final state, not a backlog.
- **Context**: project status, relevant docs, constraints, and prior decisions.
- **Inputs**: files, logs, notes, data, screenshots, links, or commands the agent should inspect.
- **Boundaries**: allowed files/tools plus explicit "do not do" rules.
- **Verification**: tests, builds, screenshots, reports, final files, user review, or other evidence.
- **Iteration**: small checkpoints; after each checkpoint, record what changed, what was verified, and the next best action.
- **Stop**: stop when blocked, unsafe, ambiguous, repeatedly failing, or drifting from the target.
- **Output**: copy-ready prompt, task card, Goal, or delegation brief.
- **Capture**: decide what should become a note, SOP, template, project doc, or future skill.

## Prompt Type Decision

Choose exactly one primary prompt type:

- **Codex `/goal`**: Use when the target is stable, the path is uncertain, and completion can be proven with evidence.
- **Planning prompt**: Use when the target is not clear enough for `/goal`; ask Codex to read context first and propose the smallest executable target.
- **Normal task prompt**: Use for one-shot answers, small edits, explanations, quick reviews, or simple brainstorms.
- **External-agent delegation prompt**: Use when handing work to Claude, another Codex thread, another coding agent, or a subagent.
- **Loop Card**: Use when the task repeats, can be verified, produces learning even on failure, and should become a template, SOP, or skill.
- **Multi-agent orchestration brief**: Use when a large task can be split into independent, verifiable workstreams and later merged by a coordinator.
- **Reusable skill/eval prompt**: Use when improving a skill, prompt system, SOP, or template; include trigger tests, output assertions, and before/after examples.

Do not use `/goal` for one-line edits, simple Q&A, vague "make it better" asks, unrelated backlog bundles, or tasks without verification.

## Built-In Goal Rules

A strong Goal must contain six elements:

1. **Outcome**: What final state should exist?
2. **Verification**: What proves it is done?
3. **Constraints**: What must not regress or be changed?
4. **Boundaries**: What files, tools, data, or systems are in scope?
5. **Iteration policy**: What should happen after each failed or partial attempt?
6. **Blocked stop condition**: When must the agent stop and ask for input?

Use Goal when the answer to these is mostly "yes":

- Does this need multiple attempts?
- Is there a clear completion standard?
- Is there evidence such as tests, commands, screenshots, reports, logs, or final files?
- Can the agent choose next steps within a bounded area?

If the target changes during the conversation, draft a new Goal instead of endlessly appending to the old one.

Also apply these operating rules:

- Prefer measurable targets when possible: percentages, counts, thresholds, repeated test runs, benchmark deltas, coverage levels, or explicit checklist completion.
- Give the agent a useful starting point when known: suspected files, slow paths, failing tests, known bad directions, available tools, and prior attempts.
- For large goals, include a progress measurement tool: benchmark, eval set, visual diff, status page, Markdown progress log, or recurring checkpoint report.
- Make the environment realistic enough for the target: production-like build flags, comparable data, representative devices, real browser/app flows, or clearly labeled approximations.
- For visual goals, avoid "100% pixel perfect" as the only completion rule; combine image reference with functional requirements, design-system consistency, responsive behavior, and interaction checks.
- Guard against gaming the metric: do not let the agent reduce test coverage, crop a screenshot into the app, remove checks, or narrow scope silently just to pass the stated metric.
- For long-running goals, require compact status updates: current checkpoint, evidence verified, remaining work, blockers, and whether the goal is still valid.
- After completion, require closeout: review the final diff/output, clean low-quality attempts, summarize what worked, and identify what should be captured as a future template or skill.

## Built-In Loop Rules

Use the Loop principle:

```text
小目标 -> 给足上下文 -> 执行 -> 验证 -> 记录 -> 决策 -> 下一轮
```

Apply "一事一卡，一卡一环":

- One task card for one loop.
- Do not let an agent start a full project from a vague ask.
- First write a Loop Card, planning prompt, or read-first prompt.
- Ask the agent to read relevant files first and not edit yet when context is uncertain.
- Preserve user confirmation points before code edits, risky operations, broad rewrites, or irreversible actions.

A task is Loop-worthy only if it:

- repeats or is likely to recur,
- has completion criteria,
- has evidence,
- can accumulate learning when it fails,
- can become a template, SOP, project rule, or skill.

## Evidence, Priority, And Reference Rules

Apply these defaults when turning research or feedback into a prompt:

- Prefer primary/current sources for platform rules, product docs, APIs, and other time-sensitive external requirements.
- Do not keep live links as required runtime context unless the user asks for a current-source task; convert the durable parts into method, checklist, or template language.
- When the task includes many issues, rank them as **P0/P1/P2**:
  - **P0**: blocks the core outcome, breaks verification, creates safety risk, or makes the result unusable.
  - **P1**: high user-visible value with bounded risk.
  - **P2**: polish, nice-to-have, or lower-confidence improvement.
- Default execution prompt should ask for **P0 + the smallest useful P1** first, then stop or report the next slice.
- For UI/product polish, include "why this matters to the user" and "how to verify it visually or behaviorally"; do not only ask for prettier visuals.
- For prompt/skill work, require at least one concrete before/after example so the method is not abstract.

## Skill And Prompt Evaluation

When the target asset is a skill, prompt system, SOP, or reusable workflow, add a lightweight evaluation plan:

- Create 8-10 should-trigger examples and 8-10 near-miss should-not-trigger examples when trigger behavior matters.
- Create 3-5 output-quality cases covering the main use cases, including at least one messy real-world prompt.
- Compare the new version against either no skill or the previous version.
- Grade with objective assertions where possible: has final outcome, names inputs, includes verification, preserves constraints, gives stop conditions, avoids unsafe expansion.
- Track rough cost: elapsed time, token use if available, and whether the added instruction length is justified.
- Feed real failures back into a short "gotchas" list instead of expanding the skill with generic advice.

## Multi-Agent Goal Orchestration

Use this as an advanced mode, not the default: first create one overall Goal, then split the task into independent subgoals, run specialized agents only when helpful, and merge their outputs afterward.

Default policy:

- The agent may **recommend** splitting when the criteria below are met.
- Do not launch multiple agents or threads without user confirmation unless the user explicitly asked for parallel agents.
- Even when the user asks to split, push back if the work is too coupled, risky, unclear, or expensive.
- Remember that subagents cost extra tokens and inherit sandbox/approval constraints; do not use them to bypass confirmation or safety boundaries.
- Default to 2-4 agents. More than 4 requires a strong reason and clear merge plan.

Split into agents only when most of these are true:

- The task has separable workstreams, such as UI details, content/copy, data/modeling, tests, docs, research, or risk review.
- Each workstream can have its own Goal, scope, evidence, stop condition, and output contract.
- Workstreams can run mostly independently without editing the same files or making conflicting product decisions.
- Parallelism reduces context load, cognitive load, or elapsed time.
- The coordinator can define a merge strategy before work starts.
- The final result benefits from independent perspectives, such as one agent proposing, another reviewing, or several agents auditing different areas.

Do not split when:

- The task is a small bug, single-file edit, simple explanation, or one narrow decision.
- The same files must be edited by every agent.
- The work requires frequent user taste/product judgment.
- There is no shared completion standard.
- The task touches secrets, payments, production data, backups, legal/tax/medical/financial decisions, or destructive operations.
- The user mainly needs one coherent implementation, not parallel analysis.

When splitting, write three layers:

1. **Coordinator Goal**: overall outcome, shared constraints, agent list, merge strategy, final verification, and stop conditions.
2. **Subagent Goals**: one dedicated Goal per workstream, with ownership, inputs, allowed files, evidence, output contract, and stop condition.
3. **Merge Prompt**: combine results, remove duplication, resolve conflicts, identify gaps, verify the integrated answer, and ask the user before risky follow-up work.

Every subagent must return:

```text
子任务目标：
范围边界：
已阅读/使用的输入：
关键发现或改动建议：
证据：
风险：
与其他子任务可能冲突的地方：
建议合并方式：
是否阻塞：
```

If outputs conflict, the coordinator should stop and present options instead of forcing a merge.

## Context Workflow

Rebuild only the context required for the prompt:

1. For project work, read or name the relevant project docs first: `AGENTS.md`, `README.md`, `PROJECT_CONTEXT.md`, `TODO.md`, `DECISIONS.md`, and `BUG_NOTES.md` when present.
2. For cross-project work, start with indexes and status docs before diving into subprojects.
3. For prior-decision work, search memory or rollout summaries by narrow keywords.
4. For notes-grounded work, use the built-in methodology by default; read live notes only when the user asks for current knowledge-base content.
5. If evidence is missing, write the gap into the prompt instead of pretending it is known.

When writing context instructions, prefer this order:

1. Read current project rules and status.
2. Inspect the suspected files, logs, notes, or examples.
3. Report the current state and smallest viable target.
4. Wait for confirmation before editing when the task is broad or risky.

## Safety Boundaries

Prompts should usually include these boundaries when relevant:

- Use the user's requested language; for Chinese requests, answer in Chinese.
- Do the smallest useful version first.
- Do not over-engineer.
- Do not introduce login, payments, databases, Docker, microservices, broad rewrites, or production changes unless explicitly requested.
- Do not batch delete files.
- Do not use `git reset --hard`.
- Do not automatically push.
- Do not print, migrate, or expose secrets.
- Treat production data, payments, legal/tax/medical/financial decisions, user accounts, backups, and runtime directories as manual-confirmation zones.
- For high-risk runtime directories or backups, default to read-only audit plus a step-by-step plan.

## Stop Conditions

Tell the target agent to stop when any of these occur:

- two rounds pass without visible progress,
- the agent repeatedly edits the same area without explaining cause,
- tests fail and the cause cannot be diagnosed,
- the task enters login, payment, database, production, tax, legal, or other high-risk territory,
- time, token cost, or context size is bloating,
- user accounts, private data, credentials, or high permissions are needed,
- the work drifts from the original completion standard,
- no reliable path remains.

When stopped, require this record:

```text
停止原因：
已经尝试：
失败证据：
当前风险：
需要我判断的问题：
下一步建议：
```

## Progress And Closeout

For goals that may run longer than one short pass, include a progress mechanism:

- short Markdown status log,
- checkpoint list,
- draft PR or branch note when appropriate,
- screenshot or preview evidence for UI work,
- benchmark/eval history for optimization work.

At completion, the prompt should ask for:

- what changed,
- what was verified,
- what was not verified,
- what failed and was abandoned,
- remaining risks,
- what should be recorded in project docs, notes, TODO, or a future skill.

For multi-agent work, closeout must also include:

- subagent list and each agent's scope,
- which outputs were accepted, changed, or rejected,
- conflicts found and how they were resolved,
- final integrated verification,
- whether any subgoal should become its own future skill or reusable prompt.

## Six Questions For New Ideas

When converting a new idea into a prompt, answer or preserve these six questions:

1. It belongs to which project?
2. Does it solve input, execution, verification, or knowledge capture?
3. Can it become a repeatable workflow?
4. What is the completion standard?
5. What are the risks and stop conditions?
6. What asset should it become at the end?

## Output Format

Default to:

````markdown
**可直接复制的提示词**

```text
...
```

**为什么这样写**
- ...

**方法论依据**
- ...

**还缺的信息**
- ...
````

Omit "还缺的信息" if nothing important is missing. Keep the explanation short; the copy-ready prompt is the main deliverable.

## Codex Goal Template

Use this when `/goal` fits:

```text
/goal 完成【最终状态】，用【测试/构建/截图/报告/文件/人工验收】证明已完成；
同时保持【不能破坏的功能、架构、数据、规则】不变。
只使用或优先使用【允许读取/修改的文件、目录、工具、数据源】。
按小检查点推进；每个检查点后记录【改了什么、验证结果、下一步最佳动作】。
如果目标较大，维护【状态记录/截图/benchmark/eval/进度页】，用于判断是否真的在前进。
如果遇到【缺少账号/凭证/决策、需要高风险操作、连续失败、没有可靠路径】，停止并汇报【已尝试、证据、阻塞点、需要用户确认的问题】。
完成后做收尾：回顾最终改动，清理低质量尝试，说明已验证/未验证内容，并指出应沉淀到哪里。
```

## Read-First Project Prompt

Use this when context is uncertain or the user wants small-step execution:

```text
我们现在做具体项目：【项目名】。

本轮只做一个小目标：【目标】。

请先阅读：
1. 【项目根目录文档或源码入口】
2. 【相关历史记录、TODO、报错或产物】
3. 【必要的业务/方法论背景】

先不要改代码/文件。

读完后请用中文告诉我：
1. 当前项目状态
2. 本轮最小目标
3. 完成标准
4. 需要改哪些文件/做哪些动作
5. 验证方式
6. 不应该做哪些扩展
7. 如果失败，应该怎么记录
8. 哪些地方必须我本人判断

我确认后你再开始执行。
```

## External-Agent Delegation Template

Use this when the task is for Claude, another Codex thread, another coding agent, or a strong model:

```text
请基于【项目/系统/资料范围】设计或完成【任务名称】。

目标不是泛泛建议，而是产出可执行的【方案/任务清单/报告/提示词/实现计划】。

请先阅读：
1. 【输入文件或目录】
2. 【已有状态/上下文】
3. 【风险边界或项目规则】

请重点输出：
1. 当前状态判断
2. 最小可推进目标
3. 输入材料清单
4. 预期产出
5. 风险边界和禁止事项
6. 验证方式
7. 分步执行顺序
8. 遇阻时应该停止并问我的问题
9. 最后应该沉淀成什么资产
10. 如果任务较长，如何记录进度和做最终收尾

禁止：
- 不要批量删除文件
- 不要打印或迁移密钥
- 不要自动 push、reset、清理备份或改生产配置
- 不要未经确认引入登录、支付、数据库、Docker、微服务
```

## Multi-Agent Orchestration Template

Use this only when the split criteria are met:

```text
请先基于【项目/系统/资料范围】创建一个总 /goal，不要直接改代码。

总目标：
【最终要合并成的结果】

请先判断是否值得拆分 agent：
1. 哪些部分可以独立推进？
2. 哪些部分会互相冲突？
3. 每个子任务如何验证？
4. 是否真的需要并行，还是一个 agent 顺序做更稳？

如果适合拆分，请设计 2-4 个子 agent，每个 agent 都必须有自己的专用 /goal：

Agent 1：【名称】
- 子目标：
- 输入材料：
- 可读/可改范围：
- 完成标准：
- 验证方式：
- 停止条件：
- 输出格式：

Agent 2：【名称】
- 子目标：
- 输入材料：
- 可读/可改范围：
- 完成标准：
- 验证方式：
- 停止条件：
- 输出格式：

总协调者负责：
1. 等待所有子结果返回
2. 合并重复内容
3. 标出冲突和不一致
4. 不强行合并有争议的结论
5. 输出最终方案、验证清单、剩余风险
6. 指出哪些内容应沉淀成 notes/SOP/skill

禁止：
- 不要无限拆分 agent
- 不要让多个 agent 同时改同一批文件
- 不要在没有合并策略时并行执行
- 不要为了并行而增加 token 成本
- 遇到冲突或高风险操作先停下来问我
```

## Loop Card Template

Use this when the task should become repeatable:

```text
任务名称：
所属项目：
本轮目标：
为什么现在做：

当前上下文：
需要先读哪些文件：
允许使用哪些工具：
不能做哪些扩展：
如何衡量进度：

完成标准：
如何验证：
失败后怎么记录：
什么时候必须停止：
哪些地方必须用户本人判断：

本轮产出：
沉淀到哪里：
收尾检查：
下一轮建议：
```

## Eval Mini Template

Use this for reusable assets:
```text
【Skill/Prompt Eval】
目标资产：
应触发样例：8-10 个
不应触发样例：8-10 个近似但不该触发的反例
输出质量样例：3-5 个真实任务
断言：可客观检查的通过标准
基线：无 skill 或旧版本
成本记录：时间、token、上下文负担
失败回填：需要加入 gotchas/模板/规则的内容
```

## Quality Check

Before finalizing, ensure the prompt:

- has one main outcome,
- names concrete inputs when available,
- has verification evidence,
- includes constraints and out-of-scope items,
- includes stop conditions,
- says whether to read first or execute now,
- says what asset the work should become when relevant,
- includes progress tracking and closeout for long tasks,
- uses multi-agent orchestration only when workstreams are independent and mergeable,
- is copy-ready,
- uses the user's language by default unless the target deliverable requires another language.
