letter = input("Enter a letter grade: ")


if letter in "AEUIOaeuio":
    print(f"{letter} is a vowel")
else:
    print(f"{letter} is consonant")