import random


num1 = random.randint(0, 100)
num2 = random.randint(0, 100)



answer = float(input(f"What is the sum of {num1} + {num2} ? "))


if answer == (num1 + num2):
    print(f"{num1} + {num2} = {answer} is True")
else:
    print(f"{num1} + {num2} = {answer} is False")