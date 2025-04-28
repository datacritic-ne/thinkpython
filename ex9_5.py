#! python3

#word = input("> ")
string = input("> ")

file1 = open('words.txt', 'r')
words = file1.readlines()

total = 0
total_using_all = 0

#def uses_all(w, str):
#    cond = True
#    letters = list(str)
#    for letter in letters:
#        if letter not in w:
#            cond = False
#        else:
#            continue
#    return cond

#uses_all(word, string)

for word in words:
    line = word.strip()
    cond = True
    letters = list(string)
    #uses_all(line, string)
    for letter in letters:
        if letter not in line:
            cond = False
            #total += 1
            #total_using_all += 0
        else:
            continue
    if cond == True:
        total += 1
        total_using_all += 1
    else:
        total += 1
        total_using_all += 0
            #total += 1
            #total_using_all += 1

final = total_using_all / total
print(f"There are {total_using_all} words that use all the letters in this string, or {final} of the total.")