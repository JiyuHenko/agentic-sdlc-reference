# Safety boundaries

Agentic development becomes safer when authority is explicit.

## Capability boundaries

Prefer narrow tools over generic authority.

Safer:

- update one file;
- query one table;
- deploy one preview;
- read one environment;
- invoke one documented operation.

Riskier:

- unrestricted shell;
- arbitrary production SQL;
- broad cloud credentials;
- generic write access to every remote system.

Use broad capabilities only when they are genuinely required and protected by the surrounding workflow.

## Side effects

Before destructive, expensive, public, or irreversible actions:

- confirm the task actually requires the side effect;
- identify rollback/recovery;
- use human approval when appropriate;
- validate the target;
- read back the result.

Examples:

- production deploy;
- database migration;
- deletion;
- customer-facing email/message;
- billing action;
- secret rotation;
- publishing content.

## Secrets

Never place real secrets in:

- prompts;
- source files;
- screenshots;
- logs;
- issue/PR text;
- generated evidence committed to the repository.

Use the platform's secret store and pass the minimum required secret to the minimum required process.

## AI inside products

If AI produces interpretations, summaries, or recommendations, decide whether it is **advisory** or **authoritative**.

For high-value product state, keep canonical facts in deterministic systems where possible.

Examples that often should remain authoritative outside the model:

- identity;
- permissions;
- billing;
- entitlements;
- progress records;
- audit state;
- feature flags.

## Remote writes

A successful write response proves that the request was accepted. It may not prove the intended state persisted.

For important writes:

1. write;
2. read back;
3. compare with expected state;
4. only then report success.

## Least surprising automation

Do not hide impactful side effects inside a harmless-sounding step.

The user/reviewer should be able to tell when the workflow crosses from analysis into mutation.
