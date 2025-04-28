#! python3

import math
import copy

class Point:
        """Represents a point (x,y) in 2-D space. Attributes are x and y."""
        
class Rectangle:
        """Represents a rectangle with attributes width, height, corner."""

class Circle:
        """Represents a circle with attributes center (a Point) and radius (a number)."""

def dist_betw_points(p1, p2):
    
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(dx**2 + dy**2)
    return dist

def point_in_circle(point, circle):
    
    d = dist_betw_points(point, circle.center)
    return d <= circle.radius

def rect_in_circle(rect, circle):
    
    p = copy.copy(rect.corner)
    if not point_in_circle(p, circle):
        return False
    
    p.x += rect.width
    if not point_in_circle(p, circle):
        return False
    
    p.y -= rect.height
    if not point_in_circle(p, circle):
        return False
    
    p.x -= rect.width
    if not point_in_circle(p, circle):
        return False
    
    return True
    
def rect_circle_overlap(rect, circle):
    
    p = copy.copy(rect.corner)

    if point_in_circle(p, circle):
        return True
    
    p.x += rect.width
    if point_in_circle(p, circle):
        return True
    
    p.y -= rect.height
    if point_in_circle(p, circle):
        return True
    
    p.x -= rect.width
    if point_in_circle(p, circle):
        return True
    
    return False

def main():
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

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))

if __name__ == '__main__':
     main()