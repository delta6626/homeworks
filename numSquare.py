import time

n = input('Enter a number : ')
s = "/"

for i in n:
    print(s*(int(i)**2))
    time.sleep(1)
