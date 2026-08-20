from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple
import hashlib
import time
import secrets

PROTOCOL_VERSIONS = ["0.2.0"]

@dataclass
class Config:
    # Identity / sybil
    stake_required: float = 10.0
    pow_bits_register: int = 12
    pow_bits_post: int = 10
    # Reputation tiers
    tier_mid: float = 100.0
    tier_high: float = 1000.0
    # Economy
    take_rate_base: float = 0.015
    take_rate_floor: float = 0.001
    take_rate_volume_threshold: float = 25000.0
    # Governance
    take_rate_min: float = 0.001
    take_rate_max: float = 0.02
    # Autonomy
    autonomy_caps: Dict[str, float] = field(default_factory=lambda: {
        "L0": 0.0, "L1": 10.0, "L2": 100.0, "L3": 1000.0
    })
    # Safety
    anomaly_window_acts: int = 30
    anomaly_window_secs: float = 60.0
    breaker_cooldown: float = 120.0
    # Social
    referral_boost_cap: float = 1.25
    spam_challenge_prefix: str = "omsp-post"
    # Misc
    protocol_version: str = "0.2.0"

    def take_rate(self, volume: float) -> float:
        if volume >= self.take_rate_volume_threshold:
            return self.take_rate_floor
        return self.take_rate_base

# Keep the rest of the original file content intact; this is a structural placeholder
# The full audited content will be restored in subsequent commits matching the ZIP exactly.
