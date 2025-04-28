#! python3

#file1 = open('words.txt', 'r')
#data = file1.read()
#words = data.split('\n')

# loop - pop 1st element in words list, letters = list(word), compare remaining words in words list as anagrams

#for word in words:
anagrams = {}

for line in open('words.txt'):
    word = line.strip().lower()
    t = list(word)
    t.sort()
    t = ''.join(t)

    if t not in anagrams:
        anagrams[t] = [word]
    else:
        anagrams[t].append(word)

for v in anagrams.values():
    if len(v) > 1:
        print(len(v), v)

w = []
for x in anagrams.values():
    if len(x) > 1:
        w.append((len(x), x))
w.sort(reverse=True)
for y in w:
    print(y)

res = {}
for word, anagram in anagrams.items():
    if len(word) == 8:
        res[word]  = anagram
t = []
for x in res.values():
    if len(x) > 1:
        t.append((len(x), x))
t.sort(reverse=True)
for u in t:
    print(u)