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

def petal(t):
    
    for i in range(2):
        arc(t, 40, 20)
        t.lt(160)

def flower_20(t):
    
    for i in range(20):
        petal(t)
        t.lt(18)
    
    turtle.mainloop()

bill = turtle.Turtle()
flower_20(bill)