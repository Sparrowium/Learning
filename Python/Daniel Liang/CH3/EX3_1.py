import math


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))


discriminant = b ** 2 - 4 * a * c


if discriminant > 0:
    print((- b + math.sqrt(discriminant)) / (2 * a), (- b - math.sqrt(discriminant)) / (2 * a))
elif discriminant == 0:
    print((- b + math.sqrt(discriminant)) / (2 * a))
else:
    print("has no real root")