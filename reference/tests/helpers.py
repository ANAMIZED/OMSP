"""Shared helpers for OMSP reference tests."""

import time
from reference.omsp.core import Platform
from reference.omsp.identity import Identity
from reference.omsp.config import Config

def make_platform(seed: int = 42) -> Platform:
    cfg = Config(seed=seed)
    return Platform(cfg)

def make_agent(platform: Platform, name: str, pow_bits: int = 0) -> Identity:
    """Register a fresh agent with optional PoW."""
    agent = platform.register(name, pow_bits=pow_bits)
    return agent

def advance(platform: Platform, ticks: int = 1):
    for _ in range(ticks):
        platform.tick()

def settle(platform: Platform):
    """Force any pending settlement / escrow resolution."""
    platform.tick()
    platform.economy.flush()
