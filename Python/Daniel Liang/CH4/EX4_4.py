import math


s = float(input("Enter the side length of the hexagon: "))


area = (6  * s ** 2) / (4 * math.tan((math.pi) / 6))


print("The area of the pentagon is", area)