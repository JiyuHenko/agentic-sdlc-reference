#!/usr/bin/env python3
"""Evidence-aware release gate.

This intentionally fails on a fresh clone until release evidence is marked
verified and tied to a concrete commit/candidate.
"""

from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

fast = subprocess.run(
    [sys.executable, str(ROOT / "checks" / "fast_check.py")],
    cwd=ROOT,
)
if fast.returncode != 0:
    sys.exit(fast.returncode)

evidence_path = ROOT / "evidence" / "release-evidence.json"

try:
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as exc:
    print(f"RELEASE GATE: FAIL — cannot read evidence: {exc}")
    sys.exit(1)

errors = []

if evidence.get("status") != "verified":
    errors.append("status must be 'verified'")

if not evidence.get("candidate"):
    errors.append("candidate must identify the evaluated commit/HEAD")

checks = evidence.get("checks")
if not isinstance(checks, list) or not checks:
    errors.append("checks must contain at least one evidence item")
else:
    for index, item in enumerate(checks, start=1):
        if not isinstance(item, dict):
            errors.append(f"check #{index} must be an object")
            continue
        if not item.get("claim"):
            errors.append(f"check #{index} is missing claim")
        if not item.get("evidence"):
            errors.append(f"check #{index} is missing evidence")

limits = evidence.get("known_limits")
if not isinstance(limits, list):
    errors.append("known_limits must be a list (empty is allowed)")

if errors:
    print("RELEASE GATE: NOT READY")
    for error in errors:
        print(f"  - {error}")
    print("\nThis is expected until a real release candidate has evidence.")
    sys.exit(1)

print("RELEASE GATE: PASS")
print(f"  candidate: {evidence['candidate']}")
print(f"  evidence items: {len(checks)}")
print(f"  known limits: {len(limits)}")
