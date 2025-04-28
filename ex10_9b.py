#! python3

import random

file1 = open('words.txt', 'r')
words = file1.readlines()
t = []

for word in words:
    line = word.strip()
    letters = list(line)
    #t = []
    x = random.choice(letters)
    t = t + [x]
print(t[:10])