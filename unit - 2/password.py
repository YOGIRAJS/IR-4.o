import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
leng = int(input("Enter password length: "))

password = ""
for i in range(leng):
    password += random.choice(chars)

print("Generated Password:", password)
