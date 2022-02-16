import random

s = input("Enter any sentence or word : ")
f = ""

for i in s:
    r = random.choice([0,1])
    if r == 0:
        f += i.upper()
    else:
        f+= i.lower()

print(f"Randomly capitalized word/sentence : {f}")