def is_power(a, b):

    #if b > 0:
    #    return True
    if a % b == 0 and (a / b) % b == 0:
        return True
    else:
        return False
    #return is_power(a / b, b)

print(is_power(15, 5))