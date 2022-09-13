# Stack

myStack = []
stackLength = int(input("Enter stack length : "))

def add():
    n = int(input("How many elements do you want to add? : "))
    if n > stackLength - len(myStack):
        print("Stack overflow")
    else:
        while(n!=0):
            e = input("Enter element : ")
            myStack.append(e)
            n-=1
        print("Done")
        print(myStack)

def remove():
    n = int(input("How many elements do you want to remove? : "))
    if n>len(myStack):
        print("Stack underflow")
    else:
        while(n!=0):
            myStack.pop()
            n-=1
        print("Done")
        print(myStack)

while(True):
    print("Enter 1 to add elements to stack\nEnter 2 to remove elements.\nPress anything else to quit.")
    choice = input("What's your choice? : ")
    if choice == "1":
        add()
    elif choice == "2":
        remove()
    else:
        quit()