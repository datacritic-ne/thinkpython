#! python 3

def has_duplicates(l):
    x = l
    x.sort()
    cond = False
    for i in range(1, len(x)):
        if x[i] == x[i-1]:
            cond = True
        else:
            continue
    print(cond)

def has_dupes_alt(l):
    cond = False
    d = dict()
    for item in l:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1
    #return d
    for item in d:
        if d[item] > 1:
            cond = True
        else:
            continue
    print(cond)

llist = [1,3,5,7,9,11]
has_duplicates(llist)
has_dupes_alt(llist)

llist2 = [1,3,5,5,6,9,10]
has_duplicates(llist2)
has_dupes_alt(llist2)