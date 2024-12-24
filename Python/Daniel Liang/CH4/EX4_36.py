# Import the re module
import re

# Get the SSN from the user
ssn = input("Enter a Social Security number in the format ddd-dd-dddd: ")

# Define the regular expression for a SSN
pattern = r"^\d{3}-\d{2}-\d{4}$"

# Check if the SSN matches the pattern
if re.match(pattern, ssn):
    # If the SSN is valid, print a message
    print("Valid SSN")
else:
    # If the SSN is invalid, print a message
    print("Invalid SSN")
