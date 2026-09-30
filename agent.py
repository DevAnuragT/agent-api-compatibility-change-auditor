
#!/usr/bin/env python3
"""Deterministic, local-only passport implementation."""
import json
import math
import sys
from pathlib import Path

DOMAIN = 'API Compatibility Change Auditor'

def _num(value, name, findings):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(float(value)):
        findings.append(f"{name}: must be a finite number")
        return 0
    return value

def analyze(payload):
    if not isinstance(payload, dict):
        raise ValueError("payload must be an object")
    findings = []
    old=payload.get("previous"); new=payload.get("current"); bump=payload.get("version_bump")
    if not isinstance(old,dict) or not isinstance(new,dict): raise ValueError("previous and current contracts must be objects")
    breaking=[]
    for endpoint, fields in old.items():
        if endpoint not in new: breaking.append(f"removed endpoint {endpoint}"); continue
        for field, typ in fields.items():
            if field not in new[endpoint]: breaking.append(f"removed field {endpoint}.{field}")
            elif new[endpoint][field] != typ: breaking.append(f"type changed {endpoint}.{field}: {typ} -> {new[endpoint][field]}")
    findings.extend(breaking)
    if breaking and bump not in ("major", "breaking"): findings.append("breaking changes require major/breaking version bump")
    if not breaking and bump == "major": findings.append("major bump declared without detected structural breaking change; review rationale")
    return {"domain": DOMAIN, "status": "needs-review" if findings else "ready", "findings": findings}

if __name__ == "__main__":
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    payload = json.loads(source.read_text(encoding="utf-8") if source else sys.stdin.read())
    print(json.dumps(analyze(payload), indent=2, sort_keys=True))
