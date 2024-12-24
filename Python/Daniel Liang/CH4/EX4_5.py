import math


n = int(input("The number of sides: "))
s = float(input("Enter the side length of the hexagon: "))


area = (n  * s ** 2) / (4 * math.tan((math.pi) / n))


print("The area of the pentagon is", area)