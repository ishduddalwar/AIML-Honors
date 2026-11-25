from abc import ABC, abstractmethod
from methods import make_method


class Provider(ABC):

    def __init__(self, label, charge_rate):
        self.label = label
        self.charge_rate = charge_rate

    @abstractmethod
    def key(self):
        pass

    def pay(self, pay_type, amount, **kwargs):
        m = make_method(self.key(), pay_type, **kwargs)
        print(f"\n{self.label} -> {m.describe()}")

        charge = round(amount * self.charge_rate, 2)
        final = amount + charge
        print(f"  Amount  : Rs {amount}")
        print(f"  Charge  : Rs {charge} ({self.charge_rate * 100:.1f}%)")
        print(f"  Payable : Rs {final}")

        return m.run(final)


class PaytmProvider(Provider):
    def __init__(self):
        super().__init__("Paytm", 0.015)

    def key(self):
        return "paytm"


class StripeProvider(Provider):
    def __init__(self):
        super().__init__("Stripe", 0.029)

    def key(self):
        return "stripe"


_providers = {
    "paytm": PaytmProvider,
    "stripe": StripeProvider,
}


def pick_provider(name):
    name = name.lower()
    if name not in _providers:
        raise ValueError(f"No provider called '{name}'")
    return _providers[name]()
