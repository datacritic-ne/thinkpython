def gcd(a, b):

    #r = a % b

    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
print(gcd(24, 16))