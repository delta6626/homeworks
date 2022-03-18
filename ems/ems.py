# Expense Managment System 
# Author : M.Hassan

import json 
import random
import datetime

# opening the json file and reading content
f = open("data.json","r+")
d = json.load(f)
f.close()

info = '''
Press 1 to add new Expense
Press 2 to add new Income 
Press 3 to view your expenses
Press 4 to view your incomes
Press 5 to view your balance
Press 6 to get a financial tip
Press 7 to change your username
Press 8 to clear expense list
Press 9 to clear Incomes list
Press 10 to modify current balance amount
Press 11 to view total expense amount
Press 12 to view total income amount
'''

tips = ["Track your spending to improve your finances (use this software)",
"Create a realistic monthly budget",
"Build up your savings—even if it takes time.",
"Pay your bills on time every month.",
"Start an investment strategy.",
"Clear all your debts as soon as possible.",
"Don't invest too much money at once.",
"Improve your credit score.",
"Don't purchase unnecessary items when you're shopping.",
"Start Saving for Retirement."]

def addExpense():
    expenseTitle = input("\nEnter expense title: ")
    expenseAmount = float(input("Enter expense amount: "))
    nf = open("data.json")
    df = json.load(nf)
    nf.close()
    df["expenses"][expenseTitle+" "+str(datetime.datetime.now())]=expenseAmount
    df["balance"]-=expenseAmount
    nf2 = open("data.json","w+")
    nf2.write(json.dumps(df))
    nf2.close()
    print("Successfully added new expense.")

def addIncome():
    incomeTitle = input("\nEnter income title: ")
    incomeAmount = float(input("Enter income amount: "))
    nf = open("data.json")
    df = json.load(nf)
    nf.close()
    df["incomes"][incomeTitle+" "+str(datetime.datetime.now())]=incomeAmount
    df["balance"]+=incomeAmount
    nf2 = open("data.json","w+")
    nf2.write(json.dumps(df))
    nf2.close()
    print("Successfully added new income.")

def viewBalance():
    nf = open("data.json")
    df = json.load(nf)
    nf.close()
    print("\nYour current balance is : ",df["balance"],"\n")

def viewExpenses():
    nf = open("data.json")
    df = json.load(nf)
    nf.close()
    print()
    print("Your expenses : ")
    for i in df["expenses"]:
        print(i+" : "+str(df["expenses"][i]))

def viewIncomes():
    nf = open("data.json")
    df = json.load(nf)
    nf.close()
    print()
    print("Your incomes : ")
    for i in df["incomes"]:
        print(i+" : "+str(df["incomes"][i]))

def getTip():
    r = random.randint(0,len(tips)-1)
    print("\n","Tip : ",tips[r],"\n")

def changeUserName():
    x = input("\nEnter new username : ")
    if(x == ""):
        print("Username can't be null.")
    elif(x==d["userName"]):
        print("You already have the same username.")
    else:
        nf = open("data.json")
        df = json.load(nf)
        nf.close()
        df["userName"] = x
        nf2 = open("data.json","w+")
        nf2.write(json.dumps(df))
        nf2.close()
        print("Successfully changed username to ",x)

def clearExpenses():
    nf = open("data.json")
    df = json.load(nf)
    nf.close()
    df["expenses"].clear()
    nf2 = open("data.json","w+")
    nf2.write(json.dumps(df))
    nf2.close()
    print("\nSuccessfully cleared all expenses.")

def clearIncomes():
    nf = open("data.json")
    df = json.load(nf)
    nf.close()
    df["incomes"].clear()
    nf2 = open("data.json","w+")
    nf2.write(json.dumps(df))
    nf2.close()
    print("\nSuccessfully cleared all incomes.")

def modifyBalance():
    amt = float(input("\nEnter new balance amount : "))
    nf = open("data.json")
    df = json.load(nf)
    nf.close()
    df["balance"] = amt
    nf2 = open("data.json","w+")
    nf2.write(json.dumps(df))
    nf2.close()
    print("Successfully modified balance amount.")

def totalExpenseAmount():
    x = 0
    nf = open("data.json")
    df = json.load(nf)
    nf.close()
    print()
    print("Your total expense amount : ")
    for i in df["expenses"]:
        x+=df["expenses"][i]
    print(x)

def totalIncomeAmount():
    x = 0
    nf = open("data.json")
    df = json.load(nf)
    nf.close()
    print()
    print("Your total income amount : ")
    for i in df["incomes"]:
        x+=df["incomes"][i]
    print(x)

def main():
    print("Welcome ",d["userName"],"\n")
    print(info)
    while(True):
        choice = input("\nEnter your option: ")
        if(choice == "1"):
            addExpense()
        elif(choice == "2"):
            addIncome()
        elif(choice == "3"):
            viewExpenses()
        elif(choice == "4"):
            viewIncomes()
        elif(choice == "5"):
            viewBalance()
        elif(choice == "6"):
            getTip()
        elif(choice == "7"):
            changeUserName()
        elif(choice == "8"):
            clearExpenses()
        elif(choice == "9"):
            clearIncomes()
        elif(choice == "10"):
            modifyBalance()
        elif(choice == "11"):
            totalExpenseAmount()
        elif(choice == "12"):
            totalIncomeAmount()
        elif(choice == "13"):
            quit()
        else:
            print("\nInvalid option. Try again.")
            print(info)

def init():
    if(d["userName"]==""):
        print("Welcome to Expense Manager.")
        n = input("Enter your name to get started : ")
        b = float(input("Enter your initial balance : "))
        d["userName"] = n
        d["balance"] = b
        f = open("data.json","w+")
        f.write(json.dumps(d))
        f.close()
        print("\nYou're all set.")
        main()
    else:
        main()

init()
