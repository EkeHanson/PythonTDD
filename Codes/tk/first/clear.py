import turtle
import random

t = turtle.Turtle()

t.getscreen().bgcolor("#000000")
t.speed(100)
t.color("white", "yellow")

def draw_star(turle_ob, size):
    for _ in range(5):
        t.forward(size)
        t.left(215)

for _ in range(100):
    x, y = random.randint(-700,700), random.randint(-700, 700)
    t .penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    draw_star(t,random.randint(5,25))
    t.end_fill()

t.clear()

turtle.done()