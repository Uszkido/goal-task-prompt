# Example 03: Multi-Agent Orchestration

## Input

```text
Redesign the app UI, improve copy, review the game rules, and check whether the result is testable. Use multiple agents if useful.
```

## Better Prompt

```text
Use $goal-task-prompt to decide whether this should be split into multiple agents.

Do not launch agents yet.

First create a coordinator /goal with:
1. final outcome,
2. shared constraints,
3. verification evidence,
4. stop conditions,
5. merge strategy.

Then decide whether the workstreams are independent enough to split.

If yes, draft 2-4 subagent goals:
- UI polish
- copy/content review
- game-rule review
- verification/risk review

Each subagent goal must include scope, allowed inputs, output format, evidence, and stop condition.

If the workstreams would edit the same files or make conflicting product decisions, recommend one sequential agent instead.
```

## Why It Works

- It separates "decide whether to split" from "launch agents".
- It prevents multiple agents from editing the same files blindly.
- It requires a merge plan before parallel work starts.

