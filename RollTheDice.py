# !RTD
from random import randint
from time import sleep

print("Lets roll some dice, but first choose your options.")
sleep (.5)
num_dice = int(input("How many dice would you like to roll? \n"))
faceD = int(1)
faceX = int(input("How many sides would you like your dice to have? \n"))

repeat = True
while repeat:
    print("Rolling the dice...")
    sleep(.5)
    roll = [randint(faceD, faceX)for die in range(num_dice)]
    print(f"You rolled: {roll}")
    sleep(.5)

    print("Want to roll again?  Y or N")
    repeat = ("y") in input().lower()
