from calendar import monthrange, month_name

month = int(input("Enter a month in a year: "))
year = int(input("Enter a year: "))


m, d = monthrange(year, month)
m = month_name[month]


print(f"{m} {year} has {d} days")



