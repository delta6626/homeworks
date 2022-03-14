import random

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@$#&*()"

try:
    l = int(input("How many characters do you want in your password?: "))
except ValueError:
    print("Invalid value entered. Please try again.")
    quit()

password = ""

while(l != 0):
    password += random.choice(characters)
    l -= 1

print(f"Your password is {password}")
