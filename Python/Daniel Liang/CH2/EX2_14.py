import math


x1 = float(input("Enter x1 coordinate for triangle: "))
y1 = float(input("Enter y1 coordinate for triangle: "))
x2 = float(input("Enter x2 coordinate for triangle: "))
y2 = float(input("Enter y2 coordinate for triangle: "))
x3 = float(input("Enter x3 coordinate for triangle: "))
y3 = float(input("Enter y3 coordinate for triangle: "))

s = (math.sqrt((x1 - x2) ** 2 + (y1- y2) ** 2)
     + math.sqrt((x2 - x3) ** 2 + (y2- y3) ** 2)
     + math.sqrt((x3 - x1) ** 2 + (y3- y1) ** 2)) / 2

area = math.sqrt(s * (s - math.sqrt((x1 - x2) ** 2 + (y1- y2) ** 2))
                * (s - math.sqrt((x2 - x3) ** 2 + (y2- y3) ** 2))
                * (s - math.sqrt((x3 - x1) ** 2 + (y3- y1) ** 2)))

print("the area of the triangle is:", area)