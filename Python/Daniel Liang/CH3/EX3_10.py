import random


num1 = random.randint(0, 100)
num2 = random.randint(0, 100)



answer = float(input(f"What is {num1} * {num2} ? "))


if answer == (num1 * num2):
    print("Your answer is True")
else:
    print("Your answer is False")
    print(f"{num1} * {num2} should be ", num1 * num2)