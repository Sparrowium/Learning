initial_temp = float(input("initial_temp: "))
final_temp = float(input("final_temp: "))
M = float(input("Amount of water: "))

Q = M * (final_temp - initial_temp) * 4184

print("Energy needed: ", Q)