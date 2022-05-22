# this is the adaptor interface

from typing import Protocol, Any


class Config(Protocol):
    def get(self, key: str, default: Any = None) -> Any | None:
        """returns the value associated with the key"""
