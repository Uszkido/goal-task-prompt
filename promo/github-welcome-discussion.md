# Show and tell: turn vague agent tasks into verifiable /goal prompts

Welcome to `goal-task-prompt`.

This is a small Codex skill for a common agent-workflow problem: fuzzy tasks create fuzzy execution.

Instead of sending an agent a request like:

```text
Make this app better.
Fix the project.
Redesign the UI.
Use multiple agents if needed.
```

the skill helps turn it into a task contract:

```text
Goal -> Context -> Inputs -> Boundaries -> Verification -> Iteration -> Stop -> Output -> Capture
```

It can draft:

- Codex `/goal` prompts
- read-first project prompts
- Loop Cards
- external-agent delegation prompts
- multi-agent orchestration briefs
- lightweight skill/prompt evaluation plans

The part I care about most: it does not recommend multi-agent work by default. It first asks whether the workstreams are independent, verifiable, and mergeable.

Repo:
https://github.com/zitao4588-create/goal-task-prompt

If you try it, please share:

1. the rough task you started with,
2. the prompt it generated,
3. where it helped,
4. where it was still too vague.

Prompt cases are the best way to improve this skill.

