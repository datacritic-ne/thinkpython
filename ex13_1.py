#! python3

import string

# string.translate(str.maketrans('', '', string.punctuation)) should remove punctuation
# str.replace(" ", "") should remove all whitespace
# str.lower() should make everything lower-case

def format_file(filename):
    
    file1 = open(filename, 'r')
    data = file1.read()
    words = data.split()
    
    #data = data.lower()
    #data = data.replace(" ", "")
    #data = data.translate(str.maketrans('', '', string.punctuation))
    #data = data.split()

    #for word in words:
    
    #words    word.replace(" ", "")
    words = [word.lower() for word in words]
    words = [word.translate(str.maketrans('', '', string.punctuation)) for word in words]

    print(words)

format_file('ex13_1.txt')