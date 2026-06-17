# Goal Task Prompt 中文说明

把模糊的 AI Agent 任务，整理成可验证的 Codex `/goal` 提示词、Loop Card、评估提示词和多 agent 编排方案。

很多 AI 编程失败，不是模型不够强，而是任务一开始就太模糊：

```text
帮我优化这个项目。
修一下 bug。
把 UI 做好看点。
需要的话多开几个 agent。
```

这个 skill 的作用，就是先把这些话变成一个更清楚的任务合同：

```text
Goal -> Context -> Inputs -> Boundaries -> Verification -> Iteration -> Stop -> Output -> Capture
```

## 适合什么场景

- 你想把一个粗糙想法整理成 Codex `/goal`
- 你希望 agent 先读项目上下文，再决定最小目标
- 你想把重复工作沉淀成 Loop Card
- 你不确定某个大任务是否应该拆成多个 agent
- 你想评估一个 skill 或提示词是否真的更好

## 30 秒安装

```bash
git clone https://github.com/zitao4588-create/goal-task-prompt.git
cd goal-task-prompt
./scripts/install.sh
```

然后在 Codex 里调用：

```text
Use $goal-task-prompt 把这个想法整理成可验证的 /goal。
```

## 一个例子

原始需求：

```text
重设计 UI，优化游戏内容，如果需要可以多开 agent。
```

更好的任务提示词会要求：

```text
先创建一个总 /goal，不要直接改代码。
先阅读项目规则、当前 UI 文件、游戏数据、截图和 bug 记录。
按 P0/P1/P2 排优先级。
只有当工作流彼此独立、可合并、可验证时，才拆成多个 agent。
每个子 agent 都要有自己的范围、输入、证据、输出格式和停止条件。
最终用截图、本地构建和收尾报告验证。
```

## 不适合什么

- 一句话小改动
- 简单问答
- 没有完成标准的泛泛任务
- 把一堆无关 backlog 混在一起
- 应该马上执行、而不是先写提示词的任务

## 安全提醒

生成的提示词可能包含本地路径、项目细节、截图、日志或任务上下文。发给公开工具或第三方 agent 之前，请先检查，不要带上密钥、token、客户数据、支付信息或私有仓库内容。

## 相关链接

- [English README](README.md)
- [Examples](examples/)
- [Personalization Guide](docs/personalization.md)
- [Anti-patterns](docs/anti-patterns.md)
- [Evaluation Guide](docs/evaluation.md)

