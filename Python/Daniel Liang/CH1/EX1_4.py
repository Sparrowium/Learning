from tabulate import tabulate

a = b = c = 0
d = []
for i in range(1, 5):
    a = i
    b = pow(a, 2)
    c = pow(a, 3)
    y = [a, b, c]
    d.append(y)

print(tabulate(d, headers=["a", "a ^ 2", "a ^ 3"]))