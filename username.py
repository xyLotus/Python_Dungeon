import player_stats
import os, random, sys

f = open("playerdata.txt", "w")

def trigger():
    global name
    wrong = False
    name = str(input("<character-name> "))
    if name == "" or name == " ":
        print("invalid input.")
        wrong = True
    else:
        pass

    while wrong:
        name = str(input("<character-name> "))
        if name == "" or name == " ":
            print("invalid input.")
            wrong == True
        else:
            wrong = False
    f.write(name)
    f.close()
