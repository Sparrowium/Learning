name = input("Enter Employee's name: ")
hour = int(input("Enter number of hours worked in a week: "))
hourly_pay_rate = float(input("Enter hourly pay rate: "))
federal_tax_rate = float(input("Enter federal tax withholding rate: "))
state_tax_rate = float(input("Enter state tax withholding rate: "))


gross_pay = hour * hourly_pay_rate
federal_tax = federal_tax_rate * hourly_pay_rate * hour
state_tax = state_tax_rate * hourly_pay_rate * hour
total_tax = federal_tax + state_tax
print(f"\nEmployee's name: {name}",
      f"\nHours worked: {hour}",
      f"\nPay rate: {hourly_pay_rate}",
      f"\nGross pay: {gross_pay}",
      "\nDeductions:",
      f"\n\tFederal Withholding ({federal_tax}): ",
      f"\n\tState Withholding ({state_tax}): ",
      f"\n\tTotal Deduction: {total_tax}",
      f"\nNet pay: {gross_pay - total_tax}")
