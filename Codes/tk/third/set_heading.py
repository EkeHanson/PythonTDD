import turtle
import math

turtle.color("red")
turtle.speed(10)

turtle.begin_fill()
for i in range(2000):
    turtle.fd(math.sqrt(i)*10)
    turtle.left(i%180)
    







turtle.done()