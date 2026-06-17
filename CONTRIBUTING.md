# Contributing

Contributions are welcome when they make the skill more useful without making it bloated.

## Good First Contributions

Good first contributions include:

- adding a realistic before/after example,
- improving a stop condition,
- clarifying an installation step,
- adding a near-miss eval case,
- tightening wording without adding scope.

Good contributions usually:

- improve task boundaries,
- add sharper verification language,
- reduce ambiguity,
- add realistic examples,
- remove over-specific personal workflow assumptions.

Avoid adding unrelated launch, marketing, product-management, or platform-specific release workflows to the core skill. Those should live in separate skills or examples.

Before opening a PR:

1. Keep `skill/goal-task-prompt/SKILL.md` concise.
2. Run `python3 scripts/validate_skill.py`.
3. Add or update an example when behavior changes.
4. Explain what kind of user request the change improves.

## Scope Boundary

This repository is for converting rough tasks into better agent prompts. It is not the place for:

- generic prompt libraries,
- marketing launch playbooks,
- platform-specific release workflows,
- unrelated agent frameworks,
- private project rules.

If a proposal is useful but out of scope, it may be better as a separate skill.
