import math


x1 = float(input("Enter the center coordinates of Circle A x1: "))
y1 = float(input("Enter the center coordinates of Circle A y1: "))
r1 = float(input("Enter the radius of Circle A: "))
x2 = float(input("Enter the center coordinates of Circle B x2: "))
y2 = float(input("Enter the center coordinates of Circle B y2: "))
r2 = float(input("Enter the radius of Circle B: "))


distance = math.sqrt(int((x1 - x2) ** 2 + (y1 - y2) ** 2))

# Check the relationship between the circles
if distance <= abs(r1 - r2):
    print("Circle B is inside Circle A")
elif distance <= r1 + r2:
    print("Circles intersect with each other")
else:
    print("Circles do not overlap")