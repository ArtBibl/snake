import os
import random
import time

import pynput

direction = 1
xfood = 0
yfood = 0
snake = [{'x': 1, 'y': 2},
         {'x': 2, 'y': 2},
         {'x': 3, 'y': 2},
         {'x': 4, 'y': 2}]
foods = [{'x': 6, 'y': 5}]
WIDTH = 30
HEIGHT = 10


def draw():
    y = 0
    while y < HEIGHT:
        x = 0
        result = " "
        while x < WIDTH:
            char = ' '
            for item in snake:
                if x == item["x"] and y == item["y"]:
                    char = "0"
            for food in foods:
                if x == food['x'] and y == food['y']:
                    char = '#'
            result += char
            x += 1
        print(" " + result)
        y += 1


def move():
    global snake
    new_head = snake[-1].copy()
    if direction == 1:
        new_head['y'] += 1
    if direction == 2:
        new_head['y'] -= 1
    if direction == 3:
        new_head['x'] -= 1
    if direction == 4:
        new_head['x'] += 1
    snake.append(new_head)
    snake.pop(0)


def randfood():
    global foods
    xfood = random.randint(0, WIDTH)
    yfood = random.randint(0, HEIGHT)
    foods = [{'x': xfood, 'y': yfood}]


def on_press(key):
    global direction
    if key == pynput.keyboard.Key.up:
        direction = 2
    if key == pynput.keyboard.Key.down:
        direction = 1
    if key == pynput.keyboard.Key.left:
        direction = 3
    if key == pynput.keyboard.Key.right:
        direction = 4


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
    time.sleep(0.1)
