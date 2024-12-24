# Get the names of the three cities from the user
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")
city3 = input("Enter the third city: ")

# Create a list of the city names
cities = [city1, city2, city3]

# Sort the list in ascending order
sorted_cities = sorted(cities)

# Print the sorted list of city names
print("The three cities in alphabetical order are", sorted_cities)
