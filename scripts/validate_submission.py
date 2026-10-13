#!/usr/bin/env python3
"""Structural checks for the six Capstone B submission artifacts.

This script checks file presence, notebook JSON validity, cell error outputs, and
remaining learner placeholders. It does not prove clinical validity or replace
a full Colab execution with the official dataset/model backend.
"""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "adk_foundations.ipynb",
    "data_understanding_and_baseline.ipynb",
    "agent_pipeline_development.ipynb",
    "agent_evaluation_and_optimisation.ipynb",
    "sahayak_starter.py",
    "final_report.pdf",
]
PLACEHOLDERS = ("# FILL IN", "# YOUR FILE", "# YOUR DESIGN NOTES", "FILL IN diagnosis")

def main():
    failures = []
    for name in REQUIRED:
        path = ROOT / name
        if not path.is_file() or path.stat().st_size == 0:
            failures.append(f"Missing/empty required artifact: {name}")
            continue
        if path.suffix == ".ipynb":
            try:
                nb = json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:
                failures.append(f"Invalid notebook JSON ({name}): {exc}")
                continue
            cells = nb.get("cells", [])
            errors = []
            unexecuted_code = []
            placeholders = []
            for idx, cell in enumerate(cells):
                source = "".join(cell.get("source", []))
                if any(p.lower() in source.lower() for p in PLACEHOLDERS):
                    placeholders.append(idx)
                if cell.get("cell_type") == "code":
                    if cell.get("execution_count") is None:
                        unexecuted_code.append(idx)
                    for out in cell.get("outputs", []):
                        if out.get("output_type") == "error":
                            errors.append((idx, out.get("ename"), out.get("evalue")))
            if errors:
                failures.append(f"{name}: error outputs: {errors[:5]}")
            if placeholders:
                print(f"WARNING {name}: placeholder markers in cells {placeholders}")
            if unexecuted_code:
                print(f"WARNING {name}: unexecuted code cells {unexecuted_code}")
            print(f"OK {name}: {len(cells)} cells; {len(unexecuted_code)} unexecuted code cells; {len(errors)} error outputs")
        else:
            print(f"OK {name}: {path.stat().st_size} bytes")
    if failures:
        print("\nFAILURES:")
        for failure in failures:
            print("-", failure)
        return 1
    print("\nStructural checks passed. This is not a substitute for full dataset-backed Colab evaluation.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
