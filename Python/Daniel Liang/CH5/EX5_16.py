num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
k = 0

for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        k = i


print(k)