x = int(input("Enter the number of students: "))
a = 0
b = ""
while x > 0:
    y = input("Enter student name: ")
    z = float(input("Enter student score: "))
    x -= 1
    if z > a:
        a = z
        b = y


print(f"Top student {b}'s score is {z}")