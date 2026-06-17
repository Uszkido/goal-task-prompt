# X Thread Draft

## Post 1

I made a small Codex skill for a problem I kept hitting:

AI coding agents do not just fail during implementation.
They often fail before implementation, because the task is vague.

So I built `goal-task-prompt`.

Repo:
https://github.com/zitao4588-create/goal-task-prompt

## Post 2

The skill turns prompts like:

```text
Make this app better.
Fix the project.
Redesign the UI.
Use multiple agents if needed.
```

into task contracts with:

- outcome
- context
- inputs
- boundaries
- verification
- stop conditions
- closeout

## Post 3

Core model:

```text
Goal -> Context -> Inputs -> Boundaries -> Verification -> Iteration -> Stop -> Output -> Capture
```

It is not a mega-prompt.
It is a way to stop agents from running ahead without a definition of done.

## Post 4

It can generate:

- Codex `/goal` prompts
- read-first project prompts
- Loop Cards
- external-agent delegation prompts
- multi-agent orchestration briefs
- lightweight skill/prompt eval plans

## Post 5

The multi-agent part is intentionally conservative.

It only recommends splitting when workstreams are independent, verifiable, and mergeable.

No "launch 10 agents and hope they agree" behavior.

## Post 6

I open sourced it here:

https://github.com/zitao4588-create/goal-task-prompt

If you use Codex or build agent workflows, try it on one vague task and compare the output before/after.

Stars and prompt cases are welcome.

