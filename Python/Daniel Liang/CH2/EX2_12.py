print(format("a", "10"), format("b", "10"), format("pow(a,b)", "10"))

for i in range(1, 6):
    print(
        format(str(i), "10"), 
        format(str(i + 1), "10"), 
        format(str(i ** (i + 1)), "10"))