#! python3

file1 = open('words.txt', 'r')
data = file1.read()
words = data.split('\n')

for word in words:
    a = "".join(reversed(word[::-3]))
    word_b = word[:-1]
    b = "".join(reversed(word_b[::-3]))
    word_c = word_b[:-1]
    c = "".join(reversed(word_c[::-3]))
    if ((a in words) and (b in words) and (c in words)):
        print(f"{word} = {c} and {b} and {a}")
    else:
        continue