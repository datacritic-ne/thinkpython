#! python3

file1 = open('words.txt', 'r')
data = file1.read()
words = data.split('\n')

for word in words:
    rev_word = "".join(reversed(word))
    if rev_word in words:
        print(f"{word}, {rev_word}")
    else:
        continue
