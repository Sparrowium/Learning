import random


print("Guess head or tail?")
answer = int(input("Enter 0 for head or 1 for tail: "))


guess = random.randint(0, 1)


if answer == guess:
    print("Correct, it is ", "Head" if guess == 0 else "Tail")
else:
    print("Sorry, it is ", "Head" if guess == 0 else "Tail")

