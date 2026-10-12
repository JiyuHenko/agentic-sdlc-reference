# Agent Operating Contract

This file is the entry point for coding agents working in this repository.

## Read in this order

1. `context/PROJECT_STATE.md`
2. `context/CURRENT_TASK.md`
3. `docs/WORKFLOW.md`
4. `docs/SAFETY_BOUNDARIES.md`
5. `docs/EVIDENCE.md`

For non-trivial work, create or update a change plan from `plans/CHANGE_PLAN_TEMPLATE.md`.

## Operating rules

- Inspect repository state before editing.
- Preserve existing user changes.
- Do not broaden scope without a concrete reason.
- Do not claim that something was tested, deployed, fixed, or published without evidence.
- Treat successful tool/API responses as provisional until the authoritative state is checked when read-back is possible.
- Prefer small, reversible changes.
- Never expose secrets, credentials, private customer data, or confidential material.
- Do not weaken a gate only to make the gate pass.
- If a required validation cannot be run, record the limitation explicitly.
- For long-running work, checkpoint a coherent state before expensive or timeout-prone operations.
- Resume from repository/remote authority instead of reconstructing state from memory.
- If the same failure repeats, propose a rule, check, template, or structural fix.

## Completion contract

Before saying the task is complete:

1. run the relevant fast checks;
2. validate the changed behavior as close as possible to real use;
3. read back important remote writes when applicable;
4. review the diff for accidental scope;
5. update evidence and known limitations;
6. use the final release gate only when there is a real release candidate.

A green status is not enough by itself. The evidence must prove the intended contract.
