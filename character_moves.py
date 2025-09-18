import pico2d
from pico2d import *

open_canvas()

character = load_image('character.png')

def move_top():
    print('Moving top')
    for x in range(0,800,10):
        draw_character(x,550)
    pass

def move_left():
    print('Moving left')
    for y in range(25, 550, 10):
        draw_character(0, y)
    pass

def move_right():
    print('Moving right')
    for y in range(550, 25, -10):
        draw_character(800, y)
    pass

def move_bottom():
    print('Moving bottom')
    for x in range(800, 0, -10):
        draw_character(x, 25)
    pass

def move_rectangle():
    print("Moving rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass

def draw_character(x: float, y: float):
    clear_canvas_now()
    character.draw_now(x, y)
    delay(0.1)


def move_circle():
    print("Moving circle")
    r = 200
    for deg in range(0, 360):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        draw_character(x, y)
    pass


while True:
    move_rectangle()
    move_circle()
    pass


close_canvas()