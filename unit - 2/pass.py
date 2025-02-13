password = input("Enter your password: ")

if 8 < len(password) > 16 and sum(c.isdigit() for c in password) >= 2 and any(c.isalpha() for c in password):
    print("Password is valid.")
else:
    print("Invalid password. Must be 9-15 characters, include at least 1 letter and 2 numbers.")
