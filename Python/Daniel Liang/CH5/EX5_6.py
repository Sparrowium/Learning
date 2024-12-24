print("Miles \t Kilometers | Kilometers \t Miles")
for i in range(1, 11):
    print(f"{i} \t {round(i * 1.609, 3):<10} | {round(i * 1.609, 3)} \t\t {i}")