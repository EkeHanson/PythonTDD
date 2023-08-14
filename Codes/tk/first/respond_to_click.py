import turtle

turtle.getscreen().bgcolor("#000000")
# turtle.getscreen().onclick(turtle.goto)

def draw_square(x, y):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()

        turtle.color("red", "yellow")
    
        turtle.begin_fill()
        for _ in range(36):
                turtle.forward(150)
                turtle.left(170)
        turtle.end_fill()

turtle.getscreen().onclick(draw_square)
turtle.speed(200)
draw_square(0,0)

turtle.done()