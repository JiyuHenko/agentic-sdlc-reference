# Project State

This file is the stable source of truth an agent should read before task-specific instructions.

Replace this template with the facts that matter in your repository.

## Project

- product:
- repository:
- default branch:
- runtime:
- package manager:
- deployment target:

## Authoritative boundaries

List the systems that are canonical for important state.

Examples:

- identity / authorization:
- billing:
- database:
- feature flags:
- production configuration:
- public content:
- generated artifacts:

## Protected areas

Changes here require explicit justification or approval:

- authentication / authorization:
- billing / payments:
- migrations:
- secrets / CI credentials:
- production deployment:
- destructive data operations:

## Validation commands

Fast iteration:

```bash
# examples
# npm run lint
# npm test
python checks/fast_check.py
```

Release candidate:

```bash
python checks/release_gate.py
```

## Operational notes

Record facts that should survive across agent runs:

- known environment limitations:
- required external services:
- expensive checks:
- deployment restrictions:
- customer/privacy constraints:
