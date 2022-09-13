# Queue

myQueue = []
queueLength = int(input("Enter max length of queue : "))

def add():
    n = int(input("How many elements do you want to add? : "))
    if n > queueLength - len(myQueue):
        print("Queue overflow")
    else:
        while(n!=0):
            e = input("Enter element : ")
            myQueue.append(e)
            n-=1
        print("Done")
        print(myQueue)

def remove():
    n = int(input("How many elements do you want to remove? : "))
    for i in range(0, n):
        del myQueue[0]
    print("Done")
    print(myQueue)

while(True):
    print("Enter 1 to add elements to stack\nEnter 2 to remove elements.\nPress anything else to quit.")
    choice = input("What's your choice? : ")
    if choice == "1":
        add()
    elif choice == "2":
        remove()
    else:
        quit()
