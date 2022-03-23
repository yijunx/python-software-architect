from dataclasses import dataclass


@dataclass
class Account:
    name: str
    number: str
    _computed_cache: int = 0

    def deposite(self, amount: int):
        self._computed_cache += amount

    def withdraw(self, amount: int):
        if amount > self._computed_cache:
            raise ValueError("cannot withdraw that much...")
        self._computed_cache -= amount
    
    def clear_cache(self):
        self._computed_cache = 0
