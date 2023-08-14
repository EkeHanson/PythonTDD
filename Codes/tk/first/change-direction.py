import turtle
import random

t = turtle.Turtle()

t.getscreen().bgcolor("#000000")
t.speed(100)
t.color("white", "yellow")

def draw_square(turle_ob, size):
    for _ in range(3):
        t.forward(size)
        t.setheading(90)
        t.forward(size)
       

draw_square(t, 40)

turtle.done()