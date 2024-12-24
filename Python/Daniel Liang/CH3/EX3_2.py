import random


num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)


answer = float(input(f"What is the sum of {num1} + {num2} + {num3} ? "))


if answer == (num1 + num2 + num3):
    print(f"{num1} + {num2} + {num3} = {answer} is True")
else:
    print(f"{num1} + {num2} + {num3} = {answer} is False")