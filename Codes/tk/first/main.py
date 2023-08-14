# import turtle


# turtle.color("red", "blue")
# turtle.begin_fill()
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)

# turtle.end_fill()



# turtle.done()



import turtle

def draw_square(size):
    turtle.begin_fill()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.end_fill()


turtle.getscreen().bgcolor("#FFFF00")
turtle.color("red", "blue")
draw_square(100)
turtle.penup()
turtle.forward(100)
turtle.pendown()
draw_square(100)




turtle.done()