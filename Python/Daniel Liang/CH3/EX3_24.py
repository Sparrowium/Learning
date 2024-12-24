import random


rank = random.randint(1, 13)
suit = random.randint(1, 4)


match rank:
    case 1: rank = "Ace"
    case 2: rank = "2"
    case 3: rank = "3"
    case 4: rank = "4"
    case 5: rank = "5"
    case 6: rank = "6"
    case 7: rank = "7"
    case 8: rank = "8"
    case 9: rank = "9"
    case 10: rank = "10"
    case 11: rank = "Jack"
    case 12: rank = "Queen"
    case 13: rank = "King"
    

match suit:
    case 1: suit = "Clubs"
    case 2: suit = "Diamonds"
    case 3: suit = "Hearts"
    case 4: suit = "Spades"


print("The card you picked is", rank, "of", suit)