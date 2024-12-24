x0 = float(input("Enter x0 coordinate: "))
y0 = float(input("Enter y0 coordinate: "))
x1 = float(input("Enter x1 coordinate: "))
y1 = float(input("Enter y1 coordinate: "))
x2 = float(input("Enter x2 coordinate: "))
y2 = float(input("Enter y2 coordinate: "))


if ((x1 - x0) * (y2 - y0) -  (x2 - x0) * (y1 - y0)) > 0:
    print("The point is on the left side of the line.")
elif ((x1 - x0) * (y2 - y0) -  (x2 - x0) * (y1 - y0)) == 0:
    print("The point is on the same side of the line.")
else:
    print("The point is on the right side of the line.")