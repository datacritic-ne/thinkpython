#! python3

def cumsum(l):
    newlist = []
    newlist.append(l[0])
    for i in range(1,len(l)):
        newlist_add = newlist[i-1] + l[i]
        newlist.append(newlist_add)
    print(newlist)

listo = [1,2,3,4,5]
cumsum(listo)