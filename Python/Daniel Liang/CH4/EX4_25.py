import calendar

# Input year and month
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Get the number of days using the calendar module
num_days = calendar.monthrange(year, month)[1]

# Display the result
print(f"{calendar.month_name[month]} {year} has {num_days}")
