import random
import time

user_input = "yes"

while user_input == "yes" or user_input == "y":
    print ("Dice is rolling....")
    time.sleep(1)

    dicefirst = random.randint(1, 6)
    dicesecond = random.randint(1, 6)

    print("Dice-1 value is : ",dicefirst,"\nDice-2 value is : ",dicesecond)
    time.sleep(1)

    if (dicesecond == dicefirst):
        print ("Congrats you got the same value!")

    user_input = input("Do you want to role the dice again ? (y/n) : ").lower()

    print ("Thanks for playing!!!!") 