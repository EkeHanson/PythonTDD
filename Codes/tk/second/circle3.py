import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.color("red")
turtle.speed(0)



for i in range(12):
    for colour in ["red", "orange", "yellow", "green","blue", "purple"]:
        turtle.color(colour)
        turtle.circle(150)
        turtle.left(5)

turtle.done()