import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.color("red")
turtle.speed(0)

for colour in ["red", "orange", "yellow", "green","blue", "purple"]:
    turtle.color(colour)
    turtle.circle(150)
    turtle.left(60)

turtle.done()