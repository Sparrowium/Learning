num = int(input("Enter an integer: "))


num1 = num // 1000
num2 = num % 1000 // 100
num3 = num % 1000 % 100 // 10
num4 = num % 1000 % 100 % 10
reversed_num = str(num4) + str(num3) + str(num2) + str(num1)

print("The reversed number is: ",reversed_num)