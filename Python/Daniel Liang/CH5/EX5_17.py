for i in range(33, 127):  # ASCII range for '!' to '~'
    if i % 10 == 0:  # New line every 10 characters
        print()
    print(chr(i), end=" ")  # Print character with a space after
print()  # Print a final newline