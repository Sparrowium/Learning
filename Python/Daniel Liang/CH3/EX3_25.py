x1 = float(input("Enter x1 coordinate: "))
y1 = float(input("Enter y1 coordinate: "))
x2 = float(input("Enter x2 coordinate: "))
y2 = float(input("Enter y2 coordinate: "))

x3 = float(input("Enter x3 coordinate: "))
y3 = float(input("Enter y3 coordinate: "))
x4 = float(input("Enter x4 coordinate: "))
y4 = float(input("Enter y4 coordinate: "))


a = y1 - y2
b = x2 - x1
c = y3 - y4
d = x4 - x3
e = a * x1 + b * y1
f = c * x3 + d * y3

# Calculate the determinant D
D = a * d - b * c

# Calculate the determinants Dx and Dy
Dx = e * d - b * f
Dy = a * f - e * c
# Calculate the values of x and y
x = Dx / D
y = Dy / D


if D == 0:
  print("The two lines are parallel")
else:
  print("The intersecting point is at", x, y)