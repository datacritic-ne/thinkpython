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

def flower_10(t):
    
    for i in range(10):
        arc(t, 40, 150)
        t.lt(102)
    
    turtle.mainloop()

bill = turtle.Turtle()
flower_10(bill)