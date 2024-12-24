weight = float(input("weight in pounds: "))
height = float(input("height in inches: "))

BMI = (weight * 0.45359257) / ((height * 0.0254) ** 2)

print("BMI:", BMI)