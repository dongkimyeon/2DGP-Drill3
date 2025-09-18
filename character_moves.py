import pico2d
from pico2d import *

open_canvas()

character = load_image('character.png')
def move_rectangle():
    print("Moving rectangle")
    pass

def move_circle():
    print("Moving circle")
    clear_canvas_now()
    character.draw_now(400,300)
    delay(0.1)
    pass


while True:
    move_rectangle()
    move_circle()
    pass


close_canvas()