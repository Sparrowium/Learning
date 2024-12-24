subtotal = float(input("subtotal: "))
gratuity_rate = float(input("gratuity rate: "))

gratuity = gratuity_rate / 100
total = subtotal * gratuity + subtotal

print("Total:", format(total, ".2f"))
print("gratuity:", gratuity)
