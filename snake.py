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
foods = {'x': 6, 'y': 5}
WIDTH = 30
HEIGHT = 20
food_not_into_snake = True


def draw():
    global foods
    y = 0
    while y < HEIGHT + 1:
        x = 0
        result = ""
        while x < WIDTH + 1:
            char = ' '
            for item in snake:
                if x == item["x"] and y == item["y"]:
                    char = "0"
                if x == foods['x'] and y == foods['y']:
                    char = '*'
                if x == 0 or x == WIDTH:
                    char = '█'
                if y == 0 or y == HEIGHT:
                    char = '█'
            result += char
            x += 1
        print("" + result)
        y += 1


def move():
    global snake, foods
    new_head = snake[-1].copy()
    if direction == 1:
        new_head['y'] += 1
    if direction == 2:
        new_head['y'] -= 1
    if direction == 3:
        new_head['x'] -= 1
    if direction == 4:
        new_head['x'] += 1
    if new_head['x'] == foods['x'] and new_head['y'] == foods['y']:
        randfood()
    else:
        snake.pop(0)
    snake.append(new_head)


def randfood():
    global foods, xfood, yfood, food_not_into_snake
    food_not_into_snake = True
    while food_not_into_snake:
        xfood = random.randint(1, WIDTH - 1)
        yfood = random.randint(1, HEIGHT - 1)
        foods = {'x': xfood, 'y': yfood}
        food_not_into_snake = False
        for item in snake:
            if item['x'] == foods['x'] and item['y'] == foods['y']:
                food_not_into_snake = True
                return foods


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

randfood()
while True:
    os.system('cls')
    draw()
    move()
    time.sleep(0.1)
