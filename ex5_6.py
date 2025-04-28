import turtle

def koch(t, length):

    if length < 3:
        t.fd(length)
        return
    m = length / 3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)

def snowflake(t, length):

    for i in range(3):
        koch(t, length)
        t.rt(120)

bill = turtle.Turtle()
snowflake(bill, 300)

turtle.mainloop()