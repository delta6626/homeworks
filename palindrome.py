x = input("Enter a word : ")
new = ""
arr = []
for i in x:
    arr.append(i)
arr.reverse()
for i in arr:
    new+=i
if(new == x ):
    print("Palindrome")
else:
    print("Not palindrome")
