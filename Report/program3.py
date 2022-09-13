import pickle

dataDict = {}

def write():
    global dataDict
    f = open("data.dat", "ab")
    n = int(input("Enter number of students : "))
    while(n!=0):
        rollNumber = input("Enter roll number : ")
        studentName = input("Enter student name : ")
        dataDict[rollNumber] = studentName
        n-=1
    pickle.dump(dataDict, f)
    dataDict = {}
    f.close()

def read():
    print("Get info about student")
    try:
        f = open("data.dat", "rb")
    except FileNotFoundError:
        print("Please enter data first!")
        quit()
    data = pickle.load(f)
    rollNumber = input("Enter roll number : ")
    if rollNumber not in data.keys():
        print("This roll number does not exist.")
    else:
        print("Student name : ", data[rollNumber],)
    f.close()


write()
while(True):
    read()