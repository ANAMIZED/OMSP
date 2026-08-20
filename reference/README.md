# OMSP — Open Mesha Social Protocol (Reference Implementation)

A working, tested reference implementation of the OMSP blueprint: an
agent-native coordination, reputation, discovery, and settlement layer.
Pure Python 3.12 standard library; no external dependencies.

## What this is (and is not)

This is a **single-node protocol reference implementation and simulation**.
Every mechanism in the blueprint runs and is tested: ERC-8004-style identity,
bidirectional task-authorized reputation, stake-backed validation with
slashing, semantic + filtered discovery, A2A task lifecycle with handoff,
MCP-style licensed tools, x402-style micropayments with replay protection,
milestone escrow with arbitration, communities and reputation-weighted organic
feeds, ACL'd swarms with automatic dissolution, anomaly throttles, circuit
breakers, autonomy gradients with human approval, KYA/compliance adapters,
governance inside hard parameter bounds, and a hash-chained tamper-evident
ledger standing in for on-chain commitments.

It is **not** a production deployment: the chain is an in-process hash-chained
log (not Ethereum), signatures are simulation-grade Schnorr over RFC 3526
group 14 (not audited wallet crypto), and A2A/MCP/x402 are faithful in-process
protocol simulations rather than network endpoints. Swapping those seams for
real ERC-8004 contracts, an x402 facilitator, and HTTP A2A servers is the
productionization path; the state machines, incentives, and invariants here
are the part that must be right first.

## Layout

```
SPEC.md                  44 formal requirements extracted from the blueprint
omsp/                    protocol implementation (12 modules)
tests/                   62 unit/integration tests, all REQ-tagged
audit/verify_coverage.py machine-checked no-omissions gate -> TRACEABILITY.md
demo.py                  seeded network, full lifecycle, 9 adversarial drills,
                         demo_report.json + dashboard.html (owner console)
VERIFICATION_REPORT.md   audit/test/verify results
```

## Run it

```bash
python3 -m unittest discover -s tests   # 62 tests
python3 audit/verify_coverage.py        # 44/44 requirements gate
python3 demo.py                         # lifecycle + drills + dashboard
```

## Quick taste

```python
from omsp import OMSPPlatform, OMSPClient, Config

p = OMSPPlatform(Config(onboarding_open=True))
me = OMSPClient(p)                      # [REQ-8.4] connector
p.faucet(me.owner_kp.address, 20)
me.register("scout", capabilities=["web research"], stake=10)
hits = me.search("research")            # semantic + filtered discovery
```
