import pico2d
from pico2d import *

open_canvas()

character = load_image('character.png')

def move_top():
    pass

def move_left():
    pass

def move_right():
    pass

def move_bottom():
    pass

def move_rectangle():
    print("Moving rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass

def move_circle():
    print("Moving circle")
    r = 200
    for deg in range(0, 360):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        clear_canvas_now()
        character.draw_now(x, y)
        delay(0.1)
    pass


while True:
    move_rectangle()
    move_circle()
    pass


close_canvas()