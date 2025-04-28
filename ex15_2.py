import turtle
import math

class Point:
        """Represents a point (x,y) in 2-D space. Attributes are x and y."""
        
class Rectangle:
        """Represents a rectangle with attributes width, height, corner."""

class Circle:
        """Represents a circle with attributes center (a Point) and radius (a number)."""

def draw_rect(t, rect):
    
    t.fd(rect.width)
    t.lt(90)
    t.fd(rect.height)
    t.lt(90)
    t.fd(rect.width)
    t.lt(90)
    t.fd(rect.height)

    turtle.mainloop()

def draw_circle(t, circle):
    
    circumf = 2 * math.pi * circle.radius
    len = circumf / 360

    for i in range(300):
        t.fd(len)
        t.lt(360/300)

    turtle.mainloop()

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 50.0
box.corner.y = 50.0

circle = Circle
circle.center = Point()
circle.center.x = 150.0
circle.center.y = 100.0
circle.radius = 75.0

#bill = turtle.Turtle()
#draw_rect(bill, box)

bob = turtle.Turtle()
draw_circle(bob, circle)

