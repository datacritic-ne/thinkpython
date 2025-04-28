#! python3

def is_anagram(str1, str2):
    l1 = []
    for letter1 in str1:
        l1.append(letter1)
    l1.sort()
    
    l2 = []
    for letter2 in str2:
        l2.append(letter2)
    l2.sort()

    cond = True

    if len(l1) != len(l2):
        cond = False
    else:
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                cond = False
            else:
                continue

    print(cond)

string1 = 'louisfriend'
string2 = 'ironsulfide'
is_anagram(string1, string2)

string1 = 'jimmorrison'
string2 = 'mrmojorisin'
is_anagram(string1, string2)

string1 = 'anagram'
string2 = 'notananagram'
is_anagram(string1, string2)