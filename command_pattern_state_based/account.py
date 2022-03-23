from dataclasses import dataclass


@dataclass
class Account:
    name: str
    number: str
    balance: int = 0

    def deposite(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        if amount > self.balance:
            raise ValueError("cannot withdraw that much...")
        self.balance -= amount
