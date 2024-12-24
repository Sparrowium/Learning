import random


char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


x = random.choice(char)
y = random.choice(char)
z = random.choice(char)

a = str(random.randint(0, 9))
b = str(random.randint(0, 9))
c = str(random.randint(0, 9))
d = str(random.randint(0, 9))


print("A random vehicle plate number:",x+y+z+a+b+c+d)