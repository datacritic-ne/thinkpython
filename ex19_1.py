#! python3

def binomial_coeff(n, k):
    """Compute the 'n choose k' binomial coefficient
    
    n: number of trials
    k: number of successes
    
    returns: int"""

    if k == 0:
        return 1
    if n == 0:
        return 0
    
    res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
    return res

def binomial_coeff_alt(n, k):
    return 1 if k == 0 else (0 if n == 0 else binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1))

print(binomial_coeff(11, 7))
print(binomial_coeff_alt(11, 7))