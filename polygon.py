import turtle

def polygon(t, n, len):

    for i in range(n):
        t.fd(len)
        t.lt(360 / n)

    turtle.mainloop()

bill = turtle.Turtle()
polygon(bill, 9, 100)