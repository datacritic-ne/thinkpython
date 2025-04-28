#! python3

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import rankdata
from collections import Counter

def zipf(file):
    # calling this creates the data object and performs the analysis

    # need a dictionary where the key is the word and the value is the count
    # then need to sort by the values in descending order, and print each row of the sorted dictionary
    # then another dictionary where the key is the count and the value is the rank
    # then take the logs of each key and each value in that dictionary
    # then plot them
    
    count = Counter(file)
    #print(count)

    rank = dict(zip(count.keys(), rankdata([-i for i in count.values()], method='min')))

    merged = dict(list(count.items()) + 
                  [(key, [count[key], rank[key]]) if key in rank else (key, count[key]) for key in count] +
                  [(key, rank[key]) for key in rank if key not in count])

    dataframe = list(merged.values())
    
    freqlist, ranklist = zip(*dataframe)
    
    logfreq = list(np.log(freqlist))
    logrank = list(np.log(ranklist))

    plt.scatter(logrank, logfreq)
    plt.title('Plot of Zipf\'s Law using the Great Gatsby')
    plt.ylabel('Log of Word Frequency')
    plt.xlabel('Log of Frequency Rank')
    plt.show()


def process_file(filename):
    # this removes the header and footer from the text file, and turns the file into a list of words
    
    with open('new_file.txt', 'r+') as file1:

        file1.truncate()
        file1.close

    start_pattern = 'START OF THE PROJECT GUTENBERG EBOOK'
    end_pattern = 'END OF THE PROJECT GUTENBERG EBOOK'

    with open(filename, 'r') as f:
        for (i, line) in enumerate(f):
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
    
    file3 = open('new_file.txt', 'r')
    lines = file3.read()
    words = lines.split()

    zipf(words)

process_file('gatsby.txt')