# orginal code
class Order:
    """does way too many things, does something the order should not be doing.."""

    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        """well this is part of order"""
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        """well could be ..."""
        return sum([x * y for x, y in zip(self.quantities, self.prices)])

    def pay(self, payment_type, security_code):
        """definitely it is not belonging to order..
        when we want to change how to pay, we dont want to change order class
        """
        if payment_type == "debit":
            print(f"DEBITTT, security code is {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print(f"CREDDIT, security code is {security_code}")
            self.status = self.status = "paid"
        else:
            raise Exception("not a good payment type")


if __name__ == "__main__":
    order = Order()

    order.add_item("coke", 8, 3)
    order.add_item("bruh", 3, 8)
    print(order.total_price())

    order.pay("debit", "uu8u8u8u")

    print(order.status)
