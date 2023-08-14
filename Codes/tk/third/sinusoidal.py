import turtle
import math

turtle.color("red")
turtle.speed(100)

turtle.begin_fill()
for i in range(2000):
    turtle.forward(10)
    turtle.left(math.sin(i/10)*25)
    turtle.left(20)
    
    







turtle.done()