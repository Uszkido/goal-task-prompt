# Example 01: Vague Task To Goal

## Input

```text
Help me improve this project. There are several bugs and the UI feels rough.
```

## Better Prompt

```text
Use $goal-task-prompt to turn this rough request into a scoped Codex /goal.

Project: [project name]
Context to inspect first:
1. AGENTS.md
2. README.md
3. PROJECT_CONTEXT.md
4. TODO.md
5. BUG_NOTES.md
6. the suspected UI and bug-related files

Do not edit files yet.

First report:
1. the smallest useful outcome for this round,
2. P0/P1/P2 issues,
3. which files are likely in scope,
4. how to verify completion,
5. what should explicitly stay out of scope.

Then write a copy-ready /goal that asks Codex to complete only the P0 issues and the smallest useful P1 improvement, with tests or screenshots as evidence.
```

## Why It Works

- It blocks vague "fix everything" behavior.
- It asks for context before edits.
- It narrows execution to P0 plus a bounded P1.
- It defines verification before implementation.

