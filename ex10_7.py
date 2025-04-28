#! python3

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

llist = [1,3,5,7]
has_duplicates(llist)

llist = [1,3,3,5,7]
has_duplicates(llist)