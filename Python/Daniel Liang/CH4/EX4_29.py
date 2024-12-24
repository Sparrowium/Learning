x = input("Enter the first 9-digit of an ISBN number as a string: ")

d10 = 0
for i in range(1, 10):
    d10 = int(x[i - 1]) * i


d10 %= 11


if d10 == 10:
    print("The ISBN number is", x + "X")
else:
    print("The ISBN number is", x + str(d10))

