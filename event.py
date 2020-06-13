import main_screen, clear, start
import os, random, sys
from player_stats import stats
from time import sleep
import pyfiglet

def texter_out(text):
    print(pyfiglet.figlet_format(text, font="standard"))

def texter(text):
    return pyfiglet.figlet_format(text, font="standard")

def typewrite(word, time):
    for char in word:
        sleep(time)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n")

def fight():
    v_count=0
    r_count=0
    prefix = ["You encounter a ", "You find a ", "You stumble upon a "]
    enemy_base = ["Slime", "Wolf", "Skeleton", "Spider"]
    global level
    global HP
    global XP
    global power
    global name
    global fighting

    os.system("cls")
    fighting = True

    print(random.choice(prefix) + random.choice(enemy_base) + "!")
    enemy_HP = random.randint(30,100)
    if enemy_HP <= 40:
        print("The enemy is easy")
    elif enemy_HP <= 65:
        print("The enemy is normal")
    elif enemy_HP <= 80:
        print("The enemy is hard")
    elif enemy_HP > 80:
        print("The enemy is super hard")
    sleep(1)
    while fighting:
        os.system("cls")
        if v_count != 1: lock_HP=enemy_HP; v_count+=1;

        print("<<===========[+[+]+]===========>>")
        print("Enemy HP: " + str(enemy_HP))
        print("Your HP: " + str(stats.HP))
        print("Your power: " + str(stats.power))
        print("<<===========[+[+]+]===========>>")
        print("")
        print("<======[-[+]-]======>")
        print("1) Normal Attack")
        print("2) Hard Attack")
        print("3) Run away")
        print("<======[-[+]-]======>")

        if stats.HP <= 0:
            typewrite(texter("Game Over!"), 0.0025)
            sleep(5)
            exit()
        elif stats.power <= 0:
            clear.trigger()
            count = 0
            while count != 15:
                sleep(0.2)
                count+=1
                sys.stdout.write('.')
                sys.stdout.flush()
                if count % 3 == 0:
                    clear.trigger()
            typewrite("You wake up back at your camp...", 0.05)
            typewrite("You ran out of stamina!", 0.05)
            typewrite("Rest a bit and regenerate.", 0.05)
            sleep(3)
            v_count=0
            clear.trigger()
            start.init()
        if enemy_HP <= 0:
            typewrite(texter("You won!"), 0.0025)
            sleep(1)
            if lock_HP <= 40:
                clear.trigger()
                texter_out("+10xp")
                stats.XP+=10
                sleep(1)
            elif lock_HP > 40 and lock_HP < 65:
                clear.trigger()
                texter_out("+30xp")
                stats.XP+=30
                sleep(1)
            elif lock_HP >= 65 and lock_HP < 80:
                clear.trigger()
                texter_out("+50xp")
                stats.XP+=50
                sleep(1)
            elif lock_HP >= 80 and lock_HP <= 100:
                clear.trigger()
                texter_out("+80xp")
                stats.XP+=80
                sleep(1)

            v_count=0
            clear.trigger()
            start.init()

        choice = int(input("<attack> "))
        if choice == 1:
            enemy_HP-=random.randint(4,15)
            stats.HP-=random.randint(4,8)
            stats.power-=random.randint(4,5)
        elif choice == 2:
            enemy_HP-=random.randint(8,25)
            stats.HP-=random.randint(6,14)
            stats.power-=random.randint(13,20)
        elif choice == 3 and r_count != 1:
            if random.randint(0,10) >= 6:
                print("You ran away!")
                sleep(1)
                os.system("cls")
                start.init()
            else:
                print("You failed to run away")
                r_count+=1
                sleep(1)
        elif choice == 3 and r_count == 1:
            print("You can't run away, you already tried once!")
            sleep(1)

    main_screen.trigger()

def rest():
    global level
    global HP
    global XP
    global power
    global name
    global HP

    print("Your HP: " + str(stats.HP))
    print("\nHow long do you want to rest for?")
    print("1 minute = 1hp / 1 minute = 1 power || max. Time = 60 minutes")
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

    print("You rested " + str(rest_time) + " and regenerated " + str(rest_time) + "HP || " + str(rest_time) + " power")

    stats.HP+=rest_time
    stats.power+=rest_time

    if stats.HP > 100:
        stats.HP = 100
    if stats.power >= 100:
        stats.power = 100

    print("Current HP: " + str(stats.HP))
    print("Current power: " + str(stats.power))

    sleep(3)

    os.system("cls")

    start.init()
