# A program based on collatz conjecture.
# Calculates number of steps taken by a number to reach 4-2-1 loop.
x = int(input("Enter any number : "))
steps = 0
while(x != 1):
    if(x % 2 != 0):
        x = 3*x+1
        steps += 1
    else:
        x = x/2
        steps += 1
print("Steps taken : ", steps)
