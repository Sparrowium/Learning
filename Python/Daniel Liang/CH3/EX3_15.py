import random


guess = int(input("Enter your 3 digit guess:"))


answer = random.randint(100, 1000)

print(f"The lottery is {answer}")


digit1 = str(answer // 100)
digit2 = str(answer % 100 // 10)
digit3 = str(answer % 100 % 10)


if answer == guess: 
    print("The awards is $10000")
elif (digit1 in str(guess)) and (digit2 in str(guess)) and (digit3 in str(guess)):
    print("The awards is $3000")
elif (digit1 in str(guess)) or (digit2 in str(guess)) or (digit3 in str(guess)):
    print("The awards is $1000")
else:
    print("Sorry, no match found")