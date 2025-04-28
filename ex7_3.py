import math

def estimate_pi():

    x = (2 * math.sqrt(2)) / 9801
    k = 0
    term = 0

    while True:
        num = math.factorial(4*k) * (1103 + 26390*k)
        den = math.factorial(k)**4 * 396**(4*k)
        
        term += num / den
        inverse = x * num/den

        if abs(inverse) < 1e-15:
            break
        k += 1
    
#    inverse = x * term
    return 1 / inverse

print(estimate_pi())
