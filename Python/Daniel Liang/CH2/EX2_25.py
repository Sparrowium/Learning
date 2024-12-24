number = int(input("Enter a number (1-1000): "))


sum_of_individual_integers = number // 100 + number / 10  // 10 + number / 110 % 10


print("Sum of individuals digits in ", number , " is ", int(sum_of_individual_integers))