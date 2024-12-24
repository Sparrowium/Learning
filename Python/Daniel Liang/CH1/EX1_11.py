print()
newpop = 312032486
for i in range(0, 5):
    newpop += (365 * 24 * 3600) / 7 - (365 * 24 * 3600) / 13 + (365 * 24 * 3600) / 45
    print("World population = ", newpop)