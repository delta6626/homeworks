import time
c = "*"
s = " "
n = 70 # total characters (width of the zig zag pattern)
sp = 40 # spaces infront
i=0 
while(True):
    while(i<=sp):
        time.sleep(0.1)
        print(s*i+(c*n))
        i+=1
    while(i>=0):
        time.sleep(0.1)
        print(s*i+(c*n))
        i-=1
    