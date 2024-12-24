x = int(input("Enter today's day: "))
y = int(input("Enter number of days elapsed since today: "))
a = ""
b = ""


y = (x + y) % 7


match x:
    case 0: a = "Sunday"
    case 1: a = "Monday"
    case 2: a = "Tuesday"
    case 3: a = "Wednesday"
    case 4: a = "Thursday"
    case 5: a = "Friday"
    case 6: a = "Saturday"
    case 7: a = "Sunday"


match y:
    case 0: b = "Sunday"
    case 1: b = "Monday"
    case 2: b = "Tuesday"
    case 3: b = "Wednesday"
    case 4: b = "Thursday"
    case 5: b = "Friday"
    case 6: b = "Saturday"
    case 7: b = "Sunday"


print(f"Today is {a} and the future day is {b}")