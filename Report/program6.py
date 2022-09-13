import random

def roll():
    print("Your random number is : ", random.randint(0,6))

while(True):
    print("Enter 1 to generate random number. Enter anything else to quit")
    c = input("Enter your choice : ")
    if c == "1":
        roll()
    else:
        quit()