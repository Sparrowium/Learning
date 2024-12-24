import math


print("Degree \t\t Sin \t\t Cos")
for i in range(0, 361, 10):
    print(f"{i} \t\t {round(math.sin(math.radians(i)), 4):<10}  \t {round(math.cos(math.radians(i)), 4):<10}")