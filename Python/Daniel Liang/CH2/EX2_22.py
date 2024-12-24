import math


n = float(input("Enter number of years: "))


newpop = 312032486


newpop += math.ceil(((365 * 24 * 3600) / 7 - (365 * 24 * 3600) / 13 + (365 * 24 * 3600) / 45) * n)
print("World population = ", newpop)