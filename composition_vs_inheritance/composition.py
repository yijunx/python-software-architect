from dataclasses import dataclass
from typing import Protocol



class FlyStrategy(Protocol):
    def fly(self) -> None:
        ...


class QuackStrategy(Protocol):
    def quack(self) -> None:
        ...


class NormalFlyStrategy:
    def fly(self):
        print("base fly")


class JetFlyStrategy:
    def fly(self):
        print("Jet fly")


class NormalQuackStrategy:
    def quack(self):
        print("normal quack")


class SuperQuackStrategy:
    def quack(self):
        print("super quackkkk!")



@dataclass
class Duck:
    name: str
    fly_strategy: FlyStrategy
    quack_stratefy: QuackStrategy

    def quack(self):
        self.fly_strategy.fly()

    def fly(self):
        self.quack_stratefy.quack()


if __name__ == "__main__":
    # with this composition method it is way more flexible to construct new ducks..
    d = Duck(name="any duck", fly_strategy=JetFlyStrategy(), quack_stratefy=SuperQuackStrategy())
    d.quack()
    d.fly()

