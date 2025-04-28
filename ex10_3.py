#! python3

def middle(l):
    l_a = l.pop(0) # remove the first element
    l_b = l.pop(-1) # remove the last element
    print(l)

llist = [1,2,3,4,5,6,7,8,9,10]
middle(llist)