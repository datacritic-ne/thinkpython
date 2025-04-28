#def box():
#    print("+ - - - - + - - - - +")
#    print("|         |         |")
#    print("|         |         |")
#    print("|         |         |")
#    print("|         |         |")
#    print("+ - - - - + - - - - +")
#    print("|         |         |")
#    print("|         |         |")
#    print("|         |         |")
#    print("|         |         |")
#    print("+ - - - - + - - - - +")

#box()

# OK, I guess I need to be cooler and functional about this

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print("+ - - - - ", end=" ")

def print_post():
    print("|         ", end=" ")

def print_beams():
    do_twice(print_beam)
    print("+")

def print_posts():
    do_twice(print_post)
    print("|")

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()

# Four by four grid

def print_long_beams():
    do_four(print_beam)
    print("+")

def print_long_posts():
    do_four(print_post)
    print("|")

def print_long_rows():
    print_long_beams()
    do_four(print_long_posts)

def print_big_grid():
    do_four(print_long_rows)
    print_long_beams()

print_big_grid()