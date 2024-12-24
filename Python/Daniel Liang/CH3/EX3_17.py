import random


guess = int(input("scissor (0), rock (1), paper(2) : "))


computer_guess = random.randint(0, 2)


if computer_guess == guess:
    if computer_guess == 0:
        print("The computer is scissor. You are scissor too. It is a draw")
    elif computer_guess == 1:
        print("The computer is rock. You are rock too. It is a draw")
    else:
        print("The computer is paper. You are paper too. It is a draw")
elif guess - computer_guess == 1 or guess - computer_guess == -2:
    if guess == 0:
        print("The computer is paper. You are scissor. You win")
    elif guess == 1:
        print("The computer is scissor. Yoy are rock. You win")
    else: 
        print("The computer is rock. Yoy are paper. You win")
else:
    if guess == 0:
        print("The computer is rock. You are scissor. You Lose")
    elif guess == 1:
        print("The computer is paper. You are rock. You Lose")
    else:
        print("The computer is scissor. You are paper. You Lose")
