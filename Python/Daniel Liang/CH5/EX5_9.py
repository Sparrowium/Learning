initial_fund = 10000
total = 10000


for i in range(1, 11):
    print(f"{i} \t {round(initial_fund, 2)}")
    initial_fund *= 1.05
    if i < 4:
        total += initial_fund

print()
print(total)