
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))


if (0 < x < 200) and (0 < y < 100) and y <= (x * (-1/2) + 100):
    print("The point is in the triangle.")
else:
    print("The point is outside the triangle.")