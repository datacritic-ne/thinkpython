#! python3

file1 = open('words.txt', 'r')
data = file1.read()
words = data.split('\n')

words_dict = dict()
x = 1

for word in words:
    words_dict[word] = x
    x += 1

firstfive = dict(list(words_dict.items())[:5])
print(firstfive)