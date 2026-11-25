from abc import ABC, abstractmethod


class PayMethod(ABC):

    @abstractmethod
    def describe(self):
        pass

    @abstractmethod
    def run(self, amount):
        pass


class PaytmCard(PayMethod):
    def __init__(self, card_no):
        self._card = card_no

    def describe(self):
        return f"Card ending {self._card[-4:]}"

    def run(self, amount):
        print(f"  Paytm charged Rs {amount:.2f} to card")
        return True


class PaytmUPI(PayMethod):
    def __init__(self, upi_handle):
        self._handle = upi_handle

    def describe(self):
        return f"UPI handle: {self._handle}"

    def run(self, amount):
        print(f"  Paytm charged Rs {amount:.2f} via UPI")
        return True


class StripeCard(PayMethod):
    def __init__(self, card_no):
        self._card = card_no

    def describe(self):
        return f"Card ending {self._card[-4:]}"

    def run(self, amount):
        print(f"  Stripe charged Rs {amount:.2f} to card")
        return True


class StripeUPI(PayMethod):
    def __init__(self, upi_handle):
        self._handle = upi_handle

    def describe(self):
        return f"UPI handle: {self._handle}"

    def run(self, amount):
        print(f"  Stripe charged Rs {amount:.2f} via UPI")
        return True


_methods = {
    ("paytm", "card"): PaytmCard,
    ("paytm", "upi"): PaytmUPI,
    ("stripe", "card"): StripeCard,
    ("stripe", "upi"): StripeUPI,
}


def make_method(provider_key, pay_type, **kwargs):
    pair = (provider_key.lower(), pay_type.lower())
    if pair not in _methods:
        raise ValueError(f"No method for {provider_key}/{pay_type}")
    return _methods[pair](**kwargs)
