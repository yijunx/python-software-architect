# well it just means single responsibility


class PaymentProcessor:
    """the issue is, if we want to add a new payment, we need to modify this class
    which we dont want, we want to adhere to the open close system"""

    def pay_credit(self, order, security_code):
        print(f"CREDDIT, security code is {security_code}")
        order.status = "paid"

    def pay_debit(self, order, security_code):
        print(f"DEBITTT, security code is {security_code}")
        order.status = "paid"


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


if __name__ == "__main__":
    order = Order()

    order.add_item("coke", 8, 3)
    order.add_item("bruh", 3, 8)
    print(order.total_price())

    p = PaymentProcessor()

    p.pay_credit(order=order, security_code="99999")

    print(order.status)
