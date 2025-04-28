#! python3

from random import randint

# generate 23 random integers between 1 and 365
# sort them, and check whether there are any duplicates, add 1 to a counter if True
# repeat 1000 times

num_iter = 10000

total = 0

#x = []
#for j in range(23):
#    x.append(randint(1,365))
#    x.sort()
#print(x)

for i in range(num_iter):
    cond = False
    x = []
    for j in range(23):
        x.append(randint(1,365))
        x.sort()
    for k in range(1, len(x)):
        if x[k] == x[k-1]:
            cond = True
        else:
            continue
    if cond == True:
        total += 1
    else:
        continue

birthday = total / num_iter
print(f"The probability that at least 2 students in a class of 23 have the same birthday: {birthday}")