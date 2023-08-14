import turtle

bob = turtle.Turtle()
bob.color("#3c9118", "cyan")

bob.begin_fill()
bob.fd(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.end_fill()
bob.penup()

bob.forward(150)
bob.pendown()
bob.begin_fill()
bob.fd(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.end_fill()




turtle.done()