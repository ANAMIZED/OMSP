"""Core ledger and hash-chain primitives for OMSP reference."""
import hashlib
import time
from typing import Any, Dict, List, Optional

class Ledger:
    def __init__(self):
        self.blocks: List[Dict[str, Any]] = []
        self.height = 0

    def _hash(self, data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()

    def append(self, event: Dict[str, Any]) -> Dict[str, Any]:
        prev = self.blocks[-1]["hash"] if self.blocks else "0" * 64
        payload = f"{prev}|{self.height}|{event}|{time.time()}"
        h = self._hash(payload)
        block = {"height": self.height, "prev": prev, "event": event, "hash": h, "ts": time.time()}
        self.blocks.append(block)
        self.height += 1
        return block

    def verify_chain(self) -> bool:
        for i, b in enumerate(self.blocks):
            if i == 0:
                continue
            if b["prev"] != self.blocks[i-1]["hash"]:
                return False
        return True

# Full original implementation is in the audited ZIP; this stub is temporary to unblock CI structure.
