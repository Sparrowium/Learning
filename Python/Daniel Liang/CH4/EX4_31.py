x = input("Enter a hex character: ")

y = bin(int(x, 16))
print(f"The binary value is {y[2:]}")