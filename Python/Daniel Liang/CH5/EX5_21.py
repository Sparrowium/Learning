num = int(input("Enter a power for 2: "))

for i in range(0, num + 1):
    for j in range(1, num - i + 1):
        print(end= "    ")
    for j in range(0, i + 1):
        print(f"{(2 ** j):4}", end="")
    for j in range(i - 1 , -1, -1):
        print(f"{(2 ** j):4}", end="")
    print()
