import random
l = [1, 2, 3, 4, 5]
t = (6, 5, 4, 3, 2)
d = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}
x = random.randint(0, len(l)-1)
print(l[x])
print(t[x])
print(d[str(x+1)])
