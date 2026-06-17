# Personalization Guide

Keep the public skill generic, then layer your personal workflow outside it.

## Good Personalization

Add project-specific instructions when invoking the skill:

```text
Use $goal-task-prompt to turn this request into a /goal.

Project conventions:
- answer in Chinese,
- read AGENTS.md and TODO.md first,
- do not introduce auth, payments, databases, or Docker,
- ask before broad rewrites.
```

This keeps the skill reusable while still letting the output match your workflow.

## What To Personalize

- language preference,
- project docs to read first,
- forbidden technology choices,
- safety boundaries,
- preferred verification commands,
- closeout format.

## What Not To Put In The Public Skill

- private paths,
- personal account names,
- private repository names,
- secrets or tokens,
- one user's project-specific defaults,
- marketing or launch workflows that belong in another skill.

