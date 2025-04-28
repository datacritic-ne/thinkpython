#! python3

def chop(l):
    del l[0]
    del l[-1]
    #print(l)

llist = [1,2,3,4,5]
chop(llist)