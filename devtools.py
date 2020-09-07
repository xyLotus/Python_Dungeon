from time import sleep
import keyboard

def hold_exit():
    print("[PRESS ENTER TO EXIT]")
    while 1:
        sleep(0.05)
        if keyboard.is_pressed("enter"):
            quit()
hold_exit()
