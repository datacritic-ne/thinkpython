#! python3

# Markov analysis
# Read a text file (don't process it?), and create a mapping between i-word prefixes and all suffixes that occur in the text
# Use the mapping to generate random text: randomly pick a prefix, randomly add a suffix to it, 
# create a new prefix from the suffix and the 2nd word of the prefix, and randomly choose a suffix, then repeat
# Experiment with prefixes longer than 2 words
# Edit the program to read in multiple books, and see what the mashup looks like

import random

# global variables

mapping = {}
prefix = {}

def map_text(words, pre):
    
    #for i in range(len(words)-pre):
        
    #    first = words[i] + ' '
    #    for j in range(len(pre)-1):
    #        next = words[i+j] + ' '
    #        next += next
        #pref = words[i] + ' ' + words[i+1] # can a for-loop extend this to more than 2-word prefixes?
    #    pref = first + next
    #    pref = pref.rstrip()
    #    suff = words[i+pre]
    #    mapping[pref] = suff

    global prefix
    if len(prefix) < pre:
        prefix += (words, )
        return
    
    try:
        mapping[prefix].append(words)
    except KeyError:
        mapping[prefix] = [words]

    prefix = shift(prefix, words)
    #random_text(mapping, 30)

def shift(t, words):
    return t[1:] + (words,)

def random_text(n):
    
    # need to create the histogram?
    # choose a random prefix (map.keys()) to start the string
    # choose a suffix from one of those associated with the prefix, append into 3-word string
    # new prefix = last_prefix[-1] + ' ' + suffix, then choose another suffix randomly
    # repeat length - 2 times
    #start = random.choice(map)
    
    start = random.choice(list(mapping.keys()))

    for i in range(n):
        suffixes = mapping.get(start, None)
        if suffixes == None:
            random_text(n-i)
            return
        
        word = random.choice(suffixes)
        print(word, end=' ')
        start = shift(start, word)

def process_file(file2):

    with open('new_file.txt', 'r+') as file1:

        file1.truncate()
        file1.close

    start_pattern = 'START OF THE PROJECT GUTENBERG EBOOK'
    end_pattern = 'END OF THE PROJECT GUTENBERG EBOOK'

    with open(file2, 'r') as f:
        for (i, line) in enumerate(f):
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
    
    file3 = open('new_file.txt', 'r')
    lines = file3.read()
    words = lines.split()

    map_text(words, 2)

process_file('gatsby.txt')