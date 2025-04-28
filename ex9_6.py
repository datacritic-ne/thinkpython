#! python3

file1 = open('words.txt', 'r')
words = file1.readlines()

total = 0
total_alph = 0

for word in words:
    line = word.strip()
    letters = list(line)
    cond = True
    for i in range(1, len(letters)):
        if letters[i] < letters[i-1]:
            cond = False
        else:
            continue
    if cond == True:
        total += 1
        total_alph += 1
    else:
        total += 1
        total_alph += 0

final = total_alph / total
print(f"There are {total_alph} words that meet the alphabetical criterion, or {final} of the total.")