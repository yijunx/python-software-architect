# interface segreation can be done via inheritance or composition
# say we want to add SMS auth to debit and paypal pay method

# here we want to use inheritance
# overall it is better to have several specific interface, instead of one general interface

# say we want to add SMSauth to Payment Processor, but some payment method
# does not require sms auth. this it is better to

# 1 inherent the payment processor, and let that has a sms auth method


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
    def pay(self, order: Order):
        pass


class PaymentProcessorSMS(PaymentProcessor):
    @abstractclassmethod
    def sms_auth(self):
        pass


class DebitPaymentProcessor(PaymentProcessorSMS):
    def __init__(self, security_code) -> None:
        self.security_code = security_code
        self.sms_verified = False

    def pay(self, order: Order):
        if self.sms_verified:
            print(f"DEBITTT, security code is {self.security_code}")
            order.status = "paid"
        else:
            raise Exception("not verified")

    def sms_auth(self):
        print("SMS authorized")
        self.sms_verified = True


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code) -> None:
        self.security_code = security_code

    def pay(self, order: Order):
        print(f"CREDIT, security code is {self.security_code}")
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

    def __init__(self, email) -> None:
        self.email = email

    def pay(self, order: Order):
        print(f"PAYPAL, email is {self.email}")
        order.status = "paid"


# if we want to add another payment processor, no need to modiy old code..
if __name__ == "__main__":
    order = Order()

    order.add_item("coke", 8, 3)
    order.add_item("bruh", 3, 8)
    print(order.total_price())

    p = DebitPaymentProcessor(security_code="0000")
    p.sms_auth()
    p.pay(order) # will raise not verfied if not sms_authed

    print(order.status)
