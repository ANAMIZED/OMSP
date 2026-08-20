# Contributing to OMSP

## The contract

1. Offline / zero-external-request path for `omsp.html` must continue to boot and exercise the full protocol
2. Guardian approvals, kill switch, and spend-path gates remain fail-closed
3. Both the Python reference and browser engine must stay in parity with the 44-REQ SPEC
4. Prefer small, focused changes
5. Regenerate parity / TRACEABILITY / build artifacts when touching core protocol logic

Read `AGENTS.md` before changing code.

## Setup

```bash
# Live app
open omsp.html   # or any static server

# Python
cd reference && python3 -m unittest discover -s tests

# Browser sources (Node ≥ 18)
cd app && node test_engine.js
```

## Verification

```bash
bash scripts/verify.sh
```

## PRs

- Small, focused changes
- Describe why / what / how verified
- Update README.md or AGENTS.md when public surfaces change
- Keep `omsp.html` byte-reproducible via `python3 app/build.py`
