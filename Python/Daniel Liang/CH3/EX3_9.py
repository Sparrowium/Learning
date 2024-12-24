pack1 = float(input("Enter weight for package 1: "))
price1 = float(input("Enter price for package 1: "))
pack2 = float(input("Enter weight for package 2: "))
price2 = float(input("Enter price for package 2: "))


if pack1/price1 > pack2/price2:
    print("Package 1 has the best price" )
else: 
    print("Package 2 has the best price")