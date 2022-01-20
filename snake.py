import os
import time

import pynput

direction = x


def draw():
    pass


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
