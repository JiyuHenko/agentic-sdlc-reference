# Workflow

## 1. Understand before editing

Read the agent contract, project state, current task, and relevant code.

If Git is available:

```bash
git status --short
git rev-parse HEAD
```

Separate pre-existing user work from the change you are about to make.

When a remote system matters, identify which state is authoritative before writing to it.

## 2. Classify the change

Use the smallest class that honestly describes the work.

### Spike

Use when the goal is to reduce uncertainty. A spike may produce code, but it does not pretend that exploratory code is production-ready.

### Bounded change

Use for a fix or feature with known boundaries and limited blast radius.

### Architectural change

Use when the work changes ownership, persistence, security, cross-domain contracts, or structural infrastructure.

Do not inflate a bounded task into architecture for prestige, and do not hide architecture inside a “small fix” to avoid review.

## 3. Plan the observable result

A useful plan names:

- the problem;
- a concrete failure or desired outcome;
- the current hypothesis;
- files/systems in scope;
- dependencies;
- risks;
- executable verification.

“Should work” is not verification.

## 4. Implement the smallest coherent unit

Prefer small changes that can be validated independently.

For bugs:

1. reproduce or prove the bad state;
2. test one cause hypothesis at a time;
3. fix the cause rather than the symptom;
4. add the nearest practical regression check;
5. re-observe the real behavior.

## 5. Verify near the real system

Choose evidence that matches the claim.

Examples:

- UI claim → render the actual route/state, not only a successful build;
- persistence claim → query/read back the persisted record;
- deployment claim → read back the deployed version/state;
- generated file claim → inspect content, not only file existence;
- API claim → validate both response and relevant side effect.

## 6. Checkpoint before expensive work

Before a long build, visual QA, large test suite, or other timeout-prone operation:

1. finish a coherent unit;
2. run available cheap validation;
3. checkpoint to the authorized remote branch when allowed;
4. record the resulting HEAD.

A future run should be able to resume from that authority.

## 7. Use a two-speed gate

During iteration, prefer the cheapest checks that catch likely mistakes.

At the real release candidate, run the heavier evidence needed to support the release claim.

This is a quality rule **and** a cost rule: expensive evidence should not be recomputed on every intermediate commit when it only matters for the final candidate.

## 8. Review the result

Before completion:

- inspect the diff;
- look for accidental deletion or unrelated formatting;
- scan for placeholders/debug output/secrets;
- confirm public copy/metadata when relevant;
- update known limits.

## 9. Report with evidence

A useful completion report says:

- what changed;
- what was verified;
- the evidence used;
- what could not be verified;
- remaining risk;
- whether a deploy/write occurred.

Avoid absolute language when the evidence is partial.

## 10. Learn from recurring failure

Classify recurring problems as:

- **rule** — document it;
- **check** — detect it automatically;
- **template** — make the safe path reusable;
- **architecture** — remove the structural cause.
