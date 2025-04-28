#! python3

def is_sorted(l):
    cond = True
    for i in range(1,len(l)):
        if l[i] < l[i-1]:
            cond = False
        else:
            continue
    print(cond)

llist = [10,3,5,7,7]
is_sorted(llist)