#! python3

# Modify ex13_1.py to read The Great Gatsby
# Start reading after the header material (i.e., with line 24). BONUS: Also drop the end material (i.e., line 6432 forward).
# Then process using ex13_1.py.
# Count the total number of words in the book, and the number of times each word is used.
# Count the number of different words used in the book. Download a couple other books from gutenberg.org and compare different eras.

import string
import re
from collections import Counter

def novel(filename):

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

    return words

    #total_words = len(words)
    #print(f"There are {total_words} total words in {filename}.")

    #for i in words:
    #    count = words.count(i)
    #    if count > 0:
    #        pass
            #print(f"{i} occurs {count} times in {filename}.")

    #uniques = Counter(words).keys()
    #unique_count = len(uniques)
    #print(f"There are {unique_count} unique words in {filename}.")

#novel('gatsby.txt')

def compare_novels(file1, file2, file3):
    pass

    start_pattern = 'START OF THE PROJECT GUTENBERG EBOOK'
    end_pattern = 'END OF THE PROJECT GUTENBERG EBOOK'

    with open(file1, 'r') as file:
        for (i, line) in enumerate(file):
            if start_pattern in line:
                start_line = i + 2
            elif end_pattern in line:
                end_line = i
        
    infile = open(file1, 'r')
    outfile = open('new_file.txt', 'w')

    for i, line in enumerate(infile):
        if i < start_line:
            continue
        elif (i >= start_line) and (i < end_line):
            outfile.write(line)
        else:
            break

    file = open('new_file.txt', 'r')
    lines = file.read()
    words = lines.split()

    words = [word.lower() for word in words]
    words = [word.translate(str.maketrans('', '', string.punctuation)) for word in words]

    uniques = Counter(words).keys()
    unique_count = len(uniques)
    print(f"There are {unique_count} unique words in {file1}.")

    with open(file2, 'r') as file:
        for (i, line) in enumerate(file):
            if start_pattern in line:
                start_line = i + 2
            elif end_pattern in line:
                end_line = i
        
    infile = open(file2, 'r')
    outfile = open('new_file.txt', 'w')

    for i, line in enumerate(infile):
        if i < start_line:
            continue
        elif (i >= start_line) and (i < end_line):
            outfile.write(line)
        else:
            break

    file = open('new_file.txt', 'r')
    lines = file.read()
    words = lines.split()

    words = [word.lower() for word in words]
    words = [word.translate(str.maketrans('', '', string.punctuation)) for word in words]

    uniques = Counter(words).keys()
    unique_count = len(uniques)
    print(f"There are {unique_count} unique words in {file2}.")

    with open(file3, 'r') as file:
        for (i, line) in enumerate(file):
            if start_pattern in line:
                start_line = i + 2
            elif end_pattern in line:
                end_line = i
        
    infile = open(file3, 'r')
    outfile = open('new_file.txt', 'w')

    for i, line in enumerate(infile):
        if i < start_line:
            continue
        elif (i >= start_line) and (i < end_line):
            outfile.write(line)
        else:
            break

    file = open('new_file.txt', 'r')
    lines = file.read()
    words = lines.split()

    words = [word.lower() for word in words]
    words = [word.translate(str.maketrans('', '', string.punctuation)) for word in words]

    uniques = Counter(words).keys()
    unique_count = len(uniques)
    print(f"There are {unique_count} unique words in {file3}.")

#compare_novels('gatsby.txt', 'beowulf.txt', 'prince.txt')