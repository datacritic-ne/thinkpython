#! python3

#file1 = open('words.txt', 'r')
#data = file1.read()
#words = data.split('\n')

#anagrams = {}

#for word in words:
#    w_index = words.pop(0)
#    l1 = list(w_index)
#    l1.sort()

#    for word in words:
#        l2 = list(word)
#        l2.sort()

#        if len(l1) != len(l2):
#            break
#        else:
#            for i in range(len(l1)):
#                if l1[i] != l2[i]:
#                    break
#                else:
#                    anagrams[w_index] = word
#    print(anagrams)
                    
#for i in anagrams:
#    metatheses = {}
#    metathesis = 0
#    w1 = list(anagrams[i][0])
#    w2 = list(anagrams[i][1])
#    for j in range(len(w1)):
#        if w1[j] != w2[j]:
#            metathesis += 1
#        else:
#            metathesis += 0
#    if metathesis == 2:
#        metatheses[i].append[w1, w2]
#    else:
#        continue

#print(metatheses)

# my code is above, and doesn't work. it gets the anagram dict wrong. below is the solution code

def signature(str):
    t = list(str)
    t.sort()
    t = ''.join(t)
    return t

def anagrams(filename):
    
    d = {}

    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)

    return d

def word_distance(word1, word2):

    assert len(word1) == len(word2)

    count = 0
    
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1
    return count

def metatheses(d):

    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_distance(word1, word2) == 2:
                    print(word1, word2)

sets = anagrams('words.txt')
metatheses(sets)