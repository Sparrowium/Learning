num = int(input("Enter an integer: "))


print(f"Is {num} divisible by 5 and 6? ", True if num % 5 == 0 and num % 6 == 0 else False)
print(f"Is {num} divisible by 5 or 6? ", True if num % 5 == 0 or num % 6 == 0 else False)
print(f"Is {num} divisible by 5 or 6, but not both? ", True if num % 5 == 0 or num % 6 == 0 else False)

    