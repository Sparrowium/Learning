money = int(input("money: "))

dollars = money // 100
remains = money % 100
quarters = remains // 25
remains = remains % 25
dimes = remains // 10
remains = remains % 10
nickels = remains // 5
remains = remains % 5
penny = remains // 1

print("dollars", dollars)
print("quarters", quarters)
print("dimes", dimes)
print("nickels", nickels)
print("pennies", penny)