# Read a text file and display the number of vowels/ consonants/
#uppercase/lowercase characters in the file.


f = open("hello.txt")
l = f.read()

vowels = 0
consonants = 0
uppercase = 0
lowercase = 0

def check(letter):
    global vowels
    global consonants 
    global uppercase
    global lowercase

    if letter.lower() in ["a", "e", "i", "o", "u"]:
        vowels+=1
    else:
        consonants+=1
    
    if letter.lower() == letter:
        lowercase+=1
    else:
        uppercase+=1

for i in l:
    if i.isalnum():
        check(i)

print("Vowels : ", vowels)
print("Consonants : ", consonants)
print("Uppercase letters : ", uppercase)
print("Lowercase letters : ", lowercase)

f.close()