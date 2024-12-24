amount = float(input("Enter monthly saving amount: "))


interest_rate = 0.05 / 12


print("After 6 months, the account value is: ", amount * (((1 + interest_rate) ** 7 - 1) / interest_rate) - amount)