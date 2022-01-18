import turtle

t = turtle.Turtle()
s = turtle.Screen()
t.speed(12)

s.bgcolor("black")

col = ("green", "red", "blue", "yellow")
c = 0

for i in range(100):
    t.forward(i*10)
    t.right(200)
    t.color(col[c])
    if c == 3:
        c = 0
    else:
        c += 1
