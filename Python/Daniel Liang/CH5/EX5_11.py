x = float(input("Enter the number of students: "))

i = 1
max_score = 0
max_name = ""
max2_score = 0
max2_name = ""
name = ""
score = 0

while i <= x:
    name = input("Enter a student name: ")
    score = float(input("Enter a student score: "))
    
    if score > max_score:
        max2_score = max_score  # Update max2_score
        max2_name = max_name  # Update max2_name
        max_score = score
        max_name = name
    elif score > max2_score:
        max2_score = score
        max2_name = name
            
    i += 1


print("Top two students: ")
print(max_name + "'s score is " + str(max_score))
print(max2_name + "'s score is " + str(max2_score))