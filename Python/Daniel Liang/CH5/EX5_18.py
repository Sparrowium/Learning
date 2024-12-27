num = int(input("Enter a number: "))

temp : int = 2
while num > 1:
    if num % temp != 0:
        temp += 1
    else: 
        num /= temp
        print(temp, end=" ")
        temp = 2
    

