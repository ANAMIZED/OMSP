"""Discovery and resolution for OMSP reference."""
from .config import Config
from .core import Ledger

class Discovery:
    def __init__(self, ledger: Ledger, config: Config):
        self.ledger = ledger
        self.config = config
        self.cards = {}

    def search(self, query: str):
        return [c for c in self.cards.values() if query.lower() in str(c).lower()]

    def resolve(self, agent_uri: str):
        return self.cards.get(agent_uri)

# Full original from audited package will replace this temporary structure.
