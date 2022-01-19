import turtle
a = turtle.Turtle()
a.getscreen().bgcolor("blue")
a.penup()
a.goto(-100, 200)
a.pendown()
a.speed(15)

def star(turtle, size):
    if size <= 8:
        return
    else:
        turtle.begin_fill()
    for i in range(5):
        turtle.forward(size)
        star(turtle, size/3)
        turtle.left(216)
        turtle.end_fill()
star(a, 420)
turtle.done()
