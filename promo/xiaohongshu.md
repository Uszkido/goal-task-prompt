# 小红书图文草稿

## 标题候选

1. 我把 AI 编程任务「跑偏」的问题，整理成了一个开源 skill
2. 别再直接让 AI「帮我优化项目」了，先把任务写清楚
3. 一个让 Codex 更稳的 /goal 提示词工具

## 封面文案

```text
AI 编程老跑偏？
先把任务变成可验证 /goal
```

## 正文

我最近开源了一个 Codex skill：

```text
goal-task-prompt
```

它解决的问题很简单：很多 AI 编程任务失败，不是因为模型不会写代码，而是因为我们一开始给的任务太模糊。

比如：

```text
帮我优化这个项目
修一下 bug
把 UI 做好看点
需要的话多开几个 agent
```

这些话看起来很自然，但对 AI agent 来说，很容易变成：

- 不知道先读哪些文件
- 不知道什么算完成
- 不知道哪些不能动
- 不知道什么时候应该停下来问人
- 多个 agent 各做各的，最后合不起来

所以我把自己常用的一套方法论整理成了一个 skill：

```text
Goal -> Context -> Inputs -> Boundaries -> Verification -> Iteration -> Stop -> Output -> Capture
```

它可以帮你生成：

- Codex `/goal` 提示词
- 先读上下文再执行的提示词
- 可复用的 Loop Card
- 多 agent 拆分与合并方案
- skill / prompt 的评估方案

我最喜欢的一点是：它不会鼓励你无脑多开 agent。

它会先判断任务是否真的能拆：

- 子任务是否独立？
- 会不会改同一批文件？
- 是否有各自的完成标准？
- 最后怎么合并？
- 冲突时谁来判断？

如果拆了只会更乱，它会建议一个 agent 顺序做。

GitHub：

```text
https://github.com/zitao4588-create/goal-task-prompt
```

适合正在用 Codex、Claude Code、各种 AI 编程工具的人。你可以把一个模糊任务丢进去，看看它生成的 `/goal` 是否更清楚。

## 图片页建议

1. 封面：AI 编程老跑偏？先把任务变成可验证 /goal
2. 痛点：不要直接说“帮我优化项目”
3. 方法：Goal -> Context -> Inputs -> Boundaries -> Verification -> Stop
4. 示例：Before / After
5. 多 agent 判断：什么时候拆，什么时候不拆
6. GitHub 链接和安装方式

