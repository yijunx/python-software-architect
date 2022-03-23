from dataclasses import dataclass, field
from typing import Dict
from account import Account
from uuid import uuid4


@dataclass
class Bank:
    accounts: Dict[str, Account] = field(default_factory=dict)

    def create_account(self, name: str):
        acc_no = str(uuid4())
        account = Account(name=name, number=acc_no)
        self.accounts[acc_no] = account
        return account

    def get_account(self, acc_no: str):
        return self.accounts[acc_no]
