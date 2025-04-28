#! python3

def most_frequent(inp):
    items = list(inp)

    d = dict()
    for c in items:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    
    sorted_d = sorted(d, key=d.get, reverse=True)
    print(sorted_d)
    
most_frequent('bookkeeper')
most_frequent('bippityboppityboo')
