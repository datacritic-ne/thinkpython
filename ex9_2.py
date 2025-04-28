#! python3

file1 = open('words.txt', 'r')

words = file1.readlines()

total = 0
tot_no_e = 0

for word in words:
    line = word.strip()
    total += 1
    check = line.find('e')
    if check != -1:
        tot_no_e += 1
    else:
        tot_no_e += 0
    
final = tot_no_e / total
print(f'The proportion of words in words.txt with no e: {final}')