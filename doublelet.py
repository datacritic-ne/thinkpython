#! python3

file1 = open('words.txt', 'r')
words = file1.readlines()

for word in words:
    line = word.strip()
    letters = list(line)
    if len(line) >= 6:
        for i in range(5, len(letters)):
            if ((letters[i] == letters [i-1]) and (letters[i-3] == letters[i-2]) and (letters[i-5] == letters[i-4])):
                print(line)
            else:
                continue
    else:
        continue
