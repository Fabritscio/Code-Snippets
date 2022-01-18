
import turtle as t
t.speed(50)
t.lt(90)
t.pensize(7)
j = 1
c = ["red", "black", "brown", "blue", "purple", "pink", "orange"]

def tree(i):
   global j
   if i < 10:
        return
   else:
        t.color(c[j%7])
        t.fd(i)
        t.lt(30)
        tree(3*i/4)
        t.rt(60)
        tree(3*i/4)
        t.lt(30)
        t.backward(i)
        j += 1
tree(100)
t.mainloop()

