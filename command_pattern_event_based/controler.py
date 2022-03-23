from dataclasses import dataclass, field
from typing import List
from transaction import Transaction


@dataclass
class BankEventControler:  # transaction based
    """it keeps ledger, also, we dont need undo redo in the transactons!!!"""


    ledger: List[Transaction] = field(default_factory=list)
    current: int = 0

    def register(self, transaction: Transaction):
        del self.ledger[self.current :]
        self.ledger.append(transaction)
        self.current += 1

    def undo(self):
        if self.current > 1:
            self.current -= 1

    def redo(self):
        if self.current < len(self.ledger):
            self.current += 1

    def compute_balances(self):
        for transaction in self.ledger[: self.current]:
            transaction.execute()


