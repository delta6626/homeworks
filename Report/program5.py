f = open("hello.txt")
lines = f.readlines()

containsA = []

for line in lines:
    for letter in line:
        if letter == "A" or letter == "a":
            containsA.append(line)
            break
f.close()

newFile = open("linesWithA.txt", "w+")
newFile.writelines(containsA)
newFile.close()
