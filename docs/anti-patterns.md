# Anti-Patterns

Use this list when reviewing changes to the skill or examples.

## Vague Outcome

Bad:

```text
Make the project better.
```

Better:

```text
Complete the P0 bugs listed in BUG_NOTES.md and one bounded P1 UI improvement, verified by tests and screenshots.
```

## No Verification

Bad:

```text
Refactor the code and tell me when done.
```

Better:

```text
Refactor the target files while preserving behavior. Verify with the existing test suite and a short diff summary.
```

## Agent Split Without Merge Plan

Bad:

```text
Launch five agents to improve everything.
```

Better:

```text
First decide whether the workstreams are independent. If yes, create 2-4 subagent goals with clear scopes and a merge plan.
```

## Metric Gaming

Bad:

```text
Make tests pass however you can.
```

Better:

```text
Make tests pass without deleting tests, narrowing coverage, hiding errors, or silently reducing scope.
```

## Scope Creep

Bad:

```text
Also add login, payments, database sync, and a redesign.
```

Better:

```text
Keep this round to one verifiable outcome. Put unrelated work into future goals.
```

