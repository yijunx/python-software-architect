# open for add new functions
# close for modify old functions


from abc import abstractclassmethod, ABC


class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        return sum([x * y for x, y in zip(self.quantities, self.prices)])


class PaymentProcessor(ABC):
    @abstractclassmethod
    def pay(self, order: Order, security_code: str):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str):
        print(f"DEBITTT, security code is {security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str):
        print(f"CREDIT, security code is {security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
    """though it is easy to add another payment type
    but it can be abused (here we use email as security code)

    so we should do something special with security code or email
    to properly deal with the case, this can be done with a initialize

    def __init__

    by liskov's substitution principle

    if we can replace the instance of their subclass,
    without altering the correctness of the program
    """

    def pay(self, order: Order, email: str):
        print(f"PAYPAL, email is {email}")
        order.status = "paid"


# if we want to add another payment processor, no need to modiy old code..
if __name__ == "__main__":
    order = Order()

    order.add_item("coke", 8, 3)
    order.add_item("bruh", 3, 8)
    print(order.total_price())

    p = PaypalPaymentProcessor()

    p.pay(order, "99999")

    print(order.status)
