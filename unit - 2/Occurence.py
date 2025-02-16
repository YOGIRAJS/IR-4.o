string = input("Enter the string: ")
char = input("Enter the character to count: ")
print(f"Occurrences of '{sum(1 for c in string if c == char)}':")
