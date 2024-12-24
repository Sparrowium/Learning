a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))
e = int(input("Enter e: "))
f = int(input("Enter f: "))


x = (e * d - b * f) / (a * d - b * c)
y = (a * f - e * c) / (a * d - b * c)


if (a * d - b * c) == 0:
    print("The equation has no solution")
else: 
    print(x, y)