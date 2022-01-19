import turtle

pat = turtle.Turtle()
scr = turtle.Screen()

scr.bgcolor("Black")
pat.speed(0)

radius = 60
pat.pensize(2)
colour = ["blue", "yellow", "green"]
for x in range(10):

    pat.color(colour[0])
    for i in range(6):
      pat.circle(radius)
      pat.right(50)
    radius = radius + 4

turtle.done()
