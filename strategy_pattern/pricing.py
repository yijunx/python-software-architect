# here is the question

# item qty range | total price
# 1 - 2          | 5
# 3 - 5          | 8
# 6 - 9          | 11
# 10 - 13        | 15
# 14 - 18        | 20

# implement above login without if else

# the if else way


from abc import ABC, abstractmethod


def get_total_price_if_else(total_qty: int) -> int:
    """the most dumb"""
    if total_qty > 18:
        raise Exception("too many")
    elif total_qty >= 13:
        return 20
    # and so on....
    ...


pricing_dict = {18: None, 13: 20, 9: 15, 5: 11, 2: 8, 0: 5}


def get_total_price_with_dict_if_else(total_qty: int) -> int:
    """a bit better"""
    for k, v in pricing_dict.items():
        # python dict is somewhat ordered...
        # but it is better to use orderedDict
        if total_qty > k:
            if v is None:
                raise ("too many")
            return v


##############################################
############ strategy pattern ################
##############################################


class PricingStrategy(ABC):
    @abstractmethod
    def get_total_price(self, total_qty: int) -> int:
        ...


class PricingStrategyTooMany(PricingStrategy):
    def get_total_price(self) -> int:
        raise Exception("too many")


class PricingStrategy14to18(PricingStrategy):
    def get_total_price(self) -> int:
        return 20


class PricingStrategy10to13(PricingStrategy):
    def get_total_price(self) -> int:
        return 15


class PriceCalculator:
    def __init__(self, strategy: PricingStrategy) -> None:
        self.strategy = strategy

    def calculate_total_price(self):
        return self.strategy.get_total_price()


def get_total_price_without_if_else(total_qty: int) -> int:
    for k, v in pricing_dict.items():
        if total_qty > k:
            if v is None:
                raise Exception("too many")
            return v
    raise Exception("qty must be > 0 bro")
