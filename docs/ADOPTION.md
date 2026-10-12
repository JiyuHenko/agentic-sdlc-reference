# Adoption guide

You do not need to adopt the whole reference at once.

## Level 1 — context discipline

Add:

- `AGENTS.md`
- `context/PROJECT_STATE.md`
- `context/CURRENT_TASK.md`

Goal: every agent starts from the same authority.

## Level 2 — observable verification

Add:

- `plans/CHANGE_PLAN_TEMPLATE.md`
- `docs/EVIDENCE.md`

Goal: plans state how success will be observed before implementation starts.

## Level 3 — automated fast gate

Adapt `checks/fast_check.py` to your stack.

Typical fast gate:

- formatting;
- lint;
- type checking;
- cheap unit/integration tests;
- repository-specific invariants.

Goal: rapid feedback without running every expensive check after every edit.

## Level 4 — explicit release gate

Adapt `checks/release_gate.py` and `evidence/release-evidence.json`.

Typical release-only evidence:

- full build/export;
- visual QA;
- security scans;
- end-to-end tests;
- signed artifacts;
- production-like integration checks.

Goal: expensive evidence runs when there is a real candidate worth validating.

## Level 5 — encode repeated lessons

When the same mistake happens twice, ask whether it belongs in:

- an operating rule;
- an automated check;
- a reusable plan template;
- the architecture itself.

This is where the workflow starts becoming an engineering asset instead of documentation.
