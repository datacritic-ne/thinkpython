#! python3

memo = {}

def ack(m, n):
    
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m-1, 1)
    
    if (m, n) in memo:
        return memo[m, n]
    else:
        memo[m, n] = ack(m-1, ack(m, n-1))
        return memo[m, n]
    
print(ack(2, 2))
print(ack(2, 4))
print(ack(3, 4))
print(ack(4, 5))
print(ack(5, 6))
print(ack(6, 8))

