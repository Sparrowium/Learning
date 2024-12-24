minutes = int(input("minutes: "))

years = minutes // (365 * 24 * 60)
remains = minutes % (365 * 24 * 60)
days = remains // (60 * 24)

print("YEARS:", years)
print("days", days)
