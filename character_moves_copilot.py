import pico2d
from pico2d import *
import math

open_canvas()

character = load_image('character.png')
speed = 10

# 삼각형 꼭짓점 좌표
A = (400, 450)  # top
B = (780, 70)   # right
C = (20, 70)    # left

def draw_character(x, y):
    clear_canvas_now()
    character.draw_now(x, y)
    delay(0.01)

def move_line(start, end, speed):
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
    distance = math.hypot(dx, dy)
    steps = int(distance // speed)
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2
        draw_character(x, y)
    draw_character(x2, y2)

def move_triangle():
    print("Moving triangle")
    move_line(A, B, speed)
    move_line(B, C, speed)
    move_line(C, A, speed)

def move_rectangle():
    print("Moving rectangle")
    rect_points = [(50, 550), (750, 550), (750, 50), (50, 50)]
    for i in range(4):
        move_line(rect_points[i], rect_points[(i+1)%4], speed)

def move_circle():
    print("Moving circle")
    r = 200
    cx, cy = 400, 300
    for deg in range(0, 360, 2):
        x = r * math.cos(math.radians(deg)) + cx
        y = r * math.sin(math.radians(deg)) + cy
        draw_character(x, y)
    draw_character(cx + r, cy)

while True:
    move_rectangle()
    move_triangle()
    move_circle()
    pass

close_canvas()

