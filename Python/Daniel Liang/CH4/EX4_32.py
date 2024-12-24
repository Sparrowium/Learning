decimal_input = int(input("Enter a decimal integer value (0 to 15): "))


hex_value = hex(decimal_input)[2:].upper()

print(f"The hex value is {hex_value}")
