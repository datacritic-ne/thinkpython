import turtle
import math

def polygon(t, n, len, angle):

    for i in range(n):
        t.fd(len)
        t.lt(angle / n)

def arc(t, r, angle):
    
    circumf = 2 * math.pi * r
    len = circumf / 360
    polygon(t, 360, len, angle)
    
    turtle.mainloop()

bill = turtle.Turtle()
arc(bill, 100, 270)