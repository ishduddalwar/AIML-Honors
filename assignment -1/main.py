from providers import pick_provider


def start():
    print("\n-- Payment System --")
    prov_name = input("Choose provider (paytm/stripe): ").strip().lower()
    prov = pick_provider(prov_name)

    pay_type = input("Pay via (card/upi): ").strip().lower()

    if pay_type == "card":
        cnum = input("Enter card number: ").strip()
        info = {"card_no": cnum}
    elif pay_type == "upi":
        uid = input("Enter UPI handle: ").strip()
        info = {"upi_handle": uid}
    else:
        print("Unsupported payment type.")
        return

    amt = float(input("Enter amount (Rs): "))
    if amt <= 0:
        print("Amount must be greater than zero.")
        return

    ok = prov.pay(pay_type, amt, **info)
    if ok:
        print("\nPayment successful.")


if __name__ == "__main__":
    start()
