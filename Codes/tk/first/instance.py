import turtle

t = turtle.Turtle()

def draw_square(turtl_object,size):
    turtl_object.begin_fill()
    turtl_object.forward(size)
    turtl_object.left(90)
    turtl_object.forward(size)
    turtl_object.left(90)
    turtl_object.forward(size)
    turtl_object.left(90)
    turtl_object.forward(size)
    turtl_object.end_fill()

t.color("red", "blue")
draw_square(t, 100)
t.penup()
t.forward(100)
t.pendown()
draw_square(t, 100)




turtle.done()