def calculate_isbn_checksum(digits):
    # Calculate the checksum
    checksum = sum((int(digit) * (i + 1)) for i, digit in enumerate(digits))
    checksum %= 11

    # Display the result
    if checksum == 10:
        return 'X'
    else:
        return str(checksum)

def main():
    # Prompt the user for the first 9 digits
    user_input = input("Enter the first 9 digits of the ISBN-10: ")
    digits = user_input.strip()[:9]  # Remove leading zeros and take the first 9 digits

    # Calculate and display the checksum
    checksum = calculate_isbn_checksum(digits)
    print(f"The ISBN-10 checksum is: {checksum}")

if __name__ == "__main__":
    main()
