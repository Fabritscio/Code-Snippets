import turtle
import time

turtle.setup(500, 500)
turtle.bgcolor("black")
leo = turtle.Turtle()
leo.pencolor("DeepSkyBlue")
leo.speed(0)

def spiral():
    for i in range(360):
     leo.forward(i * 3)
     leo.right(121)

def spin(d):
    leo.penup()
    leo.home()
    leo.left(d * n)
    leo.down()

try:
    n = 0
    while True:
        turtle.tracer(0)
        leo.clear()
        spin(3)
        spiral()
        n += 1
        turtle.update()
        time.sleep(0.01)
except:
     print("Exit")

     turtle.done()
