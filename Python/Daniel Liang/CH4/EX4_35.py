x1 = float(input("Enter x1 coordinate: "))
y1 = float(input("Enter y1 coordinate: "))
x2 = float(input("Enter x2 coordinate: "))
y2 = float(input("Enter y2 coordinate: "))


m = (y2 - y1) / (x2 - x1)
print(f"The line equation for two points ({x1}, {y1}) and ({x2}, {y2}) is y =", str(m), "x", str(y1 - m * x1))