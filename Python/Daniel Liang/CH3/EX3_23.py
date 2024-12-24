import math


x = float(input("Enter coordinates x: "))
y = float(input("Enter coordinates y: "))


if (-5 < x < 5) and (-2.5 < y < 2.5):
    print("The coordinates is in the rectangle.")
else:
    print("The coordinates is outside the rectangle.")