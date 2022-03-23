from dataclasses import dataclass, field
from typing import List
from account import Account
from transaction import Transaction


@dataclass
class Deposite:
    account: Account
    amount: int

    @property
    def transaction_details(self):
        return f"added {self.amount} to {self.account.name}"

    def execute(self):
        self.account.deposite(amount=self.amount)
        print(self.transaction_details)

    def undo(self):
        self.account.withdraw(amount=self.amount)
        print(f"UNDID {self.transaction_details}")

    def redo(self):
        self.account.deposite(amount=self.amount)
        print(f"REDID {self.transaction_details}")


@dataclass
class Withdraw:
    account: Account
    amount: int

    @property
    def transaction_details(self):
        return f"Withdraw {self.amount} from {self.account.name}"

    def execute(self):
        self.account.withdraw(amount=self.amount)
        print(self.transaction_details)

    def undo(self):
        self.account.deposite(amount=self.amount)
        print(f"UNDID {self.transaction_details}")

    def redo(self):
        self.account.withdraw(amount=self.amount)
        print(f"REDID {self.transaction_details}")


@dataclass
class Transfer:
    from_account: Account
    to_account: Account
    amount: int

    @property
    def transaction_details(self):
        return f"transfered {self.amount} from {self.from_account.name} to {self.to_account.name}"

    def execute(self):
        self.from_account.withdraw(amount=self.amount)
        self.to_account.deposite(amount=self.amount)
        print(self.transaction_details)

    def undo(self):
        self.from_account.deposite(amount=self.amount)
        self.to_account.withdraw(amount=self.amount)
        print(f"UNDID {self.transaction_details}")

    def redo(self):
        self.from_account.withdraw(amount=self.amount)
        self.to_account.deposite(amount=self.amount)
        print(f"REDID {self.transaction_details}")


@dataclass
class Batch:
    commands: List[Transaction] = field(default_factory=list)

    def execute(self):
        completed_commands: List[Transaction] = []
        try:
            for command in self.commands:
                command.execute()
                completed_commands.append(command)
        except ValueError:
            for command in reversed(completed_commands):
                command.undo()

    def undo(self):
        for command in reversed(self.commands):
            command.undo()

    def redo(self):
        for command in self.commands:
            command.redo()
