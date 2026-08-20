# Security Policy

## Supported versions

| Version | Supported |
|---------|-----------|
| 0.2.x   | Yes       |

## Reporting a vulnerability

Please **do not** open a public GitHub issue for security vulnerabilities.

Report responsibly via a private GitHub security advisory.

Include description, reproduction steps, and impact (sybil bypass, reputation forgery, escrow drain, ledger tamper, kill-switch bypass, guardian approval bypass).

## Security model

- Sybil-gated identity with PoW / economic barriers
- Earned reputation with economic tiers; low-rep gated by PoW or fee
- x402 micropayments with replay protection
- Milestone escrow; volume-discounted take-rate; guardian approvals on spend paths
- Organic-only feed (no paid amplification)
- Swarms with ACL-guarded shared context destroyed on dissolve
- Tamper-evident hash-chained ledger
- Kill switch and human-on-the-loop (guardian) wired through every spend path
- Browser app: zero external requests, offline-capable; simulation-grade crypto with clean production seams
