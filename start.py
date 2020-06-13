import event, blacksmith, player_data
from player_stats import stats
import username
import os, random, sys

f = open("playerdata.txt", "r")

def init():
    global level
    global HP
    global XP
    global power
    global name
    print("You enter the dark Python Dungeon...")
    print("The game begins... ")


    player_data.player_tab()

    print("\n What do you want to do?")
    print("<========[-[+]-]========>")
    print("1) Kill, Kill, Kill")
    print("2) Rest ")
    print("3) Blacksmith")
    print("<========[-[+]-]========>")


    choice = str(input("<choice> "))
    if choice == "1":
        event.fight()
    elif choice == "2":
        event.rest()
    elif choice == "3":
        blacksmith.shop()
    else:
        print("invalid input")
        wrong = True
        while wrong:
            choice = str(input("<choice> "))
            if choice == "1":
                event.fight()
                wrong = False
            if choice == "2":
                event.rest()
                wrong = False
            elif choice == "3":
                blacksmith.shop()
                wrong = False
    f.close()
