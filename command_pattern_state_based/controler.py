from dataclasses import dataclass, field
from typing import List
from transaction import Transaction


@dataclass
class BankControler:  # state based
    """it keeps track of the UNDO/REDO list"""

    undo_stack: List[Transaction] = field(default_factory=list)
    redo_stack: List[Transaction] = field(default_factory=list)

    def execute(self, transaction: Transaction):
        transaction.execute()
        self.redo_stack.clear()
        self.undo_stack.append(transaction)

    def undo(self):
        if not self.undo_stack:
            return
        
        transaction = self.undo_stack.pop()
        transaction.undo()
        self.redo_stack.append(transaction)

    
    def redo(self):
        if not self.redo_stack:
            return
        
        transaction = self.redo_stack.pop()
        transaction.redo()
        self.undo_stack.append(transaction)


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


