import os
import random
import sys
from time import sleep

# >> Char Stats <<
HP = 100
name = str(input("<character-name> "))
fighting = False
wrong = False

if name == "" or name == " ":
    print("invalid input.")
    wrong = True
else:
    pass

while wrong:
    print("toggled")
    name = str(input("<character-name> "))
    if name == "" or name == " ":
        print("invalid input.")
        wrong == True
    else:
        wrong = False
power = 100

level = 0

XP = 1

# >> enemy / event list
enemy_base = ["Slime", "Wolf", "Skeleton", "Spider"]
event_list = ["You encounter a ", "You find a ", "You stumble upon a "]

# main functions
def clear():
    os.system("cls")

def fight():
    global level
    global HP
    global XP
    global power
    global name
    global fighting

    os.system("cls")
    fighting = True

    print(random.choice(event_list) + random.choice(enemy_base) + "!")
    enemy_HP = random.randint(10,100)
    print("Enemy HP: " + str(enemy_HP))

    if enemy_HP <= 40:
        print("The enemy is easy")
    elif enemy_HP <= 65:
        print("The enemy is normal")
    elif enemy_HP <= 80:
        print("The enemy is hard")
    elif enemy_HP > 80:
        print("The enemy is super hard")

    while fighting:
        os.system("cls")
        print("Enemy HP: " + str(enemy_HP))
        print("Your HP: " + str(HP))
        print("Your power: " + str(power))
        print("<======[-[+]-]======>")
        print("1) Normal Attack")
        print("2) Hard Attack")
        print("3) Run away")
        print("<======[-[+]-]======>")

        if HP <= 0:
            print("""
               ____                         ___
              / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __
             | |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
             | |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |
              \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|
            """)
            sleep(5)
            exit()
        elif power <= 0:
            clear()
            count = 0
            while count != 15:
                sleep(0.2)
                count+=1
                sys.stdout.write('.')
                sys.stdout.flush()
                if count % 3 == 0:
                    clear()
            cont_next()
        if enemy_HP <= 0:
            print("Won fight!")

            if enemy_HP <= 40:
                print("+10xp")
                XP+=10
            elif enemy_HP <= 65:
                print("+30xp")
                XP+=30
            elif enemy_HP <= 80:
                print("+50xp")
                XP+=50
            elif enemy_HP > 80:
                print("+80xp")
                XP+=80
            clear()
            cont_next()

        if XP % 100 == 0:
            print("[+[+]+] Level up! [+[+]+]")
            level+=1
            XP = 1

        choice = int(input("<attack> "))
        if choice == 1:
            enemy_HP-=random.randint(4,15)
            HP-=random.randint(4,8)
            power-=5
        elif choice == 2:
            enemy_HP-=random.randint(8,25)
            HP-=random.randint(6,14)
            power-=20
        elif choice == 3:
            if random.randint(0,10) >= 6:
                print("You ran away!")
                cont_next()
            else:
                print("You failed to run away")

    main_screen()

def rest():
    global level
    global HP
    global XP
    global power
    global name
    global HP

    print("Your HP: " + str(HP))
    print("\nHow long do you want to rest for?")
    print("1 minute = 1hp || max. Time = 60 minutes")
    rest_time = int(input("<rest-time> "))

    if rest_time > 60:
        print("Invalid Input try again")
        invalid_input = True
        while invalid_input:
            rest_time = int(input("<rest-time> "))
            if rest_time > 60:
                print("Invalid Input try again")
            else:
                invalid_input = False

    print("You rested " + str(rest_time) + " and regenerated " + str(rest_time) + "HP")
    HP+=rest_time
    if HP > 100:
        HP = 100
    print("Current HP: " + str(HP))

    sleep(3)

    os.system("cls")

    main_screen()

def blacksmith():
    clear()
    print("""
                      `yNms/`
                    :ydMMMMMm
                    oMMMMMMN-
                   .dMMMMMNNNho:``
                   :ymNMMd-:odNNNho:``
                      -/s.    `:ohmNNho:.`
                                  `:ohmNNho:.`
                                      `:ohmNNho:.`
                                          .:ohmNNy
                                              .:+-


                `::::::::::::::::::::::::::::`
+yysyyyyyyyyyyyddMMMMMMMMMMMMMMMMMMMMMMMMMMMM-      1) Upgrade Sword
`smmhhdmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdh.      2) Upgrade Armor
  ./syyo+++oossmMMMMMMMMMMMMMMMMMMMMNhs/-.``        3) Exit
     `..-:/+++odMMMMMMMMMMMMMMMMMMNo.`
             ``.-+hMMMMMMMMMMMMMMM:
                  `+MMMMMMMMMMMMMN
                    mMMMMMMMMMMMMM.
                   -NMMMMMMMMMMMMMm:
               `:ohNMMMd+-...-:yNMMNdo-
               .NNNNNNh`        /NNNNNd
    """)

def stats():
    global level
    global HP
    global XP
    global power
    global name

    print("<==========[-[+]-]==========>")
    print("Username: " + str(name))
    print("Your HP: " + str(HP))
    print("Your XP: " + str(XP))
    print("Your power: " + str(power))
    print("Your level: " + str(level))
    print("<==========[-[+]-]==========>")

def main_screen():
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
        clear()
        cont_next()
    elif choice == "2":
        clear()
        exit()
    elif chocie == "3":
        clear()
        stats()
    else:
        print("invalid input!")
        sleep(2)
        clear()
        exit()

def cont_next():
    global level
    global HP
    global XP
    global power
    global name
    print("You enter the dark Python Dungeon...")
    print("The game begins... ")


    print("\Your Stats: ")
    print("Your HP: " + str(HP))
    print("Your level: " + str(level))
    print("Your power: " + str(power))
    print("username: " + str(name))

    print("\n What do you want to do?")
    print("<========[-[+]-]========>")
    print("1) Kill, Kill, Kill")
    print("2) Rest ")
    print("3) Blacksmith")
    print("<========[-[+]-]========>")


    choice = str(input("<choice> "))
    if choice == "1":
        fight()
    elif choice == "2":
        rest()
    elif choice == "3":
        blacksmith()
    else:
        print("invalid input")
        wrong = True
        while wrong:
            choice = str(input("<choice> "))
            if choice == "1":
                fight()
                wrong = False
            if choice == "2":
                rest()
                wrong = False



main_screen()
