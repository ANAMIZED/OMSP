# AGENTS.md — OMSP (OpenMesha Social Protocol)

This file is the contract for any AI coding agent working on this repository.

## What this project is

OMSP is an agent-native social/coordination protocol: sybil-gated identity, earned
reputation with economic tiers, x402 micropayments with replay protection, milestone
escrow with a volume-discounted take-rate, an organic-only feed, swarms with
ACL-guarded shared context that is destroyed on dissolve, bounded governance, and a
tamper-evident hash-chained ledger — with human oversight (guardian approvals, kill
switch) wired through every spend path.

This package contains two independent implementations of the same 44-requirement
spec (browser single-file app + Python 3.12 stdlib reference), their test suites,
machine-checked audits, and the documentation set.

A senior engineer with only the source and `README.md` must be able to open the
live app, run every test suite, and verify end-to-end via `scripts/verify.sh`.

## How to run & verify

```bash
# Open the live app (zero external requests; works offline)
# open omsp.html in any modern browser

# Python reference (from reference/)
python3 -m unittest discover -s tests     # 62 tests
python3 audit/verify_coverage.py          # REQ coverage audit
python3 demo.py                           # 9 adversarial drills

# Browser app (from app/, Node ≥ 18)
node test_engine.js                       # 77 protocol tests
node test_constellation.js                # 46 graph/physics tests
node test_ui.js                           # 48 UI harness checks
node audit/verify_parity.js               # SPEC ↔ app parity
python3 build.py                          # reassemble omsp.html (byte-reproducible)

# Full gate
bash scripts/verify.sh
```

## Hard rules for agents

1. Never break the verify contract (`scripts/verify.sh` must stay green).
2. Fail closed — guardian approvals + kill switch stay hard; never weaken spend paths.
3. Both implementations must remain independent and in parity with the 44-REQ SPEC.
4. Simulation-grade crypto (real SHA-256, PoW, nonces, hash-linked blocks) stays structural; keys/signatures are simulated with clean seams for production.
5. Prefer small, focused changes. Update README.md and AGENTS.md when public surfaces change.
6. Do not omit or alter original audited sources without regenerating parity/TRACEABILITY evidence.
7. Keep offline / zero-external-request path fully functional for the browser app.

## Surfaces that must stay working

- Live app (`omsp.html`) — single-file, offline-capable
- Python reference (`reference/omsp/`) + 62-test suite
- Browser engine (`app/engine.js`) + constellation + UI
- SPEC parity audits (`PARITY.md`, `TRACEABILITY.md`)
- `scripts/verify.sh` (full acceptance gate)
- Build reproducibility (`python3 app/build.py` → byte-identical `omsp.html`)
