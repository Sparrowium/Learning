import math


r = float(input("Enter the length from the center to a vertex: "))


s = 2 * r * math.sin((math.pi) / 5)
area = (5  * s ** 2) / (4 * math.tan((math.pi) / 5))


print("The area of the pentagon is", area)