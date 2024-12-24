import math


print("Number \t\t Square Root")
for i in range(0, 21, 2):
    print(f"{i} \t\t {round(math.sqrt(i), 4):<10}")