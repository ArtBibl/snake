import os
import time

import pynput

direction = 1

WIDTH = 30
HEIGHT =10



def draw():
    y=0
    while y < HEIGHT:
        x = 0
        result = " "
        while x< WIDTH:
            char = 'o'
            for item in snake:
                if x == item["x"] and y == item["y"]:
                    char = " "
            result += char
            x +=1
        print(" " +result)
        y+=1


def move():
    pass


def randfood():
    pass


def on_press(key):
    pass


def on_release(key):
    pass


pynput.keyboard.Listener(
    on_press=on_press,
    on_release=on_release
).start()

while True:
    os.system('cls')
    draw()
    move()
    randfood()
    time.sleep(0.05)
