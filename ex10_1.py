#! python3

def nested_sum(lol):
    total = 0
    listo_total = 0
    for listo in range(len(lol)):
        listo_total += sum(lol[listo])
    total += listo_total
    print(total)

llist = [[1,2,3,5],[3],[4,5,6],[2,10,21]]
nested_sum(llist)