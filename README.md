# Goal Task Prompt

[![Release](https://img.shields.io/github/v/release/zitao4588-create/goal-task-prompt?display_name=tag)](https://github.com/zitao4588-create/goal-task-prompt/releases)
[![Validate](https://github.com/zitao4588-create/goal-task-prompt/actions/workflows/validate.yml/badge.svg)](https://github.com/zitao4588-create/goal-task-prompt/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Turn fuzzy agent requests into verifiable Codex `/goal` prompts, Loop Cards, evaluation prompts, and multi-agent plans.

Most agent failures start before the agent writes code: the task is vague, boundaries are missing, and nobody defined what "done" means. This Codex skill turns rough asks into small task contracts with context, inputs, constraints, verification, stop conditions, and closeout.

```text
"Make this app better"
        ↓
/goal Complete the smallest useful P0 fixes and one bounded P1 improvement...
Read these files first. Do not edit yet. Verify with tests/screenshots.
Stop if the task needs product decisions, risky rewrites, or repeated failed attempts.
```

## 30-Second Install

```bash
git clone https://github.com/zitao4588-create/goal-task-prompt.git
cd goal-task-prompt
./scripts/install.sh
```

Then invoke it in Codex:

```text
Use $goal-task-prompt turn this rough idea into a verifiable /goal prompt.
```

Manual install:

```bash
mkdir -p ~/.codex/skills
cp -R skill/goal-task-prompt ~/.codex/skills/
```

## What It Generates

| Need | Output |
| --- | --- |
| A rough task is too vague | Codex `/goal` prompt |
| You need context before edits | Read-first prompt |
| The workflow repeats | Loop Card |
| Work must be delegated | External-agent prompt |
| A task may need parallel agents | Multi-agent orchestration brief |
| A skill/prompt needs testing | Evaluation plan |

## Before And After

Before:

```text
Redesign the UI and improve the game content. Use agents if useful.
```

After:

```text
Use $goal-task-prompt to create one coordinator /goal.

First inspect project rules, current UI files, game data, screenshots, and bug notes.
Rank findings as P0/P1/P2.
Only split into agents if the workstreams are independent and mergeable.
Each subagent must have scope, inputs, evidence, output format, and stop conditions.
Verify with screenshots, local build, and a closeout report.
Stop if the work needs product decisions, risky rewrites, or repeated failed attempts.
```

## Core Method

```text
Goal -> Context -> Inputs -> Boundaries -> Verification -> Iteration -> Stop -> Output -> Capture
```

The skill keeps prompts focused on:

- one main outcome,
- concrete inputs,
- explicit out-of-scope boundaries,
- evidence-based verification,
- safe stop conditions,
- closeout and knowledge capture.

## Examples

- [Vague task to `/goal`](examples/01-vague-task-to-goal.md)
- [Loop Card](examples/02-loop-card.md)
- [Multi-agent orchestration](examples/03-multi-agent-orchestration.md)
- [Skill evaluation](examples/04-skill-eval.md)
- [Debugging goal](examples/05-debugging-goal.md)
- [Documentation goal](examples/06-documentation-goal.md)

## Docs

- [Personalization guide](docs/personalization.md)
- [Anti-patterns](docs/anti-patterns.md)
- [Evaluation guide](docs/evaluation.md)
- [Roadmap](docs/roadmap.md)
- [Social preview asset](docs/social-preview.md)

## Repository Layout

```text
skill/goal-task-prompt/
  SKILL.md
  agents/openai.yaml
examples/
docs/
scripts/
```

## Validate

```bash
python3 scripts/validate_skill.py
```

The validator checks required skill files, frontmatter, line budget, examples, and common privacy leaks.

## When Not To Use It

Do not use this skill for:

- one-line edits,
- simple Q&A,
- tasks without a meaningful completion standard,
- unrelated backlog bundles,
- work that should be executed immediately rather than converted into a prompt.

## Safety

This skill can include local paths, project details, screenshots, logs, or task context in generated prompts. Review outputs before pasting them into public tools or third-party agents.

Do not include secrets, private tokens, customer data, payment data, production credentials, or private repository details in shared examples.

## Contributing

Contributions are welcome when they make the skill sharper without making it bloated. See [CONTRIBUTING.md](CONTRIBUTING.md).

If this helps you turn vague agent work into verifiable execution, star the repo so other agent builders can find it.

