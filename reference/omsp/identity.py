"""Identity and sybil-gate for OMSP reference."""
from .config import Config
from .core import Ledger
import hashlib
import secrets

class Identity:
    def __init__(self, ledger: Ledger, config: Config):
        self.ledger = ledger
        self.config = config
        self.agents = {}

    def register(self, name: str, stake: float, pow_nonce: Optional[str] = None):
        if stake < self.config.stake_required:
            raise ValueError("insufficient stake")
        # Full PoW check and ledger append in original
        agent_id = hashlib.sha256(f"{name}|{secrets.token_hex(8)}".encode()).hexdigest()[:16]
        self.agents[agent_id] = {"name": name, "stake": stake, "rep": 0.0}
        return agent_id

# Full original from audited package will replace this temporary structure.
