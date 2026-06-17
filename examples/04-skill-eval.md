# Example 04: Skill Evaluation

## Input

```text
I improved a skill. How do I check whether it is actually better?
```

## Better Prompt

```text
Use $goal-task-prompt to create a lightweight skill evaluation plan.

Target skill: [skill name]

Please produce:
1. 8-10 examples that should trigger the skill,
2. 8-10 near-miss examples that should not trigger it,
3. 3-5 realistic output-quality cases,
4. objective assertions for grading,
5. a baseline comparison plan against the old version or no skill,
6. a short gotchas section for failures found during testing.

Do not rewrite the skill yet. First create the eval plan.
```

## Why It Works

- It tests trigger behavior and output quality separately.
- It uses near-miss cases to prevent scope creep.
- It feeds failures back into concise improvements.

