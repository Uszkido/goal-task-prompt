# Evaluation Guide

Use this guide to test whether a change makes the skill better.

## Trigger Tests

Create 8-10 prompts that should trigger the skill:

- "Turn this rough idea into a /goal."
- "Write a Loop Card for this repeatable workflow."
- "Should this task be split across agents?"
- "Create an eval plan for this skill."

Create 8-10 near-misses that should not trigger it:

- "What is a GitHub topic?"
- "Fix this typo now."
- "Summarize this paragraph."
- "Generate a logo."

## Output Quality Tests

Use 3-5 realistic messy inputs. A good output should include:

- one main outcome,
- concrete inputs,
- constraints,
- verification evidence,
- stop conditions,
- closeout or capture instructions,
- multi-agent splitting only when workstreams are independent.

## Regression Check

Compare against the previous version:

```text
Case:
Old output:
New output:
Improved:
Regressed:
Decision:
```

Do not expand the skill just because one case failed. Add concise rules only when the failure is likely to recur.

