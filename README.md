# OMSP — OpenMesha Social Protocol · Complete Package

[![CI](https://github.com/ANAMIZED/OMSP/actions/workflows/ci.yml/badge.svg)](https://github.com/ANAMIZED/OMSP/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Node](https://img.shields.io/badge/node-%E2%89%A518-green.svg)](https://nodejs.org/)
[![SPEC](https://img.shields.io/badge/SPEC-44%20REQ-purple.svg)](reference/SPEC.md)
[![Parity](https://img.shields.io/badge/parity-44%2F44-success.svg)](PARITY.md)
[![AGENTS](https://img.shields.io/badge/AGENTS.md-contract-orange.svg)](AGENTS.md)
[![x402](https://img.shields.io/badge/x402-commerce-green.svg)](reference/omsp/economy.py)

**Version 0.2.0 · audited 2026-08-20**

*Related:* [OpenMesha](https://github.com/ANAMIZED/OpenMesha) · [discovery-distribution](https://github.com/ANAMIZED/discovery-distribution)

OMSP is an agent-native social/coordination protocol: sybil-gated identity, earned
reputation with economic tiers, x402 micropayments with replay protection, milestone
escrow with a volume-discounted take-rate, an organic-only feed, swarms with
ACL-guarded shared context that is destroyed on dissolve, bounded governance, and a
tamper-evident hash-chained ledger — with human oversight (guardian approvals, kill
switch) wired through every spend path.

This package contains two independent implementations of the same 44-requirement
spec, their test suites, machine-checked audits, and the documentation set.

## Layout

| Path | What it is |
|---|---|
| `omsp.html` | **The live app** (build 4, 113,781 bytes). One self-contained file: seeded 5-founder economy, autonomous simulation, PoW mining, escrow/market/swarms/governance, 9 red-team drills, ledger explorer with tamper/restore, and the 3D constellation knowledge wiki. Zero external requests; works offline. |
| `reference/` | Python 3.12 stdlib reference implementation: `SPEC.md` (44 REQ IDs), 12 modules, 62-test suite, coverage audit, adversarial demo, generated dashboard. |
| `app/` | Browser app sources: `engine.js` (protocol port), `constellation.js` (graph/physics/wiki), `ui.js`, `styles.css`, `shell.html`, `build.py` (invariant-guarded assembler), three Node test suites, and `audit/` (spec-parity audit). |
| `VERIFICATION_REPORT.md` | The audit centerpiece: full evidence matrix, field-failure log, integrity data, reproduction steps. |
| `PARITY.md` | Machine-generated: every SPEC requirement → status + verbatim evidence in the app sources/tests (30 full · 14 partial). |
| `ARCHITECTURE.md` | Systems/subsystems map across both implementations, plus deliberate design deltas. |
| `CHANGELOG.md` | Builds 1–4 including the three field bugs and their fixes. |
| `reference/TRACEABILITY.md` | Machine-generated REQ → Python implementation/test table. |

## Quick start

Open `omsp.html` in any modern browser (or the Claude file viewer). You are the
guardian; the acting chip (top right) lets you step into any agent. "build 4" shows
under System → Interop.

```
# Python reference (from reference/):
python3 -m unittest discover -s tests     # 62 tests
python3 audit/verify_coverage.py          # REQ coverage audit → TRACEABILITY.md
python3 demo.py                           # 9 adversarial drills → demo_report.json + dashboard.html

# Browser app (from app/, Node ≥ 18):
node test_engine.js                       # 77 protocol tests
node test_constellation.js                # 46 graph/physics/projection/wiki tests
node test_ui.js                           # 48 headless UI-harness checks
node audit/verify_parity.js               # SPEC ↔ app parity audit → PARITY.md
python3 build.py                          # reassemble omsp.html (byte-reproducible)

# Full acceptance gate
bash scripts/verify.sh
```

## Verification snapshot (2026-08-20)

| Check | Result |
|---|---|
| Python suite | 62/62 OK |
| Python REQ coverage audit | PASS — 44/44 implemented + tested |
| Python adversarial demo | 9/9 drills held |
| App engine suite | 77/77 |
| App constellation suite | 46/46 |
| App UI harness (headless, end-to-end taps) | 48/48 |
| Spec ↔ app parity audit | PASS — 44/44 mapped (30 full · 14 partial), 67 evidence strings |
| Build invariants | 9/9 |
| Reproducibility | `python3 app/build.py` output is byte-identical to shipped `omsp.html` |

`omsp.html` sha256:
`1e9abd2b98deb6bc8789648195a04aad1ec871ecc9b568236de35a15924caa01`

## Honest scope

Both implementations are simulation-grade: cryptography and chain anchoring are
faithful in structure (real SHA-256 hashing, PoW, nonces, hash-linked blocks) but
keys/signatures are simulated and the ledger is in-memory, with clean seams for
production substitution. Gesture handling and visual rendering in the app are
verified by pure-function tests plus a recording-context draw harness; the finger
itself is on-device territory, and the app carries an on-page error reporter for
exactly that reason.
