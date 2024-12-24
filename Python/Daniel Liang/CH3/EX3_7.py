total = float(input("Enter an amount in float: "))


print(f"Your amount of {total} consists of")


total *= 100
dollar = int(total // 100)
quarter = int(total % 100 // 25)
dime = int(total % 100 % 25 // 10)
nickel = int(total % 100 % 25 % 10 // 5)
penny = int(total % 100 % 25 % 10 % 5)

if dollar != 0:
    print(f"{dollar} \t", "dollars" if dollar > 1 else "dollar")
if quarter != 0:
    print(f"{quarter} \t", "quarters" if quarter > 1 else "quarter")
if dime != 0:
    print(f"{dime} \t", "dimes" if dime > 1 else "dime")
if nickel != 0:
    print(f"{nickel} \t", "nickels" if nickel > 1 else "nickel")
if penny != 0:
    print(f"{penny} \t", "pennies" if penny > 1 else "penny")

