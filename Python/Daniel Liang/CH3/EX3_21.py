year = int(input("Enter year: "))
month = int(input("Enter month 1-12: "))
day = int(input("Enter the day of the month 1-31: "))


match month:
    case 1: month = 13
    case 2: month = 14

q = day
m = month
k = year % 100
j = year // 100


h = (q + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7

if h == 0:
    print("The day of the week is Saturday")
elif h == 1:
    print("The day of the week is Sunday")
elif h == 2:
    print("The day of the week is Monday")
elif h == 3:
    print("The day of the week is Tuesday")
elif h == 4:
    print("The day of the week is Wednesday")
elif h == 5:
    print("The day of the week is Thursday")
elif h == 6:
    print("The day of the week is Friday")
