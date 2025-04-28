def is_triangle(a, b, c):

    if (a > b + c) or (b > a + c) or (c > a + b):
        print("Nope")
    else:
        print("Yep")

def user_check():

    a = int(input("Give me a length for side a: "))
    b = int(input("Give me a length for side b: "))
    c = int(input("Give me a length for side c: "))

    is_triangle(a, b, c)

user_check()