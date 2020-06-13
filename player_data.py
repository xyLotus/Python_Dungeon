import os, random, sys, clear, main_screen
from player_stats import stats
from time import sleep
import pyfiglet

def texter(text):
    return pyfiglet.figlet_format(text, font="standard")


def typewrite(word, time):
    for char in word:
        sleep(time)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n")

def player_tab():
    global HP
    global level
    if stats.XP >= 100:
        typewrite(texter("[+[Level up!]+]"), 0.0025)
        sleep(1)
        stats.level+=1
        stats.XP = 1
        clear.trigger()
    f = open("playerdata.txt", "r")
    print("\n<==========[-[+]-]==========>")
    print("Username: " + str(f.read()))
    print("Your HP: " + str(stats.HP))
    print("Your XP: " + str(stats.XP))
    print("Your power: " + str(stats.power))
    print("Your level: " + str(stats.level))
    print("<==========[-[+]-]==========>")

def player_tab_exit():
    global HP
    wrong = False
    f = open("playerdata.txt", "r")
    if stats.XP >= 100:
        typewrite(texter("<===[+[Level up!]+]===>"))
        level+=1
        stats.XP = 1
    print("\n<==========[-[+]-]==========>")
    print("Username: " + str(f.read()))
    print("Your HP: " + str(stats.HP))
    print("Your XP: " + str(stats.XP))
    print("Your power: " + str(stats.power))
    print("Your level: " + str(stats.level))
    print("<==========[-[+]-]==========>")
    print("1) Exit")
    choice = int(input("<option> "))
    if choice == 1:
        clear.trigger()
        main_screen.trigger()
    else:
        print("invalid input")
        sleep(1)
        wrong = True
        while wrong == True:
            choice = int(input("<option> "))
            if choice == 1:
                wrong = False
                clear.trigger()
                main_screen.trigger()
            else:
                print("invalid input")
