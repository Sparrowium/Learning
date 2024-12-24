import math

radius = float(input("Radius: "))
length = float(input("Length: "))

area = radius * radius * math.pi
volume = area * length

print("Area:", area)
print("Volume:", volume)