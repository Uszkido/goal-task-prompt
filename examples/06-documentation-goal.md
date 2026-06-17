# Example 06: Documentation Goal

## Input

```text
Update the docs so a new contributor understands this project.
```

## Better Prompt

```text
Use $goal-task-prompt to create a documentation /goal.

The output should ask Codex to:
1. read README.md, CONTRIBUTING.md, examples, and the skill file,
2. find the top 3 missing onboarding details,
3. update only the smallest necessary docs,
4. preserve the public/private boundary,
5. verify all relative links and install commands.

Stop if the docs require product decisions or unsupported claims.
```

## Why It Works

- It turns "better docs" into concrete onboarding gaps.
- It requires link and command verification.
- It avoids unsupported marketing claims.

