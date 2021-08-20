# Dice Rolling Simulator

# import Module
from random import randint

# Function for start the game


def start():
    text = """
        if You want to roll the dice type R
        if You want to quit the game type E
    """

    print(text)
    opt = input("=> ").upper().strip()

    if opt == "R":
        roll()
        roll_again()
    elif opt == "E":
        print("Good Bye")
        quit()
    else:
        print("wrong choice")
        start()


# Function for Rolling the dice
def roll():
    x = randint(1, 6)
    print(x)


# Function for Rolling again
def roll_again():
    print("Do You want to roll again? (y or n)")
    opt = input("=> ").lower().strip()
    if opt == "y":
        roll()
        roll_again()
    elif opt == "n":
        print("Good Bye")
        exit()
    else:
        print("wrong choice")
        roll_again()


# Run
start()
