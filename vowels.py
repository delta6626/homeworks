x = input("Enter a sentence or word : ").lower()
count = 0
for i in x:
    if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        count += 1
print("There are ", count, "vowels in your word/sentence.")
