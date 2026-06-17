# Example 05: Debugging Goal

## Input

```text
The build is failing. Fix it.
```

## Better Prompt

```text
Use $goal-task-prompt to create a debugging /goal.

Ask Codex to:
1. reproduce the failure with the existing build command,
2. identify the smallest likely cause,
3. change only files needed for that cause,
4. rerun the failing command,
5. stop if the failure requires credentials, production data, or broad dependency upgrades.

The final /goal must require a short report with the command output, changed files, and any remaining risk.
```

## Why It Works

- It starts with reproduction.
- It limits the fix scope.
- It makes command output the proof.

