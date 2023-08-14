import turtle

t = turtle.Turtle()

t.getscreen().bgcolor("#000000")

def draw_star(turle_ob, size):
    for _ in range(5):
        t.forward(100)
        t.left(215)



draw_star(t,100)

turtle.done()