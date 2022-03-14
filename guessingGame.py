from random import randint
setup = True


def game(val):
    num = randint(1, val)
    chances = 4
    while(chances != 0):
        try:
            guess = int(input("Guess the number: "))
            if(guess < num):
                print("guess higher")
                chances -= 1
            elif(guess > num):
                print("guess lower")
                chances -= 1
            else:
                print("Wow you win!")
                chances = 0
        except ValueError:
            print("Invalid Value")
    if(guess == num):
        pass
    else:
        print("you lose! The number was ", num)


while(setup):
    try:
        diffLevel = int(input(
            "Press 1 for Easy mode\nPress 2 for medium mode\nPress 3 for hard mode\nPress 4 to quit\nWhat mode do you want? : "))
        if(diffLevel == 1):
            game(10)
            setup = False
        elif(diffLevel == 2):
            game(50)
            setup = False
        elif(diffLevel == 3):
            game(100)
            setup = False
        elif(diffLevel == 4):
            exit()
        else:
            print("Invalid option. Try again.")
    except ValueError:
        print("Invalid Value")
