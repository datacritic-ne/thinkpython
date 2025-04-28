import turtle

def square(t, len):
    #t = turtle.Turtle()

    for i in range(4):
        t.fd(len)
        t.lt(90)

    turtle.mainloop()

bill = turtle.Turtle()
square(bill, 100)