from abc import ABC, abstractclassmethod
from typing import Dict, List


class BasicRuleStoreAdaptor(ABC):
    @abstractclassmethod
    def add_rule(rule: str):
        pass

    @abstractclassmethod
    def get_rules():
        pass

    # @abstractclassmethod
    # def another():
    #     pass


class ListRuleStoreAdaptor(BasicRuleStoreAdaptor):

    rules = []
    rule_groups = []
    rule_books = []

    def __init__(self) -> None:
        super().__init__()

    def add_rule(self, rule: str):
        self.rules.append(rule)

    def get_rules(self):
        return self.rules


if __name__ == "__main__":
    list_rule_store = ListRuleStoreAdaptor()
    list_rule_store.add_rule("xxx")
    print(list_rule_store.get_rules())
