from player_stats import stats
import os, random, sys



def player_tab():
    global HP
    f = open("playerdata.txt", "r")
    print("\n<==========[-[+]-]==========>")
    print("Username: " + str(f.read()))
    print("Your HP: " + str(stats.HP))
    print("Your XP: " + str(stats.XP))
    print("Your power: " + str(stats.power))
    print("Your level: " + str(stats.level))
    print("<==========[-[+]-]==========>")
