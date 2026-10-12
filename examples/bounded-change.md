# Example — bounded change

This is a deliberately generic example of how a small task can be framed.

## Request

“Add validation so an empty project name cannot be submitted.”

## Classification

Bounded.

## Failure

Submitting an empty string currently reaches the persistence layer.

## Hypothesis

The UI checks field presence visually, but the submit boundary does not enforce the same invariant.

## Scope

Expected:

- form validation;
- nearest submit handler;
- regression test.

Out of scope:

- redesigning the form;
- changing database schema;
- replacing the validation library.

## Verify

1. reproduce empty submission before the fix;
2. add the boundary validation;
3. add a regression test for empty/whitespace input;
4. verify a valid project name still submits;
5. inspect the diff for unrelated form changes.

## Why this matters

The plan is small, but it already tells an agent what **not** to do and how completion will be proven.
