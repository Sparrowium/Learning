num1 = float(input("Enter number1: "))
num2 = float(input("Enter number2: "))
num3 = float(input("Enter number3: "))


if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num2:
    num1, num2 = num2, num1


print("The sorted numbers are ", num1, num2, num3)