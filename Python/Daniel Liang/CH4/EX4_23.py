letter = input("Enter a letter grade: ").upper()


match letter:
    case "A": print("The numeric value for grade A is 4")
    case "B": print("The numeric value for grade B is 3")
    case "C": print("The numeric value for grade C is 2")
    case "D": print("The numeric value for grade D is 1")
    case "F": print("The numeric value for grade F is 0")