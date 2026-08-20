"""Open Mesha Social Protocol (OMSP) -- reference implementation."""
from .config import Config, PROTOCOL_VERSIONS
from .platform import OMSPPlatform
from .sdk import AltMinimalClient, OMSPClient

__all__ = ["Config", "PROTOCOL_VERSIONS", "OMSPPlatform", "OMSPClient",
           "AltMinimalClient"]
__version__ = "0.2.0"
