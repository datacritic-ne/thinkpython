import turtle
import math

def polygon(t, n, len):

    for i in range(n):
        t.fd(len)
        t.lt(360 / n)

def circle(t, r):
    
    circumf = 2 * math.pi * r
    print(circumf)
    len = circumf / 360
    print(len)
    polygon(t, 360, len)
    
    turtle.mainloop()

bill = turtle.Turtle()
print(bill)
circle(bill, 300)
