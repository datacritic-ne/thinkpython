def do_twice(f, g):
    f(g)
    f(g)

#def print_spam():
#    print('spam')

do_twice(print, 'spam')

def print_twice(s):
    print(s)
    print(s)

do_twice(print_twice, 'spam')

def do_four(i, j):
    i(j)
    i(j)
    i(j)
    i(j)

do_four(print, 'spam')