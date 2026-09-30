# API Compatibility Change Auditor

Compares two endpoint contracts and flags removed or type-changed fields that need explicit breaking-change handling.

## Architecture

```text
JSON payload → domain algorithm → evidence-backed findings → human review
                              └→ OpenAI / CrewAI / Claude Code / Lyzr export surfaces
```

The core implementation is `agent.py` and exposes `analyze(payload)`. Tests include valid, malformed, boundary, and domain-specific cases.

## Run

```bash
python3 agent.py examples/good-input.json
python3 -m unittest discover -s tests -v
python3 tools/audit-api-compatibility-change-auditor.py examples/good-input.json
```

## Limitations

This compares structural field names and types only. It cannot infer behavioral compatibility, wire-level coercion, or every consumer dependency.
