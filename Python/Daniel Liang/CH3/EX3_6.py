pounds = float(input("Enter your weights in pounds: "))
ft = float(input("Enter feet: "))
inches = float(input("Enter inches: "))


meters = ft * 0.3048 + inches * 0.0254
bmi = (pounds / 2.2046) / (meters ** 2)


print(f"BMI is {bmi}")


if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Normal")
elif 25 <= bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")