import os
import time
import random
import pynput

WIDTH = 0
HEIGHT = 0
direction = 0
directionX = 1
xfood = 0
yfood = 0
snake = [{'x': 1, 'y': 2}, {'x': 2, 'y': 2}]


def draw():
    pass


def move():
    global snake
    new_head = snake[-1]
    if direction == 1:
        new_head['y'] += 1
    if direction == 2:
        new_head['y'] -= 1
    if directionX == 3:
        new_head['x'] -= 1
    if directionX == 4:
        new_head['x'] += 1
    snake.append(new_head)
    snake.pop(0)


def randfood():
    global xfood, yfood
    xfood = random.randint(0, WIDTH)
    yfood = random.randint(0, HEIGHT)


def on_press(key):
    global direction, directionX
    if key == pynput.keyboard.Key.up:
        direction = 1
    if key == pynput.keyboard.Key.down:
        direction = 2
    if key == pynput.keyboard.Key.left:
        directionX = 3
    if key == pynput.keyboard.Key.right:
        directionX = 4

def on_release(key):
    pass


pynput.keyboard.Listener(
    on_press=on_press,
    on_release=on_release
).start()

while True:
    os.system('cls')
#     draw()
    print(snake)
    move()
    print(snake)
    time.sleep(1)