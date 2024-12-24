Investment_amount=float(input("Investment amount: "))
Annual_interest_rate = float(input("Annual interest rate: "))
Number_of_years = float(input("Number of years: "))

future_investment_value = Investment_amount * (1 + Annual_interest_rate / 12 / 100) ** (Number_of_years * 12)

print("future investment value is: ", format(future_investment_value, "2.2f"))