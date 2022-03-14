ODD = {
    "1": "One",
    "3": "Three",
    "5": "Five",
    "7": "Seven",
    "9": "Nine"
}

# displaying the key values.
print(ODD.keys())
# Displaying the values
print(ODD.values())
# Displaying the items
print(ODD.items())
# length of ODD
print(len(ODD))
# checking if 7 is present or not
print("7" in ODD)
# Retrieving the value corresponding to key 9 and deleting the item:
print(ODD.get("9"))
del ODD["9"]
print("New dict after removing 9: ", ODD)
