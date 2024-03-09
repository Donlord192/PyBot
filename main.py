import time
import keyboard
import random
import pyautogui

seter=1

while True:
    keyboard.press("w")
    time.sleep(random.random()*3)
    keyboard.release("w")

    pyautogui.moveRel(random.randint(-100000,100000),0,duration=0.8)
    if keyboard.is_pressed('p'):
        seter=2                                                         