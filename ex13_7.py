#! python3

# This program creates a histogram of words from a text file, and chooses a random word from it
# Suggestion: 
# 1. Use .keys to get a list of words from the book
# 2. Use code from ex 10_2 to build a list of the cumulative sum of word frequencies (the last item equals the total number of words in the book)
# 3. Choose a random number from 1 to n (total number of words in the book), and use a bisection search (ex10_10) to find the index where it would be inserted into the cum sum
# 4. Use the index to find the corresponding word in the word list

#import random
#import string

#def random_word(filename):

    #for line in open('words.txt'):
    #    word = line.strip().lower()
    #    t = list(word)
    
    #with open('new_file.txt', 'r+') as file:

    #    file.truncate()
    #    file.close

    #start_pattern = 'START OF THE PROJECT GUTENBERG EBOOK'
    #end_pattern = 'END OF THE PROJECT GUTENBERG EBOOK'

    #with open(filename, 'r') as file:
    #    for (i, line) in enumerate(file):
    #        if start_pattern in line:
    #            start_line = i + 2
    #        elif end_pattern in line:
    #            end_line = i
        
    #infile = open(filename, 'r')
    #outfile = open('new_file.txt', 'w')

    #for i, line in enumerate(infile):
    #    if i < start_line:
    #        continue
    #    elif (i >= start_line) and (i < end_line):
    #        outfile.write(line)
    #    else:
    #        break
    
    # now the front and end material from Gutenberg should be stripped from the text

    #file1 = open('new_file.txt', 'r')
    #lines = file1.read()
    #words = lines.split()

    #words = [word.lower() for word in words]
    #words = [word.translate(str.maketrans('', '', string.punctuation)) for word in words]

    # we've converted the book to a list of words

# Code above is my attempt, code below is the author's solution
# 
import random
import string
from bisect import bisect
#from ex13_2 import novel

def random_word(hist):

    words = []
    freqs = []
    total_freq = 0

    # list of words and list of cumulative frequencies

    for word, freq in hist.items():
        total_freq += freq
        words.append(word)
        freqs.append(total_freq)

    # choose a random value and find its location in the cumulative list

    x = random.randint(0, total_freq-1)
    index = bisect(freqs, x)
    return words[index]

def main(filename):
    
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

    hist = {}

    for word in words:
        hist[word] = hist.get(word, 0) + 1

    print(f"Here are some random words from {filename}")
    for i in range(50):
        print(random_word(hist), end=' ')

main('gatsby.txt')
