"""Shared helpers for the OMSP test suite."""
from __future__ import annotations

from omsp import Config, OMSPPlatform
from omsp import core


def make_platform(**overrides) -> OMSPPlatform:
    cfg = Config(onboarding_open=True, **overrides)
    return OMSPPlatform(cfg)


def make_agent(p: OMSPPlatform, name: str, *, usdc: float = 1000.0,
               om: float = 0.0, capabilities=None, services=None,
               vertical="general", jurisdiction="any", autonomy_level: int = 3,
               stake: float = 10.0, referrer=None):
    owner = core.KeyPair.generate()
    p.faucet(owner.address, stake + 1.0)
    agent = p.identity.register(
        owner, name, capabilities=capabilities or [],
        services=services or [], vertical=vertical, jurisdiction=jurisdiction,
        stake=stake, autonomy_level=autonomy_level, referrer=referrer)
    if usdc:
        p.faucet(agent.token_id, usdc)
    if om:
        p.faucet(agent.token_id, om, "OM")
    agent._owner_kp = owner  # test convenience
    return agent


def boost_rep(p: OMSPPlatform, agent_id: int, kinds=("auto_success",), n=10):
    """Directly append reputation entries to reach a target tier quickly."""
    for _ in range(n):
        for k in kinds:
            p.reputation.entries.append(
                {"kind": k, "frm": None, "to": agent_id, "task": "seed",
                 "ts": p.clock.now()})
