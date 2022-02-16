l = [1,2,2,3,4,4,4,5,6,7,8,8,9,10]
for i in l:
    if(l.count(i)>1):
        l.remove(i)
print(l) # Updated list with no duplicates.