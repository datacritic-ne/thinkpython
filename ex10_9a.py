#! python3

import random

file1 = open('words.txt', 'r')
words = file1.readlines()
x = []

for word in words:
    line = word.strip()
    letters = list(line)
    #x = []
    w = random.choice(letters)
    x.append(w)
print(x[:10])