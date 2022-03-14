import random
import time

characters = "|"
space = " "
show = True


def rain():
    time.sleep(0.1)
    print((characters+space*random.randint(5, 10))*random.randint(10, 20))


while(show):
    rain()
