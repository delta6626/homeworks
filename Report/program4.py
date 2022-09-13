import pickle

rollName = {}
nameMarks = {}

def write():
    global rollName
    global nameMarks
    f1 = open("rollName.dat","ab")
    f2 = open("nameMarks.dat", "ab")
    n = int(input("Enter number of students : "))
    while(n!=0):
        rollNumber = input("Enter roll number : ")
        name = input("Student name : ")
        marks = input("Student marks :")
        rollName[rollNumber] = name
        nameMarks[name] = marks
        n-=1
    pickle.dump(rollName, f1)
    pickle.dump(nameMarks, f2)
    rollName = {}
    nameMarks = {}
    f1.close()
    f2.close()

def view():
    try:
        f1 = open("rollName.dat", "rb")
        f2 = open("nameMarks.dat", "rb")
    except FileNotFoundError:
        print("Please enter some data first.")
        quit()
    rollNumber = input("Enter rollnumber : ")
    rn = pickle.load(f1)
    nm = pickle.load(f2)
    if rollNumber in rn.keys():
        print("Student name : ", rn[rollNumber])
        print("Student marks : ", nm[rn[rollNumber]])
    else:
        print("This rollnumber does not exist.")
    f1.close()
    f2.close()

def update():
    rollNumber = input("Enter roll number of student : ")
    marks = input("Enter new marks : ")
    f1 = open("rollName.dat", "rb")
    rn = pickle.load(f1)
    f1.close()
    if rollNumber in rn.keys():
        f2 = open("nameMarks.dat", "rb")
        nm = pickle.load(f2)
        f2.close()
        temp = nm
        temp[rn[rollNumber]] = marks
        f2 = open("nameMarks.dat", "wb")
        pickle.dump(temp, f2)
        f2.close()
        print("Done")
    else:
        print("This roll number does not exist.")

def choose():
    print("Press 1 to view data\nPress 2 to update marks\nPress any other key to quit.")
    option = input("What's your choice? : ")
    if option == "1":
        view()
    elif option == "2":
        update()
    else:
        quit()


write()
while(True):
    choose()