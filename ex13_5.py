#! python3
# the 'histogram' module reports frequencies of each item - this one returns probabilities of each item

import random

def choose_from_hist(s):

    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    for i in d:
        e = d[i] / sum(d.values())
        print(i, e)

test = ['a', 'a', 'b']
choose_from_hist(test)