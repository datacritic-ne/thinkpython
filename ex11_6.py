#! python3

file1 = open('words.txt', 'r')
data = file1.read()
words = data.split('\n')

for word in words:
    if len(word) == 5:
        word_a = word[1:]
        word_b = word[0]+word[2:]
        if ((word_a in words) and (word_b in words)):
            print(f"{word}, {word_a}, {word_b}")
        else:
            continue
    else:
        continue