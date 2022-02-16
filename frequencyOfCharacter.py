# A program to calculate the number of times a character appears in a string
def calc(str,c):
    n = 0
    for i in str:
        if i==c:
            n+=1
    print("The character",c," appears ",n,"time(s).")

calc("hello","l") # output- 2
calc("python progamming", "a") # ouput- 1