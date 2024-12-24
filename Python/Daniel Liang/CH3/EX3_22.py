import math


x = float(input("Enter coordinates x: "))
y = float(input("Enter coordinates y: "))


if math.sqrt(x ** 2 + y ** 2) <= 10:
    print("The coordinates is in the circle.")
else: 
    print("The coordinates is outside the circle.")