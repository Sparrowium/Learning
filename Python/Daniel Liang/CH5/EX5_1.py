x = int(input("Enter an integer, the input ends if it is 0: "))


if x == 0:
    print("There is no integer except zero.")


pos_count = 0 
neg_count = 0
count = 0
total = 0

while x != 0:
    count += 1
    if x > 0:
        pos_count += 1
        total += x
    else:
        neg_count += 1
        total += x
    
    x = int(input("Enter an integer, the input ends if it is 0: "))


avg = total / count


print("The number of positives is ", pos_count,
      "\nThe number of negatives is ", neg_count,
      "\nThe total is ", total,
      "\nThe average is ", avg)