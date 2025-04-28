#! python3

# Point the program to the words.txt file

file1 = open('words.txt', 'r')

# Loop through words in words.txt, print each word that's 20 or more characters long - load each word as a string and use len()

words = file1.readlines()

for word in words:
    line = word.strip()
    if len(line) > 20:
        print(line)
    else:
        continue