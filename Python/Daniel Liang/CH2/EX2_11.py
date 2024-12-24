fav = float(input("financial account value: "))
arr = float(input("annual interest rate: "))
years = float(input("number of years: "))

ida = fav / ((1 + arr / 1200) ** (years * 12))

print("intial deposit amount: ", ida)