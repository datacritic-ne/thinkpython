#! python3

#word = input("> ")
string = input("> ")

file1 = open('words.txt', 'r')
words = file1.readlines()

total = 0
total_not_forbidden = 0

def avoids(w, str):
    cond = True
    letters = list(str)
    for letter in letters:
        if letter in w:
            cond = False
        else:
            continue
    print(cond)
        
#avoids(word, string)

for word in words:
    line = word.strip()
    #avoids(line, string)
    letters = list(string)
    for letter in letters:
        if letter in line:
            total += 1
            total_not_forbidden += 0
        else:
            total += 1
            total_not_forbidden += 1

final = total_not_forbidden / total
print(f"The proportion of words without any forbidden letters: {final}")
        