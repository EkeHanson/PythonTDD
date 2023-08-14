import turtle

colors = ["red", "orange", "yellow","green","blue","indigo"]
turtle.speed(500)

turtle.bgcolor("black")
for i in range(360):
    turtle.pencolor(colors[i % 6])
    turtle.width(i // 100 +1)
    turtle.forward(i)
    turtle.left(59)


turtle.done()