import turtle

turtle.getscreen().bgcolor("#000000")

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


turtle.speed(200)
draw_square(0,0)

turtle.done()