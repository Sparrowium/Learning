temp = float(input("enter temp between -58*F and 41*F: "))
wind_speed = float(input("enter wind speed >= 2: "))

wind_chill = 35.74 + 0.6215 * temp - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp * (wind_speed ** 0.16)

print("Wind chill is: ", wind_chill)