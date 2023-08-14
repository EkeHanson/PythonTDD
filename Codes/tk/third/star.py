import turtle
import math

turtle.getscreen().bgcolor("#994444")
turtle.color("red", "cyan")
turtle.speed(0)


def star(size):
    if size <=10:
        return 
    else:
        turtle.begin_fill()
        for _ in range(5):
            turtle.forward(size)
            star(size/3)
            turtle.left(216)
        turtle.end_fill()
    
star(360)






turtle.done()