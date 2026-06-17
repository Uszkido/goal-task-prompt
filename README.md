# Goal Task Prompt

A community Codex skill for turning rough work requests into verifiable `/goal` prompts, Loop Cards, skill evaluation prompts, and multi-agent orchestration briefs.

It is built for situations where a task is too fuzzy to execute safely, but concrete enough to become a small contract with context, boundaries, verification, stop conditions, and closeout.

## Why This Exists

AI coding agents fail most often when the task is underspecified:

- "Make this better."
- "Fix the project."
- "Redesign the UI."
- "Use multiple agents if needed."

This skill turns those requests into prompts that are easier to execute and easier to verify.

## What It Generates

- Codex `/goal` prompts
- Read-first project prompts
- Loop Cards for repeatable workflows
- External-agent delegation prompts
- Multi-agent orchestration briefs
- Lightweight skill/prompt evaluation plans

## Install

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skill/goal-task-prompt ~/.codex/skills/
```

Then invoke it in Codex:

```text
Use $goal-task-prompt turn this rough idea into a verifiable /goal prompt.
```

## Quick Example

Input:

```text
Redesign this app UI and improve the game content. Use agents if needed.
```

Output shape:

```text
/goal Complete a scoped UI polish and game-content improvement plan...

First read the project rules, current UI files, game data, screenshots, and bug notes.
Rank findings as P0/P1/P2.
Only split into multiple agents if the workstreams are independent and mergeable.
Verify with screenshots, local build, and a short closeout report.
Stop if the work needs product decisions, risky rewrites, or repeated failed attempts.
```

## Core Method

```text
Goal -> Context -> Inputs -> Boundaries -> Verification -> Iteration -> Stop -> Output -> Capture
```

The skill keeps prompts focused on:

- one main outcome,
- concrete inputs,
- clear constraints,
- evidence-based verification,
- stop conditions,
- closeout and knowledge capture.

## Repository Layout

```text
skill/goal-task-prompt/
  SKILL.md
  agents/openai.yaml
examples/
  01-vague-task-to-goal.md
  02-loop-card.md
  03-multi-agent-orchestration.md
  04-skill-eval.md
```

## When Not To Use It

Do not use this skill for:

- one-line edits,
- simple Q&A,
- tasks without a meaningful completion standard,
- unrelated backlog bundles,
- work that should be done immediately rather than converted into a prompt.

## Safety Notes

This skill can include local paths, project details, screenshots, logs, or task context in generated prompts. Review outputs before pasting them into public tools or third-party agents.

Do not include secrets, private tokens, customer data, payment data, production credentials, or private repository details in shared examples.

## Status

Initial public release: `v0.1.0`.

