# A program to remove a given key from the dictionary if it is present
salaries = {
    "Ram": "25000",
    "Mohan": "32000",
    "Jacob": "27000",
    "Mathew": "45000"
}
k = input("Enter key to be removed : ")
if k in salaries:
    del salaries[k]
    print("Removed the key ", k)
    print("Updated dictionary : ", salaries)
else:
    print("The given key is not present in the dictionary.")
