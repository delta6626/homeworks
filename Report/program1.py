f = open("hello.txt")
lines = f.readlines()
words = []
for i in lines:
    word = i.split()
    words.append(word)

for i in words:
    for j in i:
        print(j)
        print("#")

f.close()