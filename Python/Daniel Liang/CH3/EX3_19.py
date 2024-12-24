edge1 = float(input("Enter edge1: "))
edge2 = float(input("Enter edge2: "))
edge3 = float(input("Enter edge3: "))


if (edge1 + edge2 > edge3) and (edge2 + edge3 > edge1) and (edge1 + edge3 > edge2):
    print("The perimeter is ", edge1 + edge2 + edge3)
else:
    print("Invalid")