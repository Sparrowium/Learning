exchange_rate = float(input("Enter the exchange rate from dollars to RMB: "))
choice = int(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))


if choice == 0:
    amount = float(input("Enter the dollar amount: "))
    print(amount, "dollars is", amount * exchange_rate, "Yuan")
if choice == 1:
    amount = float(input("Enter the RMB amount: "))
    print(amount, "Yuan is", amount / exchange_rate, "dollars")