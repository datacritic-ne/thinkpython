import turtle
import math

def triangle(t, len, angle): # where len is the length of the two equal sides, and angle is the half peak angle in degrees
    
    y = len * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(len)
    t.lt(90 + angle)
    t.fd(2 * y)
    t.lt(90 + angle)
    t.fd(len)
    t.lt(180 - angle)

def polygon(t, sides):

    angle = 360 / sides
    for i in range(sides):
        triangle(t, 30, angle/2)
        t.lt(angle)

    turtle.mainloop()

bill = turtle.Turtle()
polygon(bill, 7)