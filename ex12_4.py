#! python3

# use words.txt
# initialize an empty string, and add 'I' and 'a'
# how do I memoize the words known to be reducible?
# start with 2-letter words: for each word, drop letters one at a time and see if I or a are left, if so add them to the memo list
# for len(word) > 2, go to len = 3 first, drop letters one at a time and see if the remainder is in the memo list, if so add them to the memo list
# start this by finding the longest word in the list, so I can set up the above as a for loop

with open('words.txt', 'r') as filedata:

    word_list = filedata.read().split()
    longest_word = len(max(word_list, key=len))

    #print(longest_word) longest_word = 21

reducible = ['i', 'a']

#for line in open('words.txt'):
#    words = line.strip().lower()

file1 = open('words.txt', 'r')
data = file1.read()
words = data.split('\n')

for word in words:
    if len(word) == 2:
        for i in list(word):
            word_alt = word.replace(i, "", 1)
            if word_alt in ['i', 'a']:
                reducible.append(word)
            else:
                continue
    else:
        for j in range(3, longest_word):
            if len(word) == j:
                for k in list(word):
                    word_alt = word.replace(k, "", 1)
                    if word_alt in reducible:
                        reducible.append(word)
                    else:
                        continue

print(sorted(reducible, key=len))
    
# then handle words with len > 2