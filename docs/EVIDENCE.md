# Evidence, not status

Coding agents often produce convincing status reports. The workflow should care about a different question:

> What observation would actually prove this claim?

## Claim → evidence mapping

| Claim | Weak evidence | Stronger evidence |
| --- | --- | --- |
| “The page works” | build passed | intended route rendered in target viewport/state |
| “The button works” | screenshot shows button | interaction changes real runtime state as intended |
| “The upload succeeded” | API returned 200 | remote object read back and content/integrity checked |
| “The config changed” | write call succeeded | authoritative config read back with expected value |
| “The artifact is valid” | file exists | content opened/parsed/hashed and tied to evaluated HEAD |
| “The bug is fixed” | code looks right | original failure reproduced, then regression passes |
| “Deployment is live” | deploy command succeeded | deployed version/health/state observed remotely |

## Evidence should be close to authority

Prefer evidence from the system that owns the truth.

Examples:

- database → query the database;
- Git branch → read the remote branch HEAD;
- object storage → read the uploaded object;
- production route → request/render the deployed route;
- UI behavior → execute the interaction in runtime.

## Screenshots are evidence only for visual claims

A screenshot can prove layout, text, or visible state.

It usually cannot prove:

- a click handler is wired;
- persistence occurred;
- authorization is correct;
- the screenshot came from the expected route;
- production matches the local fixture.

For critical states, pair visual evidence with runtime or state evidence.

## Keep evidence attached to a specific candidate

If the code changes after a heavy validation run, that evidence may be stale.

Record the evaluated HEAD/commit in `evidence/release-evidence.json`.

## Known limits are part of evidence

If production access is unavailable, say so.

If browser automation could not run, say so.

If a third-party sandbox was used instead of the real service, say so.

A precise limitation is more trustworthy than a broad “all good.”
