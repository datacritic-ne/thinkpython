#! python3

import string
#from collections import Counter

def missing_words(filename, wordlist):
    
    for line in open('words.txt'):
        word = line.strip().lower()
        t = list(word)
    
    with open('new_file.txt', 'r+') as file:

        file.truncate()
        file.close

    start_pattern = 'START OF THE PROJECT GUTENBERG EBOOK'
    end_pattern = 'END OF THE PROJECT GUTENBERG EBOOK'

    with open(filename, 'r') as file:
        for (i, line) in enumerate(file):
            if start_pattern in line:
                start_line = i + 2
            elif end_pattern in line:
                end_line = i
        
    infile = open(filename, 'r')
    outfile = open('new_file.txt', 'w')

    for i, line in enumerate(infile):
        if i < start_line:
            continue
        elif (i >= start_line) and (i < end_line):
            outfile.write(line)
        else:
            break
    
    file1 = open('new_file.txt', 'r')
    lines = file1.read()
    words = lines.split()

    words = [word.lower() for word in words]
    words = [word.translate(str.maketrans('', '', string.punctuation)) for word in words]

    for word in words:
        if word not in t:
            print(word)

missing_words('gatsby.txt', 'words.txt')