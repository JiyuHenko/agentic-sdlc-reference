#!/usr/bin/env python3
"""Small structural check for this reference repository.

No external dependencies. Adapt this file to your real project.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "AGENTS.md",
    "context/PROJECT_STATE.md",
    "context/CURRENT_TASK.md",
    "plans/CHANGE_PLAN_TEMPLATE.md",
    "docs/WORKFLOW.md",
    "docs/EVIDENCE.md",
    "docs/SAFETY_BOUNDARIES.md",
    "evidence/release-evidence.json",
]

missing = [path for path in REQUIRED if not (ROOT / path).is_file()]

if missing:
    print("FAST CHECK: FAIL")
    for path in missing:
        print(f"  missing: {path}")
    sys.exit(1)

print(f"FAST CHECK: PASS ({len(REQUIRED)} required files present)")
