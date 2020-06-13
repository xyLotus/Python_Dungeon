import clear, start, player_stats
import os, random, sys

def trigger():
    global level
    global HP
    global XP
    global power
    global name

    print("""
      ____        _   _
     |  _ \ _   _| |_| |__   ___  _ __
     | |_) | | | | __| '_ \ / _ \| '_ \

     |  __/| |_| | |_| | | | (_) | | | |
     |_|    \__, |\__|_| |_|\___/|_| |_|
            |___/
      ____
     |  _ \ _   _ _ __   __ _  ___  ___  _ __
     | | | | | | | '_ \ / _` |/ _ \/ _ \| '_ \

     | |_| | |_| | | | | (_| |  __/ (_) | | | |
     |____/ \__,_|_| |_|\__, |\___|\___/|_| |_|
                        |___/

    <================[+[+]+]================>
    1) Play
    2) Quit
    3) Stats
    <================[+[+]+]================>
    """)

    choice = str(input("<option> "))
    if choice == "1":
        clear.trigger()
        start.init()
    elif choice == "2":
        clear.trigger()
        exit()
    elif chocie == "3":
        clear.trigger()
        player_data.stats()
    else:
        print("invalid input!")
        sleep(2)
        clear.trigger()
        exit()
