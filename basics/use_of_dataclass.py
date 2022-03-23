from dataclasses import dataclass


@dataclass
class Exchange:
    name: str

    def get_quote(self):
        return f"quote for {self.name}"


class Strategy:
    def __init__(self, name) -> None:
        self.name = name

    def should_buy(self) -> bool:
        return True


@dataclass
class TradingBot:
    exchange: Exchange
    strategy: Strategy

    def buy(self):
        print(self.exchange.get_quote())
        print(self.strategy.should_buy())


if __name__ == "__main__":
    e = Exchange(name="nihao")
    s = Strategy(name="hi")

    tb = TradingBot(exchange=e, strategy=s)
    tb.buy()
