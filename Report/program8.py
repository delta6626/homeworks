f = open("collection.txt")

lines = f.readlines()

wordList = []
countList = []
correspondingWord = []
count = 0

for i in lines:
    word = i.split()
    for j in word:
        wordList.append(j)

for i in wordList:
    for j in wordList:
        if i==j:
            count+=1
    countList.append(count)
    correspondingWord.append(i)
    count = 0


print(countList)
print(correspondingWord)

def clearOldMax():
    oldMax = max(countList)
    while(oldMax in countList):
        countList.remove(oldMax)

def clearOldWord():
    oldWord = correspondingWord[countList.index(max(countList))]
    while(oldWord in correspondingWord):
        correspondingWord.remove(oldWord)


print("The most commonly occuring words are : ")

print(correspondingWord[countList.index(max(countList))], " : " ,max(countList))
clearOldWord()
clearOldMax()
print(correspondingWord[countList.index(max(countList))], " : " ,max(countList))
clearOldWord()
clearOldMax()
print(correspondingWord[countList.index(max(countList))], " : " ,max(countList))
clearOldWord()
clearOldMax()
print(correspondingWord[countList.index(max(countList))], " : " ,max(countList))
clearOldWord()
clearOldMax()

f.close()