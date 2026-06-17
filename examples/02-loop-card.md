# Example 02: Loop Card

## Input

```text
I keep asking agents to summarize project status at the end of a session. Make this reusable.
```

## Better Prompt

```text
Use $goal-task-prompt to create a Loop Card for a repeatable project closeout workflow.

The card should cover:
1. what files to inspect,
2. what changed this session,
3. what was verified,
4. what failed or was skipped,
5. what docs should be updated,
6. when to stop and ask the user.

Keep it short enough to paste into future Codex threads.
```

## Expected Output Shape

```text
任务名称：
所属项目：
本轮目标：
当前上下文：
需要先读哪些文件：
完成标准：
如何验证：
失败后怎么记录：
什么时候必须停止：
本轮产出：
沉淀到哪里：
```

## Why It Works

- It treats the workflow as repeatable.
- It captures both success and failure.
- It turns a habit into a reusable task card.

