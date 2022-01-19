import turtle as t
t.speed(12)
t.bgcolor("black")

c = ["blue", "red", "purple", "green",
     "yellow", "magenta", "aqua"]

a = 750
for i in range(a//50):
    t.penup()
    t.goto(0, 0)
    t.fd(a/2)
    t.rt(160)
    t.pendown()
    t.begin_fill()
    t.color(c[i%7])
    for j in range(5):
        t.fd(a)
        t.rt(144)
    t.end_fill()
    t.rt(144 + 60)
t.mainloop()
