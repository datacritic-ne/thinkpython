#! python3

# open the words.txt file
# split the file in half
# iterate over the first half and look for the keyword
# if the keyword is there, kick in True criterion, print a message, and exit the loop
# if the keyword is not there, go to the second half of the word list, and recurse in_bisect

file1 = open('words.txt', 'r')
data = file1.read()
words = data.split('\n')

def in_bisect(key, words):
    try:
        x = int(0.5 * len(words))
        w_sub = words[:x]
        if key in w_sub:
            print(f"{key} is in words.txt! Yay!")
            return
        elif key not in w_sub:
            w_sub_next = words[x+1:]
            in_bisect(key, w_sub_next)
    except RecursionError:
        #print(f"{key} is not in words.txt. Bummer.")
        return

keyword = input("> ")
in_bisect(keyword, words)