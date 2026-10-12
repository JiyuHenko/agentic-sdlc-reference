# Agentic SDLC Reference

A small, provider-agnostic reference for using coding agents with **explicit context, bounded authority, evidence-based validation, and resumable execution**.

This repository is a public distillation of patterns I use in real projects. It is intentionally smaller than the private harnesses that inspired it: the goal is to make the operating model easy to inspect, clone, discuss, and adapt.

> The core idea: a coding agent should not be trusted because it sounds confident or because CI is green. The workflow should make it clear **what the agent knew, what it was allowed to change, what was actually verified, and what remains uncertain**.

## Why this exists

Coding agents are useful because they can move quickly across a repository. The same flexibility creates predictable failure modes:

- stale or missing context;
- changes outside the requested scope;
- “done” claims without semantic evidence;
- successful remote writes that were never read back;
- expensive CI repeated on every intermediate commit;
- screenshots or artifacts that prove existence, not correctness;
- long-running work that cannot be safely resumed after a timeout.

This reference turns those failure modes into a small operating contract.

## The loop

```text
Understand
   ↓
Classify
   ↓
Plan
   ↓
Implement
   ↓
Verify near the real behavior
   ↓
Checkpoint authoritative state
   ↓
Run the appropriate gate
   ↓
Report evidence + remaining uncertainty
```

## Core principles

1. **Understand before editing.** Read repository state and source-of-truth context first.
2. **Classify the change.** A spike, bounded change, and architectural change should not receive the same process.
3. **Bound authority.** Make scope, side effects, and protected areas explicit.
4. **Verification must be observable.** “Should work” is not a verification step.
5. **Write success is not proof.** Important remote writes should be read back from the authoritative system.
6. **Green is not semantic correctness.** A build, screenshot, artifact, or API 200 is evidence only when it proves the intended contract.
7. **Checkpoint long work.** Resume from remote authority, not sandbox memory.
8. **Use cheap checks while iterating; expensive evidence at the release candidate.**
9. **Turn repeated failures into tooling.** A recurring mistake should become a rule, check, template, or architectural constraint.

## Repository layout

```text
.
├── AGENTS.md
├── context/
│   ├── CURRENT_TASK.md
│   └── PROJECT_STATE.md
├── plans/
│   └── CHANGE_PLAN_TEMPLATE.md
├── docs/
│   ├── WORKFLOW.md
│   ├── EVIDENCE.md
│   ├── SAFETY_BOUNDARIES.md
│   └── ADOPTION.md
├── checks/
│   ├── fast_check.py
│   └── release_gate.py
└── evidence/
    └── release-evidence.json
```

## Try it

Requires only Python 3.11+.

Fast structural check:

```bash
python checks/fast_check.py
```

Final gate:

```bash
python checks/release_gate.py
```

The final gate is expected to fail in a fresh clone because `evidence/release-evidence.json` intentionally starts as **unverified**. That is the point: a release gate should require evidence, not manufacture confidence.

## How to use this in a real repository

1. Copy the files you want into your repository.
2. Replace `context/PROJECT_STATE.md` with the actual project authority and protected boundaries.
3. Rewrite `context/CURRENT_TASK.md` for the current change.
4. Use `plans/CHANGE_PLAN_TEMPLATE.md` for non-trivial work.
5. Adapt the checks to the real stack.
6. Make the release evidence point at real tests, screenshots, logs, queries, hashes, or remote read-back.

See [docs/ADOPTION.md](docs/ADOPTION.md) for a gradual adoption path.

## What this is not

- not a prompt collection;
- not a framework that grants an agent unrestricted repository access;
- not a replacement for code review, CI, or production observability;
- not tied to one model, vendor, IDE, or agent runtime;
- not proof that every project needs this much ceremony.

Use the smallest process that matches the actual risk.

## Related case studies

- [Agentic SDLC case study](https://jiyuhenko.github.io/mateus-lemos-figueiredo/cases/agentic-sdlc.html)
- [Violet — tool-using AI assistant (2024)](https://jiyuhenko.github.io/mateus-lemos-figueiredo/cases/violet.html)

---

Built by [Mateus Lemos Figueiredo (Jiyu Henko)](https://jiyuhenko.github.io/mateus-lemos-figueiredo/).
