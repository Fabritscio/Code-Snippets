import turtle
t = turtle.Turtle()
list1 = ["yellow", "blue", "green", "red"]
t.up()
t.goto(150,0)
for i in range(4):
    t.down()
    t.begin_fill()
    t.fillcolor(list1[i])
    t.circle(50)
    t.end_fill()
    t.up()
    t.bk(100)
