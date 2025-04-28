import math

def mysqrt(a):
    
    x = 5
    epsilon = 0.0000001
    
    while True:
        #print(x)
        y = (x + a/x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return y
    
def test_square_root(a):

    print("a   ","mysqrt(a)    ","math.sqrt(a) ","diff")
    print("-   ","---------    ","------------ ","----")

    for i in range(9):
        mysqrt(a)
        math.sqrt(a)
        diff = math.sqrt(a) - mysqrt(a)

        print(a, "  ", mysqrt(a), "         ", math.sqrt(a), "         ", diff)

        a += 1

test_square_root(1)